---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-10
hide:
- navigation
tags:
- 信息检索
- 向量量化
- 语义检索
- Matryoshka表示
- FAISS
title: Matryoshka 哈希表示：面向模型感知的紧凑语义检索
---
### 文章背景与核心概要
检索增强生成（RAG）高度依赖于稠密检索，它将文档存储为学习到的向量，并通过最近邻搜索来回答查询。然而，在大规模语料库中，维护全精度向量会带来巨大的索引成本，这促使系统采用**量化**技术——将每个向量替换为仅占用几个字节的短代码。

虽然可变预算表示允许系统在不重新编码的情况下调整其效率与质量的平衡点，但单一目标下训练所有前缀通常会引入冲突。早期的比特位往往是一种妥协，会降低全宽度代码的性能，特别是当映射到二进制代码等低比特表示时。

为了克服这一问题，本文作者提出了**Matryoshka 哈希表示（MHR）**，这是一种两阶段的训练过程：1. **全宽度训练**：首先学习较长的二进制代码。2. **前缀组织**：冻结模型，并为可直接搜索的前缀训练额外的、零初始化（zero-initialized）的残差代码适配器。实验表明，MHR 在效率与检索性能之间取得了优异的平衡，能够有效赋能多种检索流水线。

---

## Matryoshka 哈希表示：面向模型感知的紧凑语义检索

> ## Matryoshka Hash Representations for Model-Aware Compact Semantic Retrieval

**arXiv:** [2609.07276](https://arxiv.org/abs/2609.07276) [cs.IR]  
**Submitted:** September 7, 2026  
**Authors:** Peichun Hua, Yunming Xiao  
**Subjects:** Information Retrieval (`cs.IR`); Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`)

> **arXiv:** [2609.07276](https://arxiv.org/abs/2609.07276) [cs.IR]  
> **Submitted:** September 7, 2026  
> **Authors:** Peichun Hua, Yunming Xiao  
> **Subjects:** Information Retrieval (`cs.IR`); Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`)

---

## 摘要概要

检索增强生成（RAG）高度依赖于稠密检索，通过将文档存储为学习得到的向量并通过最近邻搜索来回答查询。在语料库规模下，维护全精度向量成为主要的索引成本，这促使系统采用**量化**技术——将每个向量替换为仅占用几字节的简短代码。

虽然可变预算表示允许系统在不重新编码的情况下调整其效率与质量的运行点，但在单一目标下训练所有前缀通常会引入冲突。早期的比特位往往是一种妥协，导致全宽度代码性能下降，特别是当映射到诸如二进制代码的低比特表示时。

为了克服这一限制，作者引入了 **Matryoshka 哈希表示（MHR）**，这是一种两阶段的训练流程：
1. **全宽度训练**：首先学习较长的二进制代码。
2. **前缀组织**：冻结模型，并为可直接搜索的前缀训练额外的零初始化残差代码适配器。

### 关键结果与影响
* **非对称架构**：文档使用二进制代码（每坐标一位）存储，而查询则利用连续逻辑值（类似于乘积量化）以确保足够的表达能力。
* **搜索实现**：由 FAISS FastScan 提供技术支持。
* **性能表现**：在 MS MARCO 上训练并零样本迁移至七个 BEIR 数据集，MHR 在 32 字节下实现了 **.5561 NDCG@10** 和 **.6535 Recall@100**，在同等预算下优于竞争基线。
* **流水线集成**：该表示法有效地增强了常见流水线，包括用于全精度重排的候选初筛，以及剪枝低存储图索引（如 LEANN）。

> ## Abstract Summary
> 
> Retrieval-augmented generation (RAG) heavily relies on dense retrieval, storing documents as learned vectors and answering queries via nearest-neighbor search. At corpus scale, maintaining full-precision vectors becomes a dominant index cost, driving systems to employ **quantization**—replacing each vector with a short code of a few bytes. 
> 
> While variable-budget representations allow systems to adjust their efficiency-quality operating points without re-encoding, training all prefixes under a single objective typically introduces conflicts. Early bits become a compromise, degrading full-width code performance, particularly when mapped to low-bit representations like binary codes.
> 
> To overcome this, the authors introduce **Matryoshka Hash Representations (MHR)**, a two-stage training procedure:
> 1. **Full-Width Training:** Learns a longer binary code first.
> 2. **Prefix Organization:** Freezes the model and trains additional zero-initialized residual code adaptors for directly searchable prefixes.
> 
> ### Key Results & Impact
> * **Asymmetric Architecture:** Documents are stored using binary codes (one bit per coordinate), while queries utilize continuous logits (similar to Product Quantization) to ensure sufficient expressivity.
> * **Search Implementation:** Powered by FAISS FastScan.
> * **Performance:** Trained on MS MARCO and zero-shot transferred to seven BEIR datasets, MHR achieves **.5561 NDCG@10** and **.6535 Recall@100** at 32 bytes, outperforming competing baselines at the same budget.
> * **Pipeline Integration:** The representation effectively strengthens common pipelines, including candidate shortlisting for full-precision reranking and pruning low-storage graph indexes like LEANN.

---

## 论文元数据

* **引用格式：** [arXiv:2609.07276 [cs.IR]](https://arxiv.org/abs/2609.07276)
* **DOI：** [10.48550/arXiv.2609.07276](https://doi.org/10.48550/arXiv.2609.07276)
* **文档详情：** 10 页，2 张图，6 个表

> ## Paper Metadata
> 
> * **Cite as:** [arXiv:2609.07276 [cs.IR]](https://arxiv.org/abs/2609.07276)
> * **DOI:** [10.48550/arXiv.2609.07276](https://doi.org/10.48550/arXiv.2609.07276)
> * **Document Details:** 10 pages, 2 figures, 6 tables

---

## 全文与访问链接

* [查看 PDF](https://arxiv.org/pdf/2609.07276)
* [HTML 版本（实验性）](https://arxiv.org/html/2609.07276v1)
* [TeX 源码](https://arxiv.org/src/2609.07276)
* [音频摘要](https://arxiv.org/audio/2609.07276)

> ## Full-Text & Access Links
> 
> * [View PDF](https://arxiv.org/pdf/2609.07276)
> * [HTML Version (Experimental)](https://arxiv.org/html/2609.07276v1)
> * [TeX Source](https://arxiv.org/src/2609.07276)
> * [Audio Summary](https://arxiv.org/audio/2609.07276)