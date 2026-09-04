---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 大语言模型
- KV缓存
- 推理优化
- 内存管理
- PagedAttention
title: GrowPage：用于高效大模型推理服务的按需 KV 预算管理
---
### 文章背景与核心概要
大语言模型（LLM）在长文本输出的推理任务中，生成阶段所需的大规模键值（KV）缓存会带来严重的内存瓶颈。传统的 KV 压缩方法在整个解码过程中通常维持严格的、预定义的每个请求容量预算，无法适应波动的负载和不断变化的注意力需求。

为了解决这一问题，作者推出了 **GrowPage**，这是一个将 KV 容量视为动态运行时资源的按需 KV 预算管理框架。通过利用轻量级的双时间尺度查询摘要，GrowPage 可以动态缩放请求的 KV 分配额——在需求下降时压缩状态，或者在出现更广泛的注意力需求时获取新的物理内存页。GrowPage 与 PagedAttention 无缝集成，保留了连续批处理（continuous batching）和前缀缓存（prefix caching），最终在性能与吞吐量之间实现了优于现有技术的权衡。

---

# GrowPage: On-Demand KV Budgeting for Efficient LLM Reasoning Serving

**Authors:** Qiankun Ma, Yanjiang Zhou, Zinan Xiong, Haofei Wang, Zhen Song, Yang Xiang, Ziyao Zhang, Hairong Zheng  
**Subject:** Artificial Intelligence (`cs.AI`)  
**arXiv ID:** [`2609.03494`](https://arxiv.org/abs/2609.03494)  
**Submitted:** September 3, 2026  

---

## 📌 Summary

> Long-output reasoning tasks in Large Language Models (LLMs) create a severe memory bottleneck due to the massive Key-Value (KV) cache required during generation. Traditional KV compression methods maintain a strict, predefined per-request capacity budget throughout decoding, failing to adapt to fluctuating workloads and evolving attention demands. 

> To solve this, the authors introduce **GrowPage**, an on-demand KV budgeting framework that treats KV capacity as a dynamic runtime resource. By utilizing lightweight dual-timescale query summaries, GrowPage dynamically scales a request's KV allocation—compressing states when demand drops or acquiring new physical memory pages when broader attention needs emerge. Seamlessly integrated with PagedAttention, GrowPage preserves both continuous batching and prefix caching, ultimately achieving a superior performance-to-throughput trade-off compared to existing techniques.

---

## 📑 Abstract

> 长文本输出推理使得键值（KV）缓存成为高效大模型（LLM）服务的一个关键内存瓶颈。现有的 KV 压缩方法通常依赖于预定义的每个请求预算，并且仅调整保留哪些 KV 状态，这使得总容量在整个解码过程中保持固定。然而，推理工作负载表现出巨大的需求变化：不同的请求需要不同的 KV 容量，并且单个请求的注意力需求在生成过程中也会不断演变。我们引入了 **GrowPage**，这是一个将 KV 容量视为运行时资源的按需 KV 预算管理框架。GrowPage 维护轻量级的双时间尺度查询摘要来捕获近期和长期的注意力行为，并利用其相对注意力工作集来估计需求演变。在每个容量边界处，GrowPage 要么压缩当前分配中的 KV 状态，要么在出现更广泛需求时获取额外的物理页。通过与 PagedAttention 的页级内存抽象相集成，GrowPage 保留了连续批处理和前缀缓存。在多个模型的推理基准测试上的实验表明，与现有方法相比，GrowPage 在性能与吞吐量之间实现了更优的权衡。

> Long-output reasoning has made the key–value (KV) cache a critical memory bottleneck for efficient LLM serving. Existing KV compression methods usually rely on a predefined per-request budget and adjust only which KV states are retained, leaving the total capacity fixed throughout decoding. However, reasoning workloads exhibit substantial demand variation: different requests require different KV capacities, and the attention demand of an individual request evolves during generation. We introduce **GrowPage**, an on-demand KV budgeting framework that treats KV capacity as a runtime resource. GrowPage maintains lightweight dual-timescale query summaries to capture recent and long-term attention behaviors, and uses their relative attention working sets to estimate demand evolution. At each capacity boundary, GrowPage either compresses KV states within the current allocation or acquires an additional physical page when broader demand emerges. By integrating with PagedAttention's page-level memory abstraction, GrowPage preserves continuous batching and prefix caching. Experiments on reasoning benchmarks across multiple models show that GrowPage achieves a superior performance–throughput trade-off over existing approaches.

---

## 🔗 Links & Resources

* **Full-Text Access:**
  * [View PDF](https://arxiv.org/pdf/2609.03494)
  * [HTML Version (Experimental)](https://arxiv.org/html/2609.03494v1)
  * [TeX Source](https://arxiv.org/src/2609.03494)
* **Citations & Metrics:**
  * [DOI Link](https://doi.org/10.48550/arXiv.2609.03494)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03494)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03494)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03494)