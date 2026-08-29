---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 生成式检索
- 计算机视觉
- 图像检索
- 视觉多模态
- 深度学习
title: PailitaoGR：生成式图像检索的潜在图像思考框架
---
### 文章背景与核心概要
在当前的计算机视觉与信息检索领域，生成式检索通过直接生成产品语义标识符（SIDs）展现出了强劲的性能。然而，将这一范式扩展到图像搜索并非易事，因为现实世界中的查询图像通常包含复杂多变的信息，包括搜索目标、有用的辅助证据以及无关的视觉内容。这就要求模型既能精准识别并聚焦于搜索目标，又能有选择性地利用辅助证据。

为了解决这一挑战，本文提出了 **PailitaoGR**——一种用于生成式图像检索的“潜在图像思考”（Latent Think-with-Images）方法。该方法将目标聚焦感知和辅助证据的选择性利用内化到生成式检索模型中，从而实现了“无需裁剪的缩放（Zooming without Cropping）”和“无需OCR的阅读（Reading without OCR）”。具体而言，作者设计了面向搜索目标的目标聚焦感知机制，以及能够发掘辅助证据的选择性辅助证据利用机制。通过基于真实在线图像搜索日志构建的训练和验证集进行的实验表明，该方法相比现有基线模型平均性能提升了 **13.8%**，充分验证了其在实际应用中的有效性。

---

## 📌 执行摘要 (Executive Summary)

* **论文标题 (Paper Title):** PailitaoGR: Latent Think-with-Images for Generative Image Retrieval
* **arXiv ID:** [2608.26658](https://arxiv.org/abs/2608.26658) [cs.CV]
* **作者 (Authors):** Xiaomeng Fan, Yueran Liu, Shengyu Zhou, Chenghan Fu, Wanxian Guan, Feng Li, Chuan Yu, Jian Xu, Bo Zheng
* **提交时间 (Submitted On):** 2026年8月27日
* **核心创新 (Key Innovation):** 引入了 **PailitaoGR**，这是一种*潜在图像思考*（Latent Think-with-Images）框架，将目标聚焦感知和选择性辅助证据利用内化到生成式图像检索模型中——实现了**“无需裁剪的缩放”**和**“无需OCR的阅读”**。在真实世界在线日志上的实验表明，其性能比现有基线提升了 **13.8%**。

> **Executive Summary**
> * **Paper Title:** PailitaoGR: Latent Think-with-Images for Generative Image Retrieval
> * **arXiv ID:** [2608.26658](https://arxiv.org/abs/2608.26658) [cs.CV]
> * **Authors:** Xiaomeng Fan, Yueran Liu, Shengyu Zhou, Chenghan Fu, Wanxian Guan, Feng Li, Chuan Yu, Jian Xu, Bo Zheng
> * **Submitted On:** August 27, 2026
> * **Key Innovation:** Introduces **PailitaoGR**, a *Latent Think-with-Images* framework that internalizes target-focused perception and selective auxiliary-evidence utilization into generative image retrieval models—achieving **"Zooming without Cropping"** and **"Reading without OCR."** Experiments on real-world online logs show a **13.8% performance improvement** over existing baselines.

---

## 📋 概览与元数据 (Overview & Metadata)

* **主学科 (Primary Subject):** 计算机视觉与模式识别 (`cs.CV`)
* **次学科 (Secondary Subjects):** 人工智能 (`cs.AI`)、信息检索 (`cs.IR`)
* **许可证 (License):** [知识共享 署名-非商业性使用-禁止演绎 4.0 国际版](http://creativecommons.org/licenses/by-nc-nd/4.0/) ![license icon](./images/fb423b2203a9.png)

> **Overview & Metadata**
> * **Primary Subject:** Computer Vision and Pattern Recognition (`cs.CV`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Information Retrieval (`cs.IR`)
> * **License:** [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/) ![license icon](./images/fb423b2203a9.png)

---

## 📝 摘要 (Abstract)

生成式检索通过直接生成产品语义标识符（SIDs），已经展现出了强劲的性能。然而，将该范式扩展到图像搜索并不简单，因为现实世界的查询图像包含多样化的信息，包括搜索目标、有用的辅助证据以及无关的视觉内容。

这就要求模型能够识别并聚焦于搜索目标，同时有选择性地利用辅助证据。在本文中，我们提出了 **PailitaoGR**，这是一种用于生成式图像检索的*潜在图像思考*方法，它将目标聚焦感知和选择性辅助证据利用内化到生成式检索模型中，从而实现了*无需裁剪的缩放*和*无需OCR的阅读*。

具体来说，我们设计了：
1. **目标聚焦感知机制**（由目标增强器以及基于在线策略蒸馏和注意力引导损失的学习策略组成），用于识别和增强搜索目标的视觉令牌，从而聚焦于搜索目标区域。
2. **选择性辅助证据利用机制**（包括辅助增强器和容量内增量对比蒸馏策略），用于识别和增强辅助证据的视觉令牌，从而开发利用辅助证据。

通过构建从真实世界在线图像搜索日志中采样得出的训练集和验证集，实验表明我们的方法平均超越现有基线 **13.8%**，验证了其在实际中的有效性。

> **Abstract**
> Generative retrieval has demonstrated strong performance by directly generating product semantic identifiers (SIDs). Extending this paradigm to image search, however, is nontrivial because real-world query images contain diverse information, including the search target, useful auxiliary evidence, and irrelevant visual content. 
> 
> This requires the model to identify and focus on the search target while selectively utilizing auxiliary evidence. In this paper, we propose **PailitaoGR**, a *Latent Think-with-Images* method for generative image retrieval, which internalizes target-focused perception and selective auxiliary-evidence utilization into the generative retrieval model, enabling *Zooming without Cropping* and *Reading without OCR*. 
> 
> Specifically, we design:
> 1. **A target-focused perception mechanism** that identifies and enhances visual tokens of the search target (consisting of a target Enhancer and a learning strategy based on on-policy distillation and attention guidance loss) to focus on search-target regions.
> 2. **A selective auxiliary-evidence utilization mechanism** that identifies and enhances visual tokens of auxiliary evidence (including an auxiliary enhancer and an in-capacity incremental contrastive distillation strategy) to exploit auxiliary evidence.
> 
> By constructing training and validation sets sampled from real-world online image-search logs, experiments demonstrate that our method outperforms existing baselines by an average of **13.8%**, validating its practical effectiveness.

---

## 🔗 访问与资源 (Access & Resources)

* **PDF 版本:** [查看 PDF](https://arxiv.org/pdf/2608.26658)
* **HTML 版本:** [arXiv HTML (实验性)](https://arxiv.org/html/2608.26658v1)
* **源码文件:** [TeX 源码](https://arxiv.org/src/2608.26658)
* **外部引用与工具:** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.26658)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.26658)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.26658)

> **Access & Resources**
> * **PDF Version:** [View PDF](https://arxiv.org/pdf/2608.26658)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.26658v1)
> * **Source Files:** [TeX Source](https://arxiv.org/src/2608.26658)
> * **External Citations & Tools:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.26658)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.26658)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.26658)