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
- 具身智能
- 系统安全
title: SimVerity：模拟智能体成功何时能在物理部署中转化为现实？
---
### 文章背景与核心概要
在人工智能智能体的基准测试中，模拟仿真评测一直扮演着基石的角色，然而业内此前缺乏对“模拟测试通过”究竟能多大程度转化为物理部署成功率的系统性量化。为此，本文引入了 **SimVerity** 这一判决迁移保证框架，它通过在真实世界的智能家居部署中重放匹配的场景，并将智能体的执行结果与独立合格的物理观测者进行交叉验证。

该研究的核心发现包括：部署成功是一个动态的现实世界过程，而非仿真中的静态属性；高级仿真器通过了全部灯光测试，物理摄像头却捕捉到了42起亚秒级失败；通过学习并锁定风险轮廓，框架成功预测了未测物理路径上的失败；修改智能体循环的模型客户端配置可显著提升场景匹配份额。最终，SimVerity 将判决迁移转化为部署前明确且可操作的决策：**通过（clear）**、**弃权（abstain）** 或 **升级（escalate）**。

---

# SimVerity: When Does Simulated Agent Success Survive Physical Deployment?
# SimVerity：模拟智能体成功何时能在物理部署中转化为现实？

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
## 执行摘要

Simulated evaluation is a cornerstone of benchmarking AI agents, yet the field lacks a systematic quantification of how well a simulated "pass" translates to physical deployment success. **SimVerity** is introduced as a verdict-transfer assurance framework that replays matched scenarios on real-world smart home deployments and cross-validates agent execution against independently qualified physical witnesses. 

> 模拟仿真评测是评估 AI 智能体性能的基石，然而该领域缺乏对模拟“通过”如何转化为物理部署成功率的系统性量化。**SimVerity** 作为一种判决迁移保证框架被提出，它在真实世界的智能家居部署中重放匹配的场景，并针对独立合格的物理观测者对智能体执行情况进行交叉验证。

Key insights from the evaluation include:
* **The Reality Gap:** Deployment success is a dynamic real-world process rather than a static property in simulation. Metrics like completion, reported state, observable effect, and settled outcome frequently diverge within the exact same execution.
* **Invisible Failures:** While an advanced simulator successfully cleared all 240 light trials, a physical camera detected 42 sub-second failures that completely escaped settled-state checks.
* **Predictable False Clearance:** A risk profile—learned from measured trials and locked prior to evaluation—successfully predicted failures on unmeasured physical paths, consistently outperforming a property-blind baseline across all eleven held-out sessions spanning two cohorts.
* **Measurable Auditability:** Modifying a single agent loop's model-client/serving configuration noticeably elevated its scenario-matching share from a range of 52–88% up to a robust 100%.
* **Shared Simulator Blind Spots:** A second qualified simulator offered no independent cross-checking benefit, as it never disagreed on any overlapping case, reinforcing the necessity of physical measurement to expose shared blind spots.

> 评估得出的核心洞察包括：
> * **现实鸿沟（The Reality Gap）：** 部署成功是一个动态的现实世界过程，而不是仿真中的静态属性。诸如完成度、报告状态、可观测效果和最终结果等指标在完全相同的执行过程中经常出现分歧。
> * **隐形失败（Invisible Failures）：** 尽管一个高级仿真器成功通过了所有 240 次灯光测试，但物理摄像头却检测到了 42 次完全逃过稳态检查的亚秒级故障。
> * **可预测的错误放行（Predictable False Clearance）：** 从已测试验中学习并在评估前锁定的风险画像，成功预测了未测量物理路径上的失败，在跨越两个队列的所有 11 个保留会话中，其表现始终优于盲目追求属性的基线。
> * **可测量的可审计性（Measurable Auditability）：** 修改单个智能体循环的模型客户端/服务配置，使其场景匹配份额从 52%–88% 的范围显著提升至稳健的 100%。
> * **共享的仿真器盲区（Shared Simulator Blind Spots）：** 第二个合格的仿真器没有提供任何独立的交叉检查益处，因为它在任何重叠案例上从未产生分歧，这强化了通过物理测量来暴露共享盲区的必要性。

Ultimately, **SimVerity** transforms verdict transfer into an explicit, actionable operational decision before deployment: **clear**, **abstain**, or **escalate**.

> 最终，**SimVerity** 将判决迁移转化为部署前明确且可操作的运营决策：**通过（clear）**、**弃权（abstain）** 或 **升级（escalate）**。

---

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">