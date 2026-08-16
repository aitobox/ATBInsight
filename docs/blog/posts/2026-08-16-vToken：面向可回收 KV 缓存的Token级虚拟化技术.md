---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-16
hide:
- navigation
tags:
- 大语言模型
- KV缓存
- 内存优化
- vLLM
- 虚拟化
title: vToken：面向可回收 KV 缓存的Token级虚拟化技术
---
### 文章背景与核心概要
大语言模型（LLM）的推理服务经常受到键值（KV）缓存不断增长所带来的内存瓶颈限制。尽管 *PagedAttention* 通过使用固定大小的内存块成功缓解了分配器层面的内存碎片，但由于现代 KV 淘汰算法运行在更精细的 Token 级别，它依然面临严重的**块内碎片（intra-block fragmentation）**问题。

为了解决这一痛点，**vToken** 引入了一种轻量级的虚拟化层，将逻辑 Token 的活跃状态与物理块的放置位置进行解耦。通过利用 Token 表间接寻址和异步物理重打包（repacking），vToken 在保持与现有 PagedAttention 内核以及 CUDA Graphs 兼容的同时，消除了块内部的内存浪费。

---

# vToken: Token-Level Virtualization for Reclaimable KV Caches

**arXiv:** [2608.13263](https://arxiv.org/abs/2608.13263)  
**Submitted:** 13 August 2026  
**Authors:** Yuanhang Gao, Xiangrui Yang, Yuanfeng Chen, Hongjia Chen, Qianru Lv, Wenfei Wu, Dongsheng Li

---

## Summary
大语言模型（LLM）服务经常受到由键值（KV）缓存增长引起的内存瓶颈的限制。虽然 *PagedAttention* 成功地使用固定大小的内存块缓解了分配器层面的碎片，但由于现代 KV 淘汰算法运行在更精细的 Token 级别粒度上，它遭遇了**块内碎片**的问题。

> Large Language Model (LLM) serving is frequently constrained by memory bottlenecks caused by the growth of Key-Value (KV) caches. While *PagedAttention* successfully mitigates allocator-level fragmentation using fixed-size memory blocks, it suffers from **intra-block fragmentation** because modern KV eviction algorithms operate at a finer, token-level granularity. 

vToken 引入了一个轻量级的虚拟化层，将逻辑 Token 的活跃性与物理块的放置位置解耦。通过利用 Token 表间接寻址和异步物理重打包，vToken 消除了块内浪费的内存，同时保持了与现有 PagedAttention 内核和 CUDA Graphs 的兼容性。

> **vToken** introduces a lightweight virtualization layer that decouples logical token liveness from physical block placement. By utilizing token-table indirection and asynchronous physical repacking, vToken eliminates wasted memory within blocks while maintaining compatibility with existing PagedAttention kernels and CUDA Graphs.

---

## Key Contributions
*   **Token-Level Virtualization:** Decouples the logical view of tokens from their physical storage, allowing for efficient, granular reclamation.
*   **Asynchronous Repacking:** Enables physical memory reclamation without disrupting the logical sequence flow.
*   **Performance Gains:**
    *   Reduces retained KV blocks per request by **27.2% – 72.3%**.
    *   Improves SLA-constrained throughput by up to **1.37×**.
    *   Extends maximum feasible concurrency by up to **2×** under constrained budgets.
*   **Developer Efficiency:** Reduces the integration footprint for new eviction policies from 500+ lines of code to under 50.

> ## 主要贡献
*   **Token 级虚拟化：** 将 Token 的逻辑视图与其物理存储解耦，从而实现高效、精细化的内存回收。
*   **异步重打包：** 能够在不中断逻辑序列流的情况下实现物理内存回收。
*   **性能提升：**
    *   将每个请求保留的 KV 块减少了 **27.2% – 72.3%**。
    *   在满足 SLA 约束的吞吐量上提升高达 **1.37 倍**。
    *   在受限预算下，将最大可行并发度扩展高达 **2 倍**。
*   **开发效率：** 将新淘汰策略的集成代码量从 500 多行代码缩减至 50 行以下。

---

## Technical Details
*   **Compatibility:** Fully preserves PagedAttention kernels and CUDA Graph support.
*   **Implementation:** Developed and evaluated within the [vLLM](https://github.com/vllm-project/vllm) framework.
*   **Evaluation Benchmarks:** Tested against H2O, Random, and Scissorhands eviction policies.

> ## 技术细节
*   **兼容性：** 完全保留了 PagedAttention 内核以及对 CUDA Graph 的支持。
*   **实现：** 在 [vLLM](https://github.com/vllm-project/vllm) 框架内开发并进行了评估。
*   **评估基准：** 针对 H2O、Random 和 Scissorhands 淘汰策略进行了测试。

---

## Access & Resources
*   **Full Paper:** [View PDF](https://arxiv.org/pdf/2608.13263)
*   **Experimental HTML:** [View HTML](https://arxiv.org/html/2608.13263v1)
*   **Source Code:** [TeX Source](https://arxiv.org/src/2608.13263)
*   **DOI:** [10.48550/arXiv.2608.13263](https://doi.org/10.48550/arXiv.2608.13263)

> ## 获取与资源
*   **完整论文：** [查看 PDF](https://arxiv.org/pdf/2608.13263)
*   **实验性 HTML：** [查看 HTML](https://arxiv.org/html/2608.13263v1)
*   **源代码：** [TeX 源码](https://arxiv.org/src/2608.13263)
*   **DOI：** [10.48550/arXiv.2608.13263](https://doi.org/10.48550/arXiv.2608.13263)

---

*Subjects: Artificial Intelligence (cs.AI); Distributed, Parallel, and Cluster Computing (cs.DC); Operating Systems (cs.OS)*