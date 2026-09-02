---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- 计算心理语言学
- Transformer
- 能量模型
- Hopfield网络
- 阅读时间预测
title: 基于能量的 Transformer 作为阅读难度预测指标
---
### 文章背景与核心概要
本文探讨了将基于能量的 Transformer（Energy-Based Transformers）作为预测人类阅读难度的新型计算心理语言学指标。通过将 Transformer 模型与诸如 Hopfield 网络等联想记忆框架联系起来，作者证明了基于能量的度量能够稳健地预测三个主要语料库（《自然故事》、UCL 眼动追踪和 UCL 自定步速阅读）中的阅读时间，其性能优于惊异度（surprisal）和注意力熵（attention entropy）等标准指标。

此外，该能量度量成功捕捉到了关系从句处理中经典的宾语/主语不对称性现象，这表明它有望成为一个统一的预测指标，而在过去则需要多个指标协同才能实现类似效果。该研究已被计算语言学顶级会议 EMNLP 2026 主会接收。

> This paper investigates **energy-based transformers** as novel computational psycholinguistic predictors of human reading difficulty. Connecting transformer models to associative memory frameworks like Hopfield networks, the authors demonstrate that an energy-based measure robustly predicts reading times across three major corpora (*Natural Stories*, *UCL eye-tracking*, and *UCL self-paced reading*), outperforming standard metrics like surprisal and attention entropy. Furthermore, the energy measure successfully captures the classic object/subject asymmetry in relative clause processing, suggesting it can serve as a unified predictor where multiple metrics were previously required. 
> 
> *(Accepted to **EMNLP 2026**, Main Conference)*

---

## 论文元数据 (Paper Metadata)

* **arXiv ID:** [arXiv:2606.23382](https://arxiv.org/abs/2606.23382) [cs.CL]
* **作者 (Authors):** Jakub Dotlacil, Ece Takmaz
* **研究方向 (Subjects):** 计算与语言 (`cs.CL`); 人工智能 (`cs.AI`)
* **提交历史 (Submission History):** 
  * [v1] 2026年6月22日，周一
  * [v2] 2026年9月1日，周二 *(最后修订)*
* **全文与资源 (Full-Text & Resources):** 
  * [查看 PDF](https://arxiv.org/pdf/2606.23382)
  * [HTML 版本](https://arxiv.org/html/2606.23382v2)
  * [TeX 源码](https://arxiv.org/src/2606.23382)
  * [查看许可](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" />

---

## 摘要 (Abstract)

Transformer 语言模型已成为建模人类句子处理的成熟工具，其中的惊异度（surprisal）和注意力熵（attention entropy）等度量已成为阅读难度的有效预测指标，它们共同捕捉了处理负荷的互补方面。

在本文中，我们探讨了一类相关的 Transformer 模型：**基于能量的 Transformer（energy-based transformers）**，它为联想记忆模型提供了有原则的形式化联系，使处理研究能够与关于 Hopfield 网络和稠密联想记忆的更广泛文献直接对接。据我们所知，这是在计算心理语言学中首次对基于能量的 Transformer 度量进行探索。

在多个阅读时间语料库（《自然故事》、UCL 眼动追踪、UCL 自定步速阅读）中，能量度量表现出了对阅读时间的稳健预测能力，在所有三个语料库中都提供了超越惊异度和熵的显著模型拟合度。在关于关系从句处理的对照实验中，单层网络中的能量值成功捕捉到了众所周知的宾语/主语不对称性。我们发现证据表明，它能够涵盖同时归因于注意力熵和惊异度的效应，这表明在以往需要多个互补度量的情况下，能量有望作为一个单一的统一预测指标。

> Transformer language models have become established tools for modeling human sentence processing, with measures such as surprisal and attention entropy serving as effective predictors of reading difficulty that together capture complementary aspects of processing load. 
> 
> Here, we explore a related class of transformer models: **energy-based transformers**, which provide a principled formal link to associative memory models, bringing processing research into direct contact with the broader literature on Hopfield networks and dense associative memory. To our knowledge, this is the first exploration of an energy-based transformer measure in computational psycholinguistics. 
> 
> Across reading-time corpora (*Natural Stories*, *UCL eye-tracking*, *UCL self-paced reading*), the energy measure is a robust predictor of reading times, providing significant fit beyond surprisal and entropy in all three. In a controlled experiment on relative clause processing, energy at a single layer captures the well-known object/subject asymmetry. We find evidence that it subsumes effects attributable to both attention entropy and surprisal, suggesting that energy may serve as a single unified predictor where multiple complementary measures have previously been required.