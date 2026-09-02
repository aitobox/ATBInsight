---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- 决策树
- Transformer
- 变分自编码器
- 模型可解释性
- ICDM 2026
title: 通过 Transformer 变分自编码器学习稀疏决策树
---
### 文章背景与核心概要
在医疗、金融等高风险应用场景中，决策树因其透明的决策逻辑而备受青睐。然而，现有的决策树学习算法通常只追求预测准确率，而往往忽视了对结构稀疏性等其他重要属性的联合优化，导致生成的模型往往过于复杂。

本文介绍了一种名为 **TREVIS** 的创新方法，它通过探索**树 Transformer 变分自编码器（Tree Transformer Variational Auto-Encoder, TTVAE）**的潜空间（latent space），实现了对决策树预测性能与结构稀疏性的联合优化。该方法将决策树映射到潜空间中，用连续空间替代了传统的离散搜索空间，从而能够通过可微分的代理模型进行高效的基于梯度的优化。

研究结果表明，TREVIS 生成的决策树不仅能够达到与现有近最优算法相媲美的预测性能，还能显著提升模型的结构稀疏性。该论文已被 **ICDM 2026** 接受。

---

## 摘要 (Abstract)

> Decision trees are among the most widely used models in machine learning, largely due to their transparent decision logic, making them well-suited for high-stakes decision-making contexts. However, most existing learning algorithms focus on predictive performance, overlooking the joint optimization of other desirable properties, such as structural sparsity.

决策树是机器学习中最广泛使用的模型之一，这主要归功于其透明的决策逻辑，使其非常适合用于高风险的决策场景。然而，大多数现有的学习算法都专注于预测性能，而忽略了对其他理想属性（如结构稀疏性）的联合优化。

> In this work, we propose **TREVIS**, an approach for learning decision trees with respect to complex objectives, based on the exploration of the latent space of a **Tree Transformer Variational Auto-Encoder (TTVAE)**. By mapping decision trees onto latent representations, TREVIS replaces the discrete search space with a continuous one, enabling gradient-based optimization via a differentiable surrogate model.

在这项工作中，我们提出了 **TREVIS**，这是一种基于探索**树 Transformer 变分自编码器（TTVAE）**潜空间来学习具有复杂目标的决策树的方法。通过将决策树映射到潜空间表征中，TREVIS 用连续空间替代了离散搜索空间，从而能够通过可微分的代理模型进行基于梯度的优化。

> We experiment with TREVIS for learning decision trees that jointly optimize predictive performance and sparsity. Results show that TREVIS discovers decision trees matching the predictive performance of existing near-optimal algorithms while improving their structural sparsity.

我们通过实验验证了 TREVIS 在联合优化预测性能和稀疏性方面的决策树学习能力。结果表明，TREVIS 发现的决策树能够匹配现有近最优算法的预测性能，同时显著改善了其结构稀疏性。

---

## 论文元数据 (Paper Metadata)

> * **arXiv Identifier:** [arXiv:2609.01430](https://arxiv.org/abs/2609.01430) [cs.LG]
* **Authors:** Giacomo Fidone, Alessio Cascione, Riccardo Guidotti
* **Primary Subject:** Machine Learning (`cs.LG`)
* **Secondary Subject:** Artificial Intelligence (`cs.AI`)
* **Submission Date:** 1 September 2026
* **Conference Acceptance:** 2026 IEEE International Conference on Data Mining (ICDM 2026)

* **arXiv 标识符：** [arXiv:2609.01430](https://arxiv.org/abs/2609.01430) [cs.LG]
* **作者：** Giacomo Fidone, Alessio Cascione, Riccardo Guidotti
* **主要学科：** 机器学习 (`cs.LG`)
* **次要学科：** 人工智能 (`cs.AI`)
* **提交日期：** 2026年9月1日
* **会议录用：** 2026 IEEE 国际数据挖掘会议 (ICDM 2026)

---

## 全文与资源 (Full-Text & Resources)

> * **PDF Version:** [View PDF](https://arxiv.org/pdf/2609.01430)
* **HTML Version:** [Experimental HTML](https://arxiv.org/html/2609.01430v1)
* **TeX Source:** [Download Source](https://arxiv.org/src/2609.01430)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

* **PDF 版本：** [查看 PDF](https://arxiv.org/pdf/2609.01430)
* **HTML 版本：** [实验性 HTML](https://arxiv.org/html/2609.01430v1)
* **TeX 源码：** [下载源码](https://arxiv.org/src/2609.01430)
* **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## 引用与参考 (Citation & References)

> * **BibTeX:** Available via the [arXiv Abstract Page](https://arxiv.org/abs/2609.01430)
* **External Citations:**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.01430)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.01430)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.01430)

* **BibTeX：** 可通过 [arXiv 摘要页面](https://arxiv.org/abs/2609.01430) 获取
* **外部引用：**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.01430)
  * [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2609.01430)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.01430)