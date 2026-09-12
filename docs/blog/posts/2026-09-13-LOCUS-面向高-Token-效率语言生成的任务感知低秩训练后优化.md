---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-13
hide:
  - navigation
tags:
  - 大语言模型
  - 偏好对齐
  - Token效率
  - 低秩自适应
  - LOCUS
title: "LOCUS：面向高 Token 效率语言生成的任务感知低秩训练后优化"
---

### 文章背景与核心概要

大语言模型 (LLM) 的线上服务与推理成本直接受制于输出序列的长度。然而，现有的偏好对齐算法（如直接偏好优化 DPO）常常会导致模型输出冗长啰嗦，在并未提升实际回答效用的情况下极大地增加了 Token 消耗。本文深入探索了训练后阶段参数更新对生成长度的影响，发现低秩子空间能够在不损害对齐损失的前提下有效重塑序列长度。为此，作者提出了名为 LOCUS 的任务感知低秩微调框架，在冻结主干网络的同时仅微调约 0.25% 的参数，成功使输出序列长度缩减高达 39.84%，为降低大模型部署成本提供了极具工业实用价值的精简方案。

---

# LOCUS：面向高 Token 效率语言生成的任务感知低秩训练后优化

> # LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation

## 概要

> ## Summary

大语言模型 (Large Language Model, LLM) 的部署服务成本与其输出序列的长度直接相关。然而，主流的偏好对齐技术往往会使模型生成的回复变得冗长啰嗦，而这种啰嗦并没有带来额外的实用价值。本文深入研究了训练后 (Post-Training) 更新的参数化方式如何影响生成长度，并证明低秩子空间能够在不损害对齐损失的前提下显著改变生成序列的长度。

> Large Language Model (LLM) serving costs are directly tied to the length of their output sequences, yet standard preference-alignment techniques frequently inflate response verbosity without providing extra utility. This paper investigates how post-training update parameterization influences generation length, demonstrating that low-rank subspaces can alter sequence length without compromising alignment loss. 

为了遏制生成内容的冗长现象并降低模型推理成本，作者提出了 **LOCUS**，这是一种新颖的方法，通过挑选任务感知的低秩自适应子空间，在满足严格效用约束的同时最大程度降低输出 Token 成本。通过冻结模型主干并在该子空间内沿用原生偏好目标，LOCUS 在 Pythia-2.8B 上实现了高达 39.84% 的生成长度缩减，在 Qwen2.5-3B 上实现了 14.87–17.58% 的缩减，而整个过程仅需更新 0.24–0.28% 的模型参数，同时保持了一致的偏好诊断表现。

> To address verbosity and reduce serving costs, the author introduces **LOCUS**, a novel method that selects a task-aware low-rank adaptation subspace to minimize output-token costs while upholding a strict utility constraint. By keeping the backbone frozen and utilizing the native preference objective within this subspace, LOCUS achieves substantial reductions in continuation length (up to 39.84% on Pythia-2.8B and 14.87–17.58% on Qwen2.5-3B) while updating only 0.24–0.28% of model parameters and maintaining consistent preference diagnostics.

---

## 文档元数据

> ## Document Metadata

* **arXiv ID：** [arXiv:2609.11739](https://arxiv.org/abs/2609.11739) [cs.CL]
* **标题：** LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation
* **作者：** Dongfang Zhao
* **提交日期：** 2026年9月10日
* **主要领域：** 计算与语言 (`cs.CL`)
* **次要领域：** 人工智能 (`cs.AI`)，机器学习 (`cs.LG`)
* **DOI：** [10.48550/arXiv.2609.11739](https://doi.org/10.48550/arXiv.2609.11739)
* **授权协议：** [知识共享署名-非商业性使用-禁止演绎 4.0 国际许可协议 (CC BY-NC-ND 4.0)](http://creativecommons.org/licenses/by-nc-nd/4.0/) *(查看协议图标：<img alt="license icon" role="presentation" src="./images/fb423b2203a9.png" style="vertical-align: middle; display: inline-block; max-height: 20px;" />)*

> * **arXiv ID:** [arXiv:2609.11739](https://arxiv.org/abs/2609.11739) [cs.CL]
> * **Title:** LOCUS: Task-Aware Low-Rank Post-Training for Token-Efficient Language Generation
> * **Author:** Dongfang Zhao
> * **Submitted On:** September 10, 2026
> * **Primary Subject:** Computation and Language (`cs.CL`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Machine Learning (`cs.LG`)
> * **DOI:** [10.48550/arXiv.2609.11739](https://doi.org/10.48550/arXiv.2609.11739)
> * **License:** [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/) *(View license icon: <img alt="license icon" role="presentation" src="./images/fb423b2203a9.png" style="vertical-align: middle; display: inline-block; max-height: 20px;" />)*

---

## 摘要

> ## Abstract

大语言模型的服务成本与输出序列长度直接成正比，但常规的偏好对齐方法常常会在没有提高回复效用的情况下，导致生成文本越发冗长。我们探讨了训练后更新的参数化形式是否会影响生成长度：研究发现，低秩子空间可以在不改变对齐损失的情况下改变序列长度。为此，我们提出了 **LOCUS**，该方法能够在满足效用约束的前提下，挑选任务感知的低秩自适应子空间以最小化输出 Token 成本。

> Large language model serving costs scale directly with output sequence length, yet standard preference alignment often inflates response verbosity without improving utility. We study whether the parameterization of post-training updates affects generation length: low-rank subspaces alter sequence length without modifying the alignment loss. We present **LOCUS**, a method that selects a task-aware low-rank adaptation subspace to minimize output-token cost subject to a utility constraint. 

在该子空间内，训练后优化在冻结主干网络的同时保留了原生的偏好目标。基于 Anthropic HH-RLHF 对话偏好数据集，我们在 Pythia-2.8B 和 Qwen2.5-3B 这两个约 3B 规模的解码器主干网络上进行了评估，对比了协议对齐的全参数直接偏好优化 (Direct Preference Optimization, DPO) 与 DrDPO 分支，以及公开发布的 SamPO 检查点。实验结果显示，LOCUS 在 Pythia-2.8B 上的续写长度缩减了高达 **39.84%**，在 Qwen2.5-3B 上缩减了 **14.87–17.58%**，且仅需更新 **0.24–0.28%** 的模型参数，模型内部的偏好诊断指标亦未发生实质性改变。

> Within this subspace, post-training retains the native preference objective with a frozen backbone. Across Anthropic HH-RLHF dialogue preferences, we evaluate two $\sim$3B decoder backbones, Pythia-2.8B and Qwen2.5-3B, against protocol-matched full-parameter DPO and DrDPO branches and the released SamPO checkpoint. LOCUS reduces continuation length by up to **39.84%** on Pythia-2.8B and by **14.87–17.58%** on Qwen2.5-3B while updating only **0.24–0.28%** of model parameters, with no material change in the internal preference diagnostic.

---

## 获取与资源

> ## Access & Resources

* **全文链接：**
  * [查看 PDF](https://arxiv.org/pdf/2609.11739)
  * [HTML 版本 (实验性)](https://arxiv.org/html/2609.11739v1)
  * [TeX 源码](https://arxiv.org/src/2609.11739)
* **文献与引用工具：**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.11739)
  * [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2609.11739)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.11739)
* **代码、数据与演示：**
  * [Hugging Face](https://huggingface.co/huggingface)
  * [alphaXiv](https://alphaxiv.org/)
  * [CatalyzeX 代码查找](https://www.catalyzex.com)

> * **Full-Text Links:**
>   * [View PDF](https://arxiv.org/pdf/2609.11739)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2609.11739v1)
>   * [TeX Source](https://arxiv.org/src/2609.11739)
> * **Bibliographic & Citation Tools:**
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.11739)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.11739)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.11739)
> * **Code, Data & Demos:**
>   * [Hugging Face](https://huggingface.co/huggingface)
>   * [alphaXiv](https://alphaxiv.org/)
>   * [CatalyzeX Code Finder](https://www.catalyzex.com)
