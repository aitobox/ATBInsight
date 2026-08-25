---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 事件相机
- 边缘计算
- 自编码器
- 计算机视觉
- 硬件部署
title: LiteEvent-AE：面向低延迟、受限能耗边缘设备的事件相机轻量级自编码器
---
### 文章背景与核心概要

事件相机（Event-based vision）通过处理稀疏且低延迟的视觉信号，为人工智能提供了一种高效且节能的新方法。然而，由于计算需求高，将传统的深度学习模型应用于异步且充满噪声的事件流时，在资源受限的边缘平台上仍然面临巨大挑战。

本文介绍了 **LiteEvent-AE**，这是一个紧凑且可配置的事件驱动自编码器，旨在高效压缩神经形态数据，同时保留下游任务所需的关键时空结构。通过将轻量级卷积编码与自适应事件阈值处理以及精简的分类器头部相结合，该框架在大幅降低计算成本的同时，实现了卓越的识别准确率。

---

# LiteEvent-AE: Lightweight Autoencoder for Event-Based Vision on Low-Latency Energy-Constrained Edge Devices

**arXiv:** [2608.21764](https://arxiv.org/abs/2608.21764) [cs.CV]  
**Submitted on:** August 22, 2026  
**Authors:** Riadul Islam, Joey Mule, Dhandeep Challagundla, Shahmir Rizvi, Sean Carson, Rachit Saini  

---

## 📌 Summary

事件视觉通过处理稀疏且低延迟的视觉信号，为人工智能提供了一种强大且节能的方法。然而，由于计算需求较高，在资源受限的边缘平台上，将常规深度学习模型应用于异步且带噪声的事件流仍然具有挑战性。

本文引入了 **LiteEvent-AE**，这是一个紧凑且可配置的事件驱动自编码器，旨在有效地压缩神经形态数据，同时为下游任务保留关键的时空结构。通过将轻量级卷积编码与自适应事件阈值处理以及最小分类器头部相结合，该框架在大幅降低计算成本的同时，实现了卓越的识别准确率。

> Event-based vision offers a powerful, energy-efficient approach to artificial intelligence by processing sparse and low-latency visual signals. However, applying conventional deep learning models to asynchronous and noisy event streams remains challenging on resource-constrained edge platforms due to high computational demands. 
>
> This paper introduces **LiteEvent-AE**, a compact and configurable event-driven autoencoder designed to compress neuromorphic data effectively while preserving critical spatiotemporal structures for downstream tasks. By combining lightweight convolutional encoding with adaptive event thresholding and a minimal classifier head, the framework achieves exceptional recognition accuracy with drastically reduced computational costs.

---

## 📋 Abstract

事件视觉已成为面向节能型人工智能（AI）的一个极具前景的范例，它提供稀疏、低延迟的视觉信号，可减少冗余数据处理并支持可持续的边缘计算。然而，事件流异步且易受噪声干扰的特性给传统深度学习模型带来了挑战，这些模型通常计算密集，不适合低功耗嵌入式平台。

本工作提出了一种紧凑且可配置的事件驱动自编码器，能够高效压缩神经形态数据，同时保留用于下游推理的必不可少时空结构。该架构将轻量级卷积编码与自适应事件阈值下的鲁棒性能以及极简分类器头部集成在一起，在不降低识别保真度的前提下显著降低了计算成本。

在 **Smart Event Face Dataset (SEFD)** 和 **Event-Based Crossing Dataset (EBCD)** 上的广泛评估表明，与 YOLOv9 相比，所提出的框架实现了具有竞争力或更高的准确率，同时参数量减少了多达 **35.6$\times$**。

> Event-based vision has emerged as a promising paradigm for energy-aware artificial intelligence (AI), offering sparse, low-latency visual signals that reduce redundant data processing and support sustainable edge computing. However, the asynchronous and noise-prone nature of event streams creates challenges for conventional deep learning models, which are often too computationally intensive for low-power embedded platforms. 
>
> This work presents a compact and configurable event-driven autoencoder that efficiently compresses neuromorphic data while preserving essential spatiotemporal structure for downstream inference. The architecture integrates lightweight convolutional encoding with robust performance under adaptive event thresholding and a minimal classifier head, enabling substantial reductions in computational cost without degrading recognition fidelity. 
>
> Extensive evaluations on the **Smart Event Face Dataset (SEFD)** and **Event-Based Crossing Dataset (EBCD)** show that the proposed framework achieves competitive or superior accuracy compared to YOLOv9 while requiring up to **35.6$\times$ fewer parameters**. 

---

## ⚡ Hardware Deployment & Performance

为了评估真实世界的环境可持续性，该模型被部署在资源受限的硬件平台上：
* **NVIDIA Jetson Nano：** 提供 **44.8 FPS** 的实时吞吐量。
* **Raspberry Pi 4B (CPU)：** 50% 自编码器分类器在所评估的推理工作负载下消耗 **16.19 J** 的能量——在相同的测试条件下，这比 YOLOv9 的能耗降低了大约 **726.3$\times$**。

这些结果突显了紧凑型事件驱动模型在推动面向自主、移动和嵌入式环境中高速感知的环保、低功耗人工智能系统方面的潜力。

> To assess real-world sustainability, the model was deployed on resource-constrained hardware platforms:
> * **NVIDIA Jetson Nano:** Delivers a real-time throughput of **44.8 FPS**.
> * **Raspberry Pi 4B (CPU):** The 50% autoencoder classifier consumes **16.19 J** for the evaluated inference workload—representing approximately **726.3$\times$ lower energy consumption** than YOLOv9 under the same testing conditions.
>
> These results highlight the potential of compact event-driven models to advance environmentally conscious, low-power AI systems for high-speed perception in autonomous, mobile, and embedded environments.

---

## 🗂️ Metadata & Links

* **主要主题：** 计算机视觉与模式识别 (`cs.CV`)
* **次要主题：** 人工智能 (`cs.AI`)；图像与视频处理 (`eess.IV`)
* **DOI：** [10.48550/arXiv.2608.21764](https://doi.org/10.48550/arXiv.2608.21764)
* **全文访问：** 
  * [查看 PDF](https://arxiv.org/pdf/2608.21764)
  * [HTML（实验性）](https://arxiv.org/html/2608.21764v1)
  * [TeX 源码](https://arxiv.org/src/2608.21764)
* **许可证：** [知识共享署名 4.0 国际](http://creativecommons.org/licenses/by/4.0/) [![license icon](./images/345c7ad61f1b.png)](http://creativecommons.org/licenses/by/4.0/)

> * **Primary Subject:** Computer Vision and Pattern Recognition (`cs.CV`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`); Image and Video Processing (`eess.IV`)
> * **DOI:** [10.48550/arXiv.2608.21764](https://doi.org/10.48550/arXiv.2608.21764)
> * **Full-Text Access:** 
>   * [View PDF](https://arxiv.org/pdf/2608.21764)
>   * [HTML (Experimental)](https://arxiv.org/html/2608.21764v1)
>   * [TeX Source](https://arxiv.org/src/2608.21764)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) [![license icon](./images/345c7ad61f1b.png)](http://creativecommons.org/licenses/by/4.0/)