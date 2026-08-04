import argparse
import logging
import os
import datetime
import yaml
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


def run_pipeline(
    config_path: str = "etc/ai_insight_pipeline.yaml",
    db_path: str = "var/db/pipeline_cache.db",
    output_dir: str = "docs/blog/posts",
    target_date: str | None = None,
    override_days: int | None = None,
):
    cfg = {}
    if os.path.exists(config_path):
        cfg = load_config(config_path)
    conn = init_db(db_path)

    steps = cfg.get("steps", [])
    miniflux_cfg = steps[0]["config"] if steps and isinstance(steps[0], dict) and "config" in steps[0] else {}

    url = os.getenv("MINIFLUX_URL") or miniflux_cfg.get("url") or ""
    username = os.getenv("MINIFLUX_USERNAME") or miniflux_cfg.get("username") or ""
    password = os.getenv("MINIFLUX_PASSWORD") or miniflux_cfg.get("password") or ""
    days = override_days if override_days is not None else miniflux_cfg.get("days", 7)

    logger.info(f"Starting AI Insight Pipeline execution (days={days}, target_date={target_date}).")
    entries = fetch_miniflux_entries(
        url=url,
        username=username,
        password=password,
        days=days,
        target_date=target_date,
    )

    date_str = target_date if target_date else datetime.date.today().strftime("%Y-%m-%d")
    target_dir = output_dir

    if not entries:
        logger.info("No entries to process.")
        return

    processed_count = 0
    skipped_count = 0
    cached_count = 0

    try:
        for idx, entry in enumerate(entries, 1):
            entry_id = str(entry.get("id"))
            title = entry.get("title", "Untitled")
            logger.info(f"[{idx}/{len(entries)}] Processing entry ID {entry_id}: '{title}'")

            if is_entry_processed(conn, entry_id):
                logger.info(f"  -> Entry ID {entry_id} already in cache (processed or skipped). Skipping.")
                cached_count += 1
                continue

            score = score_article(entry)
            logger.info(f"  -> LLM Quality Score: {score:.1f}/100.0 (Threshold: 30.0)")

            if score < 30.0:
                logger.info("  -> Score below threshold. Marking as skipped in cache.")
                mark_entry(
                    conn,
                    entry_id,
                    title,
                    entry.get("url", ""),
                    score,
                    "skipped",
                )
                skipped_count += 1
                continue

            logger.info("  -> Refining article content via LLM...")
            refined_md = refine_markdown(entry)
            
            logger.info("  -> Localizing images and replacing links...")
            localized_md = localize_images(refined_md, target_dir, conn)

            os.makedirs(target_dir, exist_ok=True)
            
            front_matter = {
                "title": title,
                "date": date_str,
                "authors": ["aitoboxrobot"],
                "categories": ["深度研报"],
                "tags": ["AI", "科技解构"],
            }
            fm_str = yaml.dump(front_matter, allow_unicode=True, sort_keys=False)
            post_content = f"---\n{fm_str}---\n\n{localized_md}"

            safe_title = title.replace("/", "_").replace("\\", "_")
            slug = f"{date_str}-{safe_title}.md"
            filepath = os.path.join(target_dir, slug)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(post_content)

            mark_entry(
                conn,
                entry_id,
                title,
                entry.get("url", ""),
                score,
                "processed",
                filepath,
            )
            logger.info(f"  -> Saved refined article to '{filepath}'.")
            processed_count += 1
    finally:
        conn.close()

    logger.info(
        f"Pipeline run complete. "
        f"Processed: {processed_count}, Skipped (Low Quality): {skipped_count}, Cached (Previously Handled): {cached_count}."
    )



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Insight Pipeline Runner")
    parser.add_argument("--date", type=str, help="Specific target date to fetch and process (format: YYYY-MM-DD)")
    parser.add_argument("--days", type=int, help="Number of past days to fetch entries for (e.g. 7)")
    args = parser.parse_args()

    run_pipeline(target_date=args.date, override_days=args.days)


