---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- Modelica
- 物理系统建模
- AI智能体
- 基准测试
- Pufibara
title: 超越可执行模型：用于物理系统建模的 Pufibara 智能体框架与 Modelica 智能体工作流基准
---
### 文章背景与核心概要
物理系统建模给 AI 智能体带来了超越标准软件工程代码生成的独特挑战。在像 **Modelica** 这样基于方程的语言中，代码虽然可以成功编译和仿真，但仍可能违反核心物理定律或特定场景的需求。

为了解决智能体在跨版本修订过程中跟踪需求丢失或依赖过时仿真数据的问题，本文引入了：1. **Pufibara**：一个维护持久化工程状态、将执行/仿真证据映射到生成它的特定候选者、并使提交成为显式智能体操作的智能体框架。2. **Modelica 智能体工作流基准（MAWB）**：一个通过源基底（source-grounded）方法构建包含 232 个任务的基准测试套件，涵盖*模型修复*、*模型生成*和*模型调优*，由独立的基准自有评估器进行评估。

对比实验表明，在匹配的大语言模型（LLM）后端下，**Pufibara** 的表现优于 Claude Code，在实现更高任务成功率的同时，大幅减少了逻辑 Token 消耗和串行运行时间。

---

# 超越可执行模型：用于物理系统建模的 Pufibara 智能体框架与 Modelica 智能体工作流基准

> # Beyond Executable Models: The Pufibara Agent Harness and the Modelica Agent Workflow Benchmark for Physical System Modeling

**作者：** Zizhe Wang  
**发布时间：** 2026年8月24日  
**主要学科：** 软件工程 (`cs.SE`)  
**次要学科：** 人工智能 (`cs.AI`)  
**arXiv ID：** [2608.23653](https://arxiv.org/abs/2608.23653)  

---

## 📌 摘要

> ## 📌 Summary

物理系统建模给 AI 智能体带来了超越标准软件工程代码生成的独特挑战。在像 **Modelica** 这样基于方程的语言中，代码虽然可以成功编译和仿真，但仍可能违反核心物理定律或特定场景的需求。 

> Physical system modeling introduces unique challenges for AI agents that go beyond standard software engineering code generation. In equation-based languages like **Modelica**, code may compile and simulate successfully while still violating core physical laws or scenario-dependent requirements. 

为了解决智能体在跨版本修订过程中跟踪需求丢失或依赖过时仿真数据的问题，本文引入了：
1. **Pufibara**：一个维护持久化工程状态、将执行/仿真证据映射到生成它的特定候选者、并使提交成为显式智能体操作的智能体框架。
2. **Modelica 智能体工作流基准（MAWB）**：一个通过源基底方法构建包含 232 个任务的基准测试套件，涵盖*模型修复*、*模型生成*和*模型调优*，由独立的基准自有评估器进行评估。

> To resolve the issues of agents losing track of requirements or relying on outdated simulation data across revisions, this paper introduces:
> 1. **Pufibara**: An agent harness that maintains persistent engineering state, maps execution/simulation evidence to the specific candidate that generated it, and makes submission an explicit agent action.
> 2. **Modelica Agent Workflow Benchmark (MAWB)**: A 232-task benchmark suite built via a source-grounded method, covering *Model Repair*, *Model Generation*, and *Model Tuning*, evaluated by an independent, benchmark-owned evaluator.

对比实验表明，在匹配的大语言模型（LLM）后端下，**Pufibara** 的表现优于 Claude Code，在实现更高任务成功率的同时，大幅减少了逻辑 Token 消耗和串行运行时间。

> Comparative experiments show that **Pufibara** outperforms Claude Code across matched Large Language Model (LLM) backends, achieving higher task success rates while dramatically reducing logical-token consumption and sequential runtime.

---

## 🚀 核心贡献与方法论

> ## 🚀 Key Contributions & Methodology

* **持久化工程状态：** Pufibara 跨迭代跟踪候选状态，防止智能体回退到过时的仿真日志或偏离用户约束。
* **显式提交工作流：** 要求智能体显式声明候选提交，而不是依赖隐式或不稳定的停止标准。
* **严谨的评估套件：** 232 个任务的基准严格将智能体环境与评分分离，确保物理系统任务性能测量的无偏性。

> * **Persistent Engineering State:** Pufibara tracks candidate states across iterations, preventing agents from falling back on obsolete simulation logs or straying from user constraints.
> * **Explicit Submission Workflow:** Mandates that the agent explicitly declare a candidate submission rather than relying on implicit or volatile stopping criteria.
> * **Rigorous Evaluation Suite:** The 232-task benchmark strictly separates the agent environment from scoring, ensuring unbiased performance measurement for physical system tasks.

---

## 📊 实验结果

> ## 📊 Experimental Results

当与完整的基线框架（Claude Code）进行对比测试时，Pufibara 展现出了卓越的效率和准确性：

> When tested against complete baseline harnesses (Claude Code), Pufibara demonstrated superior efficiency and accuracy:

* **DeepSeek v4 Flash 后端：**
  * **Pufibara：** 通过 202 个任务
  * **Claude Code：** 通过 185 个任务
* **Claude Sonnet 5 后端：**
  * **Pufibara：** 通过 202 个任务
  * **Claude Code：** 通过 187 个任务
* **资源效率：**
  * **逻辑 Token：** 减少 76.4% 至 82.5%。
  * **串行运行时间：** 减少 6.1% 至 58.4%。

> * **DeepSeek v4 Flash Backend:**
>   * **Pufibara:** 202 tasks passed
>   * **Claude Code:** 185 tasks passed
> * **Claude Sonnet 5 Backend:**
>   * **Pufibara:** 202 tasks passed
>   * **Claude Code:** 187 tasks passed
> * **Resource Efficiency:**
>   * **Logical Tokens:** 76.4% to 82.5% reduction.
>   * **Sequential Runtime:** 6.1% to 58.4% reduction.

---

## 🔗 链接与资源

> ## 🔗 Links & Resources

* **查看 PDF：** [arXiv:2608.23653 PDF](https://arxiv.org/pdf/2608.23653)
* **HTML 版本：** [arXiv HTML (实验性)](https://arxiv.org/html/2608.23653v1)
* **DOI：** [10.48550/arXiv.2608.23653](https://doi.org/10.48550/arXiv.2608.23653)

> * **View PDF:** [arXiv:2608.23653 PDF](https://arxiv.org/pdf/2608.23653)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.23653v1)
> * **DOI:** [10.48550/arXiv.2608.23653](https://doi.org/10.48550/arXiv.2608.23653)

---
*许可信息：* <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"><span>查看许可</span></a>
> *License info:* <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"><span>view license</span></a>