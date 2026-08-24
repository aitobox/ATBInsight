---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- 投机解码
- 门控DeltaNet
- 线性注意力
- 大语言模型
- 内存优化
title: TreeWY：门控DeltaNet混合模型的投机验证
---
### 文章背景与核心概要
现代开源语言模型越来越倾向于采用包含线性注意力层（如**门控 DeltaNet，即 GDN**）的混合架构，以此替代传统的不断增长的键值（KV）缓存。尽管这种设计在标准解码过程中提升了内存效率，但它却为**投机解码（Speculative Decoding）**造成了巨大的性能瓶颈。

传统上，验证一批草稿令牌（draft tokens）需要在 GDN 层的每个草稿位置对完整的循环状态进行快照。由于这些快照无法在草稿树的分支之间共享，因此利用宽幅、高接受率的草稿树在内存上变得不可行。

**TreeWY** 通过完全消除快照来解决这一局限性。通过利用门控 delta 规则的树状结构 WY 变换，它使用单次三角求解来计算每个草稿节点的输出，并在提交（commit）时仅重建被接受的状态。该方法存储的是轻量级的伪值矩阵，而不是每个节点的状态。在 Qwen3.5（35B 和 397B）混合模型家族上的基准测试表明，TreeWY 成功降低了投机循环状态的内存压力，释放了高带宽内存（HBM），从而在内存受限的情况下实现了更高的吞吐量并显著降低了首字延迟（TTFT）。

---

## 📌 Summary

> Modern open-source language models increasingly rely on hybrid architectures featuring linear-attention layers (such as **Gated DeltaNet, or GDN**) instead of a traditional growing key-value (KV) cache. While this design improves memory efficiency during standard decoding, it creates a major bottleneck for **speculative decoding**. 
> 
> Traditionally, verifying a batch of draft tokens requires snapshotting the full recurrent state at every draft position for GDN layers. Because these snapshots cannot be shared across branches in a draft tree, utilizing wide, high-acceptance draft trees becomes memory-infeasible. 
> 
> **TreeWY** solves this limitation by eliminating snapshots entirely. By leveraging a tree-structured WY transform of the gated delta rule, it computes the output of every draft node using a single triangular solve and reconstructs only the accepted state upon commit. This approach stores a lightweight pseudo-value matrix instead of per-node states. Benchmarking on the Qwen3.5 (35B and 397B) hybrid model family demonstrates that TreeWY successfully reduces speculative recurrent-state memory pressure, freeing up High Bandwidth Memory (HBM) to deliver higher throughput and significantly lower Time-to-First-Token (TTFT) when memory-bound.

---

## 📋 Metadata & Links

> * **Full-Text Access:** 
>   * [View PDF](https://arxiv.org/pdf/2608.20961)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.20961v1)
>   * [TeX Source](https://arxiv.org/src/2608.20961)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
> * **Additional Subjects:** 
>   * Computation and Language (`cs.CL`)
>   * Distributed, Parallel, and Cluster Computing (`cs.DC`)
>   * Machine Learning (`cs.LG`)
>   * Performance (`cs.PF`)

---

## 🔗 References & External Tools

> * **Bibliographic Databases:** 
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.20961)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.20961)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.20961)
> * **Interactive & Community Platforms:** 
>   * [alphaXiv Discussion](https://alphaxiv.org/)
>   * [Hugging Face Integration](https://huggingface.co/huggingface)