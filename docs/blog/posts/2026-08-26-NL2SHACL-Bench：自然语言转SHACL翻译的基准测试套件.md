---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- SHACL
- 知识图谱
- 大语言模型
- 基准测试
- 自然语言处理
title: NL2SHACL-Bench：自然语言转SHACL翻译的基准测试套件
---
### 文章背景与核心概要
SHACL（形状约束语言，Shapes Constraint Language）对于验证 RDF 知识图谱至关重要，但其复杂性给领域专家设置了巨大的门槛。**NL2SHACL-Bench** 套件填补了将自然语言需求翻译为 SHACL 缺乏标准化评估工具的空白。该基准测试超越了简单的字符串比较，转向语义等价性评估，为评估大语言模型（LLM）提供了一个强有力的框架。

研究表明，虽然当前的大语言模型在生成语法正确的 SHACL 方面表现出色，但它们在准确进行约束建模所需的复杂逻辑和结构模式方面依然力不从心。该论文已被 ISWC 2026 接受。

---

# NL2SHACL-Bench: A Benchmark Suite for Natural Language to SHACL Translation

**Authors:** Yuchen Zhou, Niels Bobet, Maribel Acosta  
**Published:** arXiv:2608.07530 [cs.AI] (Accepted at ISWC 2026)

> # NL2SHACL-Bench: A Benchmark Suite for Natural Language to SHACL Translation
> 
> **Authors:** Yuchen Zhou, Niels Bobet, Maribel Acosta  
> **Published:** arXiv:2608.07530 [cs.AI] (Accepted at ISWC 2026)

---

## Summary

SHACL (Shapes Constraint Language) is essential for validating RDF knowledge graphs, yet its complexity creates a significant barrier for domain experts. The **NL2SHACL-Bench** suite addresses the lack of standardized evaluation tools for translating natural language requirements into SHACL. By moving beyond simple string comparison to semantic equivalence, this benchmark provides a robust framework for evaluating Large Language Models (LLMs). The study reveals that while current LLMs excel at generating syntactically valid SHACL, they struggle with the complex logical and structural patterns required for accurate constraint modeling.

> ## Summary
> 
> SHACL (Shapes Constraint Language) is essential for validating RDF knowledge graphs, yet its complexity creates a significant barrier for domain experts. The **NL2SHACL-Bench** suite addresses the lack of standardized evaluation tools for translating natural language requirements into SHACL. By moving beyond simple string comparison to semantic equivalence, this benchmark provides a robust framework for evaluating Large Language Models (LLMs). The study reveals that while current LLMs excel at generating syntactically valid SHACL, they struggle with the complex logical and structural patterns required for accurate constraint modeling.

---

## Key Research Contributions

*   **Benchmark Development:** Introduction of the first dedicated benchmark suite specifically designed for the NL2SHACL task.
*   **Evaluation Methodology:** Implementation of evaluation methods that account for semantic equivalence, acknowledging that valid SHACL shapes can be serialized and structured in multiple ways.
*   **LLM Performance Analysis:** A comparative study of four state-of-the-art LLMs, highlighting their strengths in syntax and weaknesses in complex logical reasoning.
*   **Future Direction:** Establishes a baseline for measuring future advancements in the automated generation of semantic constraints.

> ## Key Research Contributions
> 
> *   **Benchmark Development:** Introduction of the first dedicated benchmark suite specifically designed for the NL2SHACL task.
> *   **Evaluation Methodology:** Implementation of evaluation methods that account for semantic equivalence, acknowledging that valid SHACL shapes can be serialized and structured in multiple ways.
> *   **LLM Performance Analysis:** A comparative study of four state-of-the-art LLMs, highlighting their strengths in syntax and weaknesses in complex logical reasoning.
> *   **Future Direction:** Establishes a baseline for measuring future advancements in the automated generation of semantic constraints.

---

## Metadata & Access

| Category | Details |
| :--- | :--- |
| **Subjects** | Artificial Intelligence (cs.AI), Computation and Language (cs.CL), Databases (cs.DB) |
| **DOI** | [10.48550/arXiv.2608.07530](https://doi.org/10.48550/arXiv.2608.07530) |
| **Version** | v2 (Last revised 22 Aug 2026) |

> ## Metadata & Access
> 
> | Category | Details |
> | :--- | :--- |
> | **Subjects** | Artificial Intelligence (cs.AI), Computation and Language (cs.CL), Databases (cs.DB) |
> | **DOI** | [10.48550/arXiv.2608.07530](https://doi.org/10.48550/arXiv.2608.07530) |
> | **Version** | v2 (Last revised 22 Aug 2026) |

### Full-Text Access
*   [View PDF](https://arxiv.org/pdf/2608.07530)
*   [HTML (Experimental)](https://arxiv.org/html/2608.07530v2)
*   [TeX Source](https://arxiv.org/src/2608.07530)

> ### Full-Text Access
> *   [View PDF](https://arxiv.org/pdf/2608.07530)
> *   [HTML (Experimental)](https://arxiv.org/html/2608.07530v2)
> *   [TeX Source](https://arxiv.org/src/2608.07530)

---

### License Information
<a href="http://creativecommons.org/publicdomain/zero/1.0/" title="Rights to this article">
<img alt="license icon" role="presentation" src="./images/d7507cd66373.png">
<span>View License (CC0 1.0)</span>
</a>

> ### License Information
> <a href="http://creativecommons.org/publicdomain/zero/1.0/" title="Rights to this article">
> <img alt="license icon" role="presentation" src="./images/d7507cd66373.png">
> <span>View License (CC0 1.0)</span>
> </a>