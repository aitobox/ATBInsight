---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-11
hide:
- navigation
tags:
- LLM Agent
- 强化学习
- 信用分配
- Gated-BEPO
- 贝尔曼方程
title: Gated-BEPO：面向大语言模型智能体的置信门控贝尔曼信用分配
---
### 文章背景与核心概要

在长程任务环境中训练大语言模型（LLM）智能体时，如何将稀疏的最终结果有效地分配给各个动作是一个核心难题。现有的无评论家（Critic-free）方法往往将轨迹级奖励均匀分配，无法区分成功轨迹中的无效动作或失败轨迹中的关键步骤；而状态匹配方法虽然能构建步骤级分组，但过度依赖直接的轨迹结果，且融合方式过于僵化。

为了解决这些挑战，本文提出了 **Gated-BEPO**。该方法通过均值备份贝尔曼不动点估计节点价值，从而从经验回放图中推导出细粒度的步骤级信用。通过利用广义优势估计（GAE）累积时序差分残差，Gated-BEPO 能够同时捕捉动作的即时影响与后续后果。

此外，该研究引入了一个“置信门控”（Confidence Gate）机制，用于自适应地融合片段级与步骤级信用。该机制仅在观测到多个后继状态时采用贝尔曼信用，而在其他情况下回退至片段级信用，从而在复杂决策环境中实现了更稳健的性能提升。

---

## 摘要

> Training Large Language Model (LLM) agents in long-horizon environments requires effectively distributing sparse terminal outcomes back to individual actions. Current approaches face distinct limitations:
> * **Critic-free methods** propagate trajectory-level rewards uniformly across all steps, failing to distinguish useful actions in failed trajectories from ineffective actions in successful ones.
> * **State-matching methods** construct step-level groups and compare actions directly, but rely heavily on direct trajectory outcomes and rigid, fixed-weight fusions with episode-level credit.
>
> To overcome these challenges, the authors introduce **Gated-BEPO**. This approach derives granular step-level credit directly from empirical rollout graphs by estimating node values through a mean-backup Bellman fixed point. By accumulating temporal-difference residuals along sampled trajectories using generalized advantage estimation, Gated-BEPO captures both immediate and downstream consequences. 
>
> Furthermore, to adaptively fuse episode- and step-level credit, a **confidence gate** incorporates Bellman credit exclusively at states possessing multiple observed successors, falling back to episode-level credit otherwise.

在长程环境中训练大语言模型（LLM）智能体，需要将稀疏的终端结果有效地分配给各个动作。当前的方法面临明显的局限性：
* **无评论家（Critic-free）方法**将轨迹级奖励均匀地传播到所有步骤，无法区分失败轨迹中的有用动作与成功轨迹中的无效动作。
* **状态匹配方法**构建步骤级分组并直接比较动作，但严重依赖直接的轨迹结果，且与片段级信用的融合方式僵化且权重固定。

为了克服这些挑战，作者引入了 **Gated-BEPO**。该方法通过均值备份贝尔曼不动点估计节点价值，直接从经验回放图中导出细粒度的步骤级信用。通过使用广义优势估计沿采样轨迹累积时序差分残差，Gated-BEPO 能够捕捉即时后果和后续影响。

此外，为了自适应地融合片段级和步骤级信用，**置信门控（Confidence Gate）**仅在拥有多个观测后继状态的状态下纳入贝尔曼信用，否则回退到片段级信用。

---

## 核心贡献

> * **Empirical Rollout Graphs & Bellman Estimation:** Constructs empirical graphs for rollout groups and estimates node values using a mean-backup Bellman fixed point reflective of the current policy's empirical action distribution.
> * **Step-Level Bellman Advantages:** Accumulates temporal-difference residuals via generalized advantage estimation to capture immediate and downstream effects.
> * **Adaptive Confidence Gate:** Selectively blends step-level and episode-level credit based on state transition certainty (using Bellman credit only when multiple successors are observed).
> * **Robust Performance:** Demonstrates consistent improvements across both language and vision-language models on challenging benchmarks including WebShop, ALFWorld, and visual Sokoban.

* **经验回放图与贝尔曼估计：** 为回放组构建经验图，并使用反映当前策略经验动作分布的均值备份贝尔曼不动点来估计节点价值。
* **步骤级贝尔曼优势：** 通过广义优势估计累积时序差分残差，以捕捉即时和后续影响。
* **自适应置信门控：** 基于状态转移确定性选择性地混合步骤级和片段级信用（仅在观测到多个后继状态时使用贝尔曼信用）。
* **稳健的性能：** 在 WebShop、ALFWorld 和视觉 Sokoban 等具有挑战性的基准测试中，证明了在语言模型和视觉语言模型上的一致性改进。

---

## 全文与资源

> * [View PDF](https://arxiv.org/pdf/2608.06861)
> * [arXiv HTML (Experimental)](https://arxiv.org/html/2608.06861v1)
> * [TeX Source](https://arxiv.org/src/2608.06861)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) *(License icon preserved below)*

* [查看 PDF](https://arxiv.org/pdf/2608.06861)
* [arXiv HTML (实验性)](https://arxiv.org/html/2608.06861v1)
* [TeX 源码](https://arxiv.org/src/2608.06861)
* **许可协议：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) *(许可图标保留如下)*

![license icon](https://arxiv.org/pdf/2608.06861)
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">