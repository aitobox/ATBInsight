---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-12
hide:
- navigation
tags:
- 视频预测
- 世界模型
- 交通视频
- LoRA
- AI City Challenge
title: CosmosAlign：适配世界基础模型以实现生成式交通视频预测
---
### 文章背景与核心概要
生成式交通视频预测旨在根据短期的观察历史和文本描述，合成具有时间连贯性的长视野交通场景未来视频。随着大型世界基础模型（如 NVIDIA Cosmos 系列）的兴起，如何将这些通用模型高效适配到特定垂直领域（如交通监控场景）成为了计算机视觉领域的一个核心研究方向。本文介绍的 **CosmosAlign** 正是为了解决这一挑战而提出的先进生成式交通视频预测框架。

该研究的核心假设是：成功将大型预训练世界模型适配到下游预测任务，关键在于**分布对齐（Distribution Alignment）**，而不是单纯扩大模型容量。为此，作者创新性地提出了一种两阶段的 LoRA 适配策略以及一套无需训练的推理精炼流程。凭借该方法，CosmosAlign 在 AI City Challenge 2026 赛道 5（Track 5）的最终排行榜上以 76.49 分的成绩勇夺桂冠。

---

# CosmosAlign: Adapting a World Foundation Model for Generative Traffic Video Forecasting

| Field | Details |
| :--- | :--- |
| **arXiv ID** | [2608.07693](https://arxiv.org/abs/2608.07693) [cs.CV] |
| **Authors** | Quang Minh Dinh, Tuan Kiet Doan |
| **Accepted At** | ECCVW 2026 |
| **Subjects** | Computer Vision and Pattern Recognition (`cs.CV`); Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`) |
| **Submitted** | August 7, 2026 |
| **Resources** | [View PDF](https://arxiv.org/pdf/2608.07693) \| [Project Page / Code](https://quangminhdinh.github.io/CosmosAlign/) |

---

## 📌 Executive Summary

> **CosmosAlign** is a state-of-the-art generative traffic video forecasting framework built upon the pretrained *Cosmos-3-Nano* world foundation model. The core hypothesis of this work is that successfully adapting large pretrained world models to downstream forecasting tasks relies primarily on **distribution alignment** rather than simply scaling model capacity. 
> 
> To achieve this, the authors introduce a novel two-stage LoRA adaptation strategy alongside a training-free inference refinement procedure. Securing first place on the final leaderboard, **CosmosAlign achieved a score of 76.49 on the AI City Challenge 2026 Track 5 benchmark**.

**执行摘要**

> **CosmosAlign** 是一个最先进的生成式交通视频预测框架，它构建于预训练的 *Cosmos-3-Nano* 世界基础模型之上。这项工作核心假设是，成功将大型预训练世界模型适配到下游预测任务，主要依赖于**分布对齐**，而不是简单地扩展模型容量。
>
> 为了实现这一点，作者引入了一种新颖的两阶段 LoRA 适配策略以及一个无需训练的推理精炼流程。在 AI City Challenge 2026 赛道 5 基准测试中，**CosmosAlign 取得了 76.49 分的高分**，在最终排行榜上夺得头魁。

---

## 🔍 Abstract

> Generative traffic video forecasting aims to synthesize long-horizon, temporally coherent future videos of traffic scenes from a short observation history and textual descriptions. In this paper, we present **CosmosAlign**, a generative traffic video forecasting framework built upon the pretrained `Cosmos-3-Nano` world foundation model. Our approach is motivated by the observation that successfully adapting large pretrained world models to downstream forecasting tasks depends primarily on distribution alignment rather than increased model capacity. To this end, we propose a two-stage LoRA adaptation strategy that first aligns the conditioning-mode distribution with the target forecasting task, and then aligns the training captions with the model's native structured prompting interface through an LLM-based re-captioning pipeline. During inference, we further improve prediction quality using a fully training-free procedure consisting of consensus-based medoid sample selection and motion-adaptive blending of static scene regions. CosmosAlign achieves a final score of **76.49** on the AI City Challenge 2026 Track 5 benchmark, ranking first on the final leaderboard.

**摘要**

> 生成式交通视频预测旨在根据短期的观察历史和文本描述，合成具有长视野、时间连贯性的未来交通场景视频。在本文中，我们提出了 **CosmosAlign**，这是一个基于预训练 `Cosmos-3-Nano` 世界基础模型构建的生成式交通视频预测框架。我们的方法受到以下观察的启发：成功将大型预训练世界模型适配到下游预测任务，主要取决于分布对齐，而非盲目增加模型容量。为此，我们提出了一种两阶段的 LoRA 适配策略：首先将条件模式分布与目标预测任务进行对齐，然后通过基于大语言模型（LLM）的重新描述流水线，将训练文本描述与模型原生的结构化提示词接口进行对齐。在推理过程中，我们进一步利用完全无需训练的流程来提升预测质量，该流程包括基于共识的中心点样本选择（consensus-based medoid sample selection）以及静态场景区域的运动自适应混合（motion-adaptive blending）。CosmosAlign 在 AI City Challenge 2026 赛道 5 基准测试中取得了 **76.49** 的最终得分，在最终排行榜上位列第一。

---

## ⚙️ Methodology & Technical Contributions

> 1. **Two-Stage LoRA Adaptation:**
>    * **Stage 1:** Aligns the conditioning-mode distribution with the target traffic forecasting task.
>    * **Stage 2:** Aligns the training captions with the model's native structured prompting interface leveraging an LLM-based re-captioning pipeline.
> 2. **Training-Free Inference Refinement:**
>    * **Consensus-based Medoid Sample Selection:** Enhances prediction consistency and robustness during generation.
>    * **Motion-Adaptive Blending:** Dynamically blends static scene regions to preserve structural fidelity and reduce visual artifacts in background environments.

**方法论与技术贡献**

> 1. **两阶段 LoRA 适配：**
>    * **阶段 1：** 将条件模式分布与目标交通预测任务对齐。
>    * **阶段 2：** 利用基于 LLM 的重新描述流水线，将训练描述与模型原生的结构化提示词接口对齐。
> 2. **无需训练的推理精炼：**
>    * **基于共识的中心点样本 Selection（Consensus-based Medoid Sample Selection）：** 在生成过程中增强预测的一致性和鲁棒性。
>    * **运动自适应混合（Motion-Adaptive Blending）：** 动态混合静态场景区域，以保持结构保真度并减少背景环境中的视觉伪影。

---

## 🔗 Associated Resources & Citation

> * **Code & Website:** [https://quangminhdinh.github.io/CosmosAlign/](https://quangminhdinh.github.io/CosmosAlign/)
> * **DOI:** [10.48550/arXiv.2608.07693](https://doi.org/10.48550/arXiv.2608.07693)

**相关资源与引用**

> * **代码与网站：** [https://quangminhdinh.github.io/CosmosAlign/](https://quangminhdinh.github.io/CosmosAlign/)
> * **DOI：** [10.48550/arXiv.2608.07693](https://doi.org/10.48550/arXiv.2608.07693)

<div style="display:none">
<img alt="license icon" role="presentation" src="./images/5283893486a4.png">
</div>