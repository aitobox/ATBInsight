import argparse
import logging
import os
import datetime
import yaml
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.config import load_config
from src.db import init_db, is_entry_processed, mark_entry
from src.robots.miniflux_robot import fetch_miniflux_entries
from src.robots.llm_robot import score_article, refine_markdown
from src.robots.image_robot import localize_images

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
logger = logging.getLogger("ai_insight")


def process_single_entry(entry: dict, target_dir: str, db_path: str, threshold: float = 60.0) -> tuple[str, float, str]:
    """
    Evaluates an article entry using parallel Chief Editor Agent subprocess (agy run).
    Returns (status, score, filepath/reason).
    """
    # Open individual DB connection for thread safety
    conn = init_db(db_path)
    entry_id = str(entry.get("id"))
    title = entry.get("title", "Untitled")

    try:
        if is_entry_processed(conn, entry_id):
            return ("cached", 0.0, "Already cached")

        logger.info(f"Evaluating entry ID {entry_id} ('{title}') via Chief Editor Agent...")
        score = score_article(entry)
        logger.info(f"  -> Entry ID {entry_id} Score: {score:.1f}/100.0 (Threshold: {threshold:.1f})")

        if score < threshold:
            mark_entry(
                conn,
                entry_id,
                title,
                entry.get("url", ""),
                score,
                "skipped",
            )
            return ("skipped", score, "Score below threshold")

        logger.info(f"  -> Score {score:.1f} >= {threshold:.1f}. Localizing images for entry ID {entry_id}...")
        raw_content = entry.get("content") or ""
        localized_raw_md = localize_images(raw_content, target_dir, conn)

        entry_copy = dict(entry)
        entry_copy["content"] = localized_raw_md

        logger.info(f"  -> Refining article content via LLM...")
        refined_md = refine_markdown(entry_copy)

        os.makedirs(target_dir, exist_ok=True)
        filepath = os.path.join(target_dir, f"article_{entry_id}.md")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(refined_md)

        mark_entry(
            conn,
            entry_id,
            title,
            entry.get("url", ""),
            score,
            "processed",
            filepath,
        )
        logger.info(f"  -> Successfully saved screened article to '{filepath}'.")
        return ("processed", score, filepath)
    finally:
        conn.close()


def run_pipeline(
    config_path: str = "etc/ai_insight_pipeline.yaml",
    db_path: str = "var/db/pipeline_cache.db",
    output_dir: str = "bak/origin",
    target_date: str | None = None,
    override_days: int | None = None,
    max_workers: int = 5,
):
    cfg = {}
    if os.path.exists(config_path):
        cfg = load_config(config_path)

    steps = cfg.get("steps", [])
    miniflux_cfg = steps[0]["config"] if steps and isinstance(steps[0], dict) and "config" in steps[0] else {}

    url = os.getenv("MINIFLUX_URL") or miniflux_cfg.get("url") or ""
    username = os.getenv("MINIFLUX_USERNAME") or miniflux_cfg.get("username") or ""
    password = os.getenv("MINIFLUX_PASSWORD") or miniflux_cfg.get("password") or ""
    days = override_days if override_days is not None else miniflux_cfg.get("days", 7)

    logger.info(f"Starting AI Insight Pipeline execution (days={days}, target_date={target_date}, max_workers={max_workers}).")
    entries = fetch_miniflux_entries(
        url=url,
        username=username,
        password=password,
        days=days,
        target_date=target_date,
    )

    date_str = target_date if target_date else datetime.date.today().strftime("%Y-%m-%d")
    target_dir = os.path.join(output_dir, date_str)

    if not entries:
        logger.info("No entries to process.")
        return

    # Check cache state first
    conn = init_db(db_path)
    uncached_entries = []
    cached_count = 0
    for entry in entries:
        if is_entry_processed(conn, str(entry.get("id"))):
            cached_count += 1
        else:
            uncached_entries.append(entry)
    conn.close()

    logger.info(f"Total entries: {len(entries)}. Cached: {cached_count}. Uncached for Chief Editor screening: {len(uncached_entries)}.")

    processed_count = 0
    skipped_count = 0

    if uncached_entries:
        logger.info(f"Launching {max_workers} parallel Chief Editor Agents for parallel article evaluation...")
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [
                executor.submit(process_single_entry, entry, target_dir, db_path, 60.0)
                for entry in uncached_entries
            ]
            for future in as_completed(futures):
                try:
                    status, score, msg = future.result()
                    if status == "processed":
                        processed_count += 1
                    elif status == "skipped":
                        skipped_count += 1
                    elif status == "cached":
                        cached_count += 1
                except Exception as exc:
                    logger.error(f"Worker generated an exception: {exc}")

    logger.info(
        f"Pipeline run complete. "
        f"Processed: {processed_count}, Skipped (Low Quality): {skipped_count}, Cached (Previously Handled): {cached_count}."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Insight Pipeline Runner")
    parser.add_argument("--date", type=str, help="Specific target date to fetch and process (format: YYYY-MM-DD)")
    parser.add_argument("--days", type=int, help="Number of past days to fetch entries for (e.g. 7)")
    parser.add_argument("--workers", type=int, default=5, help="Number of parallel Chief Editor agent workers")
    args = parser.parse_args()

    run_pipeline(target_date=args.date, override_days=args.days, max_workers=args.workers)
