---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-21
hide:
  - navigation
tags:
  - DeepSeek
  - DeepInfer
  - 大模型推理
  - 开源框架
  - GPU加速
title: "DeepSeek 开源 DeepInfer：揭秘支撑 DeepSeek-V4.1-Flash 的高性能推理框架"
---

# DeepSeek 开源 DeepInfer：揭秘支撑 DeepSeek-V4.1-Flash 的高性能推理框架

> # DeepSeek Open-Sources DeepInfer, the Inference Framework Behind DeepSeek-V4.1-Flash

### 文章背景与核心概要

在超大规模 AI 生产服务中，如何以极致吞吐量和最低算力成本驱动万亿级 Token 的生成，是前沿 AI 实验室的核心壁垒。DeepSeek 正式开源了其生产环境中使用的旗舰级高性能推理引擎 DeepInfer，该框架正是支撑其最新 DeepSeek-V4.1-Flash 模型的底层利器。DeepInfer 采用 Apache 2.0 协议开源，配套的 Token 编解码层 deepseek-recipe 则采用 MIT 协议，深度融合了 FlashMLA、DeepGEMM、DeepEP 等专有底层算子，并创新引入基于置信度调度的投机解码与滑动窗口注意力有界重放技术，在单集群中实现了日均处理逾 155 万亿 Token 的工业级惊人吞吐。该项目为全球大模型工程领域提供了一窥顶级实验室生产级全栈服务架构的难得窗口。

---

## 核心概述

> ## Summary

DeepSeek 正式开源了其自研的高性能大模型推理引擎 **DeepInfer**。作为支撑其在线生产服务与最新发布的 [DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) 模型的底层核心，DeepInfer 采用 Apache 2.0 开源协议，并配套以 MIT 协议开源的 `deepseek-recipe` Token 编解码层。这为开发者提供了一个不可多得的绝佳契机，得以深入探究前沿 AI 实验室内部高度严密的生产部署技术栈。尽管当前开源版本仅针对运行于 NVIDIA SM100 (Blackwell 架构) GPU 与华为昇腾 (Huawei Ascend) 950 NPU 上的 DeepSeek-V4.1-Flash 提供离线推理支持，但其系统性能极为强悍，在单个集群内便能支撑每天超过 155 万亿 Token 的生产级吞吐量。

> DeepSeek has open-sourced **DeepInfer**, the high-performance inference engine driving its production services and the [DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) model. Released under the Apache 2.0 license alongside the MIT-licensed `deepseek-recipe` token encoding/decoding layer, DeepInfer offers developers a rare look into a frontier AI lab’s production serving stack. While currently supporting offline inference exclusively for DeepSeek-V4.1-Flash on NVIDIA SM100 (Blackwell) GPUs and Huawei Ascend 950 NPUs, the framework achieves staggering production-grade performance, handling over 155 trillion tokens per day in a single cluster.

---

## 关键要点速览

> ## TL;DR

* **规模与适配范围**：支持 1 种模型架构 (`DeepSeek-V4.1-Flash`)，根据其[模型卡 (Model Card)](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)，该模型具备 100 万 Token 的超长上下文窗口；
* **硬件要求**：专为 NVIDIA SM100 (Blackwell) GPU 与华为昇腾 950 NPU 量身定制（基准测试中预填充阶段采用 4 张 GPU，解码阶段采用 64 张 GPU）；
* **性能表现**：具备顶尖的工业级生产吞吐量，据官方披露单个集群日处理量达 155 万亿 Token；
* **核心亮点**：在每卡承载 256 个请求 (EP64 专家并行、131,072 上下文) 时，单卡输出吞吐量突破 25,000 Token/秒；
* **已知局限**：目前专为离线推理设计；高级 KV Cache 管理系统、预填充与解码解耦 (P/D Disaggregation) 以及全局负载均衡等组件因与内部基础设施深度耦合而未包含在此次开源版本中。

> * **Size / Scope:** Supports 1 model architecture (`DeepSeek-V4.1-Flash`) featuring a 1M-token context window per the [model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017).
> * **Hardware Requirements:** Built for NVIDIA SM100 (Blackwell) GPUs and Huawei Ascend 950 NPUs (benchmarks utilized 4 GPUs for prefill and 64 for decode).
> * **Performance:** Exceptional production-grade throughput; reportedly serves 155 trillion tokens per day across a single cluster.
> * **Highlights:** Achieves over 25,000 output tokens/sec/GPU at 256 requests per rank (EP64, 131,072 context).
> * **Limitations:** Designed for offline inference only. Advanced KV cache systems, P/D disaggregation, and load balancing are omitted as they remain coupled to internal infrastructure.

---

## 什么是 DeepInfer？

> ## What is DeepInfer?

DeepInfer 是一款高性能大语言模型 (Large Language Model, LLM) 推理引擎，最初基于 [vLLM](https://github.com/vllm-project/vllm) 深度二次开发，并融合吸收了 SGLang 与 TensorRT-LLM 的设计灵感。根据其官方 GitHub [README](https://github.com/deepseek-ai/DeepInfer) 介绍，该引擎正是 DeepSeek 内部大规模生产服务背后的核心支柱。

> DeepInfer is a high-performance inference engine originally built on top of [vLLM](https://github.com/vllm-project/vllm), drawing inspiration from SGLang and TensorRT-LLM. According to its GitHub [README](https://github.com/deepseek-ai/DeepInfer), it powers DeepSeek’s large-scale production services. 

官方配套发布的[部署常见问题解答 (Deployment Q&A)](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md) 披露了其庞大的运行规模：仅单个计算集群每天便承载处理 155 万亿 Token 的洪峰流量；在谷电低谷时段电价下，整套基础设施的综合运营毛利据测算可达每 GPU·小时 38 美元。

> The accompanying [deployment Q&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md) outlines its massive scale: a single cluster serves 155 trillion tokens per day, with overall operational revenue reported at US$38 per GPU-hour at valley pricing.

---

## DeepInfer 的底层运行机制

> ## How Does DeepInfer Work?

该引擎深度集成了 DeepSeek 旗下的一系列专有高性能底层算子内核 —— 包括 [FlashMLA](https://github.com/deepseek-ai/FlashMLA)、[DeepGEMM](https://github.com/deepseek-ai/DeepGEMM)、[DeepEP](https://github.com/deepseek-ai/DeepEP)、TileKernels、DeepSelect 以及定制的 TileLang 算子内核 —— 并辅以五大系统级架构创新：

> The engine stacks proprietary DeepSeek kernels—including [FlashMLA](https://github.com/deepseek-ai/FlashMLA), [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM), [DeepEP](https://github.com/deepseek-ai/DeepEP), TileKernels, DeepSelect, and custom TileLang kernels—reinforced by five core system-level innovations:

### 混合并行：注意力数据并行结合宽专家并行 (Wide-EP)

> ### Parallelism: Attention DP plus Wide-EP

注意力机制采用数据并行 (Data Parallelism, DP)，而混合专家模型 (Mixture-of-Experts, MoE) 层则采用专家并行 (Expert Parallelism, EP)，并通过专家并行负载均衡器 (EPLB) 进行精细调度。解码阶段在超级节点内以 EP64 至 EP128 的宽并行规模高效执行，而预填充阶段则根据显存限制选用最小的专家并行度（通常为 EP2 到 EP8）。

> Attention mechanisms use data parallelism, while Mixture-of-Experts (MoE) layers employ expert parallelism managed by an expert-parallel load balancer (EPLB). Decode runs efficiently at EP64 to EP128 inside a supernode, whereas prefill relies on the smallest EP that memory allows (typically EP2 to EP8).

### DSpark：置信度调度的投机解码

> ### DSpark: Confidence-Scheduled Speculative Decoding

草稿模型在每个步骤提出 5 个候选 Token，同时一个专门的置信度预测头 (Confidence Head) 同步预测每个草稿 Token 的接受概率。随后调度器仅挑选最具置信度价值的前缀进行核验。根据官方 Q&A 数据，该技术在保持最终接受 Token 长度基本一致 (3.29 对比 3.20) 的前提下，成功将需要验证的草稿 Token 数量削减了约 30%。

> A draft model proposes 5 tokens per step, while a Confidence Head predicts each draft token’s acceptance rate. The scheduler then verifies only the most valuable prefix. Per the Q&A, this cuts verified draft tokens by ~30% while keeping accepted token lengths stable (3.29 vs 3.20).

### 滑动窗口注意力有界重放 (SWA Bounded Replay)

> ### SWA Bounded Replay

在发生缓存命中时，DeepInfer 仅需重算滑动窗口注意力 (Sliding-Window Attention, SWA) 状态的最后 128 个 Token。这一精妙设计使得无论上下文长度如何延伸，重计算的开销都能保持恒定常数，从而将解码器层中的预填充计算总量减少了将近一半。

> On a cache hit, DeepInfer recomputes only the final 128 tokens of the sliding-window attention state. This keeps recomputation costs constant regardless of context length, nearly halving total prefill compute in decoder layers.

### 异步调度、确定性与结构化输出

> ### Asynchronous Scheduling, Determinism, and Structured Output

CPU 的批处理调度与 GPU 的底层计算实现了完全重叠覆盖，彻底消除了不同推理步骤之间 GPU 处于空闲的“气泡”时间。在 NVIDIA 硬件上，系统独家支持了批次无关推理 (Batch-Invariant Inference) 与确定性采样，同时支持针对正则表达式、JSON Schema 和 EBNF 文法的结构化输出限制。

> CPU batch scheduling completely overlaps with GPU execution to eliminate GPU idle time between steps. Batch-invariant inference and deterministic sampling are supported exclusively on NVIDIA hardware, alongside structured outputs supporting regex, JSON schema, and EBNF grammars.

---

## DeepInfer 的实际吞吐性能有多强？

> ## How Fast Is DeepInfer?

DeepSeek 公布了 DeepSeek-V4.1-Flash 在 131,072 上下文窗口下的[帕累托前沿曲线 (Pareto curves)](https://github.com/deepseek-ai/DeepInfer#performance-benchmarks)（预填充运行于 4 张 SM100 GPU，解码运行于 64 张）。官方公布的测试数据包括：

> DeepSeek has published [Pareto curves](https://github.com/deepseek-ai/DeepInfer#performance-benchmarks) for DeepSeek-V4.1-Flash at a 131,072 context window (prefill running on 4 SM100 GPUs; decode on 64). Self-reported figures include:

* **解码阶段 (EP64DP64, nextn=3, 75% 接受率)**：在单 Rank 承载 256 个并发请求时，单 GPU 输出吞吐量突破 25,000 Token/秒（折算单用户生成速度逼近 100 Token/秒）。当并发降至 8 个请求时，单用户生成速度更是能突破 300 Token/秒。
* **预填充阶段 (EP4DP4, 140 Token 有界重放)**：在单 Rank 处理 4,096 Token 时，非缓存吞吐量达到约 60,000 Token/秒/GPU；当扩展至 65,536 Token 时，吞吐量进一步攀升至近 90,000 Token/秒（每步耗时约 730 毫秒）。
* **宽专家并行 (Wide-EP) 的性能收益**：官方提供的 [EP8 与 EP64 对比图表](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/images/wide_ep_decode_pareto.png) 明确证实，在各种不同批大小 (Batch Size) 场景下，EP64 的性能表现均全面优于 EP8。

> * **Decode (EP64DP64, nextn=3, 75% acceptance):** Exceeds 25,000 tokens/sec/GPU at 256 requests per rank (nearing 100 tokens/sec per user). At 8 requests, per-user speeds surpass 300 tokens/sec.
> * **Prefill (EP4DP4, 140-token bounded replay):** Reaches ~60,000 non-cached tokens/sec/GPU at 4,096 tokens per rank, scaling to nearly 90,000 tokens/sec at 65,536 tokens (~730 ms per step).
> * **Wide-EP Payoff:** An [EP8 vs EP64 chart](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/images/wide_ep_decode_pareto.png) demonstrates that EP64 consistently outperforms EP8 across every batch size.

---

## 核心特性横向对比：DeepInfer 对决主流推理框架

> ## Feature Comparison: DeepInfer vs. vLLM, SGLang, and TensorRT-LLM

| 特性维度 | DeepInfer | vLLM | SGLang | TensorRT-LLM |
| :--- | :--- | :--- | :--- | :--- |
| **维护团队** | [DeepSeek](https://github.com/deepseek-ai/DeepInfer) | [vLLM 项目组](https://github.com/vllm-project/vllm) | [SGLang 项目组](https://github.com/sgl-project/sglang) | [NVIDIA](https://github.com/NVIDIA/TensorRT-LLM) |
| **开源协议** | [Apache 2.0](https://github.com/deepseek-ai/DeepInfer/blob/main/LICENSE) | [Apache 2.0](https://github.com/vllm-project/vllm/blob/main/LICENSE) | [Apache 2.0](https://github.com/sgl-project/sglang/blob/main/LICENSE) | [Apache 2.0](https://github.com/NVIDIA/TensorRT-LLM/blob/main/LICENSE) |
| **模型支持覆盖** | 1 个 (DeepSeek-V4.1-Flash) | [200+ 种架构](https://github.com/vllm-project/vllm) | [大语言模型, 视觉模型, 扩散模型](https://github.com/sgl-project/sglang) | [支持矩阵表](https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html) |
| **硬件生态** | NVIDIA SM100, 华为昇腾 950 | [NVIDIA, AMD, Intel, CPU 等](https://github.com/vllm-project/vllm) | [NVIDIA, AMD, TPU, Intel 等](https://github.com/sgl-project/sglang) | [NVIDIA GPU](https://github.com/NVIDIA/TensorRT-LLM) |
| **专家并行 (EP)** | 支持 (配备自研 EPLB) | [支持](https://github.com/vllm-project/vllm) | [支持](https://github.com/sgl-project/sglang) | [Wide-EP](https://github.com/NVIDIA/TensorRT-LLM) |
| **投机解码** | DSpark (置信度调度) | [n-gram, 后缀, EAGLE, DFlash](https://github.com/vllm-project/vllm) | [支持 (SpecForge 草稿)](https://github.com/sgl-project/sglang) | [支持](https://github.com/NVIDIA/TensorRT-LLM) |
| **P/D 解耦架构** | 当前开源版本暂未包含 | [支持](https://github.com/vllm-project/vllm) | [通过 llm-d, Dynamo 等支持](https://github.com/sgl-project/sglang) | [支持](https://github.com/NVIDIA/TensorRT-LLM) |
| **在线服务接口** | 仅支持离线推理 | [兼容 OpenAI 规范的服务端](https://github.com/vllm-project/vllm) | [支持](https://github.com/sgl-project/sglang) | [支持](https://github.com/NVIDIA/TensorRT-LLM) |

> | Feature | DeepInfer | vLLM | SGLang | TensorRT-LLM |
> | :--- | :--- | :--- | :--- | :--- |
> | **Maintainer** | [DeepSeek](https://github.com/deepseek-ai/DeepInfer) | [vLLM Project](https://github.com/vllm-project/vllm) | [SGLang Project](https://github.com/sgl-project/sglang) | [NVIDIA](https://github.com/NVIDIA/TensorRT-LLM) |
> | **License** | [Apache 2.0](https://github.com/deepseek-ai/DeepInfer/blob/main/LICENSE) | [Apache 2.0](https://github.com/vllm-project/vllm/blob/main/LICENSE) | [Apache 2.0](https://github.com/sgl-project/sglang/blob/main/LICENSE) | [Apache 2.0](https://github.com/NVIDIA/TensorRT-LLM/blob/main/LICENSE) |
> | **Model Coverage** | 1 (DeepSeek-V4.1-Flash) | [200+ Architectures](https://github.com/vllm-project/vllm) | [LLMs, VLMs, Diffusion](https://github.com/sgl-project/sglang) | [Support Matrix](https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html) |
> | **Hardware** | NVIDIA SM100, Huawei Ascend 950 | [NVIDIA, AMD, Intel, CPUs, etc.](https://github.com/vllm-project/vllm) | [NVIDIA, AMD, TPU, Intel, etc.](https://github.com/sgl-project/sglang) | [NVIDIA GPUs](https://github.com/NVIDIA/TensorRT-LLM) |
> | **Expert Parallelism** | Yes, with EPLB | [Yes](https://github.com/vllm-project/vllm) | [Yes](https://github.com/sgl-project/sglang) | [Wide-EP](https://github.com/NVIDIA/TensorRT-LLM) |
> | **Speculative Decoding** | DSpark (confidence-scheduled) | [n-gram, suffix, EAGLE, DFlash](https://github.com/vllm-project/vllm) | [Yes (SpecForge drafts)](https://github.com/sgl-project/sglang) | [Yes](https://github.com/NVIDIA/TensorRT-LLM) |
> | **P/D Disaggregation** | Not in this release | [Yes](https://github.com/vllm-project/vllm) | [Via llm-d, Dynamo, etc.](https://github.com/sgl-project/sglang) | [Yes](https://github.com/NVIDIA/TensorRT-LLM) |
> | **Online Serving** | Offline inference only | [OpenAI-compatible server](https://github.com/vllm-project/vllm) | [Yes](https://github.com/sgl-project/sglang) | [Yes](https://github.com/NVIDIA/TensorRT-LLM) |

---

## DeepInfer 存在哪些局限？

> ## What Are DeepInfer’s Limitations?

* **缺失部分基础设施套件**：构建一套完备的生产级服务往往依赖于独立的 KV Cache 管理系统、预填充/解码解耦架构以及跨数据并行副本的智能负载均衡器 —— 这些模块与 DeepSeek 内部基础设施高度绑定，因此在此次开源版本中未对外提供。
* **极其严苛的硬件与环境门槛**：编译构建强制要求 Linux 系统、GCC 13+、Python 3.12 以及 CUDA 13 或 CANN 9.2；此外，实现高效生产部署所需的最小集群硬件规模就达到了 64 张预填充 GPU 配备 64 张解码 GPU。
* **算子内核版本差异**：DeepSeek 内部部署的 FlashMLA 解码内核性能比公开开源版本要高出 5% 到 10%，由此带来端到端整体性能上约 5% 以内的轻微差距。

> * **Missing Infrastructure Components:** A full production service requires an independent KV cache management system, prefill/decode disaggregation, and load balancing across data-parallel replicas—features tightly coupled to DeepSeek's internal infrastructure and omitted here.
> * **Rigid Hardware & Environment Constraints:** Builds mandate Linux, GCC 13+, Python 3.12, and CUDA 13 or CANN 9.2. Furthermore, the minimal efficient production footprint requires 64 prefill GPUs paired with 64 decode GPUs.
> * **Kernel Discrepancies:** The internal FlashMLA decoding kernel performs 5% to 10% faster than the public release, translating to an end-to-end performance gap of 5% or less.

---

## 核心总结

> ## Key Takeaways

* DeepInfer 是 DeepSeek 核心生产级推理引擎，现已正式在 GitHub 上以 **Apache 2.0 协议**开源；
* 当前版本专为 **DeepSeek-V4.1-Flash** 模型量身打造，仅支持 NVIDIA SM100 与华为昇腾 950 硬件；
* 在 64 张 GPU 的集群规模下，解码吞吐量可扩展突破至 **25,000 Token/秒/GPU** 以上；
* 创新的 **DSpark** 投机解码机制在保持候选接受率的同时，成功减少了约 30% 的待核验草稿 Token；
* 当前开源版本主要面向**离线推理**场景，未内置原生分布式 KV Cache 存储库、P/D 解耦架构及在线负载均衡器。

> * DeepInfer is DeepSeek’s production-grade inference engine, now available under the **Apache 2.0 license** on GitHub.
> * It currently supports the **DeepSeek-V4.1-Flash** model exclusively on NVIDIA SM100 and Huawei Ascend 950 hardware.
> * Decode throughput scales past **25,000 tokens/sec/GPU** across 64 GPUs.
> * **DSpark** reduces verified draft tokens by ~30% while preserving acceptance ratios.
> * The release is limited to **offline inference**, omitting native KV cache stores, P/D disaggregation, and online load balancers.

---

## 相关资源与链接

> ## Additional Resources

* **代码仓库与技术文档**：[GitHub 代码仓库](https://github.com/deepseek-ai/DeepInfer) | [部署问答手册](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md) | [`deepseek-recipe`](https://github.com/deepseek-ai/deepseek-recipe) | [模型主页](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
* **社区交流**：关注 [Twitter](https://x.com/intent/follow?screen_name=marktechpost) | 加入拥有 15 万+ 成员的 [ML SubReddit](https://www.reddit.com/r/machinelearningnews/) | 订阅[技术通讯](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526) | 加入 [Telegram 频道](https://t.me/machinelearningresearchnews)

> * **Repositories & Documentation:** [GitHub Repository](https://github.com/deepseek-ai/DeepInfer) | [Deployment Q&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md) | [`deepseek-recipe`](https://github.com/deepseek-ai/deepseek-recipe) | [Model Card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
> * **Community:** Follow on [Twitter](https://x.com/intent/follow?screen_name=marktechpost) | Join the [150k+ ML SubReddit](https://www.reddit.com/r/machinelearningnews/) | Subscribe to [the Newsletter](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526) | Join the [Telegram Channel](https://t.me/machinelearningresearchnews)

***

*本文原载于 [MarkTechPost](https://www.marktechpost.com)，原文标题为 [DeepSeek Open-Sources DeepInfer, the Inference Framework Behind DeepSeek-V4.1-Flash](https://www.marktechpost.com/2026/10/20/deepseek-deepinfer-open-source-inference-framework/)。*

> *The post [DeepSeek Open-Sources DeepInfer, the Inference Framework Behind DeepSeek-V4.1-Flash](https://www.marktechpost.com/2026/10/20/deepseek-deepinfer-open-source-inference-framework/) appeared first on [MarkTechPost](https://www.marktechpost.com).*
