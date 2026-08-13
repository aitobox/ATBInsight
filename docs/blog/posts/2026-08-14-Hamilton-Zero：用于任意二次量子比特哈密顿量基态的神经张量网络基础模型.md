---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- 量子计算
- 基础模型
- 神经张量网络
- 变分优化
- 深度强化学习
title: Hamilton-Zero：用于任意二次量子比特哈密顿量基态的神经张量网络基础模型
---
### 文章背景与核心概要
计算复杂量子哈密顿量系统的基态是经典模拟中的一个根本性瓶颈。本文引入了 **Hamilton-Zero**，这是一个包含约 **5亿个变分参数** 的神经张量网络基础模型。通过采用适配自大语言模型和深度强化学习的先进技术进行训练，该模型实现了在通用哈密顿量集合上对量子基态学习的摊销（amortization）。

通过将自旋-$1/2$ 量子基态学习重新表述为流形变分优化，作者绕过了传统的显式向量振幅，在包含多达 **8,100个量子比特** 的系统上评估并实现了可扩展的性能。这项工作将过去一个世纪的多体物理文献与现代人工智能技术深度融合，为求解大规模量子系统基态开辟了新路径。

---

## 执行摘要 (Executive Summary)

计算经典模拟方法无法企及的哈密顿系统基态，是有用量子优势的核心承诺。本文证明，通过一个拥有约 0.5 亿个变分参数的基础模型，利用大语言模型和深度强化学习的现代技术进行训练，可以有效地在任意且通用的哈密顿量集合上摊销这一问题。

> Computing the ground states of complex quantum Hamiltonian systems is a fundamental bottleneck in classical simulation. This paper introduces **Hamilton-Zero**, a neural tensor-network foundation model containing approximately **0.5 billion variational parameters**. Trained using advanced techniques adapted from large language models and deep reinforcement learning, the model amortizes quantum ground-state learning across a universal set of Hamiltonians. By reformulating spin-$1/2$ quantum ground-state learning as a manifold variational optimization, the authors bypass traditional explicit vector amplitudes, achieving scalable performance evaluated on systems containing up to **8,100 qubits**.

---

## 摘要 (Abstract)

为此，我们将自旋-$1/2$ 量子基态学习表述为 $\mathrm{SU}(2)^N$ 上中心奇标量函数（centrally odd scalar functions）的流形变分优化。这取代了显式的希尔伯特空间向量振幅，使哈密顿量能够通过李导数（Lie derivatives）作用于流形函数上，并通过自定义自动微分原语进行评估。我们利用 Peter-Weyl 定理证明了该流形上得到的变分原理保留了自旋-$1/2$ 扇区的基态上限，随后在一个包含数十万个不同哈密顿系统的数据集上预训练了我们的基础模型，这些系统涵盖了不同的连接拓扑、系统尺寸、相互作用类型和强度，从而汇集了长达一个世纪的多体物理文献。

> A central promise of useful quantum advantage is the ability to compute ground states of Hamiltonian systems beyond the reach of classical simulation methods. Here we demonstrate that this problem can be effectively amortized across an arbitrary and universal set of Hamiltonians by a foundation model with $\sim0.5$B variational parameters, trained with contemporary techniques from large language models and deep reinforcement learning. 

> To do this, we formulate $\text{spin-}1/2$ quantum ground-state learning as manifold variational optimisation over centrally odd scalar functions on $\mathrm{SU}(2)^N$. This replaces explicit Hilbert-space vector amplitudes with manifold functions on which the Hamiltonian acts through Lie derivatives, evaluated by custom automatic differentiation primitives. We prove that the resulting variational principle on this manifold preserves the $\text{spin-}1/2$ sector's ground-state upper bound using the Peter-Weyl theorem, then pre-train our foundation model on a dataset of hundreds of thousands of different Hamiltonian systems, varying the connection topology, system size, interaction types and strengths, bringing together a century of many-body literature. 

利用新型 $\mathrm{SU}(2)$ 副本交换朗之万采样器（replica-exchange Langevin sampler）和分片自然梯度优化（sharded natural-gradient optimisation），我们使用自己扩展的克罗内克因子近似曲率（KFAC）优化器，在多达 64 个量子比特的系统尺寸上训练了模型。在一个保留的泛化数据集上，我们在多达 1024 个量子比特的系统尺寸上对模型进行了微调，并在多达 8100 个量子比特的系统上进行了评估。

> Using a novel $\mathrm{SU}(2)$ replica-exchange Langevin sampler and sharded natural-gradient optimisation, we train our model with our own extension of the Kronecker-Factored Approximate Curvature (KFAC) optimiser on system sizes up to 64 qubits. On a held-out generalisation dataset, we fine-tune our model on system sizes of up to 1024 qubits, and evaluate on systems up to 8100 qubits.

---

## 核心方法亮点 (Key Methodological Highlights)

* **流形变分优化：** 将自旋-$1/2$ 量子基态重新表述为 $\mathrm{SU}(2)^N$ 上中心奇标量函数的变分优化，利用李导数通过自定义自动微分进行哈密顿量评估。
* **理论基础：** 利用 Peter-Weyl 定理在数学上保证了自旋-$1/2$ 扇区内基态上限的保持。
* **大规模预训练：** 在包含数十万种不同哈密顿量配置的海量数据上进行训练，涵盖不同的拓扑结构、规模和相互作用参数。
* **先进的优化基础设施：** 采用 $\mathrm{SU}(2)$ 副本交换朗之万采样器、分片自然梯度优化以及扩展的克罗内克因子近似曲率（KFAC）优化器。
* **卓越的可扩展性：** 在多达 64 个量子比特的系统上进行预训练，在多达 1,024 个量子比特的系统上进行微调，并成功评估了扩展至 **8,100 个量子比特** 的系统。

> * **Manifold Variational Optimization:** Reformulates $\text{spin-}1/2$ quantum ground states over centrally odd scalar functions on $\mathrm{SU}(2)^N$, using Lie derivatives for Hamiltonian evaluation via custom automatic differentiation.
> * **Theoretical Foundation:** Leverages the Peter-Weyl theorem to mathematically guarantee the preservation of the ground-state upper bound within the $\text{spin-}1/2$ sector.
> * **Massive Scale Pre-training:** Trained on hundreds of thousands of diverse Hamiltonian configurations encompassing varied topologies, sizes, and interaction parameters.
> * **Advanced Optimization Infrastructure:** Employs an $\mathrm{SU}(2)$ replica-exchange Langevin sampler, sharded natural-gradient optimization, and an extended Kronecker-Factored Approximate Curvature (KFAC) optimizer.
> * **Exceptional Scalability:** Pre-trained on up to 64 qubits, fine-tuned up to 1,024 qubits, and successfully evaluated on systems scaling up to **8,100 qubits**.

---

## 访问论文与资源 (Access Paper & Resources)

* **PDF：** [查看 PDF](https://arxiv.org/pdf/2608.11911)
* **HTML 版本：** [arXiv HTML（实验性）](https://arxiv.org/html/2608.11911v1)
* **TeX 源码：** [下载源码](https://arxiv.org/src/2608.11911)
* **DOI：** [10.48550/arXiv.2608.11911](https://doi.org/10.48550/arXiv.2608.11911)

> * **PDF:** [View PDF](https://arxiv.org/pdf/2608.11911)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.11911v1)
> * **TeX Source:** [Download Source](https://arxiv.org/src/2608.11911)
> * **DOI:** [10.48550/arXiv.2608.11911](https://doi.org/10.48550/arXiv.2608.11911)