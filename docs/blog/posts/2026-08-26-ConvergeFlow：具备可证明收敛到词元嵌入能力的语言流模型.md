---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 流模型
- 语言模型
- 连续扩散模型
- 词元嵌入
- 流匹配
title: ConvergeFlow：具备可证明收敛到词元嵌入能力的语言流模型
---
### 文章背景与核心概要
当前的连续扩散和基于流的语言模型在性能上已经能够与离散语言模型相媲美，但它们普遍存在一个核心局限：由于流轨迹无法保证终止于有效的词元（token）嵌入，因此高度依赖交叉熵（CE）监督的解码器。为了解决这一痛点，本文提出了 **ConvergeFlow**。该模型将数据预测器约束在词元嵌入的凸包（convex hull）之内，并仅利用由流匹配派生出的均方误差（MSE）目标进行训练。

在适当的正则化条件下，ConvergeFlow 能够在存在预测器误差的情况下，理论上证明所生成的流可以收敛到有效的词元嵌入，从而无需依赖交叉熵监督的解码器便可直接进行词元预测。此外，研究团队还开发了三种采样机制，用于在生成困惑度（perplexity）和熵（entropy）之间进行权衡控制。在 OpenWebText 数据集上的实验表明，ConvergeFlow 的性能与现有的连续和离散扩散语言模型相当，充分展现了基于流的模型范式在语言建模领域的巨大潜力。

---

# ConvergeFlow: Language Flow with Provable Convergence to Token Embeddings

> # ConvergeFlow: Language Flow with Provable Convergence to Token Embeddings

## Summary

> ## Summary

**ConvergeFlow** is an embedding-space flow-based language model that addresses a key limitation of existing continuous diffusion and flow-based language models: their reliance on cross-entropy (CE) supervised decoders due to a lack of guaranteed convergence to valid token embeddings. 

> **ConvergeFlow** is an embedding-space flow-based language model that addresses a key limitation of existing continuous diffusion and flow-based language models: their reliance on cross-entropy (CE) supervised decoders due to a lack of guaranteed convergence to valid token embeddings. 

By constraining the data predictor to the convex hull of token embeddings and utilizing a mean squared error objective derived from flow matching, ConvergeFlow provably converges to valid token embeddings—even in the presence of predictor errors. This allows for direct token prediction without needing a CE-supervised decoder. Evaluated on OpenWebText, ConvergeFlow demonstrates competitive performance compared to existing continuous and discrete diffusion language models.

> By constraining the data predictor to the convex hull of token embeddings and utilizing a mean squared error objective derived from flow matching, ConvergeFlow provably converges to valid token embeddings—even in the presence of predictor errors. This allows for direct token prediction without needing a CE-supervised decoder. Evaluated on OpenWebText, ConvergeFlow demonstrates competitive performance compared to existing continuous and discrete diffusion language models.

---

> ---

## Metadata & Reference Information

> ## Metadata & Reference Information

* **arXiv ID:** [arXiv:2608.23551](https://arxiv.org/abs/2608.23551) [cs.CL]
* **DOI:** [10.48550/arXiv.2608.23551](https://doi.org/10.48550/arXiv.2608.23551)
* **Authors:** Na Li, Yuchen Jiao, Changxiao Cai, Gen Li
* **Submitted Date:** August 24, 2026
* **Primary Subject:** Computation and Language (`cs.CL`)
* **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Machine Learning (`cs.LG`), Machine Learning (`stat.ML`)
* **Code Repository:** [GitHub - Na-Li66/ConvergeFlow](https://github.com/Na-Li66/ConvergeFlow)

> * **arXiv ID:** [arXiv:2608.23551](https://arxiv.org/abs/2608.23551) [cs.CL]
> * **DOI:** [10.48550/arXiv.2608.23551](https://doi.org/10.48550/arXiv.2608.23551)
> * **Authors:** Na Li, Yuchen Jiao, Changxiao Cai, Gen Li
> * **Submitted Date:** August 24, 2026
> * **Primary Subject:** Computation and Language (`cs.CL`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Machine Learning (`cs.LG`), Machine Learning (`stat.ML`)
> * **Code Repository:** [GitHub - Na-Li66/ConvergeFlow](https://github.com/Na-Li66/ConvergeFlow)

---

> ---

## Abstract

> ## Abstract

Recent advances in continuous diffusion and flow-based language models (LMs) have achieved performance competitive with discrete LMs. However, existing continuous frameworks still rely on decoders supervised with cross entropy (CE) because the flow trajectories are not guaranteed to terminate at valid token embeddings. Motivated by this limitation, we introduce **ConvergeFlow**, an embedding-space flow-based LM, which constrains the data predictor to the convex hull of token embeddings and trains it solely with the mean squared error objective induced by flow matching. Under suitable regularity conditions, we prove that the resulting flow converges to valid token embeddings despite errors in the data predictor, enabling direct token prediction without a CE-supervised decoder. We further develop three sampling mechanisms for controlling the trade-off between the generative perplexity and entropy. Experiments on OpenWebText demonstrate that ConvergeFlow achieves performance competitive with existing continuous and discrete diffusion LMs. These findings demonstrate the potential of the flow-based paradigm for language modeling.

> Recent advances in continuous diffusion and flow-based language models (LMs) have achieved performance competitive with discrete LMs. However, existing continuous frameworks still rely on decoders supervised with cross entropy (CE) because the flow trajectories are not guaranteed to terminate at valid token embeddings. Motivated by this limitation, we introduce **ConvergeFlow**, an embedding-space flow-based LM, which constrains the data predictor to the convex hull of token embeddings and trains it solely with the mean squared error objective induced by flow matching. Under suitable regularity conditions, we prove that the resulting flow converges to valid token embeddings despite errors in the data predictor, enabling direct token prediction without a CE-supervised decoder. We further develop three sampling mechanisms for controlling the trade-off between the generative perplexity and entropy. Experiments on OpenWebText demonstrate that ConvergeFlow achieves performance competitive with existing continuous and discrete diffusion LMs. These findings demonstrate the potential of the flow-based paradigm for language modeling.

---

> ---

## Full-Text & Resource Links

> ## Full-Text & Resource Links

* **Access Paper:** 
  * [View PDF](https://arxiv.org/pdf/2608.23551)
  * [HTML Version (Experimental)](https://arxiv.org/html/2608.23551v1)
  * [TeX Source](https://arxiv.org/src/2608.23551)
* **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) 
  <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> * **Access Paper:** 
>   * [View PDF](https://arxiv.org/pdf/2608.23551)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.23551v1)
>   * [TeX Source](https://arxiv.org/src/2608.23551)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) 
>   <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

> ---

## Citation Tools & External References

> ## Citation Tools & External References

* **Bibliographic Databases:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23551) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23551) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23551)
* **Interactive Tools & Explorers:** Bibliographic Explorer, Connected Papers, Litmaps, scite Smart Citations
* **Code & Demos:** Hugging Face, CatalyzeX Code Finder, DagsHub, Replicate, Hugging Face Spaces

> * **Bibliographic Databases:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23551) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23551) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23551)
> * **Interactive Tools & Explorers:** Bibliographic Explorer, Connected Papers, Litmaps, scite Smart Citations
> * **Code & Demos:** Hugging Face, CatalyzeX Code Finder, DagsHub, Replicate, Hugging Face Spaces