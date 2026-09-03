---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-04
hide:
- navigation
tags:
- 电力故障预测
- 生成式基础模型
- 扩散变压器
- 极端天气模拟
- 零样本迁移学习
title: OutageDiT：用于电力故障预测与场景模拟的生成式基础模型
---
### 文章背景与核心概要
电力故障规划要求在极端事件发生前进行严密的场景生成。然而，传统的预测方法往往面临困境，因为极端天气事件极为罕见，且单个地区的历史数据通常缺乏足够多的极端故障与恢复模式样本。

为了克服这一挑战，作者推出了 **OutageDiT**，这是一个基于美国全境全面的故障和气象记录训练而成的生成式基础模型。该模型能够统一支持点预测、不确定性量化以及条件事件模拟，并通过创新的架构设计实现了跨区域的零样本迁移学习。

---

# OutageDiT: A Generative Foundation Model for Power Outage Forecasting and Scenario Simulation

## Executive Summary
* **Authors:** Yunqin Zhu, Feng Qiu, Yao Xie  
* **Subject:** Machine Learning (`cs.LG`), Artificial Intelligence (`cs.AI`)  
* **arXiv ID:** [arXiv:2609.01896](https://arxiv.org/abs/2609.01896)  
* **Submitted:** September 1, 2026  

### Abstract Summary
Power-outage planning requires rigorous scenario generation prior to extreme events. Traditional approaches struggle because severe weather events are rare, and data from individual regions lack sufficient examples of extreme outage and restoration patterns. 

To overcome this, the authors introduce **OutageDiT**, a generative foundation model trained on comprehensive outage and weather records across the United States. 

> ## 执行摘要
> * **作者：** Yunqin Zhu, Feng Qiu, Yao Xie  
> * **研究领域：** 机器学习 (`cs.LG`)，人工智能 (`cs.AI`)  
> * **arXiv ID：** [arXiv:2609.01896](https://arxiv.org/abs/2609.01896)  
> * **提交时间：** 2026年9月1日  
> 
> ### 摘要总结
> 电力故障规划要求在极端事件发生前进行严密的场景生成。传统方法之所以举步维艰，是因为极端天气事件极其罕见，并且来自单个地区的数据缺乏足够的极端故障和恢复模式样本。
> 
> 为了克服这一问题，作者推出了 **OutageDiT**，这是一个在全美范围内的全面故障和气象记录上训练而成的生成式基础模型。

---

## Key Technical Highlights
* **Architecture:** Features a condition encoder that processes historical context and known future covariates once per forecast, coupled with a shallow flow decoder that reuses horizon-aligned states to produce complete trajectories.
* **Capabilities:** Supports point forecasting, uncertainty quantification, and conditional event simulation via a single deep generative model.
* **Performance:** Generates 7-day outage trajectories at a quarter-hour resolution, improves forecast accuracy and scenario quality over strong baselines, and demonstrates successful zero-shot transfer learning to unseen regions.

> ## 核心技术亮点
> * **架构设计：** 包含一个条件编码器（每次预测仅需处理一次历史背景和已知未来协变量），并结合了一个浅层流解码器，通过复用与预测视界对齐的状态来生成完整的轨迹。
> * **功能特性：** 通过单一深度生成模型，支持点预测、不确定性量化以及条件事件模拟。
> * **性能表现：** 能够以15分钟（刻钟）分辨率生成为期7天的故障轨迹，在预测准确度和场景质量上超越了强基线模型，并展示了向未见过地区进行成功零样本迁移学习的能力。

---

## Links & Resources
* **Full-Text Options:** 
  * [View PDF](https://arxiv.org/pdf/2609.01896)
  * [HTML Version (Experimental)](https://arxiv.org/html/2609.01896v1)
  * [TeX Source](https://arxiv.org/src/2609.01896)
* **Digital Object Identifier (DOI):** [10.48550/arXiv.2609.01896](https://doi.org/10.48550/arXiv.2609.01896)
* **Associated License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) *(License icon preserved below per instructions)*
  
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> ## 链接与资源
> * **全文选项：** 
>   * [查看 PDF](https://arxiv.org/pdf/2609.01896)
>   * [HTML 版本（实验性）](https://arxiv.org/html/2609.01896v1)
>   * [TeX 源码](https://arxiv.org/src/2609.01896)
> * **数字对象唯一标识符 (DOI)：** [10.48550/arXiv.2609.01896](https://doi.org/10.48550/arXiv.2609.01896)
> * **相关许可协议：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) *（根据说明，下方保留了许可证图标）*
>   
> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">