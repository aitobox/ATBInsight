---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-27
hide:
  - navigation
tags:
  - 稀疏注意力
  - OpenAttention
  - KV Cache
  - 大语言模型
  - 尾部代理
title: "OpenAttention：仅需 1% 尾部代理以超低读取率保留全注意力精度"
---

# OpenAttention：仅需 1% 尾部代理以超低读取率保留全注意力精度

> # OpenAttention: One Percent Is Enough with Tail Proxies

> **arXiv ID:** [arXiv:2610.30951](https://arxiv.org/abs/2610.30951) [cs.LG]  
> **Authors:** Hyunwoo Yu, Jongbeom Lee, Hyunbin Kim, Sungjun Park, Jaemin Choi, Jincheol Yang, Seunghun Moon, Bongjoon Hyun, Kyomin Sohn, Kyeongbo Kong, Suk-Ju Kang  
> **Submitted:** 22 October 2026 (v1); Last revised: 23 October 2026 (v2)  
> **DOI / Paper:** [10.48550/arXiv.2610.30951](https://doi.org/10.48550/arXiv.2610.30951)  
> **Project / Code:** [GitHub - hyunwoo137/OpenAttention](https://github.com/hyunwoo137/OpenAttention)

### 文章背景与核心概要

随着大语言模型 (Large Language Model, LLM) 上下文窗口的不断扩展，自回归解码阶段庞大的键值缓存 (KV Cache) 导致显存占用急剧膨胀、内存带宽不堪重负，稀疏注意力技术因此成为加速推理的核心方向。然而，现有的稀疏注意力机制在大幅降低 KV Cache 读取率时面临致命困境：若直接丢弃未读取的“长尾”信息会导致输出严重偏倚，而基于采样的折中方案在极低读取率 ($\le 5\%$) 下又极易错失被选择器遗漏的关键高权重 Token (Heavy-Hitters)。

针对这一瓶颈，研究人员推出了革新性的 **OpenAttention** 架构。该研究突破性地发现，与其进行复杂的随机采样，不如将整个未被读取的尾部折叠为一个“感知数量的均值代理 Token” (Count-Aware Mean Proxy Token)，在极低读取率下能大幅降低注意力权重误差。结合无需训练的查询几何聚类 (Query-Geometry Clustering, QGC)、查询几何选择器 (Query-Geometry Selector, QGS) 以及基于误差估计的 ErrorGate 动态分配策略，OpenAttention 在 Llama-3.1-8B 模型的 RULER-32K HARD 基准测试中，**仅需读取 1% 的 KV Cache 即可保留 99% 的全量稠密注意力精度**，同时将解码注意力阶段的执行速度提升了整整 **10 倍 ($10\times$)**，为超长上下文大模型的高效部署开辟了极具实用价值的全新路径。

---

## 📋 内容总结

> ## 📋 Summary

在处理长上下文时，稀疏注意力机制通常仅读取一小部分键值缓存 (KV Cache)，这使得如何妥善处理那些未被读取的“尾部 Token”成了一大核心难题。如果直接丢弃这些尾部数据，会给模型的最终输出带来显著偏差；而以往采用的随机采样策略，在极低读取率 ($\le 5\%$) 下表现极差，因为未读取的长尾区域中往往隐藏着被稀疏选择器遗漏的关键高权重 Token (Heavy-Hitters)。

> Sparse attention mechanisms typically read only a small subset of the key-value (KV) cache, leaving the unread "tail" as a significant challenge. Discarding the tail introduces output bias, while previous sampling approaches fail at low read rates ($\le 5\%$) where the tail frequently contains crucial heavy-hitters missed by the selector.

为此，本文提出了 **OpenAttention**——一种使用简易尾部代理 (Tail Proxies) 的创新方法，它将未读取的整个尾部区域折叠压缩为一个具有数量感知能力的均值 Token (Count-Aware Mean Token)，从而实现了远低于传统采样方案的输出误差。结合无需训练的**查询几何聚类 (Query-Geometry Clustering, QGC)**、**查询几何选择器 (Query-Geometry Selector, QGS)** 以及按误差估计进行配额分配的 **ErrorGate** 机制，OpenAttention 在运行 Llama-3.1-8B 模型的 RULER-32K HARD 基准测试中，**仅凭 1% 的读取率便保留了稠密全注意力 99% 的精度**，同时使解码注意力阶段的运行速度比稠密全注意力**提升了 10 倍 ($10\times$)**。

> This paper introduces **OpenAttention**, a novel approach that uses simple tail proxies—folding the entire tail into a count-aware mean token—to achieve lower output error than conventional sampling. Combined with training-free **Query-Geometry Clustering (QGC)**, **Query-Geometry Selector (QGS)**, and **ErrorGate** allocation, OpenAttention retains **99% of dense accuracy at a 1% read rate** on RULER-32K HARD with Llama-3.1-8B, while running the decode attention stage **$10\times$ faster** than dense attention.

---

## 📑 论文摘要

> ## 📑 Abstract

稀疏注意力机制往往仅读取键值缓存中极小的一部分数据，如何有效处理未被读取的“长尾”部分始终是该领域的一大核心瓶颈。若直接丢弃未读取的长尾，将导致模型输出产生系统性偏倚；而如果效仿先前的方法对其进行稀疏采样，在读取率降至 5% 及以下时便会彻底失效，因为此时尾部区域极有可能包含被稀疏选择器遗漏的关键高权重 Token。

> Sparse attention reads only a small subset of the key-value cache, and how to treat the unread tail remains a key challenge. Discarding the tail biases the output, and sampling it as previous approaches do fails at reads of 5% and below, where the tail likely holds heavy hitters the selector missed.

我们的核心观察在于：即便是构建一个最为简化的代理——仅用单个 Token 将全部尾部折叠为其感知元素数量的均值表示——在搭配实际选择器时，其输出误差在各个读取率下就已经低于传统采样方法。我们进一步通过解析闭式解证明：在极低读取率下，随机采样的注意力权重误差几乎是直接丢弃策略的两倍，而单个均值代理所产生的误差则始终低于直接丢弃。

> Our key observation is that the simplest possible proxy, one token that folds the entire tail into its count-aware mean, already yields lower output error than a sample at every read behind a practical selector. We further show in closed form that at low reads sampling nearly doubles the weight error of discarding while a single proxy stays below it.

基于这些新发现，我们探索了利用少量针对长尾的代理 Token 来逼近完整稠密注意力分布的可行性。我们提出了 OpenAttention 架构，该架构构建了一条由聚类、ErrorGate 动态配额与 Top-k 筛选组成的高效流水线，随后引入感知数量的均值代理进行精准补齐。为了兼顾聚类与选择过程的高效性与准确性，我们设计了无需任何微调或训练的查询几何聚类 (QGC) 与查询几何选择器 (QGS)，它们能够在充分尊重查询向量几何方向的同时对键 (Key) 进行高度压缩。此外，不同于以往仅依靠聚类质心排名的做法，ErrorGate 能够根据每个聚簇所估算的权重误差动态分配精确的读取配额。

> Building on these findings, we explore approximating the dense attention distribution with a few proxies that target the tail. We propose OpenAttention, a pipeline of clustering, ErrorGate and top-k selection followed by a count-aware mean proxy. To implement clustering and selection both efficiently and effectively, we design training-free Query-Geometry Clustering (QGC) and a Query-Geometry Selector (QGS), which compress the keys while respecting the query directions. Additionally, unlike prior methods that rank clusters by centroid alone, ErrorGate allocates the exact read by the estimated weight error of each cluster.

在搭载 Llama-3.1-8B 模型的 RULER-32K HARD 基准测试中，OpenAttention 仅需 1% 的读取率即可保留全量稠密注意力 99% 的精度。不仅如此，它在各类基准模型、多种上下文长度以及不同测试数据集上均取得了业内最优 (SOTA) 的精度表现。我们为 OpenAttention 专门定制的高性能注意力算子内核，更是在 1% 读取率下将自回归解码注意力阶段的执行速度提升至稠密全注意力的 10 倍 ($10\times$)。

> On RULER-32K HARD with Llama-3.1-8B, OpenAttention retains 99% of dense accuracy at a 1% read. It also achieves state-of-the-art accuracy across models, context lengths and datasets. Our customized attention kernel for OpenAttention runs the decode attention stage $10\times$ faster than dense attention at a 1% read.

---

## 🛠️ OpenAttention 的核心技术组件

> ## 🛠️ Key Components of OpenAttention

1. **尾部代理与感知数量的均值 (Tail Proxies & Count-Aware Mean)**：彻底告别对未读取尾部的粗暴丢弃或低效采样，采用单个超高效代理 Token 捕捉未读取元素的数量感知均值，以极小代价大幅拉平长尾误差；
2. **查询几何聚类 (QGC) 与查询几何选择器 (QGS)**：采用免训练 (Training-free) 机制，在严格对齐并保持查询向量空间几何方向的前提下，对大量键 (Key) 进行高效无损压缩与快速候选筛选；
3. **ErrorGate 误差门控分配机制**：突破以往单纯依靠聚类质心距离排序的局限，根据每个聚簇预估的注意力权重误差动态分配精准的读取配额，让算力与带宽集中在误差最高的关键聚类上；
4. **定制化高性能注意力算子内核 (Custom Attention Kernel)**：针对 OpenAttention 流水线在 GPU 底层深度调优打造的高效算子，在 1% 超低读取率下使自回归解码阶段的注意力计算速度狂飙 10 倍 ($10\times$)。

> 1. **Tail Proxies & Count-Aware Mean:** Replaces discarded or sampled tails with a single, highly efficient proxy token capturing the count-aware mean of the unread elements.
> 2. **Query-Geometry Clustering (QGC) & Query-Geometry Selector (QGS):** Training-free mechanisms that efficiently compress keys while precisely aligning with query directions.
> 3. **ErrorGate:** Dynamically allocates exact reads based on the estimated weight error of each cluster, moving beyond traditional centroid-only ranking methods.
> 4. **Custom Attention Kernel:** Optimized specifically for the OpenAttention pipeline, delivering a $10\times$ speedup during the decode attention stage at a 1% read rate.

---

## 🔗 相关链接与资源

> ## 🔗 Links & Resources

* **项目主页**：[hyunwoo137.github.io/OpenAttention](https://hyunwoo137.github.io/OpenAttention/)
* **代码开源仓库**：[github.com/hyunwoo137/OpenAttention](https://github.com/hyunwoo137/OpenAttention)
* **arXiv 全文检索**：[HTML 在线版本](https://arxiv.org/html/2610.30951v2) | [PDF 下载版本](https://arxiv.org/pdf/2610.30951)
* **论文 DOI**：[10.48550/arXiv.2610.30951](https://doi.org/10.48550/arXiv.2610.30951)

> * **Project Page:** [hyunwoo137.github.io/OpenAttention](https://hyunwoo137.github.io/OpenAttention/)
> * **Code Repository:** [github.com/hyunwoo137/OpenAttention](https://github.com/hyunwoo137/OpenAttention)
> * **arXiv Full-Text:** [HTML Version](https://arxiv.org/html/2610.30951v2) | [PDF Version](https://arxiv.org/pdf/2610.30951)
> * **DOI:** [10.48550/arXiv.2610.30951](https://doi.org/10.48550/arXiv.2610.30951)
