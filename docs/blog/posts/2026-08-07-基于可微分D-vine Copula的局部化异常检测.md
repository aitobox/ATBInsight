---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-07
hide:
- navigation
tags:
- 异常检测
- Copula
- 可微分编程
- 不确定性量化
- 机器学习
title: 基于可微分D-vine Copula的局部化异常检测
---
### 文章背景与核心概要
Vine Copula（藤Copula）通过将复杂的多元分布层级分解为双变量成对Copula（pair-copulas），为建模复杂多元分布提供了一个灵活的框架。然而，传统的拟合过程依赖于顺序贪婪决策，容易导致全局拟合陷入次优解。为了突破这一局限，本文引入了一种全新的估计框架，将基于梯度的最大似然估计（通过完全可微分的实现方式）与束搜索（beam-search）策略相结合。

基于拟合出的D-vine模型，研究所提出的框架借助孟德斯鸠共形预测（Mondrian conformal prediction）实现了具有统计保证的局部化异常检测，从而能够识别全局异常以及针对特定变量关系的边级别（edge-level）解释。这项工作为可解释的异常检测和不确定性量化提供了强有力的工具，在基准数据集和真实世界数据集上均表现出卓越的有效性。

---

## 局部化异常检测与可微分D-vine Copulas
## Localized Anomaly Detection via Differentiable D-vine Copulas

### 摘要
Vine copulas提供了一个灵活的框架，通过将复杂的多元分布层级分解为双变量成对copula来对其进行建模。拟合D-vine需要从编码不同依赖模式的候选集中，为每个成对copula选择一个copula族和参数配置。随着变量数量和候选copula族的增加，可能的配置数量呈组合级数增长。

> Vine copulas provide a flexible framework for modeling complex multivariate distributions through a hierarchical decomposition into bivariate pair-copulas. Fitting a D-vine requires selecting a copula family and parameter configuration for each pair-copula from a set of candidates encoding different dependence patterns. As the number of variables and candidate families increases, the number of possible configurations grows combinatorially.

现有的拟合程序通过顺序贪婪决策来应对这一挑战，在每一步确定单一的局部最优族，并可能丢弃能够产生更好全局拟合的配置。为了克服这一局限性，我们提出了一种新的估计框架，结合了：
1. **基于梯度的最大似然估计**，由我们的完全可微分实现提供支持。
2. **束搜索（beam-search）策略**，在整个拟合过程中维护多个竞争的D-vine配置。

> Existing fitting procedures address this challenge through sequential greedy decisions, committing to a single locally optimal family at each step and potentially discarding configurations that would yield a better global fit. To overcome this limitation, we propose a novel estimation framework that combines:
> 1. **Gradient-based maximum likelihood estimation**, enabled by our fully differentiable implementation.
> 2. **A beam-search strategy** that maintains multiple competing D-vine configurations throughout the fitting process.

这种设计允许在保持计算可行性的同时对配置空间进行更广泛的探索。在拟合的D-vine基础之上，我们引入了一个局部化异常检测框架，该框架利用层级分解来产生全局异常得分和边级别的解释。统计保证通过孟德斯鸠共形预测（Mondrian conformal prediction）来提供，而成对copula结构则能够将异常定位到特定的变量关系中。我们在基准数据集和真实世界数据集上评估了所提出的框架，证明了其在具有不确定性量化的可解释异常检测方面的有效性。

> This design allows a broader exploration of the configuration space while remaining computationally tractable. Building on the fitted D-vine, we introduce a localized anomaly detection framework that exploits the hierarchical decomposition to produce both global anomaly scores and edge-level explanations. Statistical guarantees are provided through Mondrian conformal prediction, while the pair-copula structure enables the localization of anomalies to specific variable relationships. We evaluate the proposed framework on both benchmark and real-world datasets, demonstrating its effectiveness for interpretable anomaly detection with uncertainty quantification.

---

## 元数据与出版详情
## Metadata & Publication Details

* **arXiv ID:** [arXiv:2607.25020](https://arxiv.org/abs/2607.25020) [cs.AI]
* **学科分类 (Subjects):** 人工智能 (`cs.AI`)
* **作者 (Authors):** 
  * Nicholas Andrea Pearson
  * Francesca Zanello
  * Davide Russo
  * Luca Bortolussi
  * Francesca Cairoli
* **提交时间线 (Submission Timeline):** 
  * 2026年7月27日提交 (`v1`)
  * 2026年8月6日最后修订 (`v2`)
* **备注 (Comments):** 已被ECML-PKDD会议内的CAESAR研讨会接受并呈报的论文（2026年9月，那不勒斯）
* **许可证 (License):** [知识共享 署名-相同方式共享 4.0 国际](http://creativecommons.org/licenses/by-sa/4.0/) [![license icon](https://arxiv.org/abs/2607.25020v2)<!-- image link placeholder -->](./images/5283893486a4.png)

> * **arXiv ID:** [arXiv:2607.25020](https://arxiv.org/abs/2607.25020) [cs.AI]
> * **Subjects:** Artificial Intelligence (`cs.AI`)
> * **Authors:** 
>   * Nicholas Andrea Pearson
>   * Francesca Zanello
>   * Davide Russo
>   * Luca Bortolussi
>   * Francesca Cairoli
> * **Submission Timeline:** 
>   * Submitted on 27 Jul 2026 (`v1`)
>   * Last revised on 6 Aug 2026 (`v2`)
> * **Comments:** Workshop paper accepted for presentation at the CAESAR workshop within ECML-PKDD (September 2026, Naples)
> * **License:** [Creative Commons Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/) [![license icon](https://arxiv.org/abs/2607.25020v2)<!-- image link placeholder -->](./images/5283893486a4.png)

---

## 访问与资源
## Access & Resources

* **全文链接 (Full-Text Links):**
  * [查看 PDF](https://arxiv.org/pdf/2607.25020)
  * [HTML 版本（实验性）](https://arxiv.org/html/2607.25020v2)
  * [TeX 源码](https://arxiv.org/src/2607.25020)
* **外部书目与引用工具 (External Bibliographic & Citation Tools):**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2607.25020)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2607.25020)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2607.25020)

> * **Full-Text Links:**
>   * [View PDF](https://arxiv.org/pdf/2607.25020)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2607.25020v2)
>   * [TeX Source](https://arxiv.org/src/2607.25020)
> * **External Bibliographic & Citation Tools:**
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2607.25020)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2607.25020)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2607.25020)