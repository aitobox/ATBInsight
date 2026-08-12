---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-07
hide:
- navigation
tags:
- CUDA
- 强化学习
- 大语言模型
- 矩阵乘法
- 性能优化
title: CUDA-L2：通过强化学习超越 cuBLAS 的矩阵乘法性能
---
### 文章背景与核心概要
矩阵乘法（如半精度通用矩阵乘法 HGEMM）是深度学习和现代人工智能工作负载的核心计算瓶颈。尽管 NVIDIA 的 `cuBLAS` 和 `cuBLASLt` 等闭源库经过了数十年的极致人工优化，但人类工程师在探索庞大的参数与代码配置空间时依然存在极限。

本文介绍了一种名为 **CUDA-L2** 的创新系统，它将大语言模型（LLM）与强化学习（RL）有机结合，用于自动优化 HGEMM CUDA 内核。CUDA-L2 以实际 CUDA 执行速度作为强化学习的奖励信号，系统化地探索高达 1,000 种配置方案。实验结果表明，无论是在离线模式还是在模拟实时推理的服务模式下，CUDA-L2 的性能均全面超越了包括 `torch.matmul`、`cuBLAS` 以及 `cuBLASLt` 在内的行业顶尖基准，展示了 LLM 引导的自动化技术在突破极端性能内核方面的巨大潜力。

# CUDA-L2: Surpassing cuBLAS Performance for Matrix Multiplication through Reinforcement Learning

> **arXiv:2512.02551** [cs.LG]  
> **Subjects:** Machine Learning (cs.LG); Artificial Intelligence (cs.AI)  
> **Authors:** Songqiao Su, Xiaoya Li, Albert Wang, Guoyin Wang, Jiwei Li, Chris Shum  
> **Submitted:** 2 Dec 2025 (v1); Last revised: 5 Aug 2026 (v4)  
> **DOI:** [10.48550/arXiv.2512.02551](https://doi.org/10.48550/arXiv.2512.02551)  
> **Project Code & Resources:** [GitHub - ornith-ai/CUDA-L2](http://github.com/ornith-ai/CUDA-L2)

---

## 📋 Summary

> **CUDA-L2** is an innovative system that integrates Large Language Models (LLMs) with Reinforcement Learning (RL) to automatically optimize Half-precision General Matrix Multiply (HGEMM) CUDA kernels. By utilizing CUDA execution speed as the RL reward signal, CUDA-L2 systematically explores vast configuration spaces—scaling to 1,000 configurations in ways that are impractical for human engineers. 
> 
> Across rigorous evaluations, CUDA-L2 outperforms leading matrix-multiplication baselines, including `torch.matmul` and NVIDIA’s closed-source, highly-optimized libraries (`cuBLAS` and `cuBLASLt`), in both offline and server inference modes.

## 📑 摘要

> 本文提出了 **CUDA-L2**，这是一个将大语言模型（LLMs）与强化学习（RL）相结合的系统，用于自动优化半精度通用矩阵乘法（HGEMM）CUDA 内核。利用 CUDA 执行速度作为 RL 奖励，CUDA-L2 在 1,000 种配置中自动优化 HGEMM 内核。
> 
> 在各项严苛的评估中，CUDA-L2 系统性地超越了迄今为止主要的矩阵乘法基准，从广泛使用的 [torch.matmul](http://torch.matmul) 到 NVIDIA 顶尖的闭源库（即 `cuBLAS`、`cuBLASLt`）。

* **离线模式**（内核连续执行且无时间间隔）：
  * 平均比 `torch.matmul` 提升 **+22.0%**。
  * 在采用最优布局配置（标准-标准 NN 和转置-标准 TN）时，比 `cuBLAS` 提升 **+19.2%**。
  * 比 `cuBLASLt-heuristic`（查询 cuBLASLt 库并根据启发式建议选择算法）提升 **+16.8%**。
  * 比最具竞争力的 `cuBLASLt-AutoTuning` 模型（从 cuBLASLt 的建议中最多 100 个候选里选择最快算法）提升 **+11.4%**。

* **服务模式**（以随机时间间隔执行内核以模拟实时推理）：
  * 性能加速进一步提升至：`torch.matmul` 的 **+28.7%**、`cuBLAS` 的 **+26.0%**、`cuBLASLt-heuristic` 的 **+22.4%** 以及 `cuBLASLt-AutoTuning` 的 **+15.9%**。

> * **Offline Mode** (kernels executed consecutively without time intervals):
>   * **+22.0%** over `torch.matmul` on average.
>   * **+19.2%** over `cuBLAS` using the optimal layout configuration (normal-normal NN and transposed-normal TN).
>   * **+16.8%** over `cuBLASLt-heuristic` (which queries the cuBLASLt library and selects algorithms based on heuristic suggestions).
>   * **+11.4%** over the most competitive `cuBLASLt-AutoTuning` model (which selects the fastest algorithm from up to 100 candidates from cuBLASLt's suggestions).
> 
> * **Server Mode** (kernels executed at random intervals simulating real-time inference):
>   * Speedups further increase to **+28.7%** (`torch.matmul`), **+26.0%** (`cuBLAS`), **+22.4%** (`cuBLASLt-heuristic`), and **+15.9%** (`cuBLASLt-AutoTuning`).

> CUDA-L2 demonstrates that even the most performance-critical, heavily-optimized kernels like HGEMM can be significantly improved through LLM-guided RL automation by exploring configuration scales previously impractical for human developers.

---

## 🔗 访问与链接

> * **Full-Text Options:** [View PDF](https://arxiv.org/pdf/2512.02551) | [HTML (experimental)](https://arxiv.org/html/2512.02551v4) | [TeX Source](https://arxiv.org/src/2512.02551)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## 📦 提交历史

> * **[v1]** Tue, 2 Dec 2025 09:20:15 UTC (545 KB)
> * **[v2]** Fri, 12 Dec 2025 00:47:40 UTC (545 KB)
> * **[v3]** Mon, 13 Jul 2026 00:51:09 UTC (1,494 KB)
> * **[v4]** Wed, 5 Aug 2026 18:31:31 UTC (1,494 KB) *(this version)*