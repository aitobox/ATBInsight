---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-16
hide:
- navigation
tags:
- UniTraffic-Agent
- 交通视频理解
- 多模态大模型
- AI City Challenge
- 计算机视觉
title: UniTraffic-Agent：2026年AI城市挑战赛赛道3的统一交通视频推理与双重跨领域评估
---
### 文章背景与核心概要
交通视频理解在智能交通系统中扮演着至关重要的角色，能够通过分析交通事故、交通违章以及车辆与弱势道路使用者（VRU）之间的交互来提供关键洞察。然而，由于交通事件具有高度稀疏性以及摄像机视角的千变万化，为这些任务设计鲁棒的多模态大模型（MLLMs）依然面临诸多挑战。

本文介绍了 **UniTraffic-Agent**，这是 MR-CAS 团队针对第十届 AI City Challenge 赛道3（Track 3）提交的解决方案。该框架旨在应对交通异常推理（TAR）任务，并成功通过了两项极具挑战性的跨领域（Out-of-Domain）评估：**FETV**（鱼眼交通事件）和 **PSI-VQA**（行人意图推理）。通过采用“观察-推理-行动-验证”（*observe–reason–act–verify*）的工作流，UniTraffic-Agent 能够采样带时间戳的视觉证据，在单次请求中处理来自同一视频片段的所有问题，并通过特定任务的动作适配器转换响应结果。

---

# UniTraffic-Agent: Unified Traffic Video Reasoning for AI City Challenge 2026 Track 3 with Two Out-of-Domain Evaluations

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/>

## Summary
交通视频理解通过分析事故、违规以及车辆与弱势道路使用者之间的交互，在智能交通系统中发挥着关键作用。然而，由于交通事件的稀疏性质以及多样化的摄像机视角，为这些任务设计鲁棒的多模态大模型（MLLMs）仍然具有挑战性。

本文介绍了 **UniTraffic-Agent**，这是针对第十届 AI City Challenge 赛道3的 MR-CAS 解决方案。该框架处理交通异常推理（TAR）以及两项跨领域评估：**FETV**（针对鱼眼交通事件）和 **PSI-VQA**（针对行人意图推理）。利用“观察-推理-行动-验证”的工作流，UniTraffic-Agent 采样带有时间戳的视觉证据，在一个请求中处理来自单个片段的所有问题，并通过特定任务的动作适配器转换响应。

> Traffic video understanding plays a critical role in intelligent transportation systems by analyzing accidents, traffic violations, and interactions between vehicles and vulnerable road users. However, designing robust multimodal large language models (MLLMs) for these tasks remains challenging due to the sparse nature of traffic events and diverse camera viewpoints. 
>
> This paper introduces **UniTraffic-Agent**, the MR-CAS solution for Track 3 of the 10th AI City Challenge. The framework addresses Traffic Anomaly Reasoning (TAR) alongside two out-of-domain evaluations: **FETV** (for fisheye traffic events) and **PSI-VQA** (for pedestrian intention reasoning). Utilizing an *observe–reason–act–verify* workflow, UniTraffic-Agent samples timestamped visual evidence, processes all questions from a single clip within one request, and translates responses using task-specific action adapters.

---

## Document Metadata

* **arXiv ID:** [arXiv:2608.13031](https://arxiv.org/abs/2608.13031) [cs.CV]
* **Authors:** Peng Li, Qianqian Xu, Shilong Bao, Yangbangyan Jiang, and Qingming Huang
* **Submitted:** August 13, 2026
* **Primary Subject:** Computer Vision and Pattern Recognition (`cs.CV`)
* **Secondary Subjects:** Artificial Intelligence (`cs.AI`)
* **Accepted Venue:** ECCV 2026 AI City Challenge Workshop
* **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)

---

## Abstract

交通视频理解已成为智能交通中的一个重要问题，因为道路视频为事故、违规以及车辆与弱势道路使用者之间的交互提供了直接证据。一个有用的系统应该解释交通事件是如何发展的、为什么会发生以及相关的交互发生在什么时候，但这对于多模态大模型（MLLMs）来说仍然很困难，因为交通视频包含稀疏的事件和多变的视角。

我们介绍了 **UniTraffic-Agent**，这是第十届 AI City Challenge 赛道3的 MR-CAS 解决方案，其中包括交通异常推理（TAR）和两项跨领域评估：用于鱼眼交通事件的 FETV 和用于行人意图推理的 PSI-VQA。UniTraffic-Agent 遵循“观察-推理-行动-验证”的工作流，采样带有时间戳的视觉证据，对来自同一片段的所有问题在单次请求中进行推理，并通过特定任务的动作适配器转换响应。

在官方公开排行榜上，MR-CAS 取得了以下排名和得分：
* **TAR:** 排名第 16 位，得分为 `0.5780`
* **FETV:** 排名第 2 位，得分为 `0.4884`
* **PSI-VQA:** 排名第 4 位，得分为 `64.4161`

> Traffic video understanding has become an important problem in intelligent transportation, as road videos provide direct evidence for accidents, violations, and interactions between vehicles and vulnerable road users. A useful system should explain how a traffic event develops, why it happens, and when the relevant interaction occurs, yet this remains difficult for multimodal large language models (MLLMs) because traffic videos contain sparse events and varied viewpoints. 
>
> We introduce **UniTraffic-Agent**, the MR-CAS solution for Track 3 of the 10th AI City Challenge, which includes Traffic Anomaly Reasoning (TAR) and two out-of-domain evaluations: FETV for fisheye traffic events and PSI-VQA for pedestrian intention reasoning. UniTraffic-Agent follows an *observe–reason–act–verify* workflow that samples timestamped visual evidence, reasons over all questions from the same clip in one request, and converts responses through task-specific action adapters. 
>
> On the official public leaderboards, MR-CAS achieves the following rankings and scores:
> * **TAR:** Ranked 16th with a score of `0.5780`
> * **FETV:** Ranked 2nd with a score of `0.4884`
> * **PSI-VQA:** Ranked 4th with a score of `64.4161`

---

## Links & Resources

* **Paper Access:** [View PDF](https://arxiv.org/pdf/2608.13031) | [HTML (Experimental)](https://arxiv.org/html/2608.13031v1) | [TeX Source](https://arxiv.org/src/2608.13031)
* **Source Code:** [GitHub Repository](https://github.com/Roclp/UniTraffic-Agent)
* **External References:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.13031) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.13031) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.13031)