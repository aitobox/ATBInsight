---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- AgentWeave
- 函数调用
- 大语言模型
- 路由层
- 工具使用
title: AgentWeave：在工具丰富的语言模型中，通过先路由后推理实现高效函数调用
---
### 文章背景与核心概要

随着大型语言模型（LLM）越来越多地被部署并用于访问庞大的工具库、函数、API和专用代理，它们面临着巨大的性能障碍。不断增长的候选动作空间迫使模型处理更多的架构模式、消耗过多的提示词Token，并且难以在相似或不相关的候选工具之间进行区分。

为了解决这一问题，作者推出了 **AgentWeave**，这是一个确定性的推理前路由层。AgentWeave 没有修改下游的语言模型，而是通过利用适用性、需求性、能力和路由信号，预先构建出一个有边界且模型可见的动作空间，从而精简候选工具集。

在使用公开的 `MadeAgents/Hammer2.1-1.5b` 模型、基于固定的 BFCL 衍生路由压力协议进行评估时：
* **成功率：** 在 48 个新的多函数任务中，AgentWeave 取得了 **12.5% (6/48)** 的原生 BFCL 成功率，而全工具（all-tools）、确定性随机前 8（deterministic random top-8）以及语义前 8（semantic top-8）基线的成功率均为 **0% (0/48)**（成对成功率差异为 +12.5 个百分点；95% 自助法置信区间：+4.17 至 +22.92 个百分点；精确 McNemar 检验 $p = 0.03125$）。
* **效率：** 与暴露全工具相比，AgentWeave 减少了 **70.18% 的工具**，消耗了 **61.70% 的输入 Token**，并实现了 **50.95% 的更低本地模型平均延迟**。

尽管绝对任务成功率仍然较低，且本研究主要作为基于 BFCL 的路由压力评估，而非官方排行榜评分，但这些发现表明，候选空间的构建对固定模型的行为具有实质性影响，并将推理前路由确立为实现高效工具使用的关键阶段。

---

## 论文元数据 (Paper Metadata)

* **arXiv ID:** [arXiv:2608.23078](https://arxiv.org/abs/2608.23078) [cs.AI]
* **学科分类:** 人工智能 (`cs.AI`)；计算与语言 (`cs.CL`)
* **ACM 类别:** I.2.11; I.2.7
* **DOI:** [10.48550/arXiv.2608.23078](https://doi.org/10.48550/arXiv.2608.23078)
* **提交时间:** 2026年8月24日
* **作者:** Saurav Singla, Aarav Singla, Advik Gupta, Parnika Gupta

---

## 链接与资源 (Links & Resources)

* **全文阅读:** [查看 PDF](https://arxiv.org/pdf/2608.23078)
* **开源许可:** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/)
* **代码与工件:** 开源实现与可复现工件可在 AgentWeave 代码仓库中获取。

---

# AgentWeave: Routing Before Reasoning for Efficient Function Calling in Tool-Rich Language Models

> # AgentWeave: Routing Before Reasoning for Efficient Function Calling in Tool-Rich Language Models

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

## Summary

> ## Summary

As large language models (LLMs) are increasingly deployed with access to vast collections of tools, functions, APIs, and specialized agents, they face significant performance hurdles. A growing candidate action space forces models to process more schemas, consume excessive prompt tokens, and struggle to distinguish between similar or irrelevant alternatives. 

> As large language models (LLMs) are increasingly deployed with access to vast collections of tools, functions, APIs, and specialized agents, they face significant performance hurdles. A growing candidate action space forces models to process more schemas, consume excessive prompt tokens, and struggle to distinguish between similar or irrelevant alternatives. 

To combat this, the authors introduce **AgentWeave**, a deterministic pre-inference routing layer. Instead of modifying the downstream language model, AgentWeave reduces the candidate set beforehand by building a bounded, model-visible action space using eligibility, requirement, capability, and routing signals. 

> To combat this, the authors introduce **AgentWeave**, a deterministic pre-inference routing layer. Instead of modifying the downstream language model, AgentWeave reduces the candidate set beforehand by building a bounded, model-visible action space using eligibility, requirement, capability, and routing signals. 

Evaluated using a frozen BFCL-derived routing-pressure protocol on the public `MadeAgents/Hammer2.1-1.5b` model:
* **Success Rate:** AgentWeave achieved **12.5% (6/48)** native BFCL successes on 48 fresh multiple-function tasks, compared to **0% (0/48)** for all-tools, deterministic random top-8, and semantic top-8 baselines (paired success difference of +12.5 percentage points; 95% bootstrap CI: +4.17 to +22.92 points; exact McNemar $p = 0.03125$).
* **Efficiency:** Relative to full all-tools exposure, AgentWeave presented **70.18% fewer tools**, consumed **61.70% fewer input tokens**, and achieved **50.95% lower mean local-model latency**.

> Evaluated using a frozen BFCL-derived routing-pressure protocol on the public `MadeAgents/Hammer2.1-1.5b` model:
> * **Success Rate:** AgentWeave achieved **12.5% (6/48)** native BFCL successes on 48 fresh multiple-function tasks, compared to **0% (0/48)** for all-tools, deterministic random top-8, and semantic top-8 baselines (paired success difference of +12.5 percentage points; 95% bootstrap CI: +4.17 to +22.92 points; exact McNemar $p = 0.03125$).
> * **Efficiency:** Relative to full all-tools exposure, AgentWeave presented **70.18% fewer tools**, consumed **61.70% fewer input tokens**, and achieved **50.95% lower mean local-model latency**.

While absolute task success remains low and the study serves primarily as a BFCL-derived routing-pressure evaluation rather than an official leaderboard score, the findings demonstrate that candidate-space construction materially impacts fixed-model behavior and establishes pre-inference routing as a critical stage for efficient tool use.

> While absolute task success remains low and the study serves primarily as a BFCL-derived routing-pressure evaluation rather than an official leaderboard score, the findings demonstrate that candidate-space construction materially impacts fixed-model behavior and establishes pre-inference routing as a critical stage for efficient tool use.

---

> ---

## Paper Metadata

> ## Paper Metadata

* **arXiv ID:** [arXiv:2608.23078](https://arxiv.org/abs/2608.23078) [cs.AI]
* **Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`)
* **ACM Classes:** I.2.11; I.2.7
* **DOI:** [10.48550/arXiv.2608.23078](https://doi.org/10.48550/arXiv.2608.23078)
* **Submitted:** August 24, 2026
* **Authors:** Saurav Singla, Aarav Singla, Advik Gupta, Parnika Gupta

> * **arXiv ID:** [arXiv:2608.23078](https://arxiv.org/abs/2608.23078) [cs.AI]
> * **Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`)
> * **ACM Classes:** I.2.11; I.2.7
> * **DOI:** [10.48550/arXiv.2608.23078](https://doi.org/10.48550/arXiv.2608.23078)
> * **Submitted:** August 24, 2026
> * **Authors:** Saurav Singla, Aarav Singla, Advik Gupta, Parnika Gupta

---

> ---

## Links & Resources

> ## Links & Resources

* **Full-Text:** [View PDF](https://arxiv.org/pdf/2608.23078)
* **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)
* **Code & Artifacts:** Open-source implementation and reproducibility artifacts are available in the AgentWeave repository.

> * **Full-Text:** [View PDF](https://arxiv.org/pdf/2608.23078)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)
> * **Code & Artifacts:** Open-source implementation and reproducibility artifacts are available in the AgentWeave repository.