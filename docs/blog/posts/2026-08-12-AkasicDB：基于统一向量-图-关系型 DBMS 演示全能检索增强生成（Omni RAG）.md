---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-12
hide:
- navigation
tags:
- AkasicDB
- Omni RAG
- 向量数据库
- 图数据库
- 检索增强生成
title: AkasicDB：基于统一向量-图-关系型 DBMS 演示全能检索增强生成（Omni RAG）
---
### 文章背景与核心概要
现代检索增强生成（RAG）应用正越来越多地将非结构化向量检索与结构化知识源（如图 RAG 和过滤向量搜索）相结合。然而，传统数据库系统在处理这些混合工作负载时往往力不从心，因为它们依赖于碎片化的库外（out-of-DB）管道或表面化的非原生集成，从而导致极高的系统开销。

为了解决这一痛点，本文作者推出了 **AkasicDB**，这是一个在单一统一执行框架内，原生支持向量相似性搜索、图遍历和关系过滤联合执行的数据库管理系统（DBMS）。AkasicDB 通过引入原生向量支持，扩展了研究团队先前的工作（*Chimera*）。依托 AkasicDB，作者展示了 **Omni RAG**——这是首个真正原生的向量-图-关系型 RAG 集成方案。该系统通过交互式聊天风格的界面，凸显了其相比传统纯向量系统更卓越的检索与推理能力。

---

# AkasicDB: Demonstrating Omni RAG with a Unified Vector-Graph-Relational DBMS

**Authors:** Geonho Lee, Jeongho Park, Donghyoung Han, Min-Soo Kim  
**Submitted:** August 10, 2026  
**Primary Subject:** Databases (`cs.DB`), Artificial Intelligence (`cs.AI`)  
**Conference/Journal Reference:** SIGMOD Companion 2026, pp. 70–73  
**Identifiers:** 
* arXiv: [2608.09214](https://arxiv.org/abs/2608.09214) 
* DOI: [10.48550/arXiv.2608.09214](https://doi.org/10.48550/arXiv.2608.09214)
* Related DOI: [10.1145/3788853.3801609](https://doi.org/10.1145/3788853.3801609)

---

## 📌 Summary

现代检索增强生成（RAG）应用程序经常需要将非结构化向量检索与结构化知识源（如图 RAG 和过滤向量搜索）结合起来。然而，传统的数据库系统在应对这些混合工作负载时举步维艰，因为它们依赖于碎片化、库外的管道，或者表面化的、非原生的集成，这导致了很高的系统开销。

> Modern Retrieval-Augmented Generation (RAG) applications frequently need to blend unstructured vector retrieval with structured knowledge sources (such as Graph RAG and filtered vector searches). However, traditional database systems struggle with these mixed workloads because they rely on fragmented, out-of-DB pipelines or superficial, non-native integrations—resulting in high system overhead. 

为了解决这一问题，作者推出了 **AkasicDB**，这是一个数据库管理系统（DBMS），它通过在单个统一的执行框架内共同执行向量相似性搜索、图遍历和关系过滤，来原生支持复杂的 RAG 工作流。AkasicDB 通过引入对向量的原生支持，扩展了团队之前的工作（*Chimera*）。通过 AkasicDB，作者演示了 **Omni RAG**——这是首个真正原生的向量-图-关系型 RAG 集成方案，它通过一个交互式的聊天风格界面，突出了其相对于传统的纯向量系统更卓越的检索和推理能力，同时也展示了现有数据库架构在支持 Omni RAG 时的实际局限性。

> To solve this, the authors introduce **AkasicDB**, a database management system (DBMS) that natively supports complex RAG workflows by jointly executing vector similarity searches, graph traversals, and relational filtering inside a single, unified execution framework. AkasicDB extends the team's previous work (*Chimera*) by introducing native vector support. Through AkasicDB, the authors demonstrate **Omni RAG**—the first truly native integration of Vector-Graph-Relational RAG—via an interactive, chat-style interface that highlights its superior retrieval and reasoning capabilities over traditional vector-only systems.

---

## 📝 Abstract

> 最近的检索增强生成（RAG）系统越来越多地将向量检索与结构化知识相结合，例如图 RAG 和过滤向量搜索。然而，现有的数据库架构很难有效地支持此类复杂的 RAG 工作流，因为它们依赖于库外管道或库内非原生集成，从而导致高昂的开销。这篇演示论文介绍了 AkasicDB，这是一个数据库系统，它通过在单个执行框架内共同执行向量相似性搜索、图遍历和关系过滤，原生支持此类 RAG 工作流。AkasicDB 扩展了我们之前的工作 Chimera，增加了对向量的原生支持以实现这种统一执行。基于 AkasicDB，我们演示了向量-图-关系型 RAG 的首次原生集成，我们将其称为 Omni RAG。通过交互式聊天风格的演示，用户可以执行和可视化 Omni RAG 查询，直接体验其优于纯向量方法的检索和推理能力，同时观察现有数据库架构在支持 Omni RAG 方面的实际局限性。

> Recent Retrieval-Augmented Generation (RAG) systems increasingly combine vector retrieval with structured knowledge, such as Graph RAG and Filtered vector search. However, existing database architectures struggle to support such complex RAG workflows efficiently, as they rely on out-of-DB pipelines or in-DB non-native integration, leading to high overhead. This demo paper presents AkasicDB, a database system that natively supports such RAG workflows by jointly executing vector similarity search, graph traversal, and relational filtering within a single execution framework. AkasicDB extends our prior work, Chimera, with native vector support to enable such unified execution. Based on AkasicDB, we demonstrate the first native integration of Vector-Graph-Relational RAG, which we refer to as Omni RAG. Through an interactive chat-style demonstration, users execute and visualize Omni RAG queries, directly experiencing its superior retrieval and reasoning over vector-only approaches while observing the practical limitations of existing database architectures in supporting Omni RAG.

---

## 🔗 Links & Resources

* **全文 PDF：** [查看 PDF](https://arxiv.org/pdf/2608.09214)
* **HTML 版本：** [arXiv HTML (实验性)](https://arxiv.org/html/2608.09214v1)
* **演示视频：** [在 YouTube 上观看](https://youtu.be/8d09_dtrEIM)
* **源码 / BibTeX：** 可通过以下 arXiv 入口页面获取：[NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.09214)、[Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.09214) 以及 [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.09214)。

> * **Full-Text PDF:** [View PDF](https://arxiv.org/pdf/2608.09214)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.09214v1)
> * **Demonstration Video:** [Watch on YouTube](https://youtu.be/8d09_dtrEIM)
> * **Source Code / BibTeX:** Available via the arXiv entry pages for [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.09214), [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.09214), and [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.09214).