---
name: tech-article-translator
description: Use when translating English Markdown technology articles into Chinese with bilingual paragraph quote blocks and YAML Front Matter headers.
---

# Tech Article Translator (科技文章翻译官)

## Overview

Guides an Agent to translate Markdown technology articles and academic papers from English into crystal-clear, engaging Chinese in the style of popular science literature (浅显易懂的中文科普读物风格) **directly using the Agent's own translation capabilities**.

<HARD-GATE>
**CRITICAL RULE**: The Agent MUST read, translate, and re-write articles directly using its own cognitive and reasoning capabilities.
Do **NOT** write or execute external python/bash scripts, API call wrappers, or automated batch LLM tools to process the articles. All reading, understanding, translating, formatting, and file writing MUST be performed directly by the Agent (or via subagents).
</HARD-GATE>

The translation process takes raw articles from `bak/origin/YYYY-MM-DD/`, inserts a standard YAML Front Matter metadata header, generates a Chinese background & overview block, presents text paragraphs and subheadings in bilingual format (a popular-science Chinese paraphrase followed by the original English paragraph in a `>` quote block), and saves the result as `docs/blog/posts/YYYY-MM-DD-<clean-title>.md`.

---

## Core Translation Rules & Tone (核心翻译规则与科普语气)

1. **通俗易懂的科普风格 (Popular Science Tone)**:
   - 翻译风格与中文科普读物相似，浅显易懂、自然生动，彻底消除翻译腔与生硬欧化句式。
   - 准确传达原文的事实、背景与逻辑，不随意杜撰或删减核心技术细节。
2. **保留原始段落格式与术语 (Preserve Structure & Acronyms)**:
   - 意译时必须保留原始段落划分与行文层次。
   - 保留专有名词与技术缩写（例如 FLAC, JPEG, CPU, GPU, CUDA 等）。
   - 保留公司名称与缩写（例如 Microsoft, Amazon, OpenAI, Google, Meta, Anthropic, NVIDIA 等），不进行汉化。
3. **人名不翻译 (Do NOT Translate Human Names)**:
   - 原文中出现的所有人名（例如 Geoffrey Hinton, Yann LeCun, Ashish Vaswani 等）严格保持英文原名，切勿音译或标注中英对照。
4. **保留文献引用 (Preserve Citations)**:
   - 严格保留所有的论文引用标记，例如 `[20]`, `[1, 3]`, `[Vaswani et al., 2017]` 等，保持位置与格式一致。
5. **图表标题翻译规范 (Figure & Table Formatting)**:
   - 翻译图表名称的同时严格保留原有结构标点：
     - `Figure 1: ` 翻译为 `图 1: `
     - `Figure 2: ` 翻译为 `图 2: `
     - `Table 1: ` 翻译为 `表 1: `
     - `Table 2: ` 翻译为 `表 2: `
6. **括号与空格规范 (Bracket & Spacing Rules)**:
   - 所有全角括号 `（）` 必须统一转换为半角括号 `()`。
   - **在左括号前必须添加一个半角空格，在右括号后必须添加一个半角空格**。
   - 示例：`大语言模型 (LLM) 的演进`，而不是 `大语言模型（LLM）的演进` 或 `大语言模型(LLM)的演进`。
   - （注：若右括号紧跟中文标点如句号、逗号、顿号，右侧半角空格由中文标点自然衔接）。
7. **Markdown 格式保真 (Markdown Preservation)**:
   - 必须严格保留原始 Markdown 语法标记（代码块、行内代码、图片、数学公式、链接等原生呈现，不额外加 `>` 引用包裹）。
8. **专业术语首见原则 (First Appearance Rule)**:
   - 专业术语在整篇译文中**首次出现**时，在术语后紧跟半角括号附带英文原文，形如：`生成式 AI (Generative AI)`。
   - 首次出现之后再次提及该术语时，直接使用规范中文，无需重复标注英文。
9. **常用 AI 术语统一映射表 (Expanded Terminology Mapping Table)**:

| 英文术语 (English) | 规范中文翻译 (Chinese) | 备注 |
| :--- | :--- | :--- |
| **Transformer** | `Transformer` | 保持英文原词，不翻译 |
| **Token** | `Token` | 保持英文原词，不翻译为“词元/令牌” |
| **LLM / Large Language Model** | `大语言模型` | 首次出现附英文 ` (Large Language Model, LLM) ` |
| **Zero-shot** | `零样本` | 保持“零样本” |
| **Few-shot** | `少样本` | 保持“少样本” |
| **AI Agent** | `AI 智能体` | 首次出现附英文 ` (AI Agent) ` |
| **AGI** | `通用人工智能` | 首次出现附英文 ` (AGI) ` |
| **Prompt / Prompt Engineering** | `提示词` / `提示词工程` | 统一为“提示词”而非“提示” |
| **Fine-tuning / SFT** | `微调` / `监督微调` | 首次出现附英文 ` (Supervised Fine-Tuning, SFT) ` |
| **Benchmark** | `基准测试` | 不翻译为“标杆/基线” |
| **RAG** | `检索增强生成` | 首次出现附英文 ` (Retrieval-Augmented Generation, RAG) ` |
| **Hallucination** | `幻觉` | 模型的输出幻觉 |
| **Grounding / Grounded** | `视觉定位` / `坐标接地` | 特指模型在图像中准确定位坐标的能力 |
| **In-Context Learning (ICL)** | `上下文学习` | 首次出现附英文 ` (In-Context Learning, ICL) ` |
| **Chain-of-Thought (CoT)** | `思维链` | 首次出现附英文 ` (Chain-of-Thought, CoT) ` |
| **Alignment / RLHF / DPO** | `对齐` / `RLHF` / `DPO` | 首次出现写全称并附缩写 |
| **Multimodal / VLM** | `多模态` / `视觉语言模型` | 首次出现附英文 ` (Vision-Language Model, VLM) ` |
| **Latency / Throughput** | `延迟` / `吞吐量` | 性能工程标准术语 |
| **Overfitting / Underfitting** | `过拟合` / `欠拟合` | 机器学习标准术语 |

- `Transformer -> Transformer`
- `Token -> Token`
- `LLM/Large Language Model -> 大语言模型`
- `Zero-shot -> 零样本`
- `Few-shot -> 少样本`
- `AI Agent -> AI 智能体`
- `AGI -> 通用人工智能`

---

## Three-Step Translation Strategy (三步迭代翻译法)

在对文章的每个段落进行翻译时，在思维中（或在交互模式下）严格遵循三步策略：

1. **直译 (Literal Translation)**: 紧贴英文原文句式和结构直译，确保信息完整、零遗漏。
2. **问题诊断 (Problem Diagnosis)**: 审视直译文本，准确指出：
   - 不符合中文表达习惯之处（语序僵硬、欧化句式等）
   - 语句不通顺之处（具体语病位置）
   - 晦涩难懂的技术概念（给出通俗易懂的科普解读思路）
3. **意译润色 (Paraphrase & Popularization)**: 结合诊断问题重新意译，在忠实原意的前提下采用通俗生动的科普笔触消除翻译腔，确保语句自然流畅、易于理解，作为最终的中文段落输出。

---

## Workflow & Output File Structure (工作流程与文件结构规范)

翻译全篇长文并输出保存至 `docs/blog/posts/` 时，必须严格遵循以下文件结构规范：

### 1. 注入标准 YAML Front Matter 标头
在 Markdown 文件第 1 行注入标准 YAML 元数据头（必须包含 `hide: - navigation` 以适配静态博客展示）：
```yaml
---
authors:
  - aitoboxrobot
categories:
  - <从 [产品发布, 工具教程, 研究解读, 商业动态, arXiv论文, 其他] 中选择最契合的1个分类>
date: YYYY-MM-DD
hide:
  - navigation
tags:
  - <提取的技术标签1>
  - <提取的技术标签2>
  - <提取的技术标签3>
title: "<翻译后的精炼中文标题>"
---
```

### 2. 论文元数据与核心概要模块
- **针对学术论文（如 arXiv 预印本）**：在主标题 `# 标题` 下方保留标准的元数据引用块：
  ```markdown
  > **arXiv:XXXX.XXXXX** [cs.XX]  
  > **Subjects:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)  
  > **Authors:** Author One, Author Two  
  > **Submitted:** 2 Dec 2025; Last revised: 5 Aug 2026  
  > **DOI / Paper:** [10.48550/arXiv.XXXX.XXXXX](https://doi.org/...)  
  > **Project / Code:** [GitHub - repo/name](https://github.com/...)
  ```
- **文章背景与核心概要**：随后紧接着插入 3-5 句浅显明快、通俗生动的科普总结：
  ```markdown
  ### 文章背景与核心概要
  [3-5 句浅显易懂、引人入胜的中文科普总结，介绍技术背景、核心突破与行业意义]

  ---
  ```

### 3. 全文双语对照排版规范 (Comprehensive Bilingual Alignment)
- **各级小标题（H2 / H3 / H4）**：小标题同样遵循双语对照，上方为科普化中文标题，下方为英文原标题引用块：
  ```markdown
  ## 2. 点击交互：教 AI 掌握鼠标操作

  > ## Challenge 2: Clicking on things
  ```
- **普通文本段落**：上方为经三步法科普润色后的中文意译段落，紧接着下方为包含在 `>` 引用块中的英文原文段落：
  ```markdown
  这是经过三步法科普润色后、通俗生动的中文意译段落。

  > This is the original English paragraph from the source text.
  ```
- **列表项（Ordered / Unordered Lists）**：**整组列表成块对照**（避免单条列表割裂），中文列表组下方跟英文原列表引用组：
  ```markdown
  1. **环境安全**：将操作系统安全隔离在受控容器中；
  2. **精准点击**：让 AI 学会识别屏幕元素并准确定位。

  > 1. **Security:** Isolating the operating system in a safe, controlled environment
  > 2. **Clicking on things:** Enabling the AI to click precisely to manipulate UI elements
  ```
- **原文自带的引用块 (Blockquotes)**：为避免与双语对照混淆，原文自带的引用内容需显式添加提示符：
  ```markdown
  > 💬 [原文引用 / Original Quote]:
  > "Simplicity is prerequisite for reliability." — Edsger W. Dijkstra
  ```
- **代码块、图片与数学公式**：保持原生 Markdown 格式，**严禁** 用 `>` 引用块包裹，图片相对路径保持正确。

### 4. 长篇论文与万字长文处理策略 (Long Article Chunking)
- **触发条件**：当原文词数 $> 3,000$ 或单文件体积 $> 15\text{ KB}$ 时。
- **处理策略**：
  1. **按章节渐进处理 (Progressive Translation)**：优先以 `##` 二级章节为单元按顺序分批处理，统一术语表和实体首见标记。
  2. **Subagent 协同机制**：可使用 `invoke_subagent` 分配独立章节，但在 Prompt 中必须统一提供 YAML Front Matter 标题与术语规范，完成后按顺序拼接，防止长篇输出遭遇上下文截断或“前精后疏、后半段质量滑坡”。

### 5. 文件名清洗与保存规范 (Filename Sanitization)
- **保存路径**：`docs/blog/posts/YYYY-MM-DD-<clean-title>.md`。
- **清洗规则**：
  - 必须保留 `YYYY-MM-DD-` 标准日期前缀。
  - 过滤或替换文件名中的非法字符（包括冒号 `:`、斜杠 `/`、反斜杠 `\`、问号 `?`、星号 `*`、引号 `"` `'`、括号 `()`、美金符号 `$`、感叹号 `!` 等），统一替换为半角连字符 `-`。
  - 将连续的连字符合并（`-` 重复缩减为单 `-`），去除标题首尾的 `-`。
  - 示例：`2026-09-10-CUDA-L2-通过强化学习超越-cuBLAS-的矩阵乘法性能.md`。
- **原始文件保护**：保留 `bak/origin/YYYY-MM-DD/` 下的原始文件完整无损，**严禁删除**。

---

## Standalone Snippet Mode (单段翻译交互格式)

当用户仅提供单段文本要求翻译，或者明确要求打印三步推理过程时，输出严格遵循以下模板：

```markdown
### 直译
{直译结果}

***

### 问题
{直译的具体问题列表}

***

### 意译
```
{意译结果}
```
```

---

## Common Mistakes & Red Flags (防雷指南)

| 违规行为 | 纠正要求 |
| :--- | :--- |
| 使用外部脚本或批处理命令替代 Agent 自行翻译 | **绝对红线 (HARD-GATE)**。必须由 Agent 或 Subagents 亲自阅读、理解并撰写。 |
| 将人名汉化音译（如将 Geoffrey Hinton 译为“杰弗里·辛顿”） | **绝对禁止**。所有人名必须保留英文原名。 |
| 将公司名汉化（如将 Microsoft 译为“微软”） | **严格保留**。Microsoft, OpenAI, Amazon 等公司名称必须保留英文。 |
| 使用全角中文括号 `（）` 或未在半角括号两侧添加空格 | **格式必须规范**。统一改为半角括号并两侧留半角空格：` (LLM) `。 |
| 将 `Token` 翻译为“词元/代币” | **遵循术语表**。`Token` 必须保留英文 `Token`。 |
| 破坏 Markdown 格式或对代码块/图片添加 `>` 引用包裹 | **严格保真**。代码、图片、公式不加 `>`，文本与标题成组双语对照。 |
| Front Matter 缺失 `hide: - navigation` | **必须保留**。确保生成的博客排版与站点布局无缝契合。 |
| 长文直接一次性刷入导致结尾截断或胡乱总结 | **按章节渐进**。篇幅过长时按 H2 模块分批翻译后有序缝合。 |
