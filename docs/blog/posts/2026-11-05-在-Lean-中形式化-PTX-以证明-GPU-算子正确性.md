---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-11-05
hide:
  - navigation
tags:
  - Lean
  - PTX
  - GPU算子
  - 形式化验证
  - 深度学习
title: "在 Lean 中形式化 PTX 以证明 GPU 算子正确性"
---

# 在 Lean 中形式化 PTX 以证明 GPU 算子正确性

> **arXiv:2611.04447** [cs.AI]  
> **Subjects:** Artificial Intelligence (cs.AI)  
> **Authors:** Luk Koska, Tom Koska, Ben Koska  
> **Submitted:** 3 Nov 2026  
> **DOI / Paper:** [10.48550/arXiv.2611.04447](https://doi.org/10.48550/arXiv.2611.04447)  
> **PDF:** [View PDF](https://arxiv.org/pdf/2611.04447)

### 文章背景与核心概要
随着现代深度学习模型规模的爆发式增长，底层 GPU 算子的极致性能优化往往伴随着极高的实现复杂度与难以察觉的并发逻辑缺陷。传统的单元测试和模糊测试难以穷尽所有非确定性执行路径，而形式化验证则是终结算子隐性漏洞的终极防线。本文提出了一套在 Lean 定理证明器中形式化建模 NVIDIA PTX (Parallel Thread Execution) 指令集的数学框架，开创性地支持对现代深度学习复杂 GPU 算子模式进行严密的逻辑建模与推理。研究团队成功利用该框架，针对 WGMMA GEMM 矩阵乘算子、FlashAttention 注意力机制以及三阶段混合专家 (Mixture-of-Experts, MoE) 流水线算子给出了完全的形式化功能正确性证明，为构建可信、高可靠的 AI 底层计算系统奠定了数学基石。

---

## 概述与核心成果

> ## Overview & Summary

本文由 Luk Koska、Tom Koska 和 Ben Koska 撰写（于 2026 年 11 月 3 日提交），创新性地提出了一种在 **Lean** 定理证明器中对 PTX (Parallel Thread Execution) 虚拟汇编指令进行数学形式化建模的全新框架。该方法首次实现了对现代深度学习 GPU 核心算子中常见复杂执行模式的严格建模与数学形式化推理。

> This paper, authored by Luk Koska, Tom Koska, and Ben Koska (submitted on November 3, 2026), introduces a novel framework for mathematically formalizing PTX (Parallel Thread Execution) in the **Lean** theorem prover. The approach enables rigorous modeling and reasoning about complex patterns frequently found in modern Deep Learning GPU kernels.

借助这一形式化系统，作者成功证明了以下三种关键深度学习算子实现的功能正确性：
* **WGMMA GEMM 算子** (Warp 组矩阵乘累加通用矩阵乘法)
* **FlashAttention**
* **三算子混合专家 (MoE) 流水线**

> Using this formalization, the authors successfully prove the functional correctness of implementations for:
> * **WGMMA GEMM kernels** (Warp Group Matrix Multiply-Accumulate General Matrix Multiply)
> * **FlashAttention**
> * **A 3-kernel Mixture-of-Experts (MoE) pipeline**

---

## 框架支持建模的核心硬件与编程特性

> ## Key Features Modeled in the Framework

该形式化 PTX 框架精准刻画了现代 GPU 高级编程抽象与底层硬件运行特征，涵盖：
* 获取-释放内存语义 (Acquire-release memory semantics)
* 张量核心 (Tensor cores)
* 内存代理机制 (Memory proxies)
* 异步并发操作 (Asynchronous operations)
* 多算子协同流水线 (Multi-kernel pipelines)
* 数据依赖型控制流 (Data-dependent control flow)

> The formalized PTX framework captures advanced GPU programming abstractions and hardware behaviors, including:
> * Acquire-release memory semantics
> * Tensor cores
> * Memory proxies
> * Asynchronous operations
> * Multi-kernel pipelines
> * Data-dependent control flow

---

## 论文元数据

> ## Article Metadata

* **arXiv 编号：** [arXiv:2611.04447](https://arxiv.org/abs/2611.04447) [cs.AI]
* **DOI 链接：** [10.48550/arXiv.2611.04447](https://doi.org/10.48550/arXiv.2611.04447)
* **主要学科领域：** 人工智能 (`cs.AI`)
* **提交日期：** 2026 年 11 月 3 日

> * **arXiv Identifier:** [arXiv:2611.04447](https://arxiv.org/abs/2611.04447) [cs.AI]
> * **DOI:** [10.48550/arXiv.2611.04447](https://doi.org/10.48550/arXiv.2611.04447)
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Submission Date:** November 3, 2026

---

## 全文获取链接

> ## Full-Text & Access Links

* [阅读 PDF 原文](https://arxiv.org/pdf/2611.04447)
* [实验性 HTML 在线阅读](https://arxiv.org/html/2611.04447v1)
* [TeX 源码包](https://arxiv.org/src/2611.04447)

> * [View PDF](https://arxiv.org/pdf/2611.04447)
> * [Experimental HTML Version](https://arxiv.org/html/2611.04447v1)
> * [TeX Source](https://arxiv.org/src/2611.04447)
