---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-12
hide:
- navigation
tags:
- Transformer
- 注意力机制
- 随机矩阵理论
- 模型剪枝
- PEFT
title: 谱奇异值揭示了Transformer注意力机制中占主导地位的学习结构
---
### 文章背景与核心概要
本文将**马尔琴科-帕斯图尔（Marchenko-Pastur, MP）随机矩阵理论**应用于预训练Transformer的注意力权重，将每个投影矩阵分解为类似随机噪声的主体（bulk）和一组谱奇异值（outliers）。

通过在Mistral-7B上进行因果验证，作者证明将MP识别出的奇异值（即信号）置零，会使HellaSwag、MMLU和PIQA等基准测试的性能降至接近随机猜测的水平。相比之下，将数量匹配的主体奇异值子集置零只会导致轻微的性能退化。

通过对11个预训练Transformer的研究，该论文发现了五个循环出现的结构模式：1. 谱奇异值编码了学习结构的主要成分；2. 查询（$Q$）投影包含最多的奇异值；3. 分组查询注意力（GQA）下的值（$V$）投影表现出信号与噪声分离的混淆；4. 入口级奇异值在$Q$矩阵中自然组织成结构化的行带（row-bands），在输出（$O$）矩阵中组织成列带（column-bands）；5. 特定的残差流维度在键（$K$）和输出（$O$）矩阵的各层中持续作为带状奇异值（band outliers）存在。这些发现为推进**参数高效微调（PEFT）**和**结构化模型剪枝**提供了具有可操作性的见解。

---

## Spectral Outliers Reveal Dominant Learned Structure in Transformer Attention

**Authors:** Kasun Dewage, Marianna Pensky, Suranadi De Silva, T. H. Bandara  
**Published:** August 8, 2026 (Accepted at ICMLA 2026; to appear in IEEE proceedings)  
**Subjects:** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`)  
**ArXiv ID:** [arXiv:2608.07921](https://arxiv.org/abs/2608.07921) [cs.LG]  

> ## Spectral Outliers Reveal Dominant Learned Structure in Transformer Attention
> 
> **Authors:** Kasun Dewage, Marianna Pensky, Suranadi De Silva, T. H. Bandara  
> **Published:** August 8, 2026 (Accepted at ICMLA 2026; to appear in IEEE proceedings)  
> **Subjects:** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`)  
> **ArXiv ID:** [arXiv:2608.07921](https://arxiv.org/abs/2608.07921) [cs.LG]  

---

## Summary

This paper applies **Marchenko-Pastur (MP) random matrix theory** to pre-trained transformer attention weights to dissect each projection matrix into a random-like bulk and a collection of spectral outliers. 

Through causal validation on Mistral-7B, the authors demonstrate that zeroing out the MP-identified outliers (signal) reduces performance on benchmarks like HellaSwag, MMLU, and PIQA to near random chance. In contrast, zeroing a count-matched subset of bulk singular values yields only minor degradation. 

Across 11 pre-trained transformers, the study uncovers five recurring structural patterns:
1. Spectral outliers encode the dominant components of the learned structure.
2. Query ($Q$) projections carry the highest number of outliers.
3. Value ($V$) projections under grouped-query attention exhibit a conflated signal/noise separation.
4. Entry-level outliers naturally organize into structured row-bands in $Q$ matrices and column-bands in output ($O$) matrices.
5. Specific residual-stream dimensions persist as band outliers consistently across layers in key ($K$) and output ($O$) matrices.

The findings offer actionable insights for advancing **parameter-efficient fine-tuning (PEFT)** and **structured model pruning**.

> ## Summary
> 
> This paper applies **Marchenko-Pastur (MP) random matrix theory** to pre-trained transformer attention weights to dissect each projection matrix into a random-like bulk and a collection of spectral outliers. 
> 
> Through causal validation on Mistral-7B, the authors demonstrate that zeroing out the MP-identified outliers (signal) reduces performance on benchmarks like HellaSwag, MMLU, and PIQA to near random chance. In contrast, zeroing a count-matched subset of bulk singular values yields only minor degradation. 
> 
> Across 11 pre-trained transformers, the study uncovers five recurring structural patterns:
> 1. Spectral outliers encode the dominant components of the learned structure.
> 2. Query ($Q$) projections carry the highest number of outliers.
> 3. Value ($V$) projections under grouped-query attention exhibit a conflated signal/noise separation.
> 4. Entry-level outliers naturally organize into structured row-bands in $Q$ matrices and column-bands in output ($O$) matrices.
> 5. Specific residual-stream dimensions persist as band outliers consistently across layers in key ($K$) and output ($O$) matrices.
> 
> The findings offer actionable insights for advancing **parameter-efficient fine-tuning (PEFT)** and **structured model pruning**.

---

## Links & Resources

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.07921) | [HTML (Experimental)](https://arxiv.org/html/2608.07921v1) | [TeX Source](https://arxiv.org/src/2608.07921)
* **Citations & References:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07921) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07921) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.07921)

> ## Links & Resources
> 
> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.07921) | [HTML (Experimental)](https://arxiv.org/html/2608.07921v1) | [TeX Source](https://arxiv.org/src/2608.07921)
> * **Citations & References:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07921) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07921) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.07921)