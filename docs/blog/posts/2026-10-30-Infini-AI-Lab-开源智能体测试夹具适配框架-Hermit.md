---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-30
hide:
  - navigation
tags:
  - AI 智能体
  - Hermit
  - 开源框架
  - 测试夹具
  - 适配器
title: "Infini-AI-Lab 开源智能体测试夹具适配框架 Hermit：无需微调基座即可演进 Agent"
---

# Infini-AI-Lab 开源智能体测试夹具适配框架 Hermit：无需微调基座即可演进 Agent

> # Infini-AI-Lab Releases Hermit, an Open-Source Harness Adapter Framework for AI Agents

### 文章背景与核心概要
在当前的 AI 智能体 (AI Agent) 研发中，想要提升智能体在特定复杂任务中的表现，开发者通常面临两难困境：要么微调大语言模型 (Large Language Model, LLM) 底层权重（成本高昂且容易破坏通用泛化能力），要么大改智能体的闭源或精密代码脚手架（极易引发组件冲突）。卡内基梅隆大学 (CMU) 博士后 Haizhong Zheng 等人主导的 Infini-AI-Lab 团队正式开源了 Hermit 框架，创新性地提出了“测试夹具适配器 (Harness Adapter)”概念。它就像给智能体的外部运行环境穿上一套轻量、可插拔的“技能外骨骼”，在完全冻结基座大模型和原有脚手架的前提下，通过强化学习驱动的演进循环自动优化提示词、记忆、工具与协同逻辑，极大降低了智能体针对新任务持续进化的技术门槛。

---

## 执行摘要

> ## Executive Summary

Infini-AI-Lab 推出了开源 Python 框架 **Hermit** (v0.1.0)。该框架旨在保持底层基础大语言模型 (Large Language Model, LLM) 与智能体测试夹具 (Agent Harness) 完全冻结的前提下，为 AI 智能体 (AI Agent) 训练外置的“测试夹具适配器 (Harness Adapter)”。该项目由 CMU 博士后 Haizhong Zheng 发布，提供了一套统一的训练循环机制，用以系统化优化指令、技能、记忆、工具以及执行逻辑。开发者无需微调基座模型权重，也无需分叉修改现有代码库，只需通过 PyPI 执行 `pip install hermit-harness`，即可轻松将 Codex 或 Claude Code 等主流编程智能体适配到全新的复杂任务中。

> Infini-AI-Lab has introduced **Hermit** (v0.1.0), an open-source Python framework designed to train external "harness adapters" for AI agents while keeping the underlying foundation model and agent harness completely frozen. Announced by CMU postdoc Haizhong Zheng, Hermit provides a unified training loop to optimize instructions, skills, memory, tools, and execution logic. Developers can easily adapt popular coding agents—such as Codex or Claude Code—to new tasks via PyPI (`pip install hermit-harness`) without the need to fine-tune weights or fork codebases.

---

## 核心要点速览

> ## TL;DR

* **极小占用 (Footprint)**：作为轻量级 Python 框架，本身不包含任何原生模型参数。采用 Apache-2.0 开源许可协议，可通过 `pip install hermit-harness` 一键安装。
* **硬件要求 (Hardware Requirements)**：离线快速入门 (Quick Start) 无需任何 GPU、模型账号或外部数据集。生产环境支持任意 API 后端，亦可通过 vLLM、SGLang 或 Ollama 进行本地推理部署。
* **基准性能 (Performance)**：在 OfficeQA、CL-Bench 以及 ServeLearnBench 评估测试中（以 GLM 5.3 Flash 为测试模型），相较无适配器的基线方案展现出了显著的性能提升。
* **核心亮点 (Highlights)**：
  * *最佳表现*：MetaWorld Model (MWM) 适配器在 CL-Bench 数据库探索任务中取得了 **0.795 的准确率**（相比之下，上下文学习基线仅为 0.580）。
  * *最低表现*：仅依赖提示词的适配器 (Prompt-only Adapter) 在同一基准测试中仅取得 **0.470**，甚至低于标准基线表现。
* **一句话总结 (Bottom Line)**：Hermit 提供了支持 5 种不同夹具演进方法的统一训练循环，不过目前披露的多数成果仍来自于单次自测运行数据。

> * **Footprint:** A lightweight Python framework with no native parameters of its own. Available under the Apache-2.0 license via `pip install hermit-harness`.
> * **Hardware Requirements:** The offline Quick Start requires no GPU, model account, or external dataset. Production runs support any API backend or local serving setups via vLLM, SGLang, or Ollama.
> * **Performance:** Demonstrates notable improvements over no-adapter baselines across OfficeQA, CL-Bench, and ServeLearnBench (evaluated using GLM 5.3 Flash).
> * **Highlights:** 
>   * *Best Performer:* The MetaWorld Model (MWM) adapter hits **0.795 accuracy** on CL-Bench database exploration (compared to 0.580 for the in-context baseline).
>   * *Lowest Performer:* The prompt-only adapter scores **0.470** on the same benchmark, falling below the standard baseline.
> * **Bottom Line:** Hermit offers a single training loop supporting 5 distinct harness evolution methods, though most reported results currently stem from single, self-reported runs.

---

## 什么是测试夹具适配器？

> ## What is a Harness Adapter?

[测试夹具适配器 (Harness Adapter)](https://infini-ai-lab.github.io/hermit/) 的功能类似于为现有智能体运行环境量身定制的可训练插件。传统的模型适配器（例如 LoRA）是通过修改底层神经网络的权重来提升能力的，而**测试夹具适配器**则是对包裹在大模型外部的智能体系统框架进行适配与改造。

> A [harness adapter](https://infini-ai-lab.github.io/hermit/) functions similarly to a trainable plugin for existing agent environments. While model adapters (like LoRA) modify the underlying neural network weights, a **harness adapter** adapts the surrounding agentic framework.

该适配器将提示词指令、操作技能、记忆状态、外部工具、可执行代码以及多智能体协同逻辑封装在一起——本质上充当了模块化的代码仓库扩展包。它的规范定义了可学习的参数空间与校验标准，而将基座大模型和底层运行环境完整保留，完全无需任何改动。

> The adapter encapsulates instructions, operational skills, memory states, tools, executable code, and agent coordination logic—essentially acting as a modular repository extension. Its specification defines learnable parameters and validation criteria, leaving the base model and harness entirely untouched.

Infini-AI-Lab 强调了采用这种设计架构的三大核心考量：

> Infini-AI-Lab highlights three core motivations for this design:

1. 业界许多先进的智能体运行环境与支撑脚手架至今仍处于闭源状态。
2. 直接修改开源运行环境中的代码，往往会破坏其内部经过精细调优的脆弱组件联动关系。
3. 一旦训练出成熟的适配器，就可以无缝迁移到其他兼容的大模型和运行环境中。

> 1. Many agent harnesses remain closed-source.
> 2. Direct modifications to open harnesses frequently break fragile, finely-tuned component interactions.
> 3. A learned adapter can be seamlessly ported across compatible models and harnesses.

---

## Hermit 是如何训练适配器的？

> ## How Does Hermit Train an Adapter?

Hermit 采用了一套强化学习 (RL) 风格的训练闭环，核心由三大组件构成：

> Hermit utilizes an RL-style training loop comprising three primary components:

1. **训练器 (Trainer)**：使用当前版本的适配器，驱动实际执行动作的智能体批量运行任务。
2. **裁判员 (Judge)**：对智能体的执行输出进行打分评估，并生成结构化的反馈意见。
3. **演进器 (Evolver)**：深度分析执行轨迹与反馈日志，进而提出经过优化演化后的新一代适配器方案。

> 1. **Trainer:** Runs batches of tasks through the acting agent using the current adapter version.
> 2. **Judge:** Evaluates outputs and provides structured feedback.
> 3. **Evolver:** Analyzes execution trajectories and feedback to propose updated adapter iterations. 

训练器会在将演进方案提交保存为新版本之前，依据预设模板对其进行严格验证。每一个版本的适配器都会妥善存储在一个内部 Git 树结构中，便于开发者随时检视演化过程、回滚历史版本或将特定迭代快速交付投产。在运行学习程序的环境沙箱方面，需要在 Linux 系统中配备 `bubblewrap` 隔离工具。

> The Trainer validates these proposals against a predefined template before committing them as the next version. Every adapter version is stored within an internal git tree, allowing developers to inspect, roll back, or ship any historical iteration. Sandbox execution of learner programs requires Linux with `bubblewrap`.

### 内置演进方法

> ### Built-in Evolution Methods

Hermit 目前内置支持五种原生演进算法：
* **GEPA**
* **SkillOpt**
* **MetaWorld Model (MWM)**
* **Harness²**
* **Continual Harness**

> Hermit currently ships with five native evolution methods:
> * **GEPA**
> * **SkillOpt**
> * **MetaWorld Model (MWM)**
> * **Harness²**
> * **Continual Harness**

*注：官方路线图显示 **ACE** 与 **ReHarness** 的集成支持即将推出，开发者也可以自行编写定制的演进器 (Evolver)。*

> *Note: Integration for **ACE** and **ReHarness** is listed as coming soon, and developers can also author custom Evolvers.*

---

## 基准测试结果

> ## Benchmark Results

*以下所有自测实验结果均采用 **GLM 5.3 Flash** 作为执行推理的基座模型。*

> *All self-reported results below utilize **GLM 5.3 Flash** as the acting model.*

### 1. OfficeQA 基准测试

> ### 1. OfficeQA

在针对美国财政部公报 (U.S. Treasury Bulletins) 的 172 个问答测试题上展开评估（评估指标为严格匹配准确率）：

> Evaluating 172 test questions regarding U.S. Treasury Bulletins (scored by exact match):

| 方法 | 准确率 |
| :--- | :--- |
| 无适配器基线 (No adapter) | 0.541 |
| 初始技能 (Initial skill) | 0.576 |
| GEPA | 0.580 |
| SkillOpt | 0.600 |
| Continual Harness | 0.634 |
| Harness² | **0.651** |

*其中 GEPA 和 SkillOpt 在 50 道训练题上完成训练并冻结权重后进行评估；而 Continual Harness 和 Harness² 则在对测试集进行单次流式处理时动态自适应更新。*

> *GEPA and SkillOpt are trained on 50 questions and evaluated frozen. Continual Harness and Harness² adapt dynamically while streaming the test set once.*

### 2. CL-Bench 基准测试

> ### 2. CL-Bench

测试来自持续学习基准测试 (Continual Learning Bench) 的有状态交互环境：

> Testing stateful environments from the Continual Learning Bench:

* **数据库探索任务 (Database Exploration)**：MWM 适配器取得了 **0.795 的准确率**，远超标准上下文学习 (ICL) 基线的 **0.580**。
* **可利用扑克博弈 (Exploitable Poker)**：MWM 每手牌可平均净赢 **3.08 个大盲注**，而标准上下文学习仅能赢得 **2.51 个大盲注**。

> * **Database Exploration:** The MWM adapter reaches **0.795 accuracy**, outperforming the standard in-context baseline of **0.580**.
> * **Exploitable Poker:** MWM wins **3.08 big blinds per hand**, compared to **2.51** for in-context learning.

### 3. ServeLearnBench 基准测试

> ### 3. ServeLearnBench

在隐式业务策略动态漂移的情境下，流式处理 624 项零售客户支持请求：

> Streaming 624 retail support requests under a shifting hidden policy:

* **MWM 适配器**：在隐式策略评估中取得 **45.3 分**。
* **Continual Harness (CH)**：取得 **28.7 分**（此前排行榜的最优基准成绩）。
* **理论上限参考 (Oracle)**：得分 **89.2 分**（在直接显式获知隐式策略的前提下取得的参考基准）。

> * **MWM:** Scores **45.3** on hidden-policy evaluations.
> * **Continual Harness (CH):** Scores **28.7** (the previous leaderboard benchmark).
> * **Oracle:** Scores **89.2** (when explicitly given the hidden policy).

---

## Hermit 与其他智能体优化器横向对比

> ## How Does Hermit Compare with Other Agent Optimizers?

| 特性 | [Hermit](https://github.com/Infini-AI-Lab/hermit) | [GEPA](https://github.com/gepa-ai/gepa) | [ACE](https://github.com/ace-agent/ace) | [Agent Lightning](https://github.com/microsoft/agent-lightning) |
| :--- | :--- | :--- | :--- | :--- |
| **训练对象** | 外置测试夹具适配器 | 任意文本参数（提示词、代码） | 上下文战略剧本 (Context Playbook) | 提示词与模型权重 |
| **是否修改模型权重** | 否 | 否 | 未公开披露 | 是（通过强化学习或监督微调 SFT） |
| **演进优化方法** | 5 种内置演进算法 + 自定义 Evolver | 反思演进 (Reflective Evolution)、帕累托选择 (Pareto Selection) | 生成器、反思器、精选器 (Generator, Reflector, Curator) | 强化学习、提示词优化、监督微调 (SFT) |
| **部署目标平台** | Codex, Claude Code, Pi；支持插件导出 | DSPy (`dspy.GEPA`) | 未公开披露 | LangChain, OpenAI Agents SDK, AutoGen, CrewAI 等 |
| **开源许可证** | Apache-2.0 | MIT | Apache-2.0 | MIT |
| **关键评测结果** | CL-Bench 数据库测试达 0.795（自测数据） | AIME 2025 数学测试：46.6% 提升至 56.6% (GPT-4.1 Mini) | AppWorld 基准提升 +10.6% | 未公开披露 |

---

## 安装、部署与命令行 (CLI) 使用指南

> ## Installation, Deployment, and CLI Usage

可通过 [PyPI](https://pypi.org/project/hermit-harness/) 快速安装该框架：

> Install the framework from [PyPI](https://pypi.org/project/hermit-harness/):

```bash
pip install hermit-harness
```

Hermit 支持采用 `<backend>/<model id>` 格式配置推理后端与模型。目前兼容的后端平台包括 Fireworks、OpenAI、Anthropic、DeepSeek、vLLM、SGLang 以及 Ollama。

> Hermit supports model configurations in the format `<backend>/<model id>`. Compatible backends include Fireworks, OpenAI, Anthropic, DeepSeek, vLLM, SGLang, and Ollama.

### 核心命令行指令

> ### Core CLI Commands

```bash
# 运行训练配置流程
hermit train --config run.yaml

# 评估特定的适配器版本
hermit eval --config run.yaml --adapter final

# 将训练好的适配器部署到活跃的智能体工作区
hermit deploy --adapter DIR --workspace WS --host codex

# 将训练好的适配器导出为原生插件
hermit convert --adapter DIR --output OUT --target claude-code
# 支持的转换导出目标：codex, pi, hermes
```

*应用范例：* 官方提供了一个完整的 [Lean 形式化定理证明协作适配器 (Lean collaboration adapter)](https://github.com/Infini-AI-Lab/hermit/tree/main/examples/lean_swarm)，可用于协同编排 5 个 Codex 智能体并发工作，共同完成单一数学定理的推导与证明。

> *Example:* A complete [Lean collaboration adapter](https://github.com/Infini-AI-Lab/hermit/tree/main/examples/lean_swarm) can be deployed to coordinate 5 Codex agents working concurrently to prove a single theorem.

---

## 核心总结与技术启示

> ## Key Takeaways

* Hermit 专注于训练外部夹具适配器，在此期间基础智能体模型和运行环境完全保持冻结。
* 内置交付了 5 种前沿演进算法：GEPA、SkillOpt、MWM、Harness² 以及 Continual Harness。
* 其中的 MetaWorld Model (MWM) 适配器在 CL-Bench 数据库交互任务中斩获了 **0.795 的高准确率**（相较之下标准上下文学习仅为 0.580）。
* 训练完成的适配器既可直接无缝部署到 Codex、Claude Code 和 Pi，也能干净利落地导出为通用原生插件。
* 需客观看待的是，当前官方公布的各项性能评测指标均来自于采用 GLM 5.3 Flash 的单次自测运行结果。

> * Hermit trains external harness adapters while keeping base agent models and harnesses frozen.
> * Ships with 5 built-in evolution methods: GEPA, SkillOpt, MWM, Harness², and Continual Harness.
> * The MetaWorld Model (MWM) adapter achieves **0.795 accuracy** on CL-Bench database tasks (vs. 0.580 in-context).
> * Adapters deploy directly to Codex, Claude Code, and Pi, or export cleanly as native plugins.
> * Reported performance metrics are currently based on single, self-reported evaluation runs using GLM 5.3 Flash.

---

## 项目资源与社区

> ## Resources & Community

* **GitHub 代码仓库**：[Infini-AI-Lab/hermit](https://github.com/Infini-AI-Lab/hermit)
* **项目主页与文档**：[Hermit 项目主页](https://infini-ai-lab.github.io/hermit/) 与 [官方技术文档](https://infini-ai-lab.github.io/hermit/docs/)
* **原始发布报道**：[MarkTechPost 专题报道](https://www.marktechpost.com/2026/10/29/infini-ai-lab-hermit-harness-adapter-framework/)

> * **GitHub Repository:** [Infini-AI-Lab/hermit](https://github.com/Infini-AI-Lab/hermit)
> * **Project Documentation:** [Hermit Project Page](https://infini-ai-lab.github.io/hermit/) & [Official Docs](https://infini-ai-lab.github.io/hermit/docs/)
> * **Original Announcement:** [MarkTechPost Coverage](https://www.marktechpost.com/2026/10/29/infini-ai-lab-hermit-harness-adapter-framework/)
