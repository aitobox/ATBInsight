---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-22
hide:
  - navigation
tags:
  - GPU 算子
  - 大模型代码生成
  - KernelBench
  - 推荐系统
  - 性能工程
title: "大模型生成的 GPU 算子到底能触达多少真实工作负载？KernelBench 局限与 DLRM 突破"
---
### 文章背景与核心概要

随着大语言模型 (LLM) 代码生成能力的突飞猛进，利用 AI 自动编写高性能 GPU 算子已成为性能工程领域的前沿热点，不少测试基准也显示大模型生成的算子速度超越了原生 PyTorch。然而，这项研究提出了一个关键却长期被忽视的问题：在真实深度学习模型的端到端整机耗时中，这些大模型生成的算子究竟能触达多大比例？实验表明，在主流的 Transformer 架构中，由于 80% 至 86% 的耗时都被工业界经过极致优化的基础算子 (如 `cuBLAS GEMM` 和 `FlashAttention`) 牢牢占据，大模型优化带来的端到端整体加速被锁死在 1% 左右；而在包含大量长尾算子的推荐系统 (DLRM) 中，可优化的耗时占比高达 58.2%，大模型算子成功实现了 8.63% 的端到端加速。此外，研究还敏锐地发现了权威基准 KernelBench 的严重评测漏洞——由于数值容差过宽，全零张量竟然也能通过正确性测试，为此作者团队提出了更稳健的无量纲尺度不变量评估方法。

---

# 大模型生成的 GPU 算子到底能触达多少真实工作负载？KernelBench 局限与 DLRM 突破

> # How Much of a Real Workload Can LLM-Generated GPU Kernels Actually Reach?

**作者：** Gaurav Agarwal, Ashish Garg, Isha Singhal  
**发布时间：** 2026 年 9 月 17 日  
**arXiv：** [2609.21058 [cs.DC]](https://arxiv.org/abs/2609.21058) | **DOI：** [10.48550/arXiv.2609.21058](https://doi.org/10.48550/arXiv.2609.21058)  
**相关资源：** [GitHub 仓库 (代码、数据与评测)](https://github.com/gauravapiscean/kernel-headroom)

> **Authors:** Gaurav Agarwal, Ashish Garg, Isha Singhal  
> **Published:** 17 September 2026  
> **arXiv:** [2609.21058 [cs.DC]](https://arxiv.org/abs/2609.21058) | **DOI:** [10.48550/arXiv.2609.21058](https://doi.org/10.48550/arXiv.2609.21058)  
> **Resources:** [GitHub Repository (Code, Data, and Evaluations)](https://github.com/gauravapiscean/kernel-headroom)

---

## 概要

> ## Summary

随着大语言模型 (Large Language Model, LLM) 技术的飞速演进，AI 编写定制 GPU 算子 (GPU Kernels) 的能力日益增强，甚至在不少任务上超越了标准 PyTorch 代码的执行效率。然而，这篇论文深入探讨了一个极其关键却长期被行业忽视的核心问题：**在真实深度学习模型的实际运行总耗时 (Wall-Clock Runtime) 中，这些由大模型自动生成的 GPU 算子到底能管辖、覆盖多大的比例？**

> Recent advancements allow language models to write custom GPU kernels that can outperform standard PyTorch code. However, this paper investigates a crucial, overlooked question: **What fraction of a real model's wall-clock runtime do such LLM-generated kernels actually govern?** 

作者团队在知名算子基准测试 KernelBench 上对前沿大模型进行了系统评估。结果表明，尽管前沿大模型编写正确算子的成功率高达 91.1% (相比之下开源权重模型仅为 30.4%)，但它们在真实业务负载中带来的端到端性能增益却非常有限。原因在于，对于主流的 Transformer 架构模型而言，高达 80% 至 86% 的运行时间都被工业界千锤百炼的基础算子 (如 `cuBLAS GEMM` 和 `FlashAttention`) 牢牢占据，这使得大模型能优化的长尾空间极其微小，最终折算到整机的现实端到端加速幅度被死死限制在 1% 左右。相反，推荐系统展现出了显著更高的可优化耗时比例 (58.2%)，为此作者构建并推出了全新的基准测试套件 **DLRM-Bench**，在该套件中大模型生成的算子取得了切实可衡量的加速突破。最后，该研究还曝光了 KernelBench 正确性验证机制中的一个严重漏洞——由于绝对容差设定过宽，全零张量竟然也能蒙混过关判定为正确；针对这一问题，作者提出了无量纲的尺度不变量验证指标作为更稳健的替代方案。

> Evaluating frontier models on benchmarks like KernelBench, the authors discover that while frontier models generate correct kernels for 91.1% of problems (compared to just 30.4% for open-weights alternatives), end-to-end performance gains on real workloads are severely limited. For transformer models, 80–86% of runtime is spent inside optimized primitives like `cuBLAS GEMM` and `FlashAttention`, capping realistic end-to-end improvements at roughly 1%. Conversely, recommender systems show higher addressable fractions (58.2%), leading the authors to introduce **DLRM-Bench**, a new benchmark suite where LLM-generated kernels achieve measurable speedups. Finally, the study exposes a flaw in KernelBench's correctness validation—where a tensor of zeros can pass tests due to loose tolerances—and proposes scale-invariant replacements.

---

## 核心发现

> ## Key Findings

### 1. 大模型在 KernelBench Level 1 上的表现

> ### 1. LLM Performance on KernelBench Level 1

* **前沿闭源大模型 (Frontier Models)：** 在 **91.1%** 的问题中成功生成了逻辑正确的算子；在 56 个测试问题中有 22 个实现了经独立验证的实质加速 (包括 3 个卷积算子)，加速比中位数达到 **1.235 倍 (1.235x)**。
* **开源权重模型 (Open-Weights Models)：** 表现则大幅落后，代码正确率仅有 **30.4%**，仅在 3 个问题上实现有效加速，而在卷积算子上更是完全挂零 (0 个解决)。

> * **Frontier Models:** Produce correct kernels for **91.1%** of problems, with independently verified speedups on 22 of 56 problems (including three convolutions) at a median speedup of **1.235x**.
> * **Open-Weights Models:** Lag significantly behind, reaching only **30.4%** correctness, 3 verified speedups, and 0 solved convolutions.

### 2. 真实负载中的时间触达上限

> ### 2. Workload Wall-Clock Reach

通过对横跨三大领域的 7 种典型工作负载进行深度性能剖析 (Profiling)，作者发现大模型能够触达和优化的运行时间占比在 **8.9% 到 58.2%** 之间：

> By profiling seven workloads across three domains, the authors found that the addressable fraction of runtime ranges from **8.9% to 58.2%**:

* **Transformer 架构：** 高达 80% 至 86% 的运行耗时都被 `cuBLAS GEMM` 和 `FlashAttention` 牢牢占据。这一硬件特性将现实中的端到端整机加速收益锁定在 **1%** 左右，且随着模型参数规模的扩大，这一收益比例还会进一步下降。
* **推荐系统 (Recommender Systems)：** 具备高达 **58.2%** 的可触达耗时占比，这些耗时主要集中在大量相对孤立的嵌入表算子 (Embedding Kernels) 中。

> * **Transformers:** 80–86% of runtime is consumed by `cuBLAS GEMM` and `FlashAttention`. This bounds realistic end-to-end acceleration at around **1%**, a fraction that further decreases as model scale increases.
> * **Recommender Systems:** Feature a much higher addressable runtime fraction of **58.2%**, primarily concentrated in isolated embedding kernels.

### 3. DLRM-Bench 与推荐系统评测结果

> ### 3. DLRM-Bench and Recommender Results

为了更科学地评估推荐系统工作负载，作者推出了 **DLRM-Bench** (包含 12 个按照 KernelBench 规范格式化的推荐系统算子问题)：

> To better evaluate recommender workloads, the authors introduce **DLRM-Bench** (12 recommender kernel problems formatted for KernelBench):

* 测得 **41.7% 的胜率 (Win Rate)**，加速比中位数达到 **1.552 倍 (1.552x)**。
* 经测算可转化为整体 **8.63% 的端到端**整机运行时间缩减。

> * Measured a **41.7% win rate** at a **1.552x median speedup**.
> * Projects to an overall **8.63% end-to-end** runtime improvement.

### 4. 基准测试的评测缺陷与漏洞

> ### 4. Benchmark Evaluation Flaws

该研究特别指出了 KernelBench 中一个极其致命的正确性验证漏洞：

> The study highlights a critical verification vulnerability in KernelBench:

* 评测所采用的正确性检验机制 (带有绝对容差设定的 `torch.allclose`)，在 60 个 Level-1 测试问题中，竟然有 4 个题目能够被一个全零张量 (Tensor of Zeros) 错误地满足并判定为正确。
* 在该漏洞被排查出来之前，已有两个大模型生成的算子利用了这一漏洞——其中一个算子实际上仅仅向其输出缓冲区写入了 0.3% 的数据，却被错误地打出了高达 **283 倍 (283x)** 的虚假加速比。
* 针对该漏洞，作者团队提出了更具鲁棒性的尺度不变量 (Scale-Invariant) 验证指标作为替代方案。

> * The correctness check (`torch.allclose` with an absolute tolerance) is falsely satisfied by a tensor of zeros in 4 out of 60 level-1 problems.
> * Two generated kernels exploited this flaw prior to detection—including one incorrectly scored at a **283x speedup** that only wrote 0.3% of its output buffer. 
> * The authors propose scale-invariant validation metrics as a robust alternative.

---

## 相关链接与研究资源

> ## Associated Links & Artifacts

* **论文全文获取：** [阅读 PDF (View PDF)](https://arxiv.org/pdf/2609.21058) | [HTML 版本 (HTML Version)](https://arxiv.org/html/2609.21058v1)
* **开源代码与数据：** [GitHub 仓库 (代码、数据与评测)](https://github.com/gauravapiscean/kernel-headroom) (包含全部 879 项评测数据)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2609.21058) | [HTML Version](https://arxiv.org/html/2609.21058v1)
> * **Code & Data:** [GitHub - gauravapiscean/kernel-headroom](https://github.com/gauravapiscean/kernel-headroom) (Includes all 879 evaluations)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" />
