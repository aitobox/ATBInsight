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
- LoRA
- 扩散策略
- 边缘计算
- 无线通信
title: AirLLM：基于扩散策略的自适应 LoRA，用于大语言模型的无线远程微调
---
### 文章背景与核心概要
在边缘设备上运行大语言模型（LLM）往往受到通信带宽、计算能力以及内存的严重制约。虽然云端辅助的远程微调有助于缓解这些问题，但传统的低秩自适应（LoRA）方法依赖于固定或启发式的秩（rank）配置，从而导致低效的无线参数传输。

为了克服这些挑战，本文作者引入了 **AirLLM**，这是一个专为通信感知 LoRA 自适应而设计的层级扩散策略框架。AirLLM 将秩配置视为跨所有 LoRA 投影的结构化动作向量，并通过结合近端策略优化（PPO）智能体与去噪扩散隐式模型（DDIM），解决了由此产生的的高维连续决策问题。该框架能够有效适应不同的信噪比，在显著降低传输成本的同时提升微调性能。

---

## AirLLM: Diffusion Policy-based Adaptive LoRA for Remote Fine-Tuning of LLM over the Air

## 摘要 (Summary)
Operating Large Language Models (LLMs) on edge devices often suffers from severe constraints in communication bandwidth, computational capacity, and memory. While cloud-assisted remote fine-tuning helps alleviate this, traditional Low-Rank Adaptation (LoRA) methods rely on fixed or heuristic rank configurations, leading to inefficient over-the-air parameter transmission. 

> Operating Large Language Models (LLMs) on edge devices often suffers from severe constraints in communication bandwidth, computational capacity, and memory. While cloud-assisted remote fine-tuning helps alleviate this, traditional Low-Rank Adaptation (LoRA) methods rely on fixed or heuristic rank configurations, leading to inefficient over-the-air parameter transmission. 

To overcome these challenges, the authors introduce **AirLLM**, a hierarchical diffusion policy framework designed for communication-aware LoRA adaptation. AirLLM treats rank configuration as a structured action vector across all LoRA projections and solves the resulting high-dimensional sequential decision-making problem by combining a Proximal Policy Optimization (PPO) agent with Denoising Diffusion Implicit Models (DDIM). The framework effectively adapts to varying signal-to-noise ratios, enhancing fine-tuning performance while substantially lowering transmission costs.

> To overcome these challenges, the authors introduce **AirLLM**, a hierarchical diffusion policy framework designed for communication-aware LoRA adaptation. AirLLM treats rank configuration as a structured action vector across all LoRA projections and solves the resulting high-dimensional sequential decision-making problem by combining a Proximal Policy Optimization (PPO) agent with Denoising Diffusion Implicit Models (DDIM). The framework effectively adapts to varying signal-to-noise ratios, enhancing fine-tuning performance while substantially lowering transmission costs.

---

## 论文元数据 (Paper Metadata)

* **arXiv ID:** [arXiv:2507.11515](https://arxiv.org/abs/2507.11515) [cs.LG]
* **研究领域 (Subjects):** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`)
* **作者 (Authors):** Shiyi Yang, Xiaoxue Yu, Rongpeng Li, Jianhang Zhu, Zhifeng Zhao, Honggang Zhang
* **提交日期 (Submission Date):** 2025年7月15日（最近修订：2026年8月27日）
* **篇幅长度 (Length):** 11 页，8 个图表
* **DOI:** [10.48550/arXiv.2507.11515](https://doi.org/10.48550/arXiv.2507.11515)

---

## 摘要原文 (Abstract)

在边缘设备上运行大语言模型（LLMs）日益面临着通信带宽有限以及计算和内存成本紧张的挑战。因此，云端辅助的远程微调变得不可或缺。然而，现有的低秩自适应（LoRA）方法通常采用固定或启发式的秩配置，随后对所有 LoRA 参数进行无线传输可能会相当低效。

> Operating Large Language Models (LLMs) on edge devices is increasingly challenged by limited communication bandwidth and strained computational and memory costs. Thus, cloud-assisted remote fine-tuning becomes indispensable. Nevertheless, existing Low-Rank Adaptation (LoRA) approaches typically employ fixed or heuristic rank configurations, and the subsequent over-the-air transmission of all LoRA parameters could be rather inefficient. 

为了解决这一局限性，我们开发了 **AirLLM**，这是一个用于通信感知 LoRA 自适应的层级扩散策略框架。具体而言，AirLLM 将秩配置建模为一个跨越所有嵌入 LoRA 投影的结构化动作向量。为了解决底层的高维连续决策问题，**近端策略优化（PPO）** 智能体通过联合观察无线状态和语言复杂度来生成粗粒度决策，然后通过 **去噪扩散隐式模型（DDIM）** 对其进行精细化，以产生高分辨率、任务和信道自适应的秩向量。这两个模块交替优化，其中 DDIM 在 **无分类器引导（CFG）** 范式下进行训练，以保持与 PPO 奖励的一致性。

> To address this limitation, we develop **AirLLM**, a hierarchical diffusion policy framework for communication-aware LoRA adaptation. Specifically, AirLLM models the rank configuration as a structured action vector that spans all LoRA-inserted projections. To solve the underlying high-dimensional sequential decision-making problem, a **Proximal Policy Optimization (PPO)** agent generates coarse-grained decisions by jointly observing wireless states and linguistic complexity, which are then refined via **Denoising Diffusion Implicit Models (DDIM)** to produce high-resolution, task- and channel-adaptive rank vectors. The two modules are optimized alternatively, with the DDIM trained under the **Classifier-Free Guidance (CFG)** paradigm to maintain alignment with PPO rewards. 

在不同信噪比下的实验表明，AirLLM 持续提升了微调性能，同时显著降低了传输成本，突显了强化驱动、扩散精细化的秩自适应在实现可扩展且高效的无线远程微调方面的有效性。

> Experiments under varying signal-to-noise ratios demonstrate that AirLLM consistently enhances fine-tuning performance while significantly reducing transmission costs, highlighting the effectiveness of reinforcement-driven, diffusion-refined rank adaptation for scalable and efficient remote fine-tuning over the air.

---

## 全文及访问链接 (Full-Text & Access Links)

* [在 arXiv 上查看 PDF](https://arxiv.org/pdf/2507.11515)
* [实验性 HTML 版本](https://arxiv.org/html/2507.11515v2)
* [TeX 源文件](https://arxiv.org/src/2507.11515)
* [NASA ADS 参考](https://ui.adsabs.harvard.edu/abs/arXiv:2507.11515)
* [Google 学术搜索](https://scholar.google.com/scholar_lookup?arxiv_id=2507.11515)
* [Semantic Scholar API](https://api.semanticscholar.org/arXiv:2507.11515)