---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- AI文本检测
- 引导向量
- 语言模型
- 表征空间
- 深度学习
title: SV-Detect：利用引导向量进行AI生成文本检测
---
### 文章背景与核心概要
随着大语言模型的快速发展，检测AI生成文本面临着严峻的挑战，特别是当面对领域变化、源模型差异以及文本编辑攻击等分布偏移（distribution shift）情况时，传统检测方法往往表现不佳。本文介绍了一种名为SV-Detect的新型AI生成文本检测器，它利用冻结语言模型隐藏表示中提取的引导向量（steering vectors），通过构建能够区分人类编写与机器生成文本的分层方向，并将投影特征输入轻量级分类器，从而在同分布测试以及各种强力攻击下均实现了卓越的鲁棒性。

可解释性分析进一步表明，这些学到的方向不仅捕获了可识别的文体线索，还捕捉到了超越表面特征的大量底层信号，成功将AI文本检测重新定义为一个表征空间探测（representation-space probing）问题，为该领域提供了一个简单而有效的解决方案。

---

# SV-Detect: AI-generated Text Detection with Steering Vectors

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" width="16" style="vertical-align: middle; margin-right: 4px;" /> [View License](http://creativecommons.org/licenses/by/4.0/)

> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" width="16" style="vertical-align: middle; margin-right: 4px;" /> [查看许可协议](http://creativecommons.org/licenses/by/4.0/)

## Summary
Detecting AI-generated text is a notoriously difficult challenge, especially when faced with distribution shifts like domain changes, varying source models, and editing attacks. **SV-Detect** introduces a novel AI-generated text detector that leverages steering vectors extracted from the hidden representations of a frozen language model. By constructing layer-wise directions that separate human-written text from machine-generated text and passing projection features through a lightweight classifier, the method achieves robust performance both in-distribution and under aggressive transformations (such as polishing and rewriting). Interpretability analyses further reveal that these learned directions capture significant signals beyond surface features, successfully redefining AI text detection as a representation-space probing problem.

> 检测AI生成的文本是一个出了名的难题，特别是当面对领域变更、不同源模型和编辑攻击等分布偏移时。**SV-Detect** 引入了一种新颖的AI生成文本检测器，它利用从冻结语言模型的隐藏表示中提取的引导向量。通过构建在每一层能够将人类编写的文本与机器生成的文本区分开来的方向，并将投影特征通过轻量级分类器，该方法在同分布以及剧烈转换（如润色和重写）下均实现了稳健的性能。可解释性分析进一步表明，这些学习到的方向捕获了表面特征之外的重要信号，成功地将AI文本检测重新定义为一个表征空间探测问题。

---

## Paper Metadata

* **arXiv ID:** [arXiv:2606.07313](https://arxiv.org/abs/2606.07313) [cs.CL]
* **DOI:** [10.48550/arXiv.2606.07313](https://doi.org/10.48550/arXiv.2606.07313)
* **Primary Subject:** Computation and Language (`cs.CL`)
* **Secondary Subjects:** Artificial Intelligence (`cs.AI`)
* **Authors:** Mikhail Vishnyakov, Tatiana Gaintseva
* **Submission History:** 
  * [v1] Fri, 5 Jun 2026
  * [v2] Thu, 3 Sep 2026 (this version)

> ## 论文元数据
> 
> * **arXiv ID:** [arXiv:2606.07313](https://arxiv.org/abs/2606.07313) [cs.CL]
> * **DOI:** [10.48550/arXiv.2606.07313](https://doi.org/10.48550/arXiv.2606.07313)
> * **主要学科:** 计算与语言 (`cs.CL`)
> * **次要学科:** 人工智能 (`cs.AI`)
> * **作者:** Mikhail Vishnyakov, Tatiana Gaintseva
> * **提交历史:** 
>   * [v1] 2026年6月5日（周五）
>   * [v2] 2026年9月3日（周四）（此版本）

---

## Abstract
> Detecting AI-generated text is especially difficult under distribution shift, such as transfer across domains, source models, and editing attacks. We propose an AI-generated text detector based on steering vectors extracted from the hidden representations of a frozen language model. At each layer, we construct a direction that separates human-written from AI-generated text, and represent each input by its layer-wise alignment with these directions. A lightweight classifier trained on these projection features yields the final detection score. Our method achieves strong performance both in-distribution and under distribution shift, including across domains, source models, and machine-editing transformations such as polishing and rewriting. Interpretation analyses show that the learned directions align with recognizable stylistic cues while capturing substantial additional signal beyond surface features. These results position AI-generated text detection as a representation-space probing problem and show that steering vectors provide a simple and effective solution.

> ## 摘要
> > 在存在分布偏移（例如跨领域迁移、不同源模型和编辑攻击）的情况下，检测AI生成的文本尤其困难。我们提出了一种基于引导向量的AI生成文本检测器，该引导向量提取自冻结语言模型的隐藏表示。在每一层中，我们构建了一个能够区分人类编写文本与AI生成文本的方向，并通过每个输入与这些方向的分层对齐来表示它。在这些投影特征上训练的轻量级分类器可产生最终的检测得分。我们的方法在同分布以及分布偏移（包括跨领域、源模型以及机器编辑转换如润色和重写）下均实现了出色的性能。解释性分析表明，学习到的方向与可识别的文体线索相一致，同时捕获了表面特征之外的大量附加信号。这些结果将AI文本检测定位为一个表征空间探测问题，并表明引导向量提供了一种简单而有效的解决方案。

---

## Access & Resources
* **Full-Text Options:** 
  * [View PDF](https://arxiv.org/pdf/2606.07313)
  * [HTML Version (Experimental)](https://arxiv.org/html/2606.07313v2)
  * [TeX Source](https://arxiv.org/src/2606.07313)
* **External References & Citations:**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2606.07313)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.07313)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.07313)

> ## 访问与资源
> * **全文选项：** 
>   * [查看 PDF](https://arxiv.org/pdf/2606.07313)
>   * [HTML 版本（实验性）](https://arxiv.org/html/2606.07313v2)
>   * [TeX 源码](https://arxiv.org/src/2606.07313)
> * **外部参考与引用：**
>   * [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2606.07313)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.07313)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.07313)