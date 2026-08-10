---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-11
hide:
- navigation
tags:
- openPangu
- 昇腾NPU
- 模型量化
- PTQ
- 华为昇腾
title: openPangu模型在昇腾NPU上的量化实证研究
---
### 文章背景与核心概要

随着国产大模型及硬件生态的迅速发展，如何在华为昇腾（Ascend）等国产硬件上高效部署大语言模型成为了工业界和学术界关注的焦点。openPangu系列模型作为私有化和国产化部署的重要选择，其在激进的训练后量化（PTQ）策略下的鲁棒性和性能表现，此前尚未得到系统性的表征。本文针对openPangu 1B和7B模型在华为昇腾910B1 NPU上的运行情况展开了对照实证研究，评估了多种代表性的仅权重（weight-only）和权重-激活值量化方法。

研究结果表明，8位仅权重量化在18个评估任务中对openPangu 1B和7B模型均达到了近乎无损的效果；而4位量化对于7B模型依然可行，但对1B模型在推理、数学和代码基准测试中会导致明显的性能退化。此外，极低精度量化（如2位和二值化）的表现大多退化至接近随机行为，W4A4 SmoothQuant则会导致非有限的困惑度（perplexity）得分。该研究为基于昇腾NPU部署openPangu模型时的量化配置选择提供了精准的精度参考地图，同时也指出了极低比特压缩技术所面临的持续挑战。

## An Empirical Study of openPangu Quantization on Ascend NPUs

## Overview & Summary

> This paper presents a controlled empirical study examining the robustness and performance of openPangu models under aggressive post-training quantization (PTQ) when deployed on Huawei Ascend 910B1 NPUs. 
> 
> **Key Takeaways:**
> * **8-bit Quantization:** Weight-only 8-bit quantization is effectively lossless for both openPangu 1B and 7B models across 18 evaluated tasks.
> * **4-bit Quantization:** Remains viable for the 7B model, but causes noticeable degradation for the 1B model, particularly in reasoning, mathematics, and coding benchmarks.
> * **Ultra-Low Precision:** 2-bit and binary settings largely collapse into near-random behavior, and W4A4 SmoothQuant leads to non-finite perplexity scores.

---

## Article Metadata

> * **arXiv ID:** [arXiv:2606.21257](https://arxiv.org/abs/2606.21257) [cs.LG]
> * **Subjects:** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`)
> * **Authors:** 
>   * Tong Shi
>   * Jiacheng Wang
>   * Hui Xie
>   * Ying Li
>   * Aishan Liu
>   * Jinyang Guo
>   * Xianglong Liu
> * **Submission Timeline:**
>   * **[v1]** 19 Jun 2026
>   * **[v2]** 26 Jun 2026
>   * **[v3]** 24 Jul 2026
>   * **[v4]** 7 Aug 2026 *(Current Version)*

---

## Abstract

> openPangu models are attractive targets for private and domestic large-language-model deployment, yet their robustness under aggressive post-training quantization on Ascend NPUs has not been systematically characterized. This paper conducts a controlled empirical study of openPangu 1B and 7B models on Huawei Ascend 910B1 NPUs. We evaluate representative weight-only and weight-activation post-training quantization methods, including RTN, GPTQ, AWQ, SmoothQuant, GPTAQ, BiLLM, and SliM-LLM, under a unified calibration and evaluation protocol. Across 18 evaluation tasks, we find that 8-bit weight-only quantization is effectively lossless for both models, while 4-bit quantization remains practical for the 7B model but is visibly more harmful for the 1B model on reasoning, math, and code tasks. Ultra-low precision remains challenging: most 2-bit and binary settings collapse to near-random behavior, and W4A4 SmoothQuant produces non-finite perplexity in our evaluation. These results provide an NPU-oriented accuracy map for selecting openPangu quantization settings and highlight the persistent difficulty of extreme low-bit compression.

---

## Full-Text & Resources

> * **PDF Version:** [View PDF](https://arxiv.org/pdf/2606.21257)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2606.21257v4)
> * **Source Files:** [TeX Source](https://arxiv.org/src/2606.21257)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

---

## External References & Tools

> * **Bibliographic Databases:** 
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.21257)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2606.21257)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.21257)
> * **Code & Community Explorers:** 
>   * [alphaXiv](https://alphaxiv.org/)
>   * [CatalyzeX Code Finder](https://www.catalyzex.com)
>   * [Hugging Face Spaces & Models](https://huggingface.co/)