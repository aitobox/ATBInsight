---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 大语言模型
- 模型微调
- 可解释性
- Logit分析
- 偏差检测
title: Diff Mining：通过Logit差异揭示微调目标
---
### 文章背景与核心概要

随着微调（Finetuning）成为适配大语言模型的标准方法，准确追踪模型习得的行为以及识别潜在的不良偏见，仍然是一个巨大的技术挑战。本文介绍了一种名为“Diff Mining”的轻量级、可扩展框架，它通过简单对比微调后模型与基础模型的输出 Logit，来揭示模型的微调目标。

该框架无需访问模型的内部权重，主要分为两个阶段：1）提取阶段：在参考语料库上计算两个模型在各个上下文中的 Logit 差异；2）聚合阶段：利用 Top-K 频率法或非负矩阵分解（NMF）将这些信号浓缩为可解释的 Token 集，从而将多重训练目标隔离为不同的聚类。实证评估表明，Diff Mining 在领域检测方面优于现有的前沿模型差异比较方法，增强了下游的可解释性，并且在无需针对性探测的情况下，成功标记了超过三分之一的注入偏见。

---

## 摘要 (Summary)

随着微调成为适配语言模型的标准方法，准确追踪习得的具体行为——并识别潜在的不良偏见——仍然是一项重大挑战。

> As finetuning becomes the standard approach for adapting language models, tracking precisely what behaviors are acquired—and identifying potential unwanted biases—remains a major challenge. 

**Diff Mining** 是一种轻量级、可扩展的框架，旨在通过简单比较微调模型与其基础模型的输出 Logit 来揭示微调目标。该框架无需访问模型的内部权重，主要分两个主要阶段运行：
1. **提取（Extraction）**：在参考语料库上计算模型之间每个上下文的 Logit 差异。
2. **聚合（Aggregation）**：使用 Top-K 频率法或非负矩阵分解（NMF）将这些信号浓缩为可解释的 Token 集，从而将多个训练目标隔离为不同的聚类。

> **Diff Mining** is a lightweight, scalable framework designed to uncover finetuning objectives by simply comparing the output logits of a finetuned model against its base model. Requiring no access to internal model weights, the framework operates in two main stages:
> 1. **Extraction:** Computes per-context logit differences between the models over a reference corpus.
> 2. **Aggregation:** Condenses these signals into interpretable token sets using either a Top-K frequency method or Non-negative Matrix Factorization (NMF) to isolate multiple training objectives into distinct clusters.

实证评估表明，在领域检测方面，Diff Mining 优于最先进的模型差异比较方法，增强了下游的可解释性，并且在无需针对性探测的情况下成功标记了超过三分之一的注入偏见。

> Empirical evaluations demonstrate that Diff Mining outperforms state-of-the-art model diffing methods in domain detection, enhances downstream interpretability, and successfully flags over a third of injected biases without requiring targeted probing.

---

## 论文元数据 (Paper Metadata)

| 字段 (Field) | 详情 (Details) |
| :--- | :--- |
| **备注 (Comments)** | 37 页，7 幅图。ICLR 2026 研讨会：可信赖 AI 的原则性设计 (ICLR 2026 Workshop: Principled Design for Trustworthy AI)。 |
| **引用方式 (Cite As)** | `arXiv:2608.26462 [cs.LG]` |
| **DOI** | [10.48550/arXiv.2608.26462](https://doi.org/10.48550/arXiv.2608.26462) |
| **许可协议 (License)** | [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> |

> | Field | Details |
> | :--- | :--- |
> | **Comments** | 37 pages, 7 figures. ICLR 2026 Workshop: Principled Design for Trustworthy AI. |
> | **Cite As** | `arXiv:2608.26462 [cs.LG]` |
> | **DOI** | [10.48550/arXiv.2608.26462](https://doi.org/10.48550/arXiv.2608.26462) |
> | **License** | [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> |