---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 蛋白质折叠
- 多智能体系统
- 代码生成
- 蒙特卡洛树搜索
- 科学机器学习
title: AgentFold：用于蛋白质折叠模型设计的闭环智能体搜索
---
### 文章背景与核心概要
本文介绍了 **AgentFold**，这是一个旨在自主改进复杂科学机器学习系统（特别是蛋白质折叠模型）的多智能体框架。该框架通过可执行的代码修改和严格的计算验证，突破了传统科学大语言智能体主要停留在文献推理和工具调用的局限。

AgentFold 基于一个包含 2000 多行代码的 **ESMFold** 代码库构建，利用类似蒙特卡洛树搜索（MCTS）的策略，通过闭环的假设生成、调试、评估和结构化记忆保留，探索了大约 80 个模型变体。在同等的计算预算下（约 5000 GPU 小时和 1.7 亿个大语言模型 Token），与独立 Codex 方案和随机搜索对照组相比，AgentFold 将最佳局部距离差测验（lDDT）得分提升了 **7.5%**。

此外，该研究的干预轨迹揭示了宝贵的经验设计模式：稳定的架构改进通常源于早期、软性的、可学习的先验以及门控求精机制，而直接的几何扰动往往会破坏训练的稳定性。

---

# AgentFold: Closed-Loop Agentic Search for Protein Folding Model Design

## Summary

> **AgentFold** is a multi-agent framework designed to autonomously improve complex scientific machine learning systems—specifically protein folding models—through executable code changes and rigorous computational validation. Built around an **ESMFold** codebase of over 2,000 lines, AgentFold uses a Monte Carlo Tree Search (MCTS)-style policy to explore approximately 80 model variants via closed-loop hypothesis generation, debugging, evaluation, and structured memory retention. 
> 
> Operating under a matched computational budget (~5,000 GPU-hours and 170 million LLM tokens), AgentFold improves the best local Distance Difference Test (lDDT) score by **7.5%** over independent Codex proposals and significantly outperforms random-search controls. Furthermore, its intervention traces uncover valuable empirical design patterns: stable architectural improvements generally stem from early, soft, learnable priors and gated refinement, whereas direct geometric perturbations often destabilize training.

**AgentFold** 是一个多智能体框架，旨在通过可执行的代码修改和严格的计算验证，自主改进复杂的科学机器学习系统——特别是蛋白质折叠模型。AgentFold 围绕一个超过 2,000 行代码的 **ESMFold** 代码库构建，采用蒙特卡洛树搜索（MCTS）风格的策略，通过闭环的假设生成、调试、评估和结构化记忆保留，探索了大约 80 个模型变体。

在匹配的计算预算下（约 5,000 GPU 小时和 1.7 亿个 LLM Token），与独立的 Codex 提案相比，AgentFold 将最佳局部距离差测验（lDDT）得分提高了 **7.5%**，并显著优于随机搜索对照组。此外，其干预轨迹揭示了宝贵的经验设计 patterns（设计模式）：稳定的架构改进通常源于早期、软性的、可学习的先验以及门控求精机制，而直接的几何扰动往往会破坏训练的稳定性。

---

## Metadata & Reference Information

> * **arXiv ID:** [`arXiv:2608.26747`](https://arxiv.org/abs/2608.26747) [cs.AI]
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Submission Date:** August 27, 2026
> * **Authors:** 
>   Mingquan Liu, Jiangyu Chen, Hanqun Cao, Xujun Zhang, Pengsen Ma, Xiangru Tang, Shuting Jin, Zhuo Yang, Tianfan Fu, Fang Wu, Xiangxiang Zeng
> * **Resources & Code:** [GitHub Repository (AgentFold)](https://github.com/lmqfly/AgentFold)

* **arXiv ID:** [`arXiv:2608.26747`](https://arxiv.org/abs/2608.26747) [cs.AI]
* **主要学科:** 人工智能 (`cs.AI`)
* **提交日期:** 2026年8月27日
* **作者:** 
  Mingquan Liu, Jiangyu Chen, Hanqun Cao, Xujun Zhang, Pengsen Ma, Xiangru Tang, Shuting Jin, Zhuo Yang, Tianfan Fu, Fang Wu, Xiangxiang Zeng
* **资源与代码:** [GitHub 仓库 (AgentFold)](https://github.com/lmqfly/AgentFold)

---

## Abstract

> Scientific LLM agents have shown promise in literature reasoning, tool use, and experiment planning, but it remains unclear whether they can autonomously improve large, tightly coupled scientific machine-learning systems through executable code changes and computationally expensive validation. 
> 
> We study this question in protein folding, where progress requires coordinated architectural modifications, multi-objective evaluation, and domain-aware interpretation. We present **AgentFold**, a multi-agent framework that formulates folding-model development as a closed-loop search over executable code variants. Starting from ESMFold, AgentFold proposes hypotheses, implements and debugs code-level modifications, evaluates model variants, analyzes experimental outcomes, and stores both successful and failed interventions in structured memory. 
> 
> An MCTS-style policy allocates computational resources across high-scoring search branches. On an engineering-scale protein-folding codebase comprising more than 2,000 lines of code, AgentFold explores approximately 80 model variants using approximately 5,000 GPU-hours and 170 million LLM tokens. Under a matched computational budget, AgentFold improves the best lDDT by 7.5% over independent Codex proposals and outperforms a random-search control. 
> 
> Beyond model improvement, the resulting intervention traces reveal recurring empirical design patterns: stable gains tend to arise from early, soft, learnable priors and gated refinement, whereas direct geometric perturbations and geometry-conditioned feedback often destabilize training.

科学大语言模型智能体（LLM agents）在文献推理、工具使用和实验规划方面展现出了巨大潜力，但它们是否能够通过可执行的代码修改和计算成本高昂的验证，自主改进大型、高度耦合的科学机器学习系统，目前尚不明确。

我们在蛋白质折叠领域研究了这一问题，在该领域中，取得进展需要进行协调一致的架构修改、多目标评估和具备领域意识的解释。我们提出了 **AgentFold**，这是一个多智能体框架，它将折叠模型的发展表述为对可执行代码变体的闭环搜索。以 ESMFold 为起点，AgentFold 提出假设、实施并调试代码级别的修改、评估模型变体、分析实验结果，并将成功和失败的干预措施存储在结构化记忆中。

MCTS 风格的策略将计算资源分配给高得分的搜索分支。在一个包含 2,000 多行代码的工程级蛋白质折叠代码库上，AgentFold 使用了约 5,000 GPU 小时和 1.7 亿个 LLM Token，探索了大约 80 个模型变体。在匹配的计算预算下，与独立的 Codex 提案相比，AgentFold 将最佳 lDDT 提高了 7.5%，并且优于随机搜索对照组。

除了模型改进之外，由此产生的干预轨迹揭示了反复出现的经验设计模式：稳定的收益往往来自早期、软性的、可学习的先验以及门控求精，而直接的几何扰动和受几何条件约束的反馈往往会破坏训练的稳定性。

---

## Full-Text & External Links

> * **PDF Version:** [View PDF](https://arxiv.org/pdf/2608.26747)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.26747v1)
> * **Source Files:** [TeX Source](https://arxiv.org/src/2608.26747)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) 
>   <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" width="30" />
> * **Citations & Metrics:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.26747)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.26747)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.26747)

* **PDF 版本:** [查看 PDF](https://arxiv.org/pdf/2608.26747)
* **HTML 版本:** [arXiv HTML (实验性)](https://arxiv.org/html/2608.26747v1)
* **源文件:** [TeX 源码](https://arxiv.org/src/2608.26747)
* **许可协议:** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/) 
  <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" width="30" />
* **引用与指标:** 
  * [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2608.26747)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.26747)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.26747)