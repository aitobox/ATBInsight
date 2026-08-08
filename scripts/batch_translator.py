import os
import re
import glob
import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.robots.llm_robot import _chat_completion_with_fallback

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s - %(message)s")
logger = logging.getLogger("batch_translator")


def translate_article_file(filepath: str, output_dir: str = "docs/blog/posts") -> str:
    filename = os.path.basename(filepath)
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", filepath)
    date_str = date_match.group(1) if date_match else "2026-08-07"

    with open(filepath, "r", encoding="utf-8") as f:
        raw_md = f.read()

    # Check if already translated by checking if any file in output_dir starts with date_str and contains similar key or if we already have it
    # We will generate a Chinese title and check if target file exists
    system_prompt = (
        "You are an expert technical translator for ATBInsight.\n"
        "Your task is to translate an English technical article into Chinese according to strict specifications:\n\n"
        "1. FRONTMATTER:\n"
        "Create YAML frontmatter:\n"
        "---\n"
        "title: \"<Chinese Translated Title>\"\n"
        f"date: {date_str}\n"
        "authors: [aitoboxrobot]\n"
        "categories: [select exactly 1 from: 产品发布, 工具教程, 研究解读, 商业动态, 其他]\n"
        "tags: [<3-5 relevant tags>]\n"
        "---\n\n"
        "2. BACKGROUND & SUMMARY BLOCK:\n"
        "Add a section:\n"
        "### 文章背景与核心概要\n"
        "<Concise 2-3 paragraph Chinese summary of background, technical core, and significance>\n\n"
        "3. BILINGUAL TEXT FORMATTING:\n"
        "- Format each section and paragraph with Chinese translation FIRST, followed by the original English paragraph in a quote block (`> ...`).\n"
        "- Preserve all code blocks, inline code, links, and markdown images (`![...](./images/...)` or `![...](https://...)`) EXACTLY as they appear without modification.\n"
        "- Ensure clean markdown formatting.\n"
    )

    user_prompt = f"Original Article:\n{raw_md}"

    try:
        translated_md = _chat_completion_with_fallback(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
            timeout=90,
        )

        # Extract Chinese title from frontmatter
        title_match = re.search(r'title:\s*"([^"]+)"', translated_md) or re.search(r"title:\s*'([^']+)'", translated_md) or re.search(r"title:\s*(.+)$", translated_md, re.MULTILINE)
        if title_match:
            ch_title = title_match.group(1).strip()
            # Clean title for YAML frontmatter if it contains invalid escape characters or quotes
            clean_yaml_title = ch_title.replace("\\", "").replace('"', "'")
            translated_md = re.sub(r'title:\s*".*?"', f'title: "{clean_yaml_title}"', translated_md, count=1)
            
            # Clean title for filename (remove special chars $, !, (, ), :, ?, etc.)
            ch_title = re.sub(r'[\$\\()!:"\'\?\/\%\*]', '-', ch_title).strip('-')
            ch_title = re.sub(r'-+', '-', ch_title)
        else:
            ch_title = f"article_{os.path.splitext(filename)[0]}"

        out_filename = f"{date_str}-{ch_title}.md"
        out_filepath = os.path.join(output_dir, out_filename)

        os.makedirs(output_dir, exist_ok=True)
        with open(out_filepath, "w", encoding="utf-8") as f:
            f.write(translated_md)

        logger.info(f"Successfully translated '{filename}' -> '{out_filepath}'")
        return out_filepath
    except Exception as e:
        logger.error(f"Failed to translate '{filename}': {e}")
        return ""


def run_batch_translation(origin_dir: str = "bak/origin/2026-08-07", max_workers: int = 5):
    files = glob.glob(os.path.join(origin_dir, "*.md"))
    logger.info(f"Found {len(files)} articles in {origin_dir} to process.")

    os.makedirs("docs/blog/posts", exist_ok=True)
    existing_posts = os.listdir("docs/blog/posts")

    todo_files = []
    for f in files:
        # Check if file has already been translated by checking origin file content/title
        todo_files.append(f)

    logger.info(f"Starting batch translation of {len(todo_files)} files with {max_workers} threads...")

    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(translate_article_file, f): f for f in todo_files}
        for future in as_completed(futures):
            res = future.result()
            if res:
                results.append(res)

    logger.info(f"Batch translation complete. Successfully generated {len(results)} translated articles.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default="bak/origin/2026-08-07")
    parser.add_argument("--workers", type=int, default=5)
    args = parser.parse_args()

    run_batch_translation(origin_dir=args.dir, max_workers=args.workers)
