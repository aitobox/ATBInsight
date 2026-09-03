---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-04
hide:
- navigation
tags:
- Diffusion Transformers
- DiT
- 模型加速
- Top-k 选择
- 计算机视觉
title: Shiva-DiT：用于高效扩散 Transformer 的基于残差的可微分 Top-$k$ 选择方法
---
### 文章背景与核心概要
扩散 Transformer（DiT）在处理高分辨率任务时面临着巨大的计算瓶颈，因为自注意力机制的计算复杂度随 Token 序列长度呈二次方增长。现有的 Token 剪枝方法难以同时满足端到端可学习性、低训练开销以及实现可预测性能所需的确定性 Token 数量。

本文引入了 **Shiva-DiT**，这是一种由**基于残差的可微分 Top-$k$ 选择（Residual-Based Differentiable Top-$k$ Selection）**驱动的新型方法。其核心亮点包括：
* **高效的前向和反向传播：** 在前向传播过程中执行硬 Top-$k$ 选择，同时利用残差感知的直通估计器（straight-through estimator）将梯度传播至 Token 分数和预算 $k$，而无需评估开销高昂的次级主干网络路径。
* **自适应控制：** 具备*上下文感知路由器（Context-Aware Router）*和*自适应比例策略（Adaptive Ratio Policy）*，能够在指定的平均目标预算下，动态学习依赖于层数和时间步的保留调度方案。
* **实证性能：** 在 SD3-Medium、Flux.1-dev 和 PixArt-$\Sigma$ 上进行了测试，证明了其在减少 FLOPs 和降低延迟方面的一致性。具体而言，在 SD3-Medium 上，Shiva-DiT 在四个不同的工作点上实现了 **$1.54\times$ 的实际运行加速（wall-clock speedup）**，同时保持了具有竞争力的生成保真度。

---

# Shiva-DiT: Residual-Based Differentiable Top-$k$ Selection for Efficient Diffusion Transformers

## Summary

> Diffusion Transformers (DiTs) face significant computational bottlenecks at high resolutions because self-attention mechanisms scale quadratically with the token sequence length. Existing token pruning methods struggle to simultaneously provide end-to-end learnability, low training overhead, and deterministic token counts required for predictable performance. 
> 
> This paper introduces **Shiva-DiT**, a novel approach powered by **Residual-Based Differentiable Top-$k$ Selection**. Key highlights include:
> * **Efficient Forward and Backward Passes:** Executes hard top-k selection during the forward pass while utilizing a residual-aware straight-through estimator to propagate gradients to both token scores and the budget $k$ without evaluating an expensive secondary backbone path.
> * **Adaptive Control:** Features a *Context-Aware Router* and *Adaptive Ratio Policy* that dynamically learn layer- and timestep-dependent retention schedules under a specified target average budget.
> * **Empirical Performance:** Tested across SD3-Medium, Flux.1-dev, and PixArt-$\Sigma$, demonstrating consistent reductions in FLOPs and latency. Specifically, on SD3-Medium, Shiva-DiT delivers a **$1.54\times$ wall-clock speedup** with competitive fidelity across four distinct operating points.

---

## Paper Metadata

| 字段 | 详情 |
| :--- | :--- |
| **标题** | Shiva-DiT: Residual-Based Differentiable Top-$k$ Selection for Efficient Diffusion Transformers |
| **作者** | Jiaji Zhang, Hailiang Zhao, Jiaju Wu, Ruichao Sun, Xinkui Zhao, Shuiguang Deng |
| **学科分类** | 机器学习 (`cs.LG`)；人工智能 (`cs.AI`)；计算机视觉与模式识别 (`cs.CV`) |
| **arXiv ID** | [arXiv:2602.05605 [cs.LG]](https://arxiv.org/abs/2602.05605) |
| **DOI** | [10.48550/arXiv.2602.05605](https://doi.org/10.48550/arXiv.2602.05605) |
| **提交历史** | v1：2026年2月5日<br>v2：2026年9月2日（此版本） |

> | Field | Details |
> | :--- | :--- |
> | **Title** | Shiva-DiT: Residual-Based Differentiable Top-$k$ Selection for Efficient Diffusion Transformers |
> | **Authors** | Jiaji Zhang, Hailiang Zhao, Jiaju Wu, Ruichao Sun, Xinkui Zhao, Shuiguang Deng |
> | **Subjects** | Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`); Computer Vision and Pattern Recognition (`cs.CV`) |
> | **arXiv ID** | [arXiv:2602.05605 [cs.LG]](https://arxiv.org/abs/2602.05605) |
> | **DOI** | [10.48550/arXiv.2602.05605](https://doi.org/10.48550/arXiv.2602.05605) |
> | **Submission History** | v1: Feb 5, 2026<br>v2: Sep 2, 2026 (This version) |

---

## Abstract

扩散 Transformer（DiT）在高分辨率下成本高昂，因为自注意力机制的计算复杂度随 Token 序列长度呈二次方增长。现有的剪枝方法无法同时提供端到端的可学习性、较低的训练开销以及用于可预测 Token 依赖计算的确定性 Token 数量。我们提出了 Shiva-DiT，它基于残差可微分 Top-k 选择方法。其前向传播执行硬 Top-k 选择，而残差感知的直通估计器将梯度传播到 Token 分数和预算 $k$，而无需评估第二个主干网络路径。上下文感知路由器和自适应比例策略在目标平均预算下学习依赖于层和时间步的保留调度。在 SD3-Medium、Flux.1-dev 和 PixArt-$\Sigma$ 上的实验表明，FLOPs 和测得的延迟均有一致的减少。在 SD3-Medium 上，Shiva-DiT 提供了四个保真度-延迟工作点，并在保持竞争力的保真度的同时实现了 1.54 倍的实际运行加速。

> > Diffusion Transformers (DiTs) are costly at high resolution because self-attention scales quadratically with token sequence length. Existing pruning methods do not jointly provide end-to-end learnability, low training overhead, and deterministic token counts for predictable token-dependent computation. We propose Shiva-DiT, based on Residual-Based Differentiable Top-k Selection. Its forward pass executes hard top-k selection, while a residual-aware straight-through estimator propagates gradients to both token scores and the budget k without evaluating a second backbone path. A Context-Aware Router and Adaptive Ratio Policy learn layer- and timestep-dependent retention schedules under a target average budget. Experiments on SD3-Medium, Flux.1-dev, and PixArt-$\Sigma$ show consistent reductions in FLOPs and measured latency. On SD3-Medium, Shiva-DiT provides four fidelity-latency operating points and reaches a 1.54x wall-clock speedup with competitive fidelity.

---

## Links & Resources

* **全文选项：** [查看 PDF](https://arxiv.org/pdf/2602.05605) | [HTML（实验性）](https://arxiv.org/html/2602.05605v2) | [TeX 源码](https://arxiv.org/src/2602.05605)
* **外部参考：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2602.05605) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2602.05605) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2602.05605)

> * **Full-Text Options:** [View PDF](https://arxiv.org/pdf/2602.05605) | [HTML (Experimental)](https://arxiv.org/html/2602.05605v2) | [TeX Source](https://arxiv.org/src/2602.05605)
> * **External References:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2602.05605) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2602.05605) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2602.05605)