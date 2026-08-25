---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 长期记忆管理
- 强化学习
- 条件互信息
- AI智能体
- 模型泛化
title: CMI-Mem：通过CMI增强强化学习实现具备泛化能力的长期记忆管理
---
### 文章背景与核心概要
在现代AI智能体（Agent）系统中，记忆管理器是核心组件之一。传统的强化学习（RL）方法通常依赖大语言模型（LLM）评估生成的合成问答（QA）对来进行训练。虽然这种方法提供了有用的下游任务支撑，但它本质上将记忆的价值评估局限于特定的采样查询分布和固定的阅读器上。

为了突破这些局限性，作者提出了 **CMI-Mem**，这是一个轻量级的强化学习记忆管理器，由一种新颖的混合奖励机制驱动：1）外部QA项，用于衡量端到端任务的正确性；2）内在条件互信息（CMI）项，用于评估新对话输入相对于现有记忆状态的信息贡献，而无需依赖采样的QA查询。这两种信号协同工作：QA组件锚定整体任务效用，而CMI组件则提供构建相关且无冗余记忆所需的细粒度、逐操作监督。实验结果表明，CMI-Mem显着提高了其在各种记忆使用场景中的泛化能力，同时增强了训练和推理的效率。

---

* **Authors:** Yubo Wang, Qiuyu Zhao, Zenghui Sun, Shichao Dong, Jinsong Lan, Xiaoyong Zhu, Haoyang Li, Bo Zheng, Lei Chen  
* **Primary Subject:** Artificial Intelligence (`cs.AI`)  
* **Secondary Subject:** Computation and Language (`cs.CL`)  
* **arXiv ID:** [arXiv:2607.20553 [cs.AI]](https://arxiv.org/abs/2607.20553)  
* **Submission Date:** 15 Jul 2026 (Last revised: 22 Aug 2026)  
* **Resources:** 
  * [GitHub Repository](https://github.com/Wyb0627/CMIMem)  
  * [Model Checkpoint (CMI-Mem-4B)](https://www.modelscope.cn/models/wyb0627/CMIMem-4B)  
  * [View PDF](https://arxiv.org/pdf/2607.20553)

> * **Authors:** Yubo Wang, Qiuyu Zhao, Zenghui Sun, Shichao Dong, Jinsong Lan, Xiaoyong Zhu, Haoyang Li, Bo Zheng, Lei Chen  
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)  
> * **Secondary Subject:** Computation and Language (`cs.CL`)  
> * **arXiv ID:** [arXiv:2607.20553 [cs.AI]](https://arxiv.org/abs/2607.20553)  
> * **Submission Date:** 15 Jul 2026 (Last revised: 22 Aug 2026)  
> * **Resources:** 
>   * [GitHub Repository](https://github.com/Wyb0627/CMIMem)  
>   * [Model Checkpoint (CMI-Mem-4B)](https://www.modelscope.cn/models/wyb0627/CMIMem-4B)  
>   * [View PDF](https://arxiv.org/pdf/2607.20553)

---

## Summary

记忆管理器模型是现代AI智能体系统中的关键组件。传统的强化学习（RL）方法通常依赖于大模型评判的合成问答（QA）对进行训练。虽然这提供了有用的下游任务扎根性，但它从根本上将记忆价值评估限制在了特定的采样查询分布和固定的阅读器上。

为了克服这些局限性，作者提出了 **CMI-Mem**，这是一个由新颖的混合奖励机制驱动的轻量级RL记忆管理器：
1. **外部QA项（Extrinsic QA Term）：** 衡量端到端任务的正确性。
2. **内在条件互信息（CMI）项（Intrinsic Conditional Mutual Information (CMI) Term）：** 评估新对话输入相对于现有记忆状态的信息贡献，而无需以采样的QA查询为条件。

这两个信号协同运作：QA组件锚定了整体任务效用，而CMI组件则提供了构建相关且非冗余记忆所需的细粒度、逐操作监督。实验结果表明，CMI-Mem显著提升了其在多样化记忆使用场景中的泛化能力，同时增强了训练和推理的效率。

> ## Summary
> 
> Memory manager models are critical components in modern AI agent systems. Traditional reinforcement learning (RL) approaches typically rely on LLM-judged synthetic question-answer (QA) pairs for training. While this offers useful downstream task grounding, it fundamentally limits memory valuation to a specific sampled query distribution and a fixed reader. 
> 
> To overcome these limitations, the authors propose **CMI-Mem**, a lightweight RL memory manager powered by a novel hybrid reward mechanism:
> 1. **Extrinsic QA Term:** Measures end-task correctness.
> 2. **Intrinsic Conditional Mutual Information (CMI) Term:** Evaluates the informational contribution of new conversational inputs relative to the existing memory state, without needing to condition on a sampled QA query.
> 
> These two signals operate synergistically: the QA component anchors overall task utility, while the CMI component delivers fine-grained, per-operation supervision necessary for constructing relevant and non-redundant memories. Experimental results demonstrate that CMI-Mem significantly improves generalizability across diverse memory-use scenarios while enhancing both training and inference efficiency.