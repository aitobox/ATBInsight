---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- Transformer
- 注意力机制
- 标记动力学
- OAttention
- 深度学习
title: 从注意力掩码到惯性零向量标记：OAttention 与 O-Closure 标记动力学
---
### 文章背景与核心概要

传统的注意力掩码（Attention Masks）主要作为关系层面的控制手段，用于规定查询（Query）与源（Source）之间的交互权限，但它们无法提供一种在注意力边界处能够自动转为“非参与”状态的表征载体。本文提出了一种名为 OAttention 和 O-Closure 的新型标记动力学框架，通过为每个标记的隐藏载体 $h_i$ 分配一个活跃存在系数 $p_i = \frac{\|h_i\|^2}{\tau + \|h_i\|^2}$，实现了对标记参与度的动态控制。

该系数具有双重作用：既能门控标记所发出的信息，又能确定该标记在共享计算中所占的权重。通过集成支持耦合注意力（support-coupled attention）、局部 O-组件以及组合闭包（OTransformer），该框架确保了精确的零接收者、零源插入及空支持属性。研究通过契约测试和对预训练回归模型的零微调改造验证了其有效性，展示了该机制在保持计算精确性和路径兼容性方面的潜力。

---

## 摘要

注意力掩码是关系层面的控制手段：它们指定了哪些查询-源对可以进行交互。它们并未提供一种在注意力边界处表现为“非参与”状态的表征载体。我们为每个标记的隐藏载体 $h_i$ 分配了一个活跃存在系数 $p_i=\lVert h_i\rVert^2/(\tau+\lVert h_i\rVert^2)$。该系数具有双重作用：它门控由标记 $i$ 发出的信息，并决定了标记 $i$ 进入与其他标记共享计算时的质量（权重）。

> Attention masks are relation-level controls: they specify which query–source pairs may interact. They do not provide a representation-carried token state that is non-participating at the attention boundary. We assign each token hidden carrier $h_i$ an active-presence coefficient $p_i=\lVert h_i\rVert^2/(\tau+\lVert h_i\rVert^2)$. The same coefficient has two roles: it gates information emitted by token $i$, and it determines the mass with which token $i$ enters computations shared with other tokens.

**OAttention** 是实现该规则的支持耦合注意力机制。它通过 $p_i$ 对接收者输出进行门控，并在注意力分子和分母（分区）中通过 $p_j$ 对源 $j$ 进行加权，同时保留了标准的评分、可见性关系、指数竞争和值聚合。这使得零向量标记成为零元素，并产生了精确的零接收者、零源插入、自注意力插入和空支持属性。相同的标记级存在性赋予了局部 O-组件（OFFN、ONorm 和 OInject）、存在加权的 OStandardize、O-Closure 定律 $M(H\oplus0)=M(H)\oplus0$，以及通过残差和组合闭包构成的 OTransformer。

> **OAttention** is the support-coupled attention realization of this rule. It gates the receiver output by $p_i$ and weights source $j$ by $p_j$ in both the attention numerator and partition, while retaining the standard score, visibility relation, exponential competition, and value aggregation. This makes the zero-vector token a zero element and yields exact null-receiver, null-source insertion, self-attention insertion, and empty-support properties. The same token-level presence gives local O-components (OFFN, ONorm, and OInject), presence-weighted OStandardize, the O-Closure law $M(H\oplus0)=M(H)\oplus0$, and an OTransformer by residual and compositional closure.

该规范算子通过了契约测试和 GPU 评估。在对克隆的预训练 TabPFN v3 回归模型进行零微调改造中，校准后的隐藏载体 OAttention 和 Full-O 变体在 18 个匹配的数据集-种子案例中，平均 RMSE 分别变化了 $+0.088\%$ 和 $+0.177\%$。两块消融实验表明，仅使用 OAttention 无法通过普通宿主组件保持 NULL 状态，而 OTransformer 路径则可以。这些是针对精确性、活跃路径兼容性和组合必要性的范围测试；它们并未确立通用的无损性、任意宿主闭包、对原点的学习吸引力或缺失值的通用语义。

> The canonical operator is checked by contract tests and a GPU evaluation. In a zero-fine-tuning retrofit of a cloned pretrained TabPFN v3 regressor, calibrated hidden-carrier OAttention and Full-O variants change mean RMSE by $+0.088\%$ and $+0.177\%$, respectively, over 18 matched dataset–seed cases. A two-block ablation shows that OAttention alone does not preserve a NULL state through ordinary host components, whereas the OTransformer path does. These are scoped tests of exactness, active-path compatibility, and compositional necessity; they do not establish universal no-loss, arbitrary-host closure, learned attraction to the origin, or a general semantics for missing values.

---

## 链接与资源

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2608.21174) | [HTML (实验性)](https://arxiv.org/html/2608.21174v1)
* **源代码与数据：** [TeX 源码](https://arxiv.org/src/2608.21174)
* **外部文献工具：** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.21174)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.21174)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.21174)

---
*许可协议：[知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/)* <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/>