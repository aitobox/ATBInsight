---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- InfraBench
- AI智能体
- 基础设施管理
- 自动化运维
- 基准测试
title: InfraBench：跨层级、全生命周期与风险维度的基础设施智能体评估基准
---
### 文章背景与核心概要
现代计算基础设施的管理随着系统复杂性的急剧上升而变得愈发困难。虽然人工智能智能体（AI Agents）的最新进展为自动化基础设施管理提供了宝贵机遇，但这些智能体在处理真实世界操作复杂性时的实际表现仍不明朗。为此，本文推出了 InfraBench——一个全面的基准测试套件，旨在评估 AI 智能体在横跨整个系统技术栈、完整运维生命周期及细粒度风险评估的真实基础设施任务中的表现。

通过对 15 种智能体-模型配置的评估，研究揭示了显著的性能局限性：没有单一个智能体能够在所有任务中获得满分，平均有效得分在 40% 到 88% 之间，且重复试验显示顶级配置也只能通过一部分尝试。逐项检查评分进一步暴露出一种系统性的失效模式：智能体往往能够满足短期目标，却留下了非持久化变更、被破坏的分布式不变量、不安全的副作用以及未清理的状态。

---

## 摘要

> Managing modern computing infrastructure has become a steadily harder problem due to the ever-increasing complexity. Recent advances in AI agents create a timely opportunity to automate infrastructure management tasks, but it remains unclear how well such agents can handle real-world infrastructure complexity. We present InfraBench, a benchmark suite for evaluating AI agents on realistic infrastructure tasks across the full system stack and full operational lifecycle with fine-grained risk assessment. Experiments with 15 agent-model configurations show that even the strongest agent cannot secure a full score across all tasks. Mean effective scores range from roughly 40% to 88% (with per-configuration standard errors of 6-12 points), repeating every task three times reveals that top configurations still pass only a fraction of their attempts, and per-check scoring exposes a general failure pattern: agents may routinely satisfy short-term objectives while leaving non-durable changes, broken distributed invariants, unsafe side effects, and uncleaned state behind. INFRABENCH, including its live leaderboard, tasks, and evaluation harness, is publicly available at [this http URL](http://infraben.ch).

> 随着复杂性的不断增加，管理现代计算基础设施变得越来越困难。人工智能智能体的最新进展为自动化基础设施管理任务创造了适时的契机，但此类智能体究竟能多大程度上处理现实世界的基础基础设施复杂性，目前仍不明确。我们提出了 InfraBench，这是一个基准测试套件，用于评估 AI 智能体在横跨整个系统技术栈、完整运维生命周期以及具备细粒度风险评估的真实基础设施任务中的表现。对 15 种智能体-模型配置的实验表明，即使是最强的智能体也无法在所有任务中获得满分。平均有效得分大致在 40% 到 88% 之间（每种配置的标准误差为 6-12 个百分点），将每项任务重复执行三次表明，顶级配置仍然只能通过一部分尝试；而逐项检查评分暴露出一种普遍的失效模式：智能体虽然能例行公事般地满足短期目标，但却留下了不持久的变更、被破坏的分布式不变量、不安全的副作用以及未清理的状态。INFRABENCH（包括其实时排行榜、任务集和评估工具套件）已在 [http](http://infraben.ch) 公开提供。

---

## 论文元数据

| 字段 | 详情 |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.11234](https://arxiv.org/abs/2608.11234) [cs.AI] |
| **研究主题** | 人工智能 (`cs.AI`); 操作系统 (`cs.OS`) |
| **MSC 类别** | C.2.4, D.4.7, I.2.11 |
| **提交历史** | [v1] 2026年7月31日 周五<br>[v2] 2026年8月24日 周一 *(当前版本)* |
| **开源许可** | [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> |
| **相关资源** | • [公共网站与排行榜](http://infraben.ch)<br>• [查看 PDF](https://arxiv.org/pdf/2608.11234)<br>• [HTML 版本](https://arxiv.org/html/2608.11234v2) |

---

## 作者团队
* **Yuan Gao**
* **Zeren Yang**
* **Junnan Li**
* **Shawn (Wanxiang) Zhong**
* **Ahmed Dajani**
* **Mai Zheng**
* **Andrea Arpaci-Dusseau**
* **Remzi Arpaci-Dusseau**

---

## 概述与核心发现

> Managing modern computing infrastructure has become increasingly complex. While recent advances in AI agents offer a timely opportunity to automate infrastructure management, it remains unclear how effectively these agents handle real-world operational complexities. **InfraBench** is a comprehensive benchmark suite designed to evaluate AI agents on realistic infrastructure tasks spanning the full system stack and operational lifecycle, incorporating fine-grained risk assessment. 
> 
> Evaluations across 15 agent-model configurations reveal significant limitations:
> * No single agent secured a full score across all tasks.
> * Mean effective scores ranged from **40% to 88%** (with per-configuration standard errors of 6–12 points).
> * Repeated trials (running every task three times) showed that top configurations pass only a fraction of their attempts.
> * Per-check scoring highlighted a systemic failure pattern: agents often satisfy short-term objectives while leaving behind non-durable changes, broken distributed invariants, unsafe side effects, and uncleaned state.

> 管理现代计算基础设施已经变得日益复杂。尽管 AI 智能体的最新进展为自动化基础设施管理提供了及时的机遇，但这些智能体如何有效地处理现实世界的运维复杂性仍不明确。**InfraBench** 是一个全面的基准测试套件，旨在评估 AI 智能体在涵盖整个系统技术栈和运维生命周期的现实基础设施任务中的表现，并纳入了细粒度的风险评估。
> 
> 对 15 种智能体-模型配置的评估揭示了重大的局限性：
> * 没有单一个智能体能在所有任务中获得满分。
> * 平均有效得分在 **40% 到 88%** 之间（每种配置的标准误差为 6-12 个百分点）。
> * 重复试验（每项任务运行三次）表明，顶级配置只能通过其尝试的一部分。
> * 逐项检查评分突显了一种系统性失效模式：智能体往往能满足短期目标，但同时却留下了不持久的变更、被破坏的分布式不变量、不安全的副作用以及未清理的状态。