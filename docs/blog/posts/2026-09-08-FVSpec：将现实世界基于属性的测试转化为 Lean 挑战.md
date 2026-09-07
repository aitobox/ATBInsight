---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-08
hide:
- navigation
tags:
- 形式化验证
- Lean 4
- AI编程
- 基准测试
- 软件工程
title: FVSpec：将现实世界基于属性的测试转化为 Lean 挑战
---
### 文章背景与核心概要

随着人工智能模型生成的代码在全球代码库中所占比例不断增加，对严谨的软件验证工具的需求也随之增长。为了解决这一领域评估基准匮乏的问题，作者推出了 **FVSpec**，这是一个旨在评估 AI 模型和智能体在真实世界形式化软件验证任务中表现的新型基准。

FVSpec 通过以下方式架起了动态测试与形式化证明之间的桥梁：首先从真实的 Python 代码库中抓取了 **11,039 个基于属性的测试（PBT）**；接着自动将其中的 **2,772 个（占 25%）** 转化为带有 `sorry` 占位符的 **9,415 个 Lean 4 规范**；并利用一个专用的 **三智能体大模型流水线** 来处理命令式 Python 语义转换以及属性推断等高难度任务，将其转化为依赖类型（dependently-typed）的 Lean 4 代码。

所有的相关代码（爬虫和智能体）以及数据集（PBT 和 Lean 规范）均已完全开源，旨在推动 AI 辅助形式化软件验证未来研究的发展。

---

## 📌 Summary

> As AI models generate an increasing share of the world's code, the demand for rigorous software verification tools grows. To address the scarcity of evaluation benchmarks in this space, the authors introduce **FVSpec**, a novel benchmark designed to evaluate AI models and agents on real-world formal software verification tasks. 
> 
> FVSpec bridges the gap between dynamic testing and formal proofs by:
> 1. Scraping **11,039 property-based tests (PBTs)** from real-world Python repositories.
> 2. Automatically translating **2,772 of them (25%)** into **9,415 Lean 4 specifications** equipped with `sorry` placeholders.
> 3. Leveraging a specialized **three-agent LLM pipeline** to handle the difficult translation of imperative Python semantics and property inference into dependently-typed Lean 4 code.
> 
> All associated code (scrapers and agents) and datasets (PBTs and Lean specifications) are fully open-source to drive future research in AI-assisted formal software verification.

---

## 📖 Abstract

> We present a benchmark for evaluating AI models and agents on real-world formal software verification tasks. We first scrape 11,039 property-based tests (PBTs) from real-world Python repositories, then automatically translate 2,772 of them (25%) into 9,415 Lean 4 specifications with sorry placeholders (about 3 formalizations/PBT; we retain multiple attempts when none dominates on quality metrics). Translating PBTs into Lean specifications is challenging: it requires modeling Python semantics in Lean, inferring the logical property encoded in an imperative PBT, and handling the inherent difficulties of dependently-typed programming in a seldom-used language. We describe a three-agent LLM pipeline for transpiling PBTs into Lean specifications, evaluate coverage and quality metrics, and provide baselines for proof generation using several automated and model based approaches. All code (scraper and agents) and data (PBTs and Lean specifications) are open source. Our benchmark aims to drive progress on the underexplored problem of AI-assisted formal verification of real-world software, which is of increasing interest as AI produces more and more of the world's code.

我们提出了一个用于评估 AI 模型和智能体在现实世界形式化软件验证任务中表现的基准。我们首先从真实的 Python 代码库中抓取了 11,039 个基于属性的测试（PBT），然后自动将其中的 2,772 个（25%）转化为带有 sorry 占位符的 9,415 个 Lean 4 规范（大约每个 PBT 对应 3 个形式化版本；当质量指标不分高下时，我们保留了多个尝试版本）。将 PBT 转化为 Lean 规范具有挑战性：它需要在 Lean 中建模 Python 语义，推断命令式 PBT 中编码的逻辑属性，并处理在较少使用的语言中进行依赖类型编程的固有困难。我们描述了一个用于将 PBT 转译为 Lean 规范的三智能体大模型流水线，评估了覆盖率和质量指标，并为使用多种自动化和基于模型的方法生成证明提供了基准。所有代码（爬虫和智能体）以及数据（PBT 和 Lean 规范）均已开源。我们的基准旨在推动 AI 辅助真实世界软件形式化验证这一尚未充分探索的问题取得进展，随着 AI 生成越来越多的全球代码，该问题正受到日益增长的关注。

---

## 🛠️ Metadata & Resources

* **Primary Subject:** Software Engineering (`cs.SE`)
* **Secondary Subject:** Artificial Intelligence (`cs.AI`)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
* **Full-Text Links:**
  * [View PDF](https://arxiv.org/pdf/2606.01008)
  * [HTML Version (Experimental)](https://arxiv.org/html/2606.01008v3)
  * [TeX Source](https://arxiv.org/src/2606.01008)
* **External Indices & Citations:**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.01008)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2606.01008)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.01008)

* **主要学科：** 软件工程 (`cs.SE`)
* **次要学科：** 人工智能 (`cs.AI`)
* **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
* **全文链接：**
  * [查看 PDF](https://arxiv.org/pdf/2606.01008)
  * [HTML 版本（实验性）](https://arxiv.org/html/2606.01008v3)
  * [TeX 源码](https://arxiv.org/src/2606.01008)
* **外部索引与引用：**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.01008)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2606.01008)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.01008)