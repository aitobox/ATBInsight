---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- KV-cache
- 多智能体系统
- 模型推理优化
- 内存管理
- 大语言模型
title: GraniKV：针对具有长共享前缀的多智能体系统的非对称粒度KV缓存分页
---
### 文章背景与核心概要
在当前的生产级分页推理引擎中，通常对键值（KV）缓存采用统一的分页粒度。然而，多智能体工作负载通常包含两个截然不同且存储需求冲突的区域：一个是需要高度连续性的长共享前缀，另一个则是受益于细粒度分配的单个请求后缀。这种存储需求的矛盾导致现有系统在处理多智能体交互时效率低下。

为了解决这一痛点，本文提出了 **GraniKV**，这是一个专为多智能体系统设计的非对称 KV 缓存分页层。它将存储空间巧妙地拆分为两部分：用于共享前缀的“连续热池”（Contiguous HOT pool）和用于后缀的“Token级冷池”（Token-level COLD pool）。结合能够动态选择最优后端（应对计算、内存或通信受限状态）的逐步调度器，GraniKV 显著提升了吞吐量。在共享 Token 长度 $L_p = 16\text{K}$ 的情况下，与标准生产基线相比，GraniKV 在输出 Token 吞吐量上实现了巨大的性能提升。

---

# GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix

**Authors:** Jinhyun Jeon, Sungjoo Yoo  
**Submitted On:** August 16, 2026  
**Subjects:** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`)  
**arXiv Identifier:** [arXiv:2608.15584 [cs.LG]](https://arxiv.org/abs/2608.15584) | [DOI](https://doi.org/10.48550/arXiv.2608.15584)

---

## Summary

生产级分页推理引擎通常对键值（KV）缓存应用统一的分页粒度。然而，多智能体工作负载具有两个截然不同的区域，其存储需求相冲突：一个长共享前缀需要高连续性，而每个请求的后缀则受益于细粒度分配。

> Production paged-serving engines typically apply a uniform paging granularity to the Key-Value (KV) cache. However, multi-agent workloads feature two distinct regions with conflicting storage demands: a long shared prefix that requires high contiguity, and a per-request suffix that benefits from fine-grained allocation. 

为了解决这个问题，**GraniKV** 引入了一个专门为多智能体系统设计的非对称 KV 缓存分页层。它将存储拆分为：
1. **用于共享前缀的连续 HOT 池（A contiguous HOT pool）**。
2. **用于后缀的 Token 级 COLD 池（A token-level COLD pool）**。

> To address this, **GraniKV** introduces an asymmetric KV-cache paging layer designed specifically for multi-agent systems. It splits storage into:
> 1. **A contiguous HOT pool** for the shared prefix.
> 2. **A token-level COLD pool** for the suffix.

结合一个按步调度器（per-step dispatcher），该调度器动态选择最优后端（处理计算受限、内存受限或通信受限的状态），GraniKV 显着提高了吞吐量。在 $L_p = 16\text{K}$ 共享 Token 下，与标准生产基线相比，GraniKV 在输出 Token 吞吐量上实现了巨大的增益：
* 在 Llama-3.1-8B/TP=1 上提升 **$2.16\times$**
* 在 Qwen-2.5-14B/TP=2 上提升 **$1.98\times$**
* 在 Qwen-2.5-32B/TP=4 上提升 **$1.57\times$**

> Coupled with a per-step dispatcher that dynamically selects the optimal backend (handling compute-, memory-, or communication-bound regimes), GraniKV significantly improves throughput. At $L_p = 16\text{K}$ shared tokens, GraniKV achieves massive gains in output-token throughput over standard production baselines:
> * **$2.16\times$** on Llama-3.1-8B/TP=1
> * **$1.98\times$** on Qwen-2.5-14B/TP=2
> * **$1.57\times$** on Qwen-2.5-32B/TP=4

---

## Abstract

生产级分页推理引擎对 KV 缓存应用统一的分页粒度，尽管多智能体工作负载的两个区域具有相反的存储要求：长共享前缀需要连续性，而每个请求的后缀需要细粒度分配。

> Production paged-serving engines apply uniform paging granularity to the KV cache, even though the two regions of a multi-agent workload have opposite storage requirements: a long shared prefix demands contiguity, while the per-request suffix demands fine-grained allocation.

我们提出了 **GraniKV**，这是一个 KV 缓存层，它在连续的 HOT 池中分配共享前缀，在 Token 级 COLD 池中分配后缀，并结合了一个按步调度器，该调度器在每个机制（计算、内存或通信受限）的双后端中选择合适的后端。据我们所知，GraniKV 是第一个将非对称分页粒度应用于生产级分页推理引擎的 KV 缓存的系统。

> We present **GraniKV**, a KV-cache layer that allocates the shared prefix in a contiguous HOT pool and the suffix in a token-level COLD pool, combined with a per-step dispatcher which selects the appropriate backend among dual backends for each regime (compute-, memory-, or communication-bound). To the best of our knowledge, GraniKV is the first system to apply asymmetric paging granularity to the KV cache of a production paged-serving engine.

在 $L_p=16\text{K}$ 共享 Token 下，与生产基线相比，GraniKV 在 Llama-3.1-8B/TP=1、Qwen-2.5-14B/TP=2 和 Qwen-2.5-32B/TP=4 上分别达到了 **$2.16\times$**、**$1.98\times$** 和 **$1.57\times$** 的输出 Token 吞吐量。增益分解如下：级联注意力（cascade attention）集成在饱和时贡献了主要部分；非对称存储层增加了 $1.05\text{--}1.15\times$ 的端到端性能，同时这也是使批处理 GEMM 前缀后端成为可能的核心。在具有不同长度的不同提示词的异构多智能体服务下，归因发生了反转：GraniKV 维持了 **$1.95\times$** 的性能，而批处理全局级联则退化至与基线持平 —— 仅存储层就在激发本文的场景中独揽大局。

> At $L_p=16\text{K}$ shared tokens GraniKV reaches **$2.16\times$**, **$1.98\times$**, and **$1.57\times$** output-token throughput over the production baseline on Llama-3.1-8B/TP=1, Qwen-2.5-14B/TP=2, and Qwen-2.5-32B/TP=4. The gain decomposes: cascade attention integration contributes the majority at saturation; the asymmetric storage layer adds $1.05\text{--}1.15\times$ end-to-end while being what makes the batched-GEMM prefix backend possible at all. Under heterogeneous multi-agent serving with *distinct* prompts of different lengths, the attribution inverts: GraniKV sustains **$1.95\times$** while batch-global cascade collapses to parity --- the storage layer alone carries the win in the regime that motivates the paper.

---

## Navigation & Full Text Links

* **查看 PDF：** [arXiv:2608.15584 PDF](https://arxiv.org/pdf/2608.15584)
* **实验性 HTML：** [arXiv HTML Viewer](https://arxiv.org/html/2608.15584v1)
* **TeX 源码：** [arXiv Source Archive](https://arxiv.org/src/2608.15584)
* **引用与参考：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.15584) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.15584) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.15584)

> * **View PDF:** [arXiv:2608.15584 PDF](https://arxiv.org/pdf/2608.15584)
> * **Experimental HTML:** [arXiv HTML Viewer](https://arxiv.org/html/2608.15584v1)
> * **TeX Source:** [arXiv Source Archive](https://arxiv.org/src/2608.15584)
> * **Citations & References:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.15584) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.15584) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.15584)