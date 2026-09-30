---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-01
hide:
  - navigation
tags:
  - ARC-KV
  - KV Cache 压缩
  - 大语言模型
  - 长上下文推理
  - Attention Matching
  - arXiv论文
title: "ARC-KV：摊薄锚点搜索开销的重构式 KV Cache 极致压缩技术"
---

### 文章背景与核心概要

在长上下文大语言模型 (LLM) 推理场景中，键值缓存 (KV Cache) 的显存占用随输入长度线性暴涨，在长系统提示词或长文档频繁复用的任务中构成了严峻的内存瓶颈。现有的重构式压缩方案 (如基于正交匹配追踪 OMP 的 Attention Matching) 虽然压缩性能出众，但依赖耗时的逐次迭代搜索锚点，导致前期压缩计算开销极其沉重。为此，研究团队提出了基于“选择性摊薄 (Selective Amortization) ”理念的 **ARC-KV** 技术：通过训练轻量级的价值感知索引器单次打分筛选真实 Key 锚点，将昂贵的搜索成本跨查询彻底均摊。实验表明，在 Llama-3.1-8B-Instruct 模型及 QuALITY、RULER 和 LongBench 等权威长文本基准上，ARC-KV 即使仅保留 10% 的 KV Cache 也能超越基线精度，同时将压缩耗时从 959.8 秒大幅缩减至 37.3 秒 (加速达 25.73 倍) ，实现了速度与精度的双重突破。

---

# ARC-KV：摊薄锚点搜索开销的重构式 KV Cache 极致压缩技术

> # ARC-KV: Amortizing Anchor Search for Reconstruction-Based KV Cache Compaction

## 核心内容综述

> ## Summary

在长上下文大语言模型 (Large Language Model, LLM) 的推理过程中，显存开销居高不下一直是业界痛点。这主要是因为键-值缓存 (Key-Value Cache, KV Cache) 的体积会随着序列长度呈线性暴涨——尤其在面对需要多次响应不同查询的超长可复用前缀 (Context Prefixes) 时，这一负担更显沉重。虽然像 Attention Matching 这样基于数学重构的压缩方法能够凭借紧凑精炼的 KV Cache 取得优异的任务性能，但它们严重依赖通过正交匹配追踪 (Orthogonal Matching Pursuit, OMP) 进行反复迭代的锚点搜索，这直接造成了巨大的计算性能瓶颈。

> Long-context large language model (LLM) inference often struggles with high memory overhead because Key-Value (KV) caches grow linearly with sequence length—a problem that is especially burdensome for long, reusable context prefixes. While reconstruction-based methods like Attention Matching offer strong performance using compact KV caches, their reliance on iterative anchor search via OMP (Orthogonal Matching Pursuit) creates a massive computational bottleneck.

为了解决这一难题，作者团队推出了 **ARC-KV**——一种基于“选择性摊薄 (Selective Amortization) ”理念的全新 KV Cache 压缩方法。ARC-KV 能够在不同上下文之间学习一套通用的可复用锚点选择策略，同时保留针对各个具体上下文的专属重构，从而彻底摆脱了反复繁琐搜索的算力泥潭。

> To solve this, the authors introduce **ARC-KV**, a novel KV cache compaction method based on the principle of *selective amortization*. ARC-KV learns a reusable anchor-selection policy across contexts while retaining context-specific reconstruction.

### 核心亮点

> ### Key Highlights:

- **价值感知索引器 (Value-Aware Indexer) ：** 训练专用索引器，仅凭单次打分前向计算即可筛选出真实的 Key 锚点，告别循环迭代。
- **先进的合并与拟合机制 (Advanced Merging & Fitting) ：** 引入受凸包约束的 Key 向量合并技术，并结合注意力质量偏置 (Attention-Mass Bias) 以及针对完整全量缓存精确拟合的紧凑 Value 向量。
- **高效的推理部署 (Efficient Inference) ：** 在推理阶段，利用参数固定的冻结索引器为每个上下文仅构建一次紧凑缓存，即可直接复用于后续的所有查询请求。
- **超越同侪的卓越性能 (Superior Performance) ：** 在基于 Llama-3.1-8B-Instruct 模型的 QuALITY、RULER 和 LongBench 等长文本权威基准测试中全面领跑。例如在 QuALITY 测试中，即便仅保留 10% 的 KV Cache，ARC-KV 相比标准 Attention Matching 仍将准确率从 **0.6409 提升至 0.6474**，同时将压缩耗时断崖式削减了 **25.73 倍** (由 959.8 秒缩减至 37.3 秒) 。

> - **Value-Aware Indexer:** Trains an indexer to select real-key anchors in a single scoring pass.
> - **Advanced Merging & Fitting:** Applies convex-hull-constrained key merging alongside attention-mass bias and compact values fitted against the full cache.
> - **Efficient Inference:** Builds the compact cache once per context using a frozen indexer and reuses it for all subsequent queries.
> - **Superior Performance:** Outperforms existing methods on benchmarks like QuALITY, RULER, and LongBench (using Llama-3.1-8B-Instruct). For example, at 10% KV retention on QuALITY, ARC-KV improves accuracy from **0.6409 to 0.6474** over standard Attention Matching while slashing compaction time by **25.73×** (from 959.8s down to 37.3s).

---

## 论文元数据

> ## Paper Metadata

| 字段 | 详情 |
| :--- | :--- |
| **arXiv ID** | [arXiv:2609.36835](https://arxiv.org/abs/2609.36835) [cs.AI] |
| **研究领域** | 人工智能 (`cs.AI`) |
| **论文作者** | Zheyu Shen, Guanhua Wang, Dezhan Tu, Mengchi Zhang, Yanjia Li, Adnan Aziz, Chunqiang Tang, Ang Li |
| **提交时间** | 2026年9月29日 |
| **DOI** | [10.48550/arXiv.2609.36835](https://doi.org/10.48550/arXiv.2609.36835) |
| **开源协议** | [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> |

> | Field | Details |
> | :--- | :--- |
> | **arXiv ID** | [arXiv:2609.36835](https://arxiv.org/abs/2609.36835) [cs.AI] |
> | **Subjects** | Artificial Intelligence (`cs.AI`) |
> | **Authors** | Zheyu Shen, Guanhua Wang, Dezhan Tu, Mengchi Zhang, Yanjia Li, Adnan Aziz, Chunqiang Tang, Ang Li |
> | **Submitted** | September 29, 2026 |
> | **DOI** | [10.48550/arXiv.2609.36835](https://doi.org/10.48550/arXiv.2609.36835) |
> | **License** | [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> |

---

## 论文摘要

> ## Abstract

长上下文大语言模型 (Large Language Model, LLM) 的推理效率，深受随序列长度线性增长的 KV Cache 显存瓶颈制约。对于需要多次响应下游查询的长文本、高复用前缀而言，这一显存负担尤为突出。以 Attention Matching 为代表的重构式压缩方案，虽然能在保持极低 KV Cache 占用的同时取得优异的任务性能，但其依赖基于 OMP 的迭代式锚点搜索，几乎构成了整个压缩过程的最大算力开销。为此，我们提出了“选择性摊薄 (Selective Amortization) ”原则——跨不同上下文训练一套可复用的锚点挑选策略，同时保留针对各个具体上下文的定制化重构。基于该原则，本文提出了全新的重构式 KV Cache 压缩方法 **ARC-KV**。我们首先训练一个轻量级的价值感知索引器，仅需单次打分前向计算即可筛选出真实的 Key 锚点；随后，ARC-KV 执行受凸包约束的 Key 合并，并结合针对全量缓存精确拟合出的注意力质量偏置与紧凑 Value 向量。在推理阶段，ARC-KV 借助参数冻结的索引器为每个上下文构建一次紧凑缓存，并将其直接复用于后续所有查询。广泛的实验表明，在基于 Llama-3.1-8B-Instruct 模型的 QuALITY、RULER 和 LongBench 等基准测试中，ARC-KV 在绝大多数配置下均显著优于现有压缩方法。特别是在 QuALITY 基准且仅保留 10% KV 缓存的极限设定下，ARC-KV 相比 Attention Matching 将任务准确率从 0.6409 进一步提高到 0.6474，同时将压缩耗时大幅降低了 25.73 倍 (从 959.8 秒直降至 37.3 秒) 。

> Long-context large language model inference is bottlenecked by KV caches that grow linearly with sequence length. This burden is especially severe for long, reusable context prefixes, whose cache must serve many downstream queries. Reconstruction-based methods such as Attention Matching achieve strong downstream task performance with compact KV caches. However, iterative anchor search dominates the compaction cost of OMP-based Attention Matching. This motivates our selective amortization principle of learning a reusable anchor-selection policy across contexts while retaining context-specific reconstruction. In this work, we propose ARC-KV, a novel reconstruction-based KV cache compaction method that follows this principle. To this end, we first train a value-aware indexer to select real-key anchors in a single scoring pass. ARC-KV then applies convex-hull-constrained key merging and fits an attention-mass bias and compact values against the full cache. At inference time, ARC-KV builds the compact cache once per context using the frozen indexer and reuses it for all subsequent queries. Extensive experiments demonstrate that ARC-KV outperforms reported compaction methods in most settings across QuALITY, RULER, and LongBench on Llama-3.1-8B-Instruct. In particular, at 10% KV retention on QuALITY, ARC-KV improves accuracy from 0.6409 to 0.6474 over Attention Matching while reducing compaction time by a factor of 25.73, from 959.8 s to 37.3 s.

---

## 获取链接与学术资源

> ## Access Links & Resources

- **PDF 论文：** [查看 PDF](https://arxiv.org/pdf/2609.36835)
- **HTML 网页版：** [实验性 HTML 论文页面](https://arxiv.org/html/2609.36835v1)
- **论文源码：** [TeX 源码包](https://arxiv.org/src/2609.36835)
- **外部学术工具检索：** 
  - [Google 学术检索](https://scholar.google.com/scholar_lookup?arxiv_id=2609.36835)
  - [Semantic Scholar 检索](https://api.semanticscholar.org/arXiv:2609.36835)
  - [NASA ADS 检索](https://ui.adsabs.harvard.edu/abs/arXiv:2609.36835)

> - **PDF:** [View PDF](https://arxiv.org/pdf/2609.36835)
> - **HTML:** [Experimental HTML Version](https://arxiv.org/html/2609.36835v1)
> - **Source Code:** [TeX Source](https://arxiv.org/src/2609.36835)
> - **External Tools:** 
>   - [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.36835)
>   - [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.36835)
>   - [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.36835)
