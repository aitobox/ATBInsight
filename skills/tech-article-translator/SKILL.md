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
