---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-07
hide:
- navigation
tags:
- 生成式模型
- 强化学习
- 流匹配
- GRPO
- 扩散模型
title: LC-GRPO：通过朗之万修正弥合基于流的 GRPO 训练与推理差距
---
### 文章背景与核心概要

LC-GRPO 是一种创新的基于流（Flow-based）的生成式相对策略优化（GRPO）框架，旨在解决扩散模型和流匹配模型中训练与推理性能不一致的问题。在当前的生成模型中，推理阶段通常依赖确定性的常微分方程（ODE）采样器，而在线强化学习训练则需要随机探索，这导致研究人员在训练时不得不使用随机微分方程（SDE）。然而，SDE 的有限步离散化往往会引入图像模糊和分布偏移。

LC-GRPO 通过结合推理对齐的 ODE 欧拉步与针对性的“随机朗之万修正”（Stochastic Langevin Correction）解决了这一难题。该方法的核心优势在于，所需的得分函数（Score function）直接从流速度（Flow velocity）中导出，无需额外的辅助得分模型，且最终的转换保持了各向同性高斯分布形式，具有可计算的似然性。在 SD3.5-Medium、FLUX.1-Dev 和 HunyuanVideo 等主流架构上的实验表明，LC-GRPO 在优化奖励的同时，有效保持了生成质量，并实现了训练与推理路径的统一。

---

## LC-GRPO：通过朗之万修正弥合基于流的 GRPO 训练与推理差距

> # LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction

### 摘要

**LC-GRPO** 是一种新颖的基于流的生成式相对策略优化（GRPO）框架，旨在消除扩散模型和流匹配模型中训练与推理之间的性能差距。虽然流模型在推理时通常依赖确定性的常微分方程（ODE）采样器，但在线强化学习需要随机探索，这导致研究人员在训练过程中使用随机微分方程（SDE）。然而，SDE 的有限步离散化经常会引入模糊和分布不匹配。

LC-GRPO 通过结合推理对齐的 ODE 欧拉步与针对性的**随机朗之万修正**解决了这一问题。关键在于，所需的得分函数直接从流速度中导出，无需辅助得分模型，且产生的转换保持了具有可处理似然性的各向同性高斯形式。对主流架构（**SD3.5-Medium**、**FLUX.1-Dev** 和 **HunyuanVideo**）的理论分析和实证评估表明，LC-GRPO 成功优化了奖励，保持了生成保真度，并统一了训练和推理路径。

> ## Summary
>
> **LC-GRPO** is a novel flow-based Generative Relative Policy Optimization (GRPO) framework designed to eliminate the train-inference performance gap in diffusion and flow-matching models. While flow models typically rely on deterministic Ordinary Differential Equation (ODE) samplers at inference, online reinforcement learning requires stochastic exploration, leading researchers to use Stochastic Differential Equations (SDEs) during training. However, finite-step discretizations of SDEs frequently introduce blurriness and distribution mismatches. 
>
> LC-GRPO resolves this by combining an inference-aligned ODE Euler step with a targeted **stochastic Langevin correction**. Crucially, the required score function is derived directly from the flow velocity without needing an auxiliary score model, and the resulting transition maintains an isotropic Gaussian form with a tractable likelihood. Theoretical analyses and empirical evaluations on prominent architectures (**SD3.5-Medium**, **FLUX.1-Dev**, and **HunyuanVideo**) demonstrate that LC-GRPO successfully optimizes rewards, preserves generation fidelity, and unifies training and inference paths.

---

## 论文元数据

* **arXiv ID:** [arXiv:2608.05600](https://arxiv.org/abs/2608.05600) [cs.LG]
* **学科分类:** 机器学习 (`cs.LG`)；人工智能 (`cs.AI`)；计算机视觉与模式识别 (`cs.CV`)
* **提交日期:** 2026年8月6日
* **作者:** Yingqing Guo, Hui Yuan, Zijian He, Mengdi Wang, Zheng Ding

> ## Paper Metadata
>
> * **arXiv ID:** [arXiv:2608.05600](https://arxiv.org/abs/2608.05600) [cs.LG]
> * **Subjects:** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`); Computer Vision and Pattern Recognition (`cs.CV`)
> * **Submission Date:** August 6, 2026
> * **Authors:** Yingqing Guo, Hui Yuan, Zijian He, Mengdi Wang, Zheng Ding

---

## 核心贡献与方法论

* **训练-推理差异：** 强调了用于策略探索的有限步 SDE 展开与确定性测试时 ODE 采样器相比，会导致样本模糊和分布漂移。
* **朗之万修正机制：** 引入了两阶段展开转换：
  1. 与推理对齐的 **ODE 欧拉步**。
  2. 针对特定时间步边缘分布的**随机朗之万修正**。
* **无得分公式化：** 利用潜在的流速度直接恢复所需的得分，消除了对单独且资源密集型得分模型的需求。
* **可处理的策略优化：** 确保最终转换保持为具有完全可处理似然性的各向同性高斯分布，适用于基于梯度的强化学习。

> ## Key Contributions & Methodology
>
> * **The Train-Inference Discrepancy:** Highlighting how finite-step SDE rollouts used for policy exploration lead to blurry samples and distribution drift compared to deterministic test-time ODE samplers.
> * **Langevin Correction Mechanism:** Introducing a two-stage rollout transition:
>   1. An inference-aligned **ODE Euler step**.
>   2. A **stochastic Langevin correction** targeting the marginal distribution at the specific timestep.
> * **Score-Free Formulation:** Leveraging the underlying flow velocity to directly recover the required score, eliminating the need for a separate, resource-intensive score model.
> * **Tractable Policy Optimization:** Ensuring that the final transition remains an isotropic Gaussian with a fully tractable likelihood suitable for gradient-based reinforcement learning.

---

## 理论亮点

* **Wasserstein 误差减少：** 作者从理论上证明，单步朗之万修正能有效减少由不完美的 ODE 欧拉步引入的 Wasserstein 误差。
* **卓越的离散化：** 在匹配随机性水平的情况下，所提出的转换比传统的反向 SDE 的欧拉-丸山（Euler–Maruyama）离散化实现了更高的精度。

> ## Theoretical Highlights
>
> * **Wasserstein Error Reduction:** The authors theoretically demonstrate that a single Langevin correction step effectively reduces the Wasserstein error introduced by an imperfect ODE Euler step.
> * **Superior Discretization:** Under matched levels of randomness, the proposed transition achieves higher accuracy than the traditional Euler–Maruyama discretization of the reverse SDE.

---

## 实验结果

在包括 **Stable Diffusion 3.5 Medium (SD3.5-Medium)**、**FLUX.1-Dev** 和 **HunyuanVideo** 在内的文本到图像和文本到视频基准测试中，广泛的评估表明 LC-GRPO：
* 持续增强了奖励优化性能。
* 保留了高频细节和结构生成质量。
* 大幅缩小了随机训练展开与确定性测试时推理之间的差距。

> ## Experimental Results
>
> Extensive evaluations across text-to-image and text-to-video benchmarks—including **Stable Diffusion 3.5 Medium (SD3.5-Medium)**, **FLUX.1-Dev**, and **HunyuanVideo**—show that LC-GRPO:
> * Consistently enhances reward optimization performance.
> * Preserves high-frequency details and structural generation quality.
> * Substantially narrows the gap between stochastic training rollouts and deterministic test-time inference.

---

## 链接与资源

* [查看 PDF](https://arxiv.org/pdf/2608.05600)
* [arXiv HTML 版本](https://arxiv.org/html/2608.05600v1)
* [TeX 源码](https://arxiv.org/src/2608.05600)
* [DOI 参考](https://doi.org/10.48550/arXiv.2608.05600)

> ## Links & Resources
>
> * [View PDF](https://arxiv.org/pdf/2608.05600)
> * [arXiv HTML Version](https://arxiv.org/html/2608.05600v1)
> * [TeX Source](https://arxiv.org/src/2608.05600)
> * [DOI Reference](https://doi.org/10.48550/arXiv.2608.05600)