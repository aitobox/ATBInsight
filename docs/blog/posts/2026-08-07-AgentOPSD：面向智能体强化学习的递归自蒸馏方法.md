---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-07
hide:
- navigation
tags:
- 强化学习
- 智能体
- 自蒸馏
- 信用分配
- 贝叶斯更新
title: AgentOPSD：面向智能体强化学习的递归自蒸馏方法
---
### 文章背景与核心概要
在长视距、多轮交互的智能体任务中，传统的、带有可验证奖励的强化学习（RL）方法往往难以准确追溯决定最终结果的关键决策。为了解决这一长期存在的信用分配难题，本文提出了 AgentOPSD——一种无需评论家（critic-free）的创新递归方法。该方法通过将词元级（token-level）的教师-学生对数概率差聚合为轮次级证据，并在对数几率空间中递归更新贝叶斯信念状态，从而将稀疏的结果监督转化为精准的轮次级信用信号。

AgentOPSD 无需额外的评论家或额外的采样回滚（rollouts），能够与标准策略优化无缝集成。实验表明，该方法在 ALFWorld、WebShop 和 Search-QA 等复杂基准测试中取得了最先进（SOTA）的性能。使用 Qwen2.5-7B 模型时，其在 ALFWorld 上的成功率高达 89.1%，充分证明了基于历史依赖的递归信念更新和轮次级聚合在提升智能体强化学习效率方面的巨大潜力。

---

## 📝 Summary

> **AgentOPSD** is a novel, critic-free method designed for turn-level credit assignment in agentic reinforcement learning (RL). While traditional RL with verifiable rewards often struggles to pinpoint the pivotal decisions responsible for final outcomes in long-horizon, multi-turn tasks, AgentOPSD solves this by aggregating token-level teacher-student log-probability gaps into turn-level evidence. It then recursively updates a Bayesian belief state in log-odds space to convert sparse outcome supervision into precise turn-level credit signals. Requiring neither additional critics nor extra rollouts, AgentOPSD integrates seamlessly with standard policy optimization and achieves state-of-the-art performance on complex benchmarks like ALFWorld, WebShop, and Search-QA.

---

## 📋 Metadata

> * **arXiv ID:** [arXiv:2608.05987](https://arxiv.org/abs/2608.05987) [cs.AI]
> * **Subjects:** Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`)
> * **Submission Date:** August 6, 2026
> * **Authors:** 
>   Zi-Han Wang, Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Jie Wu, Zhengzhou Cai, Yueqing Sun, Ziang Ye, Linji Hao, Qi Gu, Xunliang Cai, Yongliang Shen, Yujiu Yang
> * **Official Code Repository:** [GitHub - ZethWang/AgentOPSD](https://github.com/ZethWang/AgentOPSD)

---

## 🔍 Abstract

> Reinforcement learning (RL) with verifiable rewards constructs trajectory-level advantage estimates, yet it often fails to credit the few pivotal decisions that determine outcomes in long-horizon, multi-turn agentic tasks. Recent work introduces privileged self-distillation for credit assignment, providing denser supervision, but it remains unclear how such local signals should represent sequential credit. 

带有可验证奖励的强化学习（RL）构建了轨迹级的优势估计，然而它往往无法将功劳归于那些在长视距、多轮智能体任务中决定最终结果的少数关键决策。近期的研究引入了特权自蒸馏来进行信用分配以提供更密集的监督，但这些局部信号究竟应如何代表序列信用，目前尚不明确。

> We propose **AgentOPSD**, a critic-free, recursive method for turn-level credit assignment in agentic reinforcement learning. AgentOPSD aggregates token-level teacher-student log-probability gaps into turn-level evidence and recursively updates a Bayesian belief state in log-odds space. This yields a principled reweighting scheme that converts sparse outcome supervision into turn-level credit signals and identifies pivotal turns through the marginal belief revision between consecutive states. The method is fully compatible with standard policy optimization and requires neither an additional critic nor extra rollouts. 

为此，我们提出了 **AgentOPSD**，这是一种用于智能体强化学习中轮次级信用分配的、无需评论家的递归方法。AgentOPSD 将词元级的教师-学生对数概率差聚合为轮次级证据，并在对数几率空间中递归更新贝叶斯信念状态。这产生了一种原则性的重新加权方案，能够将稀疏的结果监督转化为轮次级信用信号，并通过连续状态之间的边缘信念修正来识别关键轮次。该方法与标准策略优化完全兼容，既不需要额外的评论家，也不需要额外的采样回滚。

> We evaluate AgentOPSD on ALFWorld, WebShop, and Search-QA using Qwen2.5 models at two scales (3B and 7B). AgentOPSD outperforms GRPO and strong self-distillation baselines, achieving **89.1% success on ALFWorld** with Qwen2.5-7B. Ablation studies attribute the gains to turn-level aggregation and history-dependent recursive belief updates.

我们在 ALFWorld、WebShop 和 Search-QA 上，使用 3B 和 7B 两种规模的 Qwen2.5 模型对 AgentOPSD 进行了评估。AgentOPSD 的表现超越了 GRPO 以及强自蒸馏基线，在使用 Qwen2.5-7B 时在 **ALFWorld 上取得了 89.1% 的成功率**。消融实验表明，性能的提升主要归功于轮次级聚合以及依赖历史的递归信念更新。

---

## 🔗 Links & Resources

> * [View PDF](https://arxiv.org/pdf/2608.05987)
> * [TeX Source](https://arxiv.org/src/2608.05987)
> * [DOI (DataCite)](https://doi.org/10.48550/arXiv.2608.05987)
> * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.05987)
> * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.05987)