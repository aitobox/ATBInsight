---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- GPU优化
- PTXBench
- 大语言模型
- 编译器
- 硬件架构
title: PTXBench：利用架构专用 PTX 评估与适配大语言模型以进行 GPU 核函数优化
---
### 文章背景与核心概要

随着深度学习模型规模的爆炸式增长，针对特定硬件架构（如 NVIDIA H100 和 B200 GPU）对手工或生成的底层代码进行优化变得至关重要。PTX（Parallel Thread Execution）作为 NVIDIA GPU 的底层汇编语言，对于榨取极致的计算性能起着决定性作用。然而，目前的大语言模型（LLMs）在生成和优化架构专用的 PTX 代码方面缺乏系统的评估标准与针对性的微调方案。

为了填补这一空白，本文推出了 **PTXBench**——一个用于评估和适配大语言模型以进行 GPU 核函数优化的综合基准测试。该基准从功能正确性、目标指令的运行时执行情况以及相较于前沿库的性能加速比等维度，全面评测了模型在 GEMM（通用矩阵乘法）和注意力机制（Attention）工作负载上的表现。评估结果表明，当前 LLM 在处理复杂的注意力反向传播等任务时仍显吃力，且仅生成目标指令并不能保证具备竞争力的性能。为此，作者通过基于修复条件（repair-conditioned）的监督微调（如适配 Qwen3.6-27B），显著提升了模型在多项任务上的表现，同时也指出泛化能力仍受数据覆盖度、平衡性以及推理教师质量的深度制约。

---

## 摘要与元数据

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

## Summary (英文原版概要)

> **PTXBench** is a comprehensive benchmark designed to evaluate and adapt Large Language Models (LLMs) for GPU kernel optimization using architecture-specific PTX (Parallel Thread Execution). The benchmark measures functional correctness, runtime execution of targeted instructions, and performance speedups over frontier libraries across GEMM (General Matrix Multiply) and attention workloads on H100 and B200 GPUs. 
> 
> Evaluation results reveal that current LLMs exhibit uneven architecture-specific PTX capabilities—struggling particularly with complex attention backward workloads—and that merely executing target instructions does not guarantee competitive performance. Furthermore, the authors demonstrate that supervised fine-tuning (e.g., adapting Qwen3.6-27B) via repair-conditioned training can enhance performance on several tasks, though generalization remains challenging and depends heavily on data coverage, balance, and reasoning teacher quality.

---

## 论文元数据 (Paper Metadata)

* **arXiv 标识符:** [arXiv:2608.17379](https://arxiv.org/abs/2608.17379) [cs.CL]
* **主要学科:** 计算与语言 (`cs.CL`)
* **次要学科:** 人工智能 (`cs.AI`)
* **提交日期:** 2026年8月18日
* **DOI:** [10.48550/arXiv.2608.17379](https://doi.org/10.48550/arXiv.2608.17379)

---

## 作者 (Authors)

* **Genghan Zhang**
* **Yixin Dong**
* **Chengze Fan**
* **Zhichen Zeng**
* **Yueming Yuan**
* **Shaowei Zhu**
* **Kunle Olukotun**

---

## 摘要 (Abstract)

我们推出了 PTXBench，这是一个用于评估和适配大语言模型（LLMs）以利用架构专用 PTX 进行 GPU 核函数优化的基准测试。PTXBench 从功能正确性、所选目标指令在运行时是否得以执行，以及在 H100 和 B200 GPU 上针对 GEMM 和注意力机制工作负载相较于前沿库的加速比等多个维度进行衡量。我们的评估表明：架构专用的 PTX 能力仍然很不均衡；在复杂的注意力机制反向传播工作负载上，成功率大幅下降，且执行目标指令并不一定能转化为具有竞争力的性能。在测试的套件中，没有任何一个被评估的模型能够始终如一地匹配前沿库。此外，我们利用监督微调对 Qwen3.6-27B 进行了适配。基于修复条件的训练改进了多项任务，但泛化能力依然不均衡；除了数据集规模之外，数据覆盖度、平衡性以及推理教师的质量同样至关重要。PTXBench 为衡量和提升 LLM 利用不断演进的 GPU 架构的能力提供了一个可审计的测试平台。

> We introduce PTXBench, a benchmark for evaluating and adapting large language models (LLMs) to use architecture-specific PTX for GPU kernel optimization. PTXBench measures functional correctness, whether selected target instructions execute at runtime, and speedup over frontier libraries across GEMM and attention workloads on H100 and B200 GPUs. Our evaluation shows that architecture-specific PTX capability remains uneven: success rates fall substantially on complex attention backward workloads, and executing the target instructions does not necessarily translate into competitive performance. No evaluated model consistently matches frontier libraries across the suite. We further adapt Qwen3.6-27B using supervised fine-tuning. Repair-conditioned training improves several tasks, but generalization remains uneven; data coverage, balance, and the quality of the reasoning teacher matter in addition to dataset size. PTXBench provides an auditable testbed for measuring and improving LLMs' ability to exploit evolving GPU architectures.

---

## 访问链接 (Access Links)

* [查看 PDF](https://arxiv.org/pdf/2608.17379)
* [HTML 版本（实验性）](https://arxiv.org/html/2608.17379v1)
* [TeX 源码](https://arxiv.org/src/2608.17379)
* [许可协议](http://creativecommons.org/licenses/by/4.0/)