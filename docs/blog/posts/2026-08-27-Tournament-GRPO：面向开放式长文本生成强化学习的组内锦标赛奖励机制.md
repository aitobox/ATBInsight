---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- 强化学习
- 锦标赛奖励
- 长文本生成
- 大语言模型
- GRPO
title: Tournament-GRPO：面向开放式长文本生成强化学习的组内锦标赛奖励机制
---
### 文章背景与核心概要
在开放式长文本生成的强化学习任务中，由于缺乏可靠的标准参考答案和自动化评估指标，模型训练往往面临巨大挑战。传统的基于评分标准的（Rubric-based）方法通常依赖单点的大模型作为裁判（LLM-as-a-judge）进行评分，但这存在绝对分数难以校准、同查询（same-query）输出之间区分度弱以及奖励饱和等问题。

为了克服这些局限性，本文提出了 **Tournament-GRPO** 框架，引入了一种组内奖励机制。该方法通过在相同查询的候选生成结果之间进行重复的多轮锦标赛，将基于评分标准的大模型判断转化为相对奖励。通过在组内比较候选者并累积锦标赛结果，该方法能够生成适合 GRPO 训练的归一化组内奖励。在 Deep Research Bench 上的实验表明，该方法取得了显著的性能提升（相比基线方法总分提升了 4.52 分），并在效率与效果之间实现了良好的权衡。

---

# Tournament-GRPO: Group-Wise Tournament Rewards for Reinforcement Learning in Open-Ended Long-Form Generation

## 📌 Summary
Reinforcement learning for open-ended long-form generation often suffers due to the lack of reliable reference answers and automated metrics. Traditional rubric-based methods use pointwise LLM-as-a-judge scoring, which struggles with absolute score calibration, weak discrimination among same-query outputs, and reward saturation. 

**Tournament-GRPO** addresses these limitations by introducing a group-wise reward framework. It transforms rubric-guided LLM judgments into relative rewards via repeated multi-round tournaments among same-query candidate rollouts. By comparing candidates within groups and accumulating their tournament outcomes, the method produces normalized group-wise rewards suited for GRPO training. Experiments on the Deep Research Bench demonstrate significant performance gains (a 4.52-point overall score improvement over baseline approaches) and favorable efficiency-effectiveness trade-offs.

---

## 📄 Article Metadata

* **arXiv ID:** [arXiv:2605.26958](https://arxiv.org/abs/2605.26958) [cs.CL]
* **Subjects:** Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`)
* **Conference:** Accepted to EMNLP 2026 Main Conference
* **Submission Date:** 26 May 2026 (v1), 25 August 2026 (v2)
* **DOI:** [10.48550/arXiv.2605.26958](https://doi.org/10.48550/arXiv.2605.26958)

---

## 👥 Authors
* Zixuan Yang
* Yiqun Chen
* Wei Yang
* Erhan Zhang
* Zihan Shen
* Xiaochi Wei
* Yan Gao
* Yi Wu
* Yao Hu
* Jiaxin Mao

---

## 📝 Abstract
由于通常缺乏可靠的参考答案和自动评估指标，面向开放式长文本生成的强化学习面临着诸多挑战。现有的基于评分标准的方法通常依赖单点的大模型裁判（LLM-as-a-judge）打分，然而绝对分数在复杂的回复之间很难进行校准，可能对同一查询的生成结果提供较弱的区分度，且在优化过程中容易产生奖励饱和。

> Reinforcement learning in open-ended long-form generation is challenging because reliable reference answers and automatic metrics are often unavailable. Existing rubric-based methods typically rely on pointwise LLM-as-a-judge scoring, but absolute scores are difficult to calibrate across complex responses, may provide weak discrimination among same-query rollouts, and can become saturated during optimization. 

我们提出了 **Tournament-GRPO**，这是一个组内奖励框架，它通过在相同查询的生成结果之间进行重复的多轮锦标赛，将基于评分标准的大模型判断转化为相对奖励。Tournament-GRPO 在组内对候选结果进行比较，累积锦标赛结果，并将其归一化为适合 GRPO 训练的组内奖励。

> We propose **Tournament-GRPO**, a group-wise reward framework that converts rubric-guided LLM judgments into relative rewards through repeated multi-round tournaments among same-query rollouts. Tournament-GRPO compares candidates within groups, accumulates tournament outcomes, and normalizes them into group-wise rewards for GRPO training. 

在 Deep Research Bench 上的实验表明，Tournament-GRPO 持续优于现有的奖励设计基线，相比最强的基线方法实现了 4.52 点的总分提升。进一步的分析表明，锦标赛奖励提供了良好的效果-效率权衡，并且锦标赛设计会影响训练动态。这些结果表明，基于评分标准的锦标赛比较为开放式长文本生成的强化学习提供了有效的奖励信号。

> Experiments on Deep Research Bench show that Tournament-GRPO consistently outperforms existing reward-design baselines, achieving a 4.52-point overall-score improvement over the strongest baseline. Further analyses show that tournament rewards provide a favorable effectiveness–efficiency trade-off and that tournament design affects training dynamics. These results suggest that rubric-guided tournament comparison provides an effective reward signal for reinforcement learning in open-ended long-form generation.

---

## 🔗 Links & Resources
* [View PDF](https://arxiv.org/pdf/2605.26958)
* [HTML Version (Experimental)](https://arxiv.org/html/2605.26958v2)
* [TeX Source](https://arxiv.org/src/2605.26958)