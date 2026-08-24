---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- GPU优化
- 多智能体
- 深度学习编译
- 硬件加速
- NVIDIA
title: KernelArc：面向GPU内核优化的多智能体框架
---
### 文章背景与核心概要
随着异构工作负载的日益复杂，GPU内核（Kernel）的手动优化变得极具挑战且耗费大量时间。为了解决这一痛点，本文介绍了 KernelArc——一个专为跨异构工作负载的自主GPU内核优化而设计的创新多智能体框架。该框架通过并行运行具备策略专业化的智能体，并利用“仅结论”共享内存、确定性基准测试护盾（benchmark guard）以及带平台触发起草机制的只读跨智能体状态进行协同，从而有效拓宽了搜索边界。

在基于 NVIDIA H100 和 B200 GPU 以及 SOL-ExecBench 代表性工作负载的评估中，KernelArc 在公开的 SOL-ExecBench 排行榜快照（2026年8月20日记录）中，于所有代表性的 L1、L2、量化（Quantization）和 FlashInfer 任务上均斩获第一名。这项研究证明了共享多智能体搜索能够在固定的候选预算内发现更强大的性能最优解，为自动化硬件加速开辟了新途径。

---

# KernelArc: A Multi-Agent Framework for GPU Kernel Optimization

## Summary
**KernelArc** is an autonomous multi-agent framework designed for GPU kernel optimization across heterogeneous workloads. By leveraging strategy-specialized agents running in parallel—coordinated via conclusions-only shared memory, a deterministic benchmark guard, and read-only cross-agent state with plateau-triggered drafting—KernelArc effectively broadens exploration bounds and discovers optimal performance incumbents within a fixed candidate budget.

Evaluated on NVIDIA H100 and B200 GPUs using category-representative SOL-ExecBench workloads, KernelArc achieved first place across all representative L1, L2, Quantization, and FlashInfer tasks in the public SOL-ExecBench leaderboard snapshot (recorded August 20, 2026).

---

## Paper Metadata

* **arXiv ID:** [arXiv:2608.17071](https://arxiv.org/abs/2608.17071) [cs.AI]
* **Subjects:** Artificial Intelligence (`cs.AI`); Multiagent Systems (`cs.MA`); Performance (`cs.PF`)
* **Authors:** 
  * Joyjit Kundu
  * Ben Stoffelen
  * Kaili Wang
  * Peter Vrancx
  * Ludovic Denoyer
* **Submission History:** 
  * [v1] Mon, 17 Aug 2026
  * [v2] Thu, 20 Aug 2026 *(current version)*
* **DOI:** [10.48550/arXiv.2608.17071](https://doi.org/10.48550/arXiv.2608.17071)

---

## Abstract

我们提出了 **KernelArc**，这是一个用于跨异构工作负载进行自主 GPU 内核优化的多智能体框架。策略专化的智能体并行运行，并通过“仅结论”共享内存、确定性基准测试护盾以及带平台触发起草机制的只读跨智能体状态进行协同。

> We present **KernelArc**, a multi-agent framework for autonomous GPU kernel optimization across heterogeneous workloads. Strategy-specialized agents run in parallel and coordinate through conclusions-only shared memory, a deterministic benchmark guard, and read-only cross-agent state with plateau-triggered drafting. 

我们在 NVIDIA H100 和 B200 GPU 上，使用类别代表性的 SOL-ExecBench 工作负载对 KernelArc 进行了评估。生成的实现涵盖了：
* 自定义 BF16 GEMM
* 静态 cuBLASLt Expert-API 配置表
* 融合的混合专家（MoE）反向传播
* 形状门控解码器层融合
* 原生 NVFP4 分组查询注意力（grouped-query attention）
* Paged prefill 注意力

> We evaluate KernelArc on NVIDIA H100 and B200 GPUs using category-representative SOL-ExecBench workloads. The resulting implementations span:
* Custom BF16 GEMM
* Static cuBLASLt Expert-API configuration tables
* Fused mixture-of-experts backward passes
* Shape-gated decoder-layer fusion
* Native NVFP4 grouped-query attention
* Paged prefill attention

在 2026 年 8 月 20 日记录的公开 SOL-ExecBench 排行榜快照中，**KernelArc 在评估的所有代表性 L1、L2、量化和 FlashInfer 任务中均排名第一。** 这些轨迹支持了论文的核心动机：共享的多智能体搜索可以在固定的候选预算内扩大探索范围并达到更强的最优解，而各个协同功能的价值则取决于具体的内核和优化阶段。

> In the public SOL-ExecBench leaderboard snapshot recorded on August 20, 2026, **KernelArc ranked first on every representative L1, L2, Quantization, and FlashInfer task evaluated.** The trajectories support the paper's central motivation: shared multi-agent search can broaden exploration and reach stronger incumbents within a fixed candidate budget, while the value of individual coordination features depends on the kernel and optimization stage.

---

## Evaluated Workloads & Architectures

评估的工作负载与架构：

> ## Evaluated Workloads & Architectures

* **硬件目标：** NVIDIA H100 和 B200 GPU
* **基准测试套件：** SOL-ExecBench
* **关键任务：** 
  1. L1 & L2 原语（例如，自定义 BF16 GEMM）
  2. cuBLASLt Expert-API 静态配置表
  3. 融合混合专家（MoE）反向传播
  4. 形状门控解码器层融合
  5. 原生 NVFP4 分组查询注意力
  6. Paged prefill 注意力

> * **Hardware Targets:** NVIDIA H100 and B200 GPUs
* **Benchmark Suite:** SOL-ExecBench
* **Key Tasks:** 
  1. L1 & L2 primitives (e.g., custom BF16 GEMM)
  2. cuBLASLt Expert-API static configuration tables
  3. Fused Mixture-of-Experts (MoE) backward passes
  4. Shape-gated decoder-layer fusion
  5. Native NVFP4 grouped-query attention
  6. Paged prefill attention

---

## Full-Text & Resources

全文与资源：

> ## Full-Text & Resources

* [查看 PDF](https://arxiv.org/pdf/2608.17071)
* [TeX 源码](https://arxiv.org/src/2608.17071)
* [许可证 (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/)

> * [View PDF](https://arxiv.org/pdf/2608.17071)
* [TeX Source](https://arxiv.org/src/2608.17071)
* [License (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" />