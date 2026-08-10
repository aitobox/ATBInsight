---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-11
hide:
- navigation
tags:
- 语音情绪识别
- Whisper
- 降维
- 自动语音识别
- 低资源语言
title: 基于Whisper的波斯语语音情绪识别中ASR自适应与表征降维研究
---
### 文章背景与核心概要
语音情绪识别（SER）在低资源语言（如波斯语）中由于标注数据有限，依然是一个具有挑战性的课题。本文探讨了如何利用 OpenAI 的 Whisper 模型进行波斯语语音情绪识别，重点关注高效的表征降维以及特定语言的模型自适应。

研究的核心贡献在于提出了一种轻量化框架：利用主成分分析（PCA）对 Whisper 编码器提取的帧级嵌入进行降维，从而消除了对可学习投影层的需求，大幅降低了可训练参数量、训练延迟和内存消耗。此外，文章还评估了在波斯语自动语音识别（ASR）任务上对 Whisper 进行微调是否能够提升下游 SER 性能。在 ShEMO 数据集上通过说话人独立协议进行的实验表明，ASR 微调仅带来微弱的性能提升，这表明在所测试的条件下，语言自适应向情感相关表征的迁移能力有限。

---

## A Study of ASR Adaptation and Representation Dimensionality Reduction in Persian Speech Emotion Recognition Using Whisper

> # A Study of ASR Adaptation and Representation Dimensionality Reduction in Persian Speech Emotion Recognition Using Whisper

---

## Summary

> ## Summary

This paper investigates **Speech Emotion Recognition (SER)** in low-resource languages (specifically Persian), focusing on efficient representation dimensionality reduction and language-specific model adaptation using OpenAI's **Whisper** model. 

> This paper investigates **Speech Emotion Recognition (SER)** in low-resource languages (specifically Persian), focusing on efficient representation dimensionality reduction and language-specific model adaptation using OpenAI's **Whisper** model. 

Key contributions and findings include:
* **Efficient Dimensionality Reduction:** Proposing a framework where frame-level embeddings from the Whisper encoder are reduced using Principal Component Analysis (PCA). This eliminates the need for learned projection layers, significantly lowers the number of trainable parameters, reduces training latency, and decreases memory usage.
* **Architecture:** Utilizing an attention-based pooling mechanism to aggregate reduced representations, followed by a lightweight prediction head.
* **ASR Fine-Tuning Impact:** Exploring whether fine-tuning Whisper on a Persian Automatic Speech Recognition (ASR) task improves downstream SER performance. Evaluations on the **ShEMO dataset** via a speaker-independent protocol revealed that ASR fine-tuning yields only modest gains, indicating limited transfer from language adaptation to emotion-related representations under the tested conditions.

> Key contributions and findings include:
> * **Efficient Dimensionality Reduction:** Proposing a framework where frame-level embeddings from the Whisper encoder are reduced using Principal Component Analysis (PCA). This eliminates the need for learned projection layers, significantly lowers the number of trainable parameters, reduces training latency, and decreases memory usage.
> * **Architecture:** Utilizing an attention-based pooling mechanism to aggregate reduced representations, followed by a lightweight prediction head.
> * **ASR Fine-Tuning Impact:** Exploring whether fine-tuning Whisper on a Persian Automatic Speech Recognition (ASR) task improves downstream SER performance. Evaluations on the **ShEMO dataset** via a speaker-independent protocol revealed that ASR fine-tuning yields only modest gains, indicating limited transfer from language adaptation to emotion-related representations under the tested conditions.

---

## Article Metadata

> ## Article Metadata

* **arXiv ID:** [`arXiv:2608.05165`](https://arxiv.org/abs/2608.05165) [cs.CL]
* **Primary Subject:** Computation and Language (`cs.CL`)
* **Other Subjects:** Artificial Intelligence (`cs.AI`), Machine Learning (`cs.LG`), Sound (`cs.SD`)
* **Authors:** Ali Shendabadi, Parnia Izadirad, Mostafa Salehi
* **Submission Date:** May 26, 2026 (Last revised: August 7, 2026)
* **Length:** 6 pages
* **License:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-nc-sa/4.0/) [![license icon](./images/079cd8198ba3.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

> * **arXiv ID:** [`arXiv:2608.05165`](https://arxiv.org/abs/2608.05165) [cs.CL]
> * **Primary Subject:** Computation and Language (`cs.CL`)
> * **Other Subjects:** Artificial Intelligence (`cs.AI`), Machine Learning (`cs.LG`), Sound (`cs.SD`)
> * **Authors:** Ali Shendabadi, Parnia Izadirad, Mostafa Salehi
> * **Submission Date:** May 26, 2026 (Last revised: August 7, 2026)
> * **Length:** 6 pages
> * **License:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-nc-sa/4.0/) [![license icon](./images/079cd8198ba3.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

---

## Abstract

> ## Abstract

语音情绪识别（SER）在低资源语言中由于标注数据有限，依然是一个具有挑战性的问题。在这项工作中，我们研究了使用 Whisper 进行波斯语 SER 的方法，特别关注表征降维和特定语言的模型自适应。

> Speech Emotion Recognition (SER) in low-resource languages remains a challenging problem due to limited labeled data. In this work, we study the use of Whisper for Persian SER with a particular focus on representation dimensionality reduction and language-specific model adaptation. 

我们提出了一种 SER 框架，其中利用主成分分析（PCA）对从 Whisper 编码器中提取的帧级嵌入进行降维，从而消除了对可学习投影层的需求，并大幅减少了可训练参数的数量。降维后的表征通过基于注意力的池化机制进行聚合，并使用轻量级预测头进行分类。

> We propose a SER framework in which frame-level embeddings extracted from the Whisper encoder are reduced in dimensionality using PCA, eliminating the need for learned projection layers and substantially reducing the number of trainable parameters. The reduced representations are aggregated using an attention-based pooling mechanism and classified with a lightweight prediction head. 

此外，我们研究了在波斯语自动语音识别（ASR）任务上对 Whisper 进行微调是否能改善下游的 SER 性能。在 ShEMO 数据集上基于说话人独立评估协议进行的实验表明，基于 PCA 的降维在提高训练效率和降低内存消耗的同时，一致地提升了情绪识别性能。ASR 微调对 SER 仅带来微弱的提升，这表明在所评估的条件下，语言自适应向情感相关表征的迁移十分有限。这些发现为在低资源语言情绪识别中高效使用大型预训练语音模型提供了实用的见解。

> In addition, we investigate whether fine-tuning Whisper on a Persian automatic speech recognition (ASR) task improves downstream SER performance. Experiments conducted on the ShEMO dataset under a speaker-independent evaluation protocol show that PCA-based dimensionality reduction consistently improves emotion recognition performance while reducing training latency and memory usage. ASR fine-tuning yields only modest gains for SER, suggesting limited transfer from language adaptation to emotion-related representations under the evaluated conditions. These findings provide practical insights into the efficient use of large pretrained speech models for emotion recognition in low-resource languages.

---

## Access & Resources

> ## Access & Resources

* **全文链接：** 
  * [查看 PDF](https://arxiv.org/pdf/2608.05165)
  * [HTML 版本（实验性）](https://arxiv.org/html/2608.05165v2)
  * [TeX 源码](https://arxiv.org/src/2608.05165)
* **引用与参考文献：**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.05165)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.05165)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.05165)
* **代码与相关工具：** 通过 [Hugging Face](https://huggingface.co/huggingface)、[Connected Papers](https://www.connectedpapers.com/about) 以及 [CatalyzeX](https://www.catalyzex.com) 探索相关的代码库、演示和文献计量工具。

> * **Full-Text Links:** 
>   * [View PDF](https://arxiv.org/pdf/2608.05165)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.05165v2)
>   * [TeX Source](https://arxiv.org/src/2608.05165)
> * **Citations & References:**
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.05165)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.05165)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.05165)
> * **Code & Associated Tools:** Explore related code repositories, demos, and bibliographic tools via [Hugging Face](https://huggingface.co/huggingface), [Connected Papers](https://www.connectedpapers.com/about), and [CatalyzeX](https://www.catalyzex.com).