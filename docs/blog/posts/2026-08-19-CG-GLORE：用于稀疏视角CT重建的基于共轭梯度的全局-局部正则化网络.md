---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 稀疏视角CT
- 深度展开
- 共轭梯度优化
- 全局-局部正则化
- 计算机视觉
title: CG-GLORE：用于稀疏视角CT重建的基于共轭梯度的全局-局部正则化网络
---
### 文章背景与核心概要
稀疏视角计算机断层扫描（CT）是减少辐射暴露的关键技术，但它也带来了病态逆问题和严重条纹伪影等重大挑战。**CG-GLORE** 是一种新颖且紧凑的深度展开框架，旨在通过将二阶优化原理与先进的神经网络架构相集成来解决这些问题。

该方法在每个展开阶段利用基于共轭梯度的方法来求解线性系统，从而保持了数据保真项中由物理学导出的曲率。此外，**全局-局部正则化网络（GLORE）** 将局部卷积特征提取与基于 Nyström 注意力的长距离依赖建模相结合，能够重建出具有优异解剖学细节和稳定性的高保真图像。

---

# CG-GLORE：用于稀疏视角CT重建的基于共轭梯度的全局-局部正则化网络 (CG-GLORE: A Conjugate Gradient-Based Global-Local Regularization Network for Sparse-View CT Reconstruction)

> # CG-GLORE: A Conjugate Gradient-Based Global-Local Regularization Network for Sparse-View CT Reconstruction

**作者：** Tran Xuan Hieu Le, Doanh C. Bui, Vu Trung Duong Le, Hoai Luan Pham, Khang Nguyen, Mai K. Nguyen, Tu Bao Ho, Yasuhiko Nakashima  
**发布时间：** 2026年8月15日  
**会议/期刊：** 已被 BMVC 2026 接受并将在会上展示  
**arXiv ID：** [2608.15246](https://arxiv.org/abs/2608.15246)

> **Authors:** Tran Xuan Hieu Le, Doanh C. Bui, Vu Trung Duong Le, Hoai Luan Pham, Khang Nguyen, Mai K. Nguyen, Tu Bao Ho, Yasuhiko Nakashima  
> **Published:** August 15, 2026  
> **Venue:** Accepted for presentation at BMVC 2026  
> **arXiv ID:** [2608.15246](https://arxiv.org/abs/2608.15246)

---

## 摘要 (Summary)

稀疏视角计算机断层扫描（CT）是减少辐射暴露的一项重要技术，但它带来了严峻的挑战，包括病态逆问题和严重的条纹伪影。**CG-GLORE** 是一种新颖、紧凑的深度展开框架，旨在通过将二阶优化原理与先进的神经网络架构相结合来解决这些问题。

> Sparse-view Computed Tomography (CT) is a vital technique for reducing radiation exposure, but it introduces significant challenges, including ill-posed inverse problems and severe streak artifacts. **CG-GLORE** is a novel, compact deep unrolling framework designed to address these issues by integrating second-order optimization principles with advanced neural network architectures. 

通过在每个展开阶段利用基于共轭梯度的方法来求解线性系统，该方法保留了数据保真项由物理特性决定的曲率。此外，**全局-局部正则化网络（GLORE）**——结合了局部卷积特征提取与基于 Nyström 注意力的长距离依赖建模——能够重建出具有卓越解剖学细节和稳定性的高保真图像。

> By utilizing a conjugate gradient-based approach to solve linear systems within each unrolled stage, the method preserves the physics-induced curvature of the data-fidelity term. Furthermore, the **Global-Local Regularization Network (GLORE)**—which combines local convolutional feature extraction with Nyström attention-based long-range dependency modeling—enables the reconstruction of high-fidelity images with superior anatomical detail and stability.

---

## 核心特性 (Key Features)

*   **受二阶优化启发的展开机制：** 与标准的一阶深度学习方法不同，CG-GLORE 利用结构化的 Hessian 替代矩阵，在重建过程中保持物理一致性。
*   **GLORE 架构：** 一个双路径正则化模块，利用稀疏分块（patchification）和 Nyström 注意力同时捕获局部纹理和非局部解剖学依赖关系。
*   **性能表现：** 在 AAPM 和 DeepLesion 数据集上的广泛测试表明，与最先进的重建技术相比，该模型在定量结果、收敛稳定性和降低噪声功率方面均表现出卓越的性能。

> *   **Second-Order Inspired Unrolling:** Unlike standard first-order deep learning methods, CG-GLORE leverages a structured Hessian surrogate to maintain physical consistency during the reconstruction process.
*   **GLORE Architecture:** A dual-path regularization module that captures both local textures and non-local anatomical dependencies using sparse patchification and Nyström attention.
*   **Performance:** Extensive testing on the AAPM and DeepLesion datasets demonstrates that the model achieves robust quantitative results, stable convergence, and reduced noise power compared to state-of-the-art reconstruction techniques.

---

## 访问与资源 (Access & Resources)

*   **查看 PDF：** [arXiv:2608.15246](https://arxiv.org/pdf/2608.15246)
*   **HTML 版本：** [实验性 HTML](https://arxiv.org/html/2608.15246v1)
*   **TeX 源码：** [源代码](https://arxiv.org/src/2608.15246)
*   **DOI：** [10.48550/arXiv.2608.15246](https://doi.org/10.48550/arXiv.2608.15246)

> *   **View PDF:** [arXiv:2608.15246](https://arxiv.org/pdf/2608.15246)
*   **HTML Version:** [Experimental HTML](https://arxiv.org/html/2608.15246v1)
*   **TeX Source:** [Source Code](https://arxiv.org/src/2608.15246)
*   **DOI:** [10.48550/arXiv.2608.15246](https://doi.org/10.48550/arXiv.2608.15246)

---

## 书目信息 (Bibliographic Information)
*   **主要学科：** 计算机视觉与模式识别 (cs.CV)
*   **次要学科：** 人工智能 (cs.AI)
*   **引用格式：** Le, T. X. H., et al. (2026). *CG-GLORE: A Conjugate Gradient-Based Global-Local Regularization Network for Sparse-View CT Reconstruction*. arXiv:2608.15246.

> *   **Primary Subject:** Computer Vision and Pattern Recognition (cs.CV)
> *   **Secondary Subject:** Artificial Intelligence (cs.AI)
> *   **Citation:** Le, T. X. H., et al. (2026). *CG-GLORE: A Conjugate Gradient-Based Global-Local Regularization Network for Sparse-View CT Reconstruction*. arXiv:2608.15246.