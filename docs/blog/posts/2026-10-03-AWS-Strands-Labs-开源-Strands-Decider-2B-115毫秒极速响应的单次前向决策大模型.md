---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-03
hide:
  - navigation
tags:
  - AWS
  - Strands Decider 2B
  - 决策模型
  - System One
  - Qwen3.5
  - 工具调用路由
  - 开源模型
title: "AWS Strands Labs 开源 Strands Decider 2B：115毫秒极速响应的单次前向决策大模型"
---

# AWS Strands Labs 开源 Strands Decider 2B：115 毫秒极速响应的单次前向决策大模型

> # AWS Strands Labs Releases Strands Decider 2B: An Open Source Decision Model That Picks Options in About 115 ms

### 文章背景与核心概要

在构建现代 AI 智能体 (AI Agent) 系统的过程中，传统的大语言模型 (Large Language Model, LLM) 往往扮演着“事无巨细皆需长篇大论”的角色，即便是面对二选一确认、意图路由或工具选择等简单的确定性判定，也必须逐字解码生成 Token，带来了不可忽视的延迟开销与格式幻觉隐患。为攻克这一工程痛点，AWS Strands Labs 正式开源了参数量为 19 亿的“快思考系统” (System One) 决策模型 Strands Decider 2B。该模型创新性地去除了传统大语言模型的解码生成头，改用极轻量的指针分类头，在单次前向传播中仅需约 115 毫秒即可直接返回离散选项、概率或评分，同时保持了极佳的统计校准水平。这一成果不仅能够在消费级显卡或 Apple Silicon 上本地流畅运行，更以零幻觉、低延迟和全开源的特性，为下一代端到端智能体系统的敏捷编排与实时安全护栏树立了全新的技术标杆。

---

## 执行摘要

> ## Executive Summary

AWS Strands Labs 正式推出了 **Strands Decider 2B**，这是一款包含 19 亿参数的开源“快思考系统” (System One) 决策模型。与传统的大语言模型 (Large Language Model, LLM) 不同，Strands Decider 并不生成自由文本；相反，它能够精确评估当前上下文状态与特定类型的问题，直接返回离散选项、是否概率 (yes/no) 或结构化的评分评估。该模型支持在本地 CPU、消费级 GPU 以及搭载 Apple Silicon 的 Mac 电脑上运行，中位推理延迟仅约 115 毫秒，专为工具选择、模型路由以及智能体安全护栏 (Guardrails) 等讲求高效率与校准精度的关键任务量身打造。目前，其完整模型权重已在 [Hugging Face](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19) 上完全开源，遵循宽松的 Apache-2.0 许可证。

> AWS Strands Labs has launched **Strands Decider 2B**, an open-source "System One" decision model containing 1.9 billion parameters. Unlike traditional Large Language Models (LLMs), Strands Decider does not generate text; instead, it evaluates a state and typed questions to return a discrete choice, a yes/no probability, or a scored evaluation. Running locally on CPUs, consumer GPUs, or Apple Silicon Macs with a median latency of roughly 115 ms, the model is designed for efficient, calibrated tasks like tool selection, model routing, and agent guardrails. Its weights are openly available on [Hugging Face](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19) under the Apache-2.0 license.

---

## 部署方式与易用性

> ## Deployment & Accessibility

Strands Decider 2B 完全支持在本地与私有化自托管环境中独立部署：

> Strands Decider 2B is fully deployable for local and self-hosted environments:

* **便捷安装**：只需执行 `pip install strands-decider` 即可完成一键安装，同时提供命令行工具 (CLI) 与 HTTP 服务端；
* **环境要求**：由于内置的服务器默认绑定至本地回环地址 `127.0.0.1` 且未集成原生身份验证，若在生产环境中向外部开放，必须配置外部鉴权代理层；
* **推理服务**：目前阶段尚无托管型的第三方云推理服务商接入该模型。

> * **Installation:** Easily installed via `pip install strands-decider`, providing both a CLI and an HTTP server.
> * **Requirements:** Because the bundled server binds to `127.0.0.1` without built-in authentication, production deployments require an external auth layer.
> * **Inference:** Currently, no hosted third-party inference providers serve the model.

---

## 决策模型的核心机制

> ## What a Decision Model Does

作为自 TypeSafe AI 推出 Jev 以来不断壮大的“快思考系统” (System One) 模型门类的新成员，决策模型将输出范围严格限制在预定义选项列表或特定数值刻度之内，彻底避免了标准大语言模型常见的无序自由文本生成与输出漂移。

> As part of a growing category of "System One" models that emerged following TypeSafe AI’s launch of Jev, decision models restrict their outputs strictly to predefined options or numerical scales, avoiding the arbitrary text generation common in standard LLMs. 

Strands Decider 原生支持三类各具特色的结构化提问类型：

> Strands Decider supports three distinct question types:

* **`choice` (单项选择) **：从 $N$ 个预定义候选选项中挑选出 1 个最佳选项；
* **`noul` (二元概率) **：在 0 到 1 之间精确评估针对某一命题的“是/否”判定置信概率；
* **`score` (标准评分) **：依据预设的有序评判基准量表对输入内容进行打分评级。

> * **`choice`**: Selects 1 out of $N$ possible options.
> * **`noul`**: Evaluates a yes/no probability between 0 and 1.
> * **`score`**: Rates an input against an ordered rubric.

模型的每一次输出均严格受限于所允许的候选选项子集，并附带经过严格统计校准的置信度评分。需要注意的是，该模型**并不适合**用于处理复杂的长链推理、代码编写、多轮闲聊对话或长篇文本摘要等任务。

> Every output returns a strict subset of the allowed options alongside a calibrated confidence score. The model is **not** suited for complex reasoning, coding, conversational chat, or summarization tasks.

---

## 架构设计：拆掉“发言嘴”的大语言模型

> ## Architecture: An LLM with Its Mouth Removed

该模型构建于 [Qwen3.5-2B-Base](https://huggingface.co/Qwen/Qwen3.5-2B-Base) 基础架构之上，并针对分类决策的执行效率重构了核心网络层：

> The model is built upon the [Qwen3.5-2B-Base](https://huggingface.co/Qwen/Qwen3.5-2B-Base) architecture, modifying the core structure for classification efficiency:

* **轻量指针头 (The Pointer Head)**：彻底弃用了传统大语言模型庞大的因果语言建模输出头，转而换上了一个仅约 100 万参数 (约 1M) 的精简指针头；
* **单步推理机制 (Inference Mechanism)**：该指针头直接将 `<answer>` 标记位置的隐藏状态 (Hidden State) 与每个候选选项末尾 Token 的隐藏状态进行点积比对。这使得模型无需经历缓慢的自回归**解码循环** (Decoding Loop)，仅凭单次前向传播 (Forward Pass) 即可瞬间给出决策结果；
* **模型主干与精度 (Torso & Scale)**：模型主干网络采用了 rank-16 的 LoRA 微调，而指针分类头则以高精度的 `fp32` 格式执行。由于候选标签集是在每次 API 请求中动态给出的，因此可支持的选项数量在理论上几乎不受限制 (当前发布的模型检查点为 `v19`) ；
* **极速多任务复用 (Efficiency)**：针对同一段文本输入同时进行多项问题评估时具有极致的性能优化——原始文本的状态仅需计算读取一次，后续附加的多个判定问题只会产生极小的额外 Token 计算开销。

> * **The Pointer Head:** The traditional language-modeling head is discarded and replaced with a lightweight pointer head (~1M parameters). 
> * **Inference Mechanism:** The head compares the hidden state at the `<answer>` position against the hidden state at each option’s last token. This allows the model to yield results in a single forward pass **without a decoding loop**.
> * **Torso & Scale:** The torso utilizes a rank-16 LoRA, while the head executes in `fp32`. Because label sets are defined dynamically via requests, option counts are virtually uncapped (current released checkpoint: `v19`).
> * **Efficiency:** Evaluating multiple questions for a single text input is highly optimized—the state is read just once, and subsequent questions incur minimal token overhead.

---

## 基准测试与推理延迟

> ## Benchmarks and Latency

在 [JevBench](https://benchmarkheaven.com/jev-models) 公开基准测试集上，`v19` 版本的模型检查点展现出了极具竞争力的性能水准：

> Measured against public sets on [JevBench](https://benchmarkheaven.com/jev-models), the `v19` checkpoint delivers competitive performance:

* **公开测试准确率**：0.723 (在 JevBench v1 的 231 项评测任务中成功解决 167 项) ；
* **概率校准表现**：Brier 得分为 0.342，预期校准误差 (Expected Calibration Error, ECE) 仅为 0.052；
* **分级难度表现**：简单任务达 1.000；标准任务为 0.875；困难任务为 0.505；
* **硬件延迟表现 (RTX 3090)**：中位延迟仅 115 毫秒，p95 延迟为 299 毫秒；
* **硬件延迟表现 (M3 Pro)**：预热后中位延迟为 153 毫秒 (输入文本在 300 个 Token 以内) 。

> * **Public Accuracy:** 0.723 (167 out of 231 tasks on JevBench v1).
> * **Calibration:** Brier score of 0.342; Expected Calibration Error (ECE) of 0.052.
> * **Tier Breakdown:** Easy tasks: 1.000; Standard tasks: 0.875; Hard tasks: 0.505.
> * **Latency (RTX 3090):** 115 ms median, 299 ms p95.
> * **Latency (M3 Pro):** 153 ms warm median (under 300 tokens).

### 实用可靠性分析

> ### Practical Reliability

优秀的概率校准是该模型最核心的工程竞争力所在：在面向未见过的短文本分类测试中，凡是模型输出置信度达到或超过 0.9 的判定结果，其预测准确率高达约 **95%**。因此，工程团队建议将 0.9 设为可靠阈值，低于该置信度的请求可自动路由升级至更大规模的大模型进行仲裁。

> Calibration represents a core strength of the model: on unseen short classification tasks, answers exhibiting a confidence score of 0.9 or higher were correct roughly **95% of the time**. The development team recommends routing or escalating inputs below this threshold.

---

## 横向对比评测

> ## How It Compares

| 特性 (Feature) | Strands Decider 2B (v19) | Jev 1.13.0 | decider-2b | Decision 2B |
| :--- | :--- | :--- | :--- | :--- |
| **开发者 (Developer)** | Strands Agents (AWS) | TypeSafe AI | Mapika | FlyMy.AI |
| **开放模式 (Access)** | 开源权重，遵循 Apache-2.0 协议 | 闭源托管 API | 开源代码或权重 | 开源代码或权重 |
| **基座模型 (Base model)** | Qwen3.5-2B-Base + LoRA + 指针头 | 未公开 | Qwen3.5-2B-Base + 训练读出头 | MiniCPM5-2B + LoRA + 指针头 |
| **模型体量 (Size)** | 1.9B | 未公开 | 1.9B | 2.5B dense |
| **支持自托管 (Self-hosting)** | 是 (Yes) | 否 (No) | 是 (Yes) | 是 (Yes) |
| **公开完整训练配方与数据集清单 (Full training recipe and data list published)** | 是 (Yes) | 否 (No) | 未经验证 (Not verified) | 未经验证 (Not verified) |
| **JevBench 公开准确率 (v1.4.2 board)** | 0.723 | 来源表中未收录 | 0.710 | 0.753 |
| **报告延迟 (Reported latency)** | 中位延迟 115 ms (RTX 3090) | 70 至 500 ms (厂商提供数据) | 未对比 | 未对比 |

* (注：上述延迟数据来自不同硬件配置与测试脚手架，不可直接进行等价横向比较) *

> *(Note: Latencies stem from varying hardware setups and testing harnesses and are not directly comparable.)*

---

## 典型应用场景与落地代码示例

> ## Use Cases & Implementation Example

Strands Decider 2B 在要求极致低延迟、确定性输出以及实时安全合规审查的业务场景中展现出巨大优势：

> Strands Decider 2B excels in scenarios requiring fast routing, deterministic classifications, and safety checks:

* **模型路由与工具选择**：极速匹配最契合意图的下游垂直模型或筛选待调用的 API 工具；
* **参数合法性校验与工单分流**：对输入请求进行合法性预检并快速进行分类派单；
* **安全护栏与自动化评估体系**：充当大模型的输入输出防线，提供统计可信的合规过滤；
* **混合双系统智能体架构**：实现“快思考与慢思考”分工协作，由通用大语言模型处理深度推理，而由决策模型承担高频、机械化的确定性分类。

> * Model routing and tool selection
> * Argument checking and triage
> * Guardrails and evaluation frameworks
> * Hybrid agent systems (where an LLM handles complex reasoning while the decider manages high-frequency, rote classifications)

### 实战示例：为工具调用保驾护航

> ### Example: Guarding Tool Calls

根据官方仓库中提供的范例代码，开发者可以在工具触发前设置一个 `before_tool_call` (前置拦截钩子) ，向 Strands 决策智能体发起由“是/否”构成的极速查询，用以验证当前工具调用的参数是否在上下文中得到了充分的凭据支撑 (Grounded) ，或者检测当前调用是否为时过早，从而在工具真正产生副作用前进行安全拦截。类似地，客服工单分流系统也能以此极速分发用户意图 (例如迅速将包含 *“救命！我的提现已经连续失败 3 天了！”* 的用户求助准确分类至 `billing` 账单类别，置信度得分达 0.768) 。

> Using repository-provided examples, a `before_tool_call` intervention can query a Strands agent with yes/no questions to verify whether arguments are properly grounded or if a call is premature before letting tools execute. Similarly, triage commands can rapidly route customer queries (e.g., categorizing *"Help! My payouts have been failing for 3 days!"* as `billing` with a 0.768 confidence score).

---

## 核心要点总结

> ## Key Takeaways

* **专属决策输出**：严格返回预定义的选项、得分或置信概率，绝不生成不受控的随意自然语言文本；
* **高度精简的创新架构**：舍弃了 Qwen3.5-2B 传统的语言建模头，替换为仅约 100 万参数 (约 1M) 的轻量指针头；
* **卓越可靠的校准表现**：在 JevBench 公开测试中取得 0.723 的准确率，预期校准误差 (ECE) 低至 0.052；
* **超高吞吐与极速响应**：在消费级显卡 RTX 3090 上实现了仅 115 毫秒的中位推理延迟；
* **完全开放的开源协议**：包含模型权重、源代码与训练配方在内的全部资产均在 Apache-2.0 许可证下完整开源。

> * **Specialized Output:** Returns strictly defined choices, scores, or probabilities—never free-form text.
> * **Optimized Architecture:** Swaps the traditional language modeling head of Qwen3.5-2B for a ~1M-parameter pointer head.
> * **Strong Calibration:** Achieves a 0.723 score on JevBench public with an ECE of 0.052.
> * **High Performance:** Delivers a median latency of 115 ms on an RTX 3090.
> * **Open Source:** Complete weights, code, and recipes ship freely under the Apache-2.0 license.

---

## 资源链接与延伸阅读

> ## Resources & Further Reading

* [技术原理解析与官方博客](https://strandsagents.com/blog/introducing-strands-decider/)
* [GitHub 官方代码仓库](https://github.com/strands-labs/strands-decider)
* [Hugging Face 模型权重开源主页](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19)
* [MarkTechPost 原始技术报道](https://www.marktechpost.com/2026/10/01/aws-strands-labs-releases-strands-decider-2b/)

> * [Technical Details & Blog Post](https://strandsagents.com/blog/introducing-strands-decider/)
> * [GitHub Repository](https://github.com/strands-labs/strands-decider)
> * [Model Weights on Hugging Face](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19)
> * [Original MarkTechPost Article](https://www.marktechpost.com/2026/10/01/aws-strands-labs-releases-strands-decider-2b/)
