---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 大语言模型
- 同行评审
- 幻觉检测
- 基准测试
- 科学文献
title: HalluPeer：用于检测科学同行评审中幻觉的分类法驱动基准
---
### 文章背景与核心概要
随着大语言模型（LLM）越来越多地被用于辅助学术同行评审，它们也带来了生成流畅但缺乏依据的论断的风险，从而损害了评审过程的可靠性。现有的幻觉基准测试往往无法满足这一需求，因为科学评审要求将各项论断深深植根于冗长且技术性强的论文之中。

为了填补这一空白，研究人员推出了 **HalluPeer**——一个旨在检测科学同行评审中幻觉的新型基准。HalluPeer 提供了对齐的三元组数据，包括：1. 原始论文内容；2. 人工撰写的评审意见；3. 注入幻觉的评审意见（带有检测、分类和定位的标注）。

通过利用针对同行评审定制的幻觉分类法、上下文识别以及自动化过滤等强大流程，作者测试了 1,2000 篇论文和 3,8000 篇评审。研究结果表明，现有的检测器很难将幻觉与合理的批评区分开来，这证明了 HalluPeer 定义的模式经常出现在真实同行的评审中，并强调了开发具备源感知（source-aware）验证工具的迫切需求。

---

## Summary

> As Large Language Models (LLMs) increasingly assist with academic peer reviews, they risk generating fluent yet unsupported claims that undermine the reliability of the review process. Existing hallucination benchmarks fall short because reviewing requires deeply grounding claims in long, technical papers. 
> 
> To bridge this gap, researchers introduce **HalluPeer**, a novel benchmark designed to detect hallucinations in scientific peer reviews. HalluPeer provides aligned triples of:
> 1. Original paper content,
> 2. Human-written reviews, and
> 3. Hallucination-injected reviews (annotated for detection, classification, and localization).
> 
> Through a robust pipeline that leverages a peer-review-specific hallucination taxonomy, context identification, and automated filtering, the authors tested 12K papers and 38K reviews. Their findings reveal that current detectors struggle to separate hallucinations from legitimate critiques, proving that HalluPeer-defined patterns frequently occur in authentic peer reviews and emphasizing an urgent need for source-aware verification tools.

---

## Metadata

* **arXiv Identifier:** [arXiv:2609.03580](https://arxiv.org/abs/2609.03580) [cs.AI]
* **Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`)
* **Authors:** 
  * Tzu-Ling Lin
  * Dong-Ting Yao
  * Teng-Fang Hsiao
  * Wei-Chih Chen
  * Hong-Han Shuai
* **Submission Date:** September 3, 2026
* **Comments:** Accepted to EMNLP Findings 2026

---

## Abstract

> The growing scale of academic peer review has motivated the use of Large Language Models (LLMs) as review assistants, yet LLMs can generate fluent but unsupported claims that undermine review reliability. Existing hallucination benchmarks are not designed for peer review, where verification requires grounding claims in long, technical papers. We introduce HalluPeer, a benchmark for detecting hallucinations in scientific peer reviews, providing aligned triples of paper content, human-written reviews, and hallucination-injected reviews, annotated for detection, classification, and localization. Our pipeline induces a peer-review-specific hallucination taxonomy, identifies review contexts, and injects hallucinations with automated filtering. Experiments on 12K papers and 38K reviews show that existing detectors struggle to separate hallucinations from legitimate critique, while evaluation on authentic reviews demonstrates that HalluPeer-defined hallucination patterns occur in real peer reviews, highlighting the critical need for source-aware verification.

---

## Links & Resources

* **Project Page:** [GitHub Repository (HalluPeer)](https://github.com/Lin-TzuLing/HalluPeer.git)
* **Access Paper:**
  * [View PDF](https://arxiv.org/pdf/2609.03580)
  * [HTML Version (Experimental)](https://arxiv.org/html/2609.03580v1)
  * [TeX Source](https://arxiv.org/src/2609.03580)
* **Citations & References:**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03580)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03580)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03580)