---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-27
hide:
  - navigation
tags:
  - 推测解码
  - TreeWY
  - Gated DeltaNet
  - 线性注意力
  - 显存优化
title: "TreeWY：门控 DeltaNet 混合架构的免快照推测验证机制"
---

# TreeWY：门控 DeltaNet 混合架构的免快照推测验证机制

> # TreeWY: Speculative Verification for Gated DeltaNet Hybrids

> **arXiv ID:** [arXiv:2608.20961 [cs.AI]](https://arxiv.org/abs/2608.20961) *(v2 submitted on 22 Oct 2026)*  
> **Authors:** Sneha Murthy Ghantasala  
> **Primary Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`); Distributed, Parallel, and Cluster Computing (`cs.DC`); Machine Learning (`cs.LG`); Performance (`cs.PF`)  
> **DOI:** [10.48550/arXiv.2608.20961](https://doi.org/10.48550/arXiv.2608.20961)

### 文章背景与核心概要

随着线性注意力架构的快速演进，以门控 DeltaNet (Gated DeltaNet, GDN) 为代表的混合架构正在成为现代大语言模型 (Large Language Model, LLM) 兼顾长文本生成效率与显存占用的热门方向。然而，在利用推测解码 (Speculative Decoding) 加速模型推理时，传统系统为了支持草稿树多分支的验证与回滚，不得不为每个候选节点在 GDN 层完整保存循环状态快照，造成了极为严峻的显存爆炸，严重阻碍了高接受率宽草稿树的应用。针对这一核心系统瓶颈，本文创新性地提出了 TreeWY 算法，巧妙地将经典的 WY 矩阵变换拓展至树状结构并与门控 Delta 规则深度结合，仅需单次三角求解即可并行完成全部节点的验证，彻底摒弃了循环状态快照。在工业级混合模型 Qwen3.5 (35B 与 397B) 上的真实评测表明，TreeWY 极大幅度减轻了高带宽内存 (High Bandwidth Memory, HBM) 压力，显著降低了首字生成延迟 (Time-to-First-Token, TTFT) 并拉高了系统吞吐量，为未来新一代混合架构大模型的高性能推测推理扫清了显存障碍。

---

## 📋 论文摘要

> ## Abstract Summary

当前开源大语言模型越来越多地采用混合架构，其中绝大多数网络层都由线性注意力组件构成，尤其是**门控 DeltaNet (Gated DeltaNet, GDN)** 层。与传统模型不同，GDN 在推理时无需维护随序列长度线性膨胀的键值缓存 (KV cache)，而是仅需保持一个固定大小的紧凑循环状态。尽管这种设计在常规逐 Token 解码中显著提升了显存利用效率，但在推测解码与验证过程中，却演变成了一个严重的性能瓶颈。

> Modern open-source language models increasingly rely on hybrid architectures where the majority of layers are linear-attention components, specifically **Gated DeltaNet (GDN)** layers. Unlike traditional models, GDNs maintain a small, fixed-size recurrent state instead of a growing Key-Value (KV) cache. While this design significantly improves memory efficiency during ordinary decoding, it creates a major bottleneck for speculative decoding and verification.

### 核心困境：状态快照引发的显存爆炸

> ### The Problem

当推理系统需要并行验证一批候选草稿 Token 并回滚被拒绝的分支时，传统系统必须为 GDN 层在*每一个*草稿位置都完整快照一份循环状态。由于草稿树的不同分支之间无法跨分支共享这些状态快照，导致显存消耗呈指数级剧增，使得拥有更宽分支、更高接受率的高性能草稿树在工程实践中几乎不可行。

> When verifying a batch of draft tokens and rolling back rejected branches, conventional systems must snapshot the full recurrent state at *every* draft position for GDN layers. Because these snapshots cannot be shared across different branches of a draft tree, memory consumption explodes, making wide and high-acceptance draft trees practically infeasible.

### 创新破局：TreeWY 免快照验证机制

> ### The Solution: TreeWY

针对该难题，本文提出了 **TreeWY** 机制，彻底消除了推测验证对循环状态快照的依赖：

> The paper introduces **TreeWY**, a method that completely removes the need for recurrent-state snapshots. 

* **树状 WY 变换**：利用直接由门控 Delta 规则严格推导出的树状结构 **WY 变换 (WY transform)**，完全独立于模型的其他具体架构细节；
* **单次三角求解**：仅需执行单次三角方程求解即可同时并行计算出整棵草稿树中每个候选节点的输出；
* **提交时轻量重构**：仅用极其轻量级的伪值矩阵替代逐节点保存的状态副本，在最终确认接受分支并提交时才重构单个目标状态。

> * Utilizes a tree-structured **WY transform** derived strictly from the gated delta rule (independent of other architectural details).
> * Computes every draft node's output using a single triangular solve.
> * Reconstructs only the single accepted state upon commit, storing a lightweight pseudo-value matrix in place of per-node states.

### 评测结果与性能飞跃

> ### Results

* **真实服务基准测试 (Serving Benchmarks)**：在两种规模的混合模型族 (**Qwen3.5 35B 与 397B**) 上进行实测验证，TreeWY 在保持与传统方法几乎完全一致的推测接受长度的同时，大幅降低了推测循环状态占用的显存以及 KV cache 压力；
* **显著性能收益 (Performance Gains)**：释放出来的大量高带宽内存 (High Bandwidth Memory, HBM) 转化为推理系统吞吐量的显著提升，并在显存受限场景下大幅降低了首字生成延迟 (Time-to-First-Token, TTFT) (而在非显存受限场景中仅产生微乎其微的计算开销)；
* **支持更大规模草稿扩展 (Draft Scaling)**：通过大幅削减显存开销，TreeWY 使得过去因显存受限而无法运行的宽分支、高接受率草稿树变得经济实用且计算可行。

> * **Serving Benchmarks:** Tested on two scales of a hybrid model family (**Qwen3.5 35B and 397B**), TreeWY drastically reduces speculative recurrent-state memory and KV-cache pressure while maintaining virtually identical acceptance lengths.
> * **Performance Gains:** The freed High Bandwidth Memory (HBM) translates into higher overall throughput and substantially lower Time-to-First-Token (TTFT) in memory-bound scenarios (with only a nominal cost in non-memory-bound cases).
> * **Draft Scaling:** By dramatically lowering memory overhead, TreeWY makes wider, high-acceptance draft trees computationally affordable.

---

## 🔗 论文资源与导航

> ## Navigation & Resources

* **全文阅读 (Full-Text Links)**：[查看 PDF](https://arxiv.org/pdf/2608.20961) | [HTML 网页版](https://arxiv.org/html/2608.20961v2) | [TeX 源码](https://arxiv.org/src/2608.20961)
* **引用与检索工具 (Citation Tools)**：[Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.20961) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.20961) | [SciX](https://scixplorer.org/abs/arXiv:2608.20961)
* **关联数据 / 代码 / 演示 (Associated Data / Code / Demos)**：[Hugging Face](https://huggingface.co/huggingface) | [CatalyzeX 代码检索](https://www.catalyzex.com) | [alphaXiv 论文讨论](https://alphaxiv.org/)

> * **Full-Text Links:** [View PDF](https://arxiv.org/pdf/2608.20961) | [HTML Version](https://arxiv.org/html/2608.20961v2) | [TeX Source](https://arxiv.org/src/2608.20961)
> * **Citation Tools:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.20961) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.20961) | [SciX](https://scixplorer.org/abs/arXiv:2608.20961)
> * **Associated Data / Code / Demos:** [Hugging Face](https://huggingface.co/huggingface) | [CatalyzeX Code Finder](https://www.catalyzex.com) | [alphaXiv](https://alphaxiv.org/)
