---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-10
hide:
- navigation
tags:
- 大模型
- 因果推断
- 基准测试
- 计量经济学
- R语言
title: CausalVerify：面向大模型因果推断工作流的执行接地基准测试
---
### 文章背景与核心概要
当前的各类大语言模型（LLM）因果推断基准测试，往往仅停留在评估表面层面的指标上，例如方法描述，或者生成的代码是否能够无报错运行，却缺乏对最终生成的工作流是否真正恢复出目标因果估计值的有效检验。

为了解决这一痛点，**CausalVerify** 针对结构化计量经济学因果估计工作流，引入了一个强健的验证框架，该框架将真实的语义解释与可验证的计算过程进行了清晰解耦。该基准测试主要包含两大核心组件：一是涵盖 **259 篇已发表经济学论文**的重构数据集，包含研究问题、数据描述和制度背景；二是 **100 个固定种子的合成场景**，可生成覆盖四大主流设计系列（*双重差分、事件研究、工具变量* 以及 *断点回归设计*）的具体 CSV 数据集。

---

## CausalVerify: An Execution-Grounded Benchmark for LLM Causal Inference Workflows

*[arXiv:2609.07944 [cs.AI]]*(https://arxiv.org/abs/2609.07944)  
**Submitted on:** 7 September 2026  
**Authors:** Yonghong Zhang, Ricardo Correia, Isabel M. Parra, Yong Xie  

---

## 摘要 (Summary)

> Current causal-inference benchmarks for Large Language Models (LLMs) often evaluate surface-level metrics, such as method descriptions or whether generated code simply runs, without testing whether the resulting workflow actually recovers the target causal estimate. 

> **CausalVerify** introduces a robust verification framework for structured econometric causal-estimation workflows by decoupling realistic interpretation from verifiable computation. The benchmark features:
> * **259 Published Economics Papers:** Reconstructed with research questions, data descriptions, and institutional contexts.
> * **100 Fixed-Seed Synthetic Scenarios:** Generating concrete CSV datasets across four major design families: *difference-in-differences, event study, instrumental variables,* and *regression discontinuity designs*.

### 关键实验与发现 (Key Experiments & Findings)

> 1. **Experiment A (Real-Paper Text Agreement):** Evaluates method-family and direction agreement against a four-LLM consensus label.
> 2. **Experiment B (Synthetic Execution):** Executes model-written R code to determine whether the extracted treatment-effect estimates match a canonical estimator on the same dataset. This introduces an execution-grounded correctness layer (**L2b+**), going beyond standard code execution checks (**L2b**).
>   * **Pass Rates:** Seven evaluated LLMs achieved L2b+ pass rates ranging from **10% to 88%** (at a default 50% tolerance).
>   * **Error Rates:** Out of 426 successfully executed workflows, **66 (15.5%)** returned incorrect estimates.
>   * **Metric Correlation:** Execution ranking (**L2b**) correlates strongly with L2b+ ($\tau = 0.81$, $\rho = 0.93$), whereas text-direction scoring (**L4**) shows poor alignment ($\tau$ between $-0.20$ and $0.10$).
> 3. **Calibration Arm:** Demonstrates that self-reported LLM confidence does not reliably differentiate between correct and incorrect workflows.

> *Note: Findings are specific to standardized single-shot workflows within the evaluated R backend and model panel, and do not reflect general causal-inference capabilities.*

---

## 其他元数据 (Additional Metadata)

> * **Subjects:** Artificial Intelligence (`cs.AI`); Computation and Language (`cs.CL`); Econometrics (`econ.EM`)
> * **Cite As:** [arXiv:2609.07944](https://arxiv.org/abs/2609.07944) [cs.AI]
> * **Full-Text & Resources:** 
>   * [View PDF](https://arxiv.org/pdf/2609.07944)
>   * [Code & Data Repository](https://github.com/causalverify/causalverify)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">