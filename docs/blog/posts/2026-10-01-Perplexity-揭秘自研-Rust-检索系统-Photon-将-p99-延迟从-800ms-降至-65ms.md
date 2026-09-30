---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-10-01
hide:
  - navigation
tags:
  - Perplexity
  - Photon
  - Rust
  - 搜索引擎架构
  - io_uring
  - 性能工程
title: "Perplexity 揭秘自研 Rust 检索系统 Photon：将 p99 延迟从 800ms 降至 65ms"
---

# Perplexity 揭秘自研 Rust 检索系统 Photon：将 p99 延迟从 800 ms 降至 65 ms

> # Perplexity Introduces Photon: A Rust-Based Retrieval Engine That Cuts p99 Latency From 800 ms to 65 ms

### 文章背景与核心概要
随着索引规模与知识库的飞速膨胀，传统开源检索引擎在面对严苛的高并发请求时，常常深陷长尾延迟高企与磁盘索引合并卡顿的泥潭。为了从根本上破除这一瓶颈，知名 AI 搜索产品 Perplexity 放弃了对原有开源分支修修补补的做法，完全采用 Rust 语言从零自研了全新的分布式检索与重排引擎 Photon。Photon 巧妙结合了自适应倒排列表、带算力预算的剪枝遍历，以及基于 Linux 顶尖内核特性 `io_uring` 的异步批量磁盘读取，成功将生产环境的 p99 检索延迟从约 800 ms 极限压缩至仅 65 ms，同时减少了 20% 的服务器基建资源需求。依托 Photon 打造的 Fast Search API 为 AI 智能体 (AI Agent) 工作流提供了兼具毫秒级极速响应与超高性价比的检索底座，为下一代 AI 搜索架构的性能演进树立了行业标杆。

---

## 概要

> ## Summary

AI 搜索领头羊 Perplexity 正式推出了自研的高性能检索与排序引擎 **Photon**，该系统完全采用 **Rust** 语言编写。在此之前，Perplexity 依赖的开源魔改引擎长期受困于尾部高延迟与磁盘索引合并卡顿；而全新登场的 Photon 不仅全面承接了 Perplexity 生产环境的所有线上流量，还驱动了全新推出的 **Fast Search** API 模式。通过巧妙运用自适应倒排列表 (Adaptive Posting Lists) 、带算力预算的遍历算法，以及基于 `io_uring` 的异步磁盘读取技术，Photon 将线上检索的 p99 延迟从约 800 ms 断崖式压降至约 65 ms，不仅节省了 20% 的服务器计算资源，更让 AI 智能体 (AI Agent) 工作流的运行成本直降 68%。

> Perplexity has introduced **Photon**, a high-performance, in-house retrieval and ranking engine written in **Rust**. Built to replace an open-source forked engine that struggled with tail latency and disk index fusion spikes, Photon powers all of Perplexity's production traffic as well as the new **Fast Search** API mode. By leveraging adaptive posting lists, budgeted traversal, and `io_uring` asynchronous reads, Photon dramatically reduces p99 retrieval latency from ~800 ms down to ~65 ms while saving 20% on serving infrastructure and enabling a 68% cost reduction for AI agent workflows.

---

## 为何 Perplexity 要替换旧引擎？

> ## Why Perplexity Replaced Its Old Engine

随着 Perplexity 索引数据量的不断膨胀，原先基于开源修改的旧版检索引擎遭遇了三大致命瓶颈：

> As Perplexity's index grew, the legacy open-source retrieval engine hit three major bottlenecks:

* **尾部延迟高企 (Tail Latency)**：生产环境的 p99 延迟一直徘徊在 800 ms 左右。由于索引数据总量远远超出了物理内存 (RAM) 的承载上限，无法使用 `mlock` 将数据全部常驻内存，导致冷读取时频繁触发严重缺页异常 (page faults) ，进而造成查询严重卡顿。
* **合并尖峰卡顿 (Merge Spikes)**：后台执行磁盘索引融合 (fusion) 操作时，会导致 p99 延迟猛增至约 1.2 秒，并且这种糟糕的卡顿每次会长达 10 到 15 分钟。
* **灾备恢复缓慢 (Slow Recovery)**：部署并同步备用集群需要耗费一周以上的时间，在此期间部分响应失败的比率也显著攀升。

> * **Tail Latency:** Production p99 latency hovered around 800 ms. Because the dataset exceeded available RAM, `mlock` was unviable, leading to major page faults and query stalls during cold reads.
> * **Merge Spikes:** Disk index fusion operations caused p99 latency to spike to ~1.2 seconds for durations of 10 to 15 minutes.
> * **Slow Recovery:** Deploying and syncing auxiliary clusters took over a week, simultaneously increasing the rate of partial responses.

面对这些难以逾越的技术障碍，Perplexity 团队清醒地意识到：与其在缝缝补补的旧开源分支上继续耗费精力，不如从零自研一套专属引擎。这不仅架构更纯粹、性能更强劲，综合维护成本也远比守着老系统更低廉。

> To overcome these hurdles, the Perplexity team determined that building a custom engine from scratch was cleaner, more performant, and cheaper than maintaining their fork.

---

## Photon 的技术实现原理

> ## How Photon Works

Photon 采用了由负载均衡器、代理 Broker 节点以及专属分片组 (shard groups) 协同编排的分布式架构：

> Photon utilizes a distributed architecture orchestrated by a load balancer, broker nodes, and dedicated shard groups:

* **自适应倒排列表 (Adaptive Posting Lists)**：针对短列表，将其直接内联保存在单个内存页中；长列表则被切分为固定文档 ID 的数据块。其中，稀疏块采用有序偏移数组搭配跳跃搜索 (galloping search) ；稠密块则使用位图 (bitmaps) 实现极速的单比特成员资格判定。
* **带预算的剪枝遍历 (Budgeted Traversal)**：借鉴类 WAND 算法的思想，系统将倒排列表划分为主导列表 (driving lists) 与探测列表 (probe lists) ，在无需逐个读取精确词频的情况下，以极低的计算代价快速评估候选文档的分数上下界。
* **Docblob 紧凑记录 (Docblob Records)**：每个文档都存储为一份紧凑格式的记录，对词项采用 Elias-Fano 编码压缩，使得重排阶段每个文档仅需进行一次查询即可搞定。
* **异步批量读取 (Batched Async Reads)**：各记录的偏移量均提前计算就绪，从而能够通过 Linux 内核的 `io_uring` 特性实施批量的异步磁盘读取。在缓存设计上，系统放弃了存在锁竞争的全局共享 LRU 列表，转而采用无锁友好的 CLOCK 淘汰策略。
* **构建与服务解耦 (Separate Build and Serve)**：由独立的构建节点直接从 YTsaurus 表中生成带版本号的分片索引，这让控制中心能够平滑无缝地轮转线上服务节点，并利用历史查询日志提前完成缓存预热。

> * **Adaptive Posting Lists:** Short lists are stored inline within a single page, while longer lists are split into fixed-document ID blocks. Sparse blocks rely on sorted offset arrays with galloping search, and dense blocks use bitmaps for single-bit membership lookups.
> * **Budgeted Traversal:** Utilizing a WAND-like algorithm, lists are separated into driving and probe lists to check candidate score bounds cheaply before reading exact term frequencies.
> * **Docblob Records:** Each document contains a compact record utilizing Elias-Fano encoding for terms, requiring only a single lookup per document during ranking.
> * **Batched Async Reads:** Record offsets are predetermined, enabling batch disk reads via `io_uring`. Caching bypasses locks by employing a CLOCK eviction policy instead of a shared LRU list.
> * **Separate Build and Serve:** Dedicated nodes build versioned shard indexes from YTsaurus tables, allowing a controller to rotate serving groups smoothly while pre-warming caches with historical query logs.

---

## 生产落地效果

> ## Production Results

全量迁移至 Photon 为 Perplexity 带来了基础设施与系统性能的双重飞跃：

> Migrating to Photon delivered massive infrastructure and performance gains:

* **p99 延迟断崖式下降**：检索与排序阶段的延迟从约 800 ms 直降至约 65 ms (仅涵盖 Photon 负责的处理阶段) 。
* **资源利用率大幅提升**：与先前的旧节点相比，Photon 运行所需的**在线服务机器数量减少了 20%**。
* **单文档数据密度更高**：单个文档所能存储的数据量提升了约 **2.5 倍**，显著增强了全局排序的准确性与质量。
* **极致内存优化**：如果采用传统方案通过 `mlock` 将同等规模的数据集强行锁在内存中，所需的常驻内存容量将达到 Photon 实际消耗的约 4.6 倍。
* **集群发布稳定可靠**：索引版本更新与切换时，再也不会出现因合并而引发的延迟飙升。

> * **p99 Latency Reduction:** Retrieval and ranking latency dropped from ~800 ms to ~65 ms (covering Photon's stages only).
> * **Resource Efficiency:** Photon operates on **20% fewer serving machines** than the legacy nodes.
> * **Higher Data Density:** It stores roughly **2.5x more data per document**, improving overall ranking quality.
> * **Memory Optimization:** Pinning the equivalent dataset via `mlock` would have required ~4.6x the resident memory Photon consumes.
> * **Stable Deployments:** Index version switches no longer cause latency spikes.

---

## Fast Search：为智能体量身定制的速度与成本优势

> ## Fast Search: Speed and Cost for Agents

借助 Photon 的强劲能力，Perplexity 搜索 API 推出了一种全新的 **Fast Search** (快速搜索) 模式 (请求参数为 `search_type: "fast"`，定价仅为每 1,000 次请求 1 美元) ，专为 AI 智能体的高频自动化调用而设计。

> Photon enables a new **Fast Search** mode via the Perplexity Search API (`search_type: "fast"` at `$1 per 1,000 requests`), tailored specifically for agentic workflows.

### 性能表现与基准测试

> ### Performance & Benchmarking

在涵盖六大基准评测集 (WideSearch、BrowseComp、DSQA、FRAMES、SEAL-0 与 SEAL-Hard) 的 3,554 项测试任务中：

> Tested across 3,554 tasks over six benchmarks (WideSearch, BrowseComp, DSQA, FRAMES, SEAL-0, and SEAL-Hard):

* **快速模式 (Fast Mode)**：准确率得分为 **64.3%**，总估算成本仅为 **$59.73**。
* **默认预设 (Default Preset)**：准确率得分为 **64.0%**，总估算成本为 **$187.60** (这使得 Fast 模式的调用成本足足便宜了约 68%) 。

> * **Fast Mode:** Scored **64.3%** at an estimated cost of **$59.73**.
> * **Default Preset:** Scored **64.0%** at an estimated cost of **$187.60** (making Fast ~68% cheaper).

*关于性能取舍的说明*：内部长尾基准测试显示，快速模式在检索相关性上略有微调牺牲 (折扣累积增益 DCG 从 2.45 下降至 2.21) ，答案可用性也有所微降 (下降 2.9 个百分点至 0.567) 。因此，Perplexity 官方建议：在日常高频的智能体循环中优先选用 Fast 模式；而在面对复杂、模糊、意图不明的深度查询时，则继续保持默认预设。

> *Note on Trade-offs:* Internal long-tail benchmarks showed a slight drop in relevance (DCG falling from 2.45 to 2.21) and answer availability (dropping 2.9 percentage points to 0.567). Perplexity recommends Fast for routine agent loops and the default preset for complex, ambiguous queries.

### 接入示例代码

> ### Integration Example

```bash
curl -X POST 'https://api.perplexity.ai/search' \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"query": "latest stable Rust release", "search_type": "fast", "max_results": 5}'
```

针对 Python SDK 版本 `0.43.4` 与 `0.43.5`，在调用时传入 `extra_body={"search_type": "fast"}` 即可启用该模式。

> For Python SDK versions `0.43.4` and `0.43.5`, pass `extra_body={"search_type": "fast"}`.

---

## Fast Search 与同类核心竞品横向对比

> ## Fast Search vs. Closest Competitors

| 特性 / 指标 | Perplexity Fast Search | Exa Instant | Parallel Search Turbo | Tavily Ultra-Fast |
| :--- | :--- | :--- | :--- | :--- |
| **请求参数** | `search_type: "fast"` | `type: "instant"` | `mode: "turbo"` | `search_depth: "ultra-fast"` |
| **厂商公开延迟** | p50 为 160 ms，p95 为 230 ms | 典型值约 250 ms；发布时曾宣称低于 200 ms | 约 200 ms | 未公开具体数据 |
| **千次请求官方标价** | $1 | 最多 10 条结果收费 $4 | $1 | 1 点积分 (依套餐不同折合 $5–$8) |
| **单次请求返回结果数** | 1 到 20 条 | 基础价格含 10 条，每额外增加 1,000 次查询加收 $1 | 未注明 | 未注明 |
| **已知限制** | 相关性略低于默认预设 | 超出额度的结果需单独计费 | 仅支持英语与日语查询 | 相关性低于其他深搜模式 |
| **发布日期** | 2026年9月24日 | 2026年2月12日 | 2026年7月13日 | 2026年1月5日 |

> | Feature | Perplexity Fast Search | Exa Instant | Parallel Search Turbo | Tavily Ultra-Fast |
> | :--- | :--- | :--- | :--- | :--- |
> | **Request Parameter** | `search_type: "fast"` | `type: "instant"` | `mode: "turbo"` | `search_depth: "ultra-fast"` |
> | **Vendor-Reported Latency** | 160 ms p50, 230 ms p95 | ~250 ms typical; sub-200 ms at launch | ~200 ms | No figure published |
> | **List Price per 1K Requests** | $1 | $4 for up to 10 results | $1 | 1 credit ($5–$8 depending on plan) |
> | **Results per Request** | 1 to 20 | 10 in base price, $1/1K extra | Not specified | Not specified |
> | **Known Limits** | Lower relevance than default preset | Extra results billed separately | English and Japanese queries only | Lower relevance than other depths |
> | **Launch Date** | September 24, 2026 | February 12, 2026 | July 13, 2026 | January 5, 2026 |

* (注：延迟数据均取自各厂商在不同测试环境下的自测公开值，并非同等受控基准下的严格对比) *。

> *(Note: Latency figures are vendor-reported under varying configurations and are not direct apples-to-apples comparisons).*

---

## 核心要点总结

> ## Key Takeaways

* **纯 Rust 自研高性能底座**：Photon 是 Perplexity 自主研发的检索与重排引擎，目前已平稳承载 100% 的线上生产流量。
* **极限压缩尾部延迟**：生产环境下的检索与排序 p99 延迟实现了断崖式剧降，从 800 ms 极限压缩至 65 ms。
* **为智能体工作流而生**：Fast Search 模式不仅提供低至 160 ms (p50) 和 230 ms (p95) 的响应速度，千次请求费用更是低至仅需 1 美元。
* **超高能效与成本控制**：在保持任务准确率基本相当的前提下，Fast Search 将智能体执行任务的检索成本骤降约 68%。
* **明确场景分工**：Fast 模式是日常标准智能体循环调用的理想之选；但在应对复杂度极高或语意模糊的疑难查询时，建议继续选用默认预设以确保最佳相关性。

> * **Rust-Powered Engine:** Photon is Perplexity’s custom retrieval and ranking engine handling 100% of production traffic.
> * **Massive Latency Drops:** Production p99 retrieval and ranking latency plummeted from 800 ms to 65 ms.
> * **Agent-Optimized:** Fast Search delivers 160 ms p50 and 230 ms p95 latencies at just $1 per 1,000 requests.
> * **Cost Efficiency:** Fast Search reduces agent task costs by roughly 68% while maintaining comparable task accuracy.
> * **Use-Case Distinction:** While ideal for standard agent loops, users should retain the default preset for hard or highly ambiguous queries due to slight relevance trade-offs.

---

*欲了解更多前沿技术细节，请参阅 Perplexity 官方发布的 [技术解读 (Technical Details)](https://www.perplexity.ai/hub/blog/photon) 与 [Fast Search 开发文档 (Fast Search Documentation)](https://docs.perplexity.ai/docs/search/fast-search)。*

> *For more information, explore the official [Technical Details](https://www.perplexity.ai/hub/blog/photon) and [Fast Search Documentation](https://docs.perplexity.ai/docs/search/fast-search).*
