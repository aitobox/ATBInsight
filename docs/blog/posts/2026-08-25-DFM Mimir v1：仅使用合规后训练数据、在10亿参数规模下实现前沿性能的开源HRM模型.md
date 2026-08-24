---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- 大语言模型
- 层次化推理模型
- 开源模型
- 丹麦语
- 机器学习
title: DFM Mimir v1：仅使用合规后训练数据、在10亿参数规模下实现前沿性能的开源HRM模型
---
### 文章背景与核心概要
当前的语言模型开发高度依赖于海量且往往存在版权合规争议的数据集，这给致力于开源和合规数据研究的学者们带来了很高的门槛。为了打破这一限制，研究团队推出了 Mimir v1——这是一款基于分层推理模型（HRM）架构、拥有10亿参数的语言模型。该模型完全从零开始训练，仅采用合规的后训练数据（由161个数据集混合而成），在英语上展现出极具竞争力的性能，并为丹麦语树立了全新的技术前沿（SOTA）基准。

在涵盖英语、数学、代码和丹麦语的20项评测中，Mimir v1 成功超越了原版的 HRM-Text 1B，并足以与 Qwen 3.5 4B 和 Gemma 4 E2B 等规模大得多的前沿模型相媲美。这项工作证明了在严格遵循数据合规性的前提下，利用先进架构训练出具备顶尖性能的小型语言模型是完全可行的。

---

# DFM Mimir v1：仅使用合规后训练数据、在10亿参数规模下实现前沿性能的开源HRM模型

> # DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters Using Only Permissible Post-Training Data

## 摘要

**DFM Mimir v1** 是一款基于分层推理模型（HRM）架构构建的10亿参数语言模型。该模型完全从零开始训练，全部使用经过道德采购且合规的后训练数据（由161个数据集混合而成）。Mimir v1 在英语上取得了极具竞争力的性能，同时为丹麦语设定了全新的行业前沿基准。在跨越英语、数学、代码和丹麦语的20项评测中，该模型成功超越了原版的 HRM-Text 1B，并可与 Qwen 3.5 4B 和 Gemma 4 E2B 等体量大得多的前沿模型相媲美。

> ## Summary
> **DFM Mimir v1** is a 1-billion-parameter language model built on the Hierarchical Reasoning Model (HRM) architecture. Trained from scratch entirely on ethically sourced and permissible post-training data (a mixture of 161 datasets), Mimir v1 achieves highly competitive performance in English while setting a new state-of-the-art benchmark for Danish. Across 20 evaluations spanning English, Math, Code, and Danish, the model successfully outperforms the original HRM-Text 1B and rivals much larger frontier models like Qwen 3.5 4B and Gemma 4 E2B.

---

## 论文元数据

* **arXiv 标识符：** [arXiv:2608.13517](https://arxiv.org/abs/2608.13517) [cs.CL]
* **主学科：** 计算与语言 (`cs.CL`)
* **次学科：** 人工智能 (`cs.AI`)
* **发布日期：** 
  * 2026年8月13日提交 (v1)
  * 2026年8月20日最后修订 (v2，增加了记忆审计内容)
* **技术详情：** 技术报告，20页，1个模型
* **作者：** 
  * Peter Schneider-Kamp
  * Jacob Nielsen
  * Gianluca Barmina
  * Kenneth Enevoldsen
  * Lukas Galke Poech

> ## Paper Metadata
> 
> * **arXiv Identifier:** [arXiv:2608.13517](https://arxiv.org/abs/2608.13517) [cs.CL]
> * **Primary Subject:** Computation and Language (`cs.CL`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`)
> * **Publication Dates:** 
>   * Submitted on August 13, 2026 (v1)
>   * Last revised on August 20, 2026 (v2, featuring added memorization audits)
> * **Technical Details:** Technical Report, 20 Pages, 1 Model
> * **Authors:** 
>   * Peter Schneider-Kamp
>   * Jacob Nielsen
>   * Gianluca Barmina
>   * Kenneth Enevoldsen
>   * Lukas Galke Poech

---

## 摘要原文

当前的大语言模型开发依赖于海量且往往不合规的数据集，这给致力于开源和合规数据的研究人员构成了很高的门槛。我们推出了 Mimir v1，这是一款基于分层推理模型（HRM）架构的10亿参数语言模型，它从头开始训练，仅使用合规的后训练数据，便在英语上实现了极具竞争力的性能，并为丹麦语设定了新的技术前沿。Mimir v1 在161个数据集的混合数据上进行训练，在针对英语、数学与代码以及丹麦语的20个基准测试中，表现优于原版 HRM-Text 1B，并能与 Qwen 3.5 4B 和 Gemma 4 E2B 等更大的前沿模型竞争。

> ## Abstract
> Current large language model development relies on massive, often non-permissible datasets, creating a high barrier for researchers committed to open-source and ethically sourced data. We introduce Mimir v1, a 1-billion-parameter language model based on the Hierarchical Reasoning Model (HRM) architecture, that is trained from scratch and delivers highly competitive performance for English and sets a new state of the art for Danish using only permissible post-training data. Trained on a mixture of 161 datasets, Mimir v1 outperforms the original HRM-Text 1B and competes with larger frontier models like Qwen 3.5 4B and Gemma 4 E2B, tested across 20 benchmarks for English, Math & Code and Danish.

---

## 资源与链接

* **模型仓库：** [Hugging Face Hub - DFM-Mimir](https://huggingface.co/danish-foundation-models/DFM-Mimir)
* **文档访问：** 
  * [查看 PDF](https://arxiv.org/pdf/2608.13517)
  * [HTML 版本（实验性）](https://arxiv.org/html/2608.13517v2)
  * [TeX 源码](https://arxiv.org/src/2608.13517)
  * [DOI 链接](https://doi.org/10.48550/arXiv.2608.13517)

> ## Resources & Links
> 
> * **Model Repository:** [Hugging Face Hub - DFM-Mimir](https://huggingface.co/danish-foundation-models/DFM-Mimir)
> * **Document Access:** 
>   * [View PDF](https://arxiv.org/pdf/2608.13517)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.13517v2)
>   * [TeX Source](https://arxiv.org/src/2608.13517)
>   * [DOI Link](https://doi.org/10.48550/arXiv.2608.13517)