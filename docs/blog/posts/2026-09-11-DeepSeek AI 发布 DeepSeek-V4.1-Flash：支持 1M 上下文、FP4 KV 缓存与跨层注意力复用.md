---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-11
hide:
- navigation
tags:
- DeepSeek
- 稀疏注意力
- KV缓存
- MoE模型
- 开源模型
title: DeepSeek AI 发布 DeepSeek-V4.1-Flash：支持 1M 上下文、FP4 KV 缓存与跨层注意力复用
---
### 文章背景与核心概要
随着长程 AI 智能体（Long-horizon AI agents）和百万级长上下文（million-token contexts）的普及，LLM 推理面临着极其沉重的输入密集型内存瓶颈，高带宽内存（HBM）和固态硬盘（SSD）容量常常不堪重负。为此，DeepSeek AI 推出了全新的多模态混合专家（MoE）模型 **DeepSeek-V4.1-Flash**，旨在从根本上解决这一内存挑战。

该模型引入了因果编码器-解码器（Causal Encoder-Decoder）架构、压缩稀疏注意力 2 代（CSA2）、FP4 KV 缓存量化以及解码器 SWA 有界重放（Decoder SWA Bounded Replay）等一系列创新技术。通过这些架构优化，其全局 KV 缓存占用被大幅压缩至每个 token 仅 **890 字节**，相比早期版本实现了数百倍的缩减。同时，它在各项智能体基准测试中展现出顶尖的性能，并且所有权重均在 **MIT 许可证** 下开源，为构建高效、长上下文的 AI 应用提供了强有力的支持。

---

## DeepSeek AI Released DeepSeek-V4.1-Flash with 1M Context, FP4 KV Cache, and Cross-Layer Attention Reuse

> DeepSeek AI has launched **DeepSeek-V4.1-Flash**, a multimodal Mixture-of-Experts (MoE) model engineered specifically to tackle the input-heavy memory bottlenecks of long-horizon AI agents and million-token contexts. Featuring a global KV cache footprint of just **890 bytes per token** (a ~437x reduction from DeepSeek-V1) and innovative architectural designs like a Causal Encoder-Decoder and Compressed Sparse Attention 2 (CSA2), the model achieves cutting-edge performance on agentic benchmarks while offering open weights under an **MIT license**.

---

## 概述

长程智能体已将大语言模型（LLM）的推理变成了一种输入密集的繁重工作负载。重复的 Prefill（预填充）阶段和百万级的上下文会导致 KV 缓存急剧膨胀，从而对高带宽内存（HBM）、固态硬盘（SSD）容量以及整体带宽造成巨大压力。

> Long-horizon agents have turned LLM serving into an input-heavy workload. Repeated prefills and million-token contexts leave KV caches that strain High Bandwidth Memory (HBM), Solid-State Drive (SSD) capacity, and overall bandwidth. 

[DeepSeek AI](https://huggingface.co/deepseek-ai) 围绕这一核心瓶颈构建了其最新发布的 [DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)。它是一个多模态混合专家（MoE）模型，拥有 **552B 的主干参数**、**196B 的额外 Engram 参数**以及 **1M token 的上下文窗口**。在预填充阶段，它每个 token 激活 **8B 参数**；在解码阶段则激活 **16B 参数**。

> [DeepSeek AI](https://huggingface.co/deepseek-ai) built its newest release—[DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)—around that exact bottleneck. It is a multimodal Mixture-of-Experts model with **552B backbone parameters**, **196B additional Engram parameters**, and a **1M-token context window**. It activates **8B parameters per token during prefill** and **16B during decode**. 

**它能部署吗？完全可以。** 该模型以 [MIT 许可证](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/tree/main/LICENSE)开源了权重，并在 Hugging Face 上提供了 vLLM、SGLang 和 Transformers 的支持路径。此外，研究团队还介绍了一个包含低、中、高三个推理等级的公共 API。

> **Is it deployable? Yes.** Open weights ship under an [MIT license](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/tree/main/LICENSE) with vLLM, SGLang, and Transformers paths on Hugging Face, and the research team describes a public API with low, high, and max reasoning tiers.

---

## 因果编码器-解码器：预填充计算量减半

这个 40 层的骨干网络被拆分为一个 **20 层的因果编码器（causal encoder）** 和一个 **20 层的解码器（decoder）**。受 [YOCO](https://arxiv.org/abs/2405.05254) 的启发，解码器不再计算自身的全局 KV 缓存，而是通过每层的投影权重，直接从最终的编码器隐藏状态中推导出来。

> The 40-layer backbone is split into a **20-layer causal encoder** and a **20-layer decoder**. Inspired by [YOCO](https://arxiv.org/abs/2405.05254), the decoder does not compute its own global KV. Instead, per-layer projection weights derive it from the final encoder hidden state. 

因此，提示词 token 仅在编码器处处理，这**使预填充计算量几乎减半**。每个层中仍然运行着具有 128 token 窗口大小的滑动窗口注意力（SWA），因此解码器的 SWA 状态仅通过重放最后 128 个提示词 token 来重建——研究团队将这一技术称为**解码器 SWA 有界重放（Decoder SWA Bounded Replay）**。

> Prompt tokens therefore stop at the encoder, which **nearly halves prefill compute**. Sliding-window attention (SWA) with a 128-token window still runs in every layer, so decoder SWA states are rebuilt by replaying only the last 128 prompt tokens—a technique the research team calls **Decoder SWA Bounded Replay**.

---

## 压缩稀疏注意力 2 代（CSA2）

虽然 DeepSeek-V4 将 CSA 与重度压缩注意力（Heavily Compressed Attention）结合使用，但 V4.1-Flash 采用了纯粹的 CSA2，并沿着层轴（layer axis）直接攻击缓存大小。每个 CSA2 层被静态分配为以下 3 种模式之一：

> While DeepSeek-V4 mixed CSA with Heavily Compressed Attention, V4.1-Flash uses pure CSA2 and attacks cache size along the layer axis. Each CSA2 layer is statically assigned one of 3 modes:

* **Full（全量）**：计算其自身的的主 KV，从中投影出索引器 K，并选择最新的前 512 个（Top-512）索引。
* **Reindex（重新索引）**：复用上一个 Full 层的的主 KV 和索引器 K，但使用自身的索引器 Q 对其进行重新评分。
* **Reuse（复用）**：同时复用主 KV 和最新的 Top-K 索引，完全跳过索引器。

> * **Full**: Computes its own main KV, projects indexer K from it, and selects fresh Top-512 indices.
> * **Reindex**: Reuses main KV and indexer K from the last Full layer but rescores them with its own indexer Q.
> * **Reuse**: Reuses both the main KV and the latest Top-K indices, skipping the indexer entirely.

每一层都保留自己的主 Q 和 SWA KV。18 个 CSA2 编码器层在 6 个一组（1 个 Full，5 个 Reuse）中共使用 2 的压缩比。20 个解码器层在 4 个一组中采用 1 的压缩比：第一组是 1 个 Full 加上 3 个 Reuse，其余则是 Reindex 加上 3 个 Reuse。解码器中的**分层稀疏索引器（Hierarchical Sparse Indexer）**允许 Full 层构建一个多达 16,384 个位置的候选池（2,048 个大小为 8 的块），从而让后续的 Reindex 层对一个有界集合而非整个上下文进行评分。

> Every layer keeps its own main Q and SWA KV. The 18 CSA2 encoder layers use a compression ratio of 2 in 3 groups of 6 (1 Full, 5 Reuse). The 20 decoder layers use ratio 1 in 5 groups of 4: the first is Full plus 3 Reuse, the rest Reindex plus 3 Reuse. A **Hierarchical Sparse Indexer** in the decoder lets the Full layer build a candidate pool of up to 16,384 positions (2,048 blocks of 8), so later Reindex layers score a bounded set instead of the entire context.

---

## FP4 KV、有界重放与其他扩展

* **FP4 KV 量化**：主 KV 缓存被量化为 E2M1 格式，每 16 个通道配备一个 E4M3 比例因子，这遵循了 [NVFP4](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/) 的设计但去掉了其全局缩放。通过量化感知训练引入该技术，使存储空间较 V4 的 FP8 缓存几乎减少了一半。
* **优化的 SWA 持久化**：SWA KV 不再持久化保存到 SSD 中。它存储在一个由宿主机 DRAM 的 10% 划分出的分布式池中，TTL（生存时间）为几分钟，而全局 KV 则保持有保障的 72 小时寿命。当发生未命中时，编码器 SWA 有界重放（Encoder SWA Bounded Replay）仅重新计算 128 个 token。
* **其他架构增强**：包括单通 [mHC](https://arxiv.org/abs/2512.24880)（将激活内存流量减半）、位于第 1 层和第 14 层的 [Engram](https://arxiv.org/abs/2601.07372) 条件内存模块、DSpark 推测解码，以及逐头（head-wise）Muon。当上下文从 4K 增长到 1M 时，单 token 解码的 FLOPs 仅增加 1/4。

> * **FP4 KV Quantization**: The main KV cache is quantized to E2M1 with one E4M3 scale per 16 channels, following [NVFP4](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/) without its global scale. Introduced through quantization-aware training, this nearly halves storage against V4’s FP8 cache.
> * **Optimized SWA Persistence**: SWA KV is no longer persisted to SSD. It lives in a distributed pool carved from 10% of host DRAM with a TTL of minutes, while global KV keeps a guaranteed 72-hour lifetime. On a miss, Encoder SWA Bounded Replay recomputes only 128 tokens.
> * **Additional Architectural Enhancements**: Includes Single-Pass [mHC](https://arxiv.org/abs/2512.24880) (halving activation memory traffic), the [Engram](https://arxiv.org/abs/2601.07372) conditional memory module at layers 1 and 14, DSpark speculative decoding, and head-wise Muon. Single-token decode FLOPs rise by only 1/4 when context grows from 4K to 1M.

---

## 训练与结果

预训练涵盖了 **45T 的多模态 token**，文本与多模态的比例为 7:1。稀疏注意力从头开始在 64K 序列长度下进行训练，无需稠密预热（dense warmup），并在 34T token 时将上下文扩展到 1M。基础模型在世界知识和代码能力上与 DeepSeek-V4-Pro-Base 相匹配，同时只使用了总参数的 1/3 和激活参数的 1/4。

> Pre-training covers **45T multimodal tokens** at a 7:1 text-to-multimodal ratio. Sparse attention is trained from scratch at 64K sequence length with no dense warmup, and context is extended to 1M at 34T tokens. The base model matches DeepSeek-V4-Pro-Base on world knowledge and coding while using 1/3 of the total and 1/4 of the activated parameters.

后训练没有引入新的算法，其收益主要来自于大规模的可验证智能体任务合成、跨异构脚手架的强化学习（RL），以及来自 40 多个教师模型的在线策略蒸馏（on-policy distillation）。

> Post-training introduces no new algorithms, deriving gains instead from large-scale synthesis of verifiable agent tasks, RL across heterogeneous scaffolds, and on-policy distillation from over 40 teachers. 

### 部分基准测试结果

### Selected Benchmark Results

| Benchmark | DS-V4.1-Flash | DS-V4-Flash | Opus-5 | GPT-5.6 Sol |
| :--- | :--- | :--- | :--- | :--- |
| **Terminal-Bench 2.1** | 90.6 | 82.7 | 89.1 | 88.8 |
| **DeepSWE v1.1** | 74.2 | 54.4 | 74.0 | 73.0 |
| **Terminal-Bench 4.0** | 31.2 | 7.0 | 51.8 | 39.9 |
| **Automation-Bench** | 54.8 | 37.7 | 50.3 | 45.8 |
| **GPQA Diamond** | 90.9 | 89.9 | 93.4 | 94.1 |
| **Codeforces (rating)** | 3471 | 3289 | n/a | n/a |

---

## 核心要点

* **海量 KV 缩减**：全局 KV 缓存降至每个 token 890 字节（约为 V4-Flash 的 1/4，比 V1 低 437 倍）。
* **高效预填充**：因果编码器-解码器在预填充时仅运行 20 个编码器层，激活参数为 8B，解码时为 16B。
* **灵活的注意力机制**：CSA2 通过 Full、Reindex 和 Reuse 模式在各层之间共享主 KV、索引器 K 和 Top-K 索引。
* **优化的存储**：FP4 主 KV 加 SWA 有界重放将持久化缓存削减至 V4-Flash 的约 1/8。
* **顶尖性能**：在 Terminal-Bench 2.1 和 DeepSWE v1.1 上表现优于 Opus-5 和 GPT-5.6 Sol，同时提供开源的 MIT 权重。

> * **Massive KV Reduction**: Global KV cache falls to 890 bytes per token (~1/4 of V4-Flash and 437x below V1).
> * **Efficient Prefill**: Causal Encoder-Decoder runs only 20 encoder layers in prefill, activating 8B parameters against 16B in decode.
> * **Flexible Attention**: CSA2 shares main KV, indexer K, and Top-K indices across layers using Full, Reindex, and Reuse modes.
> * **Optimized Storage**: FP4 main KV plus SWA Bounded Replay cut persistent cache to about 1/8 of V4-Flash.
> * **Top-Tier Performance**: Outperforms Opus-5 and GPT-5.6 Sol on Terminal-Bench 2.1 and DeepSWE v1.1 while offering open MIT weights.

---

## 资源与社区

* 查看 [**Hugging Face 上的模型**](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) 以及 [**技术报告**](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf)。
* 在 [**Twitter**](https://x.com/intent/follow?screen_name=marktechpost) 上关注最新动态。
* 加入拥有 [**15万+ 成员的 ML SubReddit**](https://www.reddit.com/r/machinelearningnews/) 并订阅 [**Newsletter**](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526)。
* 加入 [**Telegram**](https://t.me/machinelearningresearchnews) 社区。
* 商业合作与推广垂询（GitHub、Hugging Face、产品发布、网络研讨会），请[**联系团队**](https://forms.gle/wbash1wF6efRj8G58)。

> * Check out the [**Model on Hugging Face**](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) and the [**Technical Report**](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf). 
> * Follow updates on [**Twitter**](https://x.com/intent/follow?screen_name=marktechpost).
> * Join the [**150k+ ML SubReddit**](https://www.reddit.com/r/machinelearningnews/) and subscribe to [**the Newsletter**](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526).
> * Join the community on [**Telegram**](https://t.me/machinelearningresearchnews).
> * For partnership and promotion inquiries (GitHub, Hugging Face, product releases, webinars), [**connect with the team**](https://forms.gle/wbash1wF6efRj8G58).

***

*来源：本文最初发布于 [MarkTechPost](https://www.marktechpost.com/2026/09/10/deepseek-ai-released-deepseek-v4-1-flash-with-1m-context-fp4-kv-cache-and-cross-layer-attention-reuse/)。*

> *Source: Originally published by [MarkTechPost](https://www.marktechpost.com/2026/09/10/deepseek-ai-released-deepseek-v4-1-flash-with-1m-context-fp4-kv-cache-and-cross-layer-attention-reuse/).*