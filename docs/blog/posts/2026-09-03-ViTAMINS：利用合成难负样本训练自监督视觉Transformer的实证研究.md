---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- 计算机视觉
- 自监督学习
- 视觉Transformer
- 对比学习
- 难负样本挖掘
title: ViTAMINS：利用合成难负样本训练自监督视觉Transformer的实证研究
---
### 文章背景与核心概要

在自监督视觉Transformer（ViT）的预训练领域，当前的趋势主要由生成式方法（如MAE）和自蒸馏方法（如DINO系列、V-JEPA）主导。然而，对比学习由于其对负样本选择的敏感性，在视觉领域的应用常常面临挑战。为了突破这一瓶颈，本文作者Nikos Giakoumoglou等人提出了 **ViTAMINS** 方法，通过将合成难负样本（Synthetic Hard Negatives）无缝集成到无监督ViT预训练中，显著提升了特征表示的质量。

ViTAMINS的核心创新在于通过对现有对比学习框架进行简单而有效的修改，引入了高质量的合成难负样本。实验证明，该方法不仅在ImageNet基准测试、迁移学习、图像检索、版权检测以及图像和视频分割任务中全面超越了主流的生成式和自蒸馏方法，还展现出了极高的资源效率——例如，采用ViT-B架构的ViTAMINS模型性能即可超越采用更大ViT-L架构的V-JEPA。此外，该方法还催生了令人瞩目的涌现属性：学习到的表征不仅包含图像语义内容的显式信息，还能充当出色的分类器（较基线提升高达 **+11.3%**）。这项工作有力地证明了，对比学习完全可以作为一种比当前主流方法更简单但同样强大的替代方案。

---

# ViTAMINS: An Empirical Study of Training Self-Supervised Vision Transformers with Synthetic Hard Negatives

<div style="background-color: #f8f9fa; padding: 15px; border-left: 4px solid #007bff; margin-bottom: 20px;">
  <h3 style="margin-top: 0; color: #007bff;">📋 Summary</h3>
  <p><strong>ViTAMINS</strong> is a novel method that integrates synthetic hard negatives into unsupervised Vision Transformer (ViT) pretraining to significantly boost representation quality. Through simple modifications to existing contrastive frameworks, ViTAMINS outperforms dominant generative and self-distillation methods while maintaining greater resource efficiency (e.g., a ViT-B model surpassing V-JEPA with a ViT-L).</p>
</div>

---

## Paper Metadata

> * **arXiv ID:** [arXiv:2609.01041](https://arxiv.org/abs/2609.01041) [cs.CV]
> * **Subjects:** Computer Vision and Pattern Recognition (`cs.CV`), Artificial Intelligence (`cs.AI`), Machine Learning (`cs.LG`)
> * **Conference:** WACV 2027
> * **Submission Date:** September 1, 2026
> * **Authors:** 
>   * Nikos Giakoumoglou
>   * Andreas Floros
>   * Kleanthis-Marios Papadopoulos
>   * Tania Stathaki

---

## Abstract

我们引入了 **ViTAMINS**，这是一种将合成难负样本集成到无监督视觉Transformer预训练中以提升特征表示质量的方法。我们的方法在ImageNet、迁移学习、图像检索、版权检测以及图像和视频分割任务上进行了全面的基准测试。

> We introduce **ViTAMINS**, a method that integrates synthetic hard negatives into unsupervised vision transformer pretraining to improve representation quality. Our approach is thoroughly benchmarked on ImageNet and transfer learning, image retrieval, copy detection, and image, video segmentation tasks. 

值得注意的是，我们提出的负样本催生了涌现属性（emergent properties），在此属性下，学习到的表征包含有关图像语义内容的显式信息，并可作为出色的分类器（较基线提升高达 **+11.3%**）。ViTAMINS通过对现有对比学习框架进行简单修改便实现了这些优势，在超越竞争方法的同时具备更高的资源效率（例如，我们的ViT-B超越了采用ViT-L的V-JEPA）。我们的发现促使我们重新思考对比学习，将其视作取代主流生成式和自蒸馏方法的一种更简单但同样强大的替代方案。

> Notably, our proposed negatives give rise to emergent properties, where learned representations contain explicit information about the semantic content of an image and serve as excellent classifiers (up to **+11.3%** over baselines). ViTAMINS achieves these benefits through simple modifications to existing contrastive frameworks and outperforms competing methods while being more resource efficient, e.g., our ViT-B surpasses V-JEPA with ViT-L. Our findings motivate reconsidering contrastive learning as a simpler yet powerful alternative to dominant generative and self-distillation approaches.

---

## Links & Resources

> * **Full-Text:** [View PDF](https://arxiv.org/pdf/2609.01041) | [HTML (Experimental)](https://arxiv.org/html/2609.01041v1) | [TeX Source](https://arxiv.org/src/2609.01041)
> * **Citation Tools:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.01041) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.01041) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.01041)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="display:inline-block; vertical-align:middle; margin-left:5px; height:15px;" /></a>