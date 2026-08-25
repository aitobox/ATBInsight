---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 侧扫声呐
- 自监督学习
- DINOv3
- 物理信息神经网络
- 水下机器视觉
title: BenthicDINO：面向视角不变侧扫声呐表征的物理融合自蒸馏方法
---
### 文章背景与核心概要
侧扫声呐（Side-Scan Sonar, SSS）图像的自动化感知长期以来一直受到物理声学伪影的严重阻碍，这些伪影将本质的海底反射率与瞬变观测几何混杂在一起。为了克服标准自监督学习（SSL）框架（通常依赖自然图像增强且无法解释声学退化）的局限性，作者引入了 **BenthicDINO**。该物理融合自蒸馏框架基于 `DINOv3` 架构，并以 `ConvNeXt-v2-Tiny` 作为主干网络。

本文的核心技术创新包括：通过物理动机增强显式模拟散斑噪声、距离相关衰减以及辐射度校准失误；引入希尔伯特-施密特独立性准则（HSIC）惩罚项，将学习到的密集补丁特征与物理观测参数显式解耦；以及跨所有四个网络阶段的分层特征融合策略，从而同时保留细粒度的沉积物细节与深层语义抽象。在 `S3Seg` 数据集上的评估表明，该模型在无需人工标注的情况下，仅使用 10% 的标注数据就达到了绝对峰值性能的 96%，最终取得了 71.4% 的平均交并比（mIoU）和 86.5% 的整体准确率，展现出极高的性能与数据效率。

---

# BenthicDINO: Physics-Informed Self-Distillation for View-Invariant Side-Scan Sonar Representations

**arXiv ID:** [arXiv:2608.23215](https://arxiv.org/abs/2608.23215) [cs.CV]  
**Submitted:** August 24, 2026  
**Authors:** Taqi Hamoda, Hayat Rajani, Nuno Gracias  

---

## 📋 Executive Summary

> Automated perception in **side-scan sonar (SSS)** imagery is traditionally hindered by physical acoustic artifacts, which obscure intrinsic seabed reflectivity by mixing it with transient viewing geometries. 

> To overcome the limitations of standard self-supervised learning (SSL) frameworks—which typically rely on natural-image augmentations and fail to account for acoustic degradation—the authors introduce **BenthicDINO**. This physics-informed self-distillation framework utilizes the `DINOv3` architecture with a `ConvNeXt-v2-Tiny` backbone. 

> **Key innovations and results include:**
> * **Physics-Motivated Augmentations:** Explicitly simulates speckle noise, range-dependent attenuation, and radiometric miscalibration.
> * **Hilbert-Schmidt Independence Criterion (HSIC) Penalty:** Decouples learned dense patch features from physical viewing parameters to enforce true view-invariance.
> * **Hierarchical Feature Fusion:** Preserves fine-grained sediment details alongside deep semantic abstractions across all four network stages.
> * **High Performance & Data Efficiency:** Without manual annotations, the model groups complex benthic topographies into stable semantic clusters. On the `S3Seg` dataset, it achieved **96% of its absolute peak performance using only 10% of annotated data**, reaching a **mean Intersection over Union (mIoU) of 71.4%** and an **overall accuracy of 86.5%**.

---

## 📄 Abstract

侧扫声呐（SSS）图像中的自动化感知严重受到物理声学伪影的阻碍，导致生成的表征不可避免地将本质的海底反射率与瞬变观测几何混合在一起。现有的自监督学习（SSL）框架依赖于专为自然图像设计的增强方法，无法应对声学退化并显式强制视角不变性。为了弥补这一空白，我们引入了一个基于 DINOv3 架构的物理融合自蒸馏框架，并采用 ConvNeXt-v2-Tiny 主干网络以最大化数据效率。所提出的方法通过两个主要机制强制视角不变性：一是物理动机驱动的数据增强，用于模拟散斑噪声、距离相关衰减以及辐射度校准失误；二是希尔伯特-施密特独立性准则（HSIC）惩罚项，用于显式解耦学习到的密集补丁特征与物理观测参数。此外，我们提出了一种跨网络所有四个阶段的密集分层特征融合策略，以在保留深层语义抽象的同时，保留细粒度的沉积物细节。广泛的评估表明，该框架能够在不依赖人工标注的情况下，将复杂的底栖地形原生聚类为稳定、无噪声的语义簇。在 S3Seg 数据集的监督下游任务中，融合后的表征展现出卓越的数据效率，仅使用 10% 的可用标注数据就达到了绝对峰值性能的 96%，最终实现了 71.4% 的平均交并比（mIoU）和 86.5% 的整体准确率。

> Automated perception in side-scan sonar (SSS) imagery is severely hindered by physical acoustic artifacts, resulting in representations that inextricably mix intrinsic seabed reflectivity with transient viewing geometries. Existing self-supervised learning (SSL) frameworks rely on augmentations designed for natural images, failing to account for acoustic degradation and explicitly enforce view-invariance. To address this gap, we introduce a physics-informed self-distillation framework built upon the DINOv3 architecture utilizing a ConvNeXt-v2-Tiny backbone to maximize data efficiency. The proposed methodology enforces view-invariance through two primary mechanisms: physically motivated augmentations that simulate speckle noise, range-dependent attenuation, and radiometric miscalibration; and a Hilbert-Schmidt Independence Criterion (HSIC) penalty that explicitly decouples learned dense patch features from physical viewing parameters. Furthermore, we propose a dense, hierarchical feature fusion strategy across all four network stages to preserve fine-grained sediment details alongside deep semantic abstractions. Extensive evaluation demonstrates that the framework natively groups complex benthic topographies into stable, noise-free semantic clusters without relying on manual annotations. During supervised downstream tasks on the S3Seg dataset, the fused representations exhibited exceptional data efficiency, achieving 96% of its absolute peak performance using only 10% of the available annotated data, ultimately reaching a mean Intersection over Union (mIoU) of 71.4% and an overall accuracy of 86.5%.

---

## 📊 Article Metadata & Resources

文章元数据与资源：

* **主学科：** 计算机视觉与模式识别 (`cs.CV`)
* **附加学科：** 人工智能 (`cs.AI`)、机器学习 (`cs.LG`)
* **引用格式：** `arXiv:2608.23215 [cs.CV]`
* **DOI：** [10.48550/arXiv.2608.23215](https://doi.org/10.48550/arXiv.2608.23215)
* **全文与访问链接：**
  * [查看 PDF](https://arxiv.org/pdf/2608.23215)
  * [HTML 版本（实验性）](https://arxiv.org/html/2608.23215v1)
  * [TeX 源码](https://arxiv.org/src/2608.23215)
* **外部文献计量工具：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23215), [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23215), [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23215)

> * **Primary Subject:** Computer Vision and Pattern Recognition (`cs.CV`)
> * **Additional Subjects:** Artificial Intelligence (`cs.AI`), Machine Learning (`cs.LG`)
> * **Cite as:** `arXiv:2608.23215 [cs.CV]`
> * **DOI:** [10.48550/arXiv.2608.23215](https://doi.org/10.48550/arXiv.2608.23215)
> * **Full-Text & Access Links:**
>   * [View PDF](https://arxiv.org/pdf/2608.23215)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.23215v1)
>   * [TeX Source](https://arxiv.org/src/2608.23215)
> * **External Bibliographic Tools:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23215), [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23215), [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23215)