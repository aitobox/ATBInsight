---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 脑电图
- 大语言模型
- 进化优化
- 自动化机器学习
- 神经科学
title: NeuroWeaver：用于探索脑电图分析管道程序化空间的自主进化智能体
---
### 文章背景与核心概要
将基础模型应用于脑电图（EEG）分析时，往往受限于极高的海量数据需求和巨大的参数量，这导致在资源受限的临床环境中会产生极高的计算成本。与此同时，通用的自动化机器学习框架也难以适应这一领域，因为无边界的程序化搜索未能纳入神经生理学先验知识，常常会产生不切实际的解决方案。

为了克服这些挑战，本文提出了 **NeuroWeaver**，这是一个统一的自主进化智能体，能够跨不同的 EEG 数据集和任务进行泛化。它将管道工程重新表述为一个离散约束优化问题，并通过大语言模型（LLM）驱动的可执行代码生成来解决该问题。其核心特性包括：**领域信息子空间初始化**（将搜索空间限制在符合神经科学合理性的流形中），以及**多目标进化优化**（通过自我反思精炼动态平衡性能、创新性和效率）。在五个异构基准测试中，NeuroWeaver 合成了轻量级的管道，其性能超越了特定任务的方法，并可与大规模基础模型相媲美——在 HMC 和 Workload 基准测试中甚至超越了后者，而其参数量分别仅为 $0.18\text{M}$ 和 $0.011\text{M}$。

---

# NeuroWeaver: An Autonomous Evolutionary Agent for Exploring the Programmatic Space of EEG Analysis Pipelines

## Summary

Applying foundation models to electroencephalography (EEG) analysis is often constrained by high data requirements and massive parameter counts, leading to prohibitive computational costs in resource-constrained clinical settings. Meanwhile, general automated machine learning frameworks struggle with this domain because unbounded programmatic searches fail to include neurophysiological priors, often yielding implausible solutions. 

To overcome these challenges, **NeuroWeaver** is proposed as a unified autonomous evolutionary agent that generalizes across diverse EEG datasets and tasks. It reformulates pipeline engineering as a discrete constrained optimization problem, solved via large language model (LLM)-driven generation of executable code. Key features include:
* **Domain-Informed Subspace Initialization:** Restricts the search space to a neuroscientifically plausible manifold.
* **Multi-Objective Evolutionary Optimization:** Dynamically balances performance, novelty, and efficiency using self-reflective refinement.

Across five heterogeneous benchmarks, NeuroWeaver synthesizes lightweight pipelines that outperform task-specific methods and rival large-scale foundation models—surpassing them on the HMC and Workload benchmarks while utilizing only $0.18\text{M}$ and $0.011\text{M}$ parameters, respectively.

---

## Metadata & Publication Details

* **arXiv ID:** [arXiv:2602.13473](https://arxiv.org/abs/2602.13473) [cs.AI]
* **Primary Subject:** Artificial Intelligence (`cs.AI`)
* **Authors:** Guoan Wang, Shihao Yang, Feng Liu
* **Submission History:**
  * `[v1]` Fri, 13 Feb 2026 21:26:43 UTC
  * `[v2]` Thu, 21 May 2026 22:18:18 UTC
  * `[v3]` Thu, 3 Sep 2026 16:52:08 UTC *(This version)*
* **DOI:** [10.48550/arXiv.2602.13473](https://doi.org/10.48550/arXiv.2602.13473)

---

## Abstract

尽管基础模型在通用领域取得了显著成功，但将其应用于脑电图（EEG）分析时，却受到大量数据需求和庞大参数量的限制，这带来了极高的计算成本，并阻碍了其在资源受限的临床环境中的部署。通用的自动化机器学习框架同样不适合该领域，因为在无边界程序化空间中的探索未能融入必要的神经生理学先验，且经常会产生神经科学上不合理的解决方案。因此，我们提出了 NeuroWeaver，这是一个统一的自主进化智能体，它通过将管道工程重新表述为一个离散约束优化问题（通过大语言模型（LLM）驱动的可执行代码生成来解决），从而在各种 EEG 数据集和任务中实现泛化。领域信息子空间初始化将搜索限制在神经科学合理的流形内，而多目标进化优化则通过自我反思精炼动态平衡性能、创新性和效率。在五个异构基准测试中，NeuroWeaver 合成了轻量级的管道，在几乎所有指标上都优于当前最先进的特定任务方法，并达到了与大规模foundation模型相当的准确率，甚至在 HMC 和 Workload 基准测试中超越了它们，而参数量分别仅为 $0.18$M 和 $0.011$M。

> Although foundation models have achieved remarkable success in general domains, applying them to electroencephalography (EEG) analysis is constrained by substantial data requirements and large parameter counts, which incur prohibitive computational costs and impede deployment in resource-constrained clinical environments. General-purpose automated machine learning frameworks are likewise ill-suited to this domain, since exploration within an unbounded programmatic space fails to incorporate essential neurophysiological priors and frequently yields neuroscientifically implausible solutions. We therefore propose NeuroWeaver, a unified autonomous evolutionary agent that generalizes across diverse EEG datasets and tasks by reformulating pipeline engineering as a discrete constrained optimization problem solved through large language model (LLM)-driven generation of executable code. A Domain-Informed Subspace Initialization confines the search to a neuroscientifically plausible manifold, while a Multi-Objective Evolutionary Optimization dynamically balances performance, novelty, and efficiency via self-reflective refinement. Across five heterogeneous benchmarks, NeuroWeaver synthesizes lightweight pipelines that outperform state-of-the-art task-specific methods on nearly all metrics and attain accuracy comparable to large-scale foundation models, even surpassing them on the HMC and Workload benchmarks with only $0.18$M and $0.011$M parameters, respectively.

---

## Access & Resources

* **Full-Text Options:** 
  * [View PDF](https://arxiv.org/pdf/2602.13473)
  * [HTML Version (Experimental)](https://arxiv.org/html/2602.13473v3)
  * [TeX Source](https://arxiv.org/src/2602.13473)
* **External Resources & Citation Tools:**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2602.13473)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2602.13473)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2602.13473)