---
name: daily-publisher
description: Automates the daily publishing pipeline: ingestion, translation, and deployment.
---

# Daily Publisher Orchestrator

You are the orchestration agent for ATBInsight's daily publishing pipeline. Your job is to execute the following three phases sequentially and fully autonomously. Do not stop to ask the user for permission between phases unless an unrecoverable error occurs.

## Phase 1: Ingestion & Screening
Run the daily ingestor script. This script automatically uses the Chief Editor skill to screen for high-quality articles.
**Command:** `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python scripts/article_ingestor.py"`
Wait for this to complete. It will save the screened markdown files into `bak/origin/YYYY-MM-DD` (where YYYY-MM-DD is today's date).

## Phase 2: Translation & Categorization
Check the `bak/origin/YYYY-MM-DD` directory for new `.md` files.
If files exist, you must translate them using the `tech-article-translator` skill. 
Since there may be multiple files, **dispatch parallel subagents** (using your `invoke_subagent` tool) for each file or small batches of files, instructing them to:
1. Act under the `tech-article-translator` skill.
2. Read their assigned file from `bak/origin/YYYY-MM-DD/`.
3. Translate the content, extract a suitable category, and add relevant tags.
4. Add the standard YAML frontmatter.
5. Save the translated file to `docs/blog/posts/` with a renamed title format: `YYYY-MM-DD-Chinese_Title.md`.

Wait for all translator subagents to report completion before proceeding to Phase 3.

## Phase 3: Build & Deploy
Once translation is complete, you must update indices, build the site, and deploy.
Execute the following commands sequentially:

1. Generate chronological archive:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python scripts/generate_archive.py"`
2. Update daily headlines:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python scripts/update_daily_headlines.py"`
3. Auto-classify posts into standard categories:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && PYTHONPATH=. python scripts/auto_classify.py"`
4. Generate categories and tags pages:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python scripts/generate_indexes.py"`
5. Build the site:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && zensical build"`
6. Deploy to GitHub Pages:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && ghp-import -p -b gh-pages site"`
7. Commit and push main branch changes to git:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && git add . && git commit -m 'docs: update daily posts, indexes and site content' && git push origin main"`

Report the final success status and provide a link to the live site to the user.
