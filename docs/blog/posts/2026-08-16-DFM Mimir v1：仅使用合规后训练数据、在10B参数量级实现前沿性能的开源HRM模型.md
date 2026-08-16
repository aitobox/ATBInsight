---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-16
hide:
- navigation
tags:
- 大语言模型
- 分层推理模型
- 开源AI
- 数据合规
- 自然语言处理
title: DFM Mimir v1：仅使用合规后训练数据、在10B参数量级实现前沿性能的开源HRM模型
---
### 文章背景与核心概要
当前的语言模型开发往往严重依赖海量且版权存疑的数据集，这给致力于开源和合规数据研究的学者带来了很高的门槛。为了打破这一壁垒，DFM Mimir v1 应运而生。它是一个基于分层推理模型（HRM）架构的 10 亿参数（1B）语言模型，完全从头开始训练，并且仅使用由 161 个混合数据集组成的合规后训练数据。

在技术表现上，Mimir v1 不仅在英语任务上展现出极具竞争力的性能，更在丹麦语上树立了全新的技术先进性（SOTA）标准。在涵盖英语、数学与代码、丹麦语等领域的 20 个不同基准测试中，它成功超越了原版的 HRM-Text 1B，并能与 Qwen 3.5 4B、Gemma 4 E2B 等更大规模的前沿模型展开有力竞争，为开源社区提供了一条兼顾高性能与数据合规的全新路径。

---

# DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters Using Only Permissible Post-Training Data

> DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters Using Only Permissible Post-Training Data

**arXiv:** [arXiv:2608.13517](https://arxiv.org/abs/2608.13517) [cs.CL]  
**Submitted:** August 13, 2026  
**Subjects:** Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`)  
**Authors:** Peter Schneider-Kamp, Jacob Nielsen, Gianluca Barmina, Kenneth Enevoldsen, Lukas Galke Poech  

> **arXiv:** [arXiv:2608.13517](https://arxiv.org/abs/2608.13517) [cs.CL]  
> **Submitted:** August 13, 2026  
> **Subjects:** Computation and Language (`cs.CL`); Artificial Intelligence (`cs.AI`)  
> **Authors:** Peter Schneider-Kamp, Jacob Nielsen, Gianluca Barmina, Kenneth Enevoldsen, Lukas Galke Poech  

---

## 📌 Summary

> 📌 Summary

当前的大语言模型开发通常依赖于海量且往往不具使用许可（非合规）的数据集，这给致力于开源和道德合规数据研究的学者带来了很高的门槛。**Mimir v1** 引入了一种基于**分层推理模型（Hierarchical Reasoning Model, HRM）**架构的 10 亿参数语言模型，对此问题给出了解决方案。Mimir v1 完全从头开始训练，仅使用由 161 个数据集混合而成的合规后训练数据，在英语上实现了极具竞争力的性能，并为丹麦语树立了全新的技术先进性（SOTA）标准。它在 20 个针对英语、数学与代码以及丹麦语的基准测试中表现优异，成功超越了原版的 HRM-Text 1B，并能与诸如 Qwen 3.5 4B 和 Gemma 4 E2B 等更大规模的前沿模型展开有效竞争。

> Current large language model development typically relies on massive, often non-permissible datasets, which creates a high barrier for researchers committed to open-source and ethically sourced data. **Mimir v1** addresses this by introducing a 1-billion-parameter language model based on the **Hierarchical Reasoning Model (HRM)** architecture. Trained entirely from scratch using only permissible post-training data drawn from a mixture of 161 datasets, Mimir v1 achieves highly competitive performance in English and establishes a new state-of-the-art for Danish. It successfully outperforms the original HRM-Text 1B and competes effectively with larger frontier models—such as Qwen 3.5 4B and Gemma 4 E2B—across 20 distinct English, Math & Code, and Danish benchmarks.

---

## 📋 Abstract

> 📋 Abstract

> 当前的大语言模型开发依赖于海量且通常不具使用许可的数据集，这给致力于开源和道德合规数据研究的研究人员构成了很高的门槛。我们推出了 Mimir v1，这是一个基于分层推理模型（HRM）架构的 10 亿参数语言模型。该模型从头开始训练，仅使用合规的后训练数据，就在英语上实现了极具竞争力的性能，并为丹麦语树立了新的技术先进性（SOTA）标准。Mimir v1 在 161 个数据集的混合数据上进行训练，在横跨英语、数学与代码以及丹麦语的 20 个基准测试中，超越了原版的 HRM-Text 1B，并可与 Qwen 3.5 4B 和 Gemma 4 E2B 等更大规模的前沿模型相媲美。

> > Current large language model development relies on massive, often non-permissible datasets, creating a high barrier for researchers committed to open-source and ethically sourced data. We introduce Mimir v1, a 1-billion-parameter language model based on the Hierarchical Reasoning Model (HRM) architecture, that is trained from scratch and delivers highly competitive performance for English and sets a new state of the art for Danish using only permissible post-training data. Trained on a mixture of 161 datasets, Mimir v1 outperforms the original HRM-Text 1B and competes with larger frontier models like Qwen 3.5 4B and Gemma 4 E2B, tested across 20 benchmarks for English, Math & Code and Danish.

---

## 🔗 Resources & Links

> 🔗 Resources & Links

* **模型中心 (Model Hub):** [Hugging Face Hub - DFM-Mimir](https://huggingface.co/danish-foundation-models/DFM-Mimir)
* **全文访问 (Full-Text Access):** 
  * [查看 PDF (View PDF)](https://arxiv.org/pdf/2608.13517)
  * [HTML 版本 - 实验性 (HTML Version (Experimental))](https://arxiv.org/html/2608.13517v1)
  * [TeX 源码 (TeX Source)](https://arxiv.org/src/2608.13517)
* **DOI:** [10.48550/arXiv.2608.13517](https://doi.org/10.48550/arXiv.2608.13517)

> * **Model Hub:** [Hugging Face Hub - DFM-Mimir](https://huggingface.co/danish-foundation-models/DFM-Mimir)
> * **Full-Text Access:** 
>   * [View PDF](https://arxiv.org/pdf/2608.13517)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.13517v1)
>   * [TeX Source](https://arxiv.org/src/2608.13517)
> * **DOI:** [10.48550/arXiv.2608.13517](https://doi.org/10.48550/arXiv.2608.13517)

---

## 📚 Citation & References

> 📚 Citation & References

* **BibTeX:** 可通过 [arXiv 摘要页面](https://arxiv.org/abs/2608.13517) 获取
* **外部引用 (External Citations):**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.13517)
  * [Google Scholar (谷歌学术)](https://scholar.google.com/scholar_lookup?arxiv_id=2608.13517)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.13517)

> * **BibTeX:** Available via the [arXiv Abstract Page](https://arxiv.org/abs/2608.13517)
> * **External Citations:**
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.13517)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.13517)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.13517)