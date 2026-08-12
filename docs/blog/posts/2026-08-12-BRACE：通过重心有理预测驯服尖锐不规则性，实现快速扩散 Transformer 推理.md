---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-12
hide:
- navigation
tags:
- Diffusion Transformers
- 模型推理加速
- 重心有理插值
- 计算机视觉
- 生成式AI
title: BRACE：通过重心有理预测驯服尖锐不规则性，实现快速扩散 Transformer 推理
---
### 文章背景与核心概要

扩散 Transformer（DiTs）在高质量图像和视频生成领域表现卓越，但其巨大的计算开销限制了实际应用。为了解决这一问题，现有的研究多采用“缓存-预测”策略，即通过缓存历史特征来跳过冗余计算。然而，传统基于导数的多项式外推方法在处理高加速比时，往往因长步预测的不稳定性而导致生成质量严重下降。

本文提出的 **BRACE**（Barycentric Rational Forecasting with Chebyshev Enhancement）框架，通过将范式从导数驱动的多项式外推转向特征驱动的有理预测，有效解决了上述瓶颈。BRACE 利用局部滑动窗口缓存稀疏历史特征，并结合切比雪夫（Chebyshev）权重构建重心有理函数，直接对原始特征进行聚合。这种方法不仅保证了数值稳定性，还能在各种 DiT 架构中实现极佳的质量与效率平衡，且计算开销微乎其微。

---

## 摘要 (Abstract)

扩散 Transformer (DiTs) 在高保真图像和视频生成方面展现出了卓越的性能。为了缓解其巨大的计算开销，研究人员提出了时间特征缓存技术以绕过冗余计算。然而，现有的基于导数多项式的“缓存-预测”方法，在高加速比下往往因长步预测的不稳定性而导致严重的质量下降。为了解决这一瓶颈，我们提出了 **重心有理预测与切比雪夫增强 (BRACE)**。基于 DiT 特征轨迹虽然全局平滑但常表现出尖锐不规则性和局部非平滑性的观察，BRACE 将范式从导数驱动的多项式外推转向了特征驱动的有理预测。具体而言，它维护一个局部滑动窗口来缓存稀疏的历史特征，并利用自适应切比雪夫权重来构建重心有理函数，直接聚合这些原始特征以确保数值稳定性。广泛的实验表明，BRACE 在各种 DiT 架构中实现了最先进的质量-效率权衡，且计算开销可忽略不计。

> Diffusion Transformers (DiTs) have demonstrated exceptional performance in high-fidelity image and video generation. To alleviate their massive computational overhead, temporal feature caching has been proposed to bypass redundant computations. However, existing cache-then-forecast methods driven by derivative-based polynomials often cause severe quality degradation under high acceleration due to unstable long-step predictions. To address this bottleneck, we propose **Barycentric Rational Forecasting with Chebyshev Enhancement (BRACE)**. Motivated by the observation that DiT feature trajectories are globally smooth yet frequently exhibit sharp irregularities and local non-smoothness, BRACE shifts the paradigm from derivative-driven polynomial extrapolation to feature-driven rational forecasting. Specifically, it maintains a local sliding window to cache sparse historical features and leverages adapted Chebyshev weights to formulate a barycentric rational function, directly aggregating these raw features to ensure numerical stability. Extensive experiments demonstrate that BRACE achieves state-of-the-art quality-efficiency trade-offs across various DiT architectures with negligible computational overhead.

---

## 元数据 (Metadata)

* **arXiv ID:** [arXiv:2608.07572](https://arxiv.org/abs/2608.07572) [cs.CV]
* **学科分类:** 计算机视觉与模式识别 (`cs.CV`)；人工智能 (`cs.AI`)
* **作者:** Jinlong Yang, Jinke Wu, Lizilin, Yao Zhou
* **提交日期:** 2026年8月4日
* **备注:** 10页，6张图，5个表
* **项目主页:** [BRACE Project Website](https://youngkinlon.github.io/BRACE-Taming-Sharp-Irregularities-via-Barycentric-Rational-Forecasting-for-Fast-DiT-Inference/)

> * **arXiv ID:** [arXiv:2608.07572](https://arxiv.org/abs/2608.07572) [cs.CV]
> * **Subjects:** Computer Vision and Pattern Recognition (`cs.CV`); Artificial Intelligence (`cs.AI`)
> * **Authors:** Jinlong Yang, Jinke Wu, Lizilin, Yao Zhou
> * **Submitted on:** August 4, 2026
> * **Comments:** 10 pages, 6 figures, 5 tables
> * **Project Page:** [BRACE Project Website](https://youngkinlon.github.io/BRACE-Taming-Sharp-Irregularities-via-Barycentric-Rational-Forecasting-for-Fast-DiT-Inference/)

---

## 更多资源与链接 (Additional Resources & Links)

* **全文:** [查看 PDF](https://arxiv.org/pdf/2608.07572) | [HTML 版本](https://arxiv.org/html/2608.07572v1) | [TeX 源码](https://arxiv.org/src/2608.07572)
* **数字对象唯一标识符 (DOI):** [10.48550/arXiv.2608.07572](https://doi.org/10.48550/arXiv.2608.07572)
* **许可协议:** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/)

> * **Full-Text:** [View PDF](https://arxiv.org/pdf/2608.07572) | [HTML Version](https://arxiv.org/html/2608.07572v1) | [TeX Source](https://arxiv.org/src/2608.07572)
> * **Digital Object Identifier (DOI):** [10.48550/arXiv.2608.07572](https://doi.org/10.48550/arXiv.2608.07572)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)