---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-11
hide:
- navigation
tags:
- RAG
- 不确定性估计
- 大语言模型
- 幻觉检测
- 机制可解释性
title: INTRYGUE：基于归纳感知的熵门控机制实现可靠的RAG不确定性估计
---
### 文章背景与核心概要
检索增强生成（RAG）虽然提升了大语言模型（LLMs）的事实准确性，但仍无法完全消除幻觉，因此可靠的不确定性量化（UQ）至关重要。本文指出了RAG设定下标准基于熵的UQ方法中存在的一个“机制悖论”：归纳头（induction heads）虽然通过复制正确答案促进了基于上下文的回答，但它会伴随触发内部的“熵神经元”。这种相互作用人为地放大了预测熵，导致模型在准确的输出上发出错误的不确定性信号。

为了克服这一问题，作者引入了 **INTRYGUE**（Induction-Aware Entropy Gating for Uncertainty Estimation，用于不确定性估计的归纳感知熵门控机制）。这是一种基于模型内部机制的方法，它根据归纳头的激活模式对预测熵进行门控调节。在四个RAG基准测试和六个开源LLM（参数量从4B到13B）上的评估表明，INTRYGUE consistently 持续匹配或超越了现有的UQ基线，证明了将预测不确定性与可解释的内部上下文利用信号相结合，能够有效赋能幻觉检测。

---

## INTRYGUE: Induction-Aware Entropy Gating for Reliable RAG Uncertainty Estimation

> INTRYGUE: Induction-Aware Entropy Gating for Reliable RAG Uncertainty Estimation

## Summary

> Summary

检索增强生成（RAG）有助于提高大语言模型（LLMs）的事实可靠性，但它并不能完全消除幻觉。因此，可靠的不确定性量化（UQ）至关重要。本文指出了RAG设置中标准基于熵的UQ方法的一个“机制悖论”：虽然归纳头通过复制正确答案来促进基于上下文的响应，但它们会附带触发内部的“entropy neurons（熵神经元）”。这种交互人为地放大了预测熵，导致模型对准确的输出发出虚假的不确定性信号。

> Retrieval-Augmented Generation (RAG) helps improve the factual reliability of Large Language Models (LLMs), but it does not completely eliminate hallucinations. Consequently, reliable Uncertainty Quantification (UQ) is essential. This paper identifies a "mechanistic paradox" in standard entropy-based UQ methods within RAG settings: while induction heads promote grounded responses by copying correct answers, they collaterally trigger internal "entropy neurons." This interaction artificially inflates predictive entropy, causing models to signal false uncertainty on accurate outputs. 

为了克服这一问题，作者推出了 **INTRYGUE**（用于不确定性估计的归纳感知熵门控机制），这是一种基于机制的方法，它根据归纳头的激活模式来门控预测熵。跨越四个RAG基准测试和六个开源LLM（参数规模从4B到13B）的评估表明，INTRYGUE 持续达到或超过了现有的UQ基线，证明了将预测不确定性与可解释的内部上下文利用信号相结合，有利于实现更有效的幻觉检测。

> To overcome this issue, the authors introduce **INTRYGUE** (Induction-Aware Entropy Gating for Uncertainty Estimation), a mechanistically grounded approach that gates predictive entropy based on the activation patterns of induction heads. Evaluations across four RAG benchmarks and six open-source LLMs (ranging from 4B to 13B parameters) demonstrate that INTRYGUE consistently matches or surpasses existing UQ baselines, proving that effective hallucination detection benefits from pairing predictive uncertainty with interpretable internal context-utilization signals.

---

## Document Metadata

> Document Metadata

* **arXiv ID:** [arXiv:2603.21607](https://arxiv.org/abs/2603.21607) [cs.AI]
> * **arXiv ID:** [arXiv:2603.21607](https://arxiv.org/abs/2603.21607) [cs.AI]
* **Subjects:** Artificial Intelligence (`cs.AI`)
> * **Subjects:** Artificial Intelligence (`cs.AI`)
* **Authors:** 
  * Alexandra Bazarova
  * Andrei Volodichev
  * Daria Kotova
  * Alexey Zaytsev
> * **Authors:** 
>   * Alexandra Bazarova
>   * Andrei Volodichev
>   * Daria Kotova
>   * Alexey Zaytsev
* **Submission History:**
  * **[v1]** Mon, 23 Mar 2026
  * **[v2]** Fri, 7 Aug 2026 *(This version)*
> * **Submission History:**
>   * **[v1]** Mon, 23 Mar 2026
>   * **[v2]** Fri, 7 Aug 2026 *(This version)*
* **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

---

## Abstract

> Abstract

尽管检索增强生成（RAG）显着提高了LLM的事实可靠性，但它并未消除幻觉，因此稳健的不确定性量化（UQ）仍然至关重要。在本文中，我们揭示了标准的基于熵的UQ方法由于机制悖论而在RAG设置中经常失效。上下文中固有的内部“拔河”现象显现：虽然归纳头通过复制正确答案来促进基于上下文的响应，但它们附带触发了先前建立的“entropy neurons（熵神经元）”。这种交互放大了预测熵，导致模型对准确的输出发出虚假的不确定性信号。

> While retrieval-augmented generation (RAG) significantly improves the factual reliability of LLMs, it does not eliminate hallucinations, so robust uncertainty quantification (UQ) remains essential. In this paper, we reveal that standard entropy-based UQ methods often fail in RAG settings due to a mechanistic paradox. An internal "tug-of-war" inherent to context utilization appears: while induction heads promote grounded responses by copying the correct answer, they collaterally trigger the previously established "entropy neurons." This interaction inflates predictive entropy, causing the model to signal false uncertainty on accurate outputs. 

为了解决这个问题，我们提出了 **INTRYGUE**（用于不确定性估计的归纳感知熵门控机制），这是一种基于机制的方法，根据归纳头的激活模式来门控预测熵。在四个RAG基准测试和六个开源LLM（4B到13B参数）上进行评估，INTRYGUE 一直匹配或优于广泛的UQ基线。我们的研究结果表明，RAG中的幻觉检测受益于将预测不确定性与可解释的内部上下文利用信号相结合。

> To address this, we propose **INTRYGUE** (Induction-Aware Entropy Gating for Uncertainty Estimation), a mechanistically grounded method that gates predictive entropy based on the activation patterns of induction heads. Evaluated across four RAG benchmarks and six open-source LLMs (4B to 13B parameters), INTRYGUE consistently matches or outperforms a wide range of UQ baselines. Our findings demonstrate that hallucination detection in RAG benefits from combining predictive uncertainty with interpretable, internal signals of context utilization.

---

## Additional Resources & Links

> Additional Resources & Links

* **Full-Text Options:** 
  * [View PDF](https://arxiv.org/pdf/2603.21607)
  * [HTML Version (Experimental)](https://arxiv.org/html/2603.21607v2)
  * [TeX Source](https://arxiv.org/src/2603.21607)
> * **Full-Text Options:** 
>   * [View PDF](https://arxiv.org/pdf/2603.21607)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2603.21607v2)
>   * [TeX Source](https://arxiv.org/src/2603.21607)
* **External Citations & Databases:**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2603.21607)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2603.21607)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2603.21607)
> * **External Citations & Databases:**
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2603.21607)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2603.21607)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2603.21607)