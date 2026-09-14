---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-15
hide:
  - navigation
tags:
  - 大语言模型
  - 强化学习
  - 后训练
  - 异步计算
  - 分布式训练
title: "AsyncFlow：面向高效大模型后训练的异步流式强化学习框架"
---

### 文章背景与核心概要

在当今大语言模型 (Large Language Model, LLM) 的研发体系中，后训练阶段的强化学习 (Reinforcement Learning, RL) 已成为激发模型深度推理与泛化能力的关键核心技术。然而，现有的强化学习系统架构往往面临严峻的技术困境：同机部署架构难以应对大规模集群扩展，任务解耦架构则受阻于繁复的数据流交互与计算硬件的空转等待，且大多数主流框架均与特定的训练或推理底层引擎深度绑定。针对这一系列痛点，研究团队提出了专为高效后训练量身打造的异步流式强化学习框架 AsyncFlow。该框架凭借全流式分布式数据存储与调度传输模块、允许在参数陈旧度阈值内延迟更新的异步生产者-消费者工作流，以及架构层面上与底层引擎彻底解耦的面向服务接口设计，成功消除了硬件资源空转，取得了相比业内顶尖基准平均 1.59 倍的显著吞吐量提升，为下一代大规模强化学习训练系统的设计提供了重要的工程启示。

---

# AsyncFlow：面向高效大模型后训练的异步流式强化学习框架

> # AsyncFlow: An Asynchronous Streaming RL Framework for Efficient LLM Post-Training

## 核心概述

> ## Summary

强化学习 (Reinforcement Learning, RL) 已成为大语言模型 (Large Language Model, LLM) 后训练阶段不可或缺的关键技术。然而，传统的强化学习框架面临着严峻的局限性：将训练与生成任务同机部署的系统往往受限于扩展性瓶颈；将任务物理分离部署的系统则在处理复杂数据流与硬件资源空转等待方面步履维艰；此外，绝大多数现有框架都与特定的训练或推理引擎深度绑定，缺乏通用性。

> Reinforcement learning (RL) has become critical in the post-training phase of Large Language Models (LLMs). However, traditional RL frameworks face severe limitations: task-collocated systems suffer from scalability bottlenecks, task-separated systems struggle with complex dataflows and resource idling, and most frameworks are tightly coupled to specific training or inference engines. 

为了突破这些瓶颈，研究人员推出了 **AsyncFlow**——一个专为大模型后训练设计的异步流式强化学习框架，其核心特性包括：
* **分布式数据存储与传输模块**：提供全局全景式数据管理与细粒度调度能力，天然支持全流式传输，实现自动化流水线重叠与动态负载均衡。
* **异步生产者-消费者工作流**：在预设的参数陈旧度 (Staleness) 容忍阈值内，策略性推迟参数同步更新，从而将计算设备的空闲等待时间压缩至最低。
* **计算架构完全解耦**：彻底摆脱与底层具体训练和推理引擎的强绑定，通过面向服务的 API 接口对外开放，提供高度模块化与灵活定制的使用体验。
* **卓越的系统性能**：相较于业界领先的基准系统，取得了平均 **1.59 倍**的端到端吞吐量提升。

> To overcome these challenges, researchers introduce **AsyncFlow**, an asynchronous streaming RL framework featuring:
> * A **distributed data storage and transfer module** for panoramic data management, fine-grained scheduling, automated pipeline overlapping, and dynamic load balancing.
> * An **asynchronous producer-consumer workflow** designed to minimize computational idleness by strategically deferring parameter updates within predefined staleness thresholds.
> * **Architectural decoupling** from underlying training and inference engines, exposed via service-oriented user interfaces for a modular and customizable experience.
> * **Superior performance**, demonstrating an average throughput increase of **1.59x** compared to state-of-the-art baselines.

---

## 论文元数据与发布信息

> ## Metadata & Publication Details

| 字段 | 详情 |
| :--- | :--- |
| **arXiv ID** | [arXiv:2507.01663](https://arxiv.org/abs/2507.01663) [cs.LG] |
| **主分类** | 机器学习 (`cs.LG`)、人工智能 (`cs.AI`) |
| **提交历史** | • **v1:** 2025年7月2日<br>• **v2 (当前版本):** 2026年9月11日 |
| **DOI** | [10.48550/arXiv.2507.01663](https://doi.org/10.48550/arXiv.2507.01663) |
| **许可协议** | [Creative Commons Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/) ![license icon](./images/5283893486a4.png) |

> | Field | Details |
> | :--- | :--- |
> | **arXiv ID** | [arXiv:2507.01663](https://arxiv.org/abs/2507.01663) [cs.LG] |
> | **Primary Subject** | Machine Learning (`cs.LG`), Artificial Intelligence (`cs.AI`) |
> | **Submission History** | • **v1:** Jul 2, 2025<br>• **v2 (Current):** Sep 11, 2026 |
> | **DOI** | [10.48550/arXiv.2507.01663](https://doi.org/10.48550/arXiv.2507.01663) |
> | **License** | [Creative Commons Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/) ![license icon](./images/5283893486a4.png) |

---

## 作者信息

> ## Authors

* Zhenyu Han, Ansheng You, Haibo Wang, Kui Luo, Guang Yang, Wenqi Shi, Menglong Chen, Sicheng Zhang, Zeshun Lan, Chunshi Deng, Huazhong Ji, Wenjie Liu, Yu Huang, Yixiang Zhang, Chenyi Pan, Jing Wang, Xin Huang, Chunsheng Li, Jianping Wu

> * Zhenyu Han, Ansheng You, Haibo Wang, Kui Luo, Guang Yang, Wenqi Shi, Menglong Chen, Sicheng Zhang, Zeshun Lan, Chunshi Deng, Huazhong Ji, Wenjie Liu, Yu Huang, Yixiang Zhang, Chenyi Pan, Jing Wang, Xin Huang, Chunsheng Li, Jianping Wu

---

## 论文摘要

> ## Abstract

强化学习 (Reinforcement Learning, RL) 已成为大语言模型 (Large Language Model, LLM) 后训练阶段的关键支柱技术。传统的同机共存强化学习框架面临着严峻的扩展性瓶颈，而任务解耦分离的强化学习框架在管理复杂数据流与解决计算资源闲置方面也遭遇重重挑战。此外，多数现存框架与底层的大模型训练或推理引擎深度绑定，难以灵活支持自主定制的计算引擎。为了应对这些挑战，我们提出了专为高效后训练量身打造的异步流式强化学习框架 AsyncFlow。具体而言，我们引入了一个分布式数据存储与传输模块，以全流式传输的方式提供全局全景式数据管理与细粒度调度能力。该架构天然支持强化学习各项任务之间的自动化流水线重叠与动态负载均衡。此外，我们提出了一种异步生产者-消费者工作流，通过在陈旧度容忍阈值内策略性推迟参数更新过程，从而最大限度减少计算资源的等待与闲置。最后，AsyncFlow 的核心功能在架构层面上与底层训练及推理引擎完全解耦，并封装为面向服务的用户接口，带来了高度模块化与可定制的用户体验。大量的实验结果表明，与当前最先进的基准系统相比，AsyncFlow 实现了平均 1.59 倍的吞吐量提升。本文所提出的系统架构为设计下一代强化学习训练系统提供了极具落地价值的实践见解。

> Reinforcement learning (RL) has become a pivotal technology in the post-training phase of large language models (LLMs). Traditional task-collocated RL frameworks suffer from significant scalability bottlenecks, while task-separated RL frameworks face challenges in managing complex dataflows and resolving resource idling. Furthermore, most existing frameworks are tightly coupled with LLM training or inference engines, making them difficult to support custom-designed engines. To address these challenges, we propose AsyncFlow, an asynchronous streaming RL framework tailored for efficient post-training. Specifically, we introduce a distributed data storage and transfer module that provides panoramic data management and fine-grained scheduling capabilities in a fully streamed manner. This architecture inherently enables automated pipeline overlapping among RL tasks and dynamic load-balancing. Moreover, we propose an asynchronous producer-consumer workflow, which is engineered to minimize computational idleness by strategically deferring the parameter update process within staleness thresholds. Finally, the core capabilities of AsyncFlow are architecturally decoupled from underlying training and inference engines and encapsulated by service-oriented user interfaces, offering a modular and customizable user experience. Extensive experiments demonstrate an average throughput of 1.59x compared to the state-of-the-art baseline. The architecture presented in this work provides actionable insights for designing next-generation RL training systems.

---

## 全文获取与相关资源

> ## Access Full-Text & Resources

* **PDF 版本：** [查看 PDF](https://arxiv.org/pdf/2507.01663)
* **HTML 在线版：** [arXiv HTML (实验性)](https://arxiv.org/html/2507.01663v2)
* **TeX 源码：** [源代码 (.tar.gz)](https://arxiv.org/src/2507.01663)

> * **PDF Version:** [View PDF](https://arxiv.org/pdf/2507.01663)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2507.01663v2)
> * **TeX Source:** [Source Code (.tar.gz)](https://arxiv.org/src/2507.01663)

### 外部检索与引用索引

> ### External References & Citations

* [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2507.01663)
* [Google 学术 (Google Scholar)](https://scholar.google.com/scholar_lookup?arxiv_id=2507.01663)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2507.01663)

> * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2507.01663)
> * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2507.01663)
> * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2507.01663)
