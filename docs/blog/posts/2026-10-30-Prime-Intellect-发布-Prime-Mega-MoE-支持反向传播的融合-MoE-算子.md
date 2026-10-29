---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-30
hide:
  - navigation
tags:
  - Prime Intellect
  - MoE 算子
  - DeepGEMM
  - GPU 训练加速
  - 开源内核
title: "Prime Intellect 发布 Prime Mega MoE：支持反向传播的融合 MoE 算子，前向提速 3.11 倍"
---

# Prime Intellect 发布 Prime Mega MoE：支持反向传播的融合 MoE 算子，前向提速 3.11 倍

> # Prime Intellect Releases Prime Mega MoE: Trainable Fused MoE Kernel, 3.11x Faster Forward Pass

### 文章背景与核心概要
混合专家模型 (Mixture-of-Experts, MoE) 虽具备以更低计算成本扩展参数规模的优势，但在分布式训练中，Token 在不同 GPU 专家节点间的频繁跨卡通信往往会造成严重的计算空闲与显卡性能浪费。此前，DeepSeek 开源的 Mega MoE 融合算子虽然大幅优化了前向通信与计算重叠，却缺少训练不可或缺的反向传播 (Backward Pass) 实现。分布式 AI 计算创新机构 Prime Intellect 填补了这一空白，推出了支持完整反向传播的 Prime Mega MoE 融合算子，实现了计算与通信的高效重叠，在 Qwen3 MoE 模型训练中带来高达 55% 的端到端训练步耗时缩短，前向推理加速更达 3.11 倍，为开源大模型训练团队节省了海量宝贵的 GPU 算力资源。

---

## 核心总结

> ## Summary

[Prime Intellect](https://www.primeintellect.ai/) 正式发布了 [Prime Mega MoE](https://www.primeintellect.ai/blog/prime-mega-moe)，这是针对 DeepSeek 融合版 Mega MoE 算子的一项突破性训练级扩展。DeepSeek 最初开源的算子仅支持前向传播 (Forward Pass)，而 Prime Intellect 创新性地引入了超高速且支持通信与计算重叠的反向传播机制，使得这款融合算子能够真正投入到端到端的模型训练当中。在集成到 [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) 训练框架后，针对 Qwen3 混合专家 (Mixture-of-Experts, MoE) 模型的完整训练迭代步耗时最高缩短了 34%——与 PyTorch 官方的 TorchTitan 相比更是快了 55%，直接为 AI 团队大幅削减了昂贵的 GPU 训练时长与算力开销。

> [Prime Intellect](https://www.primeintellect.ai/) has released [Prime Mega MoE](https://www.primeintellect.ai/blog/prime-mega-moe), a groundbreaking training extension for DeepSeek’s fused Mega MoE kernel. While DeepSeek's original kernel was limited to the forward pass, Prime Intellect has introduced a fast, overlapping backward pass, making the fused kernel fully viable for model training. Integrated into the [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) trainer, full training steps on Qwen3 Mixture-of-Experts (MoE) models execute up to 34% faster—and up to 55% faster compared to TorchTitan—providing a direct reduction in GPU hours for AI teams.

---

## 极速速览

> ## TL;DR

* **定位属性**：这是一个专门针对底层优化的 GPU 算子内核，而非独立模型。已在 Qwen3-30B-A3B 与 Qwen3-235B-A22B 架构上经过充分验证 (128 个专家，Top-8 动态路由)。
* **运行平台**：支持 NVIDIA Hopper (分块 FP8 精度) 与 Blackwell (MXFP8 精度) 架构 GPU，两者均原生支持 BF16。官方公开测试数据均基于 8×H200 节点、共 32 至 128 块 GPU 集群实测。
* **整体性能**：端到端单步训练时间比 `prime-rl` 基础基准提速 32% 至 34%；比 TorchTitan 快 48% 至 55%。
* **最佳表现**：在 Qwen3-30B-A3B 的 MoE 层上前向传播提速达 3.11 倍 (耗时从 12.0 毫秒骤降至 3.9 毫秒)。
* **下限表现**：在规模更大的 Qwen3-235B-A22B MoE 层上反向传播提速 1.24 倍 (耗时从 30.5 毫秒降低至 24.6 毫秒)。

> * **Size:** A GPU kernel, not a model. Tested on Qwen3-30B-A3B and Qwen3-235B-A22B (128 experts, top-8 routing).
> * **Runs on:** NVIDIA Hopper (blockwise FP8) and Blackwell (MXFP8) GPUs, BF16 on both. Published numbers use 8×H200 nodes, 32 to 128 GPUs.
> * **Performance:** 32% to 34% faster full training steps than the `prime-rl` baseline. 48% to 55% faster than TorchTitan.
> * **Best:** 3.11x faster forward pass on a Qwen3-30B-A3B MoE layer (12.0 ms to 3.9 ms).
> * **Worst:** 1.24x backward pass on a Qwen3-235B-A22B MoE layer (30.5 ms to 24.6 ms).

---

## 什么是 Prime Mega MoE？

> ## What is Prime Mega MoE?

Prime Mega MoE 是一款专为大模型训练量身打造的算子融合与计算通信重叠 (Overlapping) MoE 内核。它直接脱胎于 DeepSeek 开源的高性能矩阵计算库 [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) 中的 Mega MoE 算子，并完成了关键的训练能力补全。

> Prime Mega MoE is a fused, overlapping MoE kernel designed specifically for training. It builds directly upon the Mega MoE kernel found in DeepSeek’s open-source [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) library.

---

## 为什么 MoE 模型的训练极易受限于跨卡通信？

> ## Why is MoE Training Communication-Bound?

在混合专家 (MoE) 架构中，输入的每个 Token 仅会被路由分发给一小部分特定专家，而这些专家通常分散驻留在集群中不同的 GPU 显卡上。正因如此，每一个 MoE 神经网络层在执行时，都必须经历“将 Token 打包发送出去、在目标专家处执行矩阵计算、再把处理结果传回汇聚”的往返过程。更为关键的是，这一复杂的跨卡流转闭环在模型的前向传播和反向传播阶段均会发生一次。

> In a Mixture-of-Experts (MoE) architecture, each token is routed to a small subset of experts distributed across different GPUs. Consequently, every layer must send tokens out, perform expert computations, and send the results back—a cycle that occurs during both the forward and backward passes.

在业界的标准实现中，上述各个步骤往往是割裂且串行运作的：GPU 必须先花费时间对 Token 进行排序重组，接着停下计算干等通信传输层完成数据跨卡搬运；等数据全到了才开始计算，算完又要把结果交还给网络并再次陷入漫长的等待。这种计算与通信脱节的状态，导致极为昂贵的 GPU 核心长期处于空转等待的低效状态。

> In standard setups, these steps operate independently. The GPU sorts tokens and waits on the transport layer, performs computations, hands results back, and waits again, resulting in idle GPU time.

---

## 融合算子究竟是如何高效运转的？

> ## How Does the Fused Kernel Work?

[DeepSeek 开源的 Mega MoE](https://github.com/deepseek-ai/DeepGEMM) 彻底颠覆了这种碎片化的串行调用链路，将其收敛整合进单次算子调用中。它将专家并行分发 (Dispatch)、专家内两层线性投影层计算、SwiGLU 激活函数以及最终的特征组合 (Combine) 步骤高度融合在一起。在底层调度上，当一组 Token 还在网络中飞速传输时，内核已经同步在对先前已抵达的 Token 组展开高并发计算；同时通过显存原生的临时暂存区 (Scratch Buffers) 彻底规避了中间张量的反复存取。然而，DeepSeek 最初开源的官方版本仅实现了前向推理，并没有提供训练必不可少的反向传播算子。

> [DeepSeek’s Mega MoE](https://github.com/deepseek-ai/DeepGEMM) replaces this fragmented chain with a single kernel call. It fuses expert-parallel dispatch, the two expert linear layers, SwiGLU, and combination steps. While one token group is in transit, the kernel computes on a group that has already arrived, skipping intermediate tensors by using GPU-only scratch buffers. However, it originally shipped without a backward implementation.

Prime Intellect 团队精准补全了这块关键拼图：他们全新编写了缺失的反向传播内核，并同样赋予了其强大的计算与通信异步重叠能力。该算子全面支持多种前沿数据类型，涵盖 BF16、MXFP8 (专供 Blackwell 架构) 以及分块式 FP8 (专供 Hopper 架构)。在 [prime-rl 配置项](https://github.com/PrimeIntellect-ai/prime-rl) 中，用户甚至可以启用极具性价比的 `fp8_bwd` 混合精度模式 (即前向使用 BF16 保持高精度，反向传播采用 FP8 极致加速)。

> Prime Intellect solved this by writing the missing backward kernel, which also features overlapping execution. Supported data types include BF16, MXFP8 (Blackwell only), and blockwise FP8 (Hopper only). The [prime-rl config](https://github.com/PrimeIntellect-ai/prime-rl) also supports an `fp8_bwd` mode (BF16 forward, FP8 backward).

---

## Prime Mega MoE 的实际加速表现究竟有多快？

> ## How Fast is Prime Mega MoE?

以下所有性能指标均由 Prime Intellect 官方团队实测公布，基准测试环境采用 8×H200 计算节点、FP8 精度、16,384 长度的 Token 序列，并开启了全激活重计算 (Full Activation Checkpointing)。各项数据均为训练第 6 步至第 20 步实测值的算术平均值。

> All metrics below are self-reported by Prime Intellect, utilizing 8×H200 nodes, FP8, 16,384-token sequences, and full activation checkpointing. Each result represents the mean of steps 6 through 20.

### 完整训练步耗时 (单位：秒——数值越小越好)

> ### Full Training Step (Seconds — Lower is Better)

| 模型 (集群规模) / Model (cluster) | prime-rl 基准 / baseline | TorchTitan (FP8) | Prime Mega MoE | 相比基准提升 / Gain vs baseline | 相比 TorchTitan 提升 / Gain vs TorchTitan |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen3-30B-A3B (32 H200) | 2.78 | 3.07 | 2.08 | 34% | 48% |
| Qwen3-235B-A22B (128 H200) | 12.72 | 14.98 | 9.65 | 32% | 55% |

与 PyTorch 官方的 TorchTitan 相比，在 30B 参数规模的模型上，单卡吞吐量 (Throughput) 从每秒每卡 5,337 Tokens 大幅跃升至 7,886 Tokens；而在更大规模的 235B 模型上，吞吐量亦从 1,094 Tokens 飙升至 1,697 Tokens/s/GPU。

> Compared to TorchTitan, throughput increased from 5,337 to 7,886 tokens/s/GPU on the 30B model, and from 1,094 to 1,697 on the 235B model.

### 单个 MoE 层计算耗时 (单位：毫秒)

> ### Single MoE Layer (Milliseconds)

*(测试配置：单节点，8×H200，专家并行度 EP=8，128 个专家，Top-8 路由，随机路由分配)*

> *(1 node, 8×H200, EP=8, 128 experts, top-8, random routing)*

| MoE 层 / Layer | 前向传播 / Forward | 反向传播 / Backward | 完整单层耗时 (2次前向+1次反向) / Full layer (2x fwd + bwd) |
| :--- | :--- | :--- | :--- |
| Qwen3-30B-A3B | 12.0 to 3.9 (3.11x) | 15.4 to 8.2 (1.87x) | 39.3 to 15.9 (2.47x) |
| Qwen3-235B-A22B | 20.7 to 9.5 (2.17x) | 30.5 to 24.6 (1.24x) | 71.9 to 43.7 (1.64x) |

---

## 与现有主流融合 MoE 方案对比如何？

> ## How Does it Compare with Other Fused MoE Options?

| 特性对比 / Feature | Prime Mega MoE | [DeepGEMM Mega MoE](https://github.com/deepseek-ai/DeepGEMM) | [TorchTitan + DeepEP](https://pytorch.org/blog/enabling-up-to-41-faster-pre-training-mxfp8-and-deepep-for-deepseek-v3-on-b200-with-torchtitan/) | [AMD Primus MegaMoE](https://rocm.docs.amd.com/projects/primus/en/main/04-technical-guides/mega-moe.html) |
| :--- | :--- | :--- | :--- | :--- |
| **开发者 (Developer)** | Prime Intellect | DeepSeek | PyTorch, Nebius | AMD |
| **训练反向支持 (Training backward)** | 支持，融合且重叠执行 | 不支持，仅限前向传播 | 支持 (独立的通信与调度内核) | 支持 (据设计文档披露) |
| **计算通信融合 (Compute and comms fused)** | 是 | 是 | 否 | 是 (调度+GEMM1融合，GEMM2+组合融合) |
| **支持的 GPU (GPUs)** | Hopper, Blackwell | SM90, SM100 (底层库支持) | 公开测试采用 B200 | MI355X (gfx950) |
| **数据精度格式 (Data types)** | BF16, MXFP8, 分块 FP8 | FP8xFP8, FP8xFP4 | BF16, MXFP8 分组 GEMM | BF16, MXFP8 |
| **公开加速幅度 (Published speedup)** | 相比 TorchTitan 单步提速最高达 55% | 未公开 | 在 DeepSeek-V3 671B 上提速最高达 41% | 未公开 |
| **开源协议 (License)** | Apache 2.0 ([prime-rl](https://github.com/PrimeIntellect-ai/prime-rl)) | MIT | BSD-3-Clause | MIT |

*(注：TorchTitan 所标榜的 41% 性能提升采用了截然不同的硬件与测试基线——使用 Blackwell B200 芯片、671B 规模模型及 BF16 纯基线，因此两者数据不可直接横向类比。)*

> *(Note: TorchTitan’s 41% gain utilizes a different hardware setup (B200, 671B model, BF16 baseline) and is not directly comparable.)*

---

## 开发者该如何快速接入与上手？

> ## How Do Developers Use It?

Prime Mega MoE 作为内置调度后端直接集成在 `prime-rl` 框架中。

> Prime Mega MoE operates as a dispatch backend within `prime-rl`.

1. 在配置文件中的 `[trainer.model.moe.dispatch]` 模块下设置 `type = "mega_moe"`；
2. 在 `precision` 选项中指定所需的数据精度：可选 `bf16`、`mxfp8`、`fp8` 或 `fp8_bwd`。

> 1. Set `type = "mega_moe"` under `[trainer.model.moe.dispatch]`.
> 2. Choose your `precision` from `bf16`, `mxfp8`, `fp8`, or `fp8_bwd`.

该训练内核通过预编译的 DeepGEMM 轮子包 (Wheel) 进行分发，开发者可直接从 [prime-kernels](https://github.com/PrimeIntellect-ai/prime-kernels/releases) 发布页获取 (注意：原版官方 DeepGEMM 构建中暂未包含这些扩展能力)。

> The training kernels are distributed via a prebuilt DeepGEMM wheel available from [prime-kernels](https://github.com/PrimeIntellect-ai/prime-kernels/releases) (the stock DeepGEMM build lacks these extensions).

---

## 核心要点总结

> ## Key Takeaways

* **补齐反向训练能力**：Prime Mega MoE 为 DeepSeek 原版的 Mega MoE 算子补全了融合且支持计算通信重叠的高性能反向传播算子。
* **显著缩短训练周期**：模型单步端到端训练耗时相比 `prime-rl` 原生基准降低了 32% 至 34%。
* **相比工业界方案优势明显**：在 Qwen3 系列 MoE 模型上，训练步耗时相比 TorchTitan 显著缩短 48% 至 55%。
* **前反向收益差异**：单层前向传播加速最高可达 3.11 倍，但在超大参数模型层上反向传播的加速增益收敛至 1.24 倍。
* **开箱即用**：现已在 `prime-rl` 训练框架中全面可用，通过 `mega_moe` 调度后端即可一键启用。

> * Prime Mega MoE introduces a fused, overlapping backward pass to DeepSeek’s Mega MoE.
> * Full training steps run 32% to 34% faster than the `prime-rl` baseline.
> * Compared to TorchTitan, steps execute 48% to 55% faster on Qwen3 MoE models.
> * Forward gains reach up to 3.11x, while backward gains taper to 1.24x on larger layers.
> * Available immediately in `prime-rl` via the `mega_moe` dispatch backend.

---

## 资源与延伸阅读链接

> ## Resources & Links

* 阅读官方博客：**[Prime Mega MoE 博客全文](https://www.primeintellect.ai/blog/prime-mega-moe)**
* 查看社交媒体发布公告：**[X (原 Twitter) 官方发布动态](https://x.com/PrimeIntellect/status/2115861613261815883)**
* 探索开源代码仓库：**[prime-rl GitHub 代码库](https://github.com/PrimeIntellect-ai/prime-rl)**

> * Read the official **[Prime Mega MoE Blog Post](https://www.primeintellect.ai/blog/prime-mega-moe)**
> * View the **[Announcement on X](https://x.com/PrimeIntellect/status/2115861613261815883)**
> * Explore the **[prime-rl Repository](https://github.com/PrimeIntellect-ai/prime-rl)**

*关注 AI 前沿动态：欢迎在 **[Twitter](https://x.com/intent/follow?screen_name=marktechpost)** 上关注我们、加入 **[15 万+成员的机器学习 Subreddit](https://www.reddit.com/r/machinelearningnews/)**、订阅 **[技术周刊 Newsletter](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526)** 或加入我们的 **[Telegram 交流频道](https://t.me/machinelearningresearchnews)**。*

> *Stay connected with the AI community by following **[Twitter](https://x.com/intent/follow?screen_name=marktechpost)**, joining the **[150k+ ML Subreddit](https://www.reddit.com/r/machinelearningnews/)**, subscribing to **[our Newsletter](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526)**, or joining our **[Telegram Channel](https://t.me/machinelearningresearchnews)**.*

*如果您希望就 GitHub 开源仓库、Hugging Face 主页、产品首发或线上研讨会与我们展开推广合作，欢迎随时 **[联系我们](https://promotions.marktechpost.com/)**。*

> *If you are looking to partner with us for promotions regarding your GitHub repository, Hugging Face page, product release, or webinar, feel free to **[connect with us](https://promotions.marktechpost.com/)**.*

*(本文原载于 [MarkTechPost](https://www.marktechpost.com)，原文标题为 [Prime Intellect Releases Prime Mega MoE: Trainable Fused MoE Kernel, 3.11x Faster Forward Pass](https://www.marktechpost.com/2026/10/29/prime-intellect-prime-mega-moe-fused-moe-kernel-training/)。)*

> *(The post [Prime Intellect Releases Prime Mega MoE: Trainable Fused MoE Kernel, 3.11x Faster Forward Pass](https://www.marktechpost.com/2026/10/29/prime-intellect-prime-mega-moe-fused-moe-kernel-training/) originally appeared on [MarkTechPost](https://www.marktechpost.com).)*
