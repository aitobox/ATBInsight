---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- LongRCA Bench
- AI Agents
- Root Cause Analysis
- Failure Attribution
- RCTA
title: LongRCA Bench：诊断长程智能体失败中的责任角色与根本原因
---
### 文章背景与核心概要

随着长程（Long-Horizon）AI智能体在复杂任务中的广泛应用，其执行失败后的归因分析变得至关重要。传统的基于结果的评估方法往往只能判定任务失败，却无法指出决定性错误究竟发生在哪个环节。面对动辄包含数百个记录步骤的执行轨迹，人工排查责任角色和最早的决定性根本原因步骤成了一大主要技术瓶颈。

为了填补这一空白，本文作者推出了 **LongRCA Bench** 基准测试集。该数据集包含5个领域内1,140条未经人为注入错误的失败轨迹，并提供了人工标注的责任角色与根本原因步骤。同时，作者提出了一种名为 **根因轨迹归因（Root-Cause Trajectory Attribution, RCTA）** 的免训练基线方法，能够通过段摘要检索候选错误步骤，并将其追溯至早期的交接指令。该研究凸显了在长轨迹失败诊断中，将“责任角色归因”和“精确根步骤定位”作为独立目标进行评估的必要性。

---

# LongRCA Bench: Diagnosing Responsible Roles and Root Causes in Long-Horizon Agent Failures

> # LongRCA Bench: Diagnosing Responsible Roles and Root Causes in Long-Horizon Agent Failures

**Authors:** Yunfei Zhang, Boyu Feng, Changhua Pei, Zexin Wang, Zhihuang Peng, Xinlong Liu, Hengyue Jiang, Difeng Ma, Jiayi Zhang, Yongzhou Yao, Yanan Zhao, Fei Sun, Yintong Huo, Zhaoyang Liu, Jingjing Li, Gaogang Xie, Dan Pei  
**Subjects:** Artificial Intelligence (`cs.AI`); Software Engineering (`cs.SE`)  
**arXiv:** [2608.15242](https://arxiv.org/abs/2608.15242) [cs.AI]  
**Submitted:** 15 Aug 2026 (Last revised: 21 Aug 2026)

---

## 📌 Summary

> ## 📌 Summary

当长程AI智能体执行失败时，传统的宏观结果级评估只能暴露出任务未成功，却无法指出决定性的错误是在轨迹的哪一步引入的。检查数百个记录步骤以识别出应负责任的角色并定位最早的决定性根本原因步骤，仍然是一个主要的瓶颈。

> When long-horizon agent executions fail, traditional outcome-level evaluations reveal only that the task was unsuccessful without pinpointing where the decisive error occurred. Inspecting hundreds of recorded steps to identify the responsible role and localize the earliest decisive root-cause step remains a major bottleneck. 

为了解决这一空白，作者引入了 **LongRCA Bench**，这是一个包含来自五个领域的1,140条失败轨迹的基准测试，其中未注入人为错误，并具有关于责任角色和根本原因步骤的人工标注。他们还提出了 **根因轨迹归因（Root-Cause Trajectory Attribution, RCTA）**，这是一种无需训练的基线方法，能够从段落摘要中检索候选错误步骤，并将其追溯到更早的交接指令。

> To address this gap, the authors introduce **LongRCA Bench**, a benchmark containing 1,140 failed trajectories across five domains without injected errors, featuring human-labeled annotations for responsible roles and root-cause steps. They also propose **Root-Cause Trajectory Attribution (RCTA)**, a training-free baseline method that retrieves candidate error steps from segment summaries and traces them back to earlier handoff instructions.

---

## 📖 Abstract

> ## 📖 Abstract

当长程智能体执行失败时，结果级别的评估仅能展示不成功的结局，而无法指出决定性的错误是如何进入轨迹的。开发者因此必须检查完整的执行过程，以识别负责任的角色并定位最早的决定性根本原因步骤。现有的失败归因基准大多集中在较短的轨迹上，这使得跨数百个记录步骤的诊断仍未得到充分探索。

> When a long-horizon agent execution fails, outcome-level evaluation reveals the unsuccessful result but not where the decisive error entered the trajectory. Developers then must inspect the full execution to identify the responsible role and localize the earliest decisive root-cause step. Existing failure-attribution benchmarks largely focus on shorter traces, leaving diagnosis across hundreds of recorded steps underexplored. 

我们推出了 **LongRCA Bench**，它包含5个领域中1,140个没有注入错误的失败轨迹。它为责任角色和最早的决定性根本原因步骤提供了独立评分的人工标签。中位数轨迹包含145个步骤，而最强的基线方法的精确根步骤准确率仅达到13.2%。

> We introduce **LongRCA Bench**, comprising 1,140 failed trajectories across five domains without injected errors. It provides independently scored human labels for the responsible role and earliest decisive root-cause step. The median trajectory contains 145 steps, and the strongest baseline reaches only 13.2% exact root-step accuracy. 

我们进一步提出了 **根因轨迹归因（Root-Cause Trajectory Attribution, RCTA）**，这是一种无需训练的方法，它从段落摘要中检索候选错误步骤，并将其追溯到可用的早期交接指令。使用相同的骨干网络、基准实例和评分协议，RCTA达到了51.1%的责任角色准确率和24.1%的精确根步骤准确率。这些结果突显了在长轨迹失败诊断中，将责任角色归因和精确根步骤定位评估为独立目标的必要性。

> We further present **Root-Cause Trajectory Attribution (RCTA)**, a training-free method that retrieves candidate error steps from segment summaries and traces them to available earlier handoff instructions. Using the same backbone, benchmark instances, and scoring protocol, RCTA reaches 51.1% responsible-role accuracy and 24.1% exact root-step accuracy. These results highlight the need to evaluate responsible-role attribution and exact root-step localization as separate targets in long-trajectory failure diagnosis.

---

## 📊 Key Details & Statistics

> ## 📊 Key Details & Statistics

* **基准规模：** 跨越5个领域的1,140条失败轨迹。
* **轨迹长度：** 中位数轨迹包含145个步骤。
* **基线性能：**
  * 现有最强基线：**13.2%** 的精确根步骤准确率。
  * **RCTA方法：** **51.1%** 的责任角色准确率和 **24.1%** 的精确根步骤准确率。
* **元数据：** 18页，6幅图。Yunfei Zhang和Boyu Feng对本文有同等贡献。裴昌华担任通讯作者。

> * **Benchmark Size:** 1,140 failed trajectories across 5 domains.
> * **Trajectory Length:** The median trajectory consists of 145 steps.
> * **Baseline Performance:** 
>   * Strongest existing baseline: **13.2%** exact root-step accuracy.
>   * **RCTA Method:** **51.1%** responsible-role accuracy and **24.1%** exact root-step accuracy.
> * **Metadata:** 18 pages, 6 figures. Yunfei Zhang and Boyu Feng contributed equally. Changhua Pei serves as the corresponding author.

---

## 🔗 Links & Resources

> ## 🔗 Links & Resources

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2608.15242) | [HTML 版本](https://arxiv.org/html/2608.15242v3) | [TeX 源码](https://arxiv.org/src/2608.15242)
* **DOI：** [10.48550/arXiv.2608.15242](https://doi.org/10.48550/arXiv.2608.15242)
* **引用与参考：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.15242) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.15242) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.15242)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.15242) | [HTML Version](https://arxiv.org/html/2608.15242v3) | [TeX Source](https://arxiv.org/src/2608.15242)
> * **DOI:** [10.48550/arXiv.2608.15242](https://doi.org/10.48550/arXiv.2608.15242)
> * **Citations & References:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.15242) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.15242) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.15242)