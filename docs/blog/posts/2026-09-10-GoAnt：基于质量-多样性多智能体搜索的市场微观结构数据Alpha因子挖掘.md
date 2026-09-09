---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-10
hide:
- navigation
tags:
- Alpha因子
- 多智能体
- 质量-多样性
- 市场微观结构
- 金融AI
title: GoAnt：基于质量-多样性多智能体搜索的市场微观结构数据Alpha因子挖掘
---
### 文章背景与核心概要
自动化Alpha因子挖掘旨在严格的评估约束下，从价量面板和订单簿数据中发现符号化交易信号。传统的单智能体和多智能体系统经常面临两大主要缺陷：一是**过度拟合预测代理指标**，在考虑执行成本后往往失效；二是**冗余地探索熟悉的因子家族**，限制了行为多样性和运营鲁棒性。

为了解决这些局限性，本文推出了 **GoAnt**，这是一个*质量-多样性（Quality-Diversity）多智能体搜索框架*。GoAnt 通过共享的自适应**心智图（Mental Map）**和一个精简的**女王调度器（Queen dispatcher）**，协调具有专业分工且不进行直接通信的工作者角色（探索者 Explorer、利用者 Exploiter 和连接者 Connector）。

---

# GoAnt: Quality-Diversity Multi-Agent Search for Alpha Factor Discovery in Market Microstructure Data

**Authors:** Stella Zhao, Tommy Sha  
**ArXiv ID:** [arXiv:2609.08719 [cs.AI]](https://arxiv.org/abs/2609.08719)  
**Submitted:** September 8, 2026  
**Subjects:** Artificial Intelligence (`cs.AI`)  

---

## 📌 Summary

自动化alpha因子挖掘旨在从价量面板和订单簿数据中，在严格的评估约束下发掘符号化交易信号。传统的单智能体和多智能体系统经常遭受两大主要缺陷：**过度拟合预测代理指标**（在计入执行成本后便会崩溃），以及**冗余地探索熟悉的因子家族**（这限制了行为多样性和运营鲁棒性）。

> Automated alpha factor discovery aims to uncover symbolic trading signals from price-volume panels and order-book data within strict evaluation constraints. Traditional single- and multi-agent systems frequently suffer from two major flaws: **overfitting predictive proxies** that collapse after accounting for execution costs, and **redundantly exploring familiar factor families**, which limits behavioral diversity and operational robustness. 

为了解决这些局限性，本文引入了 **GoAnt**，一个*质量-多样性多智能体搜索框架*。GoAnt 通过共享的自适应**心智图**和一个精简的**女王调度器**，协同各个专业化且不通信的工作者角色（探索者、利用者和连接者）。

> To resolve these limitations, this paper introduces **GoAnt**, a *quality-diversity multi-agent search framework*. GoAnt coordinates specialized, non-communicating worker roles (Explorer, Exploiter, and Connector) through a shared, adaptive **Mental Map** and a compact **Queen dispatcher**. 

### 核心创新点：
> ### Key Innovations:
* **心智图与女王调度器：** 候选因子按照无信息泄露的执行配置文件进行系统化组织，每个生态位（niche）保留一个精英候选因子。女王通过显式的搜索状态摘要动态重新分配评估预算。
  * **The Mental Map & Queen Dispatcher:** Candidates are systematically organized by leakage-free execution profiles, retaining one elite candidate per niche. The Queen dynamically reallocates evaluation budgets using explicit search-state summaries.
* **有效收益协议（Effective-Yield Protocol）：** 一种与地图无关的评估协议，直接从原始评估日志中统计高质量、互不冗余的因子，为基于存档和无地图的方法提供了一个统一的基准。
  * **Effective-Yield Protocol:** A map-independent evaluation protocol that directly counts high-quality, mutually non-redundant factors from raw evaluation logs, offering a unified benchmark for both archive-based and map-free methods.
* **卓越性能：** 在真实世界的A股微观结构数据（2023–2026年）上进行评估，在同等预算下，GoAnt的质量加权收益达到了 **41.8**（价量）和 **47.6**（订单簿），分别比最强的基线高出 **57%** 和 **97%**。此外，与静态地图架构的 0.61 和 0.63 相比，GoAnt 锁定的群体保留了更强的样本外质量（达到样本内表现的 0.64 和 0.67）。
  * **Superior Performance:** Evaluated on real-world A-share microstructure data (2023–2026), GoAnt achieves quality-weighted yields of **41.8** (price-volume) and **47.6** (order-book), outperforming the strongest baseline by **57%** and **97%** under matched budgets. Furthermore, GoAnt's locked populations retain robust out-of-sample quality (0.64 and 0.67 of in-sample performance) compared to 0.61 and 0.63 for static map architectures.

---

## 📋 Bibliographic & Access Information

* **Citation:** `Zhao, S., & Sha, T. (2026). GoAnt: Quality-Diversity Multi-Agent Search for Alpha Factor Discovery in Market Microstructure Data. arXiv:2609.08719 [cs.AI].`
* **DOI:** [10.48550/arXiv.2609.08719](https://doi.org/10.48550/arXiv.2609.08719)
* **Full-Text Links:** 
  * [View PDF](https://arxiv.org/pdf/2609.08719)
  * [HTML Version (Experimental)](https://arxiv.org/html/2609.08719v1)
  * [TeX Source](https://arxiv.org/src/2609.08719)
* **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) *(License icon preserved below per instructions)*:
  <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/>