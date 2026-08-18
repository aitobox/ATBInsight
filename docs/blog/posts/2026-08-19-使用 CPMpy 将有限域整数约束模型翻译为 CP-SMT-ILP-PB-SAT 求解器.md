---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- CPMpy
- 约束求解
- 整数规划
- 自动翻译
- 组合优化
title: 使用 CPMpy 将有限域整数约束模型翻译为 CP/SMT/ILP/PB/SAT 求解器
---
### 文章背景与核心概要
约束求解是一种解决组合满足和优化问题的声明式方法，它允许用户通过约束条件和决策变量来指定参数，然后由通用求解器进行求解。尽管存在多种约束求解技术，但没有单个求解器能在所有应用中都表现出色，因此测试替代求解器的能力至关重要。然而，不同的求解范式支持不同的约束和变量。

本文介绍了一个在开源 **CPMpy** 库中实现的模块化框架，用于将高级逻辑和算术运算（包括 CP 全局约束）翻译为更低级的形式化体系：**CP、SMT QF-LIA、ILP、PB 以及 (Max)SAT**。该框架作为一个模块化的阶梯式瀑布流运行，其中低级范式可以重用高级范式的组件。所解决的关键技术挑战包括处理任意子表达式的否定、避免不必要的辅助变量，以及针对 ILP、PB 和 SAT 求解器对非线性算子进行精细的线性化处理。

---

## 摘要 (Summary)

> Constraint solving is a declarative approach to resolving combinatorial satisfaction and optimization problems by letting users specify parameters through constraints and decision variables, which a generic solver then resolves. While multiple constraint-solving technologies exist, no single solver performs uniformly well across all applications, necessitating the ability to test alternative solvers. However, different solving paradigms support distinct constraints and variables. 

> This paper introduces a modular framework implemented in the open-source **CPMpy** library to translate high-level logical and arithmetic operations (including CP global constraints) into lower-level formalisms: **CP, SMT QF-LIA, ILP, PB, and (Max)SAT**. The framework operates as a modular waterfall where lower-level paradigms reuse components of higher-level ones. Key technical challenges addressed include handling arbitrary subexpression negations, avoiding unnecessary auxiliary variables, and carefully linearizing non-linear operators for ILP, PB, and SAT solvers.

---

## 元数据 (Metadata)

* **arXiv ID:** [arXiv:2608.15143](https://arxiv.org/abs/2608.15143) [cs.AI]
> * **arXiv ID:** [arXiv:2608.15143](https://arxiv.org/abs/2608.15143) [cs.AI]
* **学科领域:** 人工智能 (`cs.AI`)
> * **Subject:** Artificial Intelligence (`cs.AI`)
* **提交日期:** 2026年8月15日
> * **Submission Date:** 15 August 2026
* **许可协议:** [知识共享署名 4.0 国际版 (Creative Commons Attribution 4.0)](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

---

## 作者 (Authors)

* Tias Guns
> * Tias Guns
* Ignace Bleukx
> * Ignace Bleukx
* Hendrik Bierlee
> * Hendrik Bierlee
* Jo Devriendt
> * Jo Devriendt
* Emilio Gamba
> * Emilio Gamba
* Orestis Lomis
> * Orestis Lomis
* Wout Piessens
> * Wout Piessens
* Thomas Sergeys
> * Thomas Sergeys
* Dimos Tsouros
> * Dimos Tsouros
* Wout Vanroose
> * Wout Vanroose
* Hélène Verhaeghe
> * Hélène Verhaeghe

---

## 核心特性与贡献 (Key Features & Contributions)

* **统一的高级语言：** 定义了各种操作和全局约束，免去了用户为每种求解范式手动重新建模问题的麻烦。
> * **Unified High-Level Language:** Defines operations and global constraints, sparing users from manually remodeling problems for each solving paradigm.
* **模块化转换瀑布流：** 系统化地转换高级约束语言，允许低级形式化体系构建在高级翻译的基础之上。
> * **Modular Transformation Waterfall:** Transforms high-level constraint languages systematically, allowing lower-level formalisms to build upon higher-level translations.
* **对子表达式与变量的高级处理：**
> * **Advanced Handling of Subexpressions & Variables:**
  * 高效管理任意子表达式的否定。
>   * Efficiently manages the negation of arbitrary subexpressions.
  * 减轻辅助变量的激增问题。
>   * Mitigates the proliferation of auxiliary variables.
  * 为 ILP、PB 和 SAT 求解器所需的非线性算子实现优化的线性化策略。
>   * Implements optimized linearization strategies for non-linear operators required by ILP, PB, and SAT solvers.
* **开源实现：** 在 **CPMpy** 库中完全实现并评估，证明了模型经历了显著的转换，且约束线性化优化对于 ILP 和 PB 求解器至关重要。
> * **Open-Source Implementation:** Fully realized and evaluated within the **CPMpy** library, demonstrating that models undergo significant transformations and that constraint linearization optimizations are crucial for ILP and PB solvers.

---

## 访问链接 (Access Links)

* [查看 PDF (View PDF)](https://arxiv.org/pdf/2608.15143)
> * [View PDF](https://arxiv.org/pdf/2608.15143)
* [HTML 版本 - 实验性 (HTML Version (Experimental))](https://arxiv.org/html/2608.15143v1)
> * [HTML Version (Experimental)](https://arxiv.org/html/2608.15143v1)
* [TeX 源码 (TeX Source)](https://arxiv.org/src/2608.15143)
> * [TeX Source](https://arxiv.org/src/2608.15143)
* [DOI 引用 (DOI Reference)](https://doi.org/10.48550/arXiv.2608.15143)
> * [DOI Reference](https://doi.org/10.48550/arXiv.2608.15143)