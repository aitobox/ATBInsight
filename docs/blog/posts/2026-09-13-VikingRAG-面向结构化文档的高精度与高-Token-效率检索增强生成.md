---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-13
hide:
  - navigation
tags:
  - 检索增强生成
  - RAG
  - Token效率
  - 结构化文档
  - VikingRAG
title: "VikingRAG：面向结构化文档的高精度与高 Token 效率检索增强生成"
---

### 文章背景与核心概要

检索增强生成 (Retrieval-Augmented Generation, RAG) 是大语言模型获取外部知识、抑制事实幻觉的核心技术。在处理具有层级目录等复杂结构的文档时，传统 RAG 往往需要输入大量的结构上下文以定位充足证据，这导致了极其昂贵的 Token 开销。针对这一痛点，本文提出了目录感知的语义数据管理系统 VikingRAG。该系统深度融合了语义检索与结构化路径访问，创新性地将智能体多轮检索轨迹物化为可复用的“经验边”，并引入自适应升级机制：在证据充足时仅执行单轮经验增强检索，仅在必要时才升级至多轮深度探索。实验表明，VikingRAG 在保持顶级精度的同时，将 Token 消耗大幅压缩至传统方法的 5.1%–32.5%，为企业级知识库的高效落地提供了关键范式。

---

# VikingRAG：面向结构化文档的高精度与高 Token 效率检索增强生成

> # VikingRAG: Accurate and Token-efficient Retrieval-augmented Generation over Structured Documents

## 概要

> ## Summary

**VikingRAG** 是一个新颖的目录感知语义数据管理系统，旨在增强面向结构化文档的检索增强生成 (Retrieval-Augmented Generation, RAG) 表现。尽管现代 RAG 方法能够利用文档结构来获取充足的证据，但它们通常会产生海量的 Token 成本。VikingRAG 通过紧密整合语义检索与结构访问，实现了结构上下文高效、证据缺口驱动的多轮检索，有效攻克了这一难题。为了进一步最小化多轮交互的系统开销，该系统将智能体检索轨迹物化为“经验边” (experience edges)，以便在遇到相似查询时直接复用。此外，系统还引入了自适应升级策略：默认优先采用低成本的单轮经验增强检索，仅在证据不足时才触发多轮探索。实验证明，VikingRAG 在达到行业顶尖准确率的同时，将 Token 消耗大幅降至传统方法的极小一部分。

> **VikingRAG** is a novel directory-aware semantic data management system designed to enhance retrieval-augmented generation (RAG) over structured documents. While modern RAG methods leverage document structures to gather evidence, they typically incur massive token costs. VikingRAG addresses this by integrating semantic and structural access to drive structural-context-efficient, evidence-gap-driven multi-round retrieval. To minimize the overhead of multi-round interactions, the system materializes agentic retrieval traces as "experience edges" that can be reused for similar queries. Furthermore, it introduces an adaptive escalation strategy that defaults to cost-effective, one-round experience-augmented retrieval, invoking multi-round exploration only when evidence is insufficient. Experiments demonstrate that VikingRAG achieves state-of-the-art accuracy while slashing token consumption to a fraction of traditional methods.

---

## 文档元数据

> ## Document Metadata

* **arXiv ID：** [arXiv:2609.11390](https://arxiv.org/abs/2609.11390) [cs.IR]
* **主要领域：** 信息检索 (`cs.IR`)
* **其他领域：** 人工智能 (`cs.AI`)，计算与语言 (`cs.CL`)，数据库 (`cs.DB`)，机器学习 (`cs.LG`)
* **提交日期：** 2026年9月10日
* **DOI：** [10.48550/arXiv.2609.11390](https://doi.org/10.48550/arXiv.2609.11390)

> * **arXiv ID:** [arXiv:2609.11390](https://arxiv.org/abs/2609.11390) [cs.IR]
> * **Primary Subject:** Information Retrieval (`cs.IR`)
> * **Other Subjects:** Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`), Databases (`cs.DB`), Machine Learning (`cs.LG`)
> * **Submission Date:** September 10, 2026
> * **DOI:** [10.48550/arXiv.2609.11390](https://doi.org/10.48550/arXiv.2609.11390)

---

## 作者

> ## Authors

* Peiyuan Gao
* Gaoyuan Zhang
* Haojie Qin
* Yahui Sun
* Qianyi Zhang
* Yunhao Zhang
* Zeyu Wang
* Wei Lu

> * Peiyuan Gao
> * Gaoyuan Zhang
> * Haojie Qin
> * Yahui Sun
> * Qianyi Zhang
> * Yunhao Zhang
> * Zeyu Wang
> * Wei Lu

---

## 摘要

> ## Abstract

当前顶尖的检索增强生成 (RAG) 方法通常利用文档的层次结构来获取充足的上下文证据，但往往伴随着巨大的 Token 消耗。为了在不牺牲高精度 RAG 表现的前提下缩减结构上下文所消耗的 Token，我们提出了 **VikingRAG**——一个目录感知的语义数据管理系统，它将语义访问与结构访问深度整合，支持高结构上下文效率、由证据缺口驱动的多轮检索。

> State-of-the-art retrieval-augmented generation (RAG) methods exploit document structures to acquire sufficient evidence, but often incur substantial token costs. To reduce structural-context tokens without compromising high RAG accuracy, we present **VikingRAG**, a directory-aware semantic data management system that tightly integrates semantic and structural access to support structural-context-efficient, evidence-gap-driven multi-round retrieval. 

为了进一步降低多轮交互的 Token 开销，我们将智能体多轮检索轨迹物化为经验边，并在遇到相似查询时复用这些经验边，从而避免了重复的多轮检索探索。此外，为了在无需复杂多轮检索的场景下进一步节省成本，我们设计了自适应升级策略：在证据充分时仅通过单轮经验增强检索即可直接生成答案，仅在证据不足时才调用智能体多轮检索。

> To further reduce token overhead of multi-round interaction, we materialize agentic multi-round retrieval traces as experience edges, and reuse these edges for similar queries, avoiding repeated multi-round exploration. To additionally reduce token costs when agentic multi-round retrieval is unnecessary, we introduce an adaptive escalation strategy that answers from one-round experience-augmented retrieval when the evidence is sufficient, and invokes agentic multi-round retrieval only otherwise. 

在真实数据集上的实验表明，基础版 **VikingRAG** 系统不仅达到了与顶尖方法相当的高精度，而且仅消耗其 **11.6%–51.9%** 的 Token。当启用检索轨迹复用与自适应升级策略后，Token 成本进一步下降至 **5.1%–32.5%**，同时依然保持了极具竞争力的准确率与实用的文档存储性能，充分展现了该成果在构建新一代 AI 知识库中的实用价值。

> Experiments on real datasets show that the base system **VikingRAG** matches high accuracy of state-of-the-art methods while consuming only **11.6%–51.9%** of their tokens. With retrieval-trace reuse and adaptive escalation, token costs drop to **5.1%–32.5%** while maintaining competitive accuracy and practical document-storage performance, showing the utility of this work for emerging AI knowledge bases.

---

## 全文与资源链接

> ## Full-Text & Resource Links

* [查看 PDF](https://arxiv.org/pdf/2609.11390)
* [HTML 版本 (实验性)](https://arxiv.org/html/2609.11390v1)
* [TeX 源码](https://arxiv.org/src/2609.11390)
* [音频摘要](https://arxiv.org/audio/2609.11390)

> * [View PDF](https://arxiv.org/pdf/2609.11390)
> * [HTML Version (Experimental)](https://arxiv.org/html/2609.11390v1)
> * [TeX Source](https://arxiv.org/src/2609.11390)
> * [Audio Summary](https://arxiv.org/audio/2609.11390)
