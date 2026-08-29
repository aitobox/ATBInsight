---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 大模型评估
- Python评分函数
- 可解释性AI
- 自然语言处理
- EMNLP
title: ExecRubrics：用于可验证且高效长文本评估的可执行工具增强评分准则
---
### 文章背景与核心概要
传统的语言模型评估通常依赖于含糊不清的自然语言评分准则（rubrics）以及不透明的黑盒大模型裁判，且这些方法往往假设各个评估标准之间存在线性的、独立的聚合关系。为了解决这些局限性，作者推出了 **ExecRubrics** 这一新型框架，它能够将评分准则转化为紧凑、可执行的 Python 评分函数。

通过将评分准则的意图根植于可操作的决策流程中，ExecRubrics 使得评估过程可以直接被检查、执行和编辑。该框架在三大长文本回复基准（**HealthBench**、**HelpSteer** 和 **ArgQuality**）上进行了测试，成功取代了昂贵的黑盒裁判模型。它的表现持平或超越了基于自然语言准则的基线——偏好准确率分别达到 **52.9%**、**75.3%** 和 **91.5%**，同时显著降低了评估延迟。此外，集成外部资源以及如 **NLTK** 和 **spaCy** 等文本处理工具进一步提升了准确率，这使得 ExecRubrics 成为透明度、可审计性和精确度至关重要的高风险领域（如医疗和金融）的理想解决方案。

---

# ExecRubrics: Executable Tool-Augmented Rubrics for Verifiable and Efficient Long-Form Evaluation

> # ExecRubrics: Executable Tool-Augmented Rubrics for Verifiable and Efficient Long-Form Evaluation

**arXiv ID:** [2608.22559](https://arxiv.org/abs/2608.22559)  
**Authors:** Kaustubh D. Dhole, Charles L. A. Clarke, Eugene Y. Agichtein  
**Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`); Information Retrieval (`cs.IR`)  
**Publication Status:** Accepted to EMNLP 2026 Findings  
**Dates:** Submitted on 23 Aug 2026; Last revised 27 Aug 2026 (v2)  

> **arXiv ID:** [2608.22559](https://arxiv.org/abs/2608.22559)  
> **Authors:** Kaustubh D. Dhole, Charles L. A. Clarke, Eugene Y. Agichtein  
> **Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`); Information Retrieval (`cs.IR`)  
> **Publication Status:** Accepted to EMNLP 2026 Findings  
> **Dates:** Submitted on 23 Aug 2026; Last revised 27 Aug 2026 (v2)  

---

## 📋 Summary

> ## 📋 Summary

传统的语言模型评估通常依赖于含糊不清的自然语言评分准则和不透明的黑盒大模型裁判，这些裁判假设标准之间存在线性、独立的聚合关系。为了解决这些局限性，作者引入了 **ExecRubrics**，这是一个将评分准则转化为紧凑、可执行的 Python 评分函数的新颖框架。

> Traditional language model evaluation often relies on ambiguous natural-language rubrics and opaque black-box LLM judges that assume linear, independent aggregation of criteria. To address these limitations, the authors introduce **ExecRubrics**, a novel framework that transforms rubrics into compact, executable Python scoring functions. 

通过将准则意图置于可操作的决策程序中，ExecRubrics 可以直接接受检查、执行和编辑。在三个长文本回复基准（**HealthBench**、**HelpSteer** 和 **ArgQuality**）上经过测试，该框架成功取代了昂贵的黑盒裁判。它的表现达到或超过了自然语言准则基线——偏好准确率分别达到 **52.9%**、**75.3%** 和 **91.5%**——同时显著降低了评估延迟。此外，集成外部资源以及 **NLTK** 和 **spaCy** 等文本处理工具进一步提升了准确率，这使得 ExecRubrics 成为透明度、可审计性和精确度至关重要的高风险领域（例如医疗和银行）的理想解决方案。

> By grounding rubric intent in an operational decision procedure, ExecRubrics can be inspected, edited, and executed directly. Tested across three long-form response benchmarks (**HealthBench**, **HelpSteer**, and **ArgQuality**), the framework successfully replaces expensive black-box judges. It matches or outperforms natural-language rubric baselines—achieving preference accuracies of **52.9%**, **75.3%**, and **91.5%** respectively—while significantly reducing evaluation latency. Furthermore, integrating external resources and text-processing tools like **NLTK** and **spaCy** enhances accuracy further, making ExecRubrics an ideal solution for high-stakes domains (e.g., healthcare and banking) where transparency, auditability, and precision are vital.

---

## 🛠️ Key Contributions

> ## 🛠️ Key Contributions

* **可执行语义：** 用可验证的 Python 评分函数取代了含糊不清的自然语言评分准则。
* **复杂依赖处理：** 超越了简单的线性加权求和，能够无缝支持惩罚、覆盖、替代方案以及多标准依赖关系。
* **工具增强：** 结合了文本处理库（例如 `NLTK` 和 `spaCy`），以增强评估的可靠性。
* **效率与可解释性：** 大幅降低延迟，消除了对黑盒大模型裁判的依赖，提升了关键部门中的可审计性。

> * **Executable Semantics:** Replaces ambiguous natural-language rubrics with verifiable Python scoring functions.
> * **Complex Dependency Handling:** Moves beyond simple linear weighted sums to seamlessly support penalties, overrides, alternatives, and multi-criteria dependencies.
> * **Tool Augmentation:** Incorporates text-processing libraries (such as `NLTK` and `spaCy`) to bolster evaluation reliability.
> * **Efficiency & Interpretability:** Dramatically lowers latency and eliminates the dependency on black-box LLM judges, increasing auditability in critical sectors.

---

## 📊 Benchmark Performance

> ## 📊 Benchmark Performance

| 基准测试 (Benchmark) | 最佳偏好准确率 (Best Preference Accuracy) | 状态 / 比较 (Status / Comparison) |
| :--- | :--- | :--- |
| **HealthBench** | **52.9%** | 以更低的延迟匹配/改进了自然语言基线 |
| **HelpSteer** | **75.3%** | 以更低的延迟匹配/改进了自然语言基线 |
| **ArgQuality** | **91.5%** | 以更低的延迟匹配/改进了自然语言基线 |

> | Benchmark | Best Preference Accuracy | Status / Comparison |
> | :--- | :--- | :--- |
> | **HealthBench** | **52.9%** | Matches/Improves NL baselines with lower latency |
> | **HelpSteer** | **75.3%** | Matches/Improves NL baselines with lower latency |
> | **ArgQuality** | **91.5%** | Matches/Improves NL baselines with lower latency |

---

## 🔗 Links and Resources

> ## 🔗 Links and Resources

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2608.22559) | [HTML 版本（实验性）](https://arxiv.org/html/2608.22559v2) | [TeX 源码](https://arxiv.org/src/2608.22559)
* **数字对象唯一标识符 (DOI)：** [10.48550/arXiv.2608.22559](https://doi.org/10.48550/arXiv.2608.22559)
* **外部引用：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.22559) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.22559) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.22559)
* **许可协议：** [知识共享署名 4.0 国际版](http://creativecommons.org/licenses/by/4.0/)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.22559) | [HTML Version (Experimental)](https://arxiv.org/html/2608.22559v2) | [TeX Source](https://arxiv.org/src/2608.22559)
> * **Digital Object Identifier (DOI):** [10.48550/arXiv.2608.22559](https://doi.org/10.48550/arXiv.2608.22559)
> * **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.22559) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.22559) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.22559)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)

---
*(注：根据源布局保留了许可证图标)*  
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> ---
> *(Note: License icon preserved as requested by source layout)*  
> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">