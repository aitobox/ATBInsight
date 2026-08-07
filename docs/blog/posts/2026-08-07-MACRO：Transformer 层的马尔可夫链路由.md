---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-07
hide:
- navigation
tags:
- 大语言模型
- Transformer
- 动态路由
- 马尔可夫链
- 模型推理
title: MACRO：Transformer 层的马尔可夫链路由
---
### 文章背景与核心概要

标准大语言模型（LLM）通常按顺序执行各层，但动态层路由（允许层重复、跳过及其他架构路径）能够显著提升模型性能。传统的路由方法往往需要更新模型权重、在每个测试实例上运行昂贵的搜索循环，或者在推理阶段依赖真实标签，这限制了其在实际应用中的灵活性和效率。

为了克服这些局限性，本文提出了 **MACRO（Transformer 层的马尔可夫链路由）**。这是一个全新的框架，无需修改底层参数即可学习针对特定任务的 LLM 架构路由。MACRO 将层路由建模为一种上下文相关的马尔可夫策略，该策略基于层索引、计算预算阶段、方向位移和算子上下文进行条件化。它支持跳过、重复和残差隐藏状态加法操作。

通过在训练数据上的反馈更新马尔可夫路由分布，并使用 Top-k Viterbi 算法进行解码，MACRO 能够筛选出高概率的候选程序。在针对开源 LLM 的多项推理和知识基准测试中，MACRO 的平均准确率比未路由的基线模型提升了 **+5.0%**（在较小模型上增益最显著），并比现有的最先进动态路由方法 Dr. LLM 高出 **+7.2%**，同时将路由搜索时间缩短了 **9.4 倍**（从 14.8 小时降至 1.6 小时）。

---

## MACRO：Transformer 层的马尔可夫链路由

### 摘要

标准大语言模型（LLM）按顺序执行层，但动态层路由——允许层重复、跳过和其他架构路径——可以显著提高性能。传统的路由方法通常需要更新模型权重、为每个测试实例运行昂贵的搜索循环，或在推理过程中依赖真实标签。

> Standard Large Language Models (LLMs) execute layers sequentially, but dynamic layer routing—allowing for layer repetitions, skips, and other architectural paths—can significantly boost performance. Traditional routing approaches often require updating model weights, running expensive search loops per test instance, or relying on ground-truth labels during inference.

为了克服这些限制，**MACRO（Transformer 层的马尔可夫链路由）** 被引入作为一种新颖的框架，它可以在不修改底层参数的情况下学习 LLM 架构上的任务特定路由。MACRO 将层路由建模为一种上下文相关的马尔可夫策略，该策略以层索引、计算预算阶段、方向位移和算子上下文为条件。它支持跳过、重复和残差隐藏状态加法操作。马尔可夫路由分布通过训练数据的反馈进行更新，并使用 top-$k$ Viterbi 算法进行解码，以隔离高概率的候选程序。在开源 LLM 的各种推理和知识基准测试中，MACRO 在未路由基线的基础上实现了 **+5.0%** 的平均准确率提升（在较小模型上增益最大），并优于之前最先进的动态路由方法 Dr. LLM **+7.2%**，同时将路由搜索时间减少了 **9.4 倍**（从 14.8 小时减少到 1.6 小时）。

> To overcome these limitations, **MACRO (Markov Chain Routing of Transformer Layers)** is introduced as a novel framework that learns task-specific routes over LLM architectures without modifying the underlying parameters. MACRO models layer routing as a context-dependent Markov policy conditioned on layer indices, computation budget phases, directional displacements, and operator context. It supports skip, repeat, and residual hidden-state addition operations. The Markov route distribution is updated via feedback on training data and decoded using a top-$k$ Viterbi algorithm to isolate high-probability candidate programs. Evaluated across diverse reasoning and knowledge benchmarks on open-weight LLMs, MACRO achieves an average accuracy improvement of **+5.0%** over unrouted baselines (with the largest gains on smaller models) and outperforms the previous state-of-the-art dynamic routing approach, Dr. LLM, by **+7.2%**, all while reducing route-search time by **9.4x** (from 14.8 down to 1.6 hours).

---

## 元数据与出版详情

* **arXiv ID:** [arXiv:2608.05872](https://arxiv.org/abs/2608.05872) [cs.CL]
* **学科:** 计算与语言 (`cs.CL`); 人工智能 (`cs.AI`)
* **提交日期:** 2026年8月6日
* **DOI:** [10.48550/arXiv.2608.05872](https://doi.org/10.48550/arXiv.2608.05872)
* **作者:** 
  * Paweł Batorski
  * Abtin Pourhadi
  * Akylgali Aitaza
  * Przemysław Spurek
  * Paul Swoboda

> * **arXiv ID:** [arXiv:2608.05872](https://arxiv.org/abs/2608.05872) [cs.CL]
> * **Subjects:** Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`)
> * **Submission Date:** August 6, 2026
> * **DOI:** [10.48550/arXiv.2608.05872](https://doi.org/10.48550/arXiv.2608.05872)
> * **Authors:** 
>   * Paweł Batorski
>   * Abtin Pourhadi
>   * Akylgali Aitaza
>   * Przemysław Spurek
>   * Paul Swoboda

---

## 访问与资源

* **全文论文:** 
  * [查看 PDF](https://arxiv.org/pdf/2608.05872)
  * [HTML 版本 (实验性)](https://arxiv.org/html/2608.05872v1)
  * [TeX 源码](https://arxiv.org/src/2608.05872)
* **代码仓库:** [GitHub - Batorskq/MACRO](https://github.com/Batorskq/MACRO)
* **许可协议:** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/)

> * **Full-Text Papers:** 
>   * [View PDF](https://arxiv.org/pdf/2608.05872)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.05872v1)
>   * [TeX Source](https://arxiv.org/src/2608.05872)
> * **Code Repository:** [GitHub - Batorskq/MACRO](https://github.com/Batorskq/MACRO)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)

---

## 外部参考
* [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.05872)
* [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.05872)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.05872)

> * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.05872)
> * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.05872)
> * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.05872)

*(许可图标参考: <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">)*

> *(License Icon Reference: <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">)*