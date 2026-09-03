---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-04
hide:
- navigation
tags:
- WebAssembly
- 数据库
- 智能体记忆
- MVCC
- PostgreSQL
title: Zeta-Lite：面向智能体记忆的并发、可分支浏览器内 SQL 数据库
---
### 文章背景与核心概要
随着隐私保护、离线运行、本地优先协作以及浏览器端 AI 智能体持久化记忆的需求日益增长，浏览器正逐渐成为一流的数据库宿主环境。然而，传统的浏览器端 SQL 方案（如将 PostgreSQL 编译为 WebAssembly 的 PGlite）继承了严格的单进程模型，无法高效处理并发事务和复杂的分支操作。

本文介绍了 **Zeta-Lite**——Zeta 数据库引擎的浏览器版本，它是一个体积仅有 2.87 MB（经过 gzipped 压缩）的 WebAssembly 制品。Zeta-Lite 依托基于日志的异步多版本并发控制（MVCC）核心，在浏览器环境中实现了两大突破性能力：单线程下的并发快照隔离事务，以及支持完整数据库分叉（Fork）、合并（Merge）和变基（Rebase）的写时复制（Copy-on-Write）分支机制。此外，它还提供了功能完备的 PostgreSQL 兼容表面（支持联表查询、CTE、窗口函数、带有 GIN 索引的 JSONB、全文检索、HNSW 向量搜索以及 SQL/PGQ 图查询）与 OPFS 持久化能力。基准测试表明，Zeta-Lite 在主流浏览器中能够保持每秒 26.8k 到 31.5k 次的点读性能，并且在数百万次混合读写操作中表现出极佳的性能稳定性，非常适合作为 AI 智能体探索和管理试探性状态的轻量级记忆底座。

---

## 摘要 (Abstract)

> Zeta-Lite: A Concurrent, Branchable In-Browser SQL Database for Agentic Memory
> 
> * **Authors:** Gene Zhang
> * **Submitted:** 1 September 2026
> * **Primary Subjects:** Databases (`cs.DB`), Artificial Intelligence (`cs.AI`)
> * **arXiv ID:** [arXiv:2609.01818 [cs.DB]](https://arxiv.org/abs/2609.01818)
> * **DOI:** [10.48550/arXiv.2609.01818](https://doi.org/10.48550/arXiv.2609.01818)

浏览器已经成为一流的数据库宿主：为了满足隐私保护、离线运行、本地优先协作，以及最近兴起的作为浏览器内 AI 智能体持久化记忆的需求，应用程序越来越倾向于完全在客户端存储、查询和处理结构化数据。在浏览器中获取 SQL 的途径之一是将 PostgreSQL 编译为 WebAssembly（即 PGlite），但这继承了 PostgreSQL 的进程模型：单一的后端连接一次只能执行一条语句并且会发生阻塞。该模型无法表达并发事务，并且将图查询、数据库分支等更丰富的功能局限于所编译的服务器碰巧包含的内容。

我们提出了 zeta-lite，即 Zeta 数据库引擎的浏览器形态：一个将 Zeta 核心服务器编译为 2.87 MB gzipped 制品的 WebAssembly 构建版本。Zeta-lite 保留了该引擎基于日志的异步多版本并发控制（MVCC）核心，从而带来了其他浏览器内 SQL 引擎所不具备的两项能力。首先，在单线程上实现重叠的快照隔离事务：多个事务持有不同的读取/提交时间戳并交错执行，它们之间具备快照隔离冲突检测机制。其次，写时复制数据库分支——整库的分叉（fork）、合并（merge）和变基（rebase）——这在浏览器 SQL 数据库中是独一无二的，在服务器端也极为罕见。

在此基础之上，zeta-lite 提供了功能完备的 PostgreSQL 兼容表面（联表查询、CTE、窗口函数、带有 GIN 索引的 JSONB、全文搜索、HNSW 向量搜索、SQL/PGQ 图查询、多数据库支持）以及到 OPFS 的快照持久化。在 Chrome、Firefox 和原生参考运行时中，zeta-lite 能够维持每秒 26.8k-31.5k 次的点读性能，并且在数百万次操作的混合读写负载下保持性能平稳。这种小巧、功能齐全且支持并发的 SQL 数据库非常适合用于智能体记忆——低成本的可分支状态使智能体能够高效地探索、检查并提交或丢弃试探性的工作。

> The browser has become a first-class database host: applications increasingly want to store, query, and reason over structured data entirely on the client - for privacy, offline operation, local-first collaboration, and, most recently, as durable memory for in-browser AI agents. One way to get SQL in the browser, compiling PostgreSQL to WebAssembly (PGlite), inherits PostgreSQL's process model: a single backend connection that executes one statement at a time and blocks. That model cannot express concurrent transactions, and it leaves richer capabilities - graph queries, database branching - to whatever the compiled server happens to include. 
> 
> We present zeta-lite, the browser form factor of the Zeta database engine: a WebAssembly build that compiles the same Zeta server down to a 2.87 MB gzipped artifact. Zeta-lite keeps the engine's log-centric asynchronous MVCC core, which yields two capabilities no other in-browser SQL engine provides. First, overlapping snapshot-isolated transactions on a single thread: multiple transactions hold distinct read/commit timestamps and interleave, with snapshot-isolation conflict detection between them. Second, copy-on-write database branching - whole-database fork, merge, and rebase - is unique in a browser SQL database and rare even in servers. 
> 
> On top of these, zeta-lite exposes a feature-complete PostgreSQL surface (joins, CTEs, window functions, JSONB with GIN indexes, full-text search, HNSW vector search, SQL/PGQ graph queries, multi-database) and snapshot-to-OPFS durability. Across Chrome, Firefox, and a native reference runtime, zeta-lite sustains 268k-315k point reads/s and holds a mixed read/write workload flat over millions of operations. This small, fully-featured, concurrent SQL database is an especially good fit for agentic memory - where cheap branchable state lets an agent explore, inspect, and commit or discard speculative work.

---

## 访问论文与资源 (Access Paper & Resources)

* **全文链接：** [查看 PDF](https://arxiv.org/pdf/2609.01818) | [HTML (实验性)](https://arxiv.org/html/2609.01818v1) | [TeX 源码](https://arxiv.org/src/2609.01818)
* **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) [![license icon](./images/345c7ad61f1b.png)](http://creativecommons.org/licenses/by/4.0/)

> * **Full-Text Links:** [View PDF](https://arxiv.org/pdf/2609.01818) | [HTML (Experimental)](https://arxiv.org/html/2609.01818v1) | [TeX Source](https://arxiv.org/src/2609.01818)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) [![license icon](./images/345c7ad61f1b.png)](http://creativecommons.org/licenses/by/4.0/)