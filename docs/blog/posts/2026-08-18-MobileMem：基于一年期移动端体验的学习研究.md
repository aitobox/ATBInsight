---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-18
hide:
- navigation
tags:
- AI Agent
- 长短期记忆
- 移动端智能
- 多模态学习
- 个人助理
title: MobileMem：基于一年期移动端体验的学习研究
---
### 文章背景与核心概要

下一代人工智能体正从单纯的问答系统向持久化的个人助理演进，旨在理解、记忆并持续从用户体验中学习。然而，现有的评估基准难以应对移动端复杂、异构、多模态且不断演变的真实场景。

MobileMem 是一个开创性的基准测试与框架，旨在评估并增强 AI 智能体在设备端的长期记忆能力。该研究基于长达一年的移动端用户体验数据，通过知识驱动的合成流水线，将碎片化的用户应用会话转化为连贯且具有时间一致性的长周期轨迹。MobileMem 不仅支持多跳推理、知识更新和隐式偏好推断，更通过从“信息检索”向“体验智能”的范式转变，使 AI 能够真正实现对过去的回忆、对当下的理解以及对未来的适应。

---

## 📋 摘要 (Summary)

MobileMem 是一个开创性的基准测试与框架，旨在评估并增强 AI 智能体在设备端的长期记忆能力。它超越了传统仅回答孤立问题的系统，立足于长达一年的异构、多模态且不断演变的移动端用户体验数据。通过利用知识驱动的合成流水线，该框架使个人 AI 助理能够通过持续的个人学习和体验智能，实现对过去的回忆、对当下的理解以及对未来的适应。

> **MobileMem** is a pioneering benchmark and framework designed to evaluate and enhance on-device long-term memory for AI agents. Moving beyond traditional systems that answer isolated questions, MobileMem is grounded in a year-scale collection of heterogeneous, multimodal, and evolving mobile user experiences. By utilizing a knowledge-grounded synthesis pipeline, the framework enables personal AI assistants to remember the past, understand the present, and adapt to the future through continuous personal learning and experiential intelligence.

---

## 📄 概览 (Overview)

* **arXiv ID:** [arXiv:2608.13606](https://arxiv.org/abs/2608.13606) [cs.AI]
* **提交日期:** 2026年8月11日
* **主要学科:** 人工智能 (`cs.AI`)
* **次要学科:** 计算与语言 (`cs.CL`)、机器学习 (`cs.LG`)、多智能体系统 (`cs.MA`)、多媒体 (`cs.MM`)
* **项目主页:** [mobilemem.openkg.cn](http://mobilemem.openkg.cn/)

> * **arXiv ID:** [arXiv:2608.13606](https://arxiv.org/abs/2608.13606) [cs.AI]
> * **Submission Date:** August 11, 2026
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Secondary Subjects:** Computation and Language (`cs.CL`), Machine Learning (`cs.LG`), Multiagent Systems (`cs.MA`), Multimedia (`cs.MM`)
> * **Project Page:** [mobilemem.openkg.cn](http://mobilemem.openkg.cn/)

---

## 👥 作者 (Authors)

Xinle Deng, Yida Xue, Xiangyuan Ru, Haoming Xu, Shuofei Qiao, Mengru Wang, Yijun Chen, Buqiang Xu, Chen Jiang, Yuchen Eleanor Jiang, Lizhong Wang, Jianfeng Wang, Li Zeng, Haofen Wang, Guilin Qi, Huajun Chen, Ningyu Zhang

> Xinle Deng, Yida Xue, Xiangyuan Ru, Haoming Xu, Shuofei Qiao, Mengru Wang, Yijun Chen, Buqiang Xu, Chen Jiang, Yuchen Eleanor Jiang, Lizhong Wang, Jianfeng Wang, Li Zeng, Haofen Wang, Guilin Qi, Huajun Chen, Ningyu Zhang

---

## 🔍 论文摘要 (Abstract)

下一代 AI 智能体正日益超越仅能回答孤立问题的系统，转向能够理解、记忆并持续从用户体验中学习的持久化个人助理。此类助理需要长期记忆来积累并利用用户随时间产生的特定经验，然而现有的基准测试在真实的移动端场景下仍显不足，因为这些场景下的体验具有异构性、多模态性、演变性以及高度的个人化特征。

我们引入了 **MobileMem**，这是一个用于研究设备端长期记忆的基准测试与框架，其基础是长达一年的移动端体验数据集合。MobileMem 采用知识驱动的合成流水线，从用户应用会话中构建连贯且具有时间一致性的长周期轨迹。它提供了涵盖多跳推理、时间推理、知识更新和隐式偏好推断的互补性文本与多模态设置。具体而言，MobileMem 使智能体能够回忆过去、理解当下并适应未来。通过对体验而非孤立事实进行建模，MobileMem 将记忆从信息检索提升为用于持续个人学习的体验智能。

> The next generation of AI agents is increasingly moving beyond systems that answer isolated questions toward persistent personal assistants that can understand, remember, and continuously learn from users' experiences. Such assistants require long-term memory to accumulate and leverage user-specific experiences over time, yet existing benchmarks remain inadequate for realistic mobile settings, where experiences are heterogeneous, multimodal, evolving, and deeply personal. 
>
> We introduce **MobileMem**, a benchmark and framework for studying on-device long-term memory, grounded in a year-scale collection of mobile experiences. MobileMem employs a knowledge-grounded synthesis pipeline to construct coherent and temporally consistent long-horizon trajectories from user-app sessions. It provides complementary text and multimodal settings covering multi-hop and temporal reasoning, knowledge updating, and implicit preference inference. Specifically, MobileMem enables agents to remember the past, understand the present, and adapt to the future. By modeling experiences rather than isolated facts, MobileMem moves memory beyond information retrieval toward experiential intelligence for continuous personal learning.

---

## 🔗 快速链接与资源 (Quick Links & Resources)

* [查看 PDF](https://arxiv.org/pdf/2608.13606)
* [HTML 版本 (实验性)](https://arxiv.org/html/2608.13606v1)
* [TeX 源码](https://arxiv.org/src/2608.13606)
* [DOI 链接](https://doi.org/10.48550/arXiv.2608.13606)

> * [View PDF](https://arxiv.org/pdf/2608.13606)
> * [HTML Version (Experimental)](https://arxiv.org/html/2608.13606v1)
> * [TeX Source](https://arxiv.org/src/2608.13606)
> * [DOI Link](https://doi.org/10.48550/arXiv.2608.13606)