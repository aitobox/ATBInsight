---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- 数据湖
- 问答系统
- RAG
- 检索增强生成
- 基准测试
title: LakeQuest：跨数据湖基础问答的三域基准测试
---
### 文章背景与核心概要
在复杂的真实世界“数据湖”环境中评估端到端问答（QA）系统一直是一项重大挑战。传统的基准测试往往依赖于干净、模式对齐的数据，而由 Michael Solodko 等人提出的 LakeQuest 则填补了这一空白。它是一个经过人工验证的新型基准测试，迫使系统去遍历异构的表格、段落和链接元数据集合。

LakeQuest 包含来自三个不同领域（AI/ML元数据、零售银行和多模态生物医学药物信息）的 9,846 个 QA 对。该基准将源发现与跨模态综合隔离开来，从而暴露出现代检索增强生成（RAG）和智能体（Agentic）系统中的关键失效模式。基于标准 RAG 和智能体工具调用方法的基准评估表明，高质量的检索并不能保证正确的推理，这指明了未来企业级和科学数据湖智能体架构的发展方向。

---

# LakeQuest: A Three-Domain Benchmark for Grounded Question Answering across Data Lakes

> # LakeQuest: A Three-Domain Benchmark for Grounded Question Answering across Data Lakes

**Authors:** Michael Solodko, Steven Gong, Guangwei Yu, Satya Krishna Gorti, Jesse C. Cresswell, Victor Zhong  
**Published:** July 14, 2026 (Last Revised: August 11, 2026)  
**Venue:** Accepted at the Conference on Language Modeling (COLM) 2026  
**arXiv ID:** [2607.12310](https://arxiv.org/abs/2607.12310)

> **Authors:** Michael Solodko, Steven Gong, Guangwei Yu, Satya Krishna Gorti, Jesse C. Cresswell, Victor Zhong  
> **Published:** July 14, 2026 (Last Revised: August 11, 2026)  
> **Venue:** Accepted at the Conference on Language Modeling (COLM) 2026  
> **arXiv ID:** [2607.12310](https://arxiv.org/abs/2607.12310)

---

## Summary

> ## Summary

**LakeQuest** 是一个全新且经过人工验证的基准测试，旨在评估复杂真实世界“数据湖”中的端到端问答（QA）系统。与依赖干净且模式对齐数据的传统基准不同，LakeQuest 迫使系统在异构的表格、段落和链接元数据集合中进行导航。该基准测试包含跨三个不同领域（AI/ML元数据、零售银行和多模态生物医学药物信息）的 9,846 个 QA 对，将源发现与跨模态综合隔离开来，从而暴露出现代检索增强生成（RAG）和智能体系统中的关键失效模式。

> **LakeQuest** is a new, human-validated benchmark designed to evaluate end-to-end Question Answering (QA) systems within complex, real-world "data lakes." Unlike traditional benchmarks that rely on clean, schema-aligned data, LakeQuest forces systems to navigate heterogeneous collections of tables, passages, and linked metadata. With 9,846 QA pairs across three distinct domains—AI/ML metadata, retail banking, and multimodal biomedical drug information—the benchmark isolates source discovery from cross-modal synthesis to expose critical failure modes in modern Retrieval-Augmented Generation (RAG) and agentic systems.

---

## Key Features

> ## Key Features

*   **真实世界的复杂性：** 在嘈杂、弱结构化的数据而非理想化的语料库上评估系统。
*   **多领域覆盖：** 跨越三个不同的领域：
    *   **AI/ML 元数据：** 测试图中的关系链。
    *   **零售银行：** 测试账本中的策略扎根（Policy grounding）。
    *   **生物医学：** 测试联合表格问答。
*   **有依据的证据：** 每个问题都配有精确的、感知模态的证据指针，以确保可验证的推理。
*   **诊断效用：** 旨在识别当前 AI 架构中的特定弱点，例如跨文件组合和源发现方面的失效。

> *   **Realistic Complexity:** Evaluates systems on noisy, weakly structured data rather than idealized corpora.
> *   **Multi-Domain Coverage:** Spans three diverse fields:
>     *   **AI/ML Metadata:** Testing relation chaining in graphs.
>     *   **Retail Banking:** Testing policy grounding in ledgers.
>     *   **Biomedical:** Testing joint tabular QA.
> *   **Grounded Evidence:** Every question is paired with exact, modality-aware evidence pointers to ensure verifiable reasoning.
> *   **Diagnostic Utility:** Designed to identify specific weaknesses in current AI architectures, such as failures in cross-file composition and source discovery.

---

## Research Findings

> ## Research Findings

使用标准 RAG 和智能体工具调用方法的基准评估表明，**高质量的检索并不能保证正确的推理。** 该研究强调了当前系统在执行忠实的跨文件组合能力方面存在巨大差距，并表明未来的智能体 QA 系统必须优先考虑更强大的发现机制，以处理企业和科学数据湖的复杂性。

> Baseline evaluations using standard RAG and agentic tool-use methods demonstrate that **high-quality retrieval does not guarantee correct reasoning.** The study highlights a significant gap in current systems' ability to perform faithful cross-file composition and suggests that future agentic QA systems must prioritize more robust discovery mechanisms to handle the complexities of enterprise and scientific data lakes.

---

## Metadata & Access

> ## Metadata & Access

*   **主题：** 计算与语言 (cs.CL)；人工智能 (cs.AI)
*   **ACM 类别：** I.2.7; H.3.3; H.2.8
*   **全文链接：**
    *   [查看 PDF](https://arxiv.org/pdf/2607.12310)
    *   [HTML（实验性）](https://arxiv.org/html/2607.12310v3)
    *   [TeX 源码](https://arxiv.org/src/2607.12310)

> *   **Subjects:** Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
> *   **ACM Classes:** I.2.7; H.3.3; H.2.8
> *   **Full-Text Links:**
>     *   [View PDF](https://arxiv.org/pdf/2607.12310)
>     *   [HTML (Experimental)](https://arxiv.org/html/2607.12310v3)
>     *   [TeX Source](https://arxiv.org/src/2607.12310)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">