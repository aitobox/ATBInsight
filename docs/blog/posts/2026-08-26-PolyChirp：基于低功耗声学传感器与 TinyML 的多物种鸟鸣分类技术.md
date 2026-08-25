---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- TinyML
- 鸟类监测
- 声学传感器
- 嵌入式AI
- 神经网络架构优化
title: PolyChirp：基于低功耗声学传感器与 TinyML 的多物种鸟鸣分类技术
---
### 文章背景与核心概要
在野外生态监测中，利用低功耗微控制器和声学传感器进行鸟类鸣叫实时监测已成为 TinyML 领域的重要研究方向。然而，以往的技术方案受限于硬件资源，大多只能进行单一物种的二分类检测，难以满足实际生态监测中同时追踪多种动物的需求。为此，研究人员开发了 PolyChirp 系统，通过结合生物学领域知识、自动化数据集精选、神经网络架构优化以及基于神经网络处理单元（NPU）的硬件加速，成功实现了野外多物种鸟鸣的高效检测。

该研究的核心技术在于设计了全新的微型多类分类模型，不仅能够同时稳健地检测多达 10 种鸟类，还在计算性能、内存占用、推理延迟和能耗方面表现优异。实验结果表明，PolyChirp 在超越现有单物种二分类技术的同时，依然保持了极低的能耗印记，使得传感器仅凭单块电池就能在野外持续运行一整个繁殖季，为生态保护和生物多样性研究提供了强大的技术支撑。

---

## 摘要 (Summary)

**PolyChirp** 是一种创新的基于 TinyML 的方法，旨在利用野外的低功耗声学传感器同时监测多个鸟类物种。虽然以往的最先进微控制器局限于二分类（检测单个物种），但 PolyChirp 整合了生物学领域专业知识、自动化数据集精选、神经网络架构优化以及通过神经网络处理单元（NPU）实现的硬件加速。评估表明，PolyChirp 成功地同时检测多达 10 个鸟类物种，同时保持了足够小的能耗印记，仅需单次电池充电即可在整个繁殖季中持续运行。

> **PolyChirp** is an innovative TinyML-based approach designed to monitor multiple bird species simultaneously using low-power acoustic sensors in the wild. While previous state-of-the-art microcontrollers were limited to binary classification (detecting a single species), PolyChirp integrates biological domain expertise, automated dataset curation, neural architecture optimization, and hardware acceleration via a neural processing unit (NPU). Evaluations demonstrate that PolyChirp successfully detects up to 10 bird species simultaneously while maintaining an energy footprint small enough to operate for an entire breeding season on a single battery charge.

---

## 元数据与出版详情 (Metadata & Publication Details)

| 字段 | 详情 |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.23101](https://arxiv.org/abs/2608.23101) [cs.LG] |
| **主要主题** | 机器学习 (`cs.LG`), 人工智能 (`cs.AI`) |
| **作者** | Nathan Duboisset, Zhaolan Huang, Felix Bießmann, Roudy Dagher, Antoine Lavandier, Emmanuel Baccelli |
| **提交日期** | 2026年8月24日 |
| **期刊参考** | IEEE 国际声音互联网研讨会 (IS2) 2026 |
| **DOI** | [10.48550/arXiv.2608.23101](https://doi.org/10.48550/arXiv.2608.23101) |

> | Field | Details |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.23101](https://arxiv.org/abs/2608.23101) [cs.LG] |
| **Primary Subject** | Machine Learning (`cs.LG`), Artificial Intelligence (`cs.AI`) |
| **Authors** | Nathan Duboisset, Zhaolan Huang, Felix Bießmann, Roudy Dagher, Antoine Lavandier, Emmanuel Baccelli |
| **Submission Date** | August 24, 2026 |
| **Journal Reference** | IEEE International Symposium on the Internet of Sounds (IS2) 2026 |
| **DOI** | [10.48550/arXiv.2608.23101](https://doi.org/10.48550/arXiv.2608.23101) |

---

## 摘要正文 (Abstract)

TinyML 领域的最新进展表明，基于微控制器的低功耗硬件可以根据声学传感器数据实时实现鸟类物种监测，且在单次电池充电下可持续整个繁殖期。然而，迄今为止，低功耗微控制器的最先进技术仅限于单个物种的二分类。相比之下，实际的动物群监测部署通常针对多个物种同时进行。

为了应对这一挑战，我们开发了 **PolyChirp**，这是一种结合了生物学领域专业知识、自动化数据集精选、神经网络架构优化和新型硬件的方法，旨在实现野外多类鸟类物种检测。PolyChirp 基于新设计的微型多类模型，这些模型利用了最新的微控制器以及通过神经网络处理单元（NPU）实现的硬件加速。

我们评估了这些模型的预测性能，并测量了它们在常用微控制器硬件上的计算性能——内存占用、延迟和能耗。我们的结果表明，PolyChirp 不仅在单物种二分类上超越了最先进的技术，而且还实现了对多达 10 个物种的同时稳健分类，同时仍然符合传感器必须在野外依靠单块电池全季正常运行的资源包络。

> Recent progress in the field of TinyML has demonstrated that low-power hardware based on microcontrollers can achieve bird species monitoring in real time based on acoustic sensor data for an entire breeding period on a single battery charge. However, the state of the art on low-power microcontrollers was so far limited to binary classification of a single species. In contrast, real fauna monitoring deployments often target multiple species simultaneously. 
>
> To address this challenge we develop **PolyChirp**, an approach combining biological domain expertise, automated dataset curation, neural architecture optimization and novel hardware to achieve multiclass bird species detection in the wild. PolyChirp is based on newly designed tiny multiclass models that leverage recent microcontrollers and hardware acceleration with a neural processing unit (NPU). 
>
> We evaluate the predictive performance of these models, and we measure their computational performance—memory footprint, latency, energy consumption—on common microcontroller hardware. Our results demonstrate that PolyChirp not only outperforms state-of-the-art on single species binary classification, but also achieves robust classification of up to 10 species simultaneously, while still fitting within the resource envelope of a sensor that must remain operational in the field for a full season on a single battery charge.

---

## 全文与资源 (Full-Text & Resources)

* [查看 PDF](https://arxiv.org/pdf/2608.23101)
* [HTML 版本（实验性）](https://arxiv.org/html/2608.23101v1)
* [TeX 源码](https://arxiv.org/src/2608.23101)
* [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23101)
* [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23101)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23101)

> * [View PDF](https://arxiv.org/pdf/2608.23101)
* [HTML Version (Experimental)](https://arxiv.org/html/2608.23101v1)
* [TeX Source](https://arxiv.org/src/2608.23101)
* [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23101)
* [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23101)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23101)