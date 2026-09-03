---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-04
hide:
- navigation
tags:
- 自动形式化
- 神经符号方法
- 演化搜索
- 大语言模型
- 定理证明
title: FormalEvolve：用于多样化自动形式化的神经符号演化搜索
---
### 文章背景与核心概要
自动形式化（将非形式化的数学语言翻译为形式化语句）长期以来被视为一个传统的单输出预测任务。然而，标准的评估往往忽略了形式化语句作为面向定理证明器的接口，其结构会直接影响证明搜索的性能。

为此，本文提出了 **FormalEvolve**，这是一个将自动形式化重新构想为受预算约束的测试时搜索问题的神经符号框架。FormalEvolve 维护了一个可编译的归档库，并通过大语言模型（LLM）驱动的变异、交叉、有界补丁修复以及符号化抽象语法树（AST）重写，生成去重且语义接受的语句库。在生成器调用预算（$T=100$）和固定证明器预算（$B=64$）的评估下，与没有归档库的基线方法相比，FormalEvolve 显著提升了定理完整证明的成功率，在 **CombiBench**（58.0%）和 **ProofNet**（84.9%）上取得了优异的成果。

---

## 📋 摘要 (Summary)

**FormalEvolve** 是一个神经符号框架，它将自动形式化（将非形式化的数学翻译为形式化语句）从传统的单输出预测任务转变为一个受预算限制的测试时搜索问题。

> **FormalEvolve** is a neuro-symbolic framework that recasts autoformalization (translating informal mathematics into formal statements) from a traditional single-output prediction task into a budgeted test-time search problem. 

标准评估通常将自动形式化的多对多本质简化为单一预测，从而忽视了形式化语句如何作为面向证明器的接口，其结构直接影响证明搜索的性能。FormalEvolve 维护了一个可编译的归档库，并通过大语言模型（LLM）驱动的变异、交叉、有界补丁修复以及符号抽象语法树（AST）重写，生成去重且语义接受的语句库。

> Standard evaluation often reduces the many-to-many nature of autoformalization to a single prediction, overlooking how a formal statement serves as a prover-facing interface whose structure directly impacts proof search performance. FormalEvolve maintains a compilation-feasible archive and generates a deduplicated, semantically accepted repertoire using Large Language Model (LLM)-driven mutation, crossover, bounded patch repair, and symbolic Abstract Syntax Tree (AST) rewrites. 

在生成器调用预算（$T=100$）和固定证明器预算（$B=64$）下进行评估时，与没有归档库的基线方法相比，FormalEvolve 显著提高了定理完全证明的成功率，并在 **CombiBench**（58.0%）和 **ProofNet**（84.9%）上实现了更优的成功率。

> Evaluated under a generator-call budget ($T=100$) and a fixed prover budget ($B=64$), FormalEvolve significantly improves theorem-complete proving and achieves superior success rates on **CombiBench** (58.0%) and **ProofNet** (84.9%) compared to baseline methods without archives.

---

## 📌 文档元数据 (Document Metadata)

* **arXiv ID:** [arXiv:2603.19828](https://arxiv.org/abs/2603.19828) [cs.AI]
* **作者 (Authors):** Haijian Lu, Wei Wang, Jing Liu
* **主学科 (Primary Subject):** 人工智能 (`cs.AI`)
* **出版状态 (Publication Status):** 已被 *Findings of EMNLP 2026* 录用（修订版最终稿，29页，13张图）
* **提交时间 (Submitted):** 2026年3月20日（v1）；最后修订：2026年9月2日（v4）

---

## 🔗 访问链接 (Access Links)

* **PDF:** [查看 PDF](https://arxiv.org/pdf/2603.19828)
* **HTML（实验性）:** [arXiv HTML](https://arxiv.org/html/2603.19828v4)
* **源码:** [TeX 源码](https://arxiv.org/src/2603.19828)
* **DOI:** [10.48550/arXiv.2603.19828](https://doi.org/10.48550/arXiv.2603.19828)