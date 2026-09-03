---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-04
hide:
- navigation
tags:
- 联邦学习
- 视觉语言模型
- 医疗影像
- LoRA
- BiomedCLIP
title: 跨四个国际胸部X光队列的BiomedCLIP联邦LoRA自适应研究
---
### 文章背景与核心概要
本文探讨了利用联邦学习（FL）结合低秩自适应（LoRA）技术，多机构协同训练多模态视觉语言模型（具体为 BiomedCLIP）用于胸部X光片分类的方法。通过对横跨三大洲（美国、越南和西班牙）的四个公开国际队列进行评估，该研究证明了联邦参数高效微调（PEFT）能够在确保数据隐私的前提下打破机构壁垒，应对数据异构性（不同的扫描仪、协议和计算能力），并在显著优于零样本基线和孤立单队列训练的同时，逼近集中式训练的性能基准。

这项研究对于医疗人工智能领域具有重要意义。随着多模态基础模型在医疗影像分析中的作用日益凸显，如何在不共享原始敏感患者数据的前提下实现协同适配，一直是行业痛点。本文所验证的“联邦LoRA”策略不仅大幅提升了模型的泛化能力和公平性，也为未来跨医疗机构的隐私保护型AI协作提供了切实可行的技术路径。

---

# Federated LoRA Adaptation of BiomedCLIP Across Four International Chest X-Ray Cohorts

**arXiv:** [arXiv:2609.02101](https://arxiv.org/abs/2609.02101) [cs.LG]  
**Submitted:** September 2, 2026  
**Primary Subject:** Machine Learning (`cs.LG`)  
**Authors:** Sanjaya Poudel, Nirajan Kunwor, Manish Dhakal, Debesh Jha, Sunil Kumar Gaire  

---

## 执行摘要

本文探讨了利用联邦学习（FL）结合低秩自适应（LoRA）技术，协同训练用于胸部X光片分类的多模态视觉语言模型——具体为 **BiomedCLIP**。通过跨越三大洲（美国、越南和西班牙）的四个公共国际队列评估，该研究证明了联邦参数高效微调（PEFT）能够安全地跨越机构壁垒，解决数据异构性问题（不同的扫描仪、协议和计算环境），并显著优于零样本基线以及孤立的单队列训练，同时接近了集中式的性能基准。

> ## Executive Summary
> 
> This paper investigates the collaborative training of multimodal vision-language models—specifically **BiomedCLIP**—for chest radiograph classification using **Federated Learning (FL)** combined with **Low-Rank Adaptation (LoRA)**. By evaluating across four public international cohorts spanning three continents (USA, Vietnam, and Spain), the study demonstrates that federated parameter-efficient fine-tuning (PEFT) securely bridges institutional boundaries, addresses data heterogeneity (varying scanners, protocols, and compute), and significantly outperforms both zero-shot baselines and isolated single-cohort training while approaching centralized performance benchmarks.

---

## 1. 引言与动机

* **隐私挑战：** 生物医学影像中的患者数据受到严格监管，并被隔离在机构防火墙之内，这使得直接的数据集中化变得不可能。
* **机构异构性：** 各医院和研究中心在本地影像扫描仪、采集协议以及可用的计算基础设施方面存在巨大差异。
* **视觉语言模型的作用：** 随着 BiomedCLIP 等多模态基础模型成为医疗影像分析的核心，寻找在不共享原始数据的前提下对其进行协同适配的高效方法已成为当务之急。

> ## 1. Introduction & Motivation
> 
> * **The Privacy Challenge:** Patient data in biomedical imaging are strictly regulated and archived behind institutional firewalls, preventing direct data centralization.
> * **Institutional Heterogeneity:** Hospitals and research centers differ vastly in their local imaging scanners, acquisition protocols, and available compute infrastructure.
> * **The Role of Vision-Language Models:** As multimodal foundation models like BiomedCLIP become central to medical image analysis, finding efficient ways to adapt them collaboratively without sharing raw data is an urgent priority.

---

## 2. 方法论与途径

* **联邦学习（FL）：** 允许不同的机构在不交换私密患者记录的情况下协同训练共享模型。
* **低秩适配（LoRA）：** 仅传输紧凑的低秩参数更新，而不是完整的网络权重，从而使大规模联邦学习变得切实可行。
* **聚合策略：** 
  * **FlexLoRA：** 采用了基于奇异值分解（SVD）乘积空间聚合的方法，实践证明这对性能提升至关重要。
  * **朴素因子平均（Naive Factor Averaging）：** 导致性能显著下降（平均 AUC 下降 0.097）。
  * **FedProx 对比 FedAvg：** 作为纠偏优化器进行评估时，在单随机种子运行中，FedProx 并未表现出明显优于标准 FedAvg 的优势，这表明 LoRA 固有的低秩更新自然地限制了客户端漂移。

> ## 2. Methodology & Approach
> 
> * **Federated Learning (FL):** Allows distinct institutions to train a shared model collaboratively without exchanging private patient records.
> * **Low-Rank Adaptation (LoRA):** Makes FL practical at scale by communicating only compact, low-rank parameter updates rather than full network weights.
> * **Aggregation Strategies:** 
>   * **FlexLoRA:** Utilizes Singular Value Decomposition (SVD)-based product-space aggregation, which proved **essential** to performance gains.
>   * **Naive Factor Averaging:** Led to a significant drop in performance (reducing mean AUC by 0.097).
>   * **FedProx vs. FedAvg:** Evaluated as a drift-correcting optimizer, FedProx showed no distinct advantage over standard FedAvg in single-seed runs, suggesting that LoRA's inherent low-rank updates naturally restrict client drift.

---

## 3. 关键发现与结果

* **性能提升：** 与未适配的 BiomedCLIP 主干网络相比，联邦 LoRA 适配提升了所有四个队列上的共享类别 AUC，将平均 AUC 从 **0.687 提高到 0.802**。这证实了性能的提升来自于协同的联邦适配，而非预训练模型的零样本能力。
* **普惠性收益：** 相对于孤立的单队列训练，联邦学习显著提升了较弱队列的性能，同时保持了最强队列的高性能。
* **逼近集中式效果：** 联邦方法非常接近完全集中的参考基线（该基线汇集了所有数据，产生的 AUC 为 **0.812**）。

> ## 3. Key Findings & Results
> 
> * **Performance Improvement:** Federated LoRA adaptation elevated the shared-class AUC across all four cohorts compared to the unadapted BiomedCLIP backbone, raising the mean AUC from **0.687 to 0.802**. This confirms that improvements stem from collaborative federated adaptation rather than the pretrained model's zero-shot capabilities.
> * **Equitable Benefits:** Relative to isolated, single-cohort training, federation notably uplifted weaker cohorts while preserving the high performance of the strongest cohorts.
> * **Centralized Approximation:** The federated approach closely approached a fully centralized reference baseline (which pooled all data together, yielding an AUC of **0.812**).

---

## 4. 结论

利用联邦 LoRA 技术，生物医学视觉语言模型能够在异构的、地理上分散的机构之间实现成功且协同的适配——完全消除了集中敏感患者数据的需求。

> ## 4. Conclusion
> 
> Biomedical vision-language models can be successfully and collaboratively adapted across heterogeneous, geographically distributed institutions using federated LoRA—entirely removing the need to centralize sensitive patient data.

---

## 资源链接

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2609.02101) | [HTML（实验性）](https://arxiv.org/html/2609.02101v1) | [TeX 源码](https://arxiv.org/src/2609.02101)
* **数字对象唯一标识符（DOI）：** [10.48550/arXiv.2609.02101](https://doi.org/10.48550/arXiv.2609.02101)
* **许可协议：** [知识共享署名 4.0 国际版](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

> ## Resource Links
> 
> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2609.02101) | [HTML (Experimental)](https://arxiv.org/html/2609.02101v1) | [TeX Source](https://arxiv.org/src/2609.02101)
> * **Digital Object Identifier (DOI):** [10.48550/arXiv.2609.02101](https://doi.org/10.48550/arXiv.2609.02101)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)