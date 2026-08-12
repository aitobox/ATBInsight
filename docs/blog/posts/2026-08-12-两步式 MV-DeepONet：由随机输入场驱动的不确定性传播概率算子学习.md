---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-12
hide:
- navigation
tags:
- 算子学习
- 深度算子网络
- 不确定性量化
- 偏微分方程
- 概率建模
title: 两步式 MV-DeepONet：由随机输入场驱动的不确定性传播概率算子学习
---
### 文章背景与核心概要

在由随机输入场驱动的复杂物理系统中，前向不确定性传播往往会在场值输出中引发高度结构化的协方差。传统的概率型深度算子网络（Prob-DeepONet）虽然能通过单次前向传递预测逐点高斯均值和方差来进行轻量级不确定性量化，但其条件预测协方差被严格限制为对角形式，从而无法捕捉跨位置的空间相关性。

为了解决这一局限性，本文提出了**两步式均值-方差深度算子网络（Two-Step Mean-Variance DeepONet, 简称 two-step MV-DeepONet）**。该方法通过两大核心创新突破了传统瓶颈：一是采用“两步式训练”，将输出基底学习与输入到系数的映射解耦，并结合基底正交化与子空间旋转；二是将高斯概率建模从高维物理输出空间转移至低维旋转系数空间。通过在共享基底上映射这些概率系数，该方法能够在保持高效单次前向推理的同时，精确诱导出物理输出空间中非对角的条件预测协方差。

本文通过严格的弗罗贝尼乌斯范数（Frobenius-norm）误差分解、误差上界推导，以及在偏微分方程（PDE）基准测试和高超音速钝体气动热问题上的验证，充分展示了该方法在泛化能力、结构化不确定性区间以及精确恢复非对角相关性方面的优越表现。

---

# Two-Step MV-DeepONet: Probabilistic Operator Learning for Uncertainty Propagation Driven by Random Input Fields

## Summary

This paper introduces the **Two-Step Mean-Variance DeepONet (two-step MV-DeepONet)**, a novel probabilistic operator learning framework designed to improve uncertainty propagation in complex physical systems driven by random input fields. 

Traditional probabilistic DeepONets (Prob-DeepONet) perform lightweight uncertainty quantification by predicting pointwise Gaussian means and variances in a single forward pass, but they restrict conditional predictive covariance to a diagonal form—failing to capture cross-location spatial dependencies. The proposed two-step MV-DeepONet overcomes this limitation through two core innovations:
1. **Two-Step Training:** Decouples output-basis learning from the input-to-coefficient mapping, combined with basis orthogonalization and subspace rotation.
2. **Coefficient-Space Probabilistic Modeling:** Shifts Gaussian probabilistic modeling from the high-dimensional physical output space to the low-dimensional rotated coefficient space. 

By mapping these probabilistic coefficients through a shared basis, the method accurately induces a non-diagonal conditional predictive covariance in the physical output space while maintaining efficient single-pass inference. Rigorous Frobenius-norm error decompositions, upper bounds, and evaluations across PDE-governed benchmarks and a hypersonic blunt-body aerothermal problem demonstrate superior generalization, structured uncertainty bands, and precise recovery of off-diagonal correlations.

> 本文介绍了**两步式均值-方差 DeepONet（two-step MV-DeepONet）**，这是一种新颖的概率算子学习框架，旨在改善由随机输入场驱动的复杂物理系统中的不确定性传播。
> 
> 传统的概率型 DeepONet（Prob-DeepONet）通过在单次前向传递中预测逐点的高斯均值和方差来实现轻量级不确定性量化，但其条件预测协方差被限制为对角形式——无法捕捉跨位置的空间相关性。所提出的 two-step MV-DeepONet 通过两大核心创新克服了这一局限性：
> 1. **两步式训练：** 将输出基底的学习与输入到系数的映射解耦，并结合了基底正交化与子空间旋转。
> 2. **系数空间概率建模：** 将高斯概率建模从高维物理输出空间转移到低维旋转系数空间。
> 
> 通过通过共享基底映射这些概率系数，该方法在保持高效单次推理的同时，精确地在物理输出空间中诱导出了非对角的条件预测协方差。严格的弗罗贝尼乌斯范数误差分解、上界分析，以及在偏微分方程控制的基准测试和高超音速钝体气动热问题上的评估，均证明了其卓越的泛化能力、结构化不确定性区间以及对非对角相关性的精确恢复能力。

---

## Document Metadata

| Metadata Field | Details |
| :--- | :--- |
| **arXiv Identifier** | [arXiv:2608.09071](https://arxiv.org/abs/2608.09071) [math.NA] |
| **Title** | Two-Step MV-DeepONet: Probabilistic Operator Learning for Uncertainty Propagation Driven by Random Input Fields |
| **Authors** | Yupei Nie, Lei Wang, Jiasen Liu |
| **Primary Subject** | Numerical Analysis (`math.NA`) |
| **Secondary Subjects** | Artificial Intelligence (`cs.AI`) |
| **Submission Date** | August 10, 2026 |
| **DOI** | [10.48550/arXiv.2608.09071](https://doi.org/10.48550/arXiv.2608.09071) |

> ## 文档元数据
> 
> | 元数据字段 | 详情 |
> | :--- | :--- |
> | **arXiv 标识符** | [arXiv:2608.09071](https://arxiv.org/abs/2608.09071) [math.NA] |
> | **标题** | Two-Step MV-DeepONet: Probabilistic Operator Learning for Uncertainty Propagation Driven by Random Input Fields |
> | **作者** | Yupei Nie, Lei Wang, Jiasen Liu |
> | **主学科** | 数值分析 (`math.NA`) |
> | **辅学科** | 人工智能 (`cs.AI`) |
> | **提交日期** | 2026年8月10日 |
> | **DOI** | [10.48550/arXiv.2608.09071](https://doi.org/10.48550/arXiv.2608.09071) |

---

## Abstract

Forward uncertainty propagation in complex physical systems can induce structured covariance across field-valued outputs. For a probabilistic surrogate, the total predictive covariance comprises the covariance of conditional means across input realizations and the average conditional predictive covariance. Probabilistic DeepONet (Prob-DeepONet) provides lightweight uncertainty quantification by predicting pointwise Gaussian means and variances in a single forward pass, but its conditional predictive covariance is restricted to a diagonal form. 

To represent cross-location conditional dependence without explicitly parameterizing a full high-dimensional covariance matrix, we develop a two-step mean-variance DeepONet (two-step MV-DeepONet) through two principal modifications:
* **Decoupled Training & Subspace Alignment:** Two-step training is used to decouple output-basis learning from the input-to-coefficient mapping, together with basis orthogonalization and subspace rotation.
* **Low-Dimensional Probabilistic Modeling:** Gaussian probabilistic modeling is transferred from the high-dimensional physical output space to the low-dimensional rotated coefficient space. 

Mapping these probabilistic coefficients through the shared basis induces a generally non-diagonal conditional predictive covariance in the physical output space while retaining single-pass inference. A Frobenius-norm error decomposition and corresponding upper bound identify low-rank covariance compressibility, trunk-subspace approximation, finite-sample statistical error, and coefficient-space covariance estimation as the principal factors governing covariance recovery. 

Numerical experiments on three representative problems governed by partial differential equations (PDEs) and a hypersonic blunt-body aerothermal problem show improved generalization, more structured uncertainty bands, and accurate recovery of off-diagonal correlation patterns compared with Prob-DeepONet.

> ## 摘要
> 
> 复杂物理系统中的前向不确定性传播会在场值输出之间产生结构化协方差。对于概率代理模型而言，总预测协方差由不同输入实现下的条件均值协方差和平均条件预测协方差组成。概率型 DeepONet（Prob-DeepONet）通过在单次前向传递中预测逐点的高斯均值和方差，提供了轻量级的不确定性量化，但其条件预测协方差被限制在对角形式。
> 
> 为了在不显式参数化完整的全高维协方差矩阵的前提下表征跨位置的条件相关性，我们通过两项主要改进开发了两步式均值-方差 DeepONet（two-step MV-DeepONet）：
> * **解耦训练与子空间对齐：** 采用两步式训练将输出基底学习与输入到系数的映射解耦，并结合基底正交化与子空间旋转。
> * **低维概率建模：** 将高斯概率建模从高维物理输出空间转移至低维旋转系数空间。
> 
> 通过共享基底映射这些概率系数，该方法在保持单次前向推理的同时，能够在物理输出空间中诱导出通常为非对角的条件预测协方差。弗罗贝尼乌斯范数误差分解及相应的上界确定了低秩协方差可压缩性、主干子空间近似、有限样本统计误差以及系数空间协方差估计是决定协方差恢复质量的核心要素。
> 
> 在由偏微分方程（PDE）控制的三个代表性问题以及一个高超音速钝体气动热问题上的数值实验表明，与 Prob-DeepONet 相比，该方法展现出更好的泛化能力、更具结构化的不确定性区间以及对非对角相关模式的精确恢复能力。

---

## Access & Resources

* **Full-Text PDF:** [View PDF](https://arxiv.org/pdf/2608.09071)
* **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.09071v1)
* **TeX Source:** [Source Archive](https://arxiv.org/src/2608.09071)
* **License:** [Non-exclusive distribution license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)

> ## 访问与资源
> 
> * **全文 PDF：** [查看 PDF](https://arxiv.org/pdf/2608.09071)
> * **HTML 版本：** [arXiv HTML（实验性）](https://arxiv.org/html/2608.09071v1)
> * **TeX 源码：** [源码归档](https://arxiv.org/src/2608.09071)
> * **许可证：** [非独占分发许可证](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)