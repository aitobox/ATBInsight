---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- AI智能体
- 仿真评测
- 现实鸿沟
- 智能家居
- 鲁棒性验证
title: SimVerity：模拟智能体成功何时能在物理部署中持续？
---
### 文章背景与核心概要
在人工智能智能体（AI Agents）的基准测试中，基于模拟环境的评测一直是核心手段。然而，学术界和工业界一直缺乏系统性量化手段，来评估模拟环境中的“通过”能否真正转化为物理世界部署中的成功。本文引入了 SimVerity 这一判定迁移（verdict-transfer）保障框架，它能够在真实世界的智能家居部署中重放匹配的场景，并针对独立合格的物理观测者对智能体执行情况进行交叉验证。

评估的核心洞察表明：部署成功是一个动态的现实世界过程，而非仿真中的静态属性。完全相同的执行过程中，完成度、报告状态、可观测效果和最终结果等指标经常出现分歧。此外，研究揭示了“隐形失败”现象——尽管先进的模拟器成功通过了所有 240 次灯光测试，物理相机却检测到了 42 次完全逃过结算状态检查的亚秒级故障。最终，SimVerity 将判定迁移转化为部署前明确且可操作的决策：**通过（clear）**、**弃权（abstain）**或**升级（escalate）**。

---

# SimVerity: When Does Simulated Agent Success Survive Physical Deployment?

<div align="center">

| **Metadata** | **Details** |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.25067](https://arxiv.org/abs/2608.25067) [cs.AI] |
| **Subjects** | Artificial Intelligence (`cs.AI`) |
| **Authors** | Zhonghao Zhan, Yefan Zhang, Krinos Li, Hamed Haddadi |
| **Submission Date** | August 25, 2026 |
| **Status** | Submitted to the Main Technical Track of AAAI Conference on Artificial Intelligence (AAAI-27); currently under review |
| **License** | [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/) |
| **Full-Text Links** | [View PDF](https://arxiv.org/pdf/2608.25067) \| [HTML Version](https://arxiv.org/html/2608.25067v1) \| [TeX Source](https://arxiv.org/src/2608.25067) |

</div>

---

## Executive Summary

Simulated evaluation is a cornerstone of benchmarking AI agents, yet the field lacks a systematic quantification of how well a simulated "pass" translates to physical deployment success. **SimVerity** is introduced as a verdict-transfer assurance framework that replays matched scenarios on real-world smart home deployments and cross-validates agent execution against independently qualified physical witnesses. 

> 模拟评估是基准测试 AI 智能体的基石，然而该领域缺乏对模拟“通过”如何转化为物理部署成功率的系统性量化。**SimVerity** 作为一个判定迁移保障框架被引入，它能够在真实世界的智能家居部署中重放匹配的场景，并针对独立合格的物理观测者对智能体执行情况进行交叉验证。

Key insights from the evaluation include:
* **The Reality Gap:** Deployment success is a dynamic real-world process rather than a static property in simulation. Metrics like completion, reported state, observable effect, and settled outcome frequently diverge within the exact same execution.
* **Invisible Failures:** While an advanced simulator successfully cleared all 240 light trials, a physical camera detected 42 sub-second failures that completely escaped settled-state checks.
* **Predictable False Clearance:** A risk profile—learned from measured trials and locked prior to evaluation—successfully predicted failures on unmeasured physical paths, consistently outperforming a property-blind baseline across all eleven held-out sessions spanning two cohorts.
* **Measurable Auditability:** Modifying a single agent loop's model-client/serving configuration noticeably elevated its scenario-matching share from a range of 52–88% up to a robust 100%.
* **Shared Simulator Blind Spots:** A second qualified simulator offered no independent cross-checking benefit, as it never disagreed on any overlapping case, reinforcing the necessity of physical measurement to expose shared blind spots.

> 评估得出的核心洞察包括：
> * **现实鸿沟（The Reality Gap）：** 部署成功是一个动态的现实世界过程，而不是仿真中的静态属性。在完全相同的执行过程中，完成度、报告状态、可观测效果和结算结果等指标经常出现分歧。
> * **隐形失败（Invisible Failures）：** 尽管一个先进的模拟器成功通过了所有 240 次灯光测试，但物理相机检测到了 42 次完全避开结算状态检查的亚秒级故障。
> * **可预测的错误放行（Predictable False Clearance）：** 从测量试验中学习并在评估前锁定的风险配置文件，成功预测了未测量物理路径上的失败，在跨越两个同类群体的所有十一次留存会话中，其表现始终优于属性盲基线（property-blind baseline）。
> * **可衡量的可审计性（Measurable Auditability）：** 修改单个智能体循环的模型客户端/服务配置，使其场景匹配份额从 52–88% 的范围显著提升至稳健的 100%。
> * **共享模拟器盲区（Shared Simulator Blind Spots）：** 第二个合格的模拟器没有提供独立的交叉检查优势，因为它在任何重叠案例上从未产生分歧，这强化了通过物理测量来暴露共享盲区的必要性。

Ultimately, **SimVerity** transforms verdict transfer into an explicit, actionable operational decision before deployment: **clear**, **abstain**, or **escalate**.

> 最终，**SimVerity** 将判定迁移转变为部署前明确、可操作的运营决策：**通过（clear）**、**弃权（abstain）**或**升级（escalate）**。

---

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">