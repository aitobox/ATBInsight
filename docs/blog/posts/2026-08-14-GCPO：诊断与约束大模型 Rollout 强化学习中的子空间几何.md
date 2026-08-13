---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- 强化学习
- 大语言模型
- 策略优化
- 子空间几何
- GCPO
title: GCPO：诊断与约束大模型 Rollout 强化学习中的子空间几何
---
### 文章背景与核心概要
在大语言模型（LLM）的后训练阶段，诸如 **GRPO** 的同策略 Rollout 方法得到了广泛应用，但它们常常面临训练不稳定、跨任务能力退化以及回复长度膨胀（response-length inflation）等问题。本文深入研究了 Rollout 更新过程中子空间几何的逐步变化及其与模型性能之间的关系。作者引入了**主子空间重叠度（Principal-Subspace Overlap）**这一经过维度校正的指标，该指标揭示了重叠度的瞬时激增往往预示着性能的下降。

为了缓解这一问题，作者提出了 **GCPO（Geometrically Constrained Policy Optimization，几何约束策略优化）**，该方法应用硬双边正交投影，将更新限制在互补子空间内。在 Qwen3-8B 和 GLM4-9B 模型上，跨数学推理、代码生成和工具调用任务的评估表明，GCPO 在持续优于 GRPO、DAPO 和 GSPO 的同时，彻底消除了回复长度膨胀并稳定了策略熵。

---

## 📋 Summary
> On-policy rollout methods like **GRPO** are widely used for post-training large language models (LLMs), but they frequently encounter training instabilities, cross-task capability degradation, and response-length inflation. This paper investigates the stepwise variation of subspace geometry during rollout updates and its relationship to performance. The authors introduce **Principal-Subspace Overlap**—a dimension-corrected metric revealing that transient spikes in overlap often precede performance drops. To mitigate this, they propose **GCPO (Geometrically Constrained Policy Optimization)**, which applies hard bilateral orthogonal projections to restrict updates to complementary subspaces. Evaluated on Qwen3-8B and GLM4-9B across math reasoning, code generation, and tool-use tasks, GCPO consistently outperforms GRPO, DAPO, and GSPO while eliminating response-length inflation and stabilizing policy entropy.

---

## 📌 Document Metadata
> - **arXiv ID:** [arXiv:2608.11674](https://arxiv.org/abs/2608.11674) [cs.LG]
> - **Primary Subject:** Machine Learning (`cs.LG`), with cross-listing in Artificial Intelligence (`cs.AI`)
> - **Submission Date:** August 12, 2026
> - **Authors:** Kai Yang, Jingwei Xu, Wanyu Wang, Kai-Yuan Guo, Zhenbo Yu, Yi Wang, Yu Qiao
> - **Links:** 
>   - [View PDF](https://arxiv.org/pdf/2608.11674)
>   - [TeX Source](https://arxiv.org/src/2608.11674)
>   - [DOI](https://doi.org/10.48550/arXiv.2608.11674)

---

## 🔍 Abstract & Key Contributions
> * **The Problem:** While aggregate update geometries have been studied, stepwise variations and their direct link to rollout reinforcement learning (RL) instabilities in LLMs remain unclear.
> * **The Diagnostic Tool:** **Principal-Subspace Overlap**, which correlates transient overlap spikes with subsequent model performance degradation.
> * **The Solution (**`GCPO`**):** *Geometrically Constrained Policy Optimization*, applying hard bilateral orthogonal projections to prevent destabilizing parameter excursions by construction.
> * **Empirical Results:** 
>   - Improves over base models and strong baselines by up to **27.69 points** and **2.37 points**, respectively (tested on Qwen3-8B and GLM4-9B across math, coding, and tool-use benchmarks).
>   - Preserves general capabilities.
>   - Eliminates response-length inflation.
>   - Stabilizes policy entropy.