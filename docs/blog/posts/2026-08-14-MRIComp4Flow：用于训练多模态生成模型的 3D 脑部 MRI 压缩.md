---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- 3D MRI
- 生成模型
- 图像压缩
- 医疗影像
- 深度学习
title: MRIComp4Flow：用于训练多模态生成模型的 3D 脑部 MRI 压缩
---
### 文章背景与核心概要
大规模的多模态 3D MRI 数据集带来了沉重的存储和 I/O 瓶颈，使得在标准基础设施上训练生成模型变得极其困难。尽管有损压缩在分割等判别式任务中表现良好，但它对生成模型的影响——这类模型必须捕获完整的数据分布而不仅仅是决策边界——在很大程度上仍未被探索。

本文研究了标准图像编解码器是否能够有效地压缩语义丰富的脑肿瘤 MRI 数据，同时保持训练 3D 生成模型所需的高保真度。通过使用 JPEG2000 或近无损 JPEG-LS 流水线压缩 3D 体素，并在 BraTS 序列（T1n、T1c、T2、T2f）上训练小波流匹配（Wavelet Flow Matching）模型，作者证明了 **20:1 的 JPEG2000 压缩** 可以产生与未压缩数据在统计学上等效的合成质量（$\Delta\text{PSNR} < 1\text{ dB}$, $\Delta\text{SSIM} < 0.02$）。这为实现可扩展的 3D MRI 生成建模提供了一条实用的途径。

---

## MRIComp4Flow: Compression of 3D Brain MRI for Training Multi-Modal Generative Models

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/>

## Summary
> Large-scale multi-modal 3D MRI datasets create severe storage and I/O bottlenecks that make training generative models on standard infrastructure difficult. While lossy compression is known to work well for discriminative tasks like segmentation, its impact on generative models—which must capture the entire data distribution rather than just a decision boundary—remains largely unexplored. 
> 
> This paper investigates whether standard image codecs can effectively compress semantically rich brain tumor MRI data while preserving the high fidelity required for training 3D generative models. By compressing 3D volumes using JPEG2000 or near-lossless JPEG-LS pipelines and training a Wavelet Flow Matching model on BraTS sequences (T1n, T1c, T2, T2f), the authors demonstrate that **20:1 JPEG2000 compression** yields synthesis quality statistically equivalent to uncompressed data ($\Delta\text{PSNR} < 1\text{ dB}$, $\Delta\text{SSIM} < 0.02$). This offers a practical pathway toward scalable 3D MRI generative modeling.

---

## 元数据与文档信息

| 字段 | 详情 |
| :--- | :--- |
| **arXiv ID** | [`arXiv:2608.10291`](https://arxiv.org/abs/2608.10291) [cs.CV] |
| **研究主题** | 计算机视觉与模式识别 (`cs.CV`); 人工智能 (`cs.AI`); 机器学习 (`cs.LG`) |
| **提交日期** | 2026年8月10日 |
| **作者** | Lisa K. Fischer, Mykhailo Riabets, Daniel Rueckert, Benedikt Wiestler, Anke Meyer-Baese, Sandeep Nagar |
| **收录会议** | 已被 **MICCAI 2026 SASHIMI 研讨会** 接受 |
| **代码仓库** | [GitHub - lisafis/MRIComp4Flow](https://github.com/lisafis/MRIComp4Flow) |

> ## Metadata & Document Information
> 
> | Field | Details |
> | :--- | :--- |
> | **arXiv ID** | [`arXiv:2608.10291`](https://arxiv.org/abs/2608.10291) [cs.CV] |
> | **Subjects** | Computer Vision and Pattern Recognition (`cs.CV`); Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`) |
> | **Submission Date** | August 10, 2026 |
> | **Authors** | Lisa K. Fischer, Mykhailo Riabets, Daniel Rueckert, Benedikt Wiestler, Anke Meyer-Baese, Sandeep Nagar |
> | **Conference** | Accepted at **MICCAI 2026 SASHIMI workshop** |
> | **Code Repository** | [GitHub - lisafis/MRIComp4Flow](https://github.com/lisafis/MRIComp4Flow) |

---

## 摘要

大规模的多模态 MRI 数据集带来了巨大的存储和 I/O 成本，限制了在商用基础设施上训练 3D 生成模型。尽管已知有损压缩可以保持判别式分割网络的准确性，但它对生成模型的影响（生成模型必须学习完整的数据分布而不是决策边界）尚未得到探索。

我们研究了标准图像编解码器是否能够有效压缩语义丰富的脑肿瘤 MRI，同时保持训练和部署 3D MRI 生成模型所需的保真度。每个 3D 体素都使用 JPEG2000 或近无损 JPEG-LS 流水线进行压缩。接下来，在压缩数据上训练一个以 BraTS 图像序列（T1n、T1c、T2、T2f）为条件的小波流匹配模型，并在验证集上评估所得模型。

在 20:1 的压缩比下，合成质量在预先指定的误差范围内与在未压缩数据上训练的模型在统计学上等效（$\Delta\text{PSNR} < 1\text{ dB}$，$\Delta\text{SSIM} < 0.02$；配对 TOST $p=\text{val}$）：各模态的平均 PSNR 分别为 $27.3\text{ dB}$ 对比 $27.0\text{ dB}$，平均 SSIM 分别为 $0.95$ 对比 $0.96$。我们的结果表明，JPEG2000 压缩是在不降低合成质量的前提下实现可扩展 3D MRI 生成建模的实用步骤。

> ## Abstract
> Large-scale multi-modal MRI datasets impose substantial storage and I/O costs, limiting the training of 3D generative models on commodity infrastructure. While lossy compression is known to preserve accuracy for discriminative segmentation networks, its effect on generative models, which must learn the full data distribution rather than a decision boundary, is unexplored. 
> 
> We study whether standard image codecs can effectively compress semantically rich brain tumor MRI while preserving the fidelity required to train and deploy a 3D MRI generative model. Each 3D volume is compressed with JPEG2000 or a near-lossless JPEG-LS pipeline. Next, a Wavelet Flow Matching model, conditioned on BraTS image sequences (T1n, T1c, T2, T2f), is trained on compressed data, and the resulting models are evaluated on the validation set. 
> 
> At a 20:1 compression ratio, synthesis quality is statistically equivalent to a model trained on uncompressed data within a pre-specified margin ($\Delta\text{PSNR} < 1\text{ dB}$, $\Delta\text{SSIM} < 0.02$; paired TOST $p=\text{val}$): mean PSNR is $27.3\text{ dB}$ vs. $27.0\text{ dB}$ and mean SSIM is $0.95$ vs. $0.96$ across modalities. Our results indicate that JPEG2000 compression is a practical step toward scalable 3D MRI generative modeling without degrading synthesis quality.