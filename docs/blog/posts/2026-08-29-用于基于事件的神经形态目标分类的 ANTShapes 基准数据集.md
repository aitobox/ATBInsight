---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 神经形态计算
- 脉冲神经网络
- 事件相机
- 计算机视觉
- 基准数据集
title: 用于基于事件的神经形态目标分类的 ANTShapes 基准数据集
---
### 文章背景与核心概要
基于事件的计算机视觉为传统的基于帧的相机提供了一种高能效的替代方案，使其非常适合边缘计算和隐蔽传感。然而，高质量、内容丰富的视觉数据集的严重匮乏，极大地阻碍了该领域的发展进度。

本文介绍了四个通过 **ANTShapes 模拟工具** 生成的新颖目标分类数据集，其难度各不相同。作者利用卷积脉冲神经网络（SNN），将这些数据集与标准的脉冲数据集（如 N-MNIST、CIFAR10-DVS、DVSGesture 和 POKER-DVS）进行了基准测试。研究结果验证了 ANTShapes 模拟工具的有效性和可靠性，同时为神经形态计算社群提供了宝贵的全新基准测试资源。

---

## 📋 Executive Summary

> Event-based computer vision offers an energy-efficient alternative to traditional frame-based cameras, making it highly suitable for edge computing and covert sensing. However, progress in this field has been significantly bottlenecked by a shortage of high-quality, richly detailed vision datasets. 
> 
> This paper introduces four novel object classification datasets of varying difficulties generated via the **ANTShapes simulation tool**. The authors benchmark these datasets against standard spiking datasets (such as N-MNIST, CIFAR10-DVS, DVSGesture, and POKER-DVS) using a convolutional Spiking Neural Network (SNN). The results validate the efficacy and reliability of the ANTShapes simulation tool while providing valuable new benchmarking resources for the neuromorphic computing community.

---

## 📌 Article Overview

* **Title:** ANTShapes Benchmarking Datasets for Event-Based Neuromorphic Object Classification
* **Authors:** M. Middleton, H. Kayan, B. Sen Bhattacharya, T. Ali, E. Baikas, M. Vousden, C. Perera, O. Rhodes, E. Gheorghiu, M. A. Trefzer
* **Submitted on:** August 27, 2026
* **Primary Subject:** Neural and Evolutionary Computing (`cs.NE`)
* **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Computer Vision and Pattern Recognition (`cs.CV`)
* **Identifier:** arXiv:2608.27150
* **DOI:** [10.48550/arXiv.2608.27150](https://doi.org/10.48550/arXiv.2608.27150)
* **License:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-nc-sa/4.0/) ![license icon](./images/079cd8198ba3.png)

---

## 🔍 Abstract & Motivation

传统的计算机视觉流水线严重依赖同步的、基于帧的相机以及集中式的云端基础设施。尽管这种传统方法得到了广泛应用，但它存在几个致命的缺陷：
1. **高功耗与大尺寸占用：** 无法部署在极端边缘环境或隐蔽场景中。
2. **安全风险：** 将敏感数据传输到云端会使系统暴露出隐私和安全漏洞。
3. **延迟与连接性：** 持续的数据流传输需要不间断的高带宽网络连接，并会带来处理延迟。

> Traditional computer vision pipelines rely heavily on synchronous, frame-based cameras and centralized cloud infrastructure. While widespread, this conventional approach suffers from several critical drawbacks:
> 1. **High Power & Size Footprint:** Prohibits deployment in extreme edge environments or covert scenarios.
> 2. **Security Risks:** Transmitting sensitive data to the cloud exposes systems to privacy and security vulnerabilities.
> 3. **Latency & Connectivity:** Continuous data streaming requires uninterrupted, high-bandwidth network connectivity and introduces processing latency.

为了解决这些局限性，研究人员正转向在神经形态硬件上运行的**脉冲神经网络（SNN）**。尽管 SNN 前景广阔，但由于缺乏全面的基准测试数据集，基于事件的视觉研究在历史上一直举步维艰。

为了填补这一空白，本研究利用 **ANTShapes 模拟工具** 生成并标注了四个跨越不同复杂度级别的独特基于事件的视觉数据集。

> To address these limitations, researchers are turning toward **Spiking Neural Networks (SNNs)** executed on neuromorphic hardware. Despite the promise of SNNs, event-based vision research has historically struggled due to a scarcity of comprehensive benchmarking datasets. 
> 
> To bridge this gap, this study utilizes the **ANTShapes simulation tool** to generate and label four distinct event-based vision datasets spanning various complexity levels. 

---

## 🔬 Methodology & Benchmarking

* **数据集生成：** 使用 ANTShapes 模拟工具以编程方式生成了四个难度递增的新数据集。
* **网络架构：** 利用专用的卷积脉冲神经网络（SNN）执行目标分类。
* **对比分析：** 将新数据集与现有的成熟基于事件的视觉数据集进行了严格的基准测试，这些数据集包括：
  * N-MNIST
  * CIFAR10-DVS
  * DVSGesture
  * POKER-DVS

> * **Dataset Generation:** Four new datasets of increasing difficulty levels were produced programmatically using the ANTShapes simulation tool.
> * **Architecture:** Object classification is performed utilizing a specialized convolutional Spiking Neural Network (SNN).
> * **Comparative Analysis:** The new datasets are rigorously benchmarked against established event-based vision datasets, including:
>   * N-MNIST
>   * CIFAR10-DVS
>   * DVSGesture
>   * POKER-DVS

---

## 🔗 Quick Links & Resources

* **Full-Text Access:**
  * [View PDF](https://arxiv.org/pdf/2608.27150)
  * [Experimental HTML Version](https://arxiv.org/html/2608.27150v1)
  * [TeX Source Code](https://arxiv.org/src/2608.27150)
* **External Bibliographic Tools:**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.27150)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.27150)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.27150)