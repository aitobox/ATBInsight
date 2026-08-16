---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-16
hide:
- navigation
tags:
- AI Agent
- 数据库
- 内存模型
- 知识检索
- FluctlightDB
title: FluctlightDB：面向 AI Agent 的数据内存模型
---
### 文章背景与核心概要

在过去五十年的数据系统发展中，关系型模型（基于谓词匹配）和向量模型（基于相似度搜索）占据了主导地位。然而，现代 AI Agent 需要在长会话中进行基于线索驱动（cue-driven）和溯源加权（provenance-weighted）的记忆召回，现有的数据模型在处理此类任务时存在天然的局限性。

本文提出了 **FluctlightDB**，旨在将 AI Agent 的长期记忆视为一种独立的数据模型。该模型引入了独特的写入语义（编码、分离、整合、溯源）和读取语义（跨链接记忆图的线索驱动激活）。FluctlightDB 作为一个嵌入式引擎，通过 `experience()` 和 `activate()` 接口实现了这一契约，为 AI Agent 提供了一种更符合认知逻辑的记忆存储与检索方案。

---

## 摘要

> For fifty years, data systems have answered two questions. The relational model asked which records match a predicate; the vector model asked which vectors lie nearest a query. Neither was built for cue-driven, provenance-weighted recall across long sessions. We propose treating long-term agent memory as a distinct data model -- with its own write semantics (encoding, separation, consolidation, provenance) and read semantics (cue-driven activation across a linked memory graph) -- and present FluctlightDB, an embedded engine that implements this contract via experience() and activate(). We make that case carefully, not categorically: we do not claim novelty over Mem0, Zep, or HippoRAG-style memory layers, only an embedded engine contract beneath them. On LoCoMo (official evidence-recall metric; 10 conversations, 1,982 gold spans), CHORUS recalls 99.0% on an internally reproduced July 2026 run. On LongMemEval-S (500 questions, official session_recall@8), our retrieval harness scores 97.6% (488/500); end-to-end QA with our reader/judge stack scores 97.4% (487/500) -- these layers use different protocols than vendor leaderboard figures we cite for context only. On BEIR SciFact (shared MiniLM embeddings, same harness, Recall Fabric on), CHORUS/PRISM edges Chroma on nDCG@10 (0.646 vs. 0.645) and Recall@10 (0.792 vs. 0.783). We also report a small author-designed regression suite (FAMB; paraphrase n=10, other sub-tests n=1) at 100% macro -- internal validation, not peer benchmark. Strangers can verify the engine in under a minute via `pip install "fluctlightdb[native]"` and a minimal `connect() -> experience() -> activate()` script (compiled wheel, not source-only). Harnesses and frozen JSON are MIT-licensed. We claim no new neuroscience and no new transformer; we propose a missing layer of the data stack and release an engine others can reproduce and contest.

在过去五十年里，数据系统主要回答了两个问题：关系模型询问哪些记录匹配谓词；向量模型询问哪些向量最接近查询。两者都不是为长会话中基于线索驱动、溯源加权的召回而构建的。我们建议将长期 Agent 记忆视为一种独特的数据模型——具有其自身的写入语义（编码、分离、整合、溯源）和读取语义（跨链接记忆图的线索驱动激活）——并提出了 FluctlightDB，这是一个通过 `experience()` 和 `activate()` 实现该契约的嵌入式引擎。我们谨慎而非绝对地提出这一观点：我们并不声称在 Mem0、Zep 或 HippoRAG 风格的记忆层之上具有创新性，仅声称其下方的嵌入式引擎契约具有创新性。在 LoCoMo（官方证据召回指标；10 个对话，1,982 个黄金跨度）上，CHORUS 在 2026 年 7 月的内部复现运行中召回率为 99.0%。在 LongMemEval-S（500 个问题，官方 session_recall@8）上，我们的检索工具得分 97.6%（488/500）；使用我们的阅读器/判断器堆栈进行的端到端 QA 得分 97.4%（487/500）——这些层使用的协议与我们仅为背景而引用的供应商排行榜数据不同。在 BEIR SciFact（共享 MiniLM 嵌入，相同工具，开启 Recall Fabric）上，CHORUS/PRISM 在 nDCG@10（0.646 对 0.645）和 Recall@10（0.792 对 0.783）上略胜 Chroma。我们还报告了一个作者设计的回归套件（FAMB；释义 n=10，其他子测试 n=1），宏观得分为 100%——这是内部验证，而非同行基准。用户可以通过 `pip install "fluctlightdb[native]"` 和一个最小化的 `connect() -> experience() -> activate()` 脚本（编译后的 wheel 包，而非仅源代码）在不到一分钟内验证该引擎。工具和冻结的 JSON 采用 MIT 许可。我们不声称有新的神经科学或新的 Transformer；我们提出了数据栈中缺失的一层，并发布了一个其他人可以复现和质疑的引擎。

---

## 基准性能亮点

* **LoCoMo 基准：** CHORUS 实现了 **99.0%** 的证据召回率（10 个对话，1,982 个黄金跨度）。
* **LongMemEval-S：** 检索工具得分为 **97.6%**（488/500）；端到端 QA 得分为 **97.4%**（487/500）。
* **BEIR SciFact：** CHORUS/PRISM 在 `nDCG@10`（0.646 vs. 0.645）和 `Recall@10`（0.792 vs. 0.783）上略微领先于 Chroma。
* **FAMB 回归套件：** 100% 宏观内部验证（释义 $n=10$，其他子测试 $n=1$）。

> * **LoCoMo Benchmark:** CHORUS achieves **99.0%** evidence recall (10 conversations, 1,982 gold spans).
> * **LongMemEval-S:** Retrieval harness scores **97.6%** (488/500); end-to-end QA scores **97.4%** (487/500).
> * **BEIR SciFact:** CHORUS/PRISM edges Chroma on `nDCG@10` (0.646 vs. 0.645) and `Recall@10` (0.792 vs. 0.783).
> * **FAMB Regression Suite:** 100% macro internal validation (paraphrase $n=10$, other sub-tests $n=1$).

---

## 快速验证

用户可以使用预编译的 wheel 包在不到一分钟内独立验证该引擎：

> Users can independently verify the engine in under a minute using the pre-compiled wheel:

```bash
pip install "fluctlightdb[native]"
```

随后执行最小化的脚本序列：`connect()` $\rightarrow$ `experience()` $\rightarrow$ `activate()`

> Followed by a minimal script execution sequence:
> `connect()` $\rightarrow$ `experience()` $\rightarrow$ `activate()`

---

![license icon](https://github.com/voxmastery/FluctlightDB/raw/main/images/345c7ad61f1b.png)

> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">