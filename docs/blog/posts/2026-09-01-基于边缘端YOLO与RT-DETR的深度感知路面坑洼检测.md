---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- 计算机视觉
- 目标检测
- 边缘计算
- 深度感知
- RGB-D融合
title: 基于边缘端YOLO与RT-DETR的深度感知路面坑洼检测
---
### 文章背景与核心概要
城市基础设施管理中，路面坑洼的自动检测与严重程度评估长期以来一直是一个重要挑战。传统的二维RGB图像方法无法测量坑洼的物理深度。为了弥补这一技术空白，本文评估了五种架构（**YOLOv8n**、**YOLOv8nSeg**、**YOLOv9t**、**RTDETRL**和**RTDETRX**）在RGB-D传感器融合中的应用，并利用定制的离线增强流水线来模拟恶劣的路面监测环境。

研究的核心技术贡献包括：通过RANSAC地面平面正射校正来纠正相机倾斜，并将值为零的传感器像素转换为 `NaN` 以确保计算准确性。实验表明，**YOLOv8nSeg** 取得了最高的准确率（`mAP@50` 为 `0.9556`），并利用像素级精确的 Dseg 算法获得了最准确的深度估计（`2.96 cm`）；**YOLOv8n** 实现了最快的推理速度（`3.6 ms`）；而 **RTDETRX** 则获得了最高的检测置信度（`92.70%`）。此外，研究还发现边界框模型由于包含路面像素，会系统性地高估坑洼深度，证明了结构性偏差的存在。

---

## Metadata

* **arXiv Identifier:** [arXiv:2608.27633](https://arxiv.org/abs/2608.27633) [cs.CV]
* **Authors:** Md Monjurul Ahsan Prodhan, Md Nour Hossain
* **Submitted Date:** 27 August 2026
* **Primary Subject:** Computer Vision and Pattern Recognition (`cs.CV`)
* **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Machine Learning (`cs.LG`)
* **Conference Presentation:** IEEE 9th International Conference on Multimedia Information Processing and Retrieval (10 August 2026)
* **DOI:** [10.48550/arXiv.2608.27633](https://doi.org/10.48550/arXiv.2608.27633)

---

## Abstract

Pothole detection and its severity measurement is still an important challenges in urban infrastructure management, where late maintenance directly contributes to vehicle damage, road accidents, and escalating repair costs. Existing automated approaches depend on 2D RGB images and cannot measure physical depth of potholes. In this paper, we present a depth-aware pothole detection framework and then compare five architectures: **YOLOv8n**, **YOLOv8nSeg**, **YOLOv9t**, **RTDETRL**, and **RTDETRX** for RGB-D sensor fusion-based detection and automated depth measurement. 

> 坑洼检测及其严重程度测量仍然是城市基础设施管理中的一个重要挑战，不及时维护会直接导致车辆受损、道路交通事故以及维修成本的不断攀升。现有的自动化方法依赖于二维RGB图像，无法测量坑洼的物理深度。在本文中，我们提出了一种具备深度感知能力的坑洼检测框架，并对比了五种架构：**YOLOv8n**、**YOLOv8nSeg**、**YOLOv9t**、**RTDETRL** 和 **RTDETRX**，用于基于RGB-D传感器融合的检测和自动化深度测量。

A custom offline augmentation pipeline is used here to simulate adverse road monitoring conditions. All models are trained on the PothRGBD dataset with an 80% training and 20% validation split and evaluated using Precision, Recall, `mAP@50`, and `mAP@50_95`. Before measuring the depth data, all depth maps are corrected for camera tilt using RANSAC ground-plane orthorectification and all zero-valued sensor pixels are cast to `NaN` before any statistic is computed. 

> 这里使用了一个定制的离线增强流水线来模拟恶劣的路面监测条件。所有模型均在PothRGBD数据集上进行训练（按80%训练集和20%验证集划分），并使用精确度（Precision）、召回率（Recall）、`mAP@50` 和 `mAP@50_95` 进行评估。在测量深度数据之前，所有深度图都通过RANSAC地面平面正射校正进行了相机倾斜校正，并且在计算任何统计数据之前，所有值为零的传感器像素都被转换为 `NaN`。

**YOLOv8nSeg** achieves the highest `mAP@50` of `0.9556` and `mAP@50_95` of `0.6758` with the most accurate depth estimate of `2.96 cm` with the pixel-precise Dseg algorithm. **YOLOv8n** achieves the fastest inference at `3.6 ms`. **RTDETRX** achieves the highest detection confidence at `92.70%`. An important finding is that even after full RANSAC orthorectification, bounding box models overestimate pothole depth by `0.16` to `0.21 cm` compared to pixel precise segmentation masks. This confirms that the pavement inclusion bias is structural rather than a calibration artifact.

> **YOLOv8nSeg** 实现了最高的 `m`AP@50（`0.9556`）和 `mAP@50_95`（`0.6758`），并通过像素级精确的 Dseg 算法获得了 `2.96 cm` 的最准确深度估计。**YOLOv8n** 实现了最快的推理速度（`3.6 ms`）。**RTDETRX** 获得了最高的检测置信度（`92.70%`）。一个重要的发现是，即使在进行完整的RANSAC正射校正后，与像素级精确的分割掩膜相比，边界框模型仍然将坑洼深度高估了 `0.16` 至 `0.21 cm`。这证实了路面包含偏差是结构性的，而不是由校准伪影引起的。

---

## Full-Text & Access Links

* **PDF Version:** [View PDF](https://arxiv.org/pdf/2608.27633)
* **Experimental HTML:** [arXiv HTML](https://arxiv.org/html/2608.27633v1)
* **TeX Source:** [Download Source](https://arxiv.org/src/2608.27633)
* **License:** [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/) <img alt="license icon" role="presentation" src="./images/fb423b2203a9.png">

> * **PDF 版本：** [查看 PDF](https://arxiv.org/pdf/2608.27633)
> * **实验性 HTML：** [arXiv HTML](https://arxiv.org/html/2608.27633v1)
> * **TeX 源码：** [下载源码](https://arxiv.org/src/2608.27633)
> * **许可协议：** [知识共享 署名-非商业性使用-禁止演绎 4.0 国际](http://creativecommons.org/licenses/by-nc-nd/4.0/) <img alt="license icon" role="presentation" src="./images/fb423b2203a9.png">