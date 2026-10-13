---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-13
hide:
  - navigation
tags:
  - Cloudflare
  - Clef-omni
  - 决策模型
  - 多模态
title: "Cloudflare 正式发布 Clef-omni：支持音视频与图文的全模态 30B 决策大模型"
---

# Cloudflare 正式发布 Clef-omni：支持音视频与图文的全模态 30B 决策大模型

> # Meet Cloudflare Clef-omni: A 30B-A3B Multimodal Decision Model for Audio, Video, Image and Text

### 文章背景与核心概要

随着大语言模型 (Large Language Model, LLM) 和 AI 智能体 (AI Agent) 在企业生产环境的广泛落地，开发者越来越频繁地需要让模型在海量复杂数据中做出精准、低延迟的业务决策。然而，传统的生成式模型不仅逐字生成文本缓慢、成本高昂，且难以同时原生地理解音频与动态视频等多媒体流。为此，Cloudflare 正式发布了开源权重的全模态决策模型 **Clef-omni** 。该模型基于混合专家架构 (Mixture-of-Experts, MoE) ，总参数量为 30B 、激活参数量仅为 3B ，能够通过单次 API 调用直接对文本、图像、音频和视频四种模态进行联合概率打分，无需预先进行繁琐的音视频转录与字幕提取。这一创新不仅将多模态决策延迟压缩至百毫秒级，还将推理成本大幅降低，为下一代高并发多模态智能体路由与自动化后端系统树立了全新的技术标杆。

---

## 概述

> ## Summary

Cloudflare 正式扩展了其 Clef 决策模型 (Decision Model) 家族，重磅推出开源权重的多模态决策模型 **Clef-omni** 。该模型采用混合专家架构 (Mixture-of-Experts, MoE) ，总参数量为 30B ，实际激活参数仅为 3B 。Clef-omni 基于 `Qwen3-Omni-30B-A3B-Instruct` 构建，能够在单次 API 调用中同时对文本、图像、音频和视频进行精准打分，彻底免去了以往必须先做语音转录 (Transcription) 和视频字幕提取 (Captioning) 的繁琐前置环节，极大简化了开发者的工程处理链路。Clef-omni 目前已在 Cloudflare Workers AI 平台上线，遵循 Apache-2.0 开源许可协议；与此同时，Cloudflare 还宣布对轻量级模型 Clef-flash 进行大幅降价，并通过深度集成推理引擎 SGLang ，使托管版 Clef 系列模型的推理速度直接翻倍提升。

> Cloudflare has expanded its Clef decision model family with the release of **Clef-omni**, an open-weight, 30B total / 3B active parameter Mixture-of-Experts (MoE) multimodal decision model. Built on top of `Qwen3-Omni-30B-A3B-Instruct`, Clef-omni is capable of scoring text, images, audio, and video in a single API call, streamlining developer pipelines by eliminating the need for preliminary transcription and captioning steps. Available on Cloudflare Workers AI and licensed under Apache-2.0, this release coincides with significant price cuts for Clef-flash and a 2x speed improvement for hosted Clef models via SGLang integration.

---

## 核心速览 (TL;DR)

> ## TL;DR

* **模型规模：** 总参数量 30B ，激活参数量 3B (MoE 架构) ；在 Workers AI 平台上提供高达 64,000 个 Token 的上下文窗口。
* **运行环境：** 支持在 Workers AI 平台直接调用，模型标识为 `@cf/cloudflare/clef-omni` ；实测可在单张 NVIDIA H200 上完成私有化部署 (bfloat16 精度下占用显存约 64 GB) 。
* **综合性能：** 在意图分类与任务路由等场景下表现优异；但在高难度复杂推理与工作流评估任务中，略逊于标准文本版 Clef 模型。
* **最佳战绩：** 在 CLINC150+OOS 基准测试 (Benchmark) 中斩获 97.7 的宏平均 F1 分数 (Macro-F1) ，在 Clef 系列与 Jev 系列共四款对比模型中位列榜首。
* **短板弱项：** 在音乐结构分析基准 POP909-CL 上的准确率仅为 2.6 ，在权威专家级问答基准 GPQA Diamond 上的准确率为 47.4 (作为对比，Jev 模型得分高达 78.3) 。
* **总结评价：** 
  * *优势：* 只需单次调用即可跨越 4 种不同模态完成统一的概率决策。
  * *劣势：* 在严苛的纯逻辑深度推理任务上，准确率稍逊于专精文本的 Clef 变体。

> * **Size:** 30B total parameters, 3B active parameters (MoE); 64,000-token context on Workers AI.
> * **Runs on:** Workers AI as `@cf/cloudflare/clef-omni`; self-hosting tested on a single H200 (~64 GB GPU memory in bfloat16).
> * **Performance:** Excels on routing and intent tasks; trails standard Clef on complex reasoning and workflow evaluations.
> * **Best:** Achieves 97.7 macro-F1 on CLINC150+OOS (topping all four Clef and Jev models).
> * **Worst:** 2.6 accuracy on POP909-CL, and 47.4 on GPQA Diamond (compared to Jev's 78.3).
> * **Bottom Line:** 
>   * *Pros:* Makes unified decisions across 4 distinct modalities in a single call.
>   * *Cons:* Exhibits weaker accuracy than text-focused Clef variants on hard reasoning tasks.

---

## 什么是决策模型？

> ## What is a Decision Model?

与传统的生成式文本模型不同，决策模型并不会自由生成开放式自然语言文本，而是直接返回带有明确概率值的结构化答案。在实际使用中，用户只需传入一个状态对象 `state` 以及一组预先定义好的问题模式 (Schema) ，模型便会直接为每个候选选项输出置信度概率分数。Clef 支持[三类问题格式](https://huggingface.co/Cloudflare/clef-omni)：即 `noul` (判断真假，True/False) 、`choice` (单选或多选项评估) 和 `score` (连续分值评估) 。该输入输出格式完全兼容并遵循由 [TypeSafe AI](https://typesafe.ai/blog/introducing-system-one-models-and-jev) 制定的 Jev 与 SystemOne API 工业规范。

> Unlike traditional generative text models, a decision model returns typed answers accompanied by probabilities instead of free-form generated text. Users send a `state` object alongside a schema of questions, and the model responds with a probability score for every allowed option. Clef supports [three question types](https://huggingface.co/Cloudflare/clef-omni): `noul` (true or false), `choice`, and `score`. This format adheres to the Jev and SystemOne API standards introduced by [TypeSafe AI](https://typesafe.ai/blog/introducing-system-one-models-and-jev).

---

## Clef-omni 是如何工作的？

> ## How Does Clef-omni Work?

Clef-omni 是在开源多模态底座 [Qwen3-Omni-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct) 的基础上经过后训练 (Post-training) 优化而成的。Cloudflare 完整保留了该模型强大的核心多模态理解主干，同时剥离了耗费资源的语音合成 (Text-to-Speech) 输出通路。在执行推理时，模型仅需对输入的完整多模态载荷执行单次预填充处理 (Prefill Pass) ，将抽取的视频帧与音频片段精确对齐同步为一条统一的输入序列，进行深度联合计算。

> Clef-omni is post-trained from [Qwen3-Omni-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct). Cloudflare preserved the model's core comprehension backbone while dropping the text-to-speech output path. The model executes a single prefill pass over the entire payload, synchronizing video frames and audio into a unified sequence for joint processing.

随后，专门设计的联合模式头 (Joint Schema Head) 对所有选项进行精准概率评分。每个有效选项都会直接从多模态输入中提取关键证据，借助跨注意力机制 (Cross-Attention) 遍历全部上下文的字段向量，从而严密计算出最终的置信度评分。在模型微调方面，Cloudflare 冻结了 Qwen3 的底座参数，通过标签平滑交叉熵 (Label-Smoothed Cross-Entropy) 与布里尔分数校准 (Brier Score Calibration) 相结合的优化目标，训练了专属的 LoRA 适配层。

> A specialized joint schema head then scores the options. Each valid option gathers evidence directly from the input, utilizing field vectors that cross-attend across the full context to compute final confidence scores. Cloudflare froze the Qwen3 backbone and trained custom LoRA adapters using a combination of label-smoothed cross-entropy and Brier score calibration.

### Workers AI 平台支持的输入规格

> ### Supported Inputs on Workers AI

根据官方的[开发者文档](https://developers.cloudflare.com/workers-ai/models/clef-omni)说明：

> According to the [developer documentation](https://developers.cloudflare.com/workers-ai/models/clef-omni):

* **图像：** 最多支持 4 张 (格式支持 PNG、JPEG 或 WebP) ，每张图像占用 64 至 1,024 个 Token 。
* **音频：** 最多支持 4 段音频片段 (格式支持 WAV 或 MP3) ，单段音频时长上限为 300 秒 (每分钟音频大约消耗 780 个 Token) 。
* **视频：** 最多支持 2 段视频片段 (格式支持 MP4 或 WebM) ，单段视频时长上限为 60 秒，以每秒 2 帧的频率进行抽帧采样。
* **问题数量：** 单次请求可批量提交 1 到 64 个问题。

> * **Images:** Up to 4 (PNG, JPEG, or WebP), allocating 64 to 1,024 tokens each.
> * **Audio:** Up to 4 clips (WAV or MP3), up to 300 seconds each (~780 tokens per minute).
> * **Video:** Up to 2 clips (MP4 or WebM), up to 60 seconds each, sampled at 2 frames per second.
> * **Questions:** 1 to 64 per request.

在推理性能与延迟 (Latency) 方面，Cloudflare 官方公布的数据显示：纯文本决策的中位数延迟约为 130 毫秒，图像决策约为 150 毫秒；而针对一段长达 21 秒且附带完整音轨的复杂视频，整体多模态评估决策耗时仅需约 1.5 秒。

> Performance-wise, Cloudflare reports median text decision latencies of ~130 ms, images at ~150 ms, and a 21-second video with sound evaluated in approximately 1.5 seconds.

---

## 基准评测表现

> ## Benchmark Performance

Cloudflare 在其专门搭建的决策基准评估套件 [Decision Index](https://clef-evals.workers-ai-mle.workers.dev/) 上，将 Clef-omni 与标准版 Clef、轻量版 Clef-flash 以及 TypeSafe AI 的 Jev 进行了全方位横向对比。结果显示，Clef-omni 在意图分类任务上展现出压倒性的绝对优势：在金融意图测试集 BANKING77 上取得了 94.8 的宏平均 F1 分数，在多领域意图识别基准 CLINC150+OOS 上斩获了 97.7 的高分，同时在 Amazon ESCI 商品匹配基准测试中也以 57.8 分稳居榜首。

> Cloudflare evaluated Clef-omni against Clef, Clef-flash, and Jev using its proprietary [Decision Index](https://clef-evals.workers-ai-mle.workers.dev/). Clef-omni leads decisively in intent classification, scoring a 94.8 macro-F1 on BANKING77 and 97.7 on CLINC150+OOS, alongside leading Amazon ESCI at 57.8.

然而，在其他专业细分领域，Clef-omni 的表现则相对落后。在家用电器案例完全匹配测试 (Home appliances case-exact) 中，其准确率仅为 69.3 (而 Clef-flash 高达 97.73) ；在通信路由决策评测 When2Call 中，其准确率为 63.3 (而 Jev 则达到了 80.97) 。此外，在 [TypeSafe 的工作流评估](https://evals.typesafe.ai/) (Workflow Evaluations) 所涵盖的全部五项量化指标中，Clef-omni 的得分均全面低于专精文本的标准版 Clef 。

> However, it trails in other domains. Home appliances case-exact accuracy lands at 69.3 (compared to 97.73 for Clef-flash), and When2Call accuracy sits at 63.3 (versus 80.97 for Jev). On [TypeSafe’s workflow evaluations](https://evals.typesafe.ai/), Clef-omni scores lower than standard Clef across all five reported metrics.

---

## 模型全方位对比：Clef-omni vs. Clef vs. Clef-flash vs. Jev

> ## Model Comparison: Clef-omni vs. Clef vs. Clef-flash vs. Jev

| 特性维度 | [Clef-omni](https://huggingface.co/Cloudflare/clef-omni) | [Clef](https://huggingface.co/Cloudflare/clef) | [Clef-flash](https://huggingface.co/Cloudflare/clef-flash) | [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) |
| :--- | :--- | :--- | :--- | :--- |
| **研发机构** | Cloudflare | Cloudflare | Cloudflare | TypeSafe AI |
| **模型参数量** | 30B 总参数，3B 激活 (MoE) | 27B 稠密 | 9B 稠密 | 未公开 |
| **基座模型** | Qwen3-Omni-30B-A3B-Instruct | Qwen3.8-27B | Qwen3.5-9B | 未公开 |
| **支持输入模态** | 文本、图像、音频、视频 | 文本、图像、视频抽帧 | 文本、图像、视频抽帧 | 文本 (据 [Cloudflare](https://blog.cloudflare.com/clef-decision-models/) 报道) |
| **托管上下文窗口** | [64,000 个 Token](https://developers.cloudflare.com/workers-ai/models/clef-omni) | 64k | 24k (私有化部署支持 256k) | TypeSafe 未公开 (Cloudflare 引用为 32k) |
| **每百万输入 Token 价格** | [$0.15](https://developers.cloudflare.com/workers-ai/platform/pricing/) | $0.24 | $0.038 | $0.042 |
| **开源许可协议** | Apache-2.0 | Apache-2.0 | Apache-2.0 | 仅提供 API，早期预览阶段 |
| **BANKING77 (宏平均 F1)** | **94.8** | 94.20 | 90.93 | 79.74 |
| **CLINC150+OOS (宏平均 F1)** | **97.7** | 97.43 | 66.77 | 89.27 |
| **When2Call (准确率)** | 63.3 | 72.37 | 65.58 | **80.97** |
| **BRIGHT (nDCG@10)** | 42.0 | 45.91 | 39.26 | **47.52** |
| **发票处理首要操作 (Invoice processing, primary action)** | 82.0 | **86.2** | 73.3 | 83.1 |

*注：以上基准测试评分数据均源自 [Cloudflare 官方发布公告](https://blog.cloudflare.com/clef-faster-cheaper-multimodal/) ，尚未经过独立第三方的复现与验证。*

> *Note: Benchmark scores originate from [Cloudflare’s announcement](https://blog.cloudflare.com/clef-faster-cheaper-multimodal/) and have not been independently verified.*

---

## Clef 的推理速度究竟提升了多少？

> ## How Much Faster is Clef?

通过将云端托管的 Clef 服务无缝迁移至推理引擎 [SGLang](https://github.com/sgl-project/sglang/pull/42721) ，并对其模型服务基础设施进行深度性能调优 (全程无需对模型权重本身做任何修改) ，Cloudflare 实现了极其显著的推理提速：

> By migrating hosted Clef to [SGLang](https://github.com/sgl-project/sglang/pull/42721) and optimizing its serving infrastructure (without modifying model weights), Cloudflare achieved substantial speedups:

* **约 800 个 Token 场景：** 中位数延迟从 262 毫秒骤降至 152 毫秒 (**速度提升 1.7 倍**) 。
* **约 3,400 个 Token 场景：** 延迟从 616 毫秒降至 305 毫秒 (**速度提升 2.0 倍**) 。
* **约 16,000 个 Token 场景：** 延迟从 2,721 毫秒缩短至 1,635 毫秒。

> * **~800 tokens:** Median latency dropped from 262 ms to 152 ms (**1.7x gain**).
> * **~3,400 tokens:** Latency fell from 616 ms to 305 ms (**2.0x gain**).
> * **~16,000 tokens:** Latency dropped from 2,721 ms to 1,635 ms.

从版本 SGLang 0.5.22 开始，官方已正式合入了对 Clef 系列决策模型的原生支持。

> Clef support is officially included starting in SGLang 0.5.22.

---

## 总结与核心要点

> ## Key Takeaways

* **全模态一体化决策：** Clef-omni 能够在单次决策 API 调用中，同时对文本、图像、音频和视频四种模态并发进行打分评估。
* **高效 MoE 架构设计：** 基于 Qwen3-Omni 构建的 30B-A3B 混合专家架构，遵循 Apache-2.0 开源许可协议，在云端托管的调用单价仅为每百万 Token 0.15 美元。
* **极具竞争力的价格策略：** 轻量级模型 Clef-flash 的调用费用现已直降至每百万 Token 0.038 美元 (低于竞品 Jev 的 0.042 美元) ，并提供 24k 的云端上下文窗口。
* **推理服务吞吐与延迟优化：** 在迁移到底层推理引擎 SGLang 后，托管版 Clef 在中位数延迟上实现了 1.7 倍至 2.0 倍的全面提速。
* **鲜明的任务专长画像：** Clef-omni 在意图识别与分类路由任务中实力领跑，但在高强度严苛逻辑推理与工作流综合评测中仍稍落后于纯文本标准版 Clef 。

> * **Unified Multimodal Decisions:** Clef-omni scores text, images, audio, and video concurrently within a single decision call.
> * **Efficient Architecture:** Built as a 30B-A3B MoE on Qwen3-Omni under an Apache-2.0 license, priced at $0.15 per million tokens.
> * **Competitive Pricing:** Clef-flash is now priced at $0.038 per million tokens (undercutting Jev's $0.042) with a 24k hosted context.
> * **Serving Improvements:** Hosted Clef is 1.7x to 2.0x faster at the median following its transition to SGLang.
> * **Task Specialization:** Clef-omni excels at intent and classification tasks, though it trails standard Clef on rigorous reasoning and workflow evaluations.

---

## 参考资料与相关链接

> ## Additional Resources

* [Cloudflare 官方发布公告](https://blog.cloudflare.com/clef-faster-cheaper-multimodal/)
* [Hugging Face 上的开源模型权重](https://huggingface.co/Cloudflare/clef-omni)
* [Cloudflare Workers AI 官方文档](https://developers.cloudflare.com/workers-ai/models/clef-omni)

> * [Cloudflare Official Announcement](https://blog.cloudflare.com/clef-faster-cheaper-multimodal/)
> * [Hugging Face Model Weights](https://huggingface.co/Cloudflare/clef-omni)
> * [Workers AI Documentation](https://developers.cloudflare.com/workers-ai/models/clef-omni)

*本研究成果全部归属于 Cloudflare 研究团队。原文来源于 [MarkTechPost](https://www.marktechpost.com/2026/10/11/cloudflare-clef-omni-multimodal-decision-model/) 。*

> *All credit for this development goes to the Cloudflare research team. Originally sourced from [MarkTechPost](https://www.marktechpost.com/2026/10/11/cloudflare-clef-omni-multimodal-decision-model/).*
