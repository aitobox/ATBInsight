---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 音频压缩
- 量化技术
- CPU优化
- 信号处理
- AudioTQ
title: AudioTQ：一种基于随机哈达玛变换与Lloyd-Max量化的6位CPU音频编解码器
---
### 文章背景与核心概要

传统的有损音频压缩算法（如MP3、AAC和Opus）主要依赖于心理声学模型和频域表示，通过剔除人类听觉系统无法感知的冗余信息来实现压缩。然而，这些方法往往计算复杂度高且具有较强的领域依赖性。

本文提出的 **AudioTQ** 是一种创新的、与数据无关（data-oblivious）的时域有损音频编解码器。该技术借鉴了大型语言模型（LLM）的权重量化方法（特别是 TurboQuant 框架），利用正交随机快速沃尔什-哈达玛变换（FWHT）将不稳定的时域振幅归一化为可预测的标准正态分布。

AudioTQ 的核心优势在于其高效的量化策略与 CPU 友好性。它采用离线训练的 6 位 Lloyd-Max 量化器，并辅以 1 位量化联合最小二乘法（QJL）残差校正层。通过将 7 位虚拟索引打包进 8 位容器，该算法能够实现单线程实时执行，无需专用硬件加速。在处理 24 位录音室音轨时，它能实现高达 74.4% 的物理尺寸缩减，同时保持约 30 dB 的信噪比（SQNR）。

---

## 执行摘要

> Traditional lossy audio compression algorithms (such as MP3, AAC, and Opus) rely heavily on psychoacoustic modeling and frequency-domain representations to discard perceptually irrelevant information. While effective, these methods are computationally demanding and highly domain-specific. 
>
> This paper introduces **AudioTQ**, a novel, data-oblivious lossy audio codec that operates directly in the time domain. Drawing inspiration from Large Language Model (LLM) weight quantization techniques (specifically the *TurboQuant* framework), AudioTQ normalizes volatile time-domain amplitudes into a predictable standard normal distribution using an orthonormal, randomized Fast Walsh-Hadamard Transform (FWHT) rotation. 

### 关键创新与性能：
> ### Key Innovations & Performance:
* **量化策略：** 利用坐标标量量化，结合离线训练的均方误差（MSE）最优 6 位 Lloyd-Max 量化器，并增加 1 位量化联合最小二乘法（QJL）残差校正层。
> * **Quantization Strategy:** Utilizes coordinate-wise scalar quantization via an offline-trained, Mean-Squared Error (MSE)-optimal 6-bit Lloyd-Max quantizer, augmented by a 1-bit Quantized Joint Least-Squares (QJL) residual correction layer.
* **CPU 优化：** 将生成的 7 位虚拟索引打包进原生 8 位容器中，以对齐标准 CPU 寄存器边界，从而在无需专用硬件加速的情况下实现实时单线程执行。
> * **CPU Optimization:** Packs resulting 7-bit virtual indices into native 8-bit containers to align with standard CPU register boundaries, enabling real-time, single-threaded execution without dedicated hardware accelerators.
* **基准测试：** 在重构 24 位录音室音轨时，实现了高达 **74.4% 的物理尺寸缩减**，同时保持了约 **~30 dB** 的信号量化噪声比（SQNR）。
> * **Benchmarks:** Achieves up to **74.4% physical size reduction** alongside a Signal-to-Quantization-Noise Ratio (SQNR) of approximately **~30 dB** when reconstructing 24-bit studio stems.

---

## 摘要与方法论概述

> **Abstract:**  
> Lossy audio compression algorithms traditionally rely on psychoacoustic modeling and frequency-domain representations (e.g., MP3, AAC, and Opus) to discard information that is imperceptible to the human auditory system. While highly effective, these approaches are computationally complex and domain-specific. In this paper, we present the design and mathematical formulation of AudioTQ, a data-oblivious lossy audio codec that operates directly in the time domain. Inspired by Large Language Model (LLM) weight quantization techniques (specifically the TurboQuant framework), AudioTQ uniformizes volatile time-domain amplitudes into a predictable standard normal distribution using an orthonormal, randomized Fast Walsh-Hadamard Transform (FWHT) rotation. This enables coordinate-wise scalar quantization using an offline-trained, MSE-optimal 6-bit Lloyd-Max quantizer, augmented by a 1-bit Quantized Joint Least-Squares (QJL) residual correction layer. The resulting 7-bit virtual indices are packed into native 8-bit containers, aligning with standard CPU register boundaries to ensure real-time single-threaded execution without hardware parallel accelerators. We detail the bitwise reconstruction of 24-bit studio stems, analyze the butterfly network of the FWHT, derive the mathematical failure modes under sparse inputs, and present benchmarks showing up to 74.4% physical size reduction alongside a Signal-to-Quantization-Noise Ratio (SQNR) of ~30 dB.

---

## 附加元数据

* **主要学科：** 声音 (`cs.SD`)
* **次要学科：** 人工智能 (`cs.AI`)，密码学与安全 (`cs.CR`)
* **MSC 分类：** 94A12, 94A29
* **ACM 分类：** E.4; H.5.5
* **数字对象唯一标识符 (DOI)：** [10.48550/arXiv.2608.15369](https://doi.org/10.48550/arXiv.2608.15369)

> *Note: This document preserves all reference links, metadata classifications, and structural components from the original arXiv submission.*