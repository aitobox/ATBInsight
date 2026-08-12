---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-07
hide:
- navigation
tags:
- 多智能体系统
- 模型评估
- 智能体编排
- 容错机制
- 链路追踪
title: OrchestraBench：评估多智能体编排的失效模式、恢复能力与任务拆解质量
---
### 文章背景与核心概要

随着多智能体编排框架从探索性演示（Demo）加速迈向生产环境，现有的基准测试通常仅衡量最终任务的准确率。这导致它们往往无法诊断流水线在 *何处* 崩溃、系统级联故障是从哪里开始的，或者到底是哪项路由决策导致了故障。

为了填补这一空白，**OrchestraBench** 引入了一种基于模板化企业工作流设计的、受控且支持种子复现的故障注入测试框架。该基准测试通过**级联半径（cascade radius）**和**按失效模式分类的恢复率（per-failure-mode recovery）**等核心指标，并辅以自助法置信区间（bootstrap confidence intervals）与配对统计检验，全面评估故障传播、恢复率以及任务拆解质量。

---

## 📌 Summary / 摘要

> As multi-agent orchestration frameworks transition from exploratory demos to production environments, current benchmarks typically measure only end-task accuracy. They often fail to diagnose *why* a pipeline broke, where systemic cascades began, or which routing decisions caused the failure. 
> 
> To bridge this gap, **OrchestraBench** introduces a controlled, seed-reproducible failure-injection harness designed over templated enterprise workflows. The benchmark evaluates failure propagation, recovery rates, and task decomposition quality using metrics such as **cascade radius** and **per-failure-mode recovery**, backed by bootstrap confidence intervals and paired statistical tests.

随着多智能体编排框架从探索性演示（Demo）加速迈向生产环境，现有的基准测试通常仅衡量最终任务的准确率。这导致它们往往无法诊断流水线在 *何处* 崩溃、系统级联故障是从哪里开始的，或者到底是哪项路由决策导致了故障。 
 
为了填补这一空白，**OrchestraBench** 引入了一种基于模板化企业工作流设计的、受控且支持种子复现的故障注入测试框架。该基准测试通过**级联半径**和**按失效模式分类的恢复率**等指标，并辅以自助法置信区间与配对统计检验，全面评估故障传播、恢复率以及任务拆解质量。

---

## 🔍 Key Findings & Results / 关键发现与结果

* **Routing Policies:** On a 26-case gold-labelled diagnostic, a naive keyword/flag router scored **0%** on adversarial test cases featuring missing or misleading surface flags. Conversely, an intent-reasoning model router achieved a **100%** success rate, matching the performance of an oracle.
* **Failure-Handling Tiers:** Controlled mechanism probes utilizing a real Claude agent across a verifiable arithmetic dependency chain revealed three distinct failure-handling tiers across five MAST modes:
  1. *Tool faults:* Recovered fully (`1.0`)
  2. *Ambiguous delegation:* Recovered partially (`0.30`)
  3. *Latent or semantic modes:* Never recovered (`0.0`)
* **Generalizability:** This performance hierarchy remained consistent when the computational task was reframed into a loan-approval workflow, and across different model scales (Claude Sonnet, Opus, and Haiku), although absolute recovery rates shifted depending on the context window.
* **Impact of Blind Retries:** Blind retry strategies successfully reproduced latent faults and increased the time-to-detection, highlighting that active detection and attribution are prerequisites for containment.
* **Cascade Dynamics:** The cascade radius scaled upward with pipeline depth, expanding from a mean of `0.9` to `4.7` across depths ranging from 3 to 7.
* **State Repair Ablation:** A trusted-state repair ablation demonstrated that apparent containment improvements stemmed primarily from the trusted-state signal itself rather than autonomous system detection.

*(Note: These findings are derived from controlled-chain mechanism probes rather than broad domain-workload claims.)*

> * **路由策略：** 在包含 26 个黄金标准标签的诊断测试中，针对存在表面标志缺失或误导的对抗性测试用例，朴素的关键词/标志路由器（keyword/flag router）得分为 **0%**。相反，意图推理模型路由器（intent-reasoning model router）实现了 **100%** 的成功率，性能与理想预言机（oracle）不相上下。
> * **故障处理层级：** 利用真实的 Claude 智能体在可验证的算术依赖链上进行的受控机制探测，揭示了在五种 MAST 模式下存在三个截然不同的故障处理层级：
>   1. *工具故障（Tool faults）：* 完全恢复（`1.0`）
>   2. *模糊委派（Ambiguous delegation）：* 部分恢复（`0.30`）
>   3. *潜在或语义模式（Latent or semantic modes）：* 从未恢复（`0.0`）
> * **泛化能力：** 当计算任务被重构为贷款审批工作流，且跨越不同的模型规模（Claude Sonnet、Opus 和 Haiku）时，这种性能等级层级依然保持一致，尽管绝对恢复率会根据上下文窗口的大小而发生变化。
> * **盲目重试的影响：** 盲目重试策略成功重现了潜在故障并增加了检测时间（time-to-detection），这凸显了主动检测与归因是实现故障控制（containment）的前提条件。
> * **级联动力学：** 级联半径随流水线深度的增加而扩大，在深度从 3 到 7 的范围内，平均值从 `0.9` 扩展到 `4.7`。
> * **状态修复消融实验：** 受信任状态修复的消融实验表明，表面上的故障控制改善主要源于受信任状态信号本身，而不是系统的自主检测能力。
> 
> *(注：以上发现均源自受控链条机制探测，而非对广泛领域工作负载的泛化断言。)*

---

## 🔗 Links & Resources / 链接与资源

* **Paper Access:** [View PDF](https://arxiv.org/pdf/2608.05263) | [arXiv HTML (Experimental)](https://arxiv.org/html/2608.05263v1)
* **Official Metadata:** [arXiv:2608.05263 [cs.AI]](https://arxiv.org/abs/2608.05263) | [DOI](https://doi.org/10.48550/arXiv.2608.05263)

> * **论文获取：** [查看 PDF](https://arxiv.org/pdf/2608.05263) | [arXiv HTML（实验性）](https://arxiv.org/html/2608.05263v1)
> * **官方元数据：** [arXiv:2608.05263 [cs.AI]](https://arxiv.org/abs/2608.05263) | [DOI](https://doi.org/10.48550/arXiv.2608.05263)