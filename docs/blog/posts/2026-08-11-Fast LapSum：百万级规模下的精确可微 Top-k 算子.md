---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-11
hide:
- navigation
tags:
- 深度学习
- 可微计算
- Top-k
- 稀疏计算
- 算法优化
title: Fast LapSum：百万级规模下的精确可微 Top-k 算子
---
### 文章背景与核心概要
Top-$k$ 操作是现代稀疏计算的基石，在 Token 路由、专家激活（Expert Activation）以及注意力剪枝等任务中发挥着至关重要的作用。然而，标准的“硬”Top-$k$ 操作会阻断梯度传播，而现有的“软”（连续）松弛方法在处理大规模模型时往往计算开销过大。

Fast LapSum 提出了一种精确预算的软 Top-$k$ 原语，该方法在排序后仅需线性时间即可完成计算。与以往放宽归一化约束的方法不同，Fast LapSum 在保持端到端完全可微的同时，精确维持了 $k$ 个元素的总选择权重。通过利用线性时间阈值计算和针对极端规模的概率区间估计，该方法实现了极低的计算开销，处理 $10^8$ 个分数仅需 5.23 毫秒。

---

## 摘要
Top-$k$ 操作是现代稀疏计算的基石，对于 Token 路由、专家激活和注意力剪枝至关重要。然而，标准的“硬”Top-$k$ 操作会阻断梯度，而现有的“软”（连续）松弛方法对于大规模模型来说计算成本往往过高。

> The top-$k$ operation is a cornerstone of modern sparse computation, essential for token routing, expert activation, and attention pruning. However, standard "hard" top-$k$ operations block gradients, and existing "soft" (continuous) relaxations are often too computationally expensive for large-scale models. 

**Fast LapSum** 引入了一种精确预算的软 Top-$k$ 原语，它在排序后以线性时间运行。与之前放宽归一化约束的方法不同，Fast LapSum 在保持端到端完全可微的同时，保留了 $k$ 的精确选择质量。通过利用线性时间阈值计算和针对极端规模的概率区间估计，该方法实现了可忽略不计的开销，处理 $10^8$ 个分数仅需 $5.23$ 毫秒。

> **Fast LapSum** introduces an exact-budget soft top-$k$ primitive that operates in linear time after sorting. Unlike previous methods that relax normalization constraints, Fast LapSum preserves an exact selection mass of $k$ while remaining fully differentiable end-to-end. By utilizing a linear-time threshold computation and probabilistic bracketing for extreme scales, the method achieves negligible overhead, processing $10^8$ scores in just $5.23$ ms.

---

## 核心特性
*   **精确可微性：** 首个在保持 $k$ 的精确选择质量的同时实现完全可微的方法。
*   **高性能：** 具有线性时间复杂度的 GPU 优化求解器。
*   **可扩展性：** 高效处理百万级输入（$10^6$ 到 $10^8$ 个分数），延迟极低。
*   **实证效用：** 在生成百万像素稀疏对抗样本（速度提升了一个数量级）和训练完全可微的稀疏图像编码器方面展现了卓越的性能。

> *   **Exact Differentiability:** The first method to maintain an exact selection mass of $k$ while being fully differentiable.
> *   **High Performance:** GPU-optimized solver with linear-time complexity.
> *   **Scalability:** Efficiently handles million-scale inputs ($10^6$ to $10^8$ scores) with minimal latency.
> *   **Proven Utility:** Demonstrated success in generating megapixel sparse adversarial examples (with an order-of-magnitude speedup) and training fully differentiable sparse image coders.

---

## 访问与资源
*   **PDF:** [查看论文](https://arxiv.org/pdf/2608.06912)
*   **HTML:** [实验性 HTML 版本](https://arxiv.org/html/2608.06912v1)
*   **TeX 源码:** [源代码](https://arxiv.org/src/2608.06912)
*   **许可协议:** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/)  
    <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> *   **PDF:** [View Paper](https://arxiv.org/pdf/2608.06912)
> *   **HTML:** [Experimental HTML Version](https://arxiv.org/html/2608.06912v1)
> *   **TeX Source:** [Source Code](https://arxiv.org/src/2608.06912)
> *   **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)  
>     <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## 引用与元数据
*   **DOI:** [https://doi.org/10.48550/arXiv.2608.06912](https://doi.org/10.48550/arXiv.2608.06912)
*   **主要学科:** 人工智能 (cs.AI)
*   **文献工具:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.06912) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.06912) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.06912)

> *   **DOI:** [https://doi.org/10.48550/arXiv.2608.06912](https://doi.org/10.48550/arXiv.2608.06912)
> *   **Primary Subject:** Artificial Intelligence (cs.AI)
> *   **Bibliographic Tools:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.06912) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.06912) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.06912)