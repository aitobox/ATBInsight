---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- AI Agent
- Token消耗
- 成本优化
- 代码生成
- Kimi K3
title: 你的AI Agent能更省钱吗？探究任务规范对智能体编程任务中Token消耗的影响
---
### 文章背景与核心概要
随着智能体编程工作流（Agentic coding workflows）在实际系统中的普及，如何有效管理Token消耗对于控制成本和提升效率至关重要。本文由 Jakub Smékal 撰写并于 2026 年 8 月 26 日提交至 arXiv，深入研究了任务规范（Task specifications）在智能体编程任务中对 Token 消耗的具体影响。

通过使用 Kimi K3 模型在三种思考努力水平（Thinking-effort levels）下进行的 2,700 次实验运行，研究表明：将详细全面的任务规范精简为单一的简陋用户故事（User story），会导致 Token 消耗增加 29.7%。此外，提示词敏感度（Prompt-sensitivity）在很大程度上取决于任务本身（范围从 13% 到 115%），但运行间的方差（Run-to-run variance）不受提示词更改的影响。作者还引入了一种预测方法，仅需对未见任务进行一次低成本的探测，就能以 36% 的准确率对不同任务规范和思考努力配置下的完整成本分布进行定价，这为评估 AI 工作流成本提供了一个强有力的工具。

---

## 摘要与参考信息

* **arXiv ID:** [arXiv:2608.25399](https://arxiv.org/abs/2608.25399) [cs.AI]
* **DOI:** [10.48550/arXiv.2608.25399](https://doi.org/10.48550/arXiv.2608.25399)
* **主分类:** 计算机科学 > 人工智能 (`cs.AI`)
* **提交日期:** 2026年8月26日
* **许可协议:** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

---

## 英文摘要

> Agentic coding workflows are now widely deployed in real-world systems. With long-horizon reasoning and tool use, token usage has become an important consideration for both cost and efficiency. Two engineers using AI will solve the same problem differently. How the specification of a task shapes an agent's token spend, and whether that spend can be predicted in advance, are open questions. 
>
> Here, we study the effects of different task specifications on agentic token spend with the Kimi K3 model at three thinking efforts. Across $2,700$ runs, we show that reducing a full task specification to a bare user story raises token spend by $29.7\%$, while run-to-run variance remains unaffected by any prompt changes. We show that prompt-sensitivity is task-dependent, running from $13\%$ to $115\%$. We fit a simple predictor that can price a full distribution of task specifications and thinking effort configurations from a single cheap probe on an unseen task within $36\%$, improving over prior work in predicting token spend. Our work provides initial results quantifying the effects of task specification on agentic token spend and introduces a method that can be used to systematically evaluate the cost of AI coding workflows.

> 智能体编程工作流现已广泛部署于实际系统中。凭借长周期推理和工具调用能力，Token 的使用量已成为考量成本与效率的重要因素。两名使用 AI 的工程师会以不同的方式解决同一个问题。任务的规范方式如何塑造智能体的 Token 消耗，以及这种消耗是否能够被提前预测，目前仍是未解之问。
> 
> 在本文中，我们研究了在使用 Kimi K3 模型并在三种思考努力水平下，不同的任务规范对智能体 Token 消耗的影响。通过 $2,700$ 次运行，我们发现将完整的任务规范精简为单纯的用户故事会使 Token 消耗增加 $29.7\%$，而任何提示词的更改都不会影响运行间的方差。我们证明了提示词的敏感度取决于具体的任务，数值在 $13\%$ 到 $115\%$ 之间波动。我们拟合了一个简单的预测器，它仅需对未见任务进行一次低成本的探测，就能以 $36\%$ 的误差范围对任务规范和思考努力配置的完整成本分布进行定价，这超越了以往预测 Token 消耗的工作。我们的工作提供了量化任务规范对智能体 Token 消耗影响的初步结果，并引入了一种可用于系统评估 AI 编程工作流成本的方法。

---

## 访问与资源

* **全文选项:**
  * [查看 PDF](https://arxiv.org/pdf/2608.25399)
  * [HTML 版本（实验性）](https://arxiv.org/html/2608.25399v1)
  * [TeX 源码](https://arxiv.org/src/2608.25399)
* **外部引用与学术工具:**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.25399)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.25399)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.25399)