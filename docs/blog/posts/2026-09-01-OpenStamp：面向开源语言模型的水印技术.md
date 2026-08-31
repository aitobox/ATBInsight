---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- 大语言模型
- 模型水印
- 开源模型
- 权重修改
- 文本溯源
title: OpenStamp：面向开源语言模型的水印技术
---
### 文章背景与核心概要
随着大语言模型（LLM）生成内容的日益普及，水印技术被广泛用于文本溯源以及区分机器生成内容与人类写作。传统方法通过修改词元采样概率来嵌入水印，但这对于开源模型而言并不适用，因为用户拥有白盒访问权限，可以在推理过程中轻松禁用水印功能。

为了解决这一痛点，本文推出了 **OpenStamp**。该技术仅通过修改最终的投影（unembedding）层，将水印逻辑直接嵌入到模型权重中。多款模型的实验表明，OpenStamp 在保持极低模型性能损失的同时，展现出卓越的检测性能，并对释义攻击（paraphrasing）和事后微调（post-hoc fine-tuning）具有极强的鲁棒性。目前，作者已开源相关代码，并发布了四个主流开源模型的加水印版本。

---

## OpenStamp: A Watermark for Open-Source Language Models

[![license icon]( ./images/345c7ad61f1b.png )](http://creativecommons.org/licenses/by/4.0/)

## Summary
As Large Language Model (LLM) generated content becomes more prevalent, watermarking is increasingly used to attribute text and distinguish it from human writing. Traditional methods modify token sampling probabilities, but these fail for open-source models where users have white-box access and can easily disable watermarking during inference. 

To solve this, **OpenStamp** embeds watermarking logic directly into model weights by modifying only the final projection (unembedding) layer. Experiments across multiple models show that OpenStamp provides superior detection performance and robustness against paraphrasing and post-hoc fine-tuning, all while maintaining minimal capability degradation. The authors have released code and watermarked versions of four popular open-source models.

---

## Paper Metadata

* **arXiv ID:** [arXiv:2608.27899](https://arxiv.org/abs/2608.27899) [cs.CL]
* **Published at:** COLM 2026
* **Submitted Date:** August 28, 2026
* **Authors:** Miroojin Bakshi, Saksham Rastogi, Danish Pruthi
* **Primary Subject:** Computation and Language (`cs.CL`)
* **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Machine Learning (`cs.LG`)
* **DOI:** [10.48550/arXiv.2608.27899](https://doi.org/10.48550/arXiv.2608.27899)

---

## Abstract

> With the growing prevalence of large language model (LLM) generated content, watermarking is considered a promising approach for attributing text to LLMs and distinguishing it from human-written content. A prominent class of techniques embeds subtle but detectable signals in generated text by modifying token sampling probabilities. However, such methods are unsuitable for open-source models, where users have white-box access and can easily disable watermarking during inference. In this work, we introduce OpenStamp, a watermarking technique that encodes the watermarking logic directly into the model weights by modifying only the final projection, or unembedding, layer. Through experiments across two models, we show that OpenStamp achieves superior detection performance, with minimal degradation in model capabilities compared to prior methods. The implanted watermark is explicitly designed, and empirically confirmed, to be more robust to paraphrasing attacks and harder to scrub off through post-hoc fine-tuning than prior open-source watermarks. To enable developers to watermark their models, we release our code alongside watermarked versions of 4 popular open-source models.

---

## Full-Text & Access Links

* **PDF Version:** [View PDF](https://arxiv.org/pdf/2608.27899)
* **HTML Version:** [HTML (experimental)](https://arxiv.org/html/2608.27899v1)
* **TeX Source:** [Download Source](https://arxiv.org/src/2608.27899)
* **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)

---

## References & External Tools

* **Bibliographic Databases:** 
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.27899)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.27899)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.27899)
* **Code & Ecosystem Finders:**
  * [Hugging Face](https://huggingface.co/huggingface)
  * [CatalyzeX Code Finder](https://www.catalyzex.com)
  * [alphaXiv Discussion](https://alphaxiv.org/)
  * [Connected Papers](https://www.connectedpapers.com/)