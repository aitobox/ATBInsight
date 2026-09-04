---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 大模型量化
- PTQ
- Hadamard变换
- 硬件加速
- 低比特量化
title: HARP：用于极端大模型量化的哈 Hadamard 预处理自适应旋转处理器
---
### 文章背景与核心概要
在严格的内存和带宽限制下部署大语言模型（LLM）时，训练后量化（PTQ）至关重要。然而，现有的基于随机 Hadamard 变换（RHT）的方法采用的是固定混合方式，无法自适应特定的层、校准分布或量化器，导致极端低比特量化极易受到激活异常值和各向异性权重曲率的影响。

为了克服这一挑战，本文作者推出了 **HARP**（Hadamard-preconditioned Adaptive Rotation Processor，哈达玛预处理自适应旋转处理器）。HARP 是一种可学习的结构化双边正交处理器，它取代了固定的 Hadamard 混合，同时保持了精确的全精度等效性。仅需通过校准数据进行拟合，HARP 就能在不牺牲部署效率的前提下，将量化基底自适应调整到各个层和后端。

---

## 元数据与出版详情 (Metadata & Publication Details)

> * **arXiv ID:** [arXiv:2605.29843](https://arxiv.org/abs/2605.29843) [cs.LG]
> * **Subjects:** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`)
> * **Authors:** Artur Zagitov, Gleb Molodtsov, Aleksandr Beznosikov
> * **Submitted on:** 28 May 2026
> * **Last Revised:** 2 September 2026 (v2)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## 摘要 (Abstract)

训练后量化（PTQ）对于在内存和带宽受限的环境下部署大语言模型至关重要。然而，极端低比特量化对激活异常值和各向异性权重曲率仍然高度敏感。现有的基于不相干性的 PTQ 方法通过固定的随机 Hadamard 变换（RHT）来缓解这一问题，这虽然提高了量化鲁棒性，但无法针对特定的层、校准分布或量化器调整旋转基底。我们引入了 HARP（哈达玛预处理自适应旋转处理器），这是一种可学习的结构化双边正交处理器，它取代了固定的 Hadamard 混合，同时保持了精确的全精度等效性。HARP 将每次旋转表示为稀疏蝶形块正交阶段的乘积，通过混合基（Mixed-Radix）调度支持非 2 的幂次维度，并初始化为固定排列之下的 RHT 处理器。仅在校准数据上进行拟合，HARP 就能将量化基底自适应调整到各个层和后端。在从 1B 到 70B 的 Llama 模型 2–4 比特设置中，HARP 持续改善了困惑度（perplexity），并在 2 比特时取得了最显著的零样本（zero-shot）性能提升；一项针对 2 比特 Qwen3-8B 的实验表明，该方法同样能泛化到 Llama 家族之外的模型。HARP 还保持了出色的部署效率：在 Llama 2 7B 的 2 比特设置下，其吞吐量达到了 128 tok/s，保留了标准 RHT 吞吐量（142 tok/s）的 90%，并且运行速度比 FP16（61 tok/s）快约 $2.1\times$。

> Post-training quantization (PTQ) is essential for deploying LLMs under memory and bandwidth constraints. However, extreme low-bit quantization remains highly sensitive to activation outliers and anisotropic weight curvature. Existing incoherence-based PTQ methods mitigate this issue with fixed randomized Hadamard transforms (RHTs), which improve quantization robustness but cannot adapt the rotated basis to the layer, calibration distribution, or quantizer. We introduce HARP (Hadamard-preconditioned Adaptive Rotation Processor), a learnable structured two-sided orthogonal processor that replaces fixed Hadamard mixing while preserving exact full-precision equivalence. HARP represents each rotation as a product of sparse butterfly-like block-orthogonal stages, supports non-power-of-two dimensions through Mixed-Radix schedules, and initializes to the RHT processor up to a fixed permutation. Fitted only on calibration data, HARP adapts the quantization basis to each layer and backend. Across 2–4-bit settings on Llama models from 1B to 70B, HARP consistently improves perplexity and yields its clearest zero-shot gains at 2 bits; a 2-bit Qwen3-8B experiment shows the same transfer beyond the Llama family. HARP also preserves deployment efficiency: on Llama 2 7B at 2 bits, it reaches 128 tok/s, retaining 90% of RHT throughput (142 tok/s) and running approximately $2.1\times$ faster than FP16 (61 tok/s).

---

## 核心特性与性能亮点 (Key Features & Performance Highlights)

* **自适应旋转：** 用可学习的、结构化的双边正交处理器替代了刚性的随机 Hadamard 变换。
* **高灵活性：** 通过混合基（Mixed-Radix）调度支持非 2 的幂次维度。
* **广泛的兼容性：** 在 Llama 模型（1B 至 70B）的 2–4 比特设置中得到了验证，并通过 2 比特 Qwen3-8B 实验证明了其超越 Llama 家族的普适性。
* **高效能：** 保持了极高的部署速度——在 Llama 2 7B 的 2 比特设置下实现每秒 128 个 token 的吞吐量（达到标准 RHT 吞吐量的 90%，且比 FP16 快约 $2.1\times$）。

> * **Adaptive Rotation:** Replaces rigid, randomized Hadamard transforms with learnable, structured, two-sided orthogonal processors.
> * **Flexibility:** Supports non-power-of-two dimensions using Mixed-Radix schedules.
> * **Broad Compatibility:** Demonstrated across 2–4-bit settings on Llama models (1B to 70B) and validated beyond the Llama family with a 2-bit Qwen3-8B experiment.
> * **High Efficiency:** Retains high deployment speed—achieving 128 tokens/sec on Llama 2 7B at 2 bits (90% of standard RHT throughput and $\approx 2.1\times$ faster than FP16).