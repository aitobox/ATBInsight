---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- Deep Research
- 强化学习
- 规划能力
- 大语言模型
- 优势塑造
title: DeepPlanner：通过优势塑造扩展深度研究智能体的规划能力
---
### 文章背景与核心概要
大语言模型（LLM）在结合多步推理和外部工具调用能力后，在处理长周期任务时表现出卓越的性能。然而，现有的优化策略要么依赖隐式的推理阶段，要么引入了显式规划但缺乏恰当的优化机制。在朴素强化学习（RL）下，规划词元（tokens）往往表现出异常高的熵，这突显了关键且未得到充分优化的决策点。

为了解决这一问题，**DeepPlanner** 提出了一种端到端的强化学习框架，旨在显著提升深度研究智能体的规划能力。通过引入词元级的优势塑造机制（利用基于熵的项为高熵词元分配更大的更新幅度），并结合对规划密集型推理轨迹（rollouts）的有选择性的样本级加权，DeepPlanner 大幅提升了规划质量，并在降低训练预算的同时实现了最先进（SOTA）的性能。

---

## DeepPlanner: Scaling Planning Capability for Deep Research Agents via Advantage Shaping

## Summary

> Large language models (LLMs) enhanced with multi-step reasoning and external tool usage excel at long-horizon tasks. However, current optimization strategies either rely on implicit reasoning stages or introduce explicit planning without proper optimization. Under vanilla reinforcement learning (RL), planning tokens exhibit unusually high entropy, highlighting critical under-optimized decision points. 
> 
> To overcome this, **DeepPlanner** introduces an end-to-end RL framework that boosts the planning capabilities of deep research agents. By implementing token-level advantage shaping (using an entropy-based term to assign larger updates to high-entropy tokens) alongside selective sample-level upweighting for planning-intensive rollouts, DeepPlanner significantly improves planning quality and achieves state-of-the-art results with a reduced training budget.

---

## 论文元数据 (Paper Metadata)

> * **arXiv ID:** [arXiv:2510.12979](https://arxiv.org/abs/2510.12979) [cs.AI]
> * **Accepted At:** ACL 2026
> * **Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`)
> * **Submission History:** 
>   * [v1] Tue, 14 Oct 2025
>   * [v2] Thu, 27 Aug 2026 (this version)
> * **DOI:** [10.48550/arXiv.2510.12979](https://doi.org/10.48550/arXiv.2510.12979)

---

## 作者 (Authors)

> * Wei Fan
> * Wenlin Yao
> * Zheng Li
> * Feng Yao
> * Xin Liu
> * Liang Qiu
> * Qingyu Yin
> * Yangqiu Song
> * Bing Yin

---

## 摘要 (Abstract)

> Large language models (LLMs) augmented with multi-step reasoning and action generation abilities have shown promise in leveraging external tools to tackle complex tasks that require long-horizon planning. However, existing approaches either rely on implicit planning in the reasoning stage or introduce explicit planners without systematically addressing how to optimize the planning stage. As evidence, we observe that under vanilla reinforcement learning (RL), planning tokens exhibit significantly higher entropy than other action tokens, revealing uncertain decision points that remain under-optimized. To address this, we propose DeepPlanner, an end-to-end RL framework that effectively enhances the planning capabilities of deep research agents. Our approach shapes token-level advantage with an entropy-based term to allocate larger updates to high entropy tokens, and selectively upweights sample-level advantages for planning-intensive rollouts. Extensive experiments across seven deep research benchmarks demonstrate that DeepPlanner improves planning quality and achieves state-of-the-art results under a substantially lower training budget.

---

## 全文与资源 (Full-Text & Resources)

> * **PDF:** [View PDF](https://arxiv.org/pdf/2510.12979)
> * **HTML (Experimental):** [arXiv HTML Version](https://arxiv.org/html/2510.12979v2)
> * **Source Code / TeX:** [TeX Source](https://arxiv.src/2510.12979)
> * **External Citations & Tools:**
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2510.12979)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2510.12979)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2510.12979)