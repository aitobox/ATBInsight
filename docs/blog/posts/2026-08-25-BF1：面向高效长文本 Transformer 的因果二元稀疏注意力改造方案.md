---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- Transformer
- 稀疏注意力
- 长文本处理
- 模型优化
- 机器学习
title: BF1：面向高效长文本 Transformer 的因果二元稀疏注意力改造方案
---
### 文章背景与核心概要
随着上下文长度的增加，稠密因果注意力（Dense causal attention）机制的计算成本会变得高昂，即便使用精确内核（exact kernels）进行优化也难以克服这一瓶颈。本文引入了 **BF1**，这是一种确定性的、块对齐的二元稀疏注意力（dyadic sparse-attention）架构，旨在作为高效长上下文 Transformer 的即插即用改造方案。

BF1 通过结合小型精确局部邻域、全局首个块以及按对数间距排列的历史块，构建了独特的注意力拓扑结构。在固定的块宽度下，每个改造后的层仅处理 $\mathcal{O}(n \log n)$ 个选定的 Token 交互，并保持 $\mathcal{O}(\log n)$ 的图通信深度。在系统性能方面，基于 NVIDIA RTX PRO 6000 Blackwell GPU 和优化的 BF16 实现评估表明，BF1 在 2K 到 4K Token 之间超越了稠密注意力的效率，并在 32K Token 时实现了 **10.91倍的单层预填充加速**。此外，将 Qwen3-0.6B 中 28 个注意力层中的 8 个进行改造，可将首 Token 预热全模型时间在 8K、16K 和 32K 长度下分别减少 **7.7%**、**11.3%** 和 **15.3%**，同时保留了其余稠密层的二次方扩展能力。经验证，在同等预算下，BF1 在困惑度（Perplexity）和语言建模任务中均展现出显著的性能优势与统计显著性。

---

# BF1: A Causal Dyadic Sparse-Attention Retrofit for Efficient Long-Context Transformers

> # BF1: A Causal Dyadic Sparse-Attention Retrofit for Efficient Long-Context Transformers

[![License icon](./images/fb423b2203a9.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/)

> [![License icon](./images/fb423b2203a9.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/)

* **arXiv ID:** [arXiv:2608.20427](https://arxiv.org/abs/2608.20427) [cs.LG]
* **Authors:** Hina Dixit
* **Submitted:** 19 August 2026
* **Subjects:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
* **Links:** [View PDF](https://arxiv.org/pdf/2608.20427) | [DOI](https://doi.org/10.48550/arXiv.2608.20427)

> * **arXiv ID:** [arXiv:2608.20427](https://arxiv.org/abs/2608.20427) [cs.LG]
> * **Authors:** Hina Dixit
> * **Submitted:** 19 August 2026
> * **Subjects:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
> * **Links:** [View PDF](https://arxiv.org/pdf/2608.20427) | [DOI](https://doi.org/10.48550/arXiv.2608.20427)

---

## Abstract Summary

> ## Abstract Summary

Dense causal attention becomes prohibitively expensive at long contexts, even when optimized with exact kernels. This paper introduces **BF1**, a deterministic, block-aligned dyadic sparse-attention architecture designed as a drop-in retrofit for efficient long-context Transformers. 

> Dense causal attention becomes prohibitively expensive at long contexts, even when optimized with exact kernels. This paper introduces **BF1**, a deterministic, block-aligned dyadic sparse-attention architecture designed as a drop-in retrofit for efficient long-context Transformers. 

### Key Design Elements & Mechanisms
* **Attention Topology:** Combines a small exact local neighborhood, a global first block, and logarithmically spaced historical blocks. 
* **Complexity:** For a fixed block width, every converted layer operates on $\mathcal{O}(n \log n)$ selected token interactions and maintains an $\mathcal{O}(\log n)$ graph communication depth.
* **Systems Performance:** Evaluated on an NVIDIA RTX PRO 6000 Blackwell GPU using an optimized BF16 implementation:
  * Outperforms dense attention efficiency between **2K and 4K tokens**.
  * Reaches a **10.91× per-layer prefill speedup** at 32K tokens.
  * Retrofitting 8 out of 28 attention layers in Qwen3-0.6B reduces warm whole-model time to the first token by **7.7% (8K)**, **11.3% (16K)**, and **15.3% (32K)**, while retaining quadratic scaling for the remaining dense layers.

> ### Key Design Elements & Mechanisms
> * **Attention Topology:** Combines a small exact local neighborhood, a global first block, and logarithmically spaced historical blocks. 
> * **Complexity:** For a fixed block width, every converted layer operates on $\mathcal{O}(n \log n)$ selected token interactions and maintains an $\mathcal{O}(\log n)$ graph communication depth.
> * **Systems Performance:** Evaluated on an NVIDIA RTX PRO 6000 Blackwell GPU using an optimized BF16 implementation:
>   * Outperforms dense attention efficiency between **2K and 4K tokens**.
>   * Reaches a **10.91× per-layer prefill speedup** at 32K tokens.
>   * Retrofitting 8 out of 28 attention layers in Qwen3-0.6B reduces warm whole-model time to the first token by **7.7% (8K)**, **11.3% (16K)**, and **15.3% (32K)**, while retaining quadratic scaling for the remaining dense layers.

### Empirical Evaluation & Language Modeling
Under a matched 1,000-step, 16.384M-token adaptation protocol:
* **Perplexity Rankings:** BF1 ranks first across three training seeds, achieving a mean perplexity of **1.68639** (compared to 1.69154 for a matched static-random nonlocal graph, 1.69258 for dense continued training, and 1.81505 for equal-budget local sliding).
* **Statistical Significance:** At seed 1234, packed-report paired intervals place Dense-CT 0.3169–0.4055% above BF1, and the static-random graph 17 0.2441–0.3642% above BF1.

Overall, BF1 establishes itself as a reproducible sparse operator and selective retrofit primitive that delivers concrete systems value in long-context scenarios.

> ### Empirical Evaluation & Language Modeling
> Under a matched 1,000-step, 16.384M-token adaptation protocol:
> * **Perplexity Rankings:** BF1 ranks first across three training seeds, achieving a mean perplexity of **1.68639** (compared to 1.69154 for a matched static-random nonlocal graph, 1.69258 for dense continued training, and 1.81505 for equal-budget local sliding).
> * **Statistical Significance:** At seed 1234, packed-report paired intervals place Dense-CT 0.3169–0.4055% above BF1, and the static-random graph 17 0.2441–0.3642% above BF1.
> 
> Overall, BF1 establishes itself as a reproducible sparse operator and selective retrofit primitive that delivers concrete systems value in long-context scenarios.