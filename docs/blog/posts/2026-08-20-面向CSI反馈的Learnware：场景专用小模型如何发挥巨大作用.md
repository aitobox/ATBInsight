---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 6G
- CSI反馈
- Learnware
- 深度学习
- 无线通信
title: 面向CSI反馈的Learnware：场景专用小模型如何发挥巨大作用
---
### 文章背景与核心概要
智能信道状态信息（CSI）反馈对于实现未来6G系统的高容量和高频谱效率至关重要。然而，传统的深度学习解决方案在泛化能力和性能之间存在权衡：大型神经网络虽然泛化能力强，但计算和微调成本高昂；而小模型在特定环境中表现出色，但需要为每个基站（BS）进行昂贵且重复的端到端训练。

为了克服这些障碍，本文提出了一种基于Learnware（可复用构件）的模型库部署框架。该框架不直接传输原始CSI数据或从头开始训练模型，而是由集中式AI数据中心维护一个场景专用的CSI模型目录。每个模型都附带一个规范（Specification），包含表示网络架构参数的语义部分和表示训练数据分布的代码本指纹嵌入的统计部分。基站只需提交本地统计规范即可准确检索出最相关的预训练模型，在保护数据隐私的同时，最大程度地减少了延迟和通信开销。

仿真结果表明，该数据驱动的搜索策略匹配代码本指纹与模型性能的选择准确率超过了90%。与通用模型相比，该方案在视距（LOS）场景下性能提升了18.8%，在非视距（NLOS）场景下提升了57.7%，同时将本地微调需求最多减少了1,000个样本和100个训练轮次。

---

# Learnware for CSI Feedback: Scene-specific Small Models Can Do Big

**arXiv ID:** [2608.17760](https://arxiv.org/abs/2608.17760)  
**Subjects:** Information Theory (`cs.IT`); Artificial Intelligence (`cs.AI`); Signal Processing (`eess.SP`)  
**Accepted by:** *IEEE Transactions on Wireless Communications*  
**Submission Date:** August 18, 2026  

---

## Authors
* Xiangyi Li
* Jiajia Guo
* Chao-Kai Wen
* Xin Geng
* Shi Jin
* Zhi-Hua Zhou

---

## Summary

智能信道状态信息（CSI）反馈对于实现未来6G系统的高容量和高频谱效率至关重要。然而，传统的深度学习解决方案在泛化能力和性能之间存在权衡：
* **大型神经网络**泛化能力强，但计算和微调成本高。
* **小模型**在特定环境中表现卓越，但需要为每个基站（BS）进行成本高昂且重复的端到端训练。

为了克服这些障碍，本文提出了一种**基于Learnware的模型库部署框架**。集中式AI数据中心不再传输原始CSI数据或从头训练模型，而是维护一个场景专用的CSI模型目录。每个模型都附带一个规范，包含：
1. **语义部分：** 网络架构参数。
2. **统计部分：** 代表训练数据分布的代码本指纹嵌入（codebook-fingerprint embeddings）。

通过仅提交本地统计规范，基站可以准确检索出最相关的预训练模型——在保护数据隐私的同时，最大限度地减少延迟和通信开销。

### 核心亮点与结果
* **高选择准确率：** 数据驱动的搜索策略将代码本指纹与模型性能相匹配，选择准确率超过 **90%**。
* **性能提升：** 仿真表明，与通用模型相比，该方案取得了显著改进——在视距（LOS）场景下提升 **18.8%**，在非视距（NLOS）场景下提升 **57.7%**。
* **降低训练开销：** 该方法将本地微调需求最多减少了 **1,000个样本** 和 **100个训练轮次（epochs）**。

> Intelligent channel state information (CSI) feedback is crucial for achieving high capacity and spectral efficiency in future 6G systems. However, traditional deep learning solutions suffer from a trade-off between generalization and performance:
> * **Large neural networks** generalize well but require high computational and tuning costs.
> * **Small models** perform exceptionally in specific environments but require costly, repetitive end-to-end training for every base station (BS).
> 
> To overcome these hurdles, this paper proposes a **Learnware-based repository deployment framework**. Instead of transmitting raw CSI data or training models from scratch, a centralized AI data center maintains a catalog of scene-specific CSI models. Each model comes with a specification consisting of:
> 1. **A semantic part:** Network architecture parameters.
> 2. **A statistical part:** Codebook-fingerprint embeddings representing training-data distributions.
> 
> By submitting only local statistical specifications, a base station can accurately retrieve the most relevant pre-trained model—preserving data privacy while minimizing latency and communication overhead. 
> 
> ### Key Highlights & Results
> * **High Selection Accuracy:** A data-driven search strategy matches codebook fingerprints to model performance with over **90% selection accuracy**.
> * **Performance Gains:** Simulations demonstrate substantial improvements over General Models—**18.8%** in Line-of-Sight (LOS) scenarios and **57.7%** in Non-Line-of-Sight (NLOS) scenarios.
> * **Reduced Training Overhead:** The approach reduces local fine-tuning requirements by up to **1,000 samples** and **100 epochs**.

---

## Abstract

> 为了实现未来6G系统的高容量和高频谱效率目标，智能信道状态信息（CSI）反馈至关重要，然而现有的深度学习解决方案面临着模型泛化能力与场景专用性能之间的权衡。大型神经网络泛化能力好，但会带来高昂的计算和微调成本，而小模型在特定环境中表现优异，但需要为每个基站（BS）进行重复且昂贵的端到端训练。
>
> 为了解决这些挑战，我们引入了一种基于模型库的部署框架，其中集中式AI数据中心维护着一个场景专用的CSI模型目录。该模型库通过基于Learnware的框架进行增强，其中每个模型都与一个规范相关联，该规范包括语义部分（网络架构参数）和统计部分（训练数据分布的代码本指纹嵌入）。基站仅提交其本地统计规范即可检索最相关的预训练模型，通过避免原始CSI传输来增强数据隐私，并大大减少检索延迟和通信开销。
>
> 我们进一步开发了一种数据驱动的搜索策略，将代码本指纹与模型性能相匹配，实现了超过90%的选择准确率。在仿真中，我们的方案在LOS和NLOS场景下分别比通用模型带来18.8%和57.7%的性能提升，同时将本地微调减少了最多1000个样本和100个训练轮次。这种基于Learnware的方法最大限度地减少了冗余训练，最大化了模型复用，并支持快速且保护隐私的CSI反馈模型部署。

> Intelligent channel state information (CSI) feedback is essential for realizing the high capacity and spectral efficiency goals of future 6G systems, yet existing deep learning solutions face a trade-off between model generalization and scenario-specific performance. Large neural networks generalize well but incur high computational and tuning costs, while small models excel in particular environments but require repetitive costly end-to-end training for each base station (BS). 
>
> To address these challenges, we introduce a model repository-based deployment framework in which a centralized AI data center maintains a catalog of scene-specific CSI models. The repository is enhanced with a Learnware-based framework, where each model is associated with a specification including semantic part (network architecture parameters) and statistical part (codebook-fingerprint embeddings of training-data distributions). A BS submits only its local statistical specifications to retrieve the most relevant pre-trained model, enhancing data privacy by avoiding raw CSI transmission and drastically reducing retrieval latency and communication overhead. 
>
> We further develop a data-driven search strategy that matches codebook fingerprints to model performance, achieving over 90% selection accuracy. In simulations, our scheme yields 18.8% and 57.7% performance improvements over the General Model in LOS and NLOS scenarios, respectively while reducing local fine-tuning by up to 1000 samples and 100 epochs. This Learnware-based approach minimizes redundant training, maximizes model reuse, and supports rapid, privacy-enhancing deployment of CSI feedback models.

---

## Full-Text & Reference Links

* **View PDF:** [arXiv:2608.17760 PDF](https://arxiv.org/pdf/2608.17760)
* **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.17760v1)
* **Source Code/Files:** [TeX Source](https://arxiv.org/src/2608.17760)
* **Citations & Metrics:** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.17760)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.17760)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.17760)