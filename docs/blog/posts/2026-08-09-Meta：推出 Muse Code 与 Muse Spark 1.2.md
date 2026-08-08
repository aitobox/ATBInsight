---
authors:
- aitoboxrobot
categories:
- 产品发布
date: 2026-08-09
hide:
- navigation
tags:
- Meta
- Muse Code
- Muse Spark
- 终端编码代理
- GPU内核优化
title: Meta：推出 Muse Code 与 Muse Spark 1.2
---
### 文章背景与核心概要
Meta 推出了搭载其最新、最强模型 Muse Spark 1.2 的终端编码代理——Muse Code（测试版）。该系统专为处理大型代码库中的复杂软件工程任务而设计，通过异步后台代理、精确重放（replay-exact）的运行时设计以及内置技能，能够自主规划、编写和验证代码。

与此同时，Muse Spark 1.2 在代码编写、复杂调试和长周期（long-horizon）任务方面带来了重大升级，并通过严格的评估以及如高性能 GPU 内核调优等真实世界的优化得到了验证。此次发布标志着 Meta 在构建更智能、更具自主性的软件工程 AI 助手方面迈出了重要一步。

---

## Table of Contents
- [概述](#概述)
- [Muse Code 功能特长](#muse-code-功能特长)
  - [异步后台代理](#异步后台代理)
  - [运行时设计](#运行时设计)
  - [内置技能](#内置技能)
- [Muse Spark 1.2 的核心能力](#muse-spark-12-的核心能力)
  - [与 Muse Code 协同训练](#与-muse-code-协同训练)
  - [长周期任务处理](#长周期任务处理)
  - [自我改进机制](#自我改进机制)
- [案例研究：内核优化](#案例研究内核优化)
- [可用性](#可用性)

---

## 概述

我们很高兴发布 **Muse Code (beta)**，这是一个由我们的最新模型 **Muse Spark 1.2** 驱动的终端编码代理。这标志着我们向技术前沿迈出了下一步，更大、能力更强的模型也正在研发中。

> We're excited to release **Muse Code (beta)**, a terminal coding agent powered by **Muse Spark 1.2**, our newest model. This marks our next step toward the frontier, with larger and much more capable models on the way.

Muse Code 能够处理大型代码库中的复杂软件工程任务：规划变更、编写代码以及验证结果。它可以为每个任务协调多个持久化子代理，以更高、更准确的效率解决难题，并减少人工干预。

> Muse Code takes on complex software engineering tasks across large repositories: planning changes, writing code, and validating the results. It can coordinate multiple persistent subagents for each task, solving difficult problems faster, more accurately, and with less intervention.

---

## Muse Code

### 异步后台代理
Muse Code 采用简单的代理循环加一组异步后台代理的架构，以增强主代理的能力。这些专用的后台代理在整个会话期间保持活跃，而不是针对单个任务临时生成，从而避免了冗余的信息收集。它们负责执行后续步骤，并自行选择何时将信息反馈给主代理。它们的持久性降低了延迟，并减少了在复杂的、多步骤任务中进行干预的需求。

> ### Async Background Agents
> Muse Code operates with a simple agent loop plus a set of async background agents to enhance the main agent's capability. These specialized background agents remain active throughout each session, rather than being spawned for individual tasks, helping avoid redundant information gathering. They carry out next steps and choose when to communicate back to the main agent. Their persistence reduces latency and the need for steering on difficult, multi-step tasks.

### 运行时设计
Muse Code 使用本地事件日志，其中记录了每一个模型调用、工具运行、批准和编辑操作。这一单一的真相来源（single source of truth）使得运行时具备“精确重放”和“崩溃安全”的特性：在崩溃后，代理可以准确地从停止的地方恢复。这种能力使得 Muse Code 能够承担长时间运行的任务，而不会被故障所打断。

> ### Runtime Design
> Muse Code uses a local event log in which every model call, tool run, approval, and edit is appended. This single source of truth makes the runtime replay-exact and restart-safe: after a crash, the agent can resume precisely where it stopped. That ability lets Muse Code take on long-running tasks without being derailed by failures.

### 内置技能
Muse Code 随附了几项默认技能：
- `/plan` 将任务转化为需要批准的计划
- `/grill` 对该计划进行压力测试，直至其无懈可击
- `/goal` 朝着成功完成指定目标的方向推进

> ### Bundled Skills
> Muse Code ships with several default skills:
> - `/plan` turns a task into an approval-gated plan
> - `/grill` stress-tests that plan until it holds up
> - `/goal` works toward successful completion of the specified objective

---

## Muse Spark 1.2

Muse Spark 1.2 是针对 Muse Spark 1.1 的代码导向更新，在代码生成、复杂调试、代码库理解以及端到端开发人员工作流方面均有所改进。我们显著提升了编码任务的训练计算量，同时扩大了训练环境的多样性。该模型在通用代理等其他关键领域也保持了其强大实力。

> Muse Spark 1.2 is a coding-focused update to Muse Spark 1.1, featuring improvements in code generation, complex debugging, codebase understanding, and end-to-end developer workflows. We significantly scaled up training compute on coding tasks while expanding training environment diversity. The model also maintains its strength in other key areas like general agents.

### 评估表现

<picture class="site-image-module__lM2DSa__picture site-image-module__lM2DSa__fillPicture" data-site-image-fill="true">
  <source media="(min-width: 64rem)" srcset="/articles/introducing-muse-code-and-muse-spark-1-2/evaluations/terminal-bench-2-1-v1.png"/>
  <img alt="Bar chart comparing Terminal-Bench 2.1 scores for Muse Spark 1.2 and other coding models." class="site-image-module__lM2DSa__image article-dataset-media-module__b_2lNW__media article-dataset-media-module__b_2lNW__contain" src="/_next/image?url=%2Farticles%2Fintroducing-muse-code-and-muse-spark-1-2%2Fevaluations%2Fterminal-bench-2-1-v1.png&w=3840&q=90"/>
</picture>

<picture class="site-image-module__lM2DSa__picture site-image-module__lM2DSa__fillPicture" data-site-image-fill="true">
  <source media="(min-width: 64rem)" srcset="/articles/introducing-muse-code-and-muse-spark-1-2/evaluations/deepswe-1-1-v1.png"/>
  <img alt="Bar chart comparing DeepSWE 1.1 scores for Muse Spark 1.2 and other coding models." class="site-image-module__lM2DSa__image article-dataset-media-module__b_2lNW__media article-dataset-media-module__b_2lNW__contain" src="/_next/image?url=%2Farticles%2Fintroducing-muse-code-and-muse-spark-1-2%2Fevaluations%2Fdeepswe-1-1-v1.png&w=3840&q=90"/>
</picture>

<picture class="site-image-module__lM2DSa__picture site-image-module__lM2DSa__fillPicture" data-site-image-fill="true">
  <source media="(min-width: 64rem)" srcset="/articles/introducing-muse-code-and-muse-spark-1-2/evaluations/meta-internal-coding-bench-v1.png"/>
  <img alt="Bar chart claiming Meta Internal Coding Bench scores for Muse Spark 1.2 and other coding models." class="site-image-module__lM2DSa__image article-dataset-media-module__b_2lNW__media article-dataset-media-module__b_2lNW__contain" src="/_next/image?url=%2Farticles%2Fintroducing-muse-code-and-muse-spark-1-2%2Fevaluations%2Fmeta-internal-coding-bench-v1.png&w=3840&q=90"/>
</picture>

有关我们评估的更多详情，请参见[我们的报告](/static/muse-spark-1-2-methodology)。

> For more details about our evaluations, see [our report](/static/muse-spark-1-2-methodology).

### 与 Muse Code 协同训练
我们将 Muse Spark 1.2 与 Muse Code 进行了协同训练，以确保模型在两者的结合使用中展现出最佳的性能和编码可用性。训练内容包括拒绝采样（rejection sampled）的测试平台（harness）轨迹、针对目标、压缩和子代理的配方优化，以及 Muse Code 工具集的集成，从而最大程度地提高测试平台的兼容性。

> ### Co-Training With Muse Code
> We co-trained Muse Spark 1.2 with Muse Code to ensure the model exhibits its best performance and coding usability when paired together. The training included rejection sampled harness trajectories and recipe optimizations for goals, compaction, and subagents, alongside the integration of the Muse Code toolset to maximize harness compatibility.

### 长周期任务
Muse Spark 1.2 经过了广泛的长周期编码任务训练，包括全代码库生成、大型端到端项目和自动研究（auto-research）。它利用规划来编排工作序列，利用目标条件化来保持方向，并利用上下文压缩来保留维持进展所需的知识。

> ### Long-Horizon
> Muse Spark 1.2 was extensively trained on long-horizon coding tasks, including whole-repository generation, large end-to-end projects, and auto-research. It leverages planning to sequence work, goal conditioning to maintain direction, and context compaction to retain the knowledge needed to sustain progress.

### 自我改进机制
我们还利用 Muse Spark 1.1 生成了具有挑战性的编码环境和指令遵循模板。随后，模型根据候选解决方案满足这些要求的程度进行打分，为 Muse Spark 1.2 生成了可扩展的训练数据集。这种自我改进循环帮助 Muse Spark 1.2 比其前代模型更加精确地遵循复杂的指令。

> ### Self-Improvement
> We also used Muse Spark 1.1 to generate challenging coding environments and instruction-following templates. The model then graded candidate solutions on how well they satisfied those requirements, producing a scalable training dataset for Muse Spark 1.2. This self-improvement loop helped Muse Spark 1.2 follow complex instructions more precisely than its predecessor.

---

## 案例研究：内核优化

我们测试了该模型在超过 1,000 次工具调用（长达 24 小时）中迭代优化 GPU 内核的能力。利用 Muse Code 的代理式编码环境，模型能够针对所提供的基准实现，自主进行内核性能的编写、编译、性能分析和渐进式改进。我们在 NVIDIA Hopper GPU 上对 KDA 和 MLA 内核进行了基准测试。该代理在提供的基准实现基础上持续取得了实质性的改进。

> We tested the model's ability to iteratively optimize GPU kernels over 1,000+ tool calls (up to 24 hours). Leveraging Muse Code's agentic coding environment, the model writes, compiles, profiles, and progressively improves kernel performance relative to a provided baseline implementation. We benchmarked on KDA and MLA kernels for NVIDIA Hopper GPUs. The agent continues to achieve substantial improvements over the provided baseline implementation.

<picture class="site-image-module__lM2DSa__picture site-image-module__lM2DSa__fillPicture" data-site-image-fill="true">
  <source media="(min-width: 64rem)" srcset="/articles/introducing-muse-code-and-muse-spark-1-2/kernel-optimization/kda-speedup-v1.png"/>
  <img alt="Chart comparing KDA kernel speedup against the baseline over cumulative tool calls for Muse Spark 1.2 and other models." class="site-image-module__lM2DSa__image article-dataset-media-module__b_2lNW__media article-dataset-media-module__b_2lNW__contain" src="/_next/image?url=%2Farticles%2Fintroducing-muse-code-and-muse-spark-1-2%2Fkernel-optimization%2Fkda-speedup-v1.png&w=3840&q=90"/>
</picture>

> **优化细节：** 基准（baseline）是 KDA 的 FLA Triton 实现。模型被禁止直接导入 FLA 等第三方内核库；相反，它们必须应用专业的内核优化知识，在 Triton 中实现该算法。Muse Spark 1.2 将块并行（chunk-parallel）准备内核与顺序块间扫描（inter-chunk scan）相结合，将标准的融合与分块（tiling）技术，与 KDA 特定的优化（例如在块中点重新居中门控累积衰减）融为一体。
> 
> > **Optimization Detail:** The baseline is the FLA Triton implementation of KDA. Models were prohibited from importing third-party kernel libraries such as FLA directly; instead, they had to apply specialized kernel-optimization knowledge to implement the algorithm in Triton. Muse Spark 1.2 paired a chunk-parallel preparation kernel with a sequential inter-chunk scan, combining standard fusion and tiling with KDA-specific optimizations such as re-centering the gated cumulative decay at the chunk midpoint.

---

## 可用性

Muse Spark 1.2 现已在 Muse Code 以及扩展了全球访问权限的 Meta Model API 中上线。未来我们还有许多规划，包括新的测试平台功能和更强大的模型。我们迫不及待地想看大家用它创造出什么！

> Muse Spark 1.2 is available today in Muse Code and in Meta Model API with expanded global access. We have a lot on the horizon, including new harness features and more powerful models. We can’t wait to see what you build!

[开始使用 Muse Code](https://dev.meta.ai)
> [Get started with Muse Code](https://dev.meta.ai)