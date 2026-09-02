---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- Text-to-SQL
- 大语言模型
- 列表式选择
- 检索增强
- 机器学习
title: 用记忆替代训练：Text-to-SQL 的列表式选择方法
---
### 文章背景与核心概要
现代 Text-to-SQL 架构通常采用“生成-执行-选择”（generate-execute-select）的流水线模式，即先生成多个候选 SQL 查询，然后通过筛选选出最优解。尽管“列表式选择”（listwise selection）能够对多个候选进行联合比较，但对这些模型进行微调（fine-tuning）往往需要付出高昂的计算成本。

为了突破这一局限性，本文提出了 **MaP-SQL**——一种无需微调的列表式选择器。它用高效的推理时策略取代了传统的训练目标：首先，通过结构化记忆检索，将自然语言到架构元素、SQL 操作及预期结果的映射关系以记忆形式从训练数据中提取并复用，而非硬编码进模型参数；其次，通过聚合多种输入排列的排序结果来消除列表式选择器固有的位置偏差，并利用执行结果和逐点评分（pointwise scoring）来优化推理成本。

在标准的 Text-to-SQL 基准测试中，该方法在无需微调的前提下展现出更高的稳定性，同时大幅减少了不必要的比较次数。值得注意的是，在 **BIRD-dev** 基准测试中，在采用相同候选集的情况下，MaP-SQL 的执行准确率比当前最先进的基于选择器的方法（$R^3-SQL$）高出 **2.02 个百分点**，同时 Token 消耗量降低了 **$2.92\times$**。

---

# Replacing Training with Memory: Listwise Selection for Text-to-SQL

## Summary
Modern Text-to-SQL architectures typically utilize a *generate-execute-select* pipeline, where multiple candidate SQL queries are produced and subsequently filtered to identify the optimal choice. While **listwise selection** enables the joint comparison of multiple candidates, fine-tuning these models is computationally expensive. 

To overcome this limitation, this paper introduces **MaP-SQL**, a fine-tuning-free listwise selector that replaces traditional training objectives with efficient inference-time strategies:
1. **Structured Memory Retrieval:** Instead of encoding selection behavior into model parameters, the approach retrieves memories distilled from training data that illustrate how natural language translates to schema elements, SQL operations, and expected outcomes.
2. **Positional Bias Mitigation:** To neutralize ordering biases inherent to listwise selectors, the method aggregates rankings across multiple input permutations while optimizing inference costs using execution results and pointwise scoring.

Across standard Text-to-SQL benchmarks, the proposed method yields greater stability without requiring fine-tuning and necessitates significantly fewer comparisons. Notably, on the **BIRD-dev** benchmark, it surpasses the previous state-of-the-art selector-based method ($R^3-SQL$) by **2.02 execution accuracy points** using identical candidate sets, while using **$2.92\times$ fewer tokens**.

> 现代 Text-to-SQL 架构通常采用“生成-执行-选择”（generate-execute-select）流水线，即生成多个候选 SQL 查询，随后进行筛选以确定最优选择。虽然**列表式选择**（listwise selection）支持对多个候选进行联合比较，但微调这些模型的计算成本很高。
> 
> 为了克服这一局限性，本文推出了 **MaP-SQL**，这是一种无需微调的列表式选择器，它用高效的推理时策略取代了传统的训练目标：
> 1. **结构化记忆检索：** 该方法没有将选择行为编码到模型参数中，而是检索从训练数据中提取的记忆，这些记忆展示了自然语言如何转化为架构元素、SQL 操作和预期结果。
> 2. **位置偏差缓解：** 为了消除列表式选择器固有的顺序偏差，该方法在多个输入排列中聚合排名，同时使用执行结果和逐点评分来优化推理成本。
> 
> 在标准的 Text-to-SQL 基准测试中，该方法在无需微调的情况下产生了更高的稳定性，并且需要显著更少的比较。值得注意的是，在 **BIRD-dev** 基准测试中，在使用相同候选集的情况下，它超越了之前最先进的基于选择器的方法（$R^3-SQL$），执行准确率高出 **2.02 个百分点**，同时使用的 Token 减少了 **$2.92\times$**。

---

## Paper Metadata

| Attribute | Detail |
| :--- | :--- |
| **arXiv Identifier** | [arXiv:2609.00834](https://arxiv.org/abs/2609.00834) [cs.SE] |
| **Title** | Replacing Training with Memory: Listwise Selection for Text-to-SQL |
| **Authors** | Yeonseok Jeong, Soyoung Yoon, Seongjun Lee, Seung-won Hwang |
| **Submitted On** | September 1, 2026 |
| **Accepted Venue** | Findings of EMNLP 2026 |
| **Primary Subject** | Software Engineering (`cs.SE`) |
| **Secondary Subjects** | Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`) |
| **DOI** | [10.48550/arXiv.2609.00834](https://doi.org/10.48550/arXiv.2609.00834) |

> | 属性 | 详情 |
> | :--- | :--- |
> | **arXiv 标识符** | [arXiv:2609.00834](https://arxiv.org/abs/2609.00834) [cs.SE] |
> | **标题** | 用记忆替代训练：Text-to-SQL 的列表式选择方法 |
> | **作者** | Yeonseok Jeong, Soyoung Yoon, Seongjun Lee, Seung-won Hwang |
> | **提交日期** | 2026年9月1日 |
> | **录用会议** | Findings of EMNLP 2026 |
> | **主要学科** | 软件工程 (`cs.SE`) |
> | **次要学科** | 人工智能 (`cs.AI`)、计算与语言 (`cs.CL`) |
> | **DOI** | [10.48550/arXiv.2609.00834](https://doi.org/10.48550/arXiv.2609.00834) |

---

## Abstract
Modern Text-to-SQL systems often follow generate-execute-select pipelines, generating multiple candidate queries then selecting the best one. Listwise selection, by jointly comparing multiple candidates, has been widely adopted, but fine-tuning listwise selectors is costly. We thus propose a fine-tuning-free listwise selector. We replace two major fine-tuning objectives with inference-time strategies: (1) learning selection criteria as ordering and (2) mitigating positional bias. First, we build reusable structured memories instead of learning selection behavior as model parameters. Given a question, MaP-SQL retrieves memories distilled from training data that encode how natural language maps to schema elements, SQL operations, and expected outputs. These memories serve as explicit decision criteria for evaluating candidates in a listwise manner. Second, to mitigate ordering bias of listwise selectors, we aggregate rankings across multiple input permutations, with inference cost optimized by execution results and pointwise scoring. Our approach improves selection accuracy while maintaining efficiency and compatibility with existing large language models. Across Text-to-SQL benchmarks, it produces more stable selection without fine-tuning and fewer unnecessary comparisons than existing methods. On BIRD-dev, it outperforms the previous state-of-the-art selector-based method $R^3-SQL$ by 2.02 execution accuracy points on average using the same candidate sets, with 2.92x fewer tokens.

> 现代 Text-to-SQL 系统通常遵循“生成-执行-选择”流水线，即生成多个候选查询然后选择最佳查询。列表式选择通过联合比较多个候选已被广泛采用，但微调列表式选择器的成本很高。因此，我们提出了一种无需微调的列表式选择器。我们用推理时策略取代了两个主要的微调目标：（1）将选择标准学习为排序，以及（2）缓解位置偏差。首先，我们构建可重用的结构化记忆，而不是将选择行为学习为模型参数。给定一个问题，MaP-SQL 会检索从训练数据中提取的记忆，这些记忆编码了自然语言如何映射到架构元素、SQL 操作和预期输出。这些记忆可作为以列表方式评估候选者的明确决策标准。其次，为了缓解列表式选择器的顺序偏差，我们跨多个输入排列聚合排名，并通过执行结果和逐点评分来优化推理成本。我们的方法在保持效率和与现有大语言模型兼容性的同时，提高了选择准确率。在各个 Text-to-SQL 基准测试中，它在无需微调的情况下产生了更稳定的选择，并且比现有方法进行了更少的不必要比较。在 BIRD-dev 上，使用相同的候选集，它平均比以前最先进的基于选择器的方法 $R^3-SQL$ 的执行准确率高出 2.02 个百分点，同时使用的 Token 减少了 2.92 倍。

---

## Access Links & Resources

* **Full-Text Options:** 
  * [View PDF](https://arxiv.org/pdf/2609.00834)
  * [HTML Version (Experimental)](https://arxiv.org/html/2609.00834v1)
  * [TeX Source](https://arxiv.org/src/2609.00834)
* **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="vertical-align: middle; display: inline-block; max-height: 20px;" /></a>
* **External Bibliographic Tools:**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.00834)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.00834)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.00834)

> * **全文选项：**
>   * [查看 PDF](https://arxiv.org/pdf/2609.00834)
>   * [HTML 版本（实验性）](https://arxiv.org/html/2609.00834v1)
>   * [TeX 源码](https://arxiv.org/src/2609.00834)
> * **许可协议：** [知识共享署名 4.0 国际](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="vertical-align: middle; display: inline-block; max-height: 20px;" /></a>
> * **外部文献计量工具：**
>   * [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2609.00834)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.00834)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.00834)