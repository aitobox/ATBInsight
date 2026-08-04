---
name: tech-article-translator
description: Use when translating English Markdown technology articles into Chinese with bilingual paragraph quote blocks and backing up original files.
---

# Tech Article Translator (科技文章翻译官)

## Overview
Guides an Agent to translate Markdown technology articles from English into crisp, concise Chinese **directly using the Agent's own translation capabilities**. 

<HARD-GATE>
**CRITICAL RULE**: The Agent MUST read, translate, and re-write articles directly using its own cognitive and reasoning capabilities.
Do **NOT** write or execute external python/bash scripts, API call wrappers, or automated batch LLM tools to process the articles. All reading, understanding, translating, formatting, and file writing MUST be performed directly by the Agent (or via subagents).
</HARD-GATE>

The translation process backs up original files to `bak/origin/YYYY-MM-DD/`, inserts a Chinese summary at the top, and presents text paragraphs in bilingual format (Chinese translation followed by the original English in a `>` quote block).

## Workflow

1. **Backup Original Files**:
   - Create `bak/origin/<DATE>/` directory if it does not exist.
   - Copy original `.md` files to `bak/origin/<DATE>/` before editing.

2. **Generate Overview & Background (Agent Direct Execution)**:
   - Read the target Markdown file directly.
   - Below the title, add a Chinese background & summary block directly composed by the Agent:
     ```markdown
     ### 文章背景与核心概要
     [3-5 句简洁明快的中文总结]

     ---
     ```

3. **Structure-Aware Translation (Agent Direct Translation)**:
   - **Text Paragraphs**: The Agent directly translates English text paragraphs into clear Chinese, followed by the original English in a quote block (`>`):
     ```markdown
     这是中文翻译段落。

     > This is the original English paragraph.
     ```
   - **Code Blocks, Images, & Frontmatter**: Keep untouched without quote wrapping.

4. **Save & Rename File**:
   - Save the translated content directly to `docs/insight/<DATE>/`.
   - Rename the translated Markdown file from `article_<id>.md` to `<translated-title-slug>.md` (clean translated Chinese title filename) under `docs/insight/<DATE>/`, and delete/remove the old filename.
