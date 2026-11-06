---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-11-07
hide:
- navigation
tags:
- FlashAttention
- AMD
- FP8
- GPU 算子优化
title: Zyphra ZYFA：针对 AMD MI355X 的 FP8 闪存注意力算子，加速高达 1.76 倍
---
# Zyphra ZYFA：针对 AMD MI355X 的 FP8 闪存注意力算子，加速高达 1.76 倍

> # Zyphra ZYFA: FP8 FlashAttention for AMD MI355X, Up to 1.76x Faster

### 文章背景与核心概要
在现代大语言模型 (Large Language Model, LLM) 的计算中，注意力机制 (Attention Mechanism) 的预填充 (Prefill) 阶段是决定推理响应速度与训练吞吐量的关键瓶颈。尽管 AMD 最新的旗舰 GPU Instinct MI355X 配备了理论算力惊人的 FP8 矩阵运算单元，但在实际计算中，受制于 Softmax 在向量单元上的耗时与流水线空转，FP8 注意力算子的实际性能往往难以充分释放。为此，AI 基础设施团队 Zyphra 研发并开源了专为 MI355X 深度定制的注意力算子套件 ZYFA (Zyphra FlashAttention on AMD)。ZYFA 创新性地采用“精简概率计算 (Lean P)”与双波乒乓调度 (Two-Wave Ping-Pong Schedule) 技术消除硬件停顿，在真实大模型激活值测试中实现了相对 AMD 官方 AITER 库 1.16 至 1.76 倍的吞吐加速，并将量化误差削减高达 78%，为 AMD 算力生态上的大模型高效部署树立了新标杆。

---

## 核心总结

> ## Summary

Zyphra 正式推出了 **ZYFA (Zyphra FlashAttention on AMD)**，这是一套采用 `Apache 2.0` 协议开源的 FP8 与 BF16 预填充注意力算子库，专门针对 **AMD Instinct MI355X** GPU 进行了硬件级极限优化。通过引入创新的“精简概率计算 (Lean P)”以及双波乒乓调度机制，ZYFA 彻底攻克了 FP8 模式下 Softmax 运算导致的性能瓶颈。在真实大模型激活值基准测试中，ZYFA 相比 AMD 官方默认的 AITER 算子库实现了 **1.16 倍至 1.76 倍的性能加速**，同时大幅降低了量化数值误差。

> Zyphra has introduced **ZYFA (Zyphra FlashAttention on AMD)**, an open-source (`Apache 2.0`) suite of FP8 and BF16 prefill attention kernels optimized specifically for **AMD Instinct MI355X** GPUs. By addressing the bottlenecks of FP8 softmax operations using innovative approaches like "Lean P" and a two-wave ping-pong schedule, ZYFA achieves a **1.16x to 1.76x speedup** over AMD's default AITER kernel library on real model activations, while drastically reducing numerical error.

---

## 核心要点一览

> ## TL;DR

* **框架定位**：专为因果前向（预填充）注意力计算设计的算子库，支持 FP8 (e4m3) 与 BF16 数据精度，适配注意力头维度 (Head Dim) 128 以及多头潜在注意力 (Multi-Head Latent Attention, MLA) 维度规格 (192/128)。
* **软硬件环境**：专门针对 AMD Instinct MI355X GPU (CDNA4 架构，gfx950)，基于 ROCm 7.2.3 与 PyTorch 2.12 环境构建，提供可直接无缝替换的 `flash_attn_func` 标准调用接口。
* **实测性能**：在真实模型激活值下，FP8 吞吐量比 AITER 提升 1.16 至 1.76 倍；BF16 精度下性能基本持平 (1.01 至 1.02 倍)。
* **最佳表现**：在 32K Token 序列长度下，FP8 算力达到 2,672 TFLOP/s（达到硬件规格峰值算力的 53%，而 AITER 仅为 39%）。
* **最保守表现**：在 Mistral-7B 真实激活值下仍取得 1.16 倍加速；由于动态调频机制，此时 FP8 运行核心频率降至 1,628 MHz（而 AITER 为 2,108 MHz），但总执行周期显著减少。

> * **Framework:** Causal forward (prefill) attention kernel library in FP8 (e4m3) and BF16, supporting head dim 128 and MLA shapes (192/128).
> * **Hardware & Software:** AMD Instinct MI355X only (CDNA4, gfx950), ROCm 7.2.3, PyTorch 2.12, utilizing a drop-in `flash_attn_func` interface.
> * **Performance:** 1.16–1.76x faster than AITER’s FP8 throughput on real activations; roughly ties in BF16 (1.01–1.02x).
> * **Best Case:** 2,672 TFLOP/s FP8 at 32K tokens (53% of the FP8 datasheet peak vs. AITER's 39%).
> * **Worst Case:** 1.16x speedup on Mistral-7B activations, where the FP8 clock drops to 1,628 MHz compared to AITER’s 2,108 MHz.

---

## 什么是 ZYFA？

> ## What is ZYFA?

ZYFA 的核心技术细节已在技术[论文](https://arxiv.org/abs/2611.07496)中全面披露，并由 Zyphra 团队完全开源。它是 [Zyphra 优化引擎 (Zyphra Optimization Engine, ZOE)](https://zyphra.com/optimization-engine) 的核心注意力计算引擎，为 Zyphra 商业云平台提供底层算力支持。在工程实现上，BF16 算子使用 HIP 语言编写，而性能关键的 FP8 算子则是由 Python 脚本自动化生成并经过手工精心排布指令周期的纯底层汇编代码。

> ZYFA is detailed in a technical [paper](https://arxiv.org/abs/2611.07496) and is open-sourced by Zyphra. It powers the attention engine of the [Zyphra Optimization Engine (ZOE)](https://zyphra.com/optimization-engine), which drives Zyphra Cloud. While the BF16 kernels are written in HIP, the FP8 kernels consist of hand-scheduled assembly generated via a Python script.

---

## 为什么 FP8 注意力算子在 MI355X 上往往表现不佳？

> ## Why Does FP8 Attention Underperform on MI355X?

尽管在硬件理论上，FP8 矩阵乘法指令的峰值吞吐量是 BF16 的两倍，但在标准注意力计算流程中，FP8 实际上只能加速两个矩阵相乘步骤：即查询与键的相乘 $QK^T$ 以及概率与值的相乘 $PV$。而夹在两者之间的 Softmax 归一化运算是在 GPU 的向量运算单元 (Vector Unit) 上执行的，无论精度模式如何切换，向量单元的执行速度完全保持不变。

> Although FP8 matrix instructions run at twice the BF16 peak, FP8 only accelerates two matrix products: $QK^T$ and $PV$. The softmax computation between them runs on the vector unit at identical speeds regardless of precision.

以 32 个 Query 对 128 个 Key 进行计算为例，FP8 矩阵乘法仅需 1,024 个时钟周期即可完成，但标准的 FP8 Softmax 向量计算却需要消耗多达 896 个周期。这意味着，算子必须做到近乎极致完美的指令重叠 (Instruction Overlap)，才能防止矩阵计算单元陷入饥饿空转。Zyphra 深入剖析后发现，AMD 官方默认的 AITER 算子库有高达 31.7% 的周期处于矩阵流水线闲置状态，这是因为 MI355X 芯片缺乏用于跟踪矩阵指令完成状态的硬件单元，使得调度重任完全落在了软件指令编排的肩膀上。

> For 32 queries against 128 keys, FP8 matrix work requires 1,024 cycles, while the standard FP8 softmax takes 896 vector cycles. Consequently, the kernel requires near-perfect instruction overlap to keep the matrix units active. Zyphra's analysis shows that AMD's default AITER leaves the matrix pipeline idle for 31.7% of cycles because the MI355X lacks hardware tracking for matrix instruction completion, placing the burden entirely on instruction ordering.

---

## ZYFA 是如何工作的？三大核心黑科技剖析

> ## How Does ZYFA Work?

ZYFA 引入了三项颠覆性的底层架构优化技术：

> ZYFA implements three core optimization techniques:

1. **Lean P（单条乘加指令替代复杂指数运算）：** 
   将 FP8 (e4m3) 的二进制位模式直接当成整数读取时，会发现一个奇妙的数学规律：输入数值每翻一倍，对应的整数值恰好增加 8。这意味着以 2 为底的指数运算 $2^x$ 可以被高度近似为线性缩放加上一个常数偏置（即 $8x + C$）。Lean P 利用这一特性，仅用单条乘加 (Multiply-Add) 指令和单次整数类型转换，即可估算出每一个 FP8 概率值，使得每个数据块的 Softmax 向量计算周期直接从 896 骤降至 384。
2. **双波乒乓调度机制 (Two-Wave Ping-Pong Schedule)：** 
   每个单指令多数据 (SIMD) 运算单元由两个计算波 (Wave) 共享协同。当一个 Wave 在忙着分发矩阵乘法指令时，另一个 Wave 刚好在并发计算注意力概率，两者交替往复、打乒乓球般无缝衔接。配合 Lean P 技术，该机制使得矩阵运算流水线在稳态运行中的忙碌利用率高达 86%（而传统精确指数运算仅能达到 60%）。
3. **分块按需缩放与舍入行求和 (Per-Block Scaling and Rounded Row Sum)：** 
   在进行数值舍入之前，每 64 个 Key 组成的概率块都会先按 2 的整数幂进行预缩放。CDNA4 架构原生支持的带缩放矩阵计算指令能够直接吸收该缩放系数，完全不会引入额外的性能损耗。此外，ZYFA 还通过每块额外执行一条矩阵指令来计算舍入后概率的精确总和并进行归一化除法。

> 1. **Lean P (One Multiply-Add Instead of an Exponential):** 
>    Reading an e4m3 bit pattern as an integer reveals that it increases by 8 each time the value doubles, meaning $2^x$ can be approximated via linear scaling plus a constant ($8x + C$). Lean P evaluates each FP8 probability using a single multiply-add and a single integer conversion, dropping softmax vector cycles per block from 896 down to 384.
> 2. **Two-Wave Ping-Pong Schedule:** 
>    Two computational waves share each SIMD unit. While one wave issues matrix instructions, the other calculates probabilities, alternating back and forth. Combined with Lean P, this keeps the matrix pipeline busy for 86% of steady-state cycles (up from 60% with exact exponential calculations).
> 3. **Per-Block Scaling and Rounded Row Sum:** 
>    Every 64-key block of probabilities is scaled by a power of 2 prior to rounding. CDNA4's scaled matrix instruction absorbs this factor without performance penalties. ZYFA also divides by the sum of rounded probabilities, computed using an extra matrix instruction per block.

---

## ZYFA 的实际运行速度究竟有多快？

> ## How Fast Is ZYFA?

* **真实激活值加速比**：在 16K 上下文序列长度下，FP8 算子在主流大模型激活值上表现惊艳：**Mistral-7B 加速 1.16 倍**、**Qwen3-8B 加速 1.17 倍**，而在 **DeepSeek-V2-Lite 上更是取得了高达 1.76 倍的巨大飞跃**。
* **基准测试性能**：在 32K 长度的高斯合成基准测试 (Gaussian Benchmark) 中，头维度 128 的 FP8 算子吞吐量高达 **2,672 TFLOP/s**（AITER 仅为 1,944 TFLOP/s）。在针对 MLA 架构的特殊维度规格下，吞吐量更是达到 **2,464 TFLOP/s**，对比 AITER 的 1,237 TFLOP/s 实现了 **1.99 倍**的翻倍提升。
* **超高能效表现**：在 Mistral-7B 和 Qwen3-8B 的实际网络层算力捕获测试中，ZYFA 分别实现了 **1.94 TFLOP/J 和 1.91 TFLOP/J** 的能效比，显著优于 AITER 的 1.60 与 1.56 TFLOP/J。

> * **Real-Activation Speedups:** Achieves FP8 speedups at 16K sequence lengths of **1.16x (Mistral-7B)**, **1.17x (Qwen3-8B)**, and **1.76x (DeepSeek-V2-Lite)**.
> * **Benchmark Performance:** On 32K Gaussian benchmarks, the head-dim-128 FP8 kernel hits **2,672 TFLOP/s** (vs. AITER's 1,944). At MLA shapes, it reaches **2,464 TFLOP/s** vs. AITER's 1,237 (a **1.99x** multiplier).
> * **Energy Efficiency:** On captured Mistral-7B and Qwen3-8B layers, ZYFA delivers **1.94 and 1.91 TFLOP/J**, outperforming AITER's 1.60 and 1.56 TFLOP/J.

---

## 为什么真实模型下的提速比合成基准测试要稍低？

> ## Why Are Real-Model Gains Smaller Than Benchmark Gains?

AMD MI355X 显卡具备基于操作数“位翻转 (Bit-Flipping)”活跃程度动态调节核心时钟频率的功耗管理特性。AITER 算子在运算中产生了较多的数值零和次正规数 (Subnormals)，这些数据所触发的晶体管位翻转较少，从而让 GPU 能够维持更高的工作主频。例如在 Mistral-7B 模型层实测中，ZYFA 运行时的 GPU 频率自动降到了 1,628 MHz，而 AITER 却能维持在 2,108 MHz。然而，即便在明显更低的运行主频下，ZYFA 凭借极高的架构指令效率，所需执行的总时钟周期依然大幅减少，最终在整体端到端耗时上稳稳胜出。

> The MI355X clock frequency scales based on operand bit-flipping activity. AITER generates more zero values and subnormals, which flip fewer bits and allow the GPU to maintain a higher clock speed. For instance, on a Mistral-7B layer, ZYFA runs at 1,628 MHz compared to AITER’s 2,108 MHz. Despite the lower clock frequency, ZYFA requires fewer total cycles to complete execution.

---

## ZYFA 的 FP8 注意力计算精度如何？

> ## How Accurate Is ZYFA’s FP8 Attention?

以高精度 FP64（双精度浮点数）计算出的注意力真值作为对比基准：

> Measured against FP64 attention baselines:

* 在 Mistral-7B 模型上，ZYFA 的 FP8 计算误差仅为 AITER 的 **0.22 倍**；在 Qwen3-8B 上，误差仅为 AITER 的 **0.38 倍**。
* 在完整的 Mistral-7B 模型输出评估中，ZYFA 相对 FP64 黄金标准的 KL 散度 (KL Divergence) 仅为 **$3.4 \times 10^{-3}$**，显著优于 AITER 的 **$5.9 \times 10^{-3}$**。
* 在连续执行多达 7,200 次算子调用的压力测试中，ZYFA 的输出保持了完全一致的位级别确定性 (Bitwise Identical)。
* 对 Query (Q) 和 Key (K) 矩阵引入阿达马变换旋转 (Hadamard Rotation)，能够有效抑制由于 Q、K、V 格式转换引入的主要量化误差，且在 Mistral-7B 上的实测开销仅增加约 0.1%。

> * ZYFA's FP8 error is **0.22x** of AITER's on Mistral-7B and **0.38x** on Qwen3-8B.
> * In full Mistral-7B evaluations, the KL divergence from FP64 is **$3.4 \times 10^{-3}$** for ZYFA versus **$5.9 \times 10^{-3}$** for AITER.
> * ZYFA outputs remained bitwise identical across 7,200 consecutive kernel launches.
> * Applying a Hadamard rotation to Q and K helps mitigate the primary source of quantization error introduced by Q, K, and V formatting, adding only ~0.1% to attention overhead on Mistral-7B.

---

## 特性对比：ZYFA 与主流注意力算子方案全景对照

> ## Feature Comparison: ZYFA vs. Alternative Attention Kernels

| 特性对比 (Feature) | [ZYFA FP8](https://github.com/Zyphra/zyfa) | [AITER FP8](https://github.com/ROCm/aiter) | [FlashAttention-3](https://arxiv.org/abs/2407.08608) | [FlashAttention-4](https://arxiv.org/abs/2603.05451) |
| :--- | :--- | :--- | :--- | :--- |
| **研发团队 (Maker)** | Zyphra | AMD | Dao-AILab 等 | Dao-AILab 等 |
| **目标 GPU (Target GPU)** | AMD MI355X | AMD MI300X 至 MI355X | NVIDIA H100/H800 | NVIDIA B200 (兼顾 Hopper) |
| **官方标称吞吐量 (Headline Throughput)** | 2,672 TFLOP/s FP8 | 1,944 TFLOP/s FP8 | 接近 1.2 PFLOP/s FP8 | 1,613 TFLOP/s BF16 |
| **占理论峰值比例 (Share of Peak)** | 53% FP8 | 39% FP8 | 未公开 (FP8) | 71% BF16 |
| **Softmax 实现方案 (Softmax Approach)** | Lean P 线性化近似，免除指数运算 | 硬件指令级指数运算 | 借助异步 Tensor Core 实现重叠掩盖 | 软件模拟指数运算 |
| **FP8 精度指标 (FP8 Accuracy Claim)** | 误差比 AITER 降低 62–78% | 基准水平 (Baseline) | 误差比基线 FP8 降低 2.6 倍 | 未公开 |
| **功能覆盖范围 (Scope)** | 仅因果前向预填充 (Causal prefill forward only) | 预填充、解码、MLA、分页 KV 缓存 | 前向与反向，FP8 前向 | 前向与反向传播 |
| **开源许可 (License)** | [Apache 2.0](https://github.com/Zyphra/zyfa) | [MIT](https://github.com/ROCm/aiter) | [BSD-3-Clause](https://github.com/Dao-AILab/flash-attention) | [BSD-3-Clause](https://github.com/Dao-AILab/flash-attention) |

*（注：跨芯片厂商的指标对比受不同的输入参数与动态时钟频率调节机制影响；Zyphra 本次未直接实测 NVIDIA GPU 设备。）*

> *(Note: Cross-vendor metrics rely on varying inputs and clock behaviors; Zyphra did not test NVIDIA GPUs.)*

---

## 核心总结与启示

> ## Key Takeaways

* 在 AMD MI355X 上，FP8 注意力计算的本质瓶颈受制于 **Softmax 向量运算 (Softmax-bound)**，而非矩阵计算单元性能。
* **Lean P** 巧妙利用位运算规律，成功使用单条乘加指令替代了昂贵繁重的硬件指数运算，大幅解放了计算资源。
* 真实模型端到端加速比介于 **1.16 倍至 1.76 倍** 之间，虽略低于合成基准测试数值，但这是由于硬件根据位翻转活跃度动态限频导致的正常现象。
* FP8 数值计算误差得到显著抑制（在头维度 128 下，误差比 AITER **大幅降低 62%–78%**）。
* 目前该算子库严格限定于 MI355X 硬件平台上的**预填充前向运算**，尚未支持解码 (Decode) 或分页 KV 缓存 (Paged KV-cache)。

> * FP8 attention workloads on the MI355X are fundamentally **softmax-bound**, not matrix-bound.
> * **Lean P** successfully swaps expensive hardware exponentials for a single multiply-add instruction.
> * Real-world model speedups range from **1.16x to 1.76x**, landing lower than synthetic benchmarks due to hardware clock throttling dynamics.
> * FP8 error rates drop significantly (**62–78% lower** than AITER at head dimension 128).
> * The framework is strictly scoped to **prefill-only** operations on the MI355X (no decode or paged KV-cache support).

---

## 参考资源与相关链接

> ## Resources & Links

* [阅读完整学术研究论文](https://arxiv.org/abs/2611.07496)
* [Zyphra 官方技术博客发布文章](https://zyphra.com/our-work/zyfa)
* [GitHub 开源项目代码仓库](https://github.com/Zyphra/zyfa)

> * [Read the Research Paper](https://arxiv.org/abs/2611.07496)
> * [Zyphra Official Blog Post](https://zyphra.com/our-work/zyfa)
> * [GitHub Repository](https://github.com/Zyphra/zyfa)
