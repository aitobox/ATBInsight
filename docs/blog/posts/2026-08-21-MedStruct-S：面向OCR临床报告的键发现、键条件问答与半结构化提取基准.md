---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-21
hide:
- navigation
tags:
- 医学自然语言处理
- 信息提取
- 基准测试
- OCR
- 大语言模型
title: MedStruct-S：面向OCR临床报告的键发现、键条件问答与半结构化提取基准
---
### 文章背景与核心概要
从OCR识别后的临床报告中进行半结构化信息提取（IE），对于高效重建患者的纵向病史至关重要。然而，现实场景中的临床报告常包含异构且未完全知的键表示，并伴有显著的OCR噪声，现有的评估方法往往未能充分建模这两个关键因素，难以准确评估模型在真实环境下的鲁棒性。

为了填补这一空白，本文提出了 **MedStruct-S** 基准测试，专门用于在未知键和OCR噪声条件下评估三项核心任务：字段标题（键）发现、键条件问答（QA）以及端到端键值对提取。基于该基准，研究团队对两类代表性范式（具有后处理的编码器专有序列标注，以及解码器专有结构化生成）进行了基准测试，涵盖了参数量从0.11B到103B不等的4款编码器模型和5款解码器模型。

研究发现表明，在非空值键条件问答任务中，尽管编码器模型的参数量远小于解码器模型，但它们却取得了最佳性能；而在不严格控制模型规模的前提下，经过微调的解码器模型则能带来最强的整体结果。这些发现证明了MedStruct-S为在多样化半结构化信息提取设置中选择和比较模型提供了可靠且实用的基础。

---

# MedStruct-S: A Benchmark for Key Discovery, Key-Conditioned QA and Semi-Structured Extraction from OCR Clinical Reports

> MedStruct-S: A Benchmark for Key Discovery, Key-Conditioned QA and Semi-Structured Extraction from OCR Clinical Reports

## 📋 Executive Summary
* **Authors:** Yingyun Li, Yu Wang, Haiyang Qian
* **Subjects:** Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`)
* **Publication:** Accepted by KSEM 2026 (arXiv:2605.03103v2)
* **Dataset Scale:** 3,582 annotated real-world clinical report pages

> ## 📋 Executive Summary
> * **Authors:** Yingyun Li, Yu Wang, Haiyang Qian
> * **Subjects:** Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`); Machine Learning (`cs.LG`)
> * **Publication:** Accepted by KSEM 2026 (arXiv:2605.03103v2)
> * **Dataset Scale:** 3,582 annotated real-world clinical report pages

---

## 📖 Abstract
Semi-structured information extraction (IE) from OCR-derived clinical reports is crucial for efficiently reconstructing patients' longitudinal medical histories. In practice, this scenario commonly involves three tasks: 
1. Field-header (key) discovery
2. Key-conditioned question answering (QA)
3. End-to-end key-value pair extraction

However, existing evaluations often under-model two critical factors: **heterogeneous and incompletely known key representations**, and **OCR-induced noise**. This makes it difficult to assess model robustness in real-world settings.

To bridge this gap, the authors present **MedStruct-S**, a benchmark specifically designed to evaluate these tasks under unknown keys and OCR noise. Using MedStruct-S, the study benchmarks two representative paradigms—*encoder-only sequence labeling with post-processing* and *decoder-only structured generation*—covering four encoder-only and five decoder-only models spanning from 0.11B to 103B parameters.

### Key Findings:
* **Encoder-Only Models:** Achieve the best performance for non-null-value key-conditioned QA despite being substantially smaller than decoder-only models. When comparing models of a similar order of magnitude, encoder-only models still perform better overall.
* **Decoder-Only Models:** Without controlling strictly for model scale, fine-tuned decoder-only models deliver the strongest overall results.

These findings demonstrate that MedStruct-S provides a reliable and practical basis for selecting and comparing models across diverse semi-structured IE settings.

> ## 📖 Abstract
> Semi-structured information extraction (IE) from OCR-derived clinical reports is crucial for efficiently reconstructing patients' longitudinal medical histories. In practice, this scenario commonly involves three tasks: 
> 1. Field-header (key) discovery
> 2. Key-conditioned question answering (QA)
> 3. End-to-end key-value pair extraction
> 
> However, existing evaluations often under-model two critical factors: **heterogeneous and incompletely known key representations**, and **OCR-induced noise**. This makes it difficult to assess model robustness in real-world settings.
> 
> To bridge this gap, the authors present **MedStruct-S**, a benchmark specifically designed to evaluate these tasks under unknown keys and OCR noise. Using MedStruct-S, the study benchmarks two representative paradigms—*encoder-only sequence labeling with post-processing* and *decoder-only structured generation*—covering four encoder-only and five decoder-only models spanning from 0.11B to 103B parameters.
> 
> ### Key Findings:
> * **Encoder-Only Models:** Achieve the best performance for non-null-value key-conditioned QA despite being substantially smaller than decoder-only models. When comparing models of a similar order of magnitude, encoder-only models still perform better overall.
> * **Decoder-Only Models:** Without controlling strictly for model scale, fine-tuned decoder-only models deliver the strongest overall results.
> 
> These findings demonstrate that MedStruct-S provides a reliable and practical basis for selecting and comparing models across diverse semi-structured IE settings.

---

## 📊 Document Metadata & Reference Information

* **Identifiers:** arXiv:2605.03103 [cs.CL]
* **DOI:** [10.48550/arXiv.2605.03103](https://doi.org/10.48550/arXiv.2605.03103)
* **ACM Classifications:** I.2.7; H.3.1; J.3
* **Submission History:** 
  * *v1:* May 4, 2026
  * *v2:* August 19, 2026

### External Resources & Full Text Access
* [View PDF](https://arxiv.org/pdf/2605.03103)
* [TeX Source](https://arxiv.org/src/2605.03103)
* [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2605.03103)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2605.03103)

> ## 📊 Document Metadata & Reference Information
> 
> * **Identifiers:** arXiv:2605.03103 [cs.CL]
> * **DOI:** [10.48550/arXiv.2605.03103](https://doi.org/10.48550/arXiv.2605.03103)
> * **ACM Classifications:** I.2.7; H.3.1; J.3
> * **Submission History:** 
>   * *v1:* May 4, 2026
>   * *v2:* August 19, 2026
> 
> ### External Resources & Full Text Access
> * [View PDF](https://arxiv.org/pdf/2605.03103)
> * [TeX Source](https://arxiv.org/src/2605.03103)
> * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2605.03103)
> * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2605.03103)