---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- MLLM
- 指代表达式分割
- Token压缩
- 计算机视觉
- ICML2026
title: 位置即全部：基于MLLM指代表达式分割的免费午餐式Token压缩策略
---
### 文章背景与核心概要
指代表达式分割（RES）旨在根据复杂的文本查询生成像素级的分割掩码。尽管多模态大语言模型（MLLM）显著提升了RES的性能，但也带来了巨大的计算瓶颈。本文研究了标准的Token压缩技术，并揭示了其中明显的性能下降现象。通过大量实验，作者发现RES的Token压缩必须保留**原始位置嵌入**和**局部相邻空间结构**，这表明视觉位置信息对该任务具有独特的关键作用。

为了解决这一问题，作者推出了 **PAYN**（*Position Is All You Need*），这是一种即插即用、无需训练且仅依赖位置信息的Token压缩方法。PAYN通过保留充分分布在局部相邻区域的Token并维持原始位置索引，从而保持了空间关系的一致性。在多个基准测试上的实验证实，PAYN在无需重新训练的情况下，优于现有的Token压缩策略。

---

# Position Is All You Need: A Free Lunch Token Compression Strategy for MLLM-based Referring Expression Segmentation

* **Authors:** Yuhan Liu, Yixiong Zou, Yuhua Li, Ruixuan Li  
* **Subjects:** Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`)  
* **Conference/Status:** Accepted by ICML 2026  
* **arXiv ID:** [arXiv:2608.26142 [cs.CL]](https://arxiv.org/abs/2608.26142)  
* **DOI:** [10.48550/arXiv.2608.26142](https://doi.org/10.48550/arXiv.2608.26142)  
* **Code Repository:** [GitHub - PAYN](https://github.com/YuhanLiu231/PAYN)  
* **Submission Date:** June 26, 2026  

> # Position Is All You Need: A Free Lunch Token Compression Strategy for MLLM-based Referring Expression Segmentation
> 
> * **Authors:** Yuhan Liu, Yixiong Zou, Yuhua Li, Ruixuan Li  
> * **Subjects:** Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`)  
> * **Conference/Status:** Accepted by ICML 2026  
> * **arXiv ID:** [arXiv:2608.26142 [cs.CL]](https://arxiv.org/abs/2608.26142)  
> * **DOI:** [10.48550/arXiv.2608.26142](https://doi.org/10.48550/arXiv.2608.26142)  
> * **Code Repository:** [GitHub - PAYN](https://github.com/YuhanLiu231/PAYN)  
> * **Submission Date:** June 26, 2026  

---

## 📌 Summary

> ## 📌 Summary

指代表达式分割（RES）涉及根据复杂的文本查询生成像素级的分割掩码。尽管多模态大语言模型（MLLMs）增强了RES的性能，但它们也引入了显著的计算瓶颈。

> Referring Expression Segmentation (RES) involves generating pixel-wise segmentation masks based on complex textual queries. Although Multimodal Large Language Models (MLLMs) enhance RES performance, they introduce a significant computational bottleneck. 

本文研究了标准的Token压缩技术，并揭示了一个显著的性能下降问题。通过广泛的实验，作者发现RES的Token压缩需要保留**原始位置嵌入**以及**局部相邻空间结构**，这表明视觉位置信息对该任务具有无可替代的关键性。

> This paper investigates standard token compression techniques and uncovers a notable performance drop. Through extensive experiments, the authors discover that RES token compression requires preserving **original position embeddings** and **local neighboring spatial structures**, showing that visual position information is uniquely critical for this task. 

为了解决这一问题，作者推出了 **PAYN**（*Position Is All You Need*），这是一种完全依赖位置信息的即插即用、无需训练的Token压缩方法。PAYN通过保留在局部相邻区域中充分分布的Token，同时保留原始位置索引，来维护空间关系的一致性。多个基准测试上的实验证实，PAYN在不需要重新训练的情况下，超越了现有的Token压缩策略。

> To address this, the authors introduce **PAYN** (*Position Is All You Need*), a plug-and-play, training-free token compression method reliant strictly on position information. PAYN maintains spatial relational consistency by retaining tokens adequately distributed across local neighboring regions while preserving original positional indices. Experiments on multiple benchmarks confirm that PAYN outperforms existing token compression strategies without requiring retraining.

---

## 🔗 Full-Text & Resources

> ## 🔗 Full-Text & Resources

* [查看 PDF (View PDF)](https://arxiv.org/pdf/2608.26142)
* [TeX 源码 (TeX Source)](https://arxiv.org/src/2608.26142)
* [代码与实现 (Code & Implementation)](https://github.com/YuhanLiu231/PAYN)
* [谷歌学术 (Google Scholar)](https://scholar.google.com/scholar_lookup?arxiv_id=2608.26142)
* [语义学者 (Semantic Scholar)](https://api.semanticscholar.org/arXiv:2608.26142)

> * [View PDF](https://arxiv.org/pdf/2608.26142)
> * [TeX Source](https://arxiv.org/src/2608.26142)
> * [Code & Implementation](https://github.com/YuhanLiu231/PAYN)
> * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.26142)
> * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.26142)