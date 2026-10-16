---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-10-17
hide:
  - navigation
tags:
  - Claude Code
  - 代码审查
  - AI 编程
  - 研发效能
  - 自动化验证
title: "Claude Code 团队如何进行代码审查：应对 AI 生成代码爆发式增长"
---

# Claude Code 团队如何进行代码审查

> # How the Claude Code team does code review

**作者：** Addy Osmani, Morgan Westlee Lunt, Qing Wang  
**发布时间：** 2026 年 10 月 15 日 | **阅读时长：** 14 分钟  
**分类：** 工程架构 (Engineering)  

> **Authors:** Addy Osmani, Morgan Westlee Lunt, and Qing Wang  
> **Published:** Oct 15, 2026 | **Reading Time:** 14 min  
> **Category:** Engineering  

---

### 文章背景与核心概要

随着 AI 智能体 (AI Agent) 编写了 Claude Code 自身约 90% 的代码库，代码变更与合并请求 (Pull Request, PR) 的数量迎来了爆发式增长。传统的逐行人工代码审查 (Code Review) 迅速沦为研发效能的最大瓶颈，Anthropic 的 Claude Code 团队为此彻底重构了审查流程。他们通过将常规代码阅读交给自动化机器、引入多层 AI 交叉验证、推行基于风险的分级人工审批、以及严格执行收敛指标，成功在合并请求数量翻倍的同时将代码回滚率降低了 40% 以上。本文将全面拆解这套在 AI 编程时代兼顾极速迭代与极致质量防御的工程实践。

---

## 内容总结

> ## Summary

如今，AI 智能体编写了 Claude Code 自身大约 90% 的代码，这导致需要审查的代码量迎来了爆发式增长。Claude Code 团队没有继续依赖传统低效的人工逐行审查瓶颈，而是转向了一套经过专项优化的全新体系：**在不增加代码回滚 (Reverts) 或线上事故的前提下，将人工审查时间降至最低**。

> With AI agents writing roughly 90% of Claude Code's own codebase, code review volumes have surged dramatically. Rather than relying on traditional manual, line-by-line bottlenecks, the Claude Code team shifted toward a system optimized for **minimal human review time without increasing reverts or incidents**. 

通过将常规的代码阅读工作移交给自动化机器、建立多层 AI 验证机制、采用基于风险分级的人工审批流程，并强制执行严格的收敛指标，该团队成功让合并的代码请求翻了一倍，同时将代码回滚率降低了 40% 以上。本指南详细阐述了他们如何安全且高效地管理由智能体生成的海量代码。

> By moving routine reading to automated machines, instituting multi-layered AI verification, utilizing risk-based human approvals, and enforcing strict convergence metrics, the team doubled merged pull requests while reducing reverts by over 40%. This guide outlines how they manage high-volume, agent-generated code safely and effectively.

---

## 重新审视代码审查的初衷

> ## Rethinking the Purpose of Code Review

当智能体全面接管代码编写后，代码变更的数量便开始极速膨胀。在 Anthropic 的单体代码仓库 (Monorepo) 中，每天合入的代码变更从 5 月份的约 2,500 次猛增至 9 月份的超过 30,000 次。传统的人工代码审查方式根本无法跟上这种爆发式的研发节奏。

> When agents write code, change volume escalates rapidly. Across Anthropic's monorepo, daily landing changes jumped from roughly 2,500 in May to over 30,000 in September. Traditional, manual code review cannot keep pace with this velocity.

在传统的软件工程理念中，代码审查主要承担着两大职责：

1. 在代码发布上线之前，发现并修复潜在的问题与漏洞；
2. 在团队成员之间建立共享的业务上下文，加深对代码库整体架构的理解。

> Code review traditionally serves two purposes:
> 1. Finding and fixing issues before they ship.
> 2. Building shared context and codebase understanding across the team.

团队指出，纠结于*“是否有工程师逐行读过这段代码？”*实际上是一个不够精确的替代问题，真正核心的问题应当是：*“这次代码变更可能会引发哪些潜在故障？又该由哪种检查机制——无论是自动化工具还是人工介入——来最准确地捕获它？”*

> The team argues that asking *"Did a human read the code?"* is an imprecise proxy for *"What could go wrong with this change, and which check—automated or human—is the right one to catch it?"* 

现在的代码审查不再是研发流程末端的一道死卡死守的“终点关卡”，而是像实时拼写检查工具一样在编码过程中持续运行。在任何人类工程师审阅之前，绝大多数代码变更都已经被 Claude 自动审查并修复过至少一轮。

> Rather than functioning as a final gate at the end of the road, review now runs continuously like a live spellcheck. Most changes are reviewed and fixed by Claude at least once before a human ever looks at them.

---

## 真正稀缺的资源：人类工程师的时间与精力

> ## The Scarce Resource: Human Time and Attention

工程师的时间与专注力始终是研发流程中最核心的终极瓶颈。这不仅包括审阅代码所消耗的时间，还涵盖了由于劣质代码引入故障后、排查并修复线上问题所花费的精力——毕竟，如果在审查阶段省下了时间，却导致后续调试排障时间呈指数级激增，那完全是得不偿失的。

> Human time is the ultimate bottleneck. This encompasses both the time spent reviewing and the time spent fixing what bad code breaks (saving time on review is pointless if it exponentially increases debugging later). 

该团队衡量成功的核心指标非常明确：**绝大多数合并请求在最多只需一名工程师介入 (该工程师甚至可以是代码作者本人) 的情况下完成合并，同时代码回滚次数和线上事故率不发生任何增长。**

> The core metric for success: **Most pull requests merge with at most one human in the loop (who can be the author), with no increase in reverts or incidents.** 

---

## 代码变更的生命周期与分层防御架构

> ## The Life of a Change & Layer-by-Layer Architecture

一项典型的代码变更在最终推送至用户面前之前，会依次穿过六个由自动化流水线与人工协同把关的防御检查点：

> A typical change travels through six distinct, automated and human checkpoints before reaching users:

```
[ 1. Work Verified ] ➔ [ 2. AI Review ] ➔ [ 3. Security Review ] ➔ [ 4. CI Checks ] ➔ [ 5. Human Approval ] ➔ [ 6. Merge Queue & Flags ] ➔ [ 7. Rollback ]
```

### 1. 在他人审阅前先行验证工作成果

> ### 1. The work is verified before anyone else looks

在正式提交合并请求之前，工程师会先为 Claude 提供可执行的验证工具 (如自动化测试、构建脚本或视觉比对工具) ，并要求其对输出结果进行校验。与此同时，多个独立的子智能体 (Subagents) 会在全新的上下文环境中对代码差异 (Diff) 进行预审。

> Before opening a PR, engineers provide Claude with executable verification tools (tests, builds, or visual comparisons) and demand output validation. Subagents review the diff with fresh context. 

* **`CLAUDE.md`**：为 Claude 提供技术栈规范、开发约定与核心目标的指导指南。
* **`REVIEW.md`**：由代码所有者编写，用于明确告知审查者当前代码库中哪些特定故障模式至关重要。

> * **`CLAUDE.md`**: Directs Claude on the stack, conventions, and goals.
> * **`REVIEW.md`**: Written by code owners to inform reviewers what specific failures matter in their repo.

### 2. 对每个合并请求执行 AI 自动审查

> ### 2. AI review on every pull request

每一个合并请求都会接受来自 Claude 的自动化代码审查。Claude 会结合整个代码仓库的全局背景以及该 PR 的设计意图来深入分析代码差异。所有发现的潜在缺陷在正式发布前，均需经过多个独立智能体的交叉二次验证，最后按照严重程度打上标签并排序，呈现为清晰的代码行内注释。

> Every PR receives an automated review from Claude, reading the diff against the entire repo and the PR's intent. Findings are multi-verified by separate agents before being posted as sorted, severity-tagged inline comments.

### 3. 具备一票否决权的安全审查

> ### 3. Security review that can block

安全体系拥有其专属的自动化检查链路。只要存在任何未解决的安全漏洞隐患或重大 Bug 审查意见，该合并请求就绝对无法合入主干。

> Security runs its own automated checks. PRs cannot merge if any security or bug review finding remains unresolved.

### 4. 具备拦截能力的自动化流水线检查

> ### 4. Automated checks that block

标准化的持续集成 (Continuous Integration, CI) 流水线——涵盖代码静态语法检查 (Linting) 、类型检查、多平台兼容性测试以及构建流程——必须全部亮起绿灯通过，代码才能进入人工评估阶段。

> Standard CI pipelines—linting, type checking, multi-platform tests, and builds—must pass before human evaluation.

### 5. 基于风险等级动态匹配的人工审批

> ### 5. Human approval, scaled by risk

团队根据代码变更的潜在风险动态调整人工审批门槛：

> Risk tiers dynamically govern human approval requirements:

| 风险等级 | 变更示例 | 人工审批要求 |
| :--- | :--- | :--- |
| **低风险 (Low)** | 文档调整、界面文案、纯内部功能、特性开关 (Feature Flag) 保护下的增量代码 | 只要自动化流水线全部通过，无需人工审批 |
| **中风险 (Medium)** | 普通产品功能变更、缓存逻辑、自动更新程序、系统提示词 (System Prompts) | 需 1 人审批 |
| **高风险 (High)** | 高危核心逻辑与预定义的敏感代码路径 | 需 2 人审批 |

> | Risk | Examples | Human Approvals |
> | :--- | :--- | :--- |
> | **Low** | Docs, copy, internal-only features, additive changes behind a flag | None required if automated checks pass |
> | **Medium** | Ordinary product changes, caching, auto-updater, system prompts | One person |
> | **High** | High-risk code and sensitive pre-defined paths | Two people |

### 6. 合并队列、特性开关与灰度渐进式发布

> ### 6. Merge queue, flags, and gradual release

所有代码变更在合入主分支前，都会在合并队列 (Merge Queue) 中重新与最新的 `main` 分支进行联合测试验证。新功能首先通过特性开关向 Anthropic 内部员工开启灰度测试，随后才会按阶梯推向外部用户 (先发布至预发通道 `latest`，验证稳定后再进入正式版通道 `stable`) 。

> Changes are re-tested against `main` in a merge queue. New features roll out behind flags to Anthropic employees first, followed by tiered public releases (`latest` before `stable`).

### 7. 敏捷监测与闪电回滚机制

> ### 7. Fast detection, fast rollback

一旦线上发生异常，借助特性开关可在数秒内迅速停用故障功能。团队每周轮换的值班工程师与事故复盘会议，会顺藤摸瓜将每一次线上异常精准回溯到漏检该缺陷的具体防御层级。

> Features can be disabled instantly via flags. Weekly on-call rotations and incident reviews trace failures back to the specific layer that missed them.

---

## 持续迭代：让 AI 审查者变得更加敏锐

> ## Making the Reviewer Better

为了防止审查质量劣化或模型漂移，团队将审查质量视作一个持续闭环的优化飞轮：

* **将历史事故沉淀为评估基准测试集 (Eval Set)**：将历史上曾经引发线上故障的合并请求收集整理成每日评估测试集，用以对 AI 审查模型的升级进行打分验证。
* **追踪审查噪音以消灭误报**：根据工程师对审查意见的真实反馈方式 (包括“已修复”、“驳回为误判”、“符合设计预期”或“无关紧要”) 对注释进行分类归档，以此不断过滤并削减误报率。
* **强制执行收敛机制**：为了避免智能体之间陷入无休止的“AI 审查 AI”死循环，团队制定了硬性规则：限制最大审查轮数 (最多 3 轮) 、仅对增量代码差异进行复审，并采用宏观缺陷分类而非琐碎的逐行挑刺。

> To prevent review degradation, the team treats quality as an ongoing optimization loop:
> * **Incidents as an Eval Set:** Past pull requests that caused incidents are collected into a daily evaluation set to score reviewer updates.
> * **Tracking Noise:** Comments are sorted by how humans responded (fixed, dismissed as wrong, intentional, or irrelevant) to prune false positives.
> * **Enforcing Convergence:** To stop endless agent-to-agent review loops, the team instituted round caps (maximum 3 rounds), diff-only re-reviews, and broad bug classification instead of line-by-line nitpicking.

---

## 关键阵地：人类工程师不可替代的决策领域

> ## Where Humans Stay in the Loop

人类工程师的宝贵专业经验被精准保留在机器难以胜任的高阶决策领域：

* **方向把关与需求范围界定**：决断某项功能是否从一开始就值得被开发构建。
* **高危逻辑审批**：严格把关计费系统、自动更新程序以及核心 CI 工作流的配置变更。
* **系统架构设计**：制定具备长远指导意义的架构设计范式，供后续开发依循。
* **审视客观运行凭据**：审查真实日志、自动化测试报告与运行截图，而非机械盲目地点头通过纯文本代码。
* **对最终交付结果负责**：无论代码由谁或何种工具编写，始终由具体的人类工程师对发布到线上的每一行代码承担最终责任。

> Human expertise is reserved for decisions machines handle poorly:
> * **Direction & Scope:** Deciding whether a feature should be built at all.
> * **Risky Code:** Approving billing, auto-updaters, and CI workflow updates.
> * **Architecture:** Setting long-term patterns for others to follow.
> * **Reading Evidence:** Reviewing logs, test outputs, and screenshots rather than blindly approving text.
> * **Owning Outcomes:** A human remains fully accountable for every piece of code shipped.

---

## 团队上下文的同步与认知共享

> ## Sharing Context Across the Team

过去，工程师们不得不强迫自己逐行阅读繁杂零碎的代码差异来建立心智模型；而现在，团队成员只需让 Claude 针对自己即将修改的代码模块，即时生成量身定制的技术解释文档或交互式架构可视化图表，即可快速掌握系统全貌。

> Instead of reading trivial diffs line-by-line to maintain mental models, team members ask Claude to generate custom explainers or interactive visualizations for the specific codebase modules they are about to modify.

---

## “谁合入代码，谁负责到底”

> ## "You Land It, You Own It"

代码的所有权与责任感依然保持去中心化并由全员共担：

* 每次变更保持小颗粒度，并借助特性开关与闪电回滚确保其完全可逆。
* 依托开放透明的 Slack 沟通频道，任何人都可以实时观测、审查或参与到讨论与改进中。
* 事故复盘始终聚焦于系统性机制的优化升级，绝不进行无意义的事后追责或甩锅。

> Ownership remains decentralized and shared:
> * Changes are kept small and completely reversible via flags and rollbacks.
> * Transparency is maintained via open Slack channels where anyone can observe, review, or contribute.
> * Post-incident reviews focus on systemic improvements rather than assigning blame.

---

## 工程落地：团队如何平滑引入这套审查流程

> ## How You Can Adopt This Process

希望在团队中引入高吞吐量 AI 代码审查流程的工程研发团队，可以按照以下步骤循序渐进地落地实施：

> Teams looking to adopt high-velocity AI code review can implement these steps progressively:

1. **提交 PR 之前**：建立详尽明确的 `CLAUDE.md` 与 `REVIEW.md` 规范指引文件；充分利用本地审查命令在提交前自我校验。
2. **针对每一个 PR**：推行强制全面的 CI 自动化流水线，深度集成 AI 审查工具，筑牢自动化安全防线，并为审查轮数设立刚性上限。
3. **审批把关环节**：借助 CODEOWNERS 机制搭建客观公正的风险分级体系，同时严格确保机器人的自动化判定绝不僭越人类工程师的底线规则。
4. **合并与上线之后**：深度结合特性开关、合并队列与阶梯灰度放量机制，并将历史故障沉淀为基准测试集，从而对 AI 审查模型展开持续演化迭代。

> 1. **Before the PR:** Establish clear `CLAUDE.md` and `REVIEW.md` instruction files; utilize local review commands.
> 2. **On Every PR:** Require comprehensive CI, integrate an AI reviewer, enforce security checks, and cap review rounds.
> 3. **Approvals:** Set up objective, risk-based classification tiers via CODEOWNERS while ensuring bot approvals never override human requirements.
> 4. **Merge & Post-Merge:** Use feature flags, merge queues, staged rollouts, and incident-backed evaluation sets to continuously refine your review models.
