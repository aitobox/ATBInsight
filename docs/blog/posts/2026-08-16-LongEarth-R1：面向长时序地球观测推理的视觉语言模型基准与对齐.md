---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-16
hide:
- navigation
tags:
- 视觉语言模型
- 遥感
- 长时序推理
- 强化学习
- LongEarth
title: LongEarth-R1：面向长时序地球观测推理的视觉语言模型基准与对齐
---
### 文章背景与核心概要

长时序地球观测推理要求模型能够处理多阶段的地理演变，定位空间变化，检测时间异常，并根据扩展的图像序列推断未来趋势。然而，现有的遥感视觉语言模型（VLM）大多局限于单张图像、图像对或短序列，难以在相关帧和区域之间建立可靠的关联。

本文提出了 **LongEarth-Bench**，这是一个包含约 12 万个问答样本的大规模基准，涵盖了 12 项任务，包括演变总结、空间推理、异常识别和逻辑预测。为了解决这些复杂的时空任务，作者开发了 **LongEarth** 模型，并通过监督微调引入了序列标识符和结构化思维链监督。在此基础上，作者进一步提出了 **LongEarth-R1**，利用包含格式、时间和空间奖励的组相对策略优化（Group Relative Policy Optimization），在 12 项长序列地球观测任务中达到了最先进水平，同时在标准基准测试中保持了极强的竞争力。

---

## 元数据与出版详情

* **arXiv ID:** [arXiv:2608.13344](https://arxiv.org/abs/2608.13344) [cs.AI]
* **提交日期:** 2026年8月13日
* **主要学科:** 人工智能 (`cs.AI`)
* **DOI:** [10.48550/arXiv.2608.13344](https://doi.org/10.48550/arXiv.2608.13344)

> * **arXiv ID:** [arXiv:2608.13344](https://arxiv.org/abs/2608.13344) [cs.AI]
> * **Submission Date:** August 13, 2026
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **DOI:** [10.48550/arXiv.2608.13344](https://doi.org/10.48550/arXiv.2608.13344)

---

## 作者

* **Yupan Ding**
* **Jing Xiao**
* **Zhenyuan Zhang**
* **Chaofeng Chen**
* **Liang Liao**
* **Gui-Song Xia**
* **Mi Wang**

> * **Yupan Ding**
> * **Jing Xiao**
> * **Zhenyuan Zhang**
> * **Chaofeng Chen**
> * **Liang Liao**
> * **Gui-Song Xia**
> * **Mi Wang**

---

## 摘要

长时序地球观测推理要求模型能够组织多阶段的地理演变、定位空间变化、检测时间异常，并从扩展的图像序列中推断未来。然而，现有的遥感视觉语言模型主要关注孤立图像、图像对或短序列，限制了在相关帧和区域上的可靠基础能力。

我们引入了 **LongEarth-Bench**，这是一个包含约 12 万个问答样本的基准，源自 11.7 万张独特图像。其序列平均长度为 15.14 帧，最长可达 30 帧，涵盖了演变总结、空间推理、异常识别和逻辑预测等 12 项任务。其中一个包含 3 万个样本的子集还提供了结构化的推理轨迹，将关键帧和变化区域与最终答案联系起来。

我们通过带有显式序列标识符和结构化思维链监督的监督微调开发了 LongEarth。在 LongEarth 的基础上，**LongEarth-R1** 应用了带有格式、时间和空间奖励的组相对策略优化。LongEarth-R1 在所有 12 项长序列任务中均取得了最佳结果，同时在标准遥感基准测试中保持了竞争力。

> Long-horizon Earth observation reasoning requires models to organize multi-stage geographic evolution, localize spatial changes, detect temporal anomalies, and infer future from extended image sequences. However, existing remote sensing vision-language models mainly focus on isolated images, image pairs, or short sequences, limiting reliable grounding in the relevant frames and regions. 
>
> We introduce **LongEarth-Bench**, a benchmark containing approximately 120k question-answering samples derived from 117k unique images. Its sequences average 15.14 frames and extend to 30 frames, covering 12 tasks across evolution summarization, spatial reasoning, anomaly identification, and logical prediction. A 30k-sample subset further provides structured reasoning traces linking key frames and changed regions to final answers. 
>
> We develop LongEarth through supervised fine-tuning with explicit sequence identifiers and structured chain-of-thought supervision. Building on LongEarth, **LongEarth-R1** applies group relative policy optimization with format, temporal, and spatial rewards. LongEarth-R1 achieves the best results on all 12 long-sequence tasks while remaining competitive on standard remote sensing benchmarks.

---

## 访问与资源

* **全文选项:** 
  * [查看 PDF](https://arxiv.org/pdf/2608.13344)
  * [HTML (实验性)](https://arxiv.org/html/2608.13344v1)
  * [TeX 源码](https://arxiv.org/src/2608.13344)
* **外部引用与工具:**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.13344)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.13344)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.13344)

> * **Full-Text Options:** 
>   * [View PDF](https://arxiv.org/pdf/2608.13344)
>   * [HTML (experimental)](https://arxiv.org/html/2608.13344v1)
>   * [TeX Source](https://arxiv.org/src/2608.13344)
> * **External Citations & Tools:**
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.13344)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.13344)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.13344)