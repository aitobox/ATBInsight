---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- Diffusion Transformers
- 扩散模型
- 模型加速
- 特征缓存
- 有理插值
title: BRACE：通过重心有理预测驯服尖锐不规则性，实现快速扩散 Transformer 推理
---
### 文章背景与核心概要
扩散 Transformer（DiTs）在生成高质量图像和视频方面取得了卓越的成功，但通常伴随着巨大的计算开销。虽然时间特征缓存技术可以绕过冗余计算，但传统的“缓存后预测”方法依赖于基于导数的多项式，在搞加速比下往往难以应对不稳定的长步长预测。

为了克服这一瓶颈，本文引入了 **BRACE**（**B**arycentric **R**ational Forecasting with **C**hebyshev **E**nhancement，即带有切比雪夫增强的重心有理预测）。BRACE 不再使用导数驱动的多项式外推法，而是依赖于特征驱动的有理预测。通过维护稀疏历史特征的局部滑动窗口并采用自适应切比雪夫权重来构建重心有理函数，BRACE 直接聚合原始特征以保持数值稳定性。实验表明，BRACE 在各种 DiT 架构中均以可忽略的开销实现了卓越的质量与效率平衡。

---

## 摘要 (Abstract)

Diffusion Transformers (DiTs) have demonstrated exceptional performance in high-fidelity image and video generation. To alleviate their massive computational overhead, temporal feature caching has been proposed to bypass redundant computations. However, existing cache-then-forecast methods driven by derivative-based polynomials often cause severe quality degradation under high acceleration due to unstable long-step predictions. To address this bottleneck, we propose Barycentric Rational Forecasting with Chebyshev Enhancement (BRACE). Motivated by the observation that DiT feature trajectories are globally smooth yet frequently exhibit sharp irregularities and local non-smoothness, BRACE shifts the paradigm from derivative-driven polynomial extrapolation to feature-driven rational forecasting. Specifically, it maintains a local sliding window to cache sparse historical features and leverages adapted Chebyshev weights to formulate a barycentric rational function, directly aggregating these raw features to ensure numerical stability. Extensive experiments demonstrate that BRACE achieves state-of-the-art quality-efficiency trade-offs across various DiT architectures with negligible computational overhead.

> Diffusion Transformers (DiTs) have demonstrated exceptional performance in high-fidelity image and video generation. To alleviate their massive computational overhead, temporal feature caching has been proposed to bypass redundant computations. However, existing cache-then-forecast methods driven by derivative-based polynomials often cause severe quality degradation under high acceleration due to unstable long-step predictions. To address this bottleneck, we propose Barycentric Rational Forecasting with Chebyshev Enhancement (BRACE). Motivated by the observation that DiT feature trajectories are globally smooth yet frequently exhibit sharp irregularities and local non-smoothness, BRACE shifts the paradigm from derivative-driven polynomial extrapolation to feature-driven rational forecasting. Specifically, it maintains a local sliding window to cache sparse historical features and leverages adapted Chebyshev weights to formulate a barycentric rational function, directly aggregating these raw features to ensure numerical stability. Extensive experiments demonstrate that BRACE achieves state-of-the-art quality-efficiency trade-offs across various DiT architectures with negligible computational overhead.

---

## 论文元数据 (Paper Metadata)

* **arXiv ID:** [2608.07572](https://arxiv.org/abs/2608.07572) [cs.CV]
* **Authors:** Jinlong Yang, Jinke Wu, Lizilin, Yao Zhou
* **Primary Subject:** Computer Vision and Pattern Recognition (`cs.CV`)
* **Accepted at:** ACM MM 2026
* **Project Page:** [BRACE Project Page](https://youngkinlon.github.io/BRACE-Taming-Sharp-Irregularities-via-Barycentric-Rational-Forecasting-for-Fast-DiT-Inference/)

> * **arXiv ID:** [2608.07572](https://arxiv.org/abs/2608.07572) [cs.CV]
> * **Authors:** Jinlong Yang, Jinke Wu, Lizilin, Yao Zhou
> * **Primary Subject:** Computer Vision and Pattern Recognition (`cs.CV`)
> * **Accepted at:** ACM MM 2026
> * **Project Page:** [BRACE Project Page](https://youngkinlon.github.io/BRACE-Taming-Sharp-Irregularities-via-Barycentric-Rational-Forecasting-for-Fast-DiT-Inference/)

---

## 全文与资源 (Full-Text & Resources)
* **PDF 版本:** [查看 PDF](https://arxiv.org/pdf/2608.07572)
* **HTML 版本:** [arXiv HTML (实验性)](https://arxiv.org/html/2608.07572v2)
* **TeX 源码:** [源码压缩包](https://arxiv.org/src/2608.07572)
* **开源协议:** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/)

> * **PDF Version:** [View PDF](https://arxiv.org/pdf/2608.07572)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.07572v2)
> * **TeX Source:** [Source Archive](https://arxiv.org/src/2608.07572)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)