---
name: daily-publisher
description: Automates the complete daily publishing pipeline: RSS ingestion, Chief Editor screening, translation, categorization, site compilation, GitHub Pages deployment, and Git main branch syncing.
---

# Daily Publisher Orchestrator

You are the orchestration agent for ATBInsight's daily publishing pipeline. Your job is to execute the following three phases sequentially and fully autonomously. Do not stop to ask the user for permission between phases unless an unrecoverable error occurs.

## Phase 1: Ingestion & Screening
Run the daily ingestor script. This script uses the Chief Editor persona to screen for high-quality, non-political long-form technical articles.
**Command:** `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && PYTHONPATH=. python scripts/article_ingestor.py --days 1"`
Wait for this to complete. Screened raw markdown files will be saved into `bak/origin/YYYY-MM-DD` (where YYYY-MM-DD is today's date).

## Phase 2: Translation & Categorization
Check the `bak/origin/YYYY-MM-DD` directory for new `.md` files.
If files exist, you must translate them using the `tech-article-translator` skill. 
Since there may be multiple files, **dispatch parallel subagents** (using your `invoke_subagent` tool) for each file or small batches of files, instructing them to:
1. Act under the `tech-article-translator` skill rules.
2. Read their assigned file from `bak/origin/YYYY-MM-DD/`.
3. Add standard YAML Front Matter headers. **CRITICAL**: The `categories` field MUST be selected from the 5 standard site categories: `[产品发布, 工具教程, 研究解读, 商业动态, 其他]` based on article content (DO NOT hardcode single categories).
4. Add a Chinese background and summary block (`### 文章背景与核心概要`).
5. Format text paragraphs into Chinese translation accompanied by original English quote blocks (`>`).
6. Save the translated file to `docs/blog/posts/` with the filename format: `YYYY-MM-DD-Chinese_Title.md`.
7. Keep original source files in `bak/origin/YYYY-MM-DD/` intact.

Wait for all translator subagents to report completion before proceeding to Phase 3.

## Phase 3: Build, Indexing & Deploy
Once translation is complete, update all site indices, rebuild the static site, deploy to GitHub Pages, and sync the `main` branch to Git.
Execute the following commands sequentially:

1. **Generate chronological archive**:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python scripts/generate_archive.py"`
2. **Update daily headlines & homepage link**:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python scripts/update_daily_headlines.py"`
   *(Ensures `[博客动态区]` on homepage points to `archive.md`)*
3. **Auto-classify posts into standard categories**:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && PYTHONPATH=. python scripts/auto_classify.py"`
   *(Ensures all posts strictly belong to one of `[产品发布, 工具教程, 研究解读, 商业动态, 其他]`)*
4. **Generate category index pages and tags page**:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python scripts/generate_indexes.py"`
   *(Cleans old category pages and regenerates `docs/tags.md` & `docs/blog/category/*.md`)*
5. **Build the static site**:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && zensical build"`
6. **Deploy to GitHub Pages**:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && ghp-import -p -b gh-pages site"`
7. **Commit & push main branch changes to Git**:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && git add . && git commit -m 'docs: update daily posts, indexes and site content' && git push origin main"`

Report the final success status and provide a link to the live site to the user.
