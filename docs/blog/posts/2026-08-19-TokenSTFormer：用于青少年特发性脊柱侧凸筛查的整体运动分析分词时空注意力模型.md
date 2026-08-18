---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 脊柱侧凸筛查
- 时空注意力
- 计算机视觉
- 医疗AI
- 步态分析
title: TokenSTFormer：用于青少年特发性脊柱侧凸筛查的整体运动分析分词时空注意力模型
---
### 文章背景与核心概要

青少年特发性脊柱侧凸（AIS）是一种常见的脊柱畸形，若不及时治疗可能导致严重的健康问题。传统的筛查方法通常具有主观性、成本高昂且过度依赖专业经验。为应对这些挑战，本研究推出了 **ScoliGait 数据集**（包含 1,516 个步态视频片段及其对应的 X 光记录），并提出了 **TokenSTFormer**，这是一种用于整体运动分析的新型分词时空注意力模型。

TokenSTFormer 显著增强了特征表示与模型收敛能力，达到了 0.79 的最先进（SOTA）准确率，性能超越了标准的视觉 Transformer（Vision Transformer）编码器。该研究展示了一种可扩展、低成本的自动化脊柱侧凸筛查方法，为未来脊柱侧凸检测的临床应用奠定了基础。

---

## 论文元数据 (Paper Metadata)

* **arXiv ID:** [arXiv:2608.16122](https://arxiv.org/abs/2608.16122) [cs.CV]
* **学科分类:** 计算机视觉与模式识别 (`cs.CV`); 人工智能 (`cs.AI`); 机器学习 (`cs.LG`)
* **作者:** Dong Chen, Kenneth M.C. Cheung
* **提交时间:** 2026年8月17日
* **DOI:** [10.48550/arXiv.2608.16122](https://doi.org/10.48550/arXiv.2608.16122)

---

## 摘要 (Abstract)

青少年特发性脊柱侧凸（AIS）是青少年中一种高发的脊柱畸形，若未加干预可能导致严重的健康后果。传统的筛查方法受限于主观解释、对专业经验的依赖以及较低的可扩展性。为解决这些挑战，我们推出了 ScoliGait 数据集，该数据集包含 1,516 个步态视频片段，并配有相应的 X 光记录。同时，我们推出了 TokenSTFormer，这是一种通过对空间和时间语义进行分词来增强特征表示和收敛性的新型模型。我们的模型实现了最先进的性能，在包括 0.79 准确率在内的关键指标上超越了原生 Vision Transformer 编码器。本研究凸显了利用步态视频导出的整体运动特征以及基于注意力机制的模型进行可扩展、具成本效益的 AIS 筛查的潜力，为未来脊柱侧凸检测的临床应用铺平了道路。

> Adolescent Idiopathic Scoliosis (AIS) is a prevalent spinal deformity in adolescents that, if left untreated, can result in severe health outcomes. Traditional screening methods are limited by subjective interpretation, reliance on professional expertise and low scalability. To address these challenges, we present ScoliGait dataset, which comprises 1,516 gait video clips paired with corresponding X-ray records. We also introduce TokenSTFormer, a novel model that tokenizes spatial and temporal semantics to enhance feature representation and convergence. Our model achieves state-of-the-art performance, surpassing vanilla Vision Transformer encoder across key metrics, including accuracy of 0.79. This study highlights the potential of leveraging holistic motion features derived from gait video and attention-based models for scalable, cost-effective AIS screening, paving the way for future clinical applications in scoliosis detection.

---

## 资源与链接 (Resources & Links)

* **全文阅读:** [查看 PDF](https://arxiv.org/pdf/2608.16122)
* **开源许可:** [知识共享署名 4.0 国际许可协议 (Creative Commons Attribution 4.0 International)](http://creativecommons.org/licenses/by/4.0/)  
  <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article">
  <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" />
  </a>
* **引用与参考:**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.16122)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.16122)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.16122)