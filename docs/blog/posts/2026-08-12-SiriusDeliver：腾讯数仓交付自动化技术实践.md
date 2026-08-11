---
authors:
- aitoboxrobot
categories:
- 产品发布
date: 2026-08-12
hide:
- navigation
tags:
- 腾讯
- 数据仓库
- 自动化交付
- 大模型Agent
- 数据工程
title: SiriusDeliver：腾讯数仓交付自动化技术实践
---
### 文章背景与核心概要

企业级数据仓库（DW）对于业务分析至关重要，然而其生产交付流程——涵盖上下文检索、工作流配置、代码生成、平台提交以及故障诊断——却极其复杂且高度依赖人工。尽管通用大语言模型（LLM）和代码编写智能体在软件工程领域取得了长足进步，但它们仍无法满足生产级数仓交付的严苛要求。生产级交付需要具备任务依赖感知的编排能力、生命周期感知的产物控制能力，以及持续适应演进中平台规范的能力。

为了克服这些挑战，腾讯研究团队推出了 **SiriusDeliver**，这是一个专为腾讯生产环境数仓任务提交而设计端到端交付自动化智能体。该系统通过分层交付智能体、产物生命周期控制模块以及基于轨迹驱动的技能演进机制，大幅降低了数仓工程师的负担，显著提升了交付效率与成功率。

---

# SiriusDeliver：腾讯数据仓库交付自动化

**arXiv：** [arXiv:2608.09185](https://arxiv.org/abs/2608.09185) [cs.DB]  
**提交时间：** 2026年8月10日  
**作者：** Haining Xie, Xiaokai Zhou, Jiaming Yang, Siqi Shen, Ziwei Wang, Yifeng Zheng, Tengyue Xu, Yipeng Shi, Zefang Zong, Yang Li, Peng Chen, Jie Jiang, Debiao He, Xiao Yan, Jiawei Jiang  
**主分类：** 数据库 (`cs.DB`)  
**次分类：** 人工智能 (`cs.AI`)、软件工程 (`cs.SE`)  

> **arXiv:** [arXiv:2608.09185](https://arxiv.org/abs/2608.09185) [cs.DB]  
> **Submitted:** August 10, 2026  
> **Authors:** Haining Xie, Xiaokai Zhou, Jiaming Yang, Siqi Shen, Ziwei Wang, Yifeng Zheng, Tengyue Xu, Yipeng Shi, Zefang Zong, Yang Li, Peng Chen, Jie Jiang, Debiao He, Xiao Yan, Jiawei Jiang  
> **Primary Subject:** Databases (`cs.DB`)  
> **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Software Engineering (`cs.SE`)  

---

## 📋 概要

企业级数据仓库（DW）对于业务分析至关重要，然而其生产交付流程——涵盖上下文检索、工作流配置、代码生成、平台提交以及故障诊断——却极其复杂且高度依赖人工。尽管通用大语言模型（LLM）和代码编写智能体在软件工程领域取得了长足进步，但它们仍无法满足生产级数仓交付的严苛要求，因为生产交付需要具备任务依赖感知的编排能力、生命周期感知的产物控制能力，以及持续适应演进中平台规范的能力。

> Enterprise data warehouses (DWs) are critical for business analytics, but managing the production delivery process—spanning context retrieval, workflow configuration, code generation, platform submission, and failure diagnosis—is complex and labor-intensive. While general Large Language Models (LLMs) and coding agents have advanced software engineering, they fall short of the rigorous demands of production DW delivery, which requires dependency-aware orchestration, lifecycle-aware artifact control, and continuous adaptation to evolving platform practices. 

为了克服这些挑战，作者们推出了 **SiriusDeliver**，这是一个专为腾讯生产环境数仓任务提交而设计的端到端交付自动化智能体。

> To overcome these challenges, the authors introduce **SiriusDeliver**, an end-to-end delivery automation agent designed for production warehouse task submission at Tencent. 

### SiriusDeliver 的核心组件
1. **分层交付智能体（Hierarchical Delivery Agent）：** 负责编排各项专用的数仓技能。
2. **产物生命周期控制模块（Artifact Lifecycle Control Module）：** 在平台执行前后对交付产物进行验证与修正。
3. **轨迹驱动的技能演进机制（Trace-Driven Skill Evolution Mechanism）：** 从过往的交付轨迹中动态提取并维护可复用的技能。

> ### Key Components of SiriusDeliver
> 1. **Hierarchical Delivery Agent:** Orchestrates specialized warehouse skills.
> 2. **Artifact Lifecycle Control Module:** Verifies and revises delivery artifacts both before and after platform execution.
> 3. **Trace-Driven Skill Evolution Mechanism:** Extracts and maintains reusable skills dynamically from past delivery trajectories.

---

## 📊 评估与结果

SiriusDeliver 通过严苛的离线数据集以及大规模真实生产部署得到了充分验证：
* **离线实验：** 在真实的数仓交付案例中，相比代表性的基线方法，展现出了更优异的交付成功率和自动化效率。
* **生产部署：** 在过去的两个月中，该系统已部署至 **6 个业务团队** 和 **4 种数仓任务类型**，服务了 **3,600 名月活跃用户**，并支持了 **18,240 次交付会话**。它实现了 **87.2% 的端到端成功率** 以及 **73.5% 的自主提交率**。
* **A/B 测试：** 为期一个月的 A/B 测试表明，SiriusDeliver 在保持同等最终交付成功率的同时，将平均交付时间从 **228 分钟大幅缩短至 23 分钟**，并将工程师的人工投入从 **95 分钟降至 11 分钟**。

> SiriusDeliver was validated through rigorous offline datasets and large-scale real-world production deployments:
> * **Offline Experiments:** Demonstrated superior delivery success and automation efficiency compared to representative baselines on real-world warehouse delivery cases.
> * **Production Deployment:** Deployed over a two-month period across **6 business teams** and **4 warehouse task types**, serving **3,600 monthly active users** and supporting **18,240 delivery sessions**. It achieved an **87.2% end-to-end success rate** and a **73.5% autonomous submission rate**.
> * **A/B Testing:** A one-month A/B test showed that SiriusDeliver drastically reduced the median delivery time from **228 to 23 minutes** and minimized engineer effort from **95 to 11 minutes**, all while maintaining comparable final delivery success rates.

---

## 📑 元数据与参考资料

* **ACM 分类：** H.2.8; I.2.7
* **备注说明：** 13页，13张图表，3个表格。正在审稿中。
* **DOI：** [10.48550/arXiv.2608.09185](https://doi.org/10.48550/arXiv.2608.09185)
* **全文链接：** [查看 PDF](https://arxiv.org/pdf/2608.09185) | [HTML（实验性）](https://arxiv.org/html/2608.09185v1) | [TeX 源码](https://arxiv.org/src/2608.09185)

> * **ACM Classification:** H.2.8; I.2.7
> * **Comments:** 13 pages, 13 figures, 3 tables. Under submission.
> * **DOI:** [10.48550/arXiv.2608.09185](https://doi.org/10.48550/arXiv.2608.09185)
> * **Full-Text Links:** [View PDF](https://arxiv.org/pdf/2608.09185) | [HTML (Experimental)](https://arxiv.org/html/2608.09185v1) | [TeX Source](https://arxiv.org/src/2608.09185)