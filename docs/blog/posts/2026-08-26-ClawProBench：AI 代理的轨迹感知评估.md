---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- AI Agent
- 模型评估
- 轨迹感知
- 基准测试
- 运行时安全
title: ClawProBench：AI 代理的轨迹感知评估
---
### 文章背景与核心概要
当前的 AI 代理（AI Agent）基准测试往往只关注最终结果，而忽略了有状态运行时（stateful runtimes）的复杂性。为了解决这一痛点，**ClawProBench** 引入了一种“轨迹感知”（trace-aware）的评估框架，旨在对代理及其运行时配置进行全面评估。

该基准测试通过使用 *OpenClaw*（一个配备了工作区工具如网页浏览、内存管理、任务调度等的实时代理运行时），根据执行轨迹、过程质量和效率来评估代理，而不仅仅看最终结果。研究表明，传统的仅关注最终答案的排行榜往往会掩盖“原生表面”的弱点、偶然成功以及特定的代理失效模式，而这些只有通过轨迹分析才能被发现。

---

# ClawProBench：AI 代理的轨迹感知评估

**作者：** YuanHang Xiao  
**日期：** 2026年8月23日  
**arXiv：** [2608.22510](https://arxiv.org/abs/2608.22510)

---

## 摘要 (Summary)

当前的 AI 代理基准测试往往只关注最终结果，而忽略了有状态运行时的复杂性。**ClawProBench** 引入了一种“轨迹感知”的评估框架，旨在评估整个“代理 + 运行时”的配置。通过利用 *OpenClaw*（一个配备了工作区工具如浏览、内存、调度等的实时代理运行时），该基准测试根据执行轨迹、过程质量和效率来评估代理，而不仅仅是最终结果。

> Current AI agent benchmarks often focus exclusively on final outcomes, failing to account for the complexities of stateful runtimes. **ClawProBench** introduces a "trace-aware" evaluation framework designed to assess the entire agent-plus-runtime configuration. By utilizing *OpenClaw*—a live agent runtime equipped with workspace tools (browsing, memory, scheduling, etc.)—the benchmark evaluates agents based on execution traces, process quality, and efficiency rather than just the final result.

---

## 核心特性 (Key Features)

*   **轨迹感知评估：** 超越了最终答案指标，用于分析证据获取、运行时路由和安全边界中的失效模式。
*   **双轨基准测试：**
    *   **完整画像（102 个场景）：** 具备实时工作区和原生运行时路由任务。
    *   **冻结保留集（68 个场景）：** 使用封闭世界的 JSON 输出契约，以实现稳健、标准化的排名。
*   **安全门控评分：** 采用结合了正确性、过程质量和效率的公式，同时保留失效证据以供审计。

> *   **Trace-Aware Evaluation:** Moves beyond final-answer metrics to analyze failure modes in evidence acquisition, runtime routing, and safety boundaries.
> *   **Dual-Track Benchmarking:**
>     *   **Full Profile (102 scenarios):** Features a live workspace and native-runtime routing tasks.
>     *   **Frozen Holdout (68 scenarios):** Uses closed-world JSON output contracts for robust, standardized ranking.
> *   **Safety-Gated Scoring:** Employs a formula that combines correctness, process quality, and efficiency, while preserving failure evidence for auditing.

---

## 研究洞察 (Research Insights)

*   **性能差距：** 原生运行时任务的表现持续低于工作区实时任务（0.5238 对比 0.6415）。
*   **排名差异：** 完整画像与保留集排名之间的关联性较弱（斯皮尔曼相关系数为 0.1300）。
*   **指标敏感性：** 研究表明，仅基于正确性的排名与使用过程感知或安全门控指标的排名存在显著差异。
*   **结论：** 传统的最终答案排行榜往往掩盖了“原生表面”的弱点、偶然成功以及只有通过轨迹分析才能可见的具体代理失效模式。

> *   **Performance Gap:** Native-runtime tasks consistently underperform compared to workspace-live tasks (0.5238 vs. 0.6415).
> *   **Ranking Discrepancies:** There is weak alignment (Spearman 0.1300) between full-profile and holdout rankings.
> *   **Metric Sensitivity:** The study demonstrates that rankings based solely on correctness differ significantly from those using process-aware or safety-gated metrics.
> *   **Conclusion:** Traditional final-answer leaderboards often obscure "native-surface" weaknesses, one-off successes, and specific agent failure modes that are only visible through trace analysis.

---

## 访问与资源 (Access & Resources)

*   **[查看 PDF](https://arxiv.org/pdf/2608.22510)**
*   **[HTML（实验性）](https://arxiv.org/html/2608.22510v1)**
*   **[TeX 源码](https://arxiv.org/src/2608.22510)**

*注：匿名工件包括基准定义、评分代码、清单和经过脱敏处理的轨迹。*

> *   **[View PDF](https://arxiv.org/pdf/2608.22510)**
> *   **[HTML (Experimental)](https://arxiv.org/html/2608.22510v1)**
> *   **[TeX Source](https://arxiv.org/src/2608.22510)**
> 
> *Note: The anonymous artifact includes benchmark definitions, scoring code, manifests, and sanitized traces.*