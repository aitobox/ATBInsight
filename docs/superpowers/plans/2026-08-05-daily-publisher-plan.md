# Daily Publisher Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a daily publisher skill that orchestrates the entire site generation pipeline from ingestion to deployment.

**Architecture:** We will create a native Antigravity skill (`skills/daily-publisher/SKILL.md`) that guides an agent through a three-step orchestration process: running the ingestor (which uses the Chief Editor screener), dispatching parallel translator subagents, and executing build/deployment scripts.

**Tech Stack:** Markdown, Bash, Antigravity Agent tools

## Global Constraints

- The skill must instruct the agent to look for files in `bak/origin/{DATE}`.
- The skill must instruct the agent to deploy using `zensical build` and `ghp-import`.
- All Python code uses TDD (we will test that the skill file contains the right instructions).

---

### Task 1: Create Daily Publisher Skill

**Files:**
- Create: `skills/daily-publisher/SKILL.md`
- Create: `tests/test_daily_publisher_skill.py`

**Interfaces:**
- Consumes: None
- Produces: `skills/daily-publisher/SKILL.md`

- [ ] **Step 1: Write the failing test**

```python
import os

def test_daily_publisher_skill_exists():
    path = "skills/daily-publisher/SKILL.md"
    assert os.path.exists(path), "Skill file must exist"
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    assert "article_ingestor.py" in content, "Must call ingestor script"
    assert "tech-article-translator" in content, "Must invoke translator skill"
    assert "zensical build" in content, "Must build site"
    assert "ghp-import" in content, "Must deploy to gh-pages"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python -m pytest tests/test_daily_publisher_skill.py -v"`
Expected: FAIL with FileNotFoundError or assertion error

- [ ] **Step 3: Write minimal implementation**

Create `skills/daily-publisher/SKILL.md` with:
```markdown
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
3. Build the site:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && zensical build"`
4. Deploy to GitHub Pages:
   `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && ghp-import -p -b gh-pages site"`

Report the final success status and provide a link to the live site to the user.
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python -m pytest tests/test_daily_publisher_skill.py -v"`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_daily_publisher_skill.py skills/daily-publisher/SKILL.md
git commit -m "feat: create daily-publisher skill for pipeline automation"
```
