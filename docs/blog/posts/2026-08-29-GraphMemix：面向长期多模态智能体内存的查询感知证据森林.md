---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 多模态智能体
- 长期内存
- 图记忆网络
- 组合优化
- 证据森林
title: GraphMemix：面向长期多模态智能体内存的查询感知证据森林
---
### 文章背景与核心概要
长期以来，为多模态智能体构建长期记忆一直受到两大主要缺陷的限制：一是开销高昂且与问题无关的离线摘要，二是往往会引入不完整或冗余上下文的朴素嵌入相似度匹配。

为了解决这一问题，**GraphMemix** 引入了一种组合优化图内存框架，能够动态地将记忆组织构建为**查询-感知证据森林（query-aware evidence-forests）**。通过绕过沉重的生命周期成本并检索低相似度但至关重要的互补证据，GraphMemix 在多个多模态内存基准测试中，在高准确率与低生命周期开销之间实现了全新的帕累托前沿。

---

# GraphMemix: Query-Aware Evidence Forests for Long-Term Multimodal Agent Memory

**arXiv ID:** [arXiv:2608.26983](https://arxiv.org/abs/2608.26983) [cs.AI]  
**Submitted:** August 27, 2026  
**Authors:** Geng Li, Yuhao Wang, Dong Li, Jianye Hao, Yuxin Peng  
**Links:** [View PDF](https://arxiv.org/pdf/2608.26983) | [Project Page & Code](https://github.com/ligeng0197/graphmemix)

---

## 📌 Summary

组织多模态智能体的长期记忆传统上受限于两大主要缺陷：成本高昂且与查询无关的离线摘要，以及通常会注入不完整或冗余上下文的朴素嵌入相似度匹配。

> Organizing long-term memory for multimodal agents has traditionally been limited by two major flaws: expensive, question-agnostic offline summaries, and naive embedding similarity matching that often injects incomplete or redundant context. 

为了解决这一问题，**GraphMemix** 引入了一种组合优化图记忆框架，能够动态将记忆组织构建为**查询感知的证据森林**。通过绕过繁重的生命周期成本并检索低相似度但至关重要的互补证据，GraphMemix 在多个多模态记忆基准测试中，在实现高准确率的同时保持了较低的生命周期开销，达到了全新的帕累托前沿。

> To solve this, **GraphMemix** introduces a combinatorial-optimization graph memory framework that constructs memory organization dynamically as **query-aware evidence-forests**. By bypassing heavy lifecycle costs and retrieving low-similarity yet vital complementary evidence, GraphMemix achieves a new Pareto frontier between high accuracy and low lifecycle overhead across multiple multimodal memory benchmarks.

---

## 🛠️ Core Methodology

GraphMemix 通过三个主要组件运行：

> GraphMemix operates via three main components:

1. **候选图构建**  
   利用模式（schema）和语义关系扩展多视角种子记忆，以捕获初始的、查询感知的上下文。
   > **Candidate Graph Construction**  
   > Expands multi-view seed memories leveraging schema and semantic relations to capture the initial, query-aware context.
2. **证据效用与激活成本**  
   将直接内存支持与锚点条件关系验证解耦，以主动抑制冗余或冲突的信息。
   > **Evidence Utility and Activation Costs**  
   > Decouples direct memory support from anchor-conditioned relation verification to actively suppress redundant or conflicting information.
3. **森林优化**  
   在最大证据预算下联合选择森林格式的记忆上下文，同时保持可靠的关系结构。
   > **Forest Optimization**  
   > Jointly selects a forest-formatted memory context under a maximum evidence budget while maintaining a reliable relational structure.

---

## 📋 Metadata & Additional Details

* **主要主题：** 人工智能 (`cs.AI`)
  > **Primary Subject:** Artificial Intelligence (`cs.AI`)
* **引用格式：** `arXiv:2608.26983 [cs.AI]`
  > **Cite as:** `arXiv:2608.26983 [cs.AI]`
* **DOI：** [10.48550/arXiv.2608.26983](https://doi.org/10.48550/arXiv.2608.26983)
  > **DOI:** [10.48550/arXiv.2608.26983](https://doi.org/10.48550/arXiv.2608.26983)