---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 大语言模型
- 模型量化
- NVFP4
- Gated DeltaNet
- 混合架构
title: 为什么门控DeltaNet能在4位量化下存活：混合27B大模型循环部分的NVFP4 W4A4技术解析
---
### 文章背景与核心概要

混合大语言模型（LLM）将传统的Softmax注意力机制与线性注意力层（如**门控DeltaNet (GDN)**）结合，通过循环状态在固定大小内管理上下文。此前，社区针对Qwen3.8-27B等模型（包含48个GDN层和16个注意力层）的量化通常会避免将GDN模块压缩到4位——特别是其衰减和写入强度门控——因为担心循环误差会在长上下文中累积放大。

本文打破了这一固有假设，推出了 **Minima**，这是一种将 NVFP4 W4A4 配置应用到包括 GDN 在内的全部 496 个线性层的量化方案。尽管经历了极端压缩，Minima 在一系列基准测试中的性能依然在统计噪声范围内与 BF16 持平，同时拥有显著更小的模型体积（17.5 GiB）以及 14% 至 19% 的预填充（Prefill）速度提升。

---

## 📌 摘要 (Summary)

> Hybrid Large Language Models (LLMs) combine traditional softmax attention with linear-attention layers like **Gated DeltaNet (GDN)**, where a recurrent state manages context within a fixed size. Previously, community quantizations of models like Qwen3.8-27B (which features 48 GDN layers and 16 attention layers) avoided quantizing the GDN block down to 4 bits—particularly its decay and write-strength gates—due to fears that recurrence errors would compound over long contexts. 
> 
> This paper challenges that assumption by introducing **Minima**, an NVFP4 W4A4 configuration applied across all 496 linear layers, including GDN. Despite extreme compression, Minima matches BF16 performance within statistical noise across a suite of benchmarks while offering a significantly smaller footprint (17.5 GiB) and a 14–19% faster prefill speed.

---

## 🔍 关键发现与性能表现 (Key Findings & Performance)

> - **Benchmark Parity:** Minima matches BF16 baselines closely (a 5-task average difference of just `-0.52`) across perplexity at 4K/32K, MMLU-Pro, GSM8K, AIME'25, GPQA-Diamond, LiveCodeBench, and RULER retrieval up to 64K tokens.
- **Efficiency:** Achieves a compact model size of **17.5 GiB** alongside a **14% to 19% boost in prefill speed**.
- **Context Handling:** The perplexity gap at 32K context actually shrinks as position increases.

- **基准测试平齐：** Minima 在 4K/32K 困惑度、MMLU-Pro、GSM8K、AIME'25、GPQA-Diamond、LiveCodeBench 以及长达 64K token 的 RULER 检索等一系列测试中，与 BF16 基线高度一致（5个任务的平均差异仅为 `-0.52`）。
- **效率提升：** 模型体积压缩至紧凑的 **17.5 GiB**，同时**预填充速度提升了 14% 至 19%**。
- **上下文处理：** 在 32K 上下文下，随着位置增加，困惑度差距实际上在缩小。

---

## ⚙️ 四部分机制研究 (The Four-Part Mechanism Study)

> The authors investigate why the recurrent half of hybrid models is surprisingly resilient to 4-bit quantization, identifying four core reasons:
> 
> 1. **NVFP4 Block Scaling:** The 16-element block scaling successfully localizes extreme outliers in the residual stream, evenly distributing activation errors across varying layer roles.
> 2. **Robust Gate Projections:** The ostensibly fragile gate projections are actually the least sensitive components. Softplus, exponential, and sigmoid parameterizations effectively compress ~11% General Matrix Multiply (GEMM) error down to a mere ~2% output error.
> 3. **Delta-Rule Recurrence Resilience:** Injected noise remains at a flat plateau over 32K tokens. A state impulse is naturally forgotten within hundreds of steps because every write operation overwrites the state along the active key direction.
> 4. **Amortized Quantization Cost:** Per-token quantization overhead washes out over longer context lengths rather than compounding.
> 
> Additionally, the paper fixes a global-scale mismatch occurring when per-module-calibrated NVFP4 checkpoints are served using fused-module GEMM kernels, and demonstrates that calibrated FP8 KV-cache scales introduce zero performance loss.

作者深入研究了为什么混合模型的循环部分对 4 位量化表现出惊人的鲁棒性，并找出了四个核心原因：

1. **NVFP4 块缩放（Block Scaling）：** 16 元素的块缩放成功地将残差流中的极端异常值进行了局域化处理，使激活误差能够均匀分布在不同的层角色中。
2. **鲁棒的门控投影：** 表面上脆弱的门控投影实际上是最不敏感的组件。Softplus、指数和sigmoid参数化有效地将约 11% 的通用矩阵乘法（GEMM）误差压缩到仅约 2% 的输出误差。
3. **Delta规则循环的鲁棒性：** 注入的噪声在 32K token 范围内保持平坦的平台期。状态脉冲在数百步内就会被自然遗忘，因为每个写入操作都会沿着活跃的键方向覆盖状态。
4. **分摊的量化开销：** 每个 token 的量化开销会随着上下文长度的增加而被稀释，而不是累积放大。

此外，该论文还修复了使用融合模块 GEMM 内核服务于按模块校准的 NVFP4 检查点时发生的全局尺度不匹配问题，并证明了校准的 FP8 KV 缓存缩放不会引入任何性能损失。