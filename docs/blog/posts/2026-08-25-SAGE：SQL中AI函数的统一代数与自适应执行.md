---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- AI与SQL
- 数据库优化
- 关系代数
- 大语言模型
- 检索增强生成
title: SAGE：SQL中AI函数的统一代数与自适应执行
---
### 文章背景与核心概要

随着现代SQL系统日益集成AI能力以处理分类、提取、过滤、排序、检索、连接和摘要等任务，各种定制化的API层出不穷。然而，本文研究发现，这些形形色色的AI函数在关系型数据库中本质上仅归结为三种基础角色：转换单行数据、聚合数据组，或者生成行对之间的关系。为了对这些复杂的AI工作负载进行系统性优化，作者团队推出了SAGE（Self-Adaptive Generative Execution，自适应生成式执行）框架。

SAGE是一个统一的逻辑与物理执行框架，其核心围绕三种强类型的原语（`AI_SCALAR`、`AI_AGG`和`AI_JOIN`）构建，并能够与标准的关系型操作符无缝组合。该框架采用置信度门控执行接口，并通过分析谓词、分解复合条件、利用配方卡（recipe card）及无标签探测（label-free probe）等技术来应对复杂的AI连接（AI joins），从而挑选出最优的物理执行策略。实验评估表明，SAGE不仅在SemBench基准测试中取得了优异的性能，还在可因式分解的连接（factorable joins）上将成对模型调用次数降低了两个数量级以上，实现了高达358倍的成本缩减。

---

## Summary

> Modern SQL systems are increasingly integrating AI capabilities to handle tasks such as classification, extraction, filtering, ranking, retrieval, joining, and summarization. Despite their diverse APIs, the paper observes that these functions reduce to three fundamental relational roles: **transforming individual rows**, **aggregating groups**, or **generating relationships between row pairs**. 
> 
> To optimize these workflows, the authors introduce **SAGE (Self-Adaptive Generative Execution)**, a unified logical and physical framework built around three typed primitives (`AI_SCALAR`, `AI_AGG`, and `AI_JOIN`) that integrate seamlessly with standard relational operators. SAGE utilizes a confidence-gated execution interface and addresses complex AI joins by analyzing predicates, decomposing compound conditions, and employing recipe cards with label-free probes to select optimal physical execution strategies. Evaluations show that SAGE achieves superior SemBench performance and reduces pairwise model calls by over two orders of magnitude on factorable joins, yielding a 358-fold measured cost reduction.

---

## Metadata

> * **arXiv ID:** [arXiv:2608.20630](https://arxiv.org/abs/2608.20630) [cs.AI]
> * **Submitted on:** August 21, 2026
> * **Authors:** Xiangqi Wang, Nhan H. Pham, Oktie Hassanzadeh, Dharmashankar Subramanian, Xiangliang Zhang
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **DOI:** [10.48550/arXiv.2608.20630](https://doi.org/10.48550/arXiv.2608.20630)
> * **License:** [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/)  
>   <img alt="license icon" role="presentation" src="./images/fb423b2203a9.png" width="30">

---

## Abstract

> SQL systems increasingly expose AI functions for tasks such as classification, extraction, filtering, ranking, retrieval, joining, and summarization. Despite their diverse APIs, these functions play only three relational roles: transforming individual rows, aggregating groups, or generating relationships between row pairs. We present SAGE (Self-Adaptive Generative Execution), a unified logical and physical framework that captures these roles with three typed primitives, `AI_SCALAR`, `AI_AGG`, and `AI_JOIN`, and composes them naturally with standard relational operators. All primitives share a confidence-gated execution interface while supporting physical strategies tailored to their relational shape. 
> 
> The main challenge is `AI_JOIN`, where SAGE analyzes the predicate, decomposes compound conditions when possible, and uses a recipe card together with a small label-free probe to select among complete execution strategies. Across a broad audit of public AI operators and evaluations spanning scalar, aggregate, and join workloads, this formulation covers common AI functionality while consistently improving execution quality and efficiency. SAGE achieves the strongest overall SemBench performance and, on a representative factorable join, reduces pairwise model calls by more than two orders of magnitude, yielding a 358-fold measured cost reduction.

---

## Access Full-Text & Resources

> * **PDF:** [View PDF](https://arxiv.org/pdf/2608.20630)
> * **HTML (Experimental):** [arXiv HTML Version](https://arxiv.org/html/2608.20630v1)
> * **TeX Source:** [Download Source](https://arxiv.org/src/2608.20630)
> * **Citations & References:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.20630)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.20630)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.20630)