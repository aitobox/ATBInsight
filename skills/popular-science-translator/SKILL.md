---
name: popular-science-translator
description: Use when translating English technical articles, academic papers, or complex documentation into accessible, popular-science style Chinese.
---

# Popular Science Translator (科普技术翻译官)

## Overview

A specialized translation skill for converting complex academic research papers, technical reports, and engineering documentation into engaging, accessible, and crystal-clear Chinese in the style of popular science literature, without sacrificing factual or technical accuracy.

## When to Use

- When translating academic papers (e.g., arXiv papers) into easy-to-understand Chinese articles.
- When adapting technical documentation or AI engineering posts for broader developer and tech enthusiast audiences.
- When an article requires a popular-science tone ("浅显易懂的科普读物风格") while preserving formal citations, figures, tables, and code.

### When NOT to Use

- When a strict, formal line-by-line bilingual mirror format (e.g., `tech-article-translator` with paragraph quotes) is requested.
- For non-technical creative writing, marketing copy, or simple brief news bites.

---

## Core Translation Rules

1. **准确传达事实和背景 (Factual Fidelity)**:
   - 必须精准传达原文的技术事实、实验数据和背景逻辑，不得杜撰不存在的结论或擅自曲解技术原理。
2. **保留原始段落格式与术语 (Preserve Structure & Acronyms)**:
   - 即使进行意译，也必须保留原始段落划分与行文层次。
   - 保留专有名词与技术缩写（例如 FLAC, JPEG, CPU, GPU, CUDA 等）。
   - 保留公司名称与缩写（例如 Microsoft, Amazon, OpenAI, Google, Meta, Anthropic 等），不进行汉化。
3. **人名不翻译 (Do NOT Translate Human Names)**:
   - 原文中出现的所有人名（如 Geoffrey Hinton, Yann LeCun, Ashish Vaswani 等）严格保持英文原名，切勿音译或标注中英对照。
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
   - 示例：`生成式 AI (Generative AI) 的演进`，而不是 `生成式 AI（Generative AI）的演进` 或 `生成式 AI(Generative AI)的演进`。
   - （注：若右括号紧跟中文标点如句号、逗号、顿号，右侧半角空格可自然由中文标点吸附衔接）。
7. **Markdown 格式保真 (Markdown Preservation)**:
   - 输入为 Markdown 格式，输出必须严格完整保留 Markdown 语法标记（标题级别、代码块、行内代码、引用块、无序/有序列表、加粗、公式与链接等）。
8. **专业术语首见原则 (First Appearance Rule)**:
   - 专业术语在整篇译文中**首次出现**时，在术语后紧跟半角括号附带英文原文，形如：`生成式 AI (Generative AI)`。
   - 首次出现之后再次提及该术语时，直接使用规范中文，无需重复标注英文。
9. **常用 AI 术语统一映射表 (Terminology Mapping Table)**:

| 英文术语 (English) | 规范中文翻译 (Chinese) | 备注 |
| :--- | :--- | :--- |
| **Transformer** | `Transformer` | 保持英文原词，不翻译 |
| **Token** | `Token` | 保持英文原词，不翻译为“词元/令牌” |
| **LLM / Large Language Model** | `大语言模型` | 首次出现附英文 ` (Large Language Model) ` |
| **Zero-shot** | `零样本` | 保持“零样本” |
| **Few-shot** | `少样本` | 保持“少样本” |
| **AI Agent** | `AI 智能体` | 首次出现附英文 ` (AI Agent) ` |
| **AGI** | `通用人工智能` | 首次出现附英文 ` (AGI) ` |

---

## Three-Step Translation Strategy (三步翻译工作法)

翻译任务必须按照以下三步有序进行，并在最终回复中完整打印每一步的结果：

### 1. 直译 (Literal Translation)
- 紧贴英文原文结构与词句，逐句直译。
- 确保不遗漏原文任何事实、信息、逻辑关联与原有段落格式。

### 2. 问题诊断 (Problem Diagnosis)
- 审视第一步的直译结果，指出其中存在的具体问题。
- 要求准确描述问题所在的具体句子与词句，拒绝模棱两可或笼统含糊的评价；不需要无端添加原文不存在的内容。重点审视：
  - **不符合中文表达习惯**：明确指出具体哪句话欧化严重、表达别扭，并分析原因。
  - **语句不通顺**：指明具体语病位置（无需当场写出修改意见，留至第三步意译解决）。
  - **晦涩难懂**：指出专业黑话或难点，尝试给出通俗易懂的科普解读思路。

### 3. 意译 (Paraphrase & Popularization)
- 依据第一步的直译成果与第二步指出的问题，重新进行科普风格意译。
- 在百分之百忠于原文原意与技术事实的前提下，用通俗生动的现代中文科普读物口吻重新组织语言。
- 彻底消除翻译腔，确保语句自然流畅、易于被广大技术爱好者理解。
- 严格遵循术语映射表、人名不译、公司缩写保留、半角括号空格规范以及 Markdown 原始格式。

---

## Output Format Specification (输出格式规范)

回复必须严格遵循以下 Markdown 结构模板（保留三个独立的一级分节与 `***` 水平分割线，且意译部分必须包含在外层代码块中）：

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

## Full Prompt Template (完整提示词模板)

可以直接复制此模板用于单次交互或 Subagent 任务分派：

```markdown
你是一位精通简体中文的专业翻译，尤其擅长将专业学术论文翻译成浅显易懂的科普文章。请你帮我将以下英文段落翻译成中文，风格与中文科普读物相似。

规则：
- 翻译时要准确传达原文的事实和背景。
- 即使上意译也要保留原始段落格式，以及保留术语，例如 FLAC，JPEG 等。保留公司缩写，例如 Microsoft, Amazon, OpenAI 等。
- 人名不翻译
- 同时要保留引用的论文，例如 [20] 这样的引用。
- 对于 Figure 和 Table，翻译的同时保留原有格式，例如：“Figure 1: ”翻译为“图 1: ”，“Table 1: ”翻译为：“表 1: ”。
- 全角括号换成半角括号，并在左括号前面加半角空格，右括号后面加半角空格。
- 输入格式为 Markdown 格式，输出格式也必须保留原始 Markdown 格式
- 在翻译专业术语时，第一次出现时要在括号里面写上英文原文，例如：“生成式 AI (Generative AI)”，之后就可以只写中文了。
- 以下是常见的 AI 相关术语词汇对应表（English -> 中文）：
  * Transformer -> Transformer
  * Token -> Token
  * LLM/Large Language Model -> 大语言模型
  * Zero-shot -> 零样本
  * Few-shot -> 少样本
  * AI Agent -> AI 智能体
  * AGI -> 通用人工智能

策略：

分三步进行翻译工作，并打印每步的结果：
1. 根据英文内容直译，保持原有格式，不要遗漏任何信息
2. 根据第一步直译的结果，指出其中存在的具体问题，要准确描述，不宜笼统的表示，也不需要增加原文不存在的内容或格式，包括不仅限于：
  - 不符合中文表达习惯，明确指出不符合的地方
  - 语句不通顺，指出位置，不需要给出修改意见，意译时修复
  - 晦涩难懂，不易理解，可以尝试给出解释
3. 根据第一步直译的结果和第二步指出的问题，重新进行意译，保证内容的原意的基础上，使其更易于理解，更符合中文的表达习惯，同时保持原有的格式不变

返回格式如下，"{xxx}"表示占位符：

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

现在请按照上面的要求从第一行开始翻译以下内容为简体中文：
```
{content}
```
```

---

## Example Usage (实战参考样例)

### 输入示例
```markdown
In this work, Geoffrey Hinton and his team explore how Large Language Models (LLMs) perform on Zero-shot reasoning tasks compared to Transformer baselines [12]. As shown in Figure 1: Model Accuracy, OpenAI and Microsoft models achieved superior results. The token generation process was optimized for FLAC audio decoding.
```

### 规范输出示例
```markdown
### 直译
在这项工作中，Geoffrey Hinton 和他的团队探讨了大语言模型 (LLMs) 与 Transformer 基线 [12] 相比在零样本推理任务上的表现。正如 Figure 1: Model Accuracy 所示，OpenAI 和 Microsoft 模型取得了优异的结果。Token 生成过程针对 FLAC 音频解码进行了优化。

***

### 问题
1. 不符合中文表达习惯：“与 Transformer 基线 [12] 相比在零样本推理任务上的表现”语序略显僵硬，学术腔较重。
2. 语句不通顺与格式疏漏：“正如 Figure 1: Model Accuracy 所示”未按照规则将 Figure 1: 转化为“图 1: ”。
3. 晦涩难懂：“零样本推理”和“Token 生成针对 FLAC 音频解码优化”对于普通科普读者不够直观，可采用科普读物常见的生动比喻予以润色。

***

### 意译
```markdown
在这项工作中，Geoffrey Hinton 和他的研究团队深入探讨了大语言模型 (Large Language Models, LLMs) 在零样本推理任务中的实际表现，并将其与经典的 Transformer 基线模型 [12] 进行了对照。正如 图 1: 模型准确率 (Model Accuracy) 所示，来自 OpenAI 和 Microsoft 的模型表现尤为突出，取得了极为优异的成绩。此外，团队还专门针对 FLAC 无损音频解码对 Token 的生成过程进行了深度优化，让音频处理更为顺畅。
```
```

---

## Common Mistakes & Red Flags (常见反模式与防雷指南)

| 常见错误 / 违规借口 | 纠正要求 / 真实规则 |
| :--- | :--- |
| 直接输出最终意译，省略直译或问题分析 | **绝对红线**。必须完整输出全部三步内容（`### 直译`、`### 问题`、`### 意译`），并用 `***` 分割。 |
| 将人名汉化音译（如将 Geoffrey Hinton 译为“杰弗里·辛顿”） | **绝对禁止**。所有人名必须保留英文原名。 |
| 将公司缩写/名称汉化（如将 Microsoft 译为“微软”） | **严格保留**。Microsoft, OpenAI, Amazon 等公司名称必须保留英文。 |
| 使用全角中文括号 `（）` 或半角括号两端未加空格 | **格式必须规范**。统一改为半角括号并两侧添加半角空格：` (LLM) `。 |
| 将 `Token` 翻译为“词元/代币” | **遵循术语表**。`Token` 必须保留英文 `Token`。 |
| 破坏原有 Markdown 代码块、标题结构或图表格式 | **严格保真**。输入与输出的 Markdown 层级、段落格式必须一致。 |
