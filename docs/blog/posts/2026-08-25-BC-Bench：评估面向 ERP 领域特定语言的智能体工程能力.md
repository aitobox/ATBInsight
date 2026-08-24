---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- AI智能体
- 软件工程
- ERP
- 领域特定语言
- 基准测试
title: BC-Bench：评估面向 ERP 领域特定语言的智能体工程能力
---
### 文章背景与核心概要

智能体工程系统（Agentic engineering systems）在通用软件工程基准测试中展现出了令人瞩目的性能，然而它们在企业资源计划（ERP）领域特定语言（DSL）中的应用效果长期以来鲜有探索。为了填补这一空白，研究人员推出了 **BC-Bench**，这是一个专为评估智能体在微软 Dynamics 365 Business Central 所使用的 DSL——**AL** 语言中的真实世界任务表现而设计的全新基准测试。

该论文的核心亮点包括：BC-Bench 包含了从两个微软拥有的生产代码库中人工整理的 101 个任务，真实还原了企业资源规划（ERP）的开发工作流；通过改编 SWE-Bench 方法论，该基准测试克服了 AL 生态系统资源公开较少、环境配置复杂等特有挑战；除了代码功能性之外，BC-Bench 还评估了测试生成能力，并支持包含视觉上下文的多模态问题描述。评估结果表明，在通用基准上观察到的性能提升并不能可靠地转化为 AL 生态系统的优势，这凸显了建立特定领域评估框架的迫切需求。

---

# BC-Bench: Evaluating Agentic Engineering in a Domain-Specific Language for ERP

> # BC-Bench: Evaluating Agentic Engineering in a Domain-Specific Language for ERP

**Authors:** Haoran Sun, Klaus Marius Hansen  
**Submitted:** August 21, 2026  
**Primary Subjects:** Software Engineering (`cs.SE`), Artificial Intelligence (`cs.AI`)  
**arXiv:** [arXiv:2608.20851 [cs.SE]]  

> **Authors:** Haoran Sun, Klaus Marius Hansen  
> **Submitted:** August 21, 2026  
> **Primary Subjects:** Software Engineering (`cs.SE`), Artificial Intelligence (`cs.AI`)  
> **arXiv:** [arXiv:2608.20851 [cs.SE]]  

---

## 📌 Summary

> ## 📌 Summary

智能体工程系统在通用软件基准测试中表现出令人印象深刻的性能，但它们在企业资源计划 (ERP) 领域特定语言 (DSL) 中的有效性在很大程度上仍未得到探索。

> Agentic engineering systems have demonstrated impressive performance on general-purpose software benchmarks, but their effectiveness in enterprise resource planning (ERP) domain-specific languages (DSLs) has remained largely unexplored. 

为了填补这一空白，研究人员引入了 **BC-Bench**，这是一个旨在评估智能体工程在 **AL**（微软 Dynamics 365 Business Central 使用的 DSL）真实世界任务中表现的新型基准测试。该论文的主要亮点包括：
* **真实世界任务整理：** BC-Bench 具有从两个微软拥有的生产代码库中提取的 101 个手工整理的任务，反映了真实的 ERP 开发工作流程。
* **生态系统适配：** 适应 SWE-Bench 方法论，该基准测试解决了 AL 生态系统的独特限制，包括有限的公共资源和复杂的环境配置。
* **先进的评估指标：** 除了代码功能外，BC-Bench 还评估测试生成能力，并适应包含视觉上下文的多模态问题陈述。
* **主要发现：** 对多个前沿模型和智能体框架的评估（通过多运行指标考虑不确定性）表明，错误修复任务中的模型间性能差异超过了智能体框架之间的差异。至关重要的是，在通用基准测试中观察到的性能改进并不能可靠地转化为 AL 生态系统，这强调了对特定领域评估框架的迫切需求。

> To address this gap, researchers introduce **BC-Bench**, a novel benchmark designed to evaluate agentic engineering on real-world tasks in **AL**—the DSL utilized for Microsoft Dynamics 365 Business Central. Key highlights of the paper include:
> * **Real-World Task Curations:** BC-Bench features 101 manually curated tasks extracted from two Microsoft-owned production repositories, mirroring authentic ERP development workflows.
> * **Ecosystem Adaptations:** Adapting the SWE-Bench methodology, the benchmark tackles the distinct constraints of the AL ecosystem, including limited public resources and complex environment provisioning.
> * **Advanced Evaluation Metrics:** Beyond code functionality, BC-Bench assesses test generation capabilities and accommodates multimodal problem statements containing visual contexts.
> * **Key Findings:** Evaluations across multiple frontier models and agent harnesses (accounting for nondeterminism via multi-run metrics) reveal that model-to-model performance variations in bug-fixing tasks outweigh differences between agent harnesses. Crucially, performance improvements observed on general-purpose benchmarks do not reliably translate to the AL ecosystem, emphasizing the critical need for domain-specific evaluation frameworks.

---

## 🔗 Links & Resources

> ## 🔗 Links & Resources

* **全文访问：**
  * [查看 PDF](https://arxiv.org/pdf/2608.20851)
  * [HTML 版本（实验性）](https://arxiv.org/html/2608.20851v1)
  * [TeX 源码](https://arxiv.org/src/2608.20851)
* **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
* **外部书目工具：**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.20851)
  * [谷歌学术](https://scholar.google.com/scholar_lookup?arxiv_id=2608.20851)
  * [语义学者](https://api.semanticscholar.org/arXiv:2608.20851)

> * **Full-Text Access:**
>   * [View PDF](https://arxiv.org/pdf/2608.20851)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.20851v1)
>   * [TeX Source](https://arxiv.org/src/2608.20851)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
> * **External Bibliographic Tools:**
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.20851)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.20851)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.20851)