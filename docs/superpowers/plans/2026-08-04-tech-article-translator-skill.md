# Tech Article Translator Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a new skill `skills/tech-article-translator/SKILL.md` that instructs agents to backup original Markdown files to `bak/origin/DATE/` and translate English Markdown articles to bilingual Chinese/English quote-block format directly.

**Architecture:** A standalone Skill specification file placed under `skills/tech-article-translator/SKILL.md` along with test scenarios verifying compliance.

**Tech Stack:** Markdown, YAML Frontmatter, Git.

## Global Constraints

- Skill location MUST be `skills/tech-article-translator/SKILL.md`.
- Frontmatter MUST contain valid `name` and `description` (starting with "Use when...").
- Backup directory MUST strictly be `bak/origin/YYYY-MM-DD/`.
- Summary section MUST be placed at the top of translated articles.
- Original English paragraphs MUST be placed in `>` quote blocks immediately under their Chinese translations.
- Code blocks and images MUST NOT be wrapped in quote blocks.

---

### Task 1: Create Tech Article Translator Skill File

**Files:**
- Create: `skills/tech-article-translator/SKILL.md`
- Test: `tests/test_skill_structure.py`

**Interfaces:**
- Produces: `skills/tech-article-translator/SKILL.md`

- [ ] **Step 1: Write the failing test**

```python
import os

def test_tech_article_translator_skill_exists():
    path = "skills/tech-article-translator/SKILL.md"
    assert os.path.exists(path), f"{path} does not exist"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "name: tech-article-translator" in content
    assert "description: Use when" in content
    assert "bak/origin/" in content
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python -m pytest tests/test_skill_structure.py -v"`
Expected: FAIL (file does not exist)

- [ ] **Step 3: Write minimal implementation**

Create `skills/tech-article-translator/SKILL.md` with:

```markdown
---
name: tech-article-translator
description: Use when translating English Markdown technology articles into Chinese with bilingual paragraph quote blocks and backing up original files.
---

# Tech Article Translator (科技文章翻译官)

## Overview
Guides an Agent to translate Markdown technology articles from English into crisp, concise Chinese. The process backs up original files to `bak/origin/YYYY-MM-DD/`, inserts a Chinese summary at the top, and presents text paragraphs in bilingual format (Chinese translation followed by the original English in a `>` quote block).

## Workflow

1. **Backup Original Files**:
   - Create `bak/origin/<DATE>/` directory if it does not exist.
   - Copy original `.md` files to `bak/origin/<DATE>/` before editing.

2. **Generate Overview & Background**:
   - Below the title, add a Chinese background & summary block:
     ```markdown
     ### 文章背景与核心概要
     [3-5 句简洁明快的中文总结]

     ---
     ```

3. **Structure-Aware Translation**:
   - **Text Paragraphs**: Provide clear Chinese translation, followed by original English in quote block (`>`):
     ```markdown
     这是中文翻译段落。

     > This is the original English paragraph.
     ```
   - **Code Blocks, Images, & Frontmatter**: Keep untouched without quote wrapping.

4. **Replace Original File**:
   - Save translated content back to the original file path under `docs/insight/<DATE>/`.
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash -c "source /home/aitobox/miniconda3/bin/activate ATBInsight && python -m pytest tests/test_skill_structure.py -v"`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add skills/tech-article-translator/SKILL.md tests/test_skill_structure.py
git commit -m "feat: add tech-article-translator skill"
```
