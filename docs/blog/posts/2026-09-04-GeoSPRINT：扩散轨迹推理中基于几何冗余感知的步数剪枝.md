---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-04
hide:
- navigation
tags:
- 扩散模型
- 模型加速
- 几何分析
- 采样调度
- 计算机视觉
title: GeoSPRINT：扩散轨迹推理中基于几何冗余感知的步数剪枝
---
### 文章背景与核心概要
扩散模型虽然能够生成高质量的样本，但由于需要进行大量连续的神经函数评估（NFE），其推理过程在计算上依然代价高昂。现有的加速技术通常依赖于刚性的跳步调度、数值自适应的局部步长，或是成本高昂的重新训练过程。

为了克服这些局限性，本文推出了 **GeoSPRINT**（轨迹推理中的几何步数剪枝），这是一个无需训练的框架，能够直接从去噪轨迹的底层几何结构中构建自适应的非均匀采样调度。该方法通过超平面性测试和曲率感知分配，在不重新训练模型的情况下显著提升了扩散采样效率，并在多个基准测试中展现出优异的性能。

---

# GeoSPRINT: Geometric Redundancy-Aware Step Pruning for Inference in Diffusion Trajectories

* **arXiv ID:** [arXiv:2609.02160](https://arxiv.org/abs/2609.02160) [cs.LG]
* **Authors:** Arpita Joshi
* **Submitted:** September 2, 2026
* **Primary Subject:** Machine Learning (`cs.LG`)
* **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) *(View license icon: ![license icon](./images/345c7ad61f1b.png))*

---

## Summary

Diffusion models generate high-quality samples, but their inference remains computationally expensive due to the requirement of numerous sequential Neural Function Evaluations (NFEs). Existing acceleration techniques often rely on rigid step-skipping schedules, numerically adaptive local step sizes, or costly retraining procedures. 

To overcome these limitations, this paper introduces **GeoSPRINT** (Geometric Step Pruning for Inference in Trajectories), a training-free framework that constructs adaptive, non-uniform sampling schedules directly from the underlying geometry of denoising trajectories. 

### Key Contributions:
1. **Hyperplanarity Testing:** GeoSPRINT identifies geometrically redundant inference steps in the latent space using a hyperplanarity test, computed efficiently via QR factorization.
2. **Curvature-Aware Allocation:** The framework translates this redundancy profile into an optimized sampling schedule that dynamically allocates more computational steps to high-curvature regions of the trajectory.
3. **Trajectory Projection Score ($\alpha_{\mathrm{traj}}$):** A residual-variance metric designed to quantify trajectory straightness, functioning as a model-free diagnostic tool for rectified flow quality.

---

## 经验结果

在相匹配的 NFE 预算下，GeoSPRINT 在多个评估基准上始终优于均匀的去噪扩散隐式模型（DDIM）调度：

> ## Empirical Results
> 
> GeoSPRINT consistently outperforms uniform Denoising Diffusion Implicit Models (DDIM) schedules across multiple evaluation benchmarks under matched NFE budgets:

* **CIFAR-10 ($32{\times}32$)：** 在 49–89 的 NFE 范围内，其 Fréchet Inception Distance (FID) 相比 DDIM 提升了 $0.7$ 到 $1.1$ 个点；尽管依赖于一阶 DDIM 求解器，但在 $\text{NFE} \geq 30$ 时成功超越了 DPM-Solver++。

> * **CIFAR-10 ($32{\times}32$):** Improves Fréchet Inception Distance (FID) by $0.7$ to $1.1$ points over DDIM across 49–89 NFEs, successfully outperforming DPM-Solver++ at $\text{NFE} \geq 30$ despite relying on a first-order DDIM solver.

* **LSUN Church ($256{\times}256$)：** 使用 52 步的预算，将 FID 得分从 $1.48$ 降低至 $1.26$。

> * **LSUN Church ($256{\times}256$):** Lowers the FID score from $1.48$ down to $1.26$ using a 52-step budget.

* **Stable Diffusion v1.5 ($512{\times}512$ latent)：** 相比标准的 DDIM 调度，带来了高达 $1.93$ 的 FID 改进。

> * **Stable Diffusion v1.5 ($512{\times}512$ latent):** Delivers up to a $1.93$ FID improvement over standard DDIM schedules.

这些发现表明，分析轨迹几何结构为步数分配提供了一个强大的全局信号，在无需重新训练模型的情况下显著提升了扩散采样效率。

> These findings demonstrate that analyzing trajectory geometry provides a powerful global signal for step allocation, significantly boosting diffusion sampling efficiency without requiring model retraining.