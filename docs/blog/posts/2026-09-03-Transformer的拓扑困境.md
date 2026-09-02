---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- Transformer
- 递归架构
- 状态追踪
- 循环神经网络
- 深度学习
title: Transformer的拓扑困境
---
### 文章背景与核心概要
本文探讨了Transformer架构在处理动态状态追踪（dynamic state tracking）时所面临的根本性拓扑限制。由于Transformer依赖纯前馈架构来编码序列结构，在面对需要根据演化环境进行迭代更新的隐变量时，往往表现出结构上的力不从心。模型被迫随着每个输入步骤将演化的状态表示推向更深的层级，从而导致浅层网络无法访问关键信息并最终耗尽模型的深度预算。

为了克服这些局限性，作者们指出，实现时间延长的认知需要将研究重点从显式的思考轨迹（thinking traces）转移到通过递归架构实现的隐式激活动态。论文提出了一种递归与连续思考Transformer架构的分类法，并展望了未来可能的研究方向，如先进的状态空间模型和粗粒度递归机制，为解决Transformer的长程记忆与状态更新效率问题提供了重要的理论审视。

---

## 概览与总结 (Overview & Summary)

* **arXiv ID:** [2604.17121](https://arxiv.org/abs/2604.17121) [cs.LG]
* **作者:** Michael C. Mozer, Shoaib Ahmed Siddiqui, Rosanne Liu
* **提交时间:** 2026年4月18日（最后修订于2026年9月1日，版本 v5）
* **许可协议:** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/)

> * **arXiv ID:** [2604.17121](https://arxiv.org/abs/2604.17121) [cs.LG]
> * **Authors:** Michael C. Mozer, Shoaib Ahmed Siddiqui, Rosanne Liu
> * **Submitted:** 18 Apr 2026 (Last revised 1 Sep 2026, Version v5)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)

### 摘要总结 (Abstract Summary)
Transformer依赖不断扩展的上下文历史来编码序列中的结构。然而，其纯前馈架构在处理**动态状态追踪**（即响应演化环境对隐变量进行迭代更新）时引入了根本性的局限性。由于状态追踪依赖于前馈网络难以维持的序列依赖性，这些模型被迫在每个输入步骤中将不断演化的状态表示推得更深，压入其层叠结构中。

这种行为使得浅层中的关键信息无法被访问，并最终耗尽了模型的深度。虽然动态深度模型或显式/隐式“思考”轨迹等解决方案可以绕过这一深度限制，但它们在计算和内存上仍然效率低下。作者认为，实现延长的时序认知需要将焦点从显式思考轨迹转移到通过递归架构实现的隐式激活动态。他们引入了一种递归和连续思考Transformer架构的分类法（按递归轴和Token-到-递归比率分类），并概述了未来的研究方向，例如先进的状态空间模型和粗粒度递归。

> Transformers rely on an expanding contextual history to encode structure in sequences. However, their purely feedforward architecture introduces fundamental limitations when it comes to **dynamic state tracking**—the iterative updating of latent variables in response to an evolving environment. Because state tracking relies on sequential dependencies that feedforward networks struggle to maintain, these models are forced to push evolving state representations deeper into their layer stack with each input step. 
> 
> This behavior renders crucial information inaccessible in shallow layers and ultimately exhausts the model's depth. While solutions like dynamic depth models or explicit/latent "thinking" traces can bypass this depth limit, they remain computationally and memory inefficient. The authors argue that achieving temporally extended cognition requires shifting focus from explicit thought traces to implicit activation dynamics through recurrent architectures. They introduce a taxonomy of recurrent and continuous-thought transformer architectures (categorized by recurrence axis and token-to-recurrence ratios) and outline future research directions, such as advanced state-space models and coarse-grained recurrence.

---

## 文档元数据 (Document Metadata)

| 元数据字段 | 详情 |
| :--- | :--- |
| **主要学科** | 机器学习 (`cs.LG`) |
| **次要学科** | 人工智能 (`cs.AI`) |
| **引用格式** | `arXiv:2604.17121 [cs.LG]` |
| **DOI** | [10.48550/arXiv.2604.17121](https://doi.org/10.48550/arXiv.2604.17121) |
| **备注** | 添加了近期论文的引用 |

> | Metadata Field | Details |
> | :--- | :--- |
> | **Primary Subject** | Machine Learning (`cs.LG`) |
> | **Secondary Subjects** | Artificial Intelligence (`cs.AI`) |
> | **Cite As** | `arXiv:2604.17121 [cs.LG]` |
> | **DOI** | [10.48550/arXiv.2604.17121](https://doi.org/10.48550/arXiv.2604.17121) |
> | **Comments** | Added citations to recent papers |

---

## 访问与资源 (Access & Resources)

* **全文 PDF:** [查看 PDF](https://arxiv.org/pdf/2604.17121)
* **实验性 HTML:** [arXiv HTML 视图](https://arxiv.org/html/2604.17121v5)
* **源代码文件:** [TeX 源码](https://arxiv.org/src/2604.17121)

> * **Full-Text PDF:** [View PDF](https://arxiv.org/pdf/2604.17121)
> * **Experimental HTML:** [arXiv HTML View](https://arxiv.org/html/2604.17121v5)
> * **Source Files:** [TeX Source](https://arxiv.org/src/2604.17121)

### 相关许可图形
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> ### Associated License Graphics
> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">