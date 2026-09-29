---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-30
hide:
- navigation
tags:
- 谷歌
- RRSI
- AI 智能体
- Harness 架构
- 自优化
- 开源框架
title: 谷歌开源 RRSI 框架：让 AI 智能体自主优化 Harness 架构且避免过拟合
---
# 谷歌开源 RRSI 框架：让 AI 智能体自主优化 Harness 架构且避免过拟合

> # Google Research Open-Sources RRSI: AI Agents That Improve Their Own Harness Without Overfitting

### 文章背景与核心概要
在追求更高性能的 AI 智能体 (AI Agent) 研发过程中，工程师通常需要不断优化系统外围的脚手架——即所谓的“Harness 架构” (涵盖提示词、工具链、记忆机制与控制调度等) 。然而，传统的自主进化算法往往会导致智能体“死记硬背”评测集中的特定题目，陷入严重的过拟合陷阱，导致在面对全新的未知任务时表现大幅滑坡。针对这一痛点，Google Cloud AI Research 携手多所顶尖高校开源了 RRSI (Regularized Recursive Self-Improvement，正则化递归自我改进) 框架。该框架创新性地在底层模型权重完全冻结的前提下，通过引入类似于经典机器学习惩罚项的“正则化”约束机制，让智能体不仅能安全自主地修改重写自身的外围 Harness 架构，还能有效遏制代码膨胀与噪声干扰。在 8 大主流基准测试中，经由 RRSI 进化的智能体在未见过的测试集上实现了全面稳步提升，同时推理 Token 消耗降低多达 36%，为构建真正具备通用泛化与自主进化能力的 AI 智能体系统指明了全新方向。

---

## 执行摘要

> ## Executive Summary

**Google Cloud AI Research** 携手 UNC-Chapel Hill、Stanford 以及 Washington University in St. Louis 联合推出了 **RRSI (Regularized Recursive Self-Improvement)** 开源框架。这项突破性框架允许大语言模型 (Large Language Model, LLM) 智能体在底层模型权重完全冻结的前提下，自主重构并进化自身的 Harness 架构——涵盖提示词、工具集、记忆机制、控制流以及子智能体。通过对自我改进闭环引入严格的正则化机制，RRSI 确保智能体获得的性能提升不仅局限于训练任务，还能稳健地迁移泛化到从未针对优化过的全新基准测试中。

> **Google Cloud AI Research**, in collaboration with UNC-Chapel Hill, Stanford, and Washington University in St. Louis, has released **RRSI (Regularized Recursive Self-Improvement)**. This innovative framework allows LLM agents to rewrite their own harnesses—including prompts, tools, memory, control flow, and sub-agents—while keeping model weights entirely frozen. By regularizing the improvement loop, RRSI ensures that performance gains translate robustly to benchmarks the agent has never optimized against. 

该框架基于 **Apache 2.0 许可证** 开源发布，运行环境要求 Python 3.10+，并全面支持任意 LiteLLM 模型标识符 (默认配置为 Vertex AI 上的 Claude Opus 4.8) 。

> The framework is available under the **Apache 2.0 license**, requires Python 3.10+, and supports any LiteLLM model string (with defaults configured for Claude Opus 4.8 on Vertex AI).

---

## 为什么自主优化的 Harness 架构容易发生过拟合？

> ## Why Self-Improving Harnesses Overfit

传统的 Harness 架构进化闭环通常采用“提出修改建议、在固定任务集上打分评测、保留胜出方案”的模式。然而，由于系统在每一轮迭代中都反复面对同一套测试题目，这种闭环往往不可避免地走向了“死记硬背”。[RRSI 的研究](https://arxiv.org/abs/2609.24972) 指出，这一流程会引发三大典型的失效模式：

> Traditional harness evolution loops propose edits, score them against a fixed set of tasks, and retain the winners. Because the same tasks are repeatedly evaluated every round, the loop tends to memorize them. According to the [RRSI research](https://arxiv.org/abs/2609.24972), this process introduces three primary failure modes:

1. **特定基准拟合 (Benchmark-specific fitting)**：智能体学会了针对特定题库走捷径，甚至记住评测集的特有逻辑；
2. **追逐随机噪声 (Noise chasing)**：由于评估本身的波动性，把随机产生的微小分值波动误当成实质性进步；
3. **复杂度盲目堆积 (Complexity accumulation)**：代码和提示词不断变长、系统越来越臃肿，却缺乏真正提升通用能力的实质改动。

> 1. **Benchmark-specific fitting**
> 2. **Noise chasing**
> 3. **Complexity accumulation**

这三种失效模式共同拉大了“进化集上的漂亮高分”与“实际分布外 (Out-of-Distribution, OOD) 泛化性能”之间的鸿沟。

> Each failure mode widens the gap between high evolve-set scores and actual out-of-distribution transfer performance.

---

## RRSI 的工作原理

> ## How RRSI Works

RRSI 允许 Harness 架构中的每个组件都保持可编辑与可塑状态，但为整个搜索过程的演进步伐引入了极其严苛的正则化控制。

> RRSI allows every component of the harness to remain editable, but introduces rigorous regularization to how the search process moves.

### 提议端机制

> ### Proposal Side

* **退火编辑预算 (Annealed Edit Budget)**：采用类似余弦退火的调度策略，允许早期迭代大刀阔斧地捆绑多项协同修改，而在后期轮次则收敛并严格限制为单一、因果明确的细微改动。
* **基于证据的经验归因 (Evidence-Aware Credit)**：系统会完整记录每个候选方案所改动的组件、设计假设、代码补丁 (diff) 、分数波动以及推理开销变化。提议生成模块会读取这份详尽的“经验账本”，从而避免重蹈已被证伪方案的覆辙。
* **结构化探索机制 (Structured Exploration)**：一旦优化进程在噪声容限区间内停滞不前，搜索预算将动态倾斜转移到此前运行中尚未涉足的外围组件上。

> * **Annealed Edit Budget:** A cosine schedule permits early rounds to bundle several coordinated edits, while restricting late rounds to single, attributable changes.
> * **Evidence-Aware Credit:** Every candidate logs its component, hypothesis, diff, score change, and cost change. The proposer reads this ledger to prevent repeating falsified ideas.
> * **Structured Exploration:** If progress stalls within the noise band, the search budget is dynamically shifted to components that the run has not yet touched.

### 筛选端机制

> ### Selection Side

* **数据泄漏审查器 (Leakage Critic)**：在进入评估打分前，自动识别并拦截任何硬编码的任务名称、特定实体、标准答案或针对基准特异性编写的“作弊”逻辑。
* **噪声校准门槛 (Noise-Adjusted Floor)**：方案带来的性能提升幅度，必须显著超越未改动的基础 Harness 在评测中所固有的方差波动底线。
* **成本约束规则 (Cost Rule)**：任何导致推理 Token 消耗增加的改动，都必须通过可量化的显著性能增益来证明其合理性。
* **冗余剪枝机制 (Pruning)**：那些无法再带来可衡量收益的陈旧组件，会被系统列为删除和清理的目标。

> * **Leakage Critic:** Automatically rejects task names, entities, answers, or benchmark-specific logic prior to scoring.
> * **Noise-Adjusted Floor:** Performance gains must definitively clear the variance measured on the unchanged base harness.
> * **Cost Rule:** Any increase in inference tokens must be justified by a measured performance gain.
> * **Pruning:** Components that cease to produce measurable gains become targets for deletion.

* (研究团队将这些控制机制类比为经典的数学正则化方法：编辑预算起到了类似 $L_0$ 范数稀疏化的作用，剪枝机制类似于 Lasso ($L_1$) 正则化，而成本约束规则则契合了 Ridge ($L_2$) 岭回归正则化。) *

> *(The research team maps these mechanisms to classical regularizers: the edit budget acts like $L_0$, pruning functions like Lasso ($L_1$), and the cost rule mirrors Ridge ($L_2$).)*

---

## 跨 8 大基准测试的卓越性能表现

> ## Performance Across 8 Benchmarks

* **Terminal-Bench 2.1** (进化集划分 / evolve split)：准确率从 **74.2% 跃升至 80.2%**。
* **SWE-bench Verified** (保留测试集划分 / held-out，从未用于方案筛选)：准确率从 **82.0% 稳步提升至 83.8%**。
* **分布外 (OOD) 泛化测试**：[JobBench](https://github.com/Job-Bench/job-bench-eval) (**+4.7 分**)、[GDPval](https://openai.com/index/gdpval/) (**+3.5 分**) 以及 [APEX-Agents](https://www.mercor.com/apex/apex-agents-leaderboard/) (**+3.7 分**)。
* **EngDesign** (进化集划分)：提升 **+4.9 分**；[Frontier-Engineering](https://github.com/Einsia/Frontier-Engineering)：奖牌积分提升 **+4.3 分**。
* **Harvey LAB**：在进化集划分上提升 **+1.1 分**，在保留测试集划分上提升 **+2.3 分**。

> * **Terminal-Bench 2.1** (evolve split): Improved from **74.2% to 80.2%**.
> * **SWE-bench Verified** (held-out / never used for selection): Improved from **82.0% to 83.8%**.
> * **Out-of-Distribution (OOD):** [JobBench](https://github.com/Job-Bench/job-bench-eval) (**+4.7**), [GDPval](https://openai.com/index/gdpval/) (**+3.5**), and [APEX-Agents](https://www.mercor.com/apex/apex-agents-leaderboard/) (**+3.7** points).
> * **EngDesign** (evolve split): **+4.9**; [Frontier-Engineering](https://github.com/Einsia/Frontier-Engineering): **+4.3** Medal points.
> * **Harvey LAB:** **+1.1** on the evolve split, and **+2.3** on its held-out split.

在整体评测中，**所有 6 个保留划分集均实现了性能提升**。当采用 [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/) 作为基础策略模型时，Terminal-Bench 2.1 的得分从 64.6 攀升至 78.7，SWE-bench Verified 的得分也由 76.8 增至 79.0。此外，进化后的 Harness 架构更加轻量高效：在智能体工作区实例中，RRSI 每次试验仅消耗 **2.42M 策略 Token**，相比未施加正则化的传统进化基准所消耗的 **3.80M Token** 大幅缩减了 30% 到 36%。

> Across the board, **all 6 held-out splits improved**. When using [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/) as the policy, Terminal-Bench 2.1 scores rose from 64.6 to 78.7, and SWE-bench Verified rose from 76.8 to 79.0. Furthermore, the harness is lighter: on an agentic workspace instance, RRSI consumes **2.42M policy tokens per trial** compared to **3.80M** for unregularized evolution (a 30% to 36% reduction).

---

## RRSI 与主流竞品方案对比

> ## RRSI vs. Closest Competitors

*性能评测数据摘自 RRSI 研究论文中的 表 1: 。所有对比方法均基于完全相同的初始 Harness 架构、策略模型、进化集划分以及候选预算。*

> *Performance figures derived from Table 1 of the RRSI research paper. All methods share the identical starting harness, policy, evolve split, and candidate budget.*

| 特性对比 | RRSI | [Meta-Harness](https://arxiv.org/abs/2603.28052) | [AHE](https://arxiv.org/abs/2604.25850) | [TTHE](https://arxiv.org/abs/2607.08124) | [HarnessX](https://arxiv.org/abs/2606.14249) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **核心设计思想** | 正则化提议与筛选机制 | 基于代码、分数与执行轨迹的智能体提议器 | 可观测性驱动闭环；改动与已验证预测配对 | 在测试阶段演进 Harness 架构，无需真实标签 | 模块化类型化原语，执行轨迹驱动自适应 |
| **模型权重** | 冻结 | 冻结 | 冻结 | 冻结 | 冻结 |
| **成本规则与剪枝机制** | 是 | 否* | 否* | 否* | 否* |
| **Harvey LAB 进化集得分** | 90.5 | 93.0 | 90.7 | 91.1 | 91.8 |
| **分布外 (OOD) 平均得分 ($H_0 = 39.7$)** | **43.6** | 40.6 | 39.2 | 38.0 | 39.7 |

> | Feature | RRSI | [Meta-Harness](https://arxiv.org/abs/2603.28052) | [AHE](https://arxiv.org/abs/2604.25850) | [TTHE](https://arxiv.org/abs/2607.08124) | [HarnessX](https://arxiv.org/abs/2606.14249) |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | **Core idea** | Regularized proposal and selection | Agentic proposer over code, scores, and traces | Observability-driven loop; edits paired with verified predictions | Evolves harness during test time, no gold labels | Modular typed primitives, trace-driven adaptation |
> | **Model weights** | Frozen | Frozen | Frozen | Frozen | Frozen |
> | **Cost rule and pruning** | Yes | No* | No* | No* | No* |
> | **Harvey LAB evolve score** | 90.5 | 93.0 | 90.7 | 91.1 | 91.8 |
> | **OOD average ($H_0 = 39.7$)** | **43.6** | 40.6 | 39.2 | 38.0 | 39.7 |

*\*数据来源于 RRSI 研究团队。OOD 平均分代表 JobBench、GDPval 与 APEX-Agents 三大基准测试得分的算术平均值。*

> *\*Per the RRSI research team. OOD average represents the mean of JobBench, GDPval, and APEX-Agents.*

---

## 快速上手

> ## Getting Started

想要在本地上手并运行 RRSI，只需克隆官方代码仓库并执行基线运行命令：

> To get up and running with RRSI, clone the repository and run the baseline commands:

```bash
git clone https://github.com/google-research/rrsi.git && cd rrsi
pip install -e ".[dev]"
python3 rrsi.py --domain coding baseline
python3 rrsi.py --domain coding run
```

在每一轮进化过程中，系统会在相互隔离的 Git 工作树 (Git worktrees) 中起草两个候选改进方案，经过严格筛选与全面评测后，将代码分支快速推进 (fast-forward) 合并至胜出方案。

> Each round drafts two candidates in separate Git worktrees, screens them, evaluates both, and fast-forwards the branch to the winning candidate. 

---

## 核心要点总结

> ## Key Takeaways

* **冻结权重，敏捷进化 (Frozen Weights, Flexible Harness)**：在保持底层基础模型权重完全冻结的前提下，RRSI 专注于重写并自主优化外围提示词、工具调用、记忆模块以及业务工作流。
* **受控演进，杜绝过拟合 (Controlled Evolution)**：深度集成了防泄漏审查器、噪声波动门槛、推理成本规则以及冗余剪枝机制，多管齐下严格管控每次保留的代码改动。
* **实证泛化，打破孤岛 (Proven Generalization)**：在涵盖 Terminal-Bench 2.1 与 SWE-bench Verified 在内的主流编程与智能体评测基准上取得显著进步，同时彻底规避了对特定进化集的死记硬背。
* **全面开源，开放共建 (Open Source)**：该框架已在 [GitHub](https://github.com/google-research/rrsi) 正式开源，采用友好的 Apache 2.0 许可证。

> * **Frozen Weights, Flexible Harness:** RRSI evolves prompts, tools, memory, and workflows while keeping the underlying model weights untouched.
> * **Controlled Evolution:** Integrates a leakage critic, noise floor, cost rules, and pruning mechanisms to govern which edits are retained.
> * **Proven Generalization:** Noticeable performance improvements across major coding and agentic benchmarks (such as Terminal-Bench 2.1 and SWE-bench Verified) without overfitting to evolution sets.
> * **Open Source:** Available via [GitHub](https://github.com/google-research/rrsi) under the Apache 2.0 license.

---

*欲了解更多技术细节与实验数据，请查阅官方 [研究论文](https://arxiv.org/pdf/2609.24972)、[GitHub 仓库](https://github.com/google-research/rrsi) 以及 [项目主页](https://regularized-rsi.com/)。*

> *For more details, check out the official [Research Paper](https://arxiv.org/pdf/2609.24972), [GitHub Repository](https://github.com/google-research/rrsi), and [Project Website](https://regularized-rsi.com/).*
