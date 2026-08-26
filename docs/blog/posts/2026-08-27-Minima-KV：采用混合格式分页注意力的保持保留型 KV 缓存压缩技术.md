---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- KV Cache
- 大语言模型
- 模型压缩
- Paged Attention
- 量化
title: Minima-KV：采用混合格式分页注意力的保持保留型 KV 缓存压缩技术
---
### 文章背景与核心概要

随着大语言模型（LLM）上下文长度的不断扩展，KV 缓存（Key-Value Cache）已成为长文本服务中的主要容量和带宽瓶颈。现有的压缩方法往往在长文本检索任务中面临精度损失，或者需要复杂的密集型影子缓存（dense shadow），从而增加了系统开销。

Minima-KV 提出了一种保持保留型（retention-preserving）的 KV 缓存层级结构，通过混合格式分页注意力机制（mixed-format paged attention），根据缓存页面的生命周期和相关性进行动态路由：最近的及受保护的锚定页面保持在高精度的 `FP8` 格式，而较旧的非锚定页面则被压缩为打包的 `TQ3` 格式。系统利用格式特定的内核计算局部注意力状态，并通过全局归一化的在线 Softmax 合并将其综合，在实现高达 3.50 倍压缩率的同时，完美保持了长文本检索和复杂基准测试的性能。

---

**Minima-KV：采用混合格式分页注意力的保持保留型 KV 缓存压缩技术**

**作者：** Sergii Kozyrev, Davyd Maiboroda (Minima AI, Inc.)  
**发布时间：** 2026年8月24日  
**主要学科：** 人工智能 (`cs.AI`)  
**arXiv ID：** [2608.23834](https://arxiv.org/abs/2608.23834) | **DOI：** [10.48550/arXiv.2608.23834](https://doi.org/10.48550/arXiv.2608.23834)

---

## 执行摘要

> **Minima-KV** introduces a retention-preserving KV cache hierarchy designed to mitigate capacity and bandwidth bottlenecks in long-context Large Language Model (LLM) serving. By leveraging mixed-format paged attention, the system dynamically routes cache pages based on their age and relevance:
> * **Recent & Protected Anchor Pages:** Maintained in high-precision `FP8`.
> * **Older Non-Anchor Pages:** Compressed into packed `TQ3`.
> * **Addressability:** Every live-request page remains fully addressable without requiring a cache-sized dense shadow.
> 
> Using format-specific kernels, Minima-KV computes partial attention states and synthesizes them via a globally normalized online-softmax merge, enabling efficient heterogeneous decoding.

**Minima-KV** 引入了一种保持保留型（retention-preserving）的 KV 缓存层级结构，旨在缓解长上下文大语言模型（LLM）服务中的容量和带宽瓶颈。通过利用混合格式分页注意力机制，该系统根据缓存页面的年龄和相关性动态路由缓存页面：
* **近期及受保护的锚定页面：** 保持在高精度 `FP8` 格式。
* **较旧的非锚定页面：** 压缩为打包的 `TQ3` 格式。
* **可寻址性：** 每个活跃请求的页面都保持完全可寻址，无需缓存大小的密集型影子缓存（dense shadow）。

通过使用格式特定的内核，Minima-KV 计算局部注意力状态，并通过全局归一化的在线 Softmax（online-softmax）合并将其综合，从而实现高效的异构解码。

---

## 关键性能与基准测试结果

> Evaluated using Qwen3.6-27B configurations on a single 96-GB NVIDIA RTX PRO 6000 Blackwell GPU:
> * **Storage Efficiency:** Achieves **18.3 KiB** of attention KV per live token, yielding a **3.50× compression rate** relative to BF16 (and **1.75×** relative to FP8).
> * **Needle-in-a-Haystack Tasks:** Matches dense baseline control performance perfectly on 16K RULER tasks.
> * **LongBench v2 Set (503 questions):** Minimal performance deltas of **-0.80, -0.60, and -0.40 percentage points** at 16K, 32K, and 64K contexts, respectively.
> * **Direct-Decode Canary (Two 59,008-token requests):** Demonstrates **3.625× active-KV compression**, **0.9821× throughput** relative to control, successfully routes all 16 full-attention layers without fallbacks, and operates without a dense shadow.

在单张 96-GB NVIDIA RTX PRO 6000 Blackwell GPU 上使用 Qwen3.6-27B 配置进行评估：
* **存储效率：** 每个活跃 Token 实现 **18.3 KiB** 的注意力 KV 缓存，相对于 BF16 实现了 **3.50 倍的压缩率**（相对于 FP8 为 **1.75 倍**）。
* **大海捞针（Needle-in-a-Haystack）任务：** 在 16K RULER 任务上完美匹配稠密基线控制性能。
* **LongBench v2 数据集（503 个问题）：** 在 16K、32K 和 64K 上下文下，性能差异极小，分别仅为 **-0.80、-0.60 和 -0.40 个百分点**。
* **Direct-Decode Canary（两个 59,008 Token 的请求）：** 展示了 **3.625 倍活跃 KV 压缩**、相对于控制组 **0.9821 倍的吞吐量**，成功路由所有 16 个全注意力层且无回退，并且在没有密集影子缓存的情况下运行。

---

## 导航与资源

> * **Full-Text Links:** [View PDF](https://arxiv.org/pdf/2608.23834) | [HTML (Experimental)](https://arxiv.org/html/2608.23834v1) | [TeX Source](https://arxiv.org/src/2608.23834)
> * **Academic Databases:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23834) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23834) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23834)

* **全文链接：** [查看 PDF](https://arxiv.org/pdf/2608.23834) | [HTML（实验性）](https://arxiv.org/html/2608.23834v1) | [TeX 源码](https://arxiv.org/src/2608.23834)
* **学术数据库：** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23834) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23834) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23834)