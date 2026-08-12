---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-11
hide:
- navigation
tags:
- MXene
- 超表面
- 深度学习
- 光谱预测
- 迁移学习
title: 通过多通道光谱精细化与Savitzky-Golay平滑优化基于MXene超表面的光谱预测
---
### 文章背景与核心概要
本文探讨了基于MXene材料的太阳能吸收器在电磁光谱预测中所面临的计算强度挑战。为了替代传统耗时且计算量巨大的全波求解器，作者提出了一种高效的深度学习新框架，能够显著加速纳米光子学的正向设计流程。

该研究的核心创新在于将预训练的 MobileNet v2 迁移学习模型与**多通道光谱精细化**（multi-channel spectral refinement）模块相结合，并引入了 **Savitzky-Golay 平滑算法**来有效降低高频预测噪声。基于 $64\times64$ 像素的超表面设计输入，该模型能够高精度地预测 102 点吸收光谱。实验结果表明，该框架在各项关键性能指标上均显著优越于标准的 CNN 架构，为快速实现纳米光子学器件设计提供了一种极具扩展性的技术方案。

---

# Optimizing Spectral Prediction in MXene-Based Metasurfaces Through Multi-Channel Spectral Refinement and Savitzky-Golay Smoothing

**arXiv:** [2602.08406](https://arxiv.org/abs/2602.08406)  
**Subjects:** Optics (physics.optics); Artificial Intelligence (cs.AI); Signal Processing (eess.SP)  
**Authors:** Shujaat Khan, Waleed Iqbal Waseer, Muhammad Shahid Jabbar

> **arXiv:** [2602.08406](https://arxiv.org/abs/2602.08406)  
> **Subjects:** Optics (physics.optics); Artificial Intelligence (cs.AI); Signal Processing (eess.SP)  
> **Authors:** Shujaat Khan, Waleed Iqbal Waseer, Muhammad Shahid Jabbar

---

## Summary
本研究旨在解决基于 MXene 的太阳能吸收器电磁光谱预测中的计算密集性问题。作者提出了一种新颖的深度学习框架，用更高效的预测模型取代了传统且耗时的全波求解器。通过整合**迁移学习**（使用预训练的 MobileNet v2）、**多通道光谱精细化**以及 **Savitzky-Golay 平滑**，该模型基于 $64\times64$ 的超表面设计，实现了对 102 点吸收光谱的高精度预测。与标准的 CNN 架构相比，该框架表现出更优越的性能，为快速纳米光子学设计提供了一种可扩展的解决方案。

> ## Summary
> This research addresses the computational intensity of predicting electromagnetic spectra for MXene-based solar absorbers. The authors propose a novel deep learning framework that replaces traditional, time-consuming full-wave solvers with a more efficient predictive model. By integrating **transfer learning** (using a pretrained MobileNet v2), **multi-channel spectral refinement**, and **Savitzky-Golay smoothing**, the model achieves high-accuracy predictions for 102-point absorption spectra based on $64\times64$ metasurface designs. The framework demonstrates superior performance compared to standard CNN architectures, offering a scalable solution for rapid nanophotonic design.

---

## Key Technical Contributions
*   **网络架构：** 利用微调后的 MobileNet v2 来处理超表面几何结构并预测光谱输出。
*   **多通道精细化：** 实现了通过多个卷积通道处理特征图的模块，以改善特征提取效果。
*   **噪声抑制：** 采用 Savitzky-Golay 平滑技术，有效降低预测光谱中的高频噪声。
*   **性能指标：**
    *   **均方根误差 (RMSE)：** 0.0227
    *   **决定系数 ($R^2$)：** 0.9563
    *   **峰值信噪比 (PSNR)：** 33.10 dB

> ## Key Technical Contributions
> *   **Architecture:** Utilizes a fine-tuned MobileNet v2 to process metasurface geometry and predict spectral output.
> *   **Multi-Channel Refinement:** Implements a module that processes feature maps through multiple convolutional channels to improve feature extraction.
> *   **Noise Mitigation:** Employs Savitzky-Golay smoothing to effectively reduce high-frequency noise in the predicted spectra.
> *   **Performance Metrics:**
>     *   **RMSE:** 0.0227
>     *   **$R^2$ (Coefficient of Determination):** 0.9563
>     *   **PSNR (Peak Signal-to-Noise Ratio):** 33.10 dB

---

## Publication Details
*   **提交时间：** 2026年2月9日
*   **最后修订：** 2026年8月7日
*   **DOI：** [https://doi.org/10.48550/arXiv.2602.08406](https://doi.org/10.48550/arXiv.2602.08406)
*   **许可协议：** [知识共享署名 4.0 国际版 (Creative Commons Attribution 4.0 International)](http://creativecommons.org/licenses/by/4.0/)

> ## Publication Details
> *   **Submitted:** 9 Feb 2026
> *   **Last Revised:** 7 Aug 2026
> *   **DOI:** [https://doi.org/10.48550/arXiv.2602.08406](https://doi.org/10.48550/arXiv.2602.08406)
> *   **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)

---

## Access & Resources
*   **全文：** [查看 PDF](https://arxiv.org/pdf/2602.08406) | [HTML（实验性）](https://arxiv.org/html/2602.08406v2)
*   **源码：** [TeX 源码](https://arxiv.org/src/2602.08406)
*   **引用：** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2602.08406) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2602.08406) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2602.08406)

> ## Access & Resources
> *   **Full-Text:** [View PDF](https://arxiv.org/pdf/2602.08406) | [HTML (Experimental)](https://arxiv.org/html/2602.08406v2)
> *   **Source:** [TeX Source](https://arxiv.org/src/2602.08406)
> *   **Citations:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2602.08406) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2602.08406) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2602.08406)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">