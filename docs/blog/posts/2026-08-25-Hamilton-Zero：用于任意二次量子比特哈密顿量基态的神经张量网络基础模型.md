---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- 量子计算
- 神经量子态
- 基础模型
- 张量网络
- 变分优化
title: Hamilton-Zero：用于任意二次量子比特哈密顿量基态的神经张量网络基础模型
---
### 文章背景与核心概要
本文介绍了名为 *Hamilton-Zero* 的神经张量网络基础模型，该模型包含约 5 亿个变分参数，专门用于计算任意二次量子比特哈密顿量的基态。通过将自旋-$1/2$ 量子基态学习重新表述为 $\mathrm{SU}(2)^N$ 上中心奇标量函数的流形变分优化，该模型避开了显式的希尔伯特空间向量振幅，转而利用基于李导数的求值方法和自定义自动微分基元。

作者证明了该变分原理（通过 Peter-Weyl 定理）保持了基态的上界，并通过纯态基础神经量子态（NQS）的不可能性定理（no-go theorem）提供了理论支撑。该模型在包含数十万个不同哈密顿系统的海量数据集上进行了预训练，采用了 $\mathrm{SU}(2)$ 副本交换朗之万采样器以及分片自然梯度优化（通过 KFAC 的扩展），在预训练期间可扩展至 64 个量子比特，微调可达 1024 个量子比特，并能对包含多达 8100 个量子比特的系统进行评估。

---

# Hamilton-Zero: A Neural Tensor-Network Foundation Model for Ground States of Arbitrary Quadratic Qubit Hamiltonians

**arXiv:** [2608.11911](https://arxiv.org/abs/2608.11911) [quant-ph]  
**Authors:** Timothy Heightman, Elena Orlova, Philip Mantrov, Aleksei Ustimenko  
**Submitted:** August 12, 2026 (Last revised August 20, 2026)  
**Subjects:** Quantum Physics (`quant-ph`); Disordered Systems and Neural Networks (`cond-mat.dis-nn`); Strongly Correlated Electrons (`cond-mat.str-el`); Artificial Intelligence (`cs.AI`)

---

## 📋 Summary

> *Hamilton-Zero* introduces a neural tensor-network foundation model boasting approximately 0.5 billion variational parameters designed to compute the ground states of arbitrary quadratic qubit Hamiltonians. By reformulating spin-$1/2$ quantum ground-state learning as a manifold variational optimization over centrally odd scalar functions on $\mathrm{SU}(2)^N$, the model bypasses explicit Hilbert-space vector amplitudes in favor of Lie-derivative-based evaluation using custom automatic differentiation primitives. 
>
> The authors prove that this variational principle preserves the ground-state upper bound (via the Peter-Weyl theorem) and provide a theoretical justification through a no-go theorem for pure-state foundation Neural Quantum States (NQS). Pre-trained on hundreds of thousands of diverse Hamiltonian systems using an $\mathrm{SU}(2)$ replica-exchange Langevin sampler and sharded natural-gradient optimization (via an extension of KFAC), the model scales effectively to 64 qubits during pre-training, fine-tunes up to 1024 qubits, and evaluates systems containing up to 8100 qubits.

*Hamilton-Zero* 引入了一个神经张量网络基础模型，拥有约 5 亿个变分参数，旨在计算任意二次量子比特哈密顿量的基态。通过将自旋-$1/2$ 量子基态学习重新表述为 $\mathrm{SU}(2)^N$ 上中心奇标量函数的流形变分优化，该模型绕过了显式的希尔伯特空间向量振幅，转而使用基于李导数的评估以及自定义的自动微分基元。

作者证明了该变分原理通过 Peter-Weyl 定理保留了基态上界，并通过针对纯态基础神经量子态（NQS）的不可能性定理提供了理论证明。通过使用 $\mathrm{SU}(2)$ 副本交换朗之万采样器和分片自然梯度优化（通过 KFAC 的扩展）对数以十万计的不同哈密顿系统进行预训练，该模型在预训练期间可有效地扩展到 64 个量子比特，微调可达 1024 个量子比特，并可评估包含多达 8100 个量子比特的系统。

---

## 📝 Abstract

> A central promise of useful quantum advantage is the ability to compute ground states of Hamiltonian systems beyond the reach of classical simulation methods. Here we demonstrate that this problem can be effectively amortized across an arbitrary and universal set of Hamiltonians by a foundation model with $\sim0.5$B variational parameters, trained with contemporary techniques from large language models and deep reinforcement learning. 
> 
> To do this, we formulate $\text{spin-}1/2$ quantum ground-state learning as manifold variational optimisation over centrally odd scalar functions on $\mathrm{SU}(2)^N$. This replaces explicit Hilbert-space vector amplitudes with manifold functions on which the Hamiltonian acts through Lie derivatives, evaluated by custom automatic differentiation primitives. We prove that the resulting variational principle on this manifold preserves the $\text{spin-}1/2$ sector's ground-state upper bound using the Peter-Weyl theorem and justify the choice of such a representation with a no-go theorem for pure state foundation NQS. 
> 
> We then pre-train our foundation model on a dataset of hundreds of thousands of different Hamiltonian systems, varying the connection topology, system size, interaction types and strengths, bringing together a century of many-body literature. Using a novel $\mathrm{SU}(2)$ replica-exchange Langevin sampler and sharded natural-gradient optimisation, we train our model with our own extension of the Kronecker-Factored Approximate Curvature (KFAC) optimiser on system sizes up to 64 qubits. On a held-out generalisation dataset, we fine-tune our model on system sizes of up to 1024 qubits, and evaluate on systems up to 8100 qubits.

> 有用量子优势的一个核心承诺是能够计算超出经典模拟方法范围的哈密顿系统基态。在这里，我们证明了通过一个具有约 5 亿（$\sim0.5$B）个变分参数的基础模型，利用来自大语言模型和深度强化学习的现代技术进行训练，可以在任意且通用的哈密顿量集合中有效地分摊这一问题。
> 
> 为此，我们将 $\text{spin-}1/2$ 量子基态学习表述为 $\mathrm{SU}(2)^N$ 上中心奇标量函数的流形变分优化。这取代了显式的希尔伯特空间向量振幅，转而采用流形函数，哈密顿量通过李导数作用于这些函数，并通过自定义自动微分基元进行评估。我们证明了该流形上产生的变分原理利用 Peter-Weyl 定理保留了 $\text{spin-}1/2$ 扇区的基态上界，并通过针对纯态基础 NQS 的不可能性定理证明了选择这种表示形式的合理性。
> 
> 然后，我们在一个包含数十万个不同哈密顿系统的数据集上预训练了我们的基础模型，这些系统在连接拓扑、系统规模、相互作用类型和强度上各不相同，汇集了一个世纪的多体物理文献。利用新颖的 $\mathrm{SU}(2)$ 副本交换朗之万采样器和分片自然梯度优化，我们在高达 64 个量子比特的系统规模上，使用我们对 Kronecker-Factored Approximate Curvature（KFAC）优化器的自定义扩展来训练模型。在一个保留的泛化数据集上，我们将模型微调至高达 1024 个量子比特的系统规模，并在高达 8100 个量子比特的系统上进行了评估。

---

## 🔗 Additional Resources

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.11911) | [HTML (Experimental)](https://arxiv.org/html/2608.11911v3) | [TeX Source](https://arxiv.org/src/2608.11911)
* **Persistent Identifiers:** [arXiv DOI](https://doi.org/10.48550/arXiv.2608.11911)
* **Bibliographic Tools:** [INSPIRE HEP](https://inspirehep.net/arxiv/2608.11911) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.11911) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.11911) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.11911)

> * **全文访问：** [查看 PDF](https://arxiv.org/pdf/2608.11911) | [HTML（实验性）](https://arxiv.org/html/2608.11911v3) | [TeX 源码](https://arxiv.org/src/2608.11911)
> * **持久标识符：** [arXiv DOI](https://doi.org/10.48550/arXiv.2608.11911)
> * **书目工具：** [INSPIRE HEP](https://inspirehep.net/arxiv/2608.11911) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.11911) | [谷歌学术](https://scholar.google.com/scholar_lookup?arxiv_id=2608.11911) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.11911)