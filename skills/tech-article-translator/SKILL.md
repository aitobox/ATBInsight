---
name: tech-article-translator
description: Use when translating English Markdown technology articles into Chinese with bilingual paragraph quote blocks and YAML Front Matter headers.
---

# Tech Article Translator (科技文章翻译官)

## Overview
Guides an Agent to translate Markdown technology articles from English into crisp, concise Chinese **directly using the Agent's own translation capabilities**. 

<HARD-GATE>
**CRITICAL RULE**: The Agent MUST read, translate, and re-write articles directly using its own cognitive and reasoning capabilities.
Do **NOT** write or execute external python/bash scripts, API call wrappers, or automated batch LLM tools to process the articles. All reading, understanding, translating, formatting, and file writing MUST be performed directly by the Agent (or via subagents).
</HARD-GATE>

The translation process takes raw articles from `bak/origin/YYYY-MM-DD/`, inserts a YAML Front Matter metadata header at the very top of the file, places a Chinese background & summary block, presents text paragraphs in bilingual format (Chinese translation followed by original English in a `>` quote block), and saves the result as `docs/blog/posts/YYYY-MM-DD-<title>.md`.

## Workflow

1. **Inject YAML Front Matter Header**:
   - At the very beginning of the Markdown file (Line 1), insert a standard YAML Front Matter header:
     ```yaml
     ---
     title: <翻译后的中文标题>
     date: YYYY-MM-DD
     authors:
       - aitoboxrobot
     categories:
       - 深度研报
     tags:
       - <提取的标签1>
       - <提取的标签2>
     ---
     ```

2. **Generate Overview & Background**:
   - Read the target Markdown file directly from `bak/origin/YYYY-MM-DD/`.
   - Below the YAML Front Matter and main `# Title`, add a Chinese background & summary block directly composed by the Agent:
     ```markdown
     ### 文章背景与核心概要
     [3-5 句简洁明快的中文总结]

     ---
     ```

3. **Structure-Aware Translation**:
   - **Text Paragraphs**: The Agent directly translates English text paragraphs into clear Chinese, followed by the original English in a quote block (`>`):
     ```markdown
     这是中文翻译段落。

     > This is the original English paragraph.
     ```
   - **Code Blocks, Images, & Equations**: Keep untouched without quote wrapping.

4. **Save & Path Formatting**:
   - Save the translated content directly to `docs/blog/posts/YYYY-MM-DD-<translated-title>.md`.
   - Leave the original file in `bak/origin/YYYY-MM-DD/` intact (do NOT delete it).
