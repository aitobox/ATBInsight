---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-11
hide:
- navigation
tags:
- 流体模拟
- 扩散模型
- Transformer
- 图神经网络
- 深度学习
title: Fluid-DiT：用于流体流动模拟学习的无图扩散Transformer
---
### 文章背景与核心概要
模拟复杂的流体流动需要捕捉完整的平衡态分布，而不仅仅是平均轨迹，但高保真求解器在计算上往往成本高昂。尽管扩散图网络（DGNs）等近期方法结合了扩散模型与图神经网络（GNNs），能够直接从非结构化网格中采样平衡态，但它们受到架构约束、感受野受限以及多尺度设计成本高昂等问题的困扰。

为了克服这些局限性，本文推出了 **Fluid-DiT**（无图扩散Transformer），这是一种创新框架，它用基于注意力的去噪机制取代了图消息传递。通过利用潜在空间公式和Transformer的全局感受野，Fluid-DiT能够有效建模混沌流体，处理局部结构和长距离相关性，而无需进行分层图粗化，从而在复杂的流体基准测试中实现了卓越的分布准确性。

---

# Fluid-DiT: Graph-Free Diffusion Transformers for Fluid Flow Simulations Learning

## Summary

Simulating complex fluid flows requires capturing full equilibrium distributions rather than just mean trajectories, yet high-fidelity solvers remain computationally prohibitive. While recent approaches like Diffusion Graph Networks (DGNs) combine diffusion models with graph neural networks (GNNs) to sample equilibrium states directly from unstructured meshes, they suffer from architectural constraints, limited receptive fields, and costly multi-scale designs. 

To overcome these limitations, this paper introduces **Fluid-DiT** (Graph-Free Diffusion Transformers), a novel framework that replaces graph message passing with attention-based denoising. By leveraging a latent-space formulation and transformers' global receptive fields, Fluid-DiT effectively models chaotic flows, handles local structures and long-range correlations without hierarchical graph coarsening, and achieves superior distributional accuracy on complex fluid benchmarks.

---

## Paper Metadata

* **arXiv Identifier:** [arXiv:2608.07161](https://arxiv.org/abs/2608.07161) [cs.LG]
* **Primary Subject:** Machine Learning (`cs.LG`)
* **Other Subjects:** Artificial Intelligence (`cs.AI`); Computational Engineering, Finance, and Science (`cs.CE`)
* **Authors:** Shentong Mo, Guolin Ke
* **Submitted:** August 7, 2026
* **DOI:** [10.48550/arXiv.2608.07161](https://doi.org/10.48550/arXiv.2608.07161)

---

## Abstract

Simulating complex fluid flows requires capturing full equilibrium distributions rather than just mean trajectories, yet high-fidelity solvers remain computationally prohibitive. Recent advances, such as Diffusion Graph Networks (DGNs), have combined diffusion models with graph neural networks to sample equilibrium states directly from unstructured meshes, enabling distributional accuracy even from short simulations. However, graph-based diffusion approaches suffer from hand-crafted architectural constraints, limited receptive fields in message passing, and costly multi-scale designs, which restrict scalability to larger and more complex domains. 

We propose **Fluid-DiT**, a Graph-Free Diffusion Transformer that replaces graph message passing with attention-based denoising, eliminating explicit graph design while preserving the ability to model distributions of chaotic flows. Our framework introduces a latent-space formulation that disentangles geometric fidelity from distributional learning, reducing high-frequency artifacts and accelerating sampling. By leveraging the transformer's global receptive field, Fluid-DiT naturally captures both local flow structures and long-range correlations without requiring hierarchical graph coarsening. On canonical benchmarks including laminar cylinder wakes, ellipse-flow systems, and turbulent 3D wing experiments, Fluid-DiT consistently outperforms graph-based diffusion baselines in both sample quality and distributional accuracy, achieving higher $R^2$ correlations and lower Wasserstein distances. Moreover, it generalizes robustly from short, incomplete trajectories to unseen Reynolds numbers and geometries, demonstrating strong scalability.

> Simulating complex fluid flows requires capturing full equilibrium distributions rather than just mean trajectories, yet high-fidelity solvers remain computationally prohibitive. Recent advances, such as Diffusion Graph Networks (DGNs), have combined diffusion models with graph neural networks to sample equilibrium states directly from unstructured meshes, enabling distributional accuracy even from short simulations. However, graph-based diffusion approaches suffer from hand-crafted architectural constraints, limited receptive fields in message passing, and costly multi-scale designs, which restrict scalability to larger and more complex domains. 
> 
> We propose **Fluid-DiT**, a Graph-Free Diffusion Transformer that replaces graph message passing with attention-based denoising, eliminating explicit graph design while preserving the ability to model distributions of chaotic flows. Our framework introduces a latent-space formulation that disentangles geometric fidelity from distributional learning, reducing high-frequency artifacts and accelerating sampling. By leveraging the transformer's global receptive field, Fluid-DiT naturally captures both local flow structures and long-range correlations without requiring hierarchical graph coarsening. On canonical benchmarks including laminar cylinder wakes, ellipse-flow systems, and turbulent 3D wing experiments, Fluid-DiT consistently outperforms graph-based diffusion baselines in both sample quality and distributional accuracy, achieving higher $R^2$ correlations and lower Wasserstein distances. Moreover, it generalizes robustly from short, incomplete trajectories to unseen Reynolds numbers and geometries, demonstrating strong scalability.

---

## Links & Resources

* **Full-Text Access:**
  * [View PDF](https://arxiv.org/pdf/2608.07161)
  * [HTML Version (Experimental)](https://arxiv.org/html/2608.07161v1)
  * [TeX Source](https://arxiv.org/src/2608.07161)
* **External Bibliographic Tools:**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.07161)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07161)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07161)

> * **Full-Text Access:**
>   * [View PDF](https://arxiv.org/pdf/2608.07161)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.07161v1)
>   * [TeX Source](https://arxiv.org/src/2608.07161)
> * **External Bibliographic Tools:**
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.07161)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07161)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07161)