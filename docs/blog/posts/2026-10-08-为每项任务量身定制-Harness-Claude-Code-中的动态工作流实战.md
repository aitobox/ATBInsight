---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-10-08
hide:
  - navigation
tags:
  - Claude Code
  - Dynamic Workflows
  - Harness 架构
  - 多智能体
  - Subagents
  - 自动化工作流
  - 工具教程
title: "为每项任务量身定制 Harness：Claude Code 中的动态工作流实战"
---

# 为每项任务量身定制 Harness：Claude Code 中的动态工作流实战

> # A harness for every task: dynamic workflows in Claude Code

### 文章背景与核心概要

随着大语言模型 (Large Language Model, LLM) 在软件工程与复杂研发任务中的深度应用，传统的单一上下文窗口已逐渐暴露出诸如智能体倦怠 (Agentic Laziness)、自我偏好偏差 (Self-preferential Bias) 以及目标漂移 (Goal Drift) 等固有限制。针对这一核心工程瓶颈，Anthropic 在 Claude Code 中正式推出了动态工作流 (Dynamic Workflows) 功能，赋予 Claude 在运行时动态编写并编排专属多智能体 Harness (运行架构基座) 的强大能力。该机制允许 Claude 根据当前任务即时生成轻量级 JavaScript 工作流脚本，通过精确派生子智能体 (Subagents) 并配置独立工作树 (Worktree) 与差异化模型，高效处理深度调研、自动化安全审计、大规模架构重构及锦标赛排序等高价值复杂场景。本文系统解析了动态工作流的技术实现原理、六大经典编排模式与工程实战技巧，为开发者构建高可靠性、规模化自主执行的工程智能体系统提供了全面指引。

---

**核心摘要：** Claude Code 现已正式支持**动态工作流 (Dynamic Workflows)**，允许 Claude 在运行时自主编写并编排专属于当前任务的多智能体 Harness (运行架构基座)。尽管默认的 Harness 专为常规编程任务打造，但动态工作流使 Claude 能够通过创建具有专属角色的隔离子智能体 (Subagents)，原生解决深度调研 (Deep Research)、自动化安全审查以及大规模代码重构等复杂且高价值的任务。虽然这些工作流会消耗更多 Token，但它们有效克服了单一上下文所固有的局限性，例如智能体倦怠 (Agentic Laziness)、自我偏好偏差 (Self-preferential Bias) 以及目标漂移 (Goal Drift)。

> **Summary:** Claude Code now supports **dynamic workflows**, allowing Claude to write and orchestrate its own multi-agent harness on the fly. While default harnesses are designed for coding, dynamic workflows enable Claude to natively solve complex, high-value tasks—such as deep research, automated security reviews, and large-scale refactoring—by spinning up isolated subagents with specialized roles. Although they consume more tokens, these workflows overcome single-context limitations like agentic laziness, self-preferential bias, and goal drift.

---

## 作者与发布信息

> ## Author & Publication

* **作者：** Thariq Shihipar 与 Sid Bidasaria
* **发布日期：** 2026 年 6 月 2 日
* **预计阅读时间：** 11 分钟
* **所属分类：** Agents

> * **Authors:** Thariq Shihipar and Sid Bidasaria
> * **Published:** June 02, 2026
> * **Reading Time:** 11 minutes
> * **Category:** Agents

---

上周，Anthropic 正式在 Claude Code 中推出了[动态工作流 (Dynamic Workflows)](https://code.claude.com/docs/en/workflows)。现在，Claude 能够在运行时根据手头的具体任务，即时编写并构建专属于该任务的定制化 [Harness (运行架构基座)](https://code.claude.com/docs/en/glossary#agentic-harness)。

> Last week, Anthropic released [dynamic workflows](https://code.claude.com/docs/en/workflows) in Claude Code. Claude can now write its own [harness](https://code.claude.com/docs/en/glossary#agentic-harness) on the fly, custom-built for the task at hand.

虽然 Claude Code 默认的 Harness 基座主要是针对编码场景设计的，但由于许多任务在结构上都与编程类似，它同样适用于其他广泛的场景。然而，某些特定类型的任务若想发挥出极致性能，必须依赖构建在 Claude Code 之上的定制 Harness，例如[调研探索 (Research)](https://support.claude.com/en/articles/11088861-using-research-on-claude)、[安全分析 (Security Analysis)](https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code)、[智能体团队协作 (Agent Teams)](https://code.claude.com/docs/en/agent-teams) 或是[代码审查 (Code Review)](https://code.claude.com/docs/en/code-review)。

> While the default Claude Code harness is built for coding, it is also useful for many other types of tasks because many tasks resemble coding tasks. However, certain classes of tasks require custom harnesses built on top of Claude Code to achieve peak performance, such as [Research](https://support.claude.com/en/articles/11088861-using-research-on-claude), [security analysis](https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code), [agent teams](https://code.claude.com/docs/en/agent-teams), or [Code Review](https://code.claude.com/docs/en/code-review).

借助动态工作流，你可以基于 Claude Code 动态创建运行基座，从而使 Claude 能够更加原生且游刃有余地解决所有此类问题。此外，你还可以将这些工作流共享给其他开发者重复使用。

> Workflows allow you to dynamically create harnesses built on top of Claude Code that enable Claude to solve all of those problems more natively. You can also share and reuse these workflows with others.

> 💬 [原文引用 / Original Quote]:
> **提示：** 相关最佳实践仍在不断演进之中。动态工作流通常会消耗更多 Token，最适合用于处理复杂且高价值的攻坚任务。
> 
> **Note:** Best practices are still developing. Dynamic workflows often use more tokens and are best suited for complex, high-value tasks.

---

## 提示词实战范例

> ## Example Prompts

在深入探讨底层技术细节之前，我们先通过几个精选的提示词 (Prompt) 范例，直观感受一下工作流所能开启的广阔可能性：

> Before diving into the technical details, here are several example prompts to get you thinking about the possibilities with workflows:

* *“这个测试大约每跑 50 次就会偶发失败 1 次。请设置一个工作流来稳定复现它。提出多个相互竞争的竞态条件 (Race Condition) 假说，并持续验证，直到只剩下唯一能够经受住证据检验的假说为止。”*
* *“请使用工作流梳理我最近的 50 次会话记录，从中挖掘我反复指出的纠错内容，并将高频出现的问题提炼转化为 `CLAUDE.md` 规则规范。”*
* *“请使用工作流深挖过去 6 个月 Slack 中 #incidents 频道的历史记录，找出那些频频出现却至今无人为其创建工单的根本故障原因。”*
* *“获取我的商业计划书并运行一个工作流，让不同的智能体分别站在投资人、客户以及竞争对手的角度对其进行全面挑刺和极限施压。”*
* *“这里有一个包含 80 份简历的文件夹，请利用工作流针对后端开发岗位进行排序筛选，并对排名前十的候选人进行复核。在此之前，请使用 AskUserQuestion 工具向我提问，以确定评估标准。”*
* *“我需要为这个 CLI 工具起个好名字。请使用工作流进行头脑风暴构思一批方案，并通过锦标赛对决机制筛选出排名前三的最佳选项。”*
* *“请使用工作流在整个项目代码库中，将所有的 User 模型全局重命名为 Account。”*
* *“请使用工作流逐一审核我的博客草稿，将文中的每一项技术声明与代码库实际实现进行严密比对核实，确保发布的文章不存在任何事实错误。”*

> * *"This test fails maybe 1 in 50 runs. Set up a workflow to reproduce it. Form competing theories about the race, and don't stop until one theory survives the evidence."*
> * *"Using a workflow, go through my last 50 sessions and mine them for corrections I keep making and turn the recurring ones into `CLAUDE.md` rules."*
> * *“Use a workflow to dig through #incidents in Slack for the past six months and find recurring root causes where nobody has filed a ticket.”*
> * *"Take my business plan and run a workflow where different agents tear it apart from an investor's, a customer's, and a competitor's perspective."*
> * *"Here's a folder of 80 resumes, use a workflow to rank them for the backend role and double-check the top ten. Interview me using the AskUserQuestion tool for a rubric."*
> * *"I need a name for this CLI tool. Use a workflow to brainstorm a bunch of options and run a tournament to pick the top 3."*
> * *"Use a workflow to rename our User model to Account everywhere."*
> * *“Go through my blog post draft and verify every technical claim against the codebase using a workflow, I don't want to ship anything wrong.”*

---

## 动态工作流的工作原理

> ## How Dynamic Workflows Work

动态工作流本质上是执行一个轻量的 JavaScript 文件，其中包含几个专门用于派生和协调[子智能体 (Subagents)](https://code.claude.com/docs/en/sub-agents) 的特殊函数：

> Dynamic workflows execute a JavaScript file with a few special functions that help spawn and coordinate [subagents](https://code.claude.com/docs/en/sub-agents):

<figure class="art-fig"><img alt="The agent(prompt, opts) function with its options annotated: prompt is the only required input, schema returns validated JSON, model picks opus, sonnet or haiku, isolation is worktree or remote, agentType selects a subagent. Below it, parallel() fans out and waits for all; pipeline() streams each item through every stage." class="fg" decoding="async" height="1216" loading="lazy" src="/media/405c8b387ec2cc574e6d48edba5431e02e23e4fca7c31d51184fc9738eaef70b.png" style="display:block;width:100%;aspect-ratio:1760 / 1216" width="1760"/><figcaption class="cap"><b>图 A</b><span>工作流脚本的三大基石：agent() 派生单个子智能体；parallel() 与 pipeline() 组合编排多个子智能体。</span></figcaption></figure>

动态工作流中还内置了 `JSON`、`Math` 和 `Array` 等标准 JavaScript 全局对象，以帮助开发者灵活处理和转换数据。

> Dynamic workflows also include standard JavaScript functions like `JSON`, `Math`, and `Array` to help process data.

尤为值得注意的是，动态工作流能够自主决定各个智能体具体调用哪种模型，以及子智能体是否在独立的 Git 工作树 (Worktree) 中运行，从而赋予了 Claude 根据实际需要灵活选择智力水平与隔离等级的自由。

> It is particularly useful to know that dynamic workflows can decide which models an agent uses and whether subagents are run in their own worktree, allowing Claude to choose the intelligence level and isolation needed.

如果不幸遭遇工作流意外中断——例如用户手动终止或退出终端——当恢复会话时，工作流能够智能识别断点，并从此前中断的地方继续无缝执行。

> If a workflow is interrupted—for example, by user action or quitting the terminal—resuming the session will allow the workflow to pick up where it left off.

---

## 为什么需要动态工作流？

> ## Why Dynamic Workflows?

当你要求 Claude Code 默认的 Harness 基座执行一项任务时，它必须在同一个上下文窗口 (Context Window) 内同时承担规划与执行双重职责。对于许多常规编程任务而言，这种单打独斗的模式非常高效；但当面对耗时漫长、大规模并行、高度结构化或对抗性极强的复杂任务时，该模式就很容易出现破绽甚至彻底崩溃。

> When you ask the default Claude Code harness to do a task, it needs to both plan and execute in the same context window. For many coding tasks, this is highly effective, but it can break down over long-running, massively parallel, highly structured, and/or adversarial tasks.

随着 Claude 在单一上下文窗口中处理复杂任务的时间不断延长，它会越来越容易陷入以下几类典型的失效模式：

> The longer Claude works on a complex task in a single context window, the more susceptible it becomes to specific failure modes:

* **智能体倦怠 (Agentic Laziness)：** 在处理复杂的长链路多步骤任务时，Claude 往往尚未完全收尾便提前罢工，在仅完成部分进度后就匆匆宣称任务已结束 (例如在 50 项安全审查清单中仅处理了 35 项便草草交差) 。
* **自我偏好偏差 (Self-preferential Bias)：** Claude 倾向于过度信任并偏袒自己先前得出的结论或输出成果，尤其在被要求对照既定标准对其自我审查或打分评判时，往往难以保持客观中立。
* **目标漂移 (Goal Drift)：** 经历多轮交互之后，模型对初始目标的理解与忠实度会逐步退化，在上下文被浓缩压缩 (Compaction) 之后尤为严重。每一次对话摘要过程都是有损的，边缘案例的具体要求或严格限制条件很容易在这一过程中遗失殆尽。

> * **Agentic laziness:** Claude stops before finishing a particularly complex, multi-part task and declares the job done after partial progress (e.g., addressing 35 of the 50 items in a security review).
> * **Self-preferential bias:** Claude tends to prefer its own results or findings, especially when asked to verify or judge them against a rubric.
> * **Goal drift:** A gradual loss of fidelity to the original objective across many turns, especially after compaction. Each summarization step is lossy, and details like edge-case requirements or constraints can get lost.

而构建工作流则能从根本上攻克这些顽疾：它通过统筹编排多个独立的 Claude 子智能体，为每个子智能体分配干净纯粹的上下文窗口以及高度聚焦、相互隔离的任务目标。

> Creating a workflow helps combat these issues by orchestrating separate Claude subagents with their own context windows and focused, isolated goals.

---

## 动态工作流与静态工作流的对比

> ## Dynamic vs. Static Workflows

此前，你可能曾借助 Claude Agent SDK 或通过 `claude -p` 命令行参数构建过静态工作流，用以协调编排多个 Claude Code 实例协同工作。

> You may have previously created a static workflow using the Claude Agent SDK or `claude -p` to coordinate multiple instances of Claude Code together.

然而，由于静态工作流必须预先兼顾所有可能的边界情况，其逻辑往往显得泛化而呆板。而在 [Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) 与动态工作流的强强联合下，Claude 如今已具备充沛的工程智慧，能够直接针对你当前面临的具体问题，现场量身定制最契合的专属运行基座。

> However, because static workflows need to work for all edge cases, they are usually more generic. With [Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) and dynamic workflows, Claude is now intelligent enough to write a custom harness tailor-made for your specific use case.

<figure class="art-fig"><img alt="The question “Should we migrate our checkout service to a new provider?” handled two ways. A static harness runs five web searches, fetches results, verifies and summarizes into a generic research report. A dynamic workflow reads the billing code, checks each feature against the new provider’s docs, prices it at real transaction volume, runs a devil’s advocate, and ends in a specific recommendation." class="fg" decoding="async" height="915" loading="lazy" src="/media/fb7abff3846443de3b59b23208f0019bad6eb2555e5dd945594438ce4ee143c1.png" style="display:block;width:100%;aspect-ratio:1999 / 915" width="1999"/><figcaption class="cap"><b>图 B</b><span>静态 Harness 对所有问题千篇一律地运行相同步骤；而动态工作流则因地制宜，紧扣眼前的具体场景量身定制。</span></figcaption></figure>

---

## 动态工作流的实用设计模式

> ## Helpful Patterns When Using Dynamic Workflows

你只需直接要求 Claude 构建一个工作流，或者在提示词中使用触发关键词 `ultracode`，即可确保 Claude Code 主动创建并调用动态工作流。

> You can start using dynamic workflows just by asking Claude to make one, or by using the trigger word `ultracode` to ensure Claude Code creates a workflow.

为动态工作流的运行机制建立清晰的心智模型，有助于你准确判断何时该使用它们，并善用以下几种经典且可自由组合的模式在提示词中引导 Claude：

> Building a mental model for how dynamic workflows operate helps you understand when to use them and how to nudge Claude via prompts using these common composable patterns:

<figure class="art-fig"><img alt="Six workflow patterns as small diagrams: classify-and-act, fanout-and-synthesize, adversarial verification, generate-and-filter, tournament, and loop until done." class="fg" decoding="async" height="1112" loading="lazy" src="/media/0a60d2d8c1dbddc23694ead5848908e1f2c9ef9e57ed0fbdbf53a0dc11e9ed16.png" style="display:block;width:100%;aspect-ratio:1999 / 1112" width="1999"/><figcaption class="cap"><b>图 C</b><span>Claude 赖以灵活组合的六种核心工作流设计模式。</span></figcaption></figure>

### 模式一：分类与执行 (Classify-and-Act)

> ### Classify-and-Act

通过分类器智能体判定任务类型，进而将任务精准路由分发至不同的专用智能体或行为逻辑中。此外，也可以在工作流末端部署分类器来最终判定交付成果的格式或走向。

> Use a classifier agent to decide on the task type, then route to different agents or behaviors. A classifier can also be used at the end to determine the output.

### 模式二：扇出与聚合 (Fan-Out-and-Synthesize)

> ### Fan-Out-and-Synthesize

将一项大任务拆解为众多细分的小步骤，针对每个步骤分别运行一个独立的智能体，最后将各方结果融会贯通予以聚合。当子步骤数量庞大，或者每个步骤都需要一个干净纯粹的上下文窗口时，这种模式格外高效。其中的聚合步骤充当了同步屏障 (Barrier) 的角色，等待所有并发扇出的智能体执行完毕后，统一融合它们输出的结构化数据。

> Split a task into many smaller steps, run an agent on each step, and then synthesize the results. This is useful for large numbers of smaller steps or when each step benefits from a clean context window. The synthesis step acts as a barrier, waiting for all fan-out agents before merging their structured outputs.

### 模式三：对抗性校验 (Adversarial Verification)

> ### Adversarial Verification

针对派生出的每一个智能体，为其额外配置一个专门唱反调的对抗验证智能体，依据严格的标准规范或评估指标对其输出结果进行极限挑刺与校验核查。

> For each spawned agent, run a separate agent to adversarially verify its output against a rubric or set of criteria.

### 模式四：生成与筛选 (Generate-and-Filter)

> ### Generate-and-Filter

围绕特定主题发散生成海量候选方案，随后利用既定评估准则或验证步骤进行过滤筛选、数据去重，最终仅筛选输出质量最高、经过严格检验的优质方案。

> Generate multiple ideas on a topic, filter them using a rubric or verification step, deduplicate, and return only the highest-quality, tested ideas.

### 模式五：锦标赛对决 (Tournament)

> ### Tournament

与其按部就班地拆分任务，不如让智能体们展开擂台竞争。同时派生出 $N$ 个智能体，让它们采用不同的思路或架构尝试解决同一项任务，随后由裁判智能体对各方成果进行两两成对 (Pairwise) 的残酷比对评判，层层淘汰直至最终冠军脱颖而出。

> Instead of dividing the work, have agents compete on it. Spawn $N$ agents attempting the same task using different approaches, then judge the results pairwise via a judging agent until a winner emerges.

### 模式六：循环直至达标 (Loop Until Done)

> ### Loop Until Done

面对工作总量预先未知或不可预测的任务，不再采用固定的轮次限制，而是循环派生智能体持续推进，直到满足终止条件为止 (例如不再有新的问题被发现，或者日志中再无任何报错信息) 。

> For tasks with an unknown volume of work, loop spawning agents until a stop condition is met (e.g., no new findings or no further errors in logs) instead of running a fixed number of passes.

---

## 典型实战应用场景

> ## Use Cases

工作流在非技术任务中的价值往往更为惊艳。不妨考虑将其应用在以下几个重点领域：

> Workflows are frequently even more useful for non-technical tasks. Consider applying them in the following areas:

### 迁移与重构工程 (Migrations and Refactors)

> ### Migrations and Refactors

[Bun](https://bun.com/) 正是借助工作流完成了从 Zig 向 Rust 的底层重写 (可参阅 [Jarred 的推文讨论](https://x.com/jarredsumner/status/2060050578026189172) 或深入了解 [AI 代码迁移实践](https://claude.com/blog/ai-code-migration)) 。将庞大的迁移任务逐层拆解为时序步骤 (API 调用、未通过的测试、独立模块) 。针对每一处修复，在独立工作树 (Worktree) 中派生一个子智能体处理，安排另一名智能体进行严格的对抗审查，通过后再执行代码合并。

> [Bun](https://bun.com/) was rewritten from Zig to Rust using workflows (read [Jarred’s thread](https://x.com/jarredsumner/status/2060050578026189172) or learn about [AI code migrations](https://claude.com/blog/ai-code-migration)). Break down tasks into sequential steps (calls, failing tests, modules). Spin off a subagent for every fix in a worktree, have another agent adversarially review it, and then merge.

### 深度调研探索 (Deep Research)

> ### Deep Research

Claude Code 内部的深度调研技能 (`/deep-research`) 正是依托动态工作流实现的：它并发扇出执行海量网页检索、抓取一手信源、以对抗姿态核验论点真伪，并最终合成出附带严谨引用的研究报告。

> Claude Code's internal deep research skill (`/deep-research`) uses dynamic workflows to fan-out web searches, fetch sources, verify claims adversarially, and synthesize cited reports.

### 深度核验比对 (Deep Verification)

> ### Deep Verification

<figure class="art-fig"><img alt="A report flows into a claim extractor, which fans out to claim checkers 1 through N, each optionally followed by a source auditor, converging into a verified report." class="fg" decoding="async" height="800" loading="lazy" src="/media/14981a07d95b7a4f10f6e995e34ea589c6a87836a753f3ffd70047363adb34dd.png" style="display:block;width:100%;aspect-ratio:1999 / 800" width="1999"/><figcaption class="cap"><b>图 D</b><span>深度核验架构：每个事实性论点均由专属校验智能体核对，其背后还可按需配置信源审计员提供双重保障。</span></figcaption></figure>

为了严密核验并追溯报告中的每一项事实性陈述，可以构建这样一个工作流：由一个智能体负责从全文中精准提取论点，各子智能体逐一进行深度核对，并在后端由校验智能体进行严格把关，确保引用信源具有极高的权威性与可靠性。

> To check and source every factual claim in a report, use a workflow where one agent identifies claims and subagents check each in detail, backed by a verification agent ensuring high source quality.

### 大规模复杂排序 (Sorting)

> ### Sorting

<figure class="art-fig"><img alt="1,000 items enter a bracket: round one pairs items with a fresh agent per comparison, winners meet in round two, a last comparison decides the final, and the output is a sorted list." class="fg" decoding="async" height="708" loading="lazy" src="/media/be7b8dc2e6f8a2791efb3c4589fa182f0c90b380bb56d8b41a1f18fc7cb04394.png" style="display:block;width:100%;aspect-ratio:1999 / 708" width="1999"/><figcaption class="cap"><b>图 E</b><span>锦标赛排序模式：每次两两对比均启用一个崭新的智能体，无需让单一上下文窗口硬塞 1,000 个项目。</span></figcaption></figure>

当需要对大规模数据集 (例如 1,000 多行数据或客户支持工单) 进行排序时，采用锦标赛风格的两两对决流水线，远比试图在单个提示词中完成绝对打分更为精准有效。

> Sort large datasets (e.g., 1,000+ rows or support tickets) using a tournament style pipeline of pairwise comparisons rather than absolute scoring in a single prompt.

### 记忆与规则遵循 (Memory and Rule Adherence)

> ### Memory and Rule Adherence

<figure class="art-fig"><img alt="A diff of +142 and −87 lines is checked against five rules, one verifier agent per rule. Two rules flag lines 42 and 90; the rest come back clean. A skeptic agent re-reads each flag to separate real violations from false positives, leaving confirmed violations only." class="fg" decoding="async" height="786" loading="lazy" src="/media/fd6d2a8544c5541442fb2df1c24374ff8e2984274cc2bf796fe5e632bfcc400a.png" style="display:block;width:100%;aspect-ratio:1999 / 786" width="1999"/><figcaption class="cap"><b>图 F</b><span>逐条规则严审：在纯净上下文中为每条规则配备一个校验智能体，再由怀疑论者智能体过滤掉虚警标记。</span></figcaption></figure>

构建一个配备多名验证智能体的工作流——每名智能体专门盯防一条既定规范——从而严格把关硬性指标；同时引入具备“怀疑论者人设 (Skeptic Persona)”的子智能体，剔除误报杂音。或者，也可以挖掘最近的会话记录提取出高频规则，将经受住考验的最佳实践重新浓缩沉淀至 `CLAUDE.md` 规范文件中。

> Create a workflow with verifier agents—one per rule—to check strict criteria, utilizing a "skeptic persona" subagent to filter out false positives. Alternatively, mine recent sessions to extract rules and distill survivors back into a `CLAUDE.md`.

### 根本原因深度排查 (Root-Cause Investigation)

> ### Root-Cause Investigation

为了防止模型陷入自我偏好偏差，可以派生多个互不干扰的独立智能体，分别从互不重叠的隔离证据链 (例如分别审查日志、源文件以及测试数据) 出发各自独立提出假说，最后交由包含验证者与反驳者的专家评审团进行综合评议。

> Prevent self-preferential bias by spinning up agents to generate hypotheses from disjoint evidence (e.g., separate agents for logs, files, and data) evaluated by a panel of verifiers and refuters.

### 大规模工单与需求分流 (Triaging at Scale)

> ### Triaging at Scale

<figure class="art-fig"><img alt="An untrusted backlog of support tickets, bug reports and user feedback enters a quarantine zone with read-only tools, where reader agents classify each item, dedupe against what is already tracked, and emit a structured summary only. A trusted zone with high-privilege tools holds an actor agent that acts on summaries, attempting a fix and opening a PR if fixable, otherwise escalating to a human. /loop runs it continuously." class="fg" decoding="async" height="730" loading="lazy" src="/media/ebf352766b6bb484729e8a8c08f9a72f918b19f78d02e998fe3384fcf3fd88e3.png" style="display:block;width:100%;aspect-ratio:1999 / 730" width="1999"/><figcaption class="cap"><b>图 G</b><span>先隔离检疫，再落地执行：负责读取不可信外部内容的读取智能体没有任何危险特权；执行智能体则只接收过滤后的结构化摘要。</span></figcaption></figure>

利用**隔离检疫模式 (Quarantine Pattern)** 高效消化积压需求与工单：严禁负责查阅不可信公开内容的智能体调用任何高权限工具，只允许它们向拥有执行权限的智能体传递纯净的摘要数据。配合 `/loop` 轮询指令，即可实现全天候无间断持续运转。

> Process backlogs using a **quarantine pattern**: bar agents reading untrusted public content from taking high-privilege actions, passing only summaries to authorized actor agents. Pair with `/loop` for continuous execution.

### 审美探索、质量评估与模型路由 (Exploration and Taste, Evals, and Model Routing)

> ### Exploration and Taste, Evals, and Model Routing

* **审美探索 (Exploration)：** 针对设计选型或起名等高度依赖品味的非结构化任务，制定细化维度的评估量规，由审查智能体自主判定何时达到合格标准。
* **质量评估 (Evals)：** 在独立的工作树 (Worktree) 中派生专用智能体，根据严格制定的评测标准对生成产物进行全面评估与打分。
* **动态路由 (Routing)：** 部署分类器智能体先行调研当前任务的复杂程度，并在运行时动态将执行链路路由分发至 Sonnet 或 Opus 等不同量级的模型上。

> * **Exploration:** Use rubrics for taste-based tasks like design or naming, letting review agents decide when criteria are met.
> * **Evals:** Spin off separate agents in worktrees to evaluate and grade outputs against specific criteria.
> * **Routing:** Use a classifier agent to research the complexity of a task and dynamically route execution to Sonnet or Opus.

---

## 何时无需使用动态工作流？

> ## When NOT to Use Dynamic Workflows

工作流的能力固然极其强大，但它绝非放之四海而皆准的万能灵药，并且会显著消耗更多的 Token。常规且直截了当的日常编程任务，通常根本不需要兴师动众地组建一个庞大的审查委员会。正如同所有多智能体架构的通用铁律一样：并发度与专业分工带来的收益，必须能够完全覆盖其额外的协调调度成本。

> Workflows are powerful, but they are not needed for every task and consume significantly more tokens. Traditional coding tasks generally do not need an extensive panel of reviewers. As with general multi-agent architectures, parallelism and specialization must always earn their coordination cost.

---

## 构建动态工作流的实战秘诀

> ## Tips for Building Dynamic Workflows

* **提示词编写策略 (Prompting)：** 善用上文归纳的各种模式编写详实的提示词。你也可以灵活要求 Claude 执行“轻量级快速工作流” (例如对某个设计假说快速发起一轮对抗性审查) 。
* **搭配 `/goal` 与 `/loop` 组合拳：** 将可复现的工作流与 `/loop` 结合实现定时周期执行，或与 `/goal` 配合设定明确硬性的最终完成标准。
* **设定 Token 消耗预算 (Token Usage Budgets)：** 在提示词中通过类似 *“最多消耗 1 万 Token (use 10k tokens)”* 的明确限制，对 Token 消耗设置上限。
* **保存与分享动态工作流 (Saving and Sharing Dynamic Workflows)：** 在工作流菜单中按下 `s` 键即可保存当前工作流。它们通常存储在 `~/.claude/workflows` 目录下，或者可以通过技能 (Skills) 方式分发共享。

> * **Prompting:** Use detailed prompts leveraging the techniques outlined above. You can also request "quick workflows" (e.g., a quick adversarial review of an assumption).
> * **Combine with `/goal` and `/loop`:** Pair repeatable workflows with `/loop` for regular intervals and `/goal` for hard completion criteria.
> * **Token Usage Budgets:** Set explicit caps on token usage by prompting Claude with limits like *"use 10k tokens."*
> * **Saving and Sharing Dynamic Workflows:** Save workflows by pressing `s` in the workflow menu. Store them in `~/.claude/workflows` or distribute them via skills.

<figure class="art-fig"><img alt="The Dynamic workflows panel in Claude Code listing three runs with agent counts, token totals and durations: review-changes (14 agents, 482k tokens, 6m 12s), find-flaky-tests (6 agents, still running) and deep-research (22 agents, 1.1M tokens, 11m 3s). Footer keys: select, enter view, s save, esc close." class="fg" decoding="async" height="350" loading="lazy" src="/media/c8b4b65c4c43f1d01be880efd0851cdfc50e8bd9c8517a57d16a761ce7d0331a.png" style="display:block;width:100%;aspect-ratio:1278 / 350" width="1278"/><figcaption class="cap"><b>图 H</b><span>Claude Code 中的动态工作流控制面板——按下快捷键 s 即可将一次执行记录持久化保存为可复用的工作流。</span></figcaption></figure>

若希望通过技能 (Skill) 分享工作流，只需将 JavaScript 工作流文件放入对应的技能文件夹中，并在 `SKILL.md` 中将其引用为预置模板即可。

> To share via a skill, put your JavaScript workflow files in the skill folder and reference them in the `SKILL.md` as templates.

<figure class="art-fig"><img alt="A skill folder at ~/.claude/skills/deep-verify/ containing SKILL.md, verify-claims.workflow.js and rubric.md, beside the SKILL.md contents, which reference ./verify-claims.workflow.js to check each claim with its own subagent." class="fg" decoding="async" height="1016" loading="lazy" src="/media/d3d1c7dcf59433f5178c509e7510aad3d26c33ab53bddd712a244c00b37e1047.png" style="display:block;width:100%;aspect-ratio:1999 / 1016" width="1999"/></figure>

---

## 探索全新可能的新起点

> ## A New Starting Point for Discovery

动态工作流为拓展 Claude Code 的能力边界提供了一种极富想象力的新途径。不妨将其视作一个全新的探索起点，去发掘借助 Claude 高效达成任务目标的更多创新方式。

> Workflows are a helpful new way to extend Claude Code. Think of them as a starting point to explore new ways to use Claude to accomplish your tasks. 

*欲了解哪些能力理应率先纳入 Harness 基座的设计原则，请参阅三大 [Harness 设计模式 (Harness Design Patterns)](https://claude.com/blog/harnessing-claudes-intelligence)。*

> *For principles on what belongs in a harness in the first place, see the three [harness design patterns](https://claude.com/blog/harnessing-claudes-intelligence).*
