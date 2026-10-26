---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-10-27
hide:
- navigation
tags:
- SGLang
- AKV
- KV Cache
- AI 智能体
- 清华大学
title: 清华团队开源 AKV：基于 SGLang 的大模型智能体 KV 缓存工程服务系统
---
# 清华团队开源 AKV：基于 SGLang 的大模型智能体 KV 缓存工程服务系统

> # Tsinghua AI Open-Sources AKV, a Cache Engineering Server for LLM Agents on SGLang

### 文章背景与核心概要

在大模型智能体 (AI Agent) 频繁调用工具、执行多轮长程推理的过程中，不断膨胀的上下文历史使得键值缓存 (KV Cache) 显存开销居高不下，而传统的文本截断或总结不仅会破坏中间推理细节，更会引发高昂的二次重新预填充 (Re-prefill) 开销。针对这一制约智能体工业化落地的核心瓶颈，清华大学 (Tsinghua University) 与香港中文大学 (CUHK) 联合开源了专为智能体打造的缓存工程服务系统 AKV (Agent KV Cache Server) 。AKV 独辟蹊径地提出了“缓存工程”范式，直接在底层推理引擎中对 KV 缓存进行细粒度的动态丢弃与位置重排，而完全无需改动上层文本轨迹。在多项复杂智能体基准测试中，基于 SGLang 构建的 AKV 不仅将平均运行成本大幅削减了 27.7%，更将任务解决率逆势提升了 1.7 个百分点，在高并发场景下将 P95 延迟缩短了数倍，为长上下文智能体的高效低成本服务提供了突破性的全栈工程范式。

---

清华大学 (Tsinghua University) 与 CUHK 的研究团队正式开源了 **AKV**——一套专为大语言模型 (Large Language Model, LLM) 智能体 (AI Agent) 打造的创新型键值缓存 (KV Cache) 工程服务系统。与以往频繁压缩或粗暴裁剪对话历史的做法不同，AKV 赋予了智能体动态剔除特定 KV 缓存条目并高能效复用剩余缓存的硬核能力。在多种主流模型和复杂的智能体基准测试 (Benchmark) 中，这一创新方案将平均运行成本降低了 **27.7%**，同时将任务综合得分提升了 **1.7 分**。该系统基于高性能推理框架 **SGLang** 深度构建，目前已在 **Apache-2.0 协议** 下全面开源。

> Researchers from Tsinghua University and CUHK have open-sourced **AKV**, an innovative serving system designed for KV cache engineering in LLM agents. Instead of summarizing or trimming old conversation history, agents can dynamically drop selected KV cache entries and reuse the remainder. Across multiple models and agent benchmarks, this method reduces average operating costs by **27.7%** while increasing average task scores by **1.7 points**. Built on top of **SGLang**, the code is available under the **Apache-2.0 license**.

---

## 📌 执行摘要

> ## 📌 Executive Summary

* **项目定位**：一套专用的推理服务系统与缓存策略库 (不包含模型权重)。已在 GPT-OSS-120B (激活参数 5.1B)、MiniMax-M2.7 (总参数 230B，激活参数 10B) 以及 MiroThinker-1.7-Mini (总参数 30B，激活参数 3B) 等前沿模型上完成系统验证。
* **硬件要求**：依托 SGLang 运行于 NVIDIA GPU 之上。原论文研究在 BF16 精度下使用了 8 张 A800-80GB GPU，而快速上手部署仅需 2 张 GPU 即可运行 GPT-OSS-120B (张量并行度 Tensor Parallelism = 2)。
* **性能收益**：相较于传统的阈值摘要机制，实现了平均成本降低 27.7%，平均任务得分提升 1.7 分的亮眼表现。
* **最佳应用场景**：在 SWE-bench Verified 软件工程基准测试中运行 GPT-OSS-120B (单任务平均成本从 20.0 美分骤降至 9.7 美分，同时得分从 40.0 逆势跃升至 43.2)。
* **已知局限**：MiniMax-M2.7 在 BrowseComp-Plus 网页检索测试中得分为 58.9，比传统文本工程策略的 62.3 分低 3.4 分。

> * **What it is:** A specialized serving system and policy library (weights not included). It has been tested on models such as GPT-OSS-120B (5.1B active), MiniMax-M2.7 (230B total, 10B active), and MiroThinker-1.7-Mini (30B total, 3B active).
> * **Hardware Requirements:** Runs on NVIDIA GPUs via SGLang. The research paper utilized 8× A800-80GB GPUs in BF16, while quick-start deployments can serve GPT-OSS-120B on just 2 GPUs (tensor parallelism = 2).
> * **Performance Gains:** Achieves a 27.7% reduction in average cost and a +1.7 point improvement in average scores compared to traditional threshold summarization.
> * **Best Use Case:** GPT-OSS-120B on SWE-bench Verified (reducing cost per task from 20.0¢ to 9.7¢ while raising scores from 40.0 to 43.2).
> * **Current Limitations:** MiniMax-M2.7 on BrowseComp-Plus scored 58.9, which is 3.4 points lower than Text Engineering's 62.3.

---

## 什么是缓存工程与上下文工程？

> ## What is Cache Engineering vs. Context Engineering?

**AKV** 开创性地引入了一种全新服务范式，允许大语言模型智能体自主决定丢弃与重排底层的 KV 缓存状态。

> **AKV** introduces a serving paradigm that allows LLM agents to autonomously drop and reposition their own KV cache states. 

传统的**上下文工程 (Context Engineering)** 往往依赖对文本历史的暴力裁剪或文本摘要。然而，在大模型自注意力机制中，任何对文本前缀 (Prefix) 的修改都会直接导致后续所有已生成的 KV 缓存状态彻底失效，迫使系统不得不对保留下来的后缀 (Suffix) 进行耗时费电的重新预填充 (Re-prefill)。正因如此，现有的智能体编排框架通常只能采取“滞后且激进”的摘要策略，这极易抹杀中间推理步骤中至关重要的细粒度细节。

> Traditional **context engineering** relies on trimming or summarizing text history. However, editing prefixes invalidates all subsequent KV states, forcing the system to re-prefill the retained suffix. As a result, agent harnesses often summarize late and aggressively, leading to a loss of granular details from intermediate reasoning steps.

与此相反，**缓存工程 (Cache Engineering)** 完全不破坏底层的原始文本对话轨迹。它通过精细调控哪些 KV 缓存条目对后续的注意力机制保持可见，在无需任何重新计算的情况下直接复用保留下来的条目；即便前序的某些消息条目已被剔除，依然能够无损继承关键上下文。在研究人员的真实调用成本剖析中，KV 缓存的重复读取开销在整个 API 支出中竟然占据了惊人的 82.4%。

> **Cache engineering**, conversely, leaves the underlying text trajectory completely untouched. It selectively adjusts which KV entries remain visible to attention mechanisms. Retained entries are reused without recomputation and can preserve context even when preceding messages are pruned. In the researchers' cost analysis, KV cache reads accounted for a staggering 82.4% of total API expenses.

---

## AKV 是如何工作的？

> ## How Does AKV Work?

AKV 明确定义了三项核心缓存操作：

> AKV defines three core cache operations:

1. **追加 (Append)**：针对新生成 Token 的标准缓存更新机制。
2. **丢弃 (Drop)**：将指定的条目从后续注意力计算的可见范围中剔除，同时保持位置索引完全不变。
3. **重排 (Repos / Repositioning)**：利用 [RoPE 旋转位置编码 (RoPE Rotation)](https://arxiv.org/abs/2104.09864) 将保留下来的 Key 重新编码映射到位置 $0$ 至 $r-1$。在此过程中，Value 保持完全不变，从而确保隐藏状态的二次重算开销为零。在消融实验中，引入 `Repos` 机制直接使 GPT-OSS-120B 在 BrowseComp-Plus 上的任务通过率从 55% 大幅跃升至 62%。

> 1. **Append:** The standard update mechanism for newly generated tokens.
> 2. **Drop:** Removes targeted entries from future attention scopes without altering position indices.
> 3. **Repos (Repositioning):** Rewrites retained keys to positions $0$ through $r-1$ using [RoPE rotation](https://arxiv.org/abs/2104.09864). Values remain completely unchanged, ensuring zero recomputation of hidden states. In ablation studies, incorporating `Repos` boosted GPT-OSS-120B’s BrowseComp-Plus pass rate from 55% to 62%.

### 服务端创新技术

> ### Serving Innovations

要在高吞吐服务端动态处理这些操作极具挑战性，因为完全相同的 Token 序列在不同的操作历史下可能会产生截然不同的缓存状态。如果仍沿用常规的前缀匹配机制，系统极有可能会误用错误的缓存状态。

> Handling these operations dynamically is challenging because identical tokens can yield divergent cache states under different operation histories. Conventional prefix-matching would otherwise reuse incorrect states. 

为攻克这一难题，AKV 对 SGLang 的基数树 (Radix Tree) 进行了深度扩展，新增了专门的丢弃与重排节点。被丢弃的 KV 条目只会在没有任何活跃请求对其产生依赖时才被真正从显存中释放；同时，分段批量注意力 (Segment-Batch Attention) 机制能够在单次预填充遍历中快速复原已被逐出的状态。

> To solve this, AKV extends SGLang’s radix tree with specialized drop and reposition nodes. Dropped KV entries are only freed when no active requests depend on them, while segment-batch attention restores evicted states in a single prefill pass.

---

## AKV API 接口设计

> ## The AKV API Interface

该 API 采用无状态设计且[兼容 OpenAI 标准](https://github.com/thu-nics/AKV/blob/main/akv/system/README.md)。客户端在传递全量消息历史的同时，仅需额外附带两个可选字段：

> The API is stateless and [OpenAI-compatible](https://github.com/thu-nics/AKV/blob/main/akv/system/README.md). Clients pass the full message history alongside two optional fields:

* `drop_message`：将触发消息的索引映射到拟定移除的特定消息集合。
* `reposition`：列出需要进行位置紧凑化重排的索引边界。

> * `drop_message`: Maps a trigger message index to the specific messages slated for removal.
> * `reposition`: Lists the indices after which positions are compacted.

系统通过 `CachePolicy` (缓存策略) 模块，利用触发器 (Trigger)、选择器 (Selector) 和重排规则 (Reposition Rule) 来自动构建这些参数。内置策略全面支持基于话轮 (Turn-based)、基于 Token 数量 (Token-based) 以及基于模型启发式规则 (Model-based) 的多种调度方式。此外，系统还提供了一个专用的 [`CacheTool`](https://github.com/thu-nics/AKV/blob/main/akv/agent/policies/tools.py) 工具，允许模型自身根据推理状态自主发起 `drop_context` 工具调用。

> A `CachePolicy` constructs these parameters using a trigger, a selector, and a reposition rule. Built-in policies support turn-based, token-based, or model-based heuristics. Additionally, a [`CacheTool`](https://github.com/thu-nics/AKV/blob/main/akv/agent/policies/tools.py) enables models to dynamically call `drop_context` directly.

---

## 智能体基准测试性能表现

> ## Agent Benchmark Performance

评测中的基准策略采用了“工具响应滑动丢弃”方案，默认仅保留最近 12 次工具调用的输出结果。**标准 (Standard)** 基线在上下文达到 96K Token 时触发文本摘要 (MiroThinker 模型为 192K Token)，而**文本工程 (Text Engineering)** 基线则在 48K Token 时提前触发摘要。评估测试覆盖了 [BrowseComp-Plus](https://arxiv.org/abs/2508.06600)、[GAIA-Text](https://arxiv.org/abs/2311.12983)、[SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) 以及 [xbench-DeepSearch-2510](https://huggingface.co/datasets/xbench/DeepSearch-2510) 四大主流前沿基准。

> The primary baseline strategy uses a tool-response rolling drop that preserves the latest 12 tool outputs. The **Standard** baseline summarizes at 96K tokens (192K for MiroThinker), whereas **Text Engineering** summarizes at 48K tokens. Evaluations were performed across [BrowseComp-Plus](https://arxiv.org/abs/2508.06600), [GAIA-Text](https://arxiv.org/abs/2311.12983), [SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/), and [xbench-DeepSearch-2510](https://huggingface.co/datasets/xbench/DeepSearch-2510).

| 模型 (Model) | 标准基线 得分 / 成本 (Standard Score / Cost) | 文本工程 得分 / 成本 (Text Eng. Score / Cost) | AKV 得分 / 成本 (AKV Score / Cost) |
| :--- | :--- | :--- | :--- |
| **MiniMax-M2.7** | 52.4 / 5.0¢ | 52.8 / 5.7¢ | **53.7 / 4.4¢** |
| **GPT-OSS-120B** | 51.0 / 11.2¢ | 48.3 / 10.2¢ | **53.1 / 7.3¢** |
| **MiroThinker-1.7-Mini** | 44.1 / 20.4¢ | 37.1 / 18.1¢ | **45.8 / 14.8¢** |

*4 项基准测试下的平均通过率 (%) 与平均单任务成本 (美分)。数据来源：[论文表 1](https://arxiv.org/html/2610.28577v1)。*

> *Average pass rate (%) and cost (US cents per task) across 4 benchmarks. Source: [Table 1 of the paper](https://arxiv.org/html/2610.28577v1).*

相比文本工程基线，AKV 将运行成本进一步削减了 21.9%，且随着任务执行周期的拉长，准确率差距进一步扩大。在 BrowseComp-Plus (96K+ Token 超长上下文场景) 中，使用 AKV 的 GPT-OSS-120B 斩获了 37% 的任务通过率，显著优于标准基线的 24% 与文本工程基线的 32%。

> AKV reduces costs by 21.9% compared to Text Engineering, with the accuracy gap widening during long-running tasks. On BrowseComp-Plus (at 96K+ tokens), GPT-OSS-120B achieved a 37% pass rate with AKV, compared to 24% for Standard and 32% for Text Engineering.

---

## 推理服务速度与吞吐量评估

> ## Serving Speed and Throughput

服务性能评测针对 GPT-OSS-120B 在 80 个超长上下文 SWE-bench Verified 真实任务上展开：

> Serving evaluations tested GPT-OSS-120B across 80 long-context SWE-bench Verified tasks:

* **吞吐量表现**：在峰值配置下，AKV 实现了 **1.18 倍的输出吞吐量提升** 以及 **1.53 倍的输入吞吐量提升**。
* **延迟优化**：P95 请求延迟改善了 **1.51 倍**。在并发度为 16 的重压场景下，标准基线因显存压力触发频繁的重新预填充，导致 P95 延迟骤升至 229.90 秒；而 AKV 则始终保持高度稳定，P95 延迟仅为 30.63 秒。
* **注意力开销**：每个解码 (Decode) 步的全量注意力计算时间由原先的 7.082 毫秒大幅压缩至 2.849 毫秒。

> * **Throughput:** At peak settings, AKV achieves **1.18x higher output throughput** and **1.53x higher input throughput**.
> * **Latency:** P95 request latency improves by **1.51x**. At a concurrency level of 16, Standard’s P95 latency spikes to 229.90 seconds due to repeated re-prefill overheads under KV pressure, whereas AKV remains stable at 30.63 seconds.
> * **Attention Cost:** Full attention computation time per decode step drops from 7.082 ms down to 2.849 ms.

---

## 智能体自主调优与动态掌控

> ## Agent Self-Tuning and Autonomy

MiniMax-M2.7 展现出了强大的缓存策略自主迭代能力：在 20 个 BrowseComp-Plus 任务中完成自主调优后，部署于 100 个保留测试任务上。经过 6 轮迭代所生成的策略在保持基线精度的同时，将运行成本显著降低了 17.8%。

> MiniMax-M2.7 demonstrated the ability to refine its cache policies across 20 BrowseComp-Plus tasks before deployment on 100 held-out tasks. The resulting iteration-6 policy reduced operating costs by 17.8% while matching baseline accuracy. 

将缓存控制权作为智能体可直接调用的主动工具，同样带来了显著的精度提升：在 100 个任务子集上，GPT-OSS-120B 的得分从 52.1 跃升至 61.0 (尽管 MiniMax-M2.7 的成本出现轻微上升，从 5.4 美分微增至 5.9 美分)。

> Exposing cache control as an active agent tool also yielded accuracy gains: GPT-OSS-120B improved from 52.1 to 61.0 on a 100-task subset (though MiniMax-M2.7 experienced a minor cost increase from 5.4¢ to 5.9¢).

---

## 特性对比：AKV 与其他主流 KV 缓存技术方案

> ## Feature Comparison: AKV vs. Other KV Cache Approaches

| 指标维度 (Metrics) | [AKV](https://github.com/thu-nics/AKV) | 阈值摘要 (Threshold Summarization) | [SGLang RadixAttention](https://github.com/sgl-project/sglang) | [StreamingLLM](https://github.com/mit-han-lab/streaming-llm) | [SnapKV](https://arxiv.org/abs/2404.14469) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **作用机制** | 智能体导向的 KV 缓存 | 文本历史裁剪 | KV 缓存前缀复用 | 固定窗口 KV 缓存 | Prompt 提示词 KV 缓存 |
| **剔除内容** | 由策略或工具调用动态判定 | 超过 Token 阈值的旧历史 | 无 (复用共享前缀) | 中间 Token (保留注意力汇元与最新 Token) | 低注意力权重的 Prompt 位置 |
| **是否需要重新预填充？** | **否 (No)** | 是 (保留的后缀需重新预填充) | 不适用 (Not Applicable) | 无需刷新缓存 | 不适用 (Not Applicable) |
| **目标工作负载** | 多轮工具调用的 AI 智能体 | 智能体编排框架 | 通用与智能体推理服务 | 流式长对话 | 长文本 Prompt |
| **官方核心战报** | 成本降低 27.7%，得分提升 1.7 分 | AKV 论文基线 | 吞吐量最高提升 6.4 倍 | 相比滑动窗口重算最高提速 22.2 倍 | 16K 长度下生成速度提升 3.6 倍 |
| **支持模型架构** | Qwen, GPT-OSS, MiniMax-M2 | 任意模型 | 广泛支持主流模型 | Llama-2, MPT, Falcon, Pythia | Llama, Mistral, Mixtral |
| **开源许可证** | [Apache-2.0](https://github.com/thu-nics/AKV/blob/main/LICENSE) | 取决于具体编排框架 | [Apache-2.0](https://github.com/sgl-project/sglang) | [MIT](https://github.com/mit-han-lab/streaming-llm) | [Apache-2.0](https://github.com/FasterDecoding/SnapKV) |

---

## 核心要点总结

> ## Key Takeaways

* AKV 赋予了智能体直接剔除与重排底层 KV 缓存的自主能力，彻底告别了传统反复重写或裁剪文本历史的高开销方案。
* 在三个已评测的模型家族中，AKV 将平均运行成本降低了 27.7%，同时将基准任务综合得分提升了 1.7 分。
* 创新的 `Repos` 旋转重排优化，使 GPT-OSS-120B 在 BrowseComp-Plus 评测上的任务通过率从 55% 跃升至 62%。
* 在高并发重压场景 (例如 16 个并发请求) 下，P95 延迟从 229.90 秒断崖式削减至 30.63 秒。
* 当前支持的模型架构主要覆盖 Qwen、GPT-OSS 以及 MiniMax-M2 系列模型。

> * AKV empowers agents to directly drop and reposition their KV cache rather than continuously rewriting text history.
> * Reduces average operating costs by 27.7% and improves task scores by 1.7 points across three evaluated model families.
> * `Repos` optimization boosts GPT-OSS-120B performance on BrowseComp-Plus from 55% to 62%.
> * Under high concurrency (e.g., 16 concurrent requests), P95 latency is slashed from 229.90s down to 30.63s.
> * Current text architecture support is restricted to Qwen, GPT-OSS, and MiniMax-M2 models.

---

## 相关资源与链接

> ## Resources & Links

* 📄 **研究论文**：[arXiv:2610.28577](https://arxiv.org/abs/2610.28577)
* 💻 **GitHub 仓库**：[thu-nics/AKV](https://github.com/thu-nics/AKV)
* 🌐 **项目主页**：[Thinking Yard 项目主页](https://fuvty.github.io/thinking_yard_project_page/projects/akv/)

> * 📄 **Research Paper:** [arXiv:2610.28577](https://arxiv.org/abs/2610.28577)
> * 💻 **GitHub Repository:** [thu-nics/AKV](https://github.com/thu-nics/AKV)
> * 🌐 **Project Page:** [Thinking Yard Project Page](https://fuvty.github.io/thinking_yard_project_page/projects/akv/)
