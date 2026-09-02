---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- 6G
- 强化学习
- 决策Transformer
- 混合专家模型
- 无线网络优化
title: WiSDoM：面向多任务移动网络优化的基于混合专家模型的无线稀疏决策Transformer
---
### 文章背景与核心概要

随着新兴的 6G 无线网络向异构和动态部署场景发展，传统的无线资源管理（RRM）在规模化扩展上面临严峻挑战。网络拓扑、业务需求、用户移动性和无线信道条件的变化带来了相互冲突的优化目标。虽然离线强化学习（RL）提供了一种有前景的替代方案，但训练一个能够在各种环境中泛化单一策略仍然十分困难。

本文介绍了 **WiSDoM**（**Wireless Sparse Decision Transformer with Mixture-of-Experts**），这是一个专为自适应多小区选择（在协作多点传输 CoMP 中尤为有用）设计的稀疏多任务离线 RL 框架。通过将决策Transformer（DTs）与混合专家（MoE）架构相结合，WiSDoM 可以将任务动态路由至专门的专家模型。这种方法在不增加推理成本的前提下提高了模型容量，减轻了负迁移，并能够通过少样本提示（few-shot prompting）无缝泛化至未见过的无线场景。

---

# WiSDoM: Wireless Sparse Decision Transformer with Mixture-of-Experts for Multi-Task Mobile Network Optimization

## Metadata
* **Authors:** Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci
* **Subjects:** Networking and Internet Architecture (`cs.NI`); Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`)
* **Submitted On:** August 31, 2026
* **Identifier:** arXiv:2609.00284 [cs.NI]
* **License:** [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/)

---

## Executive Summary

As emerging 6G wireless networks move toward heterogeneous and dynamic deployment scenarios, traditional Radio Resource Management (RRM) struggles to scale. Variations in network topology, traffic demand, user mobility, and radio conditions create conflicting optimization objectives. While offline Reinforcement Learning (RL) presents a promising alternative, training a single policy that generalizes across diverse environments remains difficult. 

This paper introduces **WiSDoM** (**Wireless Sparse Decision Transformer with Mixture-of-Experts**), a sparse multi-task offline RL framework designed for adaptive multi-cell selection—particularly useful in coordinated multipoint (CoMP) transmission. By combining Decision Transformers (DTs) with a Mixture-of-Experts (MoE) architecture, WiSDoM dynamically routes tasks to specialized experts. This approach increases model capacity without inflating inference costs, mitigates negative transfer, and enables seamless generalization to unseen wireless scenarios via few-shot prompting.

>随着新兴的 6G 无线网络向异构和动态部署场景发展，传统的无线资源管理（RRM）在规模化扩展上面临严峻挑战。网络拓扑、业务需求、用户移动性和无线信道条件的变化带来了相互冲突的优化目标。虽然离线强化学习（RL）提供了一种有前景的替代方案，但训练一个能够在各种环境中泛化单一策略仍然十分困难。
>
>本文介绍了 **WiSDoM**（**Wireless Sparse Decision Transformer with Mixture-of-Experts**），这是一个专为自适应多小区选择（在协作多点传输 CoMP 中尤为有用）设计的稀疏多任务离线 RL 框架。通过将决策Transformer（DTs）与混合专家（MoE）架构相结合，WiSDoM 可以将任务动态路由至专门的专家模型。这种方法在不增加推理成本的前提下提高了模型容量，减轻了负迁移，并能够通过少样本提示（few-shot prompting）无缝泛化至未见过的无线场景。

---

## Key Highlights & Abstract

* **The Problem:** Conventional RRM and single-task RL policies fail to maintain consistent performance across heterogeneous wireless deployments due to conflicting objectives and limited model specialization, especially during sequential decision-making tasks like CoMP serving-cell selection.
* **The Solution:** WiSDoM integrates **Decision Transformers** with a sparse **Mixture-of-Experts (MoE)** backbone. It is trained jointly across diverse configurations (spanning base station densities, user equipment densities, mobility levels, and scheduler policies).
* **Key Performance Improvements:**
  * Boosts Quality of Experience (QoE) by **up to 55%** compared to heuristic methods, single-task models, and conventional multi-task DTs.
  * Achieves high efficiency by activating only **one-third of its total parameters** during inference relative to dense counterparts.
  * Demonstrates powerful **few-shot task generalization** to unseen wireless scenarios without requiring additional retraining or fine-tuning.

>## 核心亮点与摘要
>
>* **问题所在：** 由于目标冲突和模型专业化程度有限，传统的 RRM 和单任务 RL 策略无法在异构无线部署中保持一致的性能，在 CoMP 服务小区选择等序列决策任务中尤其明显。
>* **解决方案：** WiSDoM 将**决策Transformer**与稀疏的**混合专家（MoE）**骨干网相结合。它在各种配置（涵盖基站密度、用户设备密度、移动性水平和调度策略）下进行联合训练。
>* **关键性能提升：**
>  * 与启发式方法、单任务模型和传统多任务 DT 相比，体验质量（QoE）提升了**高达 55%**。
>  * 相比稠密对应模型，在推理过程中仅激活**总参数的三分之一**，实现了极高的效率。
>  * 展现出强大的**少样本任务泛化能力**，无需额外的重新训练或微调即可适应未见过的无线场景。

---

## Full-Text & Resources

* **View PDF:** [arXiv:2609.00284 PDF](https://arxiv.org/pdf/2609.00284)
* **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2609.00284v1)
* **Source Files:** [TeX Source](https://arxiv.org/src/2609.00284)
* **DOI:** [10.48550/arXiv.2609.00284](https://doi.org/10.48550/arXiv.2609.00284)

---

*(Note: Original article license icon representation preserved via markdown link structure where applicable.)*
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="display:none;">

>## 全文与资源
>
>* **查看 PDF：** [arXiv:2609.00284 PDF](https://arxiv.org/pdf/2609.00284)
>* **HTML 版本：** [arXiv HTML (实验性)](https://arxiv.org/html/2609.00284v1)
>* **源文件：** [TeX Source](https://arxiv.org/src/2609.00284)
>* **DOI：** [10.48550/arXiv.2609.00284](https://doi.org/10.48550/arXiv.2609.00284)
>
>---
>
>*(注：原文的许可证图标表现形式已在适用的情况下通过 Markdown 链接结构保留。)*
><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="display:none;">