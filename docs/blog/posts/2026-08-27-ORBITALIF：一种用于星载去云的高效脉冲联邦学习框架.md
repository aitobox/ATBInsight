---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- 脉冲神经网络
- 联邦学习
- 卫星遥感
- 图像去云
- 边缘计算
title: ORBITALIF：一种用于星载去云的高效脉冲联邦学习框架
---
### 文章背景与核心概要
在低轨（LEO）卫星对地观测中，云层遮挡一直是影响数据质量和实时应用的关键痛点。传统的处理方式依赖于将大量原始遥感数据下传至地面站进行去云处理，这不仅带来了巨大的通信延迟，还对星地链路带宽造成了严峻考验。

为此，本文介绍了 **ORBITALIF** 框架，它创新性地将去云处理流程从地面直接迁移至卫星星载端。该系统利用仅有 230 万参数的紧凑型脉冲神经网络（SNN），直接在神经形态硬件上执行训练与推理。结合去中心化的联邦学习策略，卫星能够通过星间链路共享模型权重，在实现高质量去云的同时，较传统人工神经网络（ANN）降低了高达 98.6% 的能耗。

---

# ORBITALIF：一种用于星载去云的高效脉冲联邦学习框架 (ORBITALIF: An Efficient Spiking Federated Learning Framework for Onboard Cloud Removal)

**作者：** Bohan Zhang, Chenyu Xu, Yijie Mao, Yuanming Shi  
**发表时间：** 2026年8月25日  
**会议期刊：** IEEE GLOBECOM 2026  
**arXiv ID：** [2608.24073](https://arxiv.org/abs/2608.24073)

---

## 摘要 (Summary)
**ORBITALIF**（Orbital Attention Leaky Integrate-and-Fire，轨道注意力泄漏积分发放）是一种新颖的框架，旨在解决低轨（LEO）卫星中受云层遮挡的地球观测数据所面临的挑战。通过将去云处理从地面站转移到卫星星载端，该框架消除了传统以数据下行为主的管线所带来的延迟和带宽限制。

该系统采用了一个紧凑的 2.30M 参数的脉冲神经网络（SNN），直接在神经形态硬件上进行训练和推理。通过去中心化的联邦学习策略，卫星通过星间链路共享模型权重，在实现高质量去云的同时，与传统人工神经网络（ANN）相比，能耗降低了 98.6%。

> **ORBITALIF** (Orbital Attention Leaky Integrate-and-Fire) is a novel framework designed to address the challenges of cloud-obscured Earth observation data from Low-Earth-Orbit (LEO) satellites. By moving cloud-removal processing from ground stations to onboard the satellite, the framework eliminates the latency and bandwidth constraints of traditional downlink-heavy pipelines. 
> 
> The system utilizes a compact 2.30M-parameter Spiking Neural Network (SNN) that performs both training and inference directly on neuromorphic hardware. Through a decentralized federated learning strategy, satellites share model weights via inter-satellite links, achieving high-quality cloud removal with a 98.6% reduction in energy consumption compared to traditional Artificial Neural Networks (ANNs).

---

## 核心技术组件 (Key Technical Components)

### 1. 脉冲神经网络（SNN）主干网络
该框架的核心是一个轻量级的 SNN 架构，它在硬件部署上具有天然的更高能效，经过优化以适应卫星系统受限的功耗环境。

> ### 1. Spiking Neural Network (SNN) Backbone
> The core of the framework is a lightweight SNN architecture, which is inherently more energy-efficient for hardware deployment. It is optimized for the constrained power environments of satellite systems.

### 2. 高级模块
*   **自适应门控融合模块（AGFM）：** 增强了模型高效整合多模态或多时相数据的能力。
*   **光谱-空间混合注意力模块（SHAM）：** 允许模型聚焦于光谱和空间维度上的关键特征，确保在云层覆盖的情况下仍能进行高保真图像重建。

> ### 2. Advanced Modules
> *   **Adaptive Gated Fusion Module (AGFM):** Enhances the model's ability to integrate multi-modal or multi-temporal data efficiently.
> *   **Spectral-Spatial Hybrid Attention Module (SHAM):** Allows the model to focus on critical features across both spectral and spatial dimensions, ensuring high-fidelity image reconstruction despite cloud coverage.

### 3. 联邦学习策略
为了在整个卫星星座中保持模型性能，ORBITALIF 采用了一种去中心化的联邦学习方法。卫星通过星间链路共享权重，协同改进去云模型，从而在无需持续与地面站接触的情况下实现持续学习。

> ### 3. Federated Learning Strategy
> To maintain model performance across a constellation, ORBITALIF employs a decentralized federated learning approach. Satellites collaboratively improve the cloud-removal model by sharing weights through inter-satellite links, ensuring continuous learning without requiring constant ground-station contact.

---

## 性能亮点 (Performance Highlights)
*   **能源效率：** 在神经形态硬件上，**每次推理仅消耗 0.287 mJ** 的能量。
*   **对比优势：** 与同等的人工神经网络（ANN）实现相比，实现了 **72.3倍（98.6%）的能耗降低**。
*   **图像质量：** 提供适用于实时灾害监测和环境监视的具备竞争力的去云性能。

> **Performance Highlights**
> *   **Energy Efficiency:** Consumes only **0.287 mJ per inference** on neuromorphic hardware.
> *   **Comparative Advantage:** Achieves a **72.3x (98.6%) energy reduction** compared to equivalent Artificial Neural Network (ANN) implementations.
> *   **Quality:** Delivers competitive cloud-removal performance suitable for real-time disaster monitoring and environmental surveillance.

---

## 访问与资源 (Access & Resources)
*   **[查看 PDF](https://arxiv.org/pdf/2608.24073)**
*   **[HTML 版本（实验性）](https://arxiv.org/html/2608.24073v1)**
*   **[TeX 源码](https://arxiv.org/src/2608.24073)**
*   **DOI：** [10.48550/arXiv.2608.24073](https://doi.org/10.48550/arXiv.2608.24073)

> **Access & Resources**
> *   **[View PDF](https://arxiv.org/pdf/2608.24073)**
> *   **[HTML Version (Experimental)](https://arxiv.org/html/2608.24073v1)**
> *   **[TeX Source](https://arxiv.org/src/2608.24073)**
> *   **DOI:** [10.48550/arXiv.2608.24073](https://doi.org/10.48550/arXiv.2608.24073)