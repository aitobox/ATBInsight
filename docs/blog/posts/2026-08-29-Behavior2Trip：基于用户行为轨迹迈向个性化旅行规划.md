---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 旅行规划
- 用户行为轨迹
- 智能体
- 强化学习
- 大语言模型
title: Behavior2Trip：基于用户行为轨迹迈向个性化旅行规划
---
### 文章背景与核心概要
当前的旅行规划智能体通常依赖显式的用户指令或多轮交互澄清来理解用户偏好。然而，这些方法忽略了隐藏在用户过去在线行为中的丰富潜在偏好信号。为了克服这一局限性，本文作者引入了一项名为“行为感知旅行规划”（Behavior-Aware Travel Planning）的新任务，直接从过去的行为轨迹中推断用户偏好。

与此任务并行，作者推出了 **Behavior2Trip**，这是一个源自中国领先在线旅游平台的大规模基准测试，包含 11,400 个实例。他们还提出了 **B2T-Agent**，这是一个基于强化学习的模型，利用用户行为轨迹、外部检索工具和内部记忆模块，以实现卓越、高度个性化的旅行行程规划。该论文已被 EMNLP 2026 Findings 接受。

---

# Behavior2Trip：基于用户行为轨迹迈向个性化旅行规划

> **arXiv:** [arXiv:2608.26807 [cs.CL]]  
> **Authors:** Zihao Cheng, Yingyu Shan, Hongru Wang, Zeming Liu, Xinyi Wang, Xiangrong Zhu, Yuhang Guo, Wei Lin, Yunhong Wang  
> **Venue:** Accepted by EMNLP 2026 Findings  
> **Links:** [View PDF](https://arxiv.org/pdf/2608.26807) | [GitHub Repository](https://github.com/BUAA-IRIP-LLM/Behavior2Trip)

---

## 📌 摘要

当前的旅行规划智能体通常依赖显式的用户指令或多轮交互澄清来理解用户偏好。然而，这些方法忽略了隐藏在用户过去在线行为中的丰富潜在偏好信号。

> Current travel planning agents typically rely on explicit user instructions or interactive multi-turn clarifications to understand user preferences. However, these methods ignore the rich, latent preference signals hidden within users' past online behaviors. 

为了克服这一局限性，作者引入了一项名为**行为感知旅行规划**（Behavior-Aware Travel Planning）的新任务，该任务直接从过去的行为轨迹中推断用户偏好。伴随该任务，他们推出了 **Behavior2Trip**，这是一个源自中国领先在线旅游平台的大规模基准测试，包含 11,400 个实例。他们还提出了 **B2T-Agent**，这是一个基于强化学习的模型，利用用户行为轨迹、外部检索工具和内部记忆模块，从而实现卓越且高度个性化的旅行行程规划。

> To overcome this limitation, the authors introduce a novel task called **Behavior-Aware Travel Planning**, which infers user preferences directly from past behavioral trajectories. Alongside this task, they present **Behavior2Trip**, a large-scale benchmark derived from a leading Chinese online travel platform containing 11,400 instances. They also propose **B2T-Agent**, a reinforcement learning-based model that utilizes user behavior trajectories, external retrieval tools, and an internal memory module to achieve superior, highly personalized travel itineraries.

---

## 📋 核心细节

* **基准规模：** 11,400 个实例。
* **实例特征：** 每个实例平均包含 39.8 条过去的用户行为，横跨 5 个偏好维度下的 14 个属性。
* **提出方法：** **B2T-Agent**（一个基于强化学习的智能体，利用用户行为轨迹、工具增强的偏好检索以及内部记忆）。
* **主要发现：**
  * GPT-4.1 在 Behavior2Trip 最难的任务上，全约束通过率仅为 0.5%，凸显了基于行为规划的复杂性。
  * 由 **B2T-Agent** 驱动的 Qwen3-8B 模型在 Behavior2Trip 上表现优于所有基线模型，甚至在 TravelPlanner 基准测试中超越了 GPT-4.1，证明了其强大的泛化能力。

> * **Benchmark Size:** 11,400 instances.
> * **Instance Characteristics:** Each instance averages 39.8 past user behaviors spanning 14 attributes across 5 preference dimensions.
> * **Proposed Approach:** **B2T-Agent** (a reinforcement learning-based agent leveraging user behavior trajectories, tool-augmented preference retrieval, and internal memory).
> * **Key Findings:** 
>   * GPT-4.1 achieves a full-constraint pass rate of only 0.5% on the hardest tasks of Behavior2Trip, highlighting the complexity of behavioral-based planning.
>   * The Qwen3-8B model powered by **B2T-Agent** outperforms all baselines on Behavior2Trip and even surpasses GPT-4.1 on the TravelPlanner benchmark, proving strong generalization capabilities.