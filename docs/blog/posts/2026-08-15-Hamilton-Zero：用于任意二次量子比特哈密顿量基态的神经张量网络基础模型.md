---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-15
hide:
- navigation
tags:
- 量子多体物理
- 基础模型
- 神经张量网络
- 变分优化
- 深度强化学习
title: Hamilton-Zero：用于任意二次量子比特哈密顿量基态的神经张量网络基础模型
---
### 文章背景与核心概要
在量子多体物理中，计算超出经典模拟能力边界的哈密顿系统基态是实现实用量子优势的核心承诺之一。本文提出的 Hamilton-Zero 模型引入了一种范式转变，它是一个包含约 5 亿个变分参数的神经张量网络基础模型，旨在高效计算任意通用二次量子比特哈密顿量的基态，并通过在大规模系统集上的预训练实现计算成本的分摊。

该技术的核心创新在于将 $\text{spin-1/2}$ 量子基态学习建模为 $\mathrm{SU}(2)^N$ 上中心奇标量函数的流形变分优化。模型利用李导数代替显式的希尔伯特空间向量振幅，并通过 Peter-Weyl 定理在理论上保证了变分原理能够维持基态上限。结合 $\mathrm{SU}(2)$ 副本交换朗之万采样器（replica-exchange Langevin sampler）以及基于自定义 KFAC 扩展的分片自然梯度优化，研究团队在多达 64 个量子比特的系统上完成了预训练，并成功将模型微调扩展至 1024 个量子比特，并在高达 8100 个量子比特的系统上进行了评估，展现出强大的泛化与扩展性能。

---

# Hamilton-Zero: A Neural Tensor-Network Foundation Model for Ground States of Arbitrary Quadratic Qubit Hamiltonians

**arXiv:** [2608.11911](https://arxiv.org/abs/2608.11911) [quant-ph]  
**Authors:** Timothy Heightman, Elena Orlova, Philip Mantrov, Aleksei Ustimenko  
**Submitted:** August 12, 2026 (Revised: August 13, 2026)  
**Primary Subject:** Quantum Physics (`quant-ph`)  
**Other Subjects:** Disordered Systems and Neural Networks (`cond-mat.dis-nn`), Strongly Correlated Electrons (`cond-mat.str-el`), Artificial Intelligence (`cs.AI`)

---

## Summary

**Hamilton-Zero** introduces a paradigm shift in quantum many-body physics by presenting a neural tensor-network foundation model containing $\sim0.5$ billion variational parameters. Designed to compute the ground states of arbitrary and universal quadratic qubit Hamiltonians, the model leverages contemporary techniques from large language models and deep reinforcement learning to amortize computational costs across massive sets of systems. 

Key innovations include:
* **Manifold Variational Optimization:** Formulates $\text{spin-}1/2$ quantum ground-state learning over centrally odd scalar functions on $\mathrm{SU}(2)^N$, replacing explicit Hilbert-space vector amplitudes with manifold functions acted upon by Lie derivatives.
* **Theoretical Guarantees:** Proves via the Peter-Weyl theorem that the variational principle preserves the $\text{spin-}1/2$ sector's ground-state upper bound.
* **Large-Scale Training:** Pre-trained on hundreds of thousands of diverse Hamiltonian systems (varying topology, size, and interaction strengths) using an $\mathrm{SU}(2)$ replica-exchange Langevin sampler and sharded natural-gradient optimization with a custom Kronecker-Factored Approximate Curvature (KFAC) extension.
* **Scaling Performance:** Demonstrates successful fine-tuning on held-out datasets up to 1,024 qubits and evaluation on systems reaching up to 8,100 qubits.

---

## Abstract

> A central promise of useful quantum advantage is the ability to compute ground states of Hamiltonian systems beyond the reach of classical simulation methods. Here we demonstrate that this problem can be effectively amortized across an arbitrary and universal set of Hamiltonians by a foundation model with $\sim0.5$B variational parameters, trained with contemporary techniques from large language models and deep reinforcement learning. To do this, we formulate $\text{spin-}1/2$ quantum ground-state learning as manifold variational optimisation over centrally odd scalar functions on $\mathrm{SU}(2)^N$. This replaces explicit Hilbert-space vector amplitudes with manifold functions on which the Hamiltonian acts through Lie derivatives, evaluated by custom automatic differentiation primitives. We prove that the resulting variational principle on this manifold preserves the $\text{spin-}1/2$ sector's ground-state upper bound using the Peter-Weyl theorem, then pre-train our foundation model on a dataset of hundreds of thousands of different Hamiltonian systems, varying the connection topology, system size, interaction types and strengths, bringing together a century of many-body literature. Using a novel $\mathrm{SU}(2)$ replica-exchange Langevin sampler and sharded natural-gradient optimisation, we train our model with our own extension of the Kronecker-Factored Approximate Curvature (KFAC) optimiser on system sizes up to 64 qubits. On a held-out generalisation dataset, we fine-tune our model on system sizes of up to 1024 qubits, and evaluate on systems up to 8100 qubits.

---

## Submission History

* **[v1]** Wed, 12 Aug 2026 10:42:38 UTC (5,487 KB)
* **[v2]** Thu, 13 Aug 2026 13:29:22 UTC (5,446 KB) — *This version*

---

## Access & Resources

* **Full-Text Links:** [View PDF](https://arxiv.org/pdf/2608.11911) | [HTML (Experimental)](https://arxiv.org/html/2608.11911v2) | [TeX Source](https://arxiv.org/src/2608.11911)
* **DOI:** [10.48550/arXiv.2608.11911](https://doi.org/10.48550/arXiv.2608.11911)
* **External References:** [INSPIRE HEP](https://inspirehep.net/arxiv/2608.11911) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.11911) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.11911) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.11911)