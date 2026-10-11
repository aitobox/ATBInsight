---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-11
hide:
  - navigation
tags:
  - Drex
  - 决策模型
  - 开源模型
  - 智能体
title: "Nace AI 开源 Drex 1.5：无需生成文本、专注于为选项直接打分的 9B 决策模型"
---

# Nace AI 开源 Drex 1.5：无需生成文本、专注于为选项直接打分的 9B 决策模型

> # Nace AI Open-Sources Drex 1.5: A 9B Decision Model That Scores Options, Not Text

### 文章背景与核心概要

传统的生成式大语言模型在做决策判断时往往“废话连篇”：不仅需要自回归逐字生成冗长文本，还极易受到随机采样与幻觉漂移的干扰，导致后端流水线延迟居高不下且计费高昂。为破解这一工业落地瓶颈，Nace.AI 正式开源了参数量为 8.95B 的轻量级专用决策模型 **Drex 1.5** 。该模型彻底摒弃了繁琐的文本生成机制，通过精巧的指针头部架构，仅需单次前向传播 (Single Forward Pass) 即可直接计算出预设选项的精确概率分布。在公开的权威基准测试 Decision Index 0.3.1 中，Drex 1.5 以 58.08 的高分逼平了顶级商业闭源模型 Jev 1.13.0 ，尤其在 32K 至 128K 超长上下文处理中展现出高达 93.4% 的惊人准确率。这不仅为高并发 AI 智能体 (AI Agents) 与自动化后端工作流提供了极速、确定且廉价的决策底座，更标志着开源模型在单卡与端侧设备上迈入了轻量级决策智能的新里程碑。

---

## 📌 执行摘要

> ## 📌 Executive Summary

Nace.AI 正式开源了参数量为 8.95B 的决策模型 **Drex 1.5** ，专门为 AI 智能体 (AI Agents) 与后端自动化工作流量身打造。与传统的大语言模型 (Large Language Models, LLMs) 不同，Drex 1.5 完全不生成冗余的自然语言文本；相反，它能够结合输入的状态与特定类型的问题，仅通过单次前向传播 (Single Forward Pass) 便直接输出预定义选项的概率分布。在权威的 **Decision Index 0.3.1 基准测试** 中，Drex 1.5 斩获了 **58.08 分** 的顶尖战绩，不仅全面比肩主流前沿闭源模型，还能在单张消费级或云端 GPU 上高吞吐运行，甚至可在 Apple Silicon 芯片设备上流畅进行本地部署。

> Nace.AI has open-sourced **Drex 1.5**, an 8.95B parameter decision model designed specifically for agents and backend workflows. Unlike traditional large language models, Drex 1.5 does not generate text; instead, it evaluates a given state alongside typed questions and directly returns probabilities for a predefined set of options in a single forward pass. Achieving a top-tier score of **58.08 on Decision Index 0.3.1**, Drex 1.5 matches the performance of leading closed models while running efficiently on a single consumer or cloud GPU, or locally via Apple Silicon.

---

## 🚀 核心速览 (TL;DR)

> ## 🚀 TL;DR

* **模型规模：** 8.95B 稠密参数 (bf16 格式权重约 18 GB) 。默认上下文长度为 16,384 个 Token ，最高可扩展至 131,072 个 Token 。
* **硬件门槛：** 仅需 1 张 CUDA GPU 即可运行 bf16 权重 (在 24 GB 显存的 A10G 上通过实测) ；其 Q8_0 量化版本的 GGUF 文件 (~9.5 GB) 还可在 Apple Silicon 芯片与标准 CPU 上高效运转。
* **综合性能：** 在公开的 Decision Index 0.3.1 基准测试中斩获 **58.08 分** ，与顶级闭源模型 Jev 1.13.0 (57.96 分) 处于完全相同的并列领先梯队。
* **核心优势：** 在长文档处理场景中表现卓越 (在 32K 至 128K Token 长度下达到 **93.4% 的超高准确率**) 。
* **主要短板：** 在宽泛的通用世界知识测试 (例如 GPQA Diamond) 以及细粒度情感分析任务上表现相对吃力。

> * **Size:** 8.95B dense parameters (bf16 weights approx. 18 GB). Default context of 16,384 tokens, scaling up to 131,072 tokens.
> * **Hardware Requirements:** Runs on 1 CUDA GPU in bf16 (tested on a 24 GB A10G). A Q8_0 GGUF (~9.5 GB) runs efficiently on Apple Silicon and standard CPUs.
> * **Performance:** Scores **58.08** on Decision Index 0.3.1 (public), placing it squarely within the tie band of Jev 1.13.0 (57.96).
> * **Strengths:** Exceptional performance on long-document processing (**93.4% accuracy** on 32K–128K tokens).
> * **Weaknesses:** Struggles with broad general knowledge (e.g., GPQA Diamond) and fine-grained sentiment analysis tasks.

---

## 什么是 Drex 1.5？

> ## What is Drex 1.5?

Drex 1.5 是一款专精于决策判断的轻量级模型，其核心特点是在单次前向传播中直接为一组固定选项进行概率打分。用户向模型输入一段状态描述 `state` (支持纯文本或 JSON 格式) 以及具名的问题。它支持三类不同的问题类型：
* `choice` (多选一选择题)
* `noul` (是/否二元判定)
* 序数型 `score` (等级评分)

> Drex 1.5 is a specialized decision model that scores a fixed set of options in a single forward pass. Users input a `state` (text or JSON) alongside named questions. It supports three distinct question types:
> * `choice`
> * `noul` (yes/no)
> * Ordinal `score`

由于在推理阶段完全不需要采样生成任何 Token ，因此像采样温度 `temperature` 与核采样 `top_p` 这类超参数对它完全不适用。该模型被严格限制为只能基于预先给定的选项进行评估作答，从根本上杜绝了天马行空的幻觉。

> Because no tokens are sampled during inference, parameters like `temperature` and `top_p` do not apply. The model is strictly constrained to answering using the provided options.

在接口兼容性方面，Drex 1.5 提供了标准的 `POST /v1/systemone` API 接口——这与 TypeSafe AI 旗下 Jev 所开创的请求规范完全一致。这意味着现有基于 Jev 构建的客户端应用，只需简单修改环境变量中的服务地址，就能无缝迁移至 Drex 1.5。

> It serves the `POST /v1/systemone` API—the same request format pioneered by TypeSafe’s Jev—allowing existing Jev clients to migrate simply by updating environment variables.

---

## Drex 1.5 的底层架构与工作原理

> ## How Does Drex 1.5 Work?

Drex 1.5 的基座骨干网络采用了 **MiMo-V2.6-Distill-Qwen-9B** (源自 Qwen 3.5 9B 的知识蒸馏变体) ，整网包含 32 层结构并引入了混合注意力机制 (Hybrid Attention ，即每 1 层全注意力层搭配 3 层线性注意力层) 。在该骨干网络之上，挂载了一个专用的指针头部 (`head.pt`) ，它能直接基于骨干网络输出的隐藏状态向量 (Hidden States) 对每一个候选选项进行打分。

> The model's backbone is **MiMo-V2.6-Distill-Qwen-9B** (a distilled variant of Qwen 3.5 9B), featuring 32 layers with hybrid attention (3 linear-attention layers per full-attention layer). A specialized pointer head (`head.pt`) scores each option based on the backbone's hidden states.

在处理流程上，针对每个问题，模型仅需对“状态内容与该特定问题拼接后的序列”执行单次前向推理。借助 `llama.cpp` 的推理优化，复杂的状态上下文只需被编码一次，即可高效地在多个并行提问之间共享复用，大幅削减了重复计算开销。

> Each question executes a single pass over the state combined with that specific question. Using `llama.cpp`, the state is encoded once and efficiently shared across multiple questions.

---

## 性能表现与基准测试

> ## Performance & Benchmarks

在公开的 **Decision Index 0.3.1** 基准测试 (涵盖 37 项校正随机概率后的严苛基准任务) 中，Drex 1.5 稳居 10B 以下参数量规模模型的榜首：

> On the public **Decision Index 0.3.1** (comprising 37 chance-corrected benchmarks), Drex 1.5 competes at the very top of the sub-10B parameter category:

* **Drex 1.5：** 58.08 分
* **Jev 1.13.0：** 57.96 分
* **Bespoke Nimble 9B v3：** 57.19 分
* **Cloudflare clef-flash：** 56.15 分

> * **Drex 1.5:** 58.08
> * **Jev 1.13.0:** 57.96
> * **Bespoke Nimble 9B v3:** 57.19
> * **Cloudflare clef-flash:** 56.15

### 核心性能亮点

> ### Key Performance Highlights:

* **超长文本处理：** 在长文本语境下展现出顶尖的判断水准：
  * *8K 至 32K Token 长度：* 达到 89.5% 的准确率 (耗时中位数为 0.65 秒)
  * *32K 至 128K Token 长度：* 达到 93.4% 的超高准确率 (耗时中位数为 2.0 秒)
* **博弈对抗决策：** 在涵盖 8 款 OpenSpiel 经典博弈游戏的正面交锋评测中，Drex 面对商业劲敌 Jev 斩获了 122 胜、47 平、87 负的战绩 (胜率达 56.8%) 。

> * **Long Documents:** Exhibits elite performance on lengthy texts:
>   * *8K to 32K tokens:* 89.5% accuracy (median 0.65s)
>   * *32K to 128K tokens:* 93.4% accuracy (median 2.0s)
> * **Game Theory:** In head-to-head evaluations across 8 OpenSpiel games, Drex secured 122 wins, 47 draws, and 87 losses against Jev (56.8% win rate).

---

## 开发者如何部署与运行 Drex 1.5

> ## How Developers Can Run Drex 1.5

目前主要有四种主流的本地与云端部署途径：
1. **Python (基于 Kev 运行时) ：** 直接在配备 CUDA 的 GPU 环境中原生运行 `inference.py` 推理脚本与 `serve.py` 服务程序。
2. **llama.cpp：** 使用 Nace 专门定制的 fork 分支，在 CUDA、Metal 或 CPU 架构上加载 bf16 或 Q8_0 量化格式的 GGUF 权重。
3. **Ollama：** 通过 Nace 的专用 fork 分支进行部署，该版本内置了原生的 `decision` 决策交互能力。
4. **托管 API 云服务：** 现已接入 **OpenRouter** (由 DeepInfra 提供算力驱动，价格仅为每 100 万输入 Token 收费 0.04 美元，输出 Token 费用为 0 美元) ，也可直接使用 Nace 官方的 Console API 服务。

> There are four primary deployment pathways:
> 1. **Python (Kev runtime):** Run `inference.py` and `serve.py` natively on a CUDA GPU.
> 2. **llama.cpp:** Utilize Nace’s custom fork supporting GGUF in bf16 or Q8_0 across CUDA, Metal, or CPU.
> 3. **Ollama:** Deploy via Nace's fork which introduces native `decision` capabilities.
> 4. **Hosted APIs:** Available via **OpenRouter** ($0.04 per 1M input tokens, $0 output) powered by DeepInfra, or directly through Nace’s Console API.

此外，官方还提供了一款 **Drex 智能体技能 (Agent Skill)** ，能够无缝接入各类流行的 AI 编程辅助工具中，包括 Claude Code、Cursor、Codex、OpenCode、Hermes Agent、Gemini CLI 以及 GitHub Copilot 等。

> Additionally, a **Drex agent skill** seamlessly integrates the model into coding environments like Claude Code, Cursor, Codex, OpenCode, Hermes Agent, Gemini CLI, and GitHub Copilot.

---

## 主流决策模型特性横向对比

> ## Model Comparison

| 特性维度 | Drex 1.5 | Jev 1.13.0 | Bespoke Nimble 9B v3 |
| :--- | :--- | :--- | :--- |
| **研发机构** | Nace.AI | TypeSafe AI | Bespoke Labs |
| **模型参数量** | 8.95B | 未公开 | 基于 Qwen3.5-9B 的 LoRA 适配器 |
| **权重开放状态** | 完全开源 | 闭源 (仅提供 API) | 开源 (仅提供 Adapter 适配器) |
| **开源许可协议** | Nace.AI Open RAIL-M | 商业私有 | CC BY-NC 4.0 |
| **上下文窗口** | 默认 16,384 (最高可达 131,072) | 单次请求 64K | 未公开 |
| **Decision Index 0.3.1 得分** | **58.08** | 57.96 | 57.19 |
| **本地硬件要求** | 1 张 CUDA GPU / Apple Silicon / CPU | 不支持本地部署 | Qwen3.5-9B 基座 + Adapter |
| **API 价格 (每 100 万输入/输出 Token)** | $0.04 / $0 (OpenRouter) | $0.042 / $0 | 未公开 |

---

## 模型局限性与使用边界

> ## Limitations

* **无法生成自然语言文本：** Drex 1.5 的定位是纯粹的决策判断层；它无法像常规大模型那样自由输出自然语言对话、编写通用代码，也无法展开解释其决策推理过程。
* **常识与学科知识储备有限：** 在考察深厚学科常识与密集知识储备的学术基准测试中表现相对较弱，在 GPQA Diamond 上的准确率仅为 45.4% (相比之下 Jev 达到 78.6%) ，在 MMLU-Pro 上的得分也仅为 58.7% 。
* **生态依赖与协议约束：** 目前基于 Ollama 和 llama.cpp 的本地运行仍依赖于官方定制的 fork 分支，尚未合入上游主线代码库；此外，商业用户在落地部署时需注意遵守 RAIL-M 许可证中的各项附加使用规范。

> * **No Text Generation:** Drex 1.5 is strictly a decision layer; it cannot generate natural language text, write general code, or explain its reasoning.
> * **Knowledge Constraints:** Struggles with knowledge-heavy academic benchmarks, scoring 45.4% on GPQA Diamond (compared to Jev's 78.6%) and 58.7% on MMLU-Pro.
> * **Ecosystem Dependencies:** Local deployments through Ollama and llama.cpp currently rely on specialized forks rather than mainline builds. Commercial users must review the constraints of the RAIL-M license.

---

## 总结与核心要点

> ## Key Takeaways

* **专注垂直决策场景：** Drex 1.5 是一款参数量为 9B 级别的开源专用决策模型，旨在通过单次前向推理对显式选项直接打分，完全跳过了文本生成的繁冗计算。
* **比肩顶级闭源性能：** 在 Decision Index 0.3.1 基准测试中取得 58.08 分的佳绩，完全追平了顶尖商业闭源竞争对手 Jev 1.13.0 。
* **出色的长文本驾驭力：** 在 32K 至 128K Token 的超长上下文场景下，其选项判别准确率高达 93.4% 。
* **极低的部署与硬件门槛：** 既能在单张标准 GPU 上高效运行，也可通过 GGUF 量化格式在 Apple Silicon 与通用 CPU 上轻松实现纯本地部署。

> * **Specialized Purpose:** Drex 1.5 is a 9B open decision model engineered to score explicit options in a single forward pass rather than generating text.
> * **Competitive Edge:** Matches closed-source alternatives like Jev 1.13.0 with a score of 58.08 on Decision Index 0.3.1.
> * **Context Handling:** Delivers up to 93.4% accuracy on ultra-long documents (32K–128K tokens).
> * **Accessibility:** Highly deployable on standard single-GPU setups or localized hardware via GGUF formats.

---

*欢迎访问 [Hugging Face 上的模型权重](https://huggingface.co/nace-ai/drex-v1.5) 、 [GitHub 代码仓库](https://github.com/nace-ai/drex-decision-models) 以及官方 [Drex 产品主页](https://www.nace.ai/drex) 获取更多技术细节与实操资源。*

> *Check out the [Model Weights on Hugging Face](https://huggingface.co/nace-ai/drex-v1.5), the [GitHub Repository](https://github.com/nace-ai/drex-decision-models), and the official [Drex Product Page](https://www.nace.ai/drex).*
