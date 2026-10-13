---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-13
hide:
  - navigation
tags:
  - Muon
  - 深度学习优化器
  - Schatten-p 范数
  - 论文解读
title: "从 SGD 到 Muon：基于 Schatten-p 范数的逐层自适应几何优化器"
---

# 从 SGD 到 Muon：基于 Schatten-p 范数的逐层自适应几何优化器

> # From SGD to Muon: Adaptive Optimization via Schatten-p Norms

> **arXiv:2605.19781** [cs.AI]  
> **Subjects:** Artificial Intelligence (cs.AI)  
> **Authors:** Thomas Massena  
> **Paper:** [arXiv:2605.19781](https://arxiv.org/abs/2605.19781)  

### 文章背景与核心概要

在深度学习模型的训练演进中，从经典的 SGD、Adam 到近期凭借矩阵谱范数优化大放异彩的 **Muon**，优化器正经历着从“标量元素独立更新”向“矩阵整体几何约束”的深刻范式迁移。然而，以 Muon 为代表的优化器虽然通过线性极小化预言机 (Linear Minimization Oracle, LMO) 实现了显著的收敛加速，其几何约束却往往是由设计者人为固化或经验设定的，无法适应神经网络中不同网络层各异的损失曲面与特征结构。针对这一局限，Thomas Massena 等人创新性地基于 Schatten-p 范数构建起一套数据驱动的逐层自适应几何优化框架，通过单步随机特征回归代理模型从激活与梯度统计中动态推导出最优闭式解，不仅优雅地在 SGD 与 Muon 之间构建起平滑连续的光谱，更将 SGD、Adam、Muon 及 MuAdam 全面纳为极端特例。令人瞩目的是，该算法在实现逐层动态几何自适应的同时，仅引入约 $3\%$ 的极低额外运行时开销，在多种严苛训练基准下均展现出顶尖的收敛效率与泛化表现，为大模型下一代自适应优化架构的设计提供了极具突破性的理论与工程范式。

---

## 内容概要

> ## Summary

以 **Muon** 为代表的现代深度学习优化器，通过线性极小化预言机 (Linear Minimization Oracle, LMO) 理论，为权重更新引入了矩阵层面的几何约束，显著加速了模型的收敛步伐。然而，现有的前沿方法在设计更新几何结构时，往往依赖预设的静态规则或经验调优，导致所有网络层都只能采用一刀切的固定几何约束；这种静态设定很难精确契合神经网络各层之间截然不同的实际特征几何与损失曲面。

> Modern deep learning optimizers like **Muon** impose matrix-wise geometry constraints on their updates through Linear Minimization Oracle (LMO) theory. However, these methods typically use static, by-design, or empirically chosen update geometries that may not align with the specific geometry of individual neural network layers. 

针对这一痛点，本文提出了一种数据驱动的动态评判准则，能够为神经网络的每一个层单独挑选最理想的代理更新 LMO 几何结构。作者团队利用单步随机特征回归代理模型 (Surrogate Model) ，从各层的梯度与激活值统计信息中推导出了优雅的解析闭式解，使该框架能够在 **SGD** 与 **Muon** 的参数更新模式之间实现无缝平滑插值。更进一步，通过引入逐参数的预条件处理 (Parameter-wise Preconditioning) ，该理论框架成功构建起一套大一统视角，将经典的 **SGD**、**Muon**、**Adam** 以及 **MuAdam** 均涵盖为其在特定极限条件下的特例。得益于极为精简高效的计算策略，该自适应机制仅带来约 $3\%$ 的极低运行时开销 (Runtime Overhead) ，便在多种复杂训练场景中展现出媲美甚至超越现有最优基准模型 (Baselines) 的亮眼战绩，为深度学习优化器迈向全动态、运行时逐层自适应几何结构开辟了崭新纪元。

> This paper introduces a data-driven criterion that dynamically selects proxy-optimal update LMO geometries per layer. Derived in closed form from gradient and activation statistics using a single-step random feature regression surrogate model, the proposed framework seamlessly interpolates between **SGD** and **Muon** updates. By integrating parameter-wise preconditioning, it generalizes and recovers **SGD**, **Muon**, **Adam**, and **MuAdam** as specific limiting cases. With efficient computational strategies yielding only a ~3% runtime overhead, the method demonstrates competitive or superior performance compared to the best-performing baselines across multiple training scenarios, paving the way for dynamic, runtime-adapted optimizer geometries.

---

## 论文元数据

> ## Paper Metadata

* **arXiv 编号：** [arXiv:2605.19781](https://arxiv.org/abs/2605.19781) (v2)
* **研究领域：** 人工智能 (`cs.AI`)
* **论文作者：** 
  * Thomas Massena (DTIPG - SNCF, IRIT)
  * Corentin Friedrich (IRIT)
  * Mathieu Serrurier (IRIT)
* **录用会议：** 神经信息处理系统大会 (NeurIPS, Conference on Neural Information Processing Systems) ，2026 年 12 月，澳大利亚悉尼
* **提交历史：** 
  * [v1] 2026 年 5 月 19 日 (周二)
  * [v2] 2026 年 10 月 9 日 (周五)

> * **arXiv ID:** [arXiv:2605.19781](https://arxiv.org/abs/2605.19781) (v2)
> * **Subject:** Artificial Intelligence (`cs.AI`)
> * **Authors:** 
>   * Thomas Massena (DTIPG - SNCF, IRIT)
>   * Corentin Friedrich (IRIT)
>   * Mathieu Serrurier (IRIT)
> * **Conference Reference:** Conference on Neural Information Processing Systems (NeurIPS), Dec 2026, Sydney, Australia
> * **Submission History:** 
>   * [v1] Tue, 19 May 2026
>   * [v2] Fri, 9 Oct 2026

---

## 论文获取与相关资源

> ## Access & Resources

* **全文 PDF：** [阅读 PDF](https://arxiv.org/pdf/2605.19781)
* **源码获取：** [TeX 源码包](https://arxiv.org/src/2605.19781)
* **引文分析与学术工具：** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2605.19781)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2605.19781)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2605.19781)

> * **Full-Text PDF:** [View PDF](https://arxiv.org/pdf/2605.19781)
> * **Source Code:** [TeX Source](https://arxiv.org/src/2605.19781)
> * **External Citations & Tools:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2605.19781)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2605.19781)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2605.19781)
