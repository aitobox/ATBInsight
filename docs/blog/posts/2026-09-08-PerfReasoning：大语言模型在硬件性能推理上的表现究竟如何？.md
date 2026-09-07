---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-08
hide:
- navigation
tags:
- 大语言模型
- 硬件性能
- 性能建模
- 基准测试
- 人工智能
title: PerfReasoning：大语言模型在硬件性能推理上的表现究竟如何？
---
### 文章背景与核心概要

性能建模是硬件设计和软件优化的核心环节，但构建这些模型需要对计算、数据重用、存储和数据移动进行结构化的推理。本文介绍了 **PerfReasoning**，这是一个全新的基准测试，旨在评估大语言模型（LLM）在硬件性能建模方面的能力——特别测试它们作为直接性能推理器以及分析型性能模型代码生成器的表现。

研究表明，在直接推理问答（Reasoning Q&A）任务中，最强的闭源模型准确率超过了 **90%**，而最佳开源权重模型达到了 **82.4%**。然而，构建性能模型代码则要困难得多：尽管 GPT-5.6 Sol 的通过率超过了 **80%**，但所有其他模型配置的平均通过率均低于 **15%**，且多次运行之间的表现波动显著。该基准测试揭示了表面上合理的架构推理与可靠的性能模型构建之间存在着巨大的差距。

---

## 摘要 (Abstract)

> Performance modeling is central to hardware design and software optimization, yet constructing these models requires structured reasoning about computation, data reuse, storage, and movement. We introduce **PerfReasoning**, a benchmark that evaluates LLMs both as direct performance reasoners and as generators of analytical performance-model code. 

性能建模是硬件设计和软件优化的核心，然而构建这些模型需要对计算、数据重用、存储和移动进行结构化推理。我们推出了 **PerfReasoning**，这是一个用于评估大语言模型（LLM）作为直接性能推理器和分析型性能模型代码生成器能力的基准测试。

> Given workload, architecture, and mapping specifications, models compare mappings and predict off-chip traffic and buffer requirements:
* **Reasoning Q&A:** The strongest closed-source models exceed **90%** accuracy, while the best open-weight model reaches **82.4%**.
* **Model Construction:** Constructing performance-model code is substantially harder. While GPT-5.6 Sol exceeds an **80%** pass rate, all other model configurations average below **15%** and vary markedly across runs.
* **Prompting & RL:** Task-specific reinforcement learning (RL) raises a 4B model's mapping-reasoning accuracy by **15.7 points**, whereas feedback-free multi-round self-revision prompting is not reliably effective.

给定工作负载、架构和映射规范，模型需要比较映射并预测片外流量和缓冲区需求：
* **推理问答：** 最强的闭源模型准确率超过 **90%**，而最佳开源权重模型达到 **82.4%**。
* **模型构建：** 构建性能模型代码要困难得多。虽然 GPT-5.6 Sol 的通过率超过 **80%**，但所有其他模型配置的平均通过率低于 **15%**，且在不同运行之间存在显著差异。
* **提示词与强化学习：** 针对特定任务的强化学习（RL）使 4B 模型的映射推理准确率提高了 **15.7 个百分点**，而无反馈的多轮自我修正提示并没有稳定的效果。

> PerfReasoning exposes the critical gap between plausible architectural reasoning and reliable performance-model construction. The authors plan to publicly release the benchmark to support reproducible evaluation and track future progress.

PerfReasoning 揭示了表面上合理的架构推理与可靠的性能模型构建之间的关键差距。作者计划公开该基准测试，以支持可复现的评估并追踪未来的进展。

---

## 链接与资源 (Links and Resources)

> * **arXiv:** [arXiv:2609.04476](https://arxiv.org/abs/2609.04476)
* **DOI:** [10.48550/arXiv.2609.04476](https://doi.org/10.48550/arXiv.2609.04476)
* **Access Full-Text:** 
  * [View PDF](https://arxiv.org/pdf/2609.04476)
  * [HTML Version (Experimental)](https://arxiv.org/html/2609.04476v1)
  * [TeX Source](https://arxiv.org/src/2609.04476)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" />

* **arXiv 预印本：** [arXiv:2609.04476](https://arxiv.org/abs/2609.04476)
* **DOI 链接：** [10.48550/arXiv.2609.04476](https://doi.org/10.48550/arXiv.2609.04476)
* **访问全文：** 
  * [查看 PDF](https://arxiv.org/pdf/2609.04476)
  * [HTML 版本（实验性）](https://arxiv.org/html/2609.04476v1)
  * [TeX 源码](https://arxiv.org/src/2609.04476)
* **许可协议：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" />