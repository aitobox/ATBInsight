---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 社交机器人
- 大语言模型
- 多智能体系统
- 人机交互
- 机器人控制
title: MistyPilot：通过多智能体大模型技能编排实现社交机器人控制
---
### 文章背景与核心概要

随着社交机器人应用场景的日益复杂，传统的编程方式往往需要开发者手动编写API、绑定传感器事件并管理繁琐的任务状态，这极大地提高了开发门槛。MistyPilot 提出了一种基于多智能体大语言模型（LLM）的框架，旨在通过自然语言简化小型社交机器人的编程与控制流程。

该框架的核心在于一个“任务路由器（Task Router）”，它能够将指令智能地分发给两个专业智能体：负责传感器触发控制与技能调用的“物理交互智能体”，以及负责对话状态管理与多模态响应的“社交交互智能体”。通过这种分工协作，MistyPilot 不仅提升了任务执行的准确性（支持多达100种技能），还通过结果复用优化了系统效率。在物理Misty机器人上的实验及用户研究表明，该系统在降低控制方差的同时，显著提升了人机交互的易用性。

---

## 📋 摘要

MistyPilot 是一个多智能体大语言模型（LLM）框架，旨在通过自然语言简化小型社交机器人的编程过程。传统方法要求开发者手动组合API、绑定传感器事件并管理任务状态。MistyPilot 通过利用“任务路由器（Task Router）”将指令分发给两个专业智能体来解决这一问题：

> **MistyPilot** is a multi-agent Large Language Model (LLM) framework designed to simplify the programming of small social robots using natural language. Traditional methods require developers to manually compose APIs, bind sensor events, and manage task states. MistyPilot solves this by utilizing a **Task Router** that delegates instructions to two specialized agents:

1. **物理交互智能体（Physically Interactive Agent）：** 处理传感器触发的机器人控制和直接的技能调用。
2. **社交交互智能体（Social Interaction Agent）：** 管理面向对话的任务状态和依赖上下文的多模态响应（同时通过结果复用优化效率）。

> 1. **Physically Interactive Agent:** Handles sensor-triggered robot control and direct skill invocation.
> 2. **Social Interaction Agent:** Manages dialogue-oriented task states and context-dependent multimodal responses (while optimizing efficiency through result reuse).

通过在物理Misty机器人上进行的组件级测试套件和初步用户研究评估，MistyPilot 展示了高准确性（支持多达100种技能）、比单智能体基线更低的方差，以及用户对可用性的积极反馈。

> Evaluated through component-level suites on a physical Misty robot and a preliminary user study, MistyPilot demonstrates high accuracy (supporting up to 100 skills), lower variance than single-agent baselines, and positive user feedback on usability.

---

## 📄 元数据

* **arXiv ID:** [arXiv:2608.15549](https://arxiv.org/abs/2608.15549) [cs.RO]
* **学科分类:** 机器人学 (`cs.RO`)；人工智能 (`cs.AI`)
* **作者:** Xiao Wang, Lu Dong, Ifeoma Nwogu, Srirangaraj Setlur, Venu Govindaraju
* **提交日期:** 2026年8月16日
* **备注:** 已被 ECCV 2026 ACVR 研讨会录用

> * **arXiv ID:** [arXiv:2608.15549](https://arxiv.org/abs/2608.15549) [cs.RO]
> * **Subjects:** Robotics (`cs.RO`); Artificial Intelligence (`cs.AI`)
> * **Authors:** Xiao Wang, Lu Dong, Ifeoma Nwogu, Srirangaraj Setlur, Venu Govindaraju
> * **Submission Date:** August 16, 2026
> * **Comments:** Accepted at the ECCV 2026 ACVR Workshop

---

## 🔗 链接与资源

* **全文访问:** 
  * [查看 PDF](https://arxiv.org/pdf/2608.15549)
  * [HTML 版本 (实验性)](https://arxiv.org/html/2608.15549v1)
  * [TeX 源码](https://arxiv.org/src/2608.15549)
* **引用与参考:** 
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.15549)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.15549)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.15549)

> * **Full-Text Access:** 
>   * [View PDF](https://arxiv.org/pdf/2608.15549)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.15549v1)
>   * [TeX Source](https://arxiv.org/src/2608.15549)
> * **Citations & References:** 
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.15549)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.15549)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.15549)