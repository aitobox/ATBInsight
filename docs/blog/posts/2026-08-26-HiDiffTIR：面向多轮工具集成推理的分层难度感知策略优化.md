---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 大语言模型
- 强化学习
- 工具集成推理
- 策略优化
- 难度感知
title: HiDiffTIR：面向多轮工具集成推理的分层难度感知策略优化
---
### 文章背景与核心概要
本文介绍了 **HiDiffTIR**，这是一种专为大语言模型（LLM）的多轮工具集成推理（TIR）而设计的全新强化学习框架。传统的强化学习方法通常分配统一的轨迹级优势，并平等对待所有正确的工具调用，从而忽略了单个推理步骤和轨迹的动态难度。

为了克服这一局限性，**HiDiffTIR** 在**轨迹**和**轮次（turn）**两个层面上应用了细粒度的、分层的难度感知信用分配机制。它引导策略智能体专注于更具信息量的轨迹和更具挑战性的推理步骤，而无需任何额外的监督，完全依赖于从标准强化学习 Rollout 中派生出的群体级统计数据。广泛的基准测试证实，与现有的强化学习基线相比，HiDiffTIR 始终能够提升性能和工具调用准确率。

---

## HiDiffTIR：面向多轮工具集成推理的分层难度感知策略优化

> ## HiDiffTIR: Hierarchical Difficulty-Aware Policy Optimization for Multi-Turn Tool-Integrated Reasoning

## 概要

**HiDiffTIR** 引入了一种新颖的强化学习框架，用于大语言模型（LLM）中的多轮工具集成推理（TIR）。传统的强化学习方法通常分配统一的轨迹级优势，并平等对待所有正确的工具调用，忽略了个体推理步骤和轨迹的动态难度。

为了克服这一问题，**HiDiffTIR** 在**轨迹**和**轮次**两个层面上应用了细粒度的、分层的难度感知信用分配。这引导策略智能体专注于更具信息量的轨迹和更具挑战性的推理步骤，而无需任何额外的监督——完全依赖于从标准强化学习 rollout 中派生出的群体级统计数据。广泛的基准测试证实，HiDiffTIR 在性能和工具调用准确率上均持续超越了现有的强化学习基线。

> ## Summary
> 
> **HiDiffTIR** introduces a novel reinforcement learning framework for Multi-Turn Tool-Integrated Reasoning (TIR) in Large Language Models (LLMs). Traditional RL approaches typically assign uniform trajectory-level advantages and treat all correct tool calls equally, ignoring the dynamic difficulty of individual reasoning steps and trajectories. 
> 
> To overcome this, **HiDiffTIR** applies a fine-grained, hierarchical difficulty-aware credit assignment at both the **trajectory** and **turn** levels. This guides the policy agent to concentrate on more informative trajectories and challenging reasoning steps without requiring any extra supervision—relying exclusively on group-level statistics derived from standard RL rollouts. Extensive benchmarking confirms that HiDiffTIR consistently improves performance and tool-invocation accuracy over established RL baselines.

---

## 论文元数据

* **arXiv ID:** [arXiv:2608.21863](https://arxiv.org/abs/2608.21863) [cs.CL]
* **作者:** Yucan Guo, Xiaohan Wang, Miao Su, Saiping Guan, Zhongni Hou, Jiajun Chai, Wei Lin, Guojun Yin, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
* **提交日期:** 2026年8月22日
* **录用会议:** 已被 **EMNLP 2026 (Findings)** 录用
* **主学科:** 计算与语言 (`cs.CL`)
* **辅学科:** 人工智能 (`cs.AI`)

> ## Paper Metadata
> 
> * **arXiv ID:** [arXiv:2608.21863](https://arxiv.org/abs/2608.21863) [cs.CL]
> * **Authors:** Yucan Guo, Xiaohan Wang, Miao Su, Saiping Guan, Zhongni Hou, Jiajun Chai, Wei Lin, Guojun Yin, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
> * **Submission Date:** August 22, 2026
> * **Venue:** Accepted by **EMNLP 2026 (Findings)**
> * **Primary Subject:** Computation and Language (`cs.CL`)
> * **Secondary Subject:** Artificial Intelligence (`cs.AI`)

---

## 摘要

工具集成推理（TIR）是 LLM 智能体通过与外部工具进行迭代交互来解决复杂任务的基本能力。强化学习（RL）已成为实现这一能力的主导范式。然而，现有方法通常分配统一的轨迹级优势，并平等对待所有正确的工具调用，忽略了不同轨迹和推理步骤之间差异化的难度与学习价值。这可能导致学习信号不够精准，无法充分区分平庸和具有挑战性的工具使用模式。

为了解决这一局限性，我们提出了 **HiDiffTIR**，这是一种用于多轮 TIR 的分层难度感知策略优化框架。HiDiffTIR 在轨迹和轮次两个层面上执行难度感知信用分配，使策略能够专注于信息量更丰富的轨迹和更困难的推理步骤。值得注意的是，这种细粒度的优化无需额外的监督，仅依赖于从标准强化学习 rollout 中派生出的群体级统计数据。在三个工具使用基准上进行的广泛实验表明，与强强化学习基线相比，HiDiffTIR 持续提高了多轮 TIR 的性能和工具调用准确率，凸显了难度感知信用分配对于工具集成 LLM 智能体进行有效策略优化的必要性。

> ## Abstract
> 
> Tool-Integrated Reasoning (TIR) is a fundamental capability for LLM agents to solve complex tasks by interacting with external tools iteratively. Reinforcement Learning (RL) has become the dominant paradigm for enabling this capability. However, existing approaches typically assign uniform trajectory-level advantages and treat all correct tool calls equally, ignoring the varying difficulty and learning value across trajectories and reasoning steps. This can lead to imprecise learning signals that do not adequately distinguish between trivial and challenging tool-use patterns. 
> 
> To address this limitation, we propose **HiDiffTIR**, a Hierarchical Difficulty-aware policy optimization framework for multi-turn TIR. HiDiffTIR performs difficulty-aware credit assignment at both trajectory and turn levels, enabling the policy to focus on more informative trajectories and harder reasoning steps. Notably, this fine-grained optimization is achieved without additional supervision, relying solely on group-level statistics derived from standard RL rollouts. Extensive experiments on three tool-using benchmarks demonstrate that HiDiffTIR consistently improves multi-turn TIR performance and tool invocation accuracy over strong RL baselines, highlighting the necessity of difficulty-aware credit assignment for effective policy optimization in tool-integrated LLM agents.

---

## 快速链接与资源

* **全文访问:** [查看 PDF](https://arxiv.org/pdf/2608.21863) | [HTML 版本](https://arxiv.org/html/2608.21863v1) | [TeX 源码](https://arxiv.org/src/2608.21863)
* **外部引用与工具:** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.21863)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.21863)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.21863)

> ## Quick Links & Resources
> 
> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.21863) | [HTML Version](https://arxiv.org/html/2608.21863v1) | [TeX Source](https://arxiv.org/src/2608.21863)
> * **External Citations & Tools:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.21863)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.21863)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.21863)