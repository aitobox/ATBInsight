---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-09-04
hide:
- navigation
tags:
- Perplexity
- Apple Silicon
- Rust
- Metal
- 模型推理
title: Perplexity开源Lily：专为Apple Silicon上Qwen3.6-35B-A3B打造的Rust + Metal推理引擎
---
### 文章背景与核心概要
在这篇技术文章中，Perplexity 宣布开源其用于驱动 Perplexity Computer 中混合计算（Hybrid Compute）的自定义本地推理引擎——**Lily**。该引擎专为 Apple Silicon 芯片上的 **Qwen3.6-35B-A3B** 模型设计，彻底抛弃了 PyTorch 和 MLX 等传统框架，转而采用高性能的 Rust 运行时与手写 Metal 内核。通过针对单一模型和硬件架构进行深度定制，Lily 实现了卓越的性能表现——在 M5 Max 芯片上，其预填充（prefill）速度平均比 MLX-LM 快 **1.23倍**，解码（decode）速度快 **1.35倍**。

文章详细探讨了专门化架构的必要性、模型的特定工作负载形态，以及 Lily 在预填充和解码阶段所采用的技术优化（如按需反量化、GPU 常驻路由、并发 Metal 传递以及内存优化等）。这些创新不仅大幅减少了数据搬运，还在长上下文场景下带来了显著的性能提升。

> ## Perplexity Open Sources Lily: A Rust + Metal Inference Engine for Qwen3.6-35B-A3B on Apple Silicon
> 
> ## Summary
> 
> Perplexity has open-sourced **Lily**, the custom local inference engine powering Hybrid Compute in Perplexity Computer. Designed exclusively for the **Qwen3.6-35B-A3B** model on Apple Silicon, Lily bypasses traditional frameworks like PyTorch and MLX, utilizing a high-performance Rust runtime coupled with hand-written Metal kernels. By heavily specializing the engine for a single model and hardware architecture, Lily achieves superior performance—outperforming MLX-LM by an average of **1.23x in prefill** and **1.35x in decode** speeds on an M5 Max chip.

---

为什么要进行专门化设计？
虽然像 **MLX** 和 **MLX-LM** 这样的默认 Mac 软件栈提供了极大的灵活性，但其操作必须能够在各种模型架构之间保持通用和可复用。Lily 摒弃了这种通用化方法，将模型结构、执行计划和内核选择紧密耦合到一个单一的优化运行时中。

> ---
> 
> ## Why Specialize at All?
> 
> While default Mac stacks like **MLX** and **MLX-LM** offer great flexibility, their operations must remain reusable across various model architectures. Lily discards this generalized approach, tightly coupling model structure, execution plans, and kernel selection into a single, optimized runtime.

---

三种工作负载形态
Qwen3.6-35B-A3B 模型拥有 350 亿参数，但每个 Token 仅激活约 30 亿参数。其架构呈现出三种不同的计算模式：
* **混合专家模型（MoE）：** 路由器对 256 个专家进行评分并选择其中 8 个，同时包含 1 个共享专家。
* **注意力层（Attention Layers）：** 结合了使用分组查询注意力（GQA）的 10 个全注意力层与 30 个 Gated DeltaNet 层。
* **循环机制（Recurrence）：** 结合了不均匀的专家组、不断增长的 KV 缓存以及固定大小的循环。

> ---
> 
> ## Three Workload Shapes
> 
> The Qwen3.6-35B-A3B model utilizes 35 billion parameters while activating roughly 3 billion per token. Its architecture presents three distinct computational patterns:
> * **Mixture-of-Experts (MoE):** A router scores 256 experts to pick 8, alongside 1 shared expert.
> * **Attention Layers:** Mixes 10 full-attention layers using grouped-query attention (GQA) with 30 Gated DeltaNet layers.
> * **Recurrence:** Combines uneven expert groups, a growing KV cache, and a fixed-size recurrence.

---

预填充：保持权重压缩，将路由保留在 GPU 上
该检查点使用分组仿射 4 位量化（groupwise affine 4-bit quantization），将约 70 GB 的 bfloat16 权重压缩至 19.4 GB。Lily 通过以下几个关键机制优化了预填充性能：
* **动态反量化（On-the-Fly Dequantization）：** 在分组 GEMM 内核内部一次重建一个瓦片（tile）的权重，并将结果保存在线程组内存中，以防止扩展后的数组触及统一内存。
* **GPU 常驻路由（GPU-Resident Routing）：** 将路由直方图、前缀扫描（prefix scan）、散布（scatter）和块映射保留在单个 GPU 命令缓冲区中，在 512 个 Token 时将预填充速度提升了 **89%**。
* **算子融合（Fused Operations）：** 将反量化融合进分组 GEMM 中，在 512 个 Token 的提示词下，将端到端预填充性能提升了 **77.4%**。

> ---
> 
> ## Prefill: Keep Weights Packed, Keep Routing on the GPU
> 
> The checkpoint uses groupwise affine 4-bit quantization, compressing ~70 GB of bfloat16 weights down to 19.4 GB. Lily optimizes prefill performance through several key mechanisms:
> * **On-the-Fly Dequantization:** Weights are reconstructed one tile at a time inside grouped GEMM kernels, holding results in threadgroup memory to prevent expanded arrays from reaching unified memory.
> * **GPU-Resident Routing:** Keeping the routing histogram, prefix scan, scatter, and block map inside a single GPU command buffer boosted prefill speeds by **89%** at 512 tokens.
> * **Fused Operations:** Fusing dequantization into grouped GEMM raised end-to-end prefill performance by **77.4%** at a 512-token prompt.

---

解码：最小化每个 Token 传输的字节数
由于 Batch-1 解码主要受限于内存带宽而非计算能力，Lily 专注于减少数据移动：
* **并发 Metal 传递（Concurrent Metal Passes）：** 在并发传递中记录真实的依赖关系，以允许独立的内核重叠执行。
* **零 CPU 往返（Zero CPU Round-Trips）：** 将选定的 Token 直接写入下一步的 GPU 常驻输入槽中。
* **内存优化（Memory Optimizations）：** 合并的缓存读取将键（key）带宽从 33.8 提升至 47.9 GB/s，值（value）带宽从 42.0 提升至 61.8 GB/s。此外，GQA 打包和固定块注意力布局在扩展上下文时带来了显著的加速（例如在 128K 上下文中提升 **+40.2%**）。

> ---
> 
> ## Decode: Minimize Bytes Moved Per Token
> 
> Because batch-1 decode is heavily bottlenecked by memory bandwidth rather than compute, Lily focuses on reducing data movement:
> * **Concurrent Metal Passes:** Records real dependencies in a concurrent pass to allow independent kernels to overlap.
> * **Zero CPU Round-Trips:** Writes selected tokens straight into the next step’s GPU-resident input slot.
> * **Memory Optimizations:** Coalesced cache reads increased key bandwidth from 33.8 to 47.9 GB/s and value bandwidth from 42.0 to 61.8 GB/s. Furthermore, GQA packing and fixed-block attention layouts yielded substantial speedups at extended contexts (e.g., **+40.2%** at 128K context).

---

性能结果
在 40 核、128 GB 的 M5 Max（Batch 大小为 1）上进行了测试，Lily 与 MLX-LM 在 256 到 128K 的 Token 长度范围内进行了基准对比：
* **预填充：** 平均达到 **4,156 tokens/s**，而 MLX-LM 为 3,388 tokens/s（**1.23x**）。
* **解码：** 平均达到 **170.0 tokens/s**，而 MLX-LM 为 126.4 tokens/s（**1.35x**）。
* **准确率：** 对 192 个位置进行的教师强制检查（teacher-forced check）表明，Lily 的困惑度（perplexity）仅高出 0.04%，并且有 **96.35%** 的时间与排名第一的 Token 相匹配。

> ---
> 
> ## Performance Results
> 
> Tested on a 40-core, 128 GB M5 Max (batch size 1), Lily was benchmarked against MLX-LM across token lengths from 256 to 128K:
> * **Prefill:** Averaged **4,156 tokens/s** vs. MLX-LM's 3,388 tokens/s (**1.23x**).
> * **Decode:** Averaged **170.0 tokens/s** vs. MLX-LM's 126.4 tokens/s (**1.35x**).
> * **Accuracy:** A teacher-forced check across 192 positions showed Lily's perplexity was only 0.04% higher, matching the top-ranked token **96.35%** of the time.

---

核心要点
* **独立架构：** 专门为 Apple Silicon 上的 Qwen3.6-35B-A3B 构建的 Rust + Metal 推理引擎，完全舍弃了 PyTorch 和 MLX。
* **卓越速度：** 在 M5 Max 芯片上，相比 MLX-LM，预填充速度快 1.23 倍，解码速度快 1.35 倍。
* **预填充提升：** GPU 常驻专家路由（**+89%**）以及将反量化融合至分组 GEMM（**+77.4%**）。
* **解码提升：** GQA 打包（在 32K 时 **+23.8%**）以及固定块注意力（在 128K 时 **+40.2%**）。

> ---
> 
> ## Key Takeaways
> 
> * **Standalone Architecture:** A Rust + Metal inference engine built specifically for Qwen3.6-35B-A3B on Apple Silicon, omitting PyTorch and MLX entirely.
> * **Superior Speed:** Delivers 1.23x faster prefill and 1.35x faster decode compared to MLX-LM on an M5 Max chip.
> * **Prefill Boosts:** GPU-resident expert routing (**+89%**) and fused dequantization into grouped GEMM (**+77.4%**).
> * **Decode Boosts:** GQA packing (**+23.8% at 32K**) and fixed-block attention (**+40.2% at 128K**).

---

资源与链接
* [Perplexity 技术详情](https://www.perplexity.ai/hub/blog/optimizing-on-device-inference-for-apple-silicon)
* [Lily GitHub 仓库](https://github.com/perplexityai/pplx-garden/tree/main/lily)

> ---
> 
> ## Resources & Links
> 
> * [Technical Details from Perplexity](https://www.perplexity.ai/hub/blog/optimizing-on-device-inference-for-apple-silicon)
> * [Lily GitHub Repository](https://github.com/perplexityai/pplx-garden/tree/main/lily)