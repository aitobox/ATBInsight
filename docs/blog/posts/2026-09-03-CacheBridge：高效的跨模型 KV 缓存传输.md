---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- 大语言模型
- KV缓存
- 模型互操作性
- 架构映射
- 性能优化
title: CacheBridge：高效的跨模型 KV 缓存传输
---
### 文章背景与核心概要
在多模型大语言模型（LLM）系统中，由于键值（KV）缓存（KV Cache）具有模型特异性，不同模型之间共享上下文传统上需要接收模型重新预填充（re-prefill）共享的前缀。虽然近期的“全头映射”（Full-Head Mapping）方法通过使用免训练的仿射映射器将源缓存转换到目标缓存来避免这种重复计算，但它们容易受架构差异的影响，且面临映射器存储成本高、计算开销大的问题。

为了解决这些局限性，本文提出了 **CacheBridge** 框架。该框架具有三大核心技术：架构索引的映射器支持、注意力对齐的校准，以及有界的映射器构建（同时在在线部署中保留了闭式仿射接口）。实验表明，CacheBridge 在 Ministral 3 的跨模型传输中完全恢复了传统全-头映射丢失的大量精度，在 Qwen3 上保留了 99.83% 的平均目标保留率，将 Qwen3 $14\mathrm{B}\to32\mathrm{B}$ 的映射器存储减少了 $8\times$，应用加速高达 $3.0\times$，并且仅需十分之一的校准数据即可达到全头映射的精度水平，构建时间大幅缩短 $10.7\times$。

---

## CacheBridge: Efficient Cross-Model KV Cache Transfer

**Authors:** Xingyu Qu, Siyuan Lu, Zhiyu Chen, Sheng Wang, Tao Lin  
**Submitted:** 1 September 2026  
**Primary Subject:** Artificial Intelligence (`cs.AI`)  
**arXiv ID:** [arXiv:2609.00891](https://arxiv.org/abs/2609.00891) | **DOI:** [10.48550/arXiv.2609.00891](https://doi.org/10.48550/arXiv.2609.00891)

---

## Summary

> Sharing context between Large Language Models (LLMs) in multi-model systems traditionally requires the receiving model to re-prefill shared prefixes because Key-Value (KV) caches are model-specific. Recent "Full-Head Mapping" approaches avoid this replay by using training-free affine mappers from source to target caches, but they suffer from sensitivity to architectural differences, high mapper storage costs, and expensive computational overheads.
> 
> To address these limitations, the paper introduces **CacheBridge**, a framework featuring:
> 1. Architecture-indexed mapper support
> 2. Attention-aligned calibration
> 3. Bounded mapper construction (retaining a closed-form affine interface for online deployment)
> 
> ### Key Performance Highlights:
> * **Accuracy Recovery:** Completely recovers the two Ministral 3 transfer directions where traditional Full-Head Mapping loses substantial accuracy, while preserving 99.83% mean target retention on Qwen3.
> * **Storage Reduction:** Reduces mapper storage by **$8\times$** on Qwen3 $14\mathrm{B}\to32\mathrm{B}$.
> * **Speedup:** Accelerates application by up to **$3.0\times$**.
> * **Data Efficiency:** Matches Full-Head Mapping accuracy using only **one-tenth** of the calibration data.
> * **Construction Efficiency:** Reduces 500-sequence construction time from 92.63 to 8.63 seconds (**$10.7\times$ speedup**).

---

## 摘要

> Sharing context between LLMs in a multi-model system requires the receiving model to prefill the shared prefix because KV caches are model-specific. Recent closed-form cross-model KV transfer, hereafter Full-Head Mapping, avoids this replay by fitting a training-free affine mapper from source to target caches. However, its full-head design maps each target KV head from every source KV head in the selected layers, making transfer quality sensitive to architectural differences and causing mapper storage and application cost to grow with layer support. To this end, we introduce CacheBridge, which co-designs architecture-indexed mapper support, attention-aligned calibration, and bounded mapper construction while retaining a closed-form affine interface for online deployment. CacheBridge restricts each target head to a matched source head, weights reconstruction errors by causal attention sensitivity, and uses a fused GPU kernel to construct weighted sufficient statistics without materializing full observation tensors. Across three transfer directions, CacheBridge recovers the two Ministral 3 transfer directions where Full-Head Mapping loses substantial accuracy while preserving 99.83% mean target retention on Qwen3. On Qwen3 $14\mathrm{B}\to32\mathrm{B}$, it reduces mapper storage by $8\times$, accelerates application by up to $3.0\times$, matches \fullhead with one tenth of the calibration data, and reduces 500-sequence construction from 92.63 to 8.63 seconds ($10.7\times$).

> 在多模型系统中，在 LLM 之间共享上下文需要接收模型重新预填充共享的前缀，因为 KV 缓存具有模型特异性。近期的闭式跨模型 KV 传输（以下称为全头映射，Full-Head Mapping）通过从源缓存到目标缓存拟合一个免训练的仿射映射器，避免了这种重复计算。然而，其全头设计将所选层中的每个目标 KV 头映射自所有源 KV 头，这使得传输质量对架构差异高度敏感，并导致映射器存储和应用成本随层支持的增加而增长。为此，我们引入了 CacheBridge，它协同设计了架构索引的映射器支持、注意力对齐的校准以及有界的映射器构建，同时为在线部署保留了闭式仿射接口。CacheBridge 将每个目标头限制为一个匹配的源头，通过因果注意力灵敏度对重建误差进行加权，并使用融合 GPU 内核构建加权充分统计量，而无需实例化完整的观测张量。在三个传输方向上，CacheBridge 完全恢复了全头映射丢失大量精度的两个 Ministral 3 传输方向，同时在 Qwen3 上保留了 99.83% 的平均目标保留率。在 Qwen3 $14\mathrm{B}\to32\mathrm{B}$ 上，它将映射器存储减少了 $8\times$，应用加速高达 $3.0\times$，仅用十分之一的校准数据即可达到 \fullhead 的精度，并将 500 个序列的构建时间从 92.63 秒缩短至 8.63 秒（$10.7\times$）。

---

## 全文与资源 (Full-Text & Resources)

> * **PDF:** [View PDF](https://arxiv.org/pdf/2609.00891)
> * **HTML (Experimental):** [arXiv HTML View](https://arxiv.org/html/2609.00891v1)
> * **TeX Source:** [Download Source](https://arxiv.org/src/2609.00891)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">