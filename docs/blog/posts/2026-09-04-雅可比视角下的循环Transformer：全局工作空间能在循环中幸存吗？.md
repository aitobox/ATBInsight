---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-04
hide:
- navigation
tags:
- Transformer
- 循环架构
- 全局工作空间
- 雅可比透镜
- 深度循环
title: 雅可比视角下的循环Transformer：全局工作空间能在循环中幸存吗？
---
### 文章背景与核心概要

标准的前馈Transformer通常在网络中部拥有一个可转换为自然语言、具强因果效力的表征带，该表征带可作为“全局工作空间（Global Workspace）”的功能类比。然而，当网络的深度不是通过静态堆叠不同的层来实现，而是通过**循环（Recurrence）**——即在多个循环中重复使用相同的权重——来实现时，这种工作空间的功能是否依然存在，这仍然是一个未解之谜。

本文通过扩展带有**虚拟展开适配器（virtual-unrolling adapter）**的雅可比透镜（Jacobian lens），对循环和深度递归的Transformer进行了深入研究。作者在三个模型上评估了工作空间的特征（透镜拟合、读出以及11类因果实验）：Ouro-2.6B、Huginn-0125以及标准基线Qwen3.6-27B。研究发现，全局工作空间确实能够在递归架构的迭代部分成功形成，但循环从根本上改变了访问该工作空间的方式：Ouro在每个循环中重建工作空间内容，而Huginn则在所有16次递归中向前维持内容。该研究为理解循环神经网络内部的表征动力学提供了重要的实证依据。

---

# 雅可比视角下的循环Transformer：全局工作空间能在循环中幸存吗？(Looped Transformers under the Jacobian Lens: Does the Global Workspace Survive Recurrence?)

**作者：** Wenlong Wang, Fergal Reid  
**提交时间：** 2026年9月4日  
**研究领域：** 人工智能 (`cs.AI`)  
**arXiv：** [2609.01924 [cs.AI]](https://arxiv.org/abs/2609.01924) | **DOI：** [10.48550/arXiv.2609.01924](https://doi.org/10.48550/arXiv.2609.01924)

---

## 📌 摘要 (Summary)

标准的前馈Transformer通常在网络中部拥有一个可转换为自然语言、具强因果效力的表征带，该表征带可作为“全局工作空间”的功能类比。然而，当网络的深度是通过**循环**（即在多个循环中重复使用相同的权重）而不是通过静态堆叠不同的层来实现时，这种工作空间的功能是否依然存在，仍然是一个未解之谜.

> Standard feedforward transformers typically feature a mid-depth band of verbalisable, causally potent representations that act as a functional analogue to a "global workspace." However, it remains an open question whether this workspace functionality persists when network depth is achieved via **recurrence**—reusing the same weights across multiple loops—rather than a static stack of distinct layers. 

本文通过扩展带有**虚拟展开适配器**的雅可比透镜，对循环和深度递归的Transformer进行了研究。作者在三个模型上评估了工作空间的特征（透镜拟合、读出以及11类因果实验）：
* **Ouro-2.6B：** 48层，循环4次并带有深度监督。
* **Huginn-0125：** 4层核心，递归16次，专为潜空间推理训练。
* **Qwen3.6-27B：** 包含64个独立层的标准基线模型。

> This paper investigates looped and depth-recurrent transformers by extending the Jacobian lens with a **virtual-unrolling adapter**. The authors evaluate workspace characteristics (lens fitting, readout, and eleven causal experiment families) across three models:
> * **Ouro-2.6B:** 48 layers looped 4 times with deep supervision.
> * **Huginn-0125:** A 4-layer core recurred 16 times, trained for latent reasoning.
> * **Qwen3.6-27B:** A standard baseline featuring 64 untied layers.

### 核心发现 (Key Findings)
* **工作空间的涌现：** 全局工作空间成功地在递归架构的迭代部分中形成。
* **访问与传输限制：** 循环从根本上改变了访问工作空间的方式：
  * *Ouro* 在每个循环中重建工作空间内容，且线性传输无法跨越循环边界传递内容（需要写入和消融操作跨越所有剩余的循环）。
  * *Huginn* 在所有16次递归中向前维持内容，而读取、写入和消融操作则在大约两次递归的滑动窗口内起作用。
* **监督与引导：** 将新注入的内容转化为自然语言的能力，与显式的逐次迭代监督直接相关，而引导现有内容的能力则不然。

> ### Key Findings
> * **Workspace Emergence:** A global workspace successfully forms within the iterated parts of recurrent architectures.
> * **Access and Transport Constraints:** Recurrence fundamentally alters how the workspace can be accessed:
>   * *Ouro* reconstructs workspace content in every loop, and linear transport cannot carry content across loop boundaries (requiring writes and ablations to span every remaining loop).
>   * *Huginn* maintains content forward across all 16 recurrences, while reads, writes, and ablations function within a sliding window of roughly two recurrences.
> * **Supervision vs. Steering:** The ability to verbalise newly injected content correlates directly with explicit per-iteration supervision, whereas the ability to steer existing content does not.

---

## 🔗 全文与资源 (Full-Text & Resources)

* **PDF：** [查看 PDF](https://arxiv.org/pdf/2609.01924)
* **HTML（实验性）：** [arXiv HTML 视图](https://arxiv.org/html/2609.01924v1)
* **TeX 源码：** [arXiv 源码下载](https://arxiv.org/src/2609.01924)
* **相关工具：** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.01924) | [谷歌学术](https://scholar.google.com/scholar_lookup?arxiv_id=2609.01924) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.01924)

> * **PDF:** [View PDF](https://arxiv.org/pdf/2609.01924)
> * **HTML (Experimental):** [arXiv HTML View](https://arxiv.org/html/2609.01924v1)
> * **TeX Source:** [arXiv Source Download](https://arxiv.org/src/2609.01924)
> * **Associated Tools:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.01924) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.01924) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.01924)