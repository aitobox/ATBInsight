---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- 神经模糊系统
- 双曲几何
- 可解释人工智能
- 机器学习
- 知识表示
title: HyperANFIS：通过双曲几何增强自适应神经模糊系统中的规则表示与可解释性
---
### 文章背景与核心概要
自适应神经模糊推理系统（ANFIS）因其能够生成明确的“IF-THEN”模糊规则以实现透明决策，在可解释推理领域备受推崇。然而，传统的 ANFIS 模型主要在欧几里得空间中运行，这限制了它们对复杂规则的表示能力以及预测性能。

为了克服这些局限性，本文引入了**双曲 ANFIS（HyperANFIS）**。这一创新扩展在保持传统 ANFIS 核心架构和模糊语义的同时，将规则原型学习、规则激活以及后件聚合等关键操作转移到了双曲空间中。通过利用双曲空间的几何特性，HyperANFIS 显著增强了模糊推理过程，与标准的欧几里得基线模型相比，实现了更优的预测准确率、更好的规则间协作以及更高可信度的可解释规则。

---

# HyperANFIS: Enhancing Rule Representation and Interpretability in Adaptive Neuro-Fuzzy Systems via Hyperbolic Geometry

> # HyperANFIS: Enhancing Rule Representation and Interpretability in Adaptive Neuro-Fuzzy Systems via Hyperbolic Geometry

* **arXiv ID:** [arXiv:2608.11768](https://arxiv.org/abs/2608.11768) [cs.AI]
* **Submitted:** August 12, 2026
* **Authors:** Haoran Pei, Zhao Su, Zetao Lin, Haoran Li, Jun Shen, Qi Zhu, Lan Guo, Qingguo Zhou, Binbin Yong
* **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) *(<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> view license)*

> * **arXiv ID:** [arXiv:2608.11768](https://arxiv.org/abs/2608.11768) [cs.AI]
> * **Submitted:** August 12, 2026
> * **Authors:** Haoran Pei, Zhao Su, Zetao Lin, Haoran Li, Jun Shen, Qi Zhu, Lan Guo, Qingguo Zhou, Binbin Yong
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) *(<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> view license)*

---

## Abstract Summary

> ## Abstract Summary

自适应神经模糊推理系统（ANFIS）因其能够生成明确的 **IF-THEN** 模糊规则以实现透明决策，在可解释推理领域备受推崇。然而，传统的 ANFIS 模型主要在欧几里得空间中运行，这限制了它们对复杂规则的表示能力以及预测性能。

> Adaptive Neuro-Fuzzy Inference Systems (ANFIS) are widely valued for their interpretable reasoning capabilities, achieved by generating explicit **IF-THEN** fuzzy rules for transparent decision-making. However, traditional ANFIS models operate primarily within Euclidean space, which can limit their capacity for complex rule representation and predictive performance. 

为了克服这些局限性，本文引入了**双曲 ANFIS（HyperANFIS）**。这一创新扩展在保持传统 ANFIS 核心架构和模糊语义的同时，将关键操作（例如规则原型学习、规则激活和后件聚合）转移到了双曲空间中。通过利用双曲空间的几何特性，HyperANFIS 显著增强了模糊推理过程，与标准的欧几里得基线模型相比，实现了更优的预测准确率、更好的规则间协作以及更高可信度的可解释规则。

> To overcome these constraints, this paper introduces **Hyperbolic ANFIS (HyperANFIS)**. This novel extension preserves the core architecture and fuzzy semantics of conventional ANFIS while shifting key operations—such as rule-prototype learning, rule activation, and consequent aggregation—into hyperbolic space. By leveraging the geometric properties of hyperbolic spaces, HyperANFIS significantly enhances the fuzzy inference process, resulting in superior predictive accuracy, better inter-rule collaboration, and higher credibility of its interpretable rules compared to standard Euclidean baselines.

---

## Metadata & Reference Information

> ## Metadata & Reference Information

* **Primary Subject:** Artificial Intelligence (`cs.AI`)
* **DOI:** [10.48550/arXiv.2608.11768](https://doi.org/10.48550/arXiv.2608.11768)
* **Full-Text & Access Links:**
  * [View PDF](https://arxiv.org/pdf/2608.11768)
  * [HTML Version (Experimental)](https://arxiv.org/html/2608.11768v1)
  * [TeX Source](https://arxiv.org/src/2608.11768)
* **External Citations & Tools:**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.11768)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.11768)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.11768)

> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **DOI:** [10.48550/arXiv.2608.11768](https://doi.org/10.48550/arXiv.2608.11768)
> * **Full-Text & Access Links:**
>   * [View PDF](https://arxiv.org/pdf/2608.11768)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.11768v1)
>   * [TeX Source](https://arxiv.org/src/2608.11768)
> * **External Citations & Tools:**
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.11768)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.11768)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.11768)