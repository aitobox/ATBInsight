---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 贝叶斯校准
- 多智能体系统
- 先验分布
- 科学文献挖掘
- 本地大模型
title: Distribird：基于文献信息的贝叶斯模型校准先验分布设计
---
### 文章背景与核心概要
在基于过程的模型（process-based models）的贝叶斯校准过程中，为每个模型参数构建信息丰富的先验分布（informative prior distributions）至关重要。然而，由于文献检索既耗时又高度依赖专业领域知识，研究人员在实践中往往退而求其次，几乎总是使用无信息先验（uniform priors）。为了解决这一痛点，本文介绍了 Distribird——一个旨在自动化生成贝叶斯校准信息先验的智能体网络应用。该工具通过部署多智能体流水线，能够自动检索科学文献、根据领域相关性提取并加权报告值，最后利用 AIC（赤池信息准则）模型选择拟合出最优的概率分布。

在包含 10 个科学领域的 24 个参数评估中，研究人员对比了三款开源模型（*Qwen3.6 27B*、*Gemma 4 31B* 和 *Mistral Small 4 119B*）与单提示词大模型基线的表现。结果表明，Distribird 的完整流水线在先验质量上与基线相当，但在透明度、严格的有效性检查以及本地执行隐私（防止未公开的模型细节泄露给第三方 API）方面表现出显著优势。该研究证明，对于科学应用而言，透明度、可追溯性与安全性比单纯的准确度边际提升更为重要。

---

## 摘要 (Abstract)

Bayesian calibration of process-based models requires a prior distribution for each model parameter. Despite decades of methodological work, researchers almost always fall back on uniform priors. The main reason is that building informative priors from scientific literature is slow and needs both domain and statistical expertise. 

> 基于过程的模型的贝叶斯校准需要为每个模型参数设定一个先验分布。尽管经过了几十年的方法论研究，研究人员几乎总是退而求其次地使用均匀先验。主要原因是从科学文献中构建信息丰富的先验既耗时又需要领域和统计专业知识。

We present **Distribird**, an agentic web application that automates this process. Given a parameter name, physical description, and domain context, Distribird deploys a multi-agent pipeline that searches the literature, extracts and weights reported values by domain relevance, and fits a probability distribution via AIC model selection. When no literature is available, the system falls back to sensible uninformative alternatives, and clearly reports both the evidence behind and the confidence level of every prior it produces. It is designed for the problems where the models have physically interpretable parameters, where domain knowledge exists in the published literature. 

> 我们提出了 **Distribird**，这是一个能将该过程自动化的智能体网络应用。给定参数名称、物理描述和领域背景，Distribird 会部署一个多智能体流水线，用于搜索文献、根据领域相关性提取并加权报告的值，并通过 AIC 模型选择拟合概率分布。当没有可用的文献时，系统会退回到合理的无信息替代方案，并清楚地报告其生成的每个先验背后的证据和置信水平。它专为模型具有物理解释性参数、且已发表文献中存在领域知识的问题而设计。

We evaluate the tool on 24 parameters across 10 scientific domains comparing three open-weight models (*Qwen3.6 27B*, *Gemma 4 31B*, *Mistral Small 4 119B*) with a single-prompt LLM baseline. On prior quality the full pipeline matches this baseline. Every prior is traced to the specific papers and values from which it was constructed; a built-in validity layer declines to produce priors for out-of-scope requests, whereas the single-prompt baseline returns confident but unfounded priors for them in 11 of 30 model-parameter cases; and every language-model call runs locally, so no parameter description or unpublished modelling detail is transmitted to a third-party LLM provider (only generated search terms reach the public literature databases). For scientific use, we argue these properties matter more than a marginal improvement in point-estimate accuracy.

> 我们在 10 个科学领域的 24 个参数上对该工具进行了评估，将三个开源权重模型（*Qwen3.6 27B*、*Gemma 4 31B* 和 *Mistral Small 4 119B*）与单提示词大模型基线进行了比较。在先验质量方面，完整的流水线与该基线相匹配。每个先验都可以追溯到构建它的特定论文和数值；内置的有效性层拒绝为超出范围的请求生成先验，而单提示词基线在 30 个模型参数案例中有 11 个案例为其返回了自信但毫无根据的先验；此外，每个语言模型调用都在本地运行，因此没有任何参数描述或未发布的建模细节被传输到第三方大模型提供商（只有生成的搜索词才会到达公共文献数据库）。对于科学应用，我们认为这些特性比点估计准确性的边际提升更为重要。

---

## 附加资源与访问 (Additional Resources & Access)

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.11210) | [HTML Version](https://arxiv.org/html/2608.11210v2) | [TeX Source](https://arxiv.org/src/2608.11210)
* **External Citations & Tools:** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.11210)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.11210)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.11210)