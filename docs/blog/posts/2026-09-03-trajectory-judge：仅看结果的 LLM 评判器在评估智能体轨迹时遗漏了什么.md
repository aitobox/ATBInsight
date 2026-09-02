---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- LLM智能体
- 评估方法
- 评判器
- 错误注入
- 可复现性
title: trajectory-judge：仅看结果的 LLM 评判器在评估智能体轨迹时遗漏了什么
---
### 文章背景与核心概要
当前，大语言模型（LLM）智能体的评估普遍采用“仅看结果（outcome-only）”的方法，即仅向评判器展示初始请求和最终回复来判定任务是否成功。然而，这种方法在结构上无法识别那些通过有缺陷的过程偶然得到正确答案的智能体。Hadi Mohammadi 在其论文《trajectory-judge: What Outcome-Only LLM Judges Miss on Agent Trajectories》中深入探讨了这种传统评估方式的局限性。

为了量化这一盲区，作者引入了一个受控的、确定性的工具调用客服支持环境，并配备了预言机策略（oracle policy）和故障注入器。通过对 5 个不同评判器的 400 条轨迹进行测试，该研究揭示了基于结果的评估方法所存在的重大漏洞（例如遗漏静默故障和幻觉承诺），提倡采用关注步骤的评分标准（step-aware rubrics），并提供了用于可复现分析的开源工具。

---

## 元数据与参考信息

* **arXiv ID:** [arXiv:2609.00038 [cs.CL]](https://arxiv.org/abs/2609.00038)
* **作者:** Hadi Mohammadi
* **主要学科:** 计算与语言 (`cs.CL`)
* **次要学科:** 人工智能 (`cs.AI`)、软件工程 (`cs.SE`)
* **状态:** 16页（正文8页）；正在 NeurIPS 2026 研讨会审稿中。
* **代码与数据:** [GitHub 仓库](https://github.com/mohammadi-hadi/trajectory-judge)

> ## Metadata & Reference Information
> 
> * **arXiv ID:** [arXiv:2609.00038 [cs.CL]](https://arxiv.org/abs/2609.00038)
> * **Authors:** Hadi Mohammadi
> * **Primary Subject:** Computation and Language (`cs.CL`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Software Engineering (`cs.SE`)
> * **Status:** 16 pages (8-page main text); under review at a NeurIPS 2026 workshop.
> * **Code & Data:** [GitHub Repository](https://github.com/mohammadi-hadi/trajectory-judge)

---

## 摘要与核心发现

仅看结果的评估是 LLM 智能体在生产环境中的默认做法，但它很难捕捉到那些最终面向用户的成果侥幸存活下来的过程级失败。

> ## Abstract & Core Findings
> 
> Outcome-only evaluation is the production default for LLM agents, but it struggles to catch process-level failures where the final user-facing outcome accidentally survives. 

### 关键实验设置
* **环境：** 一个确定性的、支持工具调用的客服桌面环境。
* **方法论：** 编写始终能解决环境问题的预言机策略，并搭配一个在已知步骤中精确破坏单个组件的故障注入器。故障被分层为：
  * **显式故障（Loud faults）：** 用户可见的结果未能存活。
  * **静默故障（Silent faults）：** 尽管存在内部错误，但用户可见的结果依然存活。
* **被评估的评判器（在 400 条轨迹上测试）：**
  1. 编程规则
  2. 仅看结果的 LLM 评判器
  3. 步骤评分标准评判器（在两种模型规模下测试）
  4. 自洽性集成评判器

> ### Key Experimental Setup
> * **Environment:** A deterministic tool-using support-desk environment.
> * **Methodology:** A scripted oracle policy that always solves the environment paired with a fault injector that breaks exactly one component at a known step. Faults are stratified into:
>   * **Loud faults:** Customer-visible outcome did not survive.
>   * **Silent faults:** Customer-visible outcome survived despite internal errors.
> * **Evaluated Judges (Tested over 400 trajectories):**
>   1. Programmatic rules
>   2. Outcome-only LLM judge
>   3. Step-rubric judges (tested at two model sizes)
>   4. Self-consistency ensemble judge

### 关键结果
* **仅看结果的盲区：** 仅看结果的评判器能够捕捉 **84% 的显式故障**，但只能捕捉 **45% 的静默故障**，同时错误地将 **33% 的正确轨迹** 标记为有问题。
* **步骤评分标准的表现：** 步骤评分标准评判器达到了 **77% 的静默故障召回率且误报率为零**，不过其**成本是前者的 3 倍**。
* **最终回复陷阱：** *没有任何*一个评判器能够充分阅读最终的回复上下文；附加在完美轨迹上的虚构承诺完全避开了简单规则的检测，并且在 **82% 的情况下**成功欺骗了步骤评判器。
* **成本与收益：** 自洽性集成（Self-consistency ensembles）使评估成本翻了三倍，却没有带来任何性能提升。

> ### Key Results
> * **The Outcome-Only Blind Spot:** The outcome-only judge catches **84% of loud faults**, but only **45% of silent ones**, while incorrectly flagging **33% of correct trajectories**.
> * **Step-Rubric Performance:** A step-rubric judge reaches **77% silent recall with zero false alarms**, though at **3x the cost**.
> * **The Final Reply Trap:** *No* judge adequately reads the final reply context; an invented promise appended to an otherwise perfect trajectory evades simple rules entirely and fools the step judge **82% of the time**.
> * **Cost vs. Benefit:** Self-consistency ensembles triple evaluation costs without yielding any performance improvements.

---

## 全文与访问链接

* [查看 PDF](https://arxiv.org/pdf/2609.00038)
* [HTML 版本（实验性）](https://arxiv.org/html/2609.00038v1)
* [TeX 源码](https://arxiv.org/src/2609.00038)
* [DOI 链接](https://doi.org/10.48550/arXiv.2609.00038)

> ## Full-Text & Access Links
> 
> * [View PDF](https://arxiv.org/pdf/2609.00038)
> * [HTML Version (Experimental)](https://arxiv.org/html/2609.00038v1)
> * [TeX Source](https://arxiv.org/src/2609.00038)
> * [DOI Link](https://doi.org/10.48550/arXiv.2609.00038)