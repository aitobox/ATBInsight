---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 提示词优化
- 参数提取
- 动态上下文
- 大语言模型
- 自改进框架
title: DynaContext：异构参数提取中优化提示词的自改进动态上下文构建方法
---
### 文章背景与核心概要
在自动化提示词与技能优化的领域中，传统的做法通常依赖于跨所有推理实例重复使用的静态指令。然而，当面对异构输入（例如电子元器件中电阻器、电容器和晶体管需要完全不同的字段和约束条件）时，这种静态方法往往显得力不从心。

为了解决这一痛点，本文作者推出了 **DynaContext** 框架。该框架将离线优化的提取核心（通过 GEPA 或 SkillOpt 学习）与推理时的上下文自适应以及验证门控的自改进机制结合起来。DynaContext 能够动态路由每个输入项，组合出定制化的特定项提示词，并采用确定性验证与大模型裁判双重机制。只有经过人工验证的修正结果才会进入演示记忆库，从而在异构参数提取任务中实现了显著的性能跃升。

---

# DynaContext: Self-Improving Dynamic Contextualization of Optimized Prompts for Heterogeneous Parameter Extraction

**arXiv:** [2608.22014](https://arxiv.org/abs/2608.22014) [cs.AI]  
**Submitted:** August 22, 2026  
**Authors:** Joe Yu, Shibin Thomas Stanley Paul, Sven Mayer  

---

## 📌 Summary

自动化提示词和技能优化通常依赖于在所有推理实例中重复使用的静态指令，但在处理异构输入（如电子元器件，其中电阻器、电容器和晶体管需要完全不同的字段和约束）时，这种方法往往表现不佳。

为了解决这个问题，作者推出了 **DynaContext** 框架，该框架将通过 GEPA 或 SkillOpt 学习的离线优化提取核心与**推理时上下文自适应**以及**验证门控的自改进**相结合。DynaContext 动态路由每个项目，组合出特定于项目的定制提示，并采用确定性验证和大模型裁判机制。只有经过人工验证的修正才能进入演示记忆库。

### 核心结果：
* **单类别基准测试：** 平均准确率从基础提示词的 **86.6%** 提升至独立 SkillOpt 的 **96.9%** 以及最佳 DynaContext 配置的 **98.6%**。
* **异构基准测试（850个黄金事实）：** 平均字段级 F1 分数从未经优化的对照组的 **51.8%** 提升至仅使用动态演示的 **59.2%**、仅使用优化核心的 **66.9%** 以及完整 DynaContext 的 **71.0%**。
* **相对提升：** 在固定模型的前提下，完整的 DynaContext 配置平均比部署的静态提示词流水线高出 **17.3 个 F1 点**。

> Automated prompt and skill optimization typically relies on static instructions reused across all inference instances, which struggles when dealing with heterogeneous inputs (such as electronic components where resistors, capacitors, and transistors require entirely different fields and constraints). 
>
> To solve this, the authors introduce **DynaContext**, a framework combining an offline-optimized extraction core (learned via GEPA or SkillOpt) with **inference-time contextual adaptation** and **validation-gated self-improvement**. DynaContext routes each item dynamically, composes tailored item-specific prompts, and employs both deterministic validation and an LLM judge. Only human-verified corrections enter the demonstration memory.
>
> ### Key Results:
> * **Single-category benchmark:** Average accuracy increased from **86.6%** (base prompt) to **96.9%** (standalone SkillOpt) and **98.6%** (best DynaContext configuration).
> * **Heterogeneous benchmark (850 gold facts):** Average field-level F1 improved from **51.8%** (unoptimized control) to **59.2%** (dynamic demos alone), **66.9%** (optimized core alone), and **71.0%** (full DynaContext).
> * **Relative Improvement:** Holding the model fixed, the full configuration outperforms the deployed static-prompting pipeline by **17.3 F1 points** on average.

---

## 📄 Abstract

自动化提示词和技能优化通常会生成一个单一的静态指令，该指令在下一次优化周期之前会在各个推理实例中重复使用。然而，当所需的上下文、约束和证据在不同实例之间发生变化时，这种方法无法自适应。例如，从电子元器件描述中提取参数就打破了这一假设：电阻器、电容器、晶体管和连接器需要不同的字段、单位约束和演示，且每个输入都提供不同的证据状态。我们引入了 DynaContext，这是一个将通过 GEPA 或 SkillOpt 学习的离线优化提取核心与推理时上下文自适应和验证门控自改进相结合的框架。DynaContext 通过内部、外部或回退证据路径路由每个项目，并由核心、模式、证据、未解决字段和已验证的演示组合出特定于项目的提示。确定性验证和大模型裁判对每个输出进行门控，不确定的情况转交给人工审核，只有经过人工验证的修正才会进入演示记忆库。在单类别基准测试中，平均准确率从基础提示词的 86.6% 提高到独立 SkillOpt 的 96.9% 以及最佳 DynaContext 配置的 98.6%。在 850 个异构黄金参数事实中，平均字段级 F1 从未经优化、无演示的对照组的 51.8% 提高到仅使用动态演示时的 59.2%、仅使用优化核心时的 66.9% 以及两者结合时的 71.0%。在模型保持不变的情况下，完整配置平均比部署的静态提示词流水线高出 17.3 个 F1 点。

> > Automated prompt and skill optimization typically produces a single static instruction that is reused across inference instances until the next optimization cycle. However, this approach cannot adapt when the required context, constraints, and evidence vary from one instance to another. For instance, parameter extraction from electronic component descriptions breaks this assumption: resistors, capacitors, transistors, and connectors require different fields, unit constraints, and demonstrations, and each input provides a different evidence state. We introduce DynaContext, a framework that combines an offline-optimized extraction core, learned with GEPA or SkillOpt, with inference-time contextual adaptation and validation-gated self-improvement. DynaContext routes each item through internal, external, or fallback evidence paths and composes an item-specific prompt from the core, schema, evidence, unresolved fields, and validated demonstrations. Deterministic validation and an LLM judge gate every output, uncertain cases go to human review, and only human-verified corrections enter the demonstration memory. On a single-category benchmark, average accuracy increases from 86.6% for the base prompt to 96.9% for standalone SkillOpt and 98.6% for the best DynaContext configuration. Across 850 heterogeneous gold parameter facts, average field-level F1 increases from 51.8% for an unoptimized, demonstration-free control to 59.2% with dynamic demonstrations alone, 66.9% with the optimized core alone, and 71.0% with both. Holding the model fixed, the full configuration outperforms the deployed static-prompting pipeline by 17.3 F1 points on average.

---

## 🔗 Links & Resources

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2608.22014) | [HTML (实验性)](https://arxiv.org/html/2608.22014v1) | [TeX 源码](https://arxiv.org/src/2608.22014)
* **元数据与引用：** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.22014) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.22014) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.22014)
* **DOI：** [10.48550/arXiv.2608.22014](https://doi.org/10.48550/arXiv.2608.22014)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.22014) | [HTML (Experimental)](https://arxiv.org/html/2608.22014v1) | [TeX Source](https://arxiv.org/src/2608.22014)
> * **Metadata & Citations:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.22014) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.22014) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.22014)
> * **DOI:** [10.48550/arXiv.2608.22014](https://doi.org/10.48550/arXiv.2608.22014)