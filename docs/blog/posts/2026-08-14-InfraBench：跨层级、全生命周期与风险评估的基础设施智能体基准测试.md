---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- AI智能体
- 基础设施管理
- 基准测试
- 系统工程
- 自动化运维
title: InfraBench：跨层级、全生命周期与风险评估的基础设施智能体基准测试
---
### 文章背景与核心概要

随着现代计算基础设施规模的不断扩大和系统复杂性的日益增加，运维管理已成为一项极具挑战性的任务。近期人工智能智能体（AI Agents）的突破为实现基础设施管理的自动化提供了契机，但这些智能体在真实生产环境中的可靠性与实际能力仍缺乏系统性的验证。

为了填补这一空白，研究人员推出了 **InfraBench**。这是一个全面的基准测试套件，旨在评估AI智能体在真实基础设施任务中的表现。该基准测试覆盖了完整的系统栈和运维生命周期，并集成了细粒度的风险评估机制。

通过对15种智能体-模型配置的评估，研究发现当前AI基础设施智能体存在显著缺陷：即使是最强的配置也无法在所有任务中获得满分；平均有效得分在40%至88%之间波动，且表现不稳定；重复测试显示，顶级配置的成功率依然较低。此外，细粒度评分揭示了系统性的失败模式：智能体往往能达成短期目标，却留下了非持久性变更、破坏了分布式一致性、产生了不安全的副作用或未清理的状态。

---

## 📌 执行摘要

> Managing modern computing infrastructure has become increasingly complex due to rising system scale and intricacy. While recent breakthroughs in AI agents present promising opportunities to automate infrastructure management, their reliability and capability in real-world environments remain largely unproven. 
>
> To address this gap, researchers introduce **InfraBench**, a comprehensive benchmark suite designed to evaluate AI agents on realistic infrastructure tasks. The benchmark spans the full system stack, the complete operational lifecycle, and integrates fine-grained risk assessment. 
>
> Key findings from evaluating 15 agent-model configurations reveal critical shortcomings in current AI infrastructure agents:
> * **Incomplete Success:** Even the strongest agent configuration fails to secure a full score across all tasks.
> * **Variable Performance:** Mean effective scores range from roughly **40% to 88%** (with per-configuration standard errors of 6–12 points). 
> * **Low Reliability:** Repeating tasks multiple times demonstrates that top configurations successfully pass only a fraction of their attempts.
> * **Underlying Failure Patterns:** Per-check scoring exposes a systemic issue: agents frequently satisfy short-term objectives while leaving behind non-durable changes, broken distributed invariants, unsafe side effects, and uncleaned states.

---

## 📝 摘要

> 随着系统复杂性的不断增加，管理现代计算基础设施已成为一个日益困难的问题。人工智能智能体的最新进展为自动化基础设施管理任务提供了及时的契机，但这些智能体在处理现实世界基础设施复杂性方面的能力尚不明确。我们提出了 InfraBench，这是一个用于评估AI智能体在真实基础设施任务中表现的基准测试套件，涵盖了完整的系统栈、全生命周期运维以及细粒度的风险评估。对15种智能体-模型配置的实验表明，即使是最强的智能体也无法在所有任务中获得满分。平均有效得分范围约为 40% 至 88%（每种配置的标准误差为 6-12 个点），对每项任务进行三次重复测试显示，顶级配置通过的尝试次数仅占一小部分。此外，细粒度评分揭示了一种普遍的失败模式：智能体可能经常满足短期目标，但却留下了非持久性变更、破坏了分布式一致性、产生了不安全的副作用以及未清理的状态。

> Managing modern computing infrastructure has been a steadily harder problem due to the ever-increasing complexity. Recent advances in AI agents create a timely opportunity to automate infrastructure management tasks, but it remains unclear how well such agents can handle real-world infrastructure complexity. We present InfraBench, a benchmark suite for evaluating AI agents on realistic infrastructure tasks across the full system stack and full operational lifecycle with fine-grained risk assessment. Experiments with 15 agent-model configurations show that even the strongest agent cannot secure a full score across all tasks. Mean effective scores range from roughly 40% to 88% (with per-configuration standard errors of 6-12 points), repeating every task three times reveals that top configurations still pass only a fraction of their attempts, and per-check scoring exposes a general failure pattern: agents may routinely satisfy short-term objectives while leaving non-durable changes, broken distributed invariants, unsafe side effects, and uncleaned state behind.

---

## 🔗 更多链接与资源

> * **Paper Access:** [View PDF](https://arxiv.org/pdf/2608.11234) | [HTML Version](https://arxiv.org/html/2608.11234v1) | [TeX Source](https://arxiv.org/src/2608.11234)
> * **Official Website:** [infraben.ch](http://infraben.ch)
> * **Citation (BibTeX):** Available via the arXiv abstract page or standard bibliographic tools (NASA ADS, Google Scholar, Semantic Scholar).