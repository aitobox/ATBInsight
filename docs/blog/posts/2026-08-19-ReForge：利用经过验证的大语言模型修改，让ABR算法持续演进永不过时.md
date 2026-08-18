---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 大语言模型
- 自适应比特率
- 持续学习
- 网络流媒体
- 启发式规则
title: ReForge：利用经过验证的大语言模型修改，让ABR算法持续演进永不过时
---
### 文章背景与核心概要
传统的自适应比特率（ABR）视频流传输算法随着网络环境从3G演进到4G、5G及更高版本，往往会迅速过时。为了解决这一局限性，作者推出了 **ReForge**，这是一个由大语言模型（LLM）驱动的持续启发式学习框架。ReForge允许ABR算法在几分钟内持续适应新的网络场景，同时不会降低先前已学习环境中的性能。通过在路由规则中采用经过验证的“LLM闭环”编辑机制，ReForge超越了静态人工设计和单策略模型，实现了接近全知（oracle）的性能。

本文提出了一种全新的范式：利用大语言模型对控制策略的模糊规则页面进行持续的微小编辑，并通过对历史所有已知网络场景进行回放验证，确保每次改动都不会破坏既有性能。实验表明，ReForge在面对不断演进的真实网络家族时表现出色，不仅大幅提升了平均QoE（体验质量），还能修复模型未曾直接见过的场景，展现出极强的泛化与持续演进能力。

---

# ReForge: Keeping ABR Algorithms Never Finished with Verified Large Language Model Edits

**arXiv:** [2608.15138](https://arxiv.org/abs/2608.15138) [cs.AI]  
**Authors:** Zhiqiang He, Zhi Liu  
**Submitted:** August 15, 2026  

---

## 📌 Summary

传统自适应比特率（ABR）视频流算法随着网络环境从 3G 演进到 4G、5G 及更高级别，很快就会变得过时。为了解决这一局限性，作者引入了 **ReForge**，这是一个由大语言模型（LLM）驱动的持续启发式学习框架。ReForge 允许 ABR 算法在几分钟内持续适应新的网络场景，同时不会降低先前已学环境中的性能。通过在路由规则中采用经过验证的 LLM 闭环编辑机制，ReForge 的表现超越了静态手工设计和单策略模型，达到了接近全知（oracle）的性能。

> Traditional Adaptive Bitrate (ABR) video streaming algorithms quickly become obsolete as network environments evolve from 3G to 4G, 5G, and beyond. To solve this limitation, the authors introduce **ReForge**, a continual heuristic learning framework powered by Large Language Models (LLMs). ReForge allows an ABR algorithm to continuously adapt to new network scenarios in minutes without degrading performance on previously learned environments. By employing a verified LLM-in-the-loop editing mechanism over routing rules, ReForge outperforms static hand-built designs and single-policy models, achieving near-oracle performance.

---

## 📖 Abstract

为单一网络场景设计一个 ABR 算法需要工程师花费数月时间，而现在大语言模型可以在几小时内完成这项工作，其效果足以媲美甚至超越手工设计的方案。但无论采用哪种方式，设计出来的方案都只契合其诞生时可见的世界，而无法适应随后出现的新世界。我们不禁要问：ABR 算法能否跟上世界的步伐，在每个新场景到来时于几分钟内完成重新设计，并且确保每一次改动都被证明对所有已经服务过的场景无害？

> Designing an ABR algorithm for one network scenario takes an engineer months, and large language models now do this work in hours, matching or beating hand-built designs. But either way, the design fits only the world visible at its birth, and fails on the world that arrives after. We ask whether an ABR algorithm can keep pace with the world, redesigned in minutes as each scenario arrives, with every change proven harmless to every scenario already served. 

在这项工作中，我们提出了 **ReForge**，这是一个能够适应不断变化场景的持续启发式学习框架。ReForge 在循环中引入大语言模型（LLM）来运行该常规流程。每一轮中，LLM 会读取当前设计的不足之处并提出一个微小的修改建议，然后通过对迄今为止服务过的所有网络进行回放来决定是否采纳。具体而言，它编辑的是单页模糊规则，这些规则将每个决策路由到一个冻结的预训练策略池中的某个策略。LLM 仅根据测量数据编写第一页规则，然后由其自主不断改进。每一轮它都会读取当前规则的不足并提出一个小修改，通过对迄今为止服务过的所有网络进行回放，来决定该修改是否能够落地。

> In this work, we propose **ReForge**, a continual heuristic learning framework that adapts to continuously changing scenarios. ReForge runs that routine with a large language model (LLM) in the loop. Each round the LLM reads where the current design falls short and proposes one small edit, and a replay over every network served so far decides. Specifically, what it edits is a single page of fuzzy rules that routes every decision to one of a frozen pool of pre-trained policies. The LLM writes the first page from measurements alone, then keeps improving it on its own. Each round it reads where the current rules fall short and proposes one small edit, and a replay over every network served so far decides whether the edit lands. 

我们在依次出现的九个真实世界网络家族（依次为 3G、4G、然后是 5G）上评估了 ReForge。每次网络环境到来时进行几次修改，就将平均 QoE 从 1.23 提升至 1.74，超越了最佳单策略的 1.66，达到了全知（oracle）性能的 94%，甚至修复了循环从未见过的网络家族（其中一个家族的指标从 0.30 跃升至 0.80）。所有代码、数据和实验记录将在清理后开源。

> We evaluate ReForge on nine real-world network families arriving one at a time as 3G, 4G, then 5G. A few edits per arrival lift mean QoE from 1.23 to 1.74, past the best single policy at 1.66 and to 94% of an oracle, and even repair families the loop never saw, one rising from 0.30 to 0.80. All code, data, and experiment records will be open-sourced upon cleanup.

---

## 🔗 Additional Resources & Links

* **查看 PDF:** [arXiv:2608.15138 PDF](https://arxiv.org/pdf/2608.15138)
* **HTML 版本:** [arXiv HTML 实验版](https://arxiv.org/html/2608.15138v1)
* **DOI:** [10.48550/arXiv.2608.15138](https://doi.org/10.48550/arXiv.2608.15138)
* **外部引用:** [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2608.15138) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.15138) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.15138)

> * **View PDF:** [arXiv:2608.15138 PDF](https://arxiv.org/pdf/2608.15138)
> * **HTML Version:** [arXiv HTML Experimental](https://arxiv.org/html/2608.15138v1)
> * **DOI:** [10.48550/arXiv.2608.15138](https://doi.org/10.48550/arXiv.2608.15138)
> * **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.15138) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.15138) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.15138)