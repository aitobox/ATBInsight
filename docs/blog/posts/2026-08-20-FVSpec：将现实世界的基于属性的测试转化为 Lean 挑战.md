---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 形式化验证
- Lean 4
- AI基准测试
- 软件工程
- 属性测试
title: FVSpec：将现实世界的基于属性的测试转化为 Lean 挑战
---
### 文章背景与核心概要
随着人工智能生成了全球越来越多的代码，如何确保这些代码的正确性和安全性变得至关重要。形式化验证虽然是保证软件无瑕疵的黄金标准，但由于门槛高、编写规范繁琐，长期以来难以在工业界大规模普及。为了弥合这一差距，来自学术界的研究人员推出了 FVSpec 这一全新基准测试。

FVSpec 的核心思路是从真实的 Python 代码库中提取基于属性的测试（PBTs），并利用专门设计的三智能体大语言模型（LLM）流水线，自动将其翻译为带有 `sorry` 占位符的 Lean 4 形式化规范。该数据集包含了从 11,039 个真实 PBT 中转化而来的 9,415 个 Lean 4 规范。这项工作不仅攻克了在 Lean 中对 Python 语义建模和推导逻辑不变量的难题，也为评估和推动 AI 在现实世界软件形式化验证领域的发展奠定了重要基础。全部代码和数据集均已开源。

---

# FVSpec: Real-World Property-Based Tests as Lean Challenges

> **arXiv ID:** [2606.01008](https://arxiv.org/abs/2606.01008) [cs.SE]  
> **Subjects:** Software Engineering (`cs.SE`); Artificial Intelligence (`cs.AI`)  
> **Authors:** Quinn Dougherty, Max von Hippel, Simon Henniger, Hazel Shackleton, Mike Dodds  
> **Submission History:** Submitted on 31 May 2026; Last revised 17 Aug 2026 (v2).

> **arXiv ID:** [2606.01008](https://arxiv.org/abs/2606.01008) [cs.SE]  
> **Subjects:** Software Engineering (`cs.SE`); Artificial Intelligence (`cs.AI`)  
> **Authors:** Quinn Dougherty, Max von Hippel, Simon Henniger, Hazel Shackleton, Mike Dodds  
> **Submission History:** Submitted on 31 May 2026; Last revised 17 Aug 2026 (v2).

---

## 📌 Executive Summary

> **FVSpec** 是一个旨在评估 AI 模型和智能体在现实世界形式化软件验证任务中表现的新型基准测试。该基准测试通过从真实世界的 Python 代码库中抓取 11,039 个基于属性的测试（PBT），并自动将其中的四分之一（2,772 个 PBT）翻译为带有 `sorry` 占位符的 9,415 个 Lean 4 形式化规范，从而搭建了命令式编程与形式化方法之间的桥梁。
> 
> 为了实现这一目标，作者开发了一个三智能体 LLM 流水线，以应对在 Lean 4 中建模 Python 语义、从命令式代码中推导逻辑不变量以及处理依赖类型编程复杂性的挑战。整个数据集和流水线均已开源，旨在推动 AI 辅助现实世界代码库形式化验证技术的发展。

> **FVSpec** is a novel benchmark designed to evaluate AI models and agents on real-world formal software verification tasks. The benchmark bridges imperative programming and formal methods by scraping 11,039 property-based tests (PBTs) from real-world Python repositories and automatically translating a quarter of them (2,772 PBTs) into 9,415 Lean 4 formal specifications complete with `sorry` placeholders. 
> 
> To achieve this, the authors developed a three-agent LLM pipeline that tackles the complexities of modeling Python semantics, inferring logical invariants from imperative code, and managing dependently-typed programming in Lean 4. The entire dataset and pipeline are open-sourced to foster advancements in AI-assisted formal verification for real-world codebases.

---

## 🧭 Abstract

> 我们提出了一种用于评估 AI 模型和智能体在现实世界形式化软件验证任务中表现的基准测试。我们首先从真实的 Python 代码库中抓取了 11,039 个基于属性的测试（PBT），然后自动将其中的 2,772 个（25%）翻译为带有 `sorry` 占位符的 9,415 个 Lean 4 规范（平均每个 PBT 约有 3 个形式化版本；当质量指标没有绝对优势时，我们保留了多个尝试结果）。
> 
> 将 PBT 翻译为 Lean 规范具有挑战性：它需要在 Lean 中对 Python 语义进行建模、推导命令式 PBT 中编码的逻辑属性，并处理一种较少使用的语言中依赖类型编程固有的困难。我们描述了一个用于将 PBT 转译为 Lean 规范的三智能体 LLM 流水线，评估了覆盖率和质量指标，并为使用多种自动化和基于模型的方法生成证明提供了基线。
> 
> 所有的代码（爬虫和智能体）以及数据（PBT 和 Lean 规范）均已开源。我们的基准测试旨在推动 AI 辅助现实世界软件形式化验证这一鲜有涉足的问题取得进展，随着 AI 编写了越来越多的世界代码，这一点正受到日益广泛的关注。

> We present a benchmark for evaluating AI models and agents on real-world formal software verification tasks. We first scrape 11,039 property-based tests (PBTs) from real-world Python repositories, then automatically translate 2,772 of them (25%) into 9,415 Lean 4 specifications with sorry placeholders (about 3 formalizations/PBT; we retain multiple attempts when none dominates on quality metrics). 
> 
> Translating PBTs into Lean specifications is challenging: it requires modeling Python semantics in Lean, inferring the logical property encoded in an imperative PBT, and handling the inherent difficulties of dependently-typed programming in a seldom-used language. We describe a three-agent LLM pipeline for transpiling PBTs into Lean specifications, evaluate coverage and quality metrics, and provide baselines for proof generation using several automated and model based approaches. 
> 
> All code (scraper and agents) and data (PBTs and Lean specifications) are open source. Our benchmark aims to drive progress on the underexplored problem of AI-assisted formal verification of real-world software, which is of increasing interest as AI produces more and more of the world's code.

---

## 🔗 Quick Links & Resources

> * **全文访问：** [查看 PDF](https://arxiv.org/pdf/2606.01008) | [实验性 HTML](https://arxiv.org/html/2606.01008v2) | [TeX 源码](https://arxiv.org/src/2606.01008)
> * **文献计量工具：** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.01008) | [谷歌学术](https://scholar.google.com/scholar_lookup?arxiv_id=2606.01008) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.01008)
> * **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) [![license icon](./images/345c7ad61f1b.png)](http://creativecommons.org/licenses/by/4.0/)

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2606.01008) | [Experimental HTML](https://arxiv.org/html/2606.01008v2) | [TeX Source](https://arxiv.org/src/2606.01008)
* **Bibliographic Tools:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.01008) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2606.01008) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.01008)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) [![license icon](./images/345c7ad61f1b.png)](http://creativecommons.org/licenses/by/4.0/)