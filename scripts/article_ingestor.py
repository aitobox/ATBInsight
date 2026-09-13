import argparse
import logging
import os
import sqlite3
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


import re
import requests
from bs4 import BeautifulSoup

def fetch_full_article_content(url: str) -> str:
    """
    Fetches the web page from the original URL and extracts the main article content
    when the RSS feed content is truncated or incomplete.
    """
    if not url or not url.startswith("http"):
        return ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, "html.parser")

        for tag in soup(["script", "style", "nav", "footer", "header", "aside", "iframe", "noscript", "svg", "button", "form"]):
            tag.decompose()

        container = (
            soup.find("article")
            or soup.find("main")
            or soup.find(attrs={"role": "main"})
            or soup.find("div", class_=re.compile(r"post-content|article-content|entry-content|main-content|post-body|article-body|content-body", re.I))
            or soup.find("div", id=re.compile(r"content|main|article|post", re.I))
            or soup.find("body")
        )

        if container:
            return str(container)
        return str(soup)
    except Exception as e:
        logger.warning(f"Failed to fetch full article content from {url}: {e}")
        return ""


def is_arxiv_entry(entry: dict) -> bool:
    """
    Detects whether an entry originates from arXiv based on url, title or content.
    """
    url = (entry.get("url") or "").lower()
    title = (entry.get("title") or "").lower()
    content = (entry.get("content") or "").lower()
    return "arxiv.org" in url or "arxiv" in url or "arxiv" in title or "arxiv:" in content[:1000]


def get_processed_arxiv_count(conn: sqlite3.Connection, target_dir: str) -> int:
    """
    Counts how many arXiv entries have already been processed for the target directory/date.
    """
    cur = conn.cursor()
    dir_pattern = f"%{target_dir}%"
    date_pattern = f"%{os.path.basename(target_dir)}%"
    cur.execute(
        """
        SELECT count(*) FROM processed_entries 
        WHERE status = 'processed' 
          AND (output_path LIKE ? OR output_path LIKE ?)
          AND (url LIKE '%arxiv.org%' OR url LIKE '%arxiv%' OR title LIKE '%arxiv%')
        """,
        (dir_pattern, date_pattern),
    )
    row = cur.fetchone()
    return row[0] if row else 0


def evaluate_entry(entry: dict, db_path: str, threshold: float = 70.0) -> tuple[str, float, dict, str]:
    """
    Evaluates an article entry using parallel Chief Editor Agent subprocess (agy run/llm).
    Returns (status, score, entry, message).
    Status is one of: 'cached', 'skipped', 'qualified'.
    """
    conn = init_db(db_path)
    entry_id = str(entry.get("id"))
    title = entry.get("title", "Untitled")

    try:
        if is_entry_processed(conn, entry_id):
            return ("cached", 0.0, entry, "Already cached")

        url = entry.get("url") or ""
        raw_content = entry.get("content") or ""

        if url and (len(raw_content) < 3000 or "continue reading" in raw_content.lower() or "read more" in raw_content.lower()):
            logger.info(f"Entry ID {entry_id}: RSS content is short/incomplete ({len(raw_content)} chars). Fetching full content from original URL...")
            full_content = fetch_full_article_content(url)
            if len(full_content) > len(raw_content):
                logger.info(f"  -> Successfully expanded content to {len(full_content)} chars from original URL.")
                entry["content"] = full_content

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
            return ("skipped", score, entry, "Score below threshold")

        return ("qualified", score, entry, "Score meets threshold")
    finally:
        conn.close()


def materialize_entry(entry: dict, score: float, target_dir: str, db_path: str) -> tuple[str, float, str]:
    """
    Downloads/localizes images, refines markdown, saves the article to target_dir and marks it processed in DB.
    Returns (status, score, filepath).
    """
    conn = init_db(db_path)
    entry_id = str(entry.get("id"))
    title = entry.get("title", "Untitled")

    try:
        logger.info(f"Localizing images for approved entry ID {entry_id} ('{title}')...")
        raw_content = entry.get("content") or ""
        localized_raw_md = localize_images(raw_content, target_dir, conn)

        entry_copy = dict(entry)
        entry_copy["content"] = localized_raw_md

        logger.info(f"Refining article content via LLM for entry ID {entry_id}...")
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
        logger.info(f"Successfully saved screened article to '{filepath}'.")
        return ("processed", score, filepath)
    finally:
        conn.close()


def process_single_entry(entry: dict, target_dir: str, db_path: str, threshold: float = 70.0) -> tuple[str, float, str]:
    """
    Evaluates and materializes an article entry.
    Maintained for backward compatibility and single-entry invocations.
    Returns (status, score, filepath/reason).
    """
    status, score, eval_entry, msg = evaluate_entry(entry, db_path, threshold)
    if status == "qualified":
        return materialize_entry(eval_entry, score, target_dir, db_path)
    return (status, score, msg)


def run_pipeline(
    config_path: str = "etc/ai_insight_pipeline.yaml",
    db_path: str = "var/db/pipeline_cache.db",
    output_dir: str = "bak/origin",
    target_date: str | None = None,
    override_days: int | None = None,
    max_workers: int = 5,
    threshold: float = 70.0,
    max_arxiv: int = 3,
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

    logger.info(f"Starting AI Insight Pipeline execution (days={days}, target_date={target_date}, max_workers={max_workers}, threshold={threshold}, max_arxiv={max_arxiv}).")
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
        logger.info(f"Phase 1.1: Launching {max_workers} parallel Chief Editor Agents for article evaluation (threshold: {threshold})...")
        qualified_entries: list[tuple[dict, float]] = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [
                executor.submit(evaluate_entry, entry, db_path, threshold)
                for entry in uncached_entries
            ]
            for future in as_completed(futures):
                try:
                    status, score, eval_entry, msg = future.result()
                    if status == "qualified":
                        qualified_entries.append((eval_entry, score))
                    elif status == "skipped":
                        skipped_count += 1
                    elif status == "cached":
                        cached_count += 1
                except Exception as exc:
                    logger.error(f"Worker generated an exception during evaluation: {exc}")

        # Phase 1.2: Enforce daily quota for arXiv papers (Top N by score)
        non_arxiv_qualified = [(e, s) for e, s in qualified_entries if not is_arxiv_entry(e)]
        arxiv_qualified = [(e, s) for e, s in qualified_entries if is_arxiv_entry(e)]

        conn = init_db(db_path)
        already_processed_arxiv = get_processed_arxiv_count(conn, target_dir)
        conn.close()

        remaining_arxiv_quota = max(0, max_arxiv - already_processed_arxiv)
        logger.info(
            f"Phase 1.2: Qualified entries: {len(qualified_entries)} (Non-arXiv: {len(non_arxiv_qualified)}, arXiv: {len(arxiv_qualified)}). "
            f"Daily arXiv quota: {max_arxiv}, already processed today: {already_processed_arxiv}, remaining quota: {remaining_arxiv_quota}."
        )

        # Sort arXiv papers descending by score and pick top N
        arxiv_qualified.sort(key=lambda item: item[1], reverse=True)
        approved_arxiv = arxiv_qualified[:remaining_arxiv_quota]
        exceeded_arxiv = arxiv_qualified[remaining_arxiv_quota:]

        if exceeded_arxiv:
            conn = init_db(db_path)
            for entry, score in exceeded_arxiv:
                entry_id = str(entry.get("id"))
                title = entry.get("title", "Untitled")
                url = entry.get("url", "")
                mark_entry(conn, entry_id, title, url, score, "skipped")
                logger.info(f"  -> arXiv Entry ID {entry_id} ('{title}') [Score: {score:.1f}] skipped: Exceeded daily arXiv quota of {max_arxiv} papers.")
                skipped_count += 1
            conn.close()

        approved_entries = non_arxiv_qualified + approved_arxiv
        logger.info(f"Phase 1.3: Materializing {len(approved_entries)} approved articles ({len(non_arxiv_qualified)} Non-arXiv, {len(approved_arxiv)} Top arXiv)...")

        if approved_entries:
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = [
                    executor.submit(materialize_entry, entry, score, target_dir, db_path)
                    for entry, score in approved_entries
                ]
                for future in as_completed(futures):
                    try:
                        status, score, filepath = future.result()
                        if status == "processed":
                            processed_count += 1
                    except Exception as exc:
                        logger.error(f"Worker generated an exception during materialization: {exc}")

    logger.info(
        f"Pipeline run complete. "
        f"Processed: {processed_count}, Skipped (Low Quality / Quota Exceeded): {skipped_count}, Cached (Previously Handled): {cached_count}."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Insight Pipeline Runner")
    parser.add_argument("--date", type=str, help="Specific target date to fetch and process (format: YYYY-MM-DD)")
    parser.add_argument("--days", type=int, help="Number of past days to fetch entries for (e.g. 7)")
    parser.add_argument("--workers", type=int, default=5, help="Number of parallel Chief Editor agent workers")
    parser.add_argument("--threshold", type=float, default=70.0, help="Minimum score threshold to accept article (default: 70.0)")
    parser.add_argument("--max-arxiv", type=int, default=3, help="Maximum number of arXiv papers to accept per day (default: 3)")
    args = parser.parse_args()

    run_pipeline(
        target_date=args.date,
        override_days=args.days,
        max_workers=args.workers,
        threshold=args.threshold,
        max_arxiv=args.max_arxiv,
    )

