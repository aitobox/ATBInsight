---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- LLM智能体
- 推测解码
- 工具调用
- 延迟优化
- 强化学习
title: 用于加速工具使用型智能体的推测性宏指令提交（Speculative Macro Commit）
---
### 文章背景与核心概要
现代大语言模型（LLM）智能体在处理复杂任务时，往往受制于串行的“动作-观察”（action-observation）交互循环。每一次工具调用、环境状态转换和观察结果反馈都会带来显著的系统延迟。为打破这一瓶颈，本文作者提出了**推测性宏指令提交（Speculative Macro Commit, SMC）**机制，专为双层智能体系统设计：包含生成权威轨迹的大型决策模型（Actor），以及在隔离环境快照上持续预测和执行未来动作链的快速草稿模型（Drafter）。

SMC 通过从训练轨迹中挖掘重复出现的复合动作骨架，并将其存储在宏指令库中。在运行时，系统将这些模板与草稿模型预测的动作链进行匹配。当权威模型的下一个工具调用与草稿的第一步动作相匹配时，SMC 便可直接将剩余预执行的草稿步骤及其观察结果“提交”到官方轨迹中。实验表明，在 $\tau^2$-Bench（电信子集）和 AppWorld 等基准测试中，SMC 在保持智能体准确率的同时，大幅降低了运行延迟，为多步骤推测执行在智能体领域的应用提供了高效实用的解决方案。

---

# Speculative Macro Commit for Faster Tool-Using Agents

> # Speculative Macro Commit for Faster Tool-Using Agents

## Summary

> ## Summary
> 
> Tool-using Large Language Model (LLM) agents are often bottlenecked by serial action–observation turns, where each tool call, environment transition, and observation creates significant latency. To address this, the authors introduce **Speculative Macro Commit (SMC)**, a runtime mechanism designed for a two-tier agent system:
> 1. **Authoritative Actor Model:** A large model that produces the official trajectory.
> 2. **Speculative Drafter Model:** A faster model that continuously predicts and executes future action chains on an isolated environment snapshot.
> 
> SMC mines recurring multi-action skeletons from training traces and stores them in a macro library. At runtime, these are matched against action chains predicted by the drafter. When the actor's next tool call matches the first drafted action, SMC commits the remaining pre-executed draft steps—along with their observations—directly to the official trajectory. 

### Key Results

> ### Key Results
> * **$\tau^2$-Bench (Telecom Subset):** Using Qwen3.5-27B INT4 (actor) and Qwen3.5-4B (drafter), SMC matches sequential agent accuracy while reducing latency by **10.23%** over the Speculative Actions (SA) baseline and **18.59%** over standard sequential execution.
> * **AppWorld:** SMC reduces wall-clock time by **7.7%** over the SA baseline and **44.9%** over sequential execution, accompanied by only a minor reduction in task completion.

---

## Paper Metadata

> ---
> 
> ## Paper Metadata
> 
> * **arXiv ID:** [arXiv:2609.03236](https://arxiv.org/abs/2609.03236) [cs.AI]
> * **Authors:** Zeyu Liu, Souvik Kundu, Peter A. Beerel
> * **Submitted:** September 3, 2026
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Secondary Subjects:** Multiagent Systems (`cs.MA`)
> * **Comments:** Accepted in MLSP 2026
> * **Official Code Repository:** [GitHub - speculative-macro-commit](https://github.com/zeyuliu1037/speculative-macro-commit)

---

## Abstract

> 工具使用型大语言模型（LLM）智能体不仅在模型推理上消耗实际运行时间（wall-clock time），还在串行的“动作-观察”交互轮次中耗费大量时间，其中每一次工具调用、环境状态转换和观察结果都会延迟后续的决策。为此，我们引入了**推测性宏指令提交**（Speculative Macro Commit, SMC），这是一种针对双层智能体系统的运行时机制：一个大型的权威行动者模型（Actor）生成官方轨迹，而一个更快的推测性草稿模型（Drafter）则在隔离的环境快照上持续预测并执行未来的动作链。SMC 从训练轨迹中挖掘重复的多动作骨架，并将其存储在宏指令库中，用于在运行时与草稿模型预测的动作链进行匹配。当行动者的下一个工具调用与草稿的第一步动作匹配时，SMC 会将剩余的预执行草稿步骤及其观察结果直接提交到官方轨迹中。使用 Qwen3.5-27B INT4 作为权威行动者模型、Qwen3.5-4B 作为推测草稿模型，在 $\tau^2$-Bench 电信子集上，SMC 在保持串行智能体总体准确率的同时，相比推测动作（SA）基线降低了 10.23% 的延迟，相比串行执行降低了 18.59% 的延迟。在 AppWorld 上，SMC 的实际运行时间比 SA 基线减少了 7.7%，比串行执行减少了 44.9%，同时任务完成率仅有微小的下降。总体而言，SMC 提供了一种实用方法，能够复用多步推测执行，并进一步超越单步推测动作，从而减少智能体延迟。
> 
> > Tool-using LLM agents spend wall-clock time not only on model inference but also in serial action--observation turns, where each tool call, environment transition, and observation can delay subsequent decisions. We introduce **Speculative Macro Commit** (SMC), a runtime mechanism for a two-tier agent system: a large authoritative actor model produces the official trajectory, while a faster speculative drafter model continuously predicts and executes future action chains on an isolated environment snapshot. SMC mines recurring multi-action skeletons from training traces and stores them in a macro library used to match against action chains predicted by the drafter at runtime. When the actor's next tool call matches the first drafted action, SMC commits the remaining pre-executed draft steps, together with their observations, to the official trajectory. Using Qwen3.5-27B INT4 as the authoritative actor model and Qwen3.5-4B as the speculative drafter model, SMC matches the sequential agent's overall accuracy while reducing latency by 10.23\% over the Speculative Actions (SA) baseline and 18.59\% over sequential execution on the $\tau^2$-Bench Telecom subset. On AppWorld, SMC reduces wall time by 7.7\% over SA baseline and 44.9\% over sequential execution, with a small reduction in task completion. Overall, SMC provides a practical way to reuse multi-step speculative execution and reduce agent latency beyond single-step speculative actions.