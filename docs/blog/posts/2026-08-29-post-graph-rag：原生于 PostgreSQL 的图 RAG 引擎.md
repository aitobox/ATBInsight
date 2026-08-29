---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- GraphRAG
- PostgreSQL
- pgvector
- 知识图谱
- 检索增强生成
title: post-graph-rag：原生于 PostgreSQL 的图 RAG 引擎
---
### 文章背景与核心概要

`post-graph-rag` 旨在解决传统多存储架构 Graph RAG 实现中常见的逻辑缺陷与基础设施冗余问题。传统的 Graph RAG 系统通常依赖于向量数据库、图数据库和文档存储的组合，这不仅带来了巨大的同步开销，还常因缺乏质量控制导致图结构被噪声污染，且难以处理事实的时序演变。

该引擎的核心创新在于将文本分块（通过 `pgvector` 实现向量化）、规范化实体图以及社区摘要统一整合进单一的 PostgreSQL 数据库中。通过引入提取阶段的“不变性约束”（Invariants），该系统能够有效过滤噪声、规范化谓词并解析实体。此外，它还内置了时序层，支持对事实演变的追踪及“截至某时”（as-of）的查询，在保持高性能的同时，显著提升了图的密度与查询质量。

---

## 执行摘要

`post-graph-rag` 是一个开源的、原生于 PostgreSQL 的图检索增强生成（Graph RAG）引擎，旨在解决传统多存储 Graph RAG 实现中常见的架构和逻辑缺陷。

> `post-graph-rag` is an open-source, PostgreSQL-native Graph Retrieval-Augmented Generation (RAG) engine designed to solve the infrastructural and logical flaws common in traditional multi-store Graph RAG implementations. 

传统的 Graph RAG 引擎通常存在三个主要问题：
1. **基础设施开销：** 需要独立的向量存储、图数据库和文档存储，且必须保持数据同步。
2. **图质量低下：** 提取流水线盲目接收输出，导致图中充斥着无意义或过于模糊的边。
3. **缺乏时序感知：** 引擎只是随时间累积数据，将过时的事实与当前事实同等对待。

> Traditional Graph RAG engines typically suffer from three major issues:
> 1. **Infrastructure Overhead:** Requiring separate vector stores, graph databases, and document stores that must be kept consistently in sync.
> 2. **Poor Graph Quality:** Extraction pipelines that blindly accept outputs, polluting the graph with meaningless or overly vague edges.
> 3. **Lack of Temporal Awareness:** Engines that simply accumulate data over time, treating superseded facts and current facts identically.

`post-graph-rag` 将文本分块（通过 `pgvector` 提供嵌入）、规范化实体图和社区摘要整合到一个 PostgreSQL 数据库中。它引入了提取时的不变性约束来过滤噪声、规范化谓词、将实体解析为规范顶点，并结合了一个能够追踪事实演变并回答“截至某时”查询的时序层。

> `post-graph-rag` consolidates text chunks (with embeddings via `pgvector`), a canonical entity graph, and community summaries into a single PostgreSQL database. It introduces extraction-time invariants to filter out noise, normalizes predicates, resolves entities to canonical vertices, and incorporates a temporal layer capable of tracking the evolution of facts and answering as-of queries.

---

## 关键特性与架构

### 1. 统一的 PostgreSQL 基础设施
* **单一数据库解决方案：** 消除了同步不同向量数据库、图存储和文档存储的复杂性。
* **核心技术：** 利用 `pgvector` 进行相似度搜索，并结合针对图遍历优化的关系边表。

> ### 1. Unified PostgreSQL Infrastructure
> * **Single Database Solution:** Eliminates the complexity of synchronizing disparate vector databases, graph stores, and document stores.
> * **Core Technologies:** Utilizes `pgvector` for similarity search alongside relational edge tables optimized for graph traversal.

### 2. 提取阶段的不变性约束
在数据写入数据库之前，引擎会运行严格的验证不变性约束：
* 拒绝模糊的谓词、代词名称和纯数量描述。
* 将谓词规范化为可选的受控词汇表。
* 利用模型提供的别名将实体解析为每个规范名称下的单一顶点。
* 保留负面关系：通过在否定标志下附加正面谓词，而不是丢弃有用的上下文。

> ### 2. Extraction-Time Invariants
> Before any data is written to the database, the engine runs strict validation invariants:
> * Rejects vague predicates, pronominal names, and bare quantities.
> * Normalizes predicates onto an optional controlled vocabulary.
> * Resolves entities to a single vertex per canonical name utilizing model-supplied aliases.
> * Preserves negative relations by attaching the positive predicate under a negation flag rather than discarding useful context.

### 3. 时序层
* **有效性追踪：** 允许关系携带直接从源文本中提取的有效期。
* **文档顺序覆盖：** 根据文档顺序自动覆盖早期不兼容的断言。
* **历史查询：** 全面支持时间点（"as-of"）查询。

> ### 3. Temporal Layer
> * **Validity Tracking:** Allows relationships to carry a validity period extracted directly from the source text.
> * **Document-Order Superseding:** Automatically supersedes earlier incompatible assertions using document order.
> * **Historical Queries:** Fully supports point-in-time ("as-of") queries.

---

## 性能与工程测量

在三个不同的语料库上使用相同的提取和嵌入模型与 **LightRAG** 进行对比评估时，`post-graph-rag` 表现出：

* **更高的图密度：** 在所有场景下构建的图密度更高，每个实体的关系数最高可达 **$2.4\times$**。
* **改进的查询能力：** 每个关系的唯一边标签计数更低（0.46 到 0.58，若使用受控词汇表则为 0.11，而 LightRAG 为 0.77 到 1.33）。
* **竞争性的延迟：** 在保持较低延迟配置的同时，提供可比的查询响应。
* **时序演变：** 在一个新颖的序列和十年的备案文件中，分别成功覆盖了 13 个和 8 个关系（而基准引擎记录为零）。

> ## Performance & Engineering Measurements
> 
> When evaluated against **LightRAG** across three distinct corpora using identical extraction and embedding models, `post-graph-rag` demonstrated:
> 
> * **Higher Graph Density:** Builds denser graphs everywhere, achieving up to **$2.4\times$ the relations per entity**.
> * **Improved Queryability:** Features lower distinct edge label counts per relation (0.46 to 0.58, or 0.11 with a controlled vocabulary, compared to LightRAG's 0.77 to 1.33).
> * **Competitive Latency:** Answers queries comparably while maintaining lower latency profiles.
> * **Temporal Evolution:** Successfully superseded 13 and 8 relationships respectively on a novel sequence and a decade of filings (whereas the baseline baseline engine recorded zero).

*(注：这些数据代表工程测量结果，而非正式的基准测试声明。)*

> *(Note: These figures represent engineering measurements rather than formal benchmark claims.)*