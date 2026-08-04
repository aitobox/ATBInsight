import os
import datetime
from src.config import load_config
from src.db import init_db, is_entry_processed, mark_entry
from src.robots.miniflux_robot import fetch_miniflux_entries
from src.robots.llm_robot import score_article, refine_markdown
from src.robots.image_robot import localize_images


def run_pipeline(
    config_path: str = "etc/ai_insight_pipeline.yaml",
    db_path: str = "var/db/pipeline_cache.db",
    output_dir: str = "docs/insight",
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
    days = miniflux_cfg.get("days", 7)

    entries = fetch_miniflux_entries(
        url=url,
        username=username,
        password=password,
        days=days,
    )

    date_str = datetime.date.today().strftime("%Y-%m-%d")
    target_dir = os.path.join(output_dir, date_str)

    try:
        for entry in entries:
            entry_id = str(entry.get("id"))
            if is_entry_processed(conn, entry_id):
                continue

            score = score_article(entry)
            if score < 30.0:
                mark_entry(
                    conn,
                    entry_id,
                    entry.get("title", ""),
                    entry.get("url", ""),
                    score,
                    "skipped",
                )
                continue

            refined_md = refine_markdown(entry)
            localized_md = localize_images(refined_md, target_dir, conn)

            os.makedirs(target_dir, exist_ok=True)
            slug = f"article_{entry_id}.md"
            filepath = os.path.join(target_dir, slug)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(localized_md)

            mark_entry(
                conn,
                entry_id,
                entry.get("title", ""),
                entry.get("url", ""),
                score,
                "processed",
                filepath,
            )
    finally:
        conn.close()


if __name__ == "__main__":
    run_pipeline()
