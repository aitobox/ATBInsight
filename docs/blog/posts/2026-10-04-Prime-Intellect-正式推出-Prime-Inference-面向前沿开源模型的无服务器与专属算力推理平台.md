---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-04
hide:
  - navigation
tags:
  - Prime Intellect
  - Prime Inference
  - vLLM
  - Dynamo
  - Mooncake
  - FlashInfer
  - NVIDIA Blackwell
  - 开源模型
title: "Prime Intellect 正式推出 Prime Inference：面向前沿开源模型的无服务器与专属算力推理平台"
---

# Prime Intellect 正式推出 Prime Inference：面向前沿开源模型的无服务器与专属算力推理平台

> # Prime Intellect Launches Prime Inference: Serverless and Reserved Serving for Frontier Open Models

### 文章背景与核心概要

随着开源前沿大语言模型 (LLM) 参数规模与应用复杂度的飞速跃升，如何在生产环境中以极低延迟、高吞吐和高可靠性提供稳定服务，已成为整个 AI 行业的核心工程瓶颈。知名去中心化 AI 计算与训练团队 Prime Intellect 正式推出了其全新推理平台 —— Prime Inference，提供无服务器端点与跨多数据中心的专属预留算力。该平台深度整合了包括 NVIDIA Blackwell 硬件与 NVIDIA Dynamo、vLLM、Mooncake、FlashInfer 在内的前沿开源技术栈，在公开发布前已在内部承受日均近万亿 Token 的极端压力考验。在 GLM-5.3 等前沿开源模型的基准测试中，该平台不仅实现了 100% 的高可用率，更以接近零失误的工具调用表现树立了开源推理服务的新标杆。Prime Inference 的正式推出，成功打通了从模型强化学习采样、自动化评估到生产部署的完整技术闭环。

---

## 执行摘要

> ## Executive Summary

Prime Intellect 正式推出了 **Prime Inference**，这是一个专为前沿开源模型打造的高性能推理服务平台。该平台跨多个数据中心同时提供灵活的无服务器 (Serverless) 端点与专属预留算力 (Reserved Capacity) 选项。在正式公开发布前，该平台已在团队内部历经高强度实战检验——日均吞吐近一万亿 Token，稳定支撑着强化学习采样 (RL Rollouts)、合成数据生成、模型自动化评估以及长时间运行的代码智能体 (Coding Agents) 任务。通过搭载以 NVIDIA Blackwell 为代表的先进硬件，并深度融合 vLLM、NVIDIA Dynamo、Mooncake 与 FlashInfer 等顶尖开源服务工具链，Prime Inference 实现了极高的吞吐性能、卓越的系统在线率以及接近于零的工具调用 (Tool Call) 失败率。

> Prime Intellect has launched **Prime Inference**, a high-performance serving platform designed specifically for frontier open-source models. Offering both serverless endpoints and reserved capacity across multiple datacenters, the platform processed nearly a trillion tokens per day internally before its public release to handle RL rollouts, synthetic data generation, evaluations, and long-running coding agents. By integrating advanced hardware like NVIDIA Blackwell and combining cutting-edge open-source serving tools (such as vLLM, NVIDIA Dynamo, Mooncake, and FlashInfer), Prime Inference delivers high throughput, exceptional uptime, and near-zero tool-call error rates.

---

## 什么是 Prime Inference？

> ## What is Prime Inference?

Prime Inference 在 Prime Intellect 的开源训练技术体系中充当着基石般的服务层。由于该团队此前已研发了包括 `prime-rl`、验证器 (Verifiers) 以及安全沙盒 (Sandboxes) 等后训练 (Post-training) 关键工具，这一全新推理层的加入使得整体技术架构实现了闭环：线上部署的模型在生产环境中生成的真实运行轨迹 (Production Traces)，能够直接无缝反哺并注入后续的训练迭代循环中。

> Prime Inference serves as the foundational serving layer for Prime Intellect’s open training stack. Because the company already develops post-training tools like `prime-rl`, verifiers, and sandboxes, this new inference layer closes the loop: deployed models generate production traces that directly feed back into subsequent training cycles. 

据 Prime 官方公布的数据，其托管的 [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) 端点在 OpenRouter 平台的性能排行中跻身最快梯队，自上线以来不仅保持着 100% 的极高可用率，其工具调用错误率更是几乎降为零。

> Prime reports that its [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) endpoint ranks among the fastest on OpenRouter, accompanied by a near-zero tool-call error rate and 100% uptime since launch.

### 核心特性与架构亮点

> ### Core Features & Architecture

* **双模服务形态：** 既提供应对弹性波动的无服务器 (Serverless) 端点，也提供支撑稳定工作负载的专属预留算力 (Reserved Capacity)。
* **全面兼容 OpenAI：** 接入极其便捷，开发者只需将标准 OpenAI SDK 地址直接指向 `https://api.pinference.ai/api/v1` 即可完成对接 ([查阅官方文档](https://docs.primeintellect.ai/inference/overview))。
* **高可靠与自动容灾：** 支持跨数据中心自动故障转移 (Failover)，在节点波动时能平滑顺畅地将流量动态路由至健康的部署集群。
* **尖端硬件加持：** 当前全面搭载 NVIDIA Blackwell 架构，同时已做好架构规划，将在不久的将来直接引入支持下一代 Vera Rubin 芯片。
* **统一计费体系：** 配备支持团队级使用量精细追踪的统一账单管理系统 (针对具体各模型的定价细则目前正等待官方完整文档发布)。

> * **Two Modes:** Serverless endpoints for variable demand and reserved capacity for sustained workloads.
> * **OpenAI Compatible:** Easily integrate by pointing any standard OpenAI SDK to `https://api.pinference.ai/api/v1` ([Documentation](https://docs.primeintellect.ai/inference/overview)).
> * **High Reliability:** Automatic failover across datacenters seamlessly routes traffic to healthy deployments.
> * **Hardware:** Powered by NVIDIA Blackwell today, with support for Vera Rubin slated for the near future.
> * **Billing:** Features unified billing with team-level usage tracking (per-model pricing is currently pending full documentation release).

---

## 推理服务栈的工作原理

> ## How the Serving Stack Works

该推理服务栈由 Prime 联合 Inferact 与 NVIDIA 共同协作研发，深度融合了 [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo)、[vLLM](https://github.com/vllm-project/vllm)、[Mooncake](https://github.com/kvcache-ai/Mooncake) 与 [FlashInfer](https://github.com/flashinfer-ai/flashinfer)，并持续将性能调优与 Bug 修复贡献回各个上游开源项目。

> The serving stack is built collaboratively using [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo), [vLLM](https://github.com/vllm-project/vllm), [Mooncake](https://github.com/kvcache-ai/Mooncake), and [FlashInfer](https://github.com/flashinfer-ai/flashinfer) via Inferact and NVIDIA, contributing fixes upstream.

整套架构在设计之初就充分考虑了智能体 (Agent) 类工作负载的特征——在这类复杂任务中，单轮典型的智能体执行往往会在长达 140K Token 的提示词 (Prompt) 基础上再追加约 6K Token 的上下文。Prime 团队利用 SemiAnalysis 打造的 [AgentX](https://inferencex.semianalysis.com/agentx) 基准测试框架，并在模拟注入冷启动请求 (Cold Arrivals) 的严苛环境下对该配置进行了深度基准评测。

> Designed with agentic workloads in mind—where a typical agent turn adds roughly 6K tokens to a 140K-token prompt—Prime benchmarks this configuration using SemiAnalysis's [AgentX](https://inferencex.semianalysis.com/agentx) framework alongside injected cold arrivals.

* **Prefill（首字预填充）与 Decode（增量解码）彻底分离解耦：** 计算密集的预填充 (Prefill) 与访存密集的解码 (Decode) 计算分别运行在独立的物理 GPU 集群上。Dynamo 负责全局动态流量路由调度，而 vLLM 则在各个集群内驱动模型的高效计算。解码节点通过 [NIXL](https://github.com/ai-dynamo/nixl) 极速拉取预计算完毕的 KV 缓存 (KV Cache) 状态，使 p90 级别的 Token 间生成延迟 (Inter-token Latency) 大幅降低了近 40%。
* **感知缓存的智能路由 (Cache-Aware Routing)：** Dynamo 内置的 KV 缓存感知路由器能够精确权衡请求前缀的重合度与当前队列的积压情况，确保同一用户会话在多轮交互中始终绑定在同一解码节点上。同时，Mooncake 还开创性地在主机内存 (Host DRAM) 中构建了二级 KV 缓存池，进一步避免了昂贵的重复计算。

> * **Prefill/Decode Disaggregation:** Prefill and decode operations run on separate GPU groups. Dynamo manages routing while vLLM runs the model on each group. Decoders pull computed KV cache states through [NIXL](https://github.com/ai-dynamo/nixl), resulting in nearly 40% lower p90 inter-token latency.
> * **Cache-Aware Routing:** Dynamo’s KV-aware router carefully weighs cached prefix overlap against queued work, ensuring sessions remain pinned to the same decoder between turns. Mooncake further introduces a secondary KV tier stored directly in host DRAM.

---

## GB200 NVL72 上的 GLM-5.3：核心性能实测数据

> ## GLM-5.3 on GB200 NVL72: Performance Numbers

为达成每位用户每秒 100 个端到端 Token (Tokens/sec) 的极致交互体验目标，Prime 经过精密工程推演，确定了 1:4 的预填充 (Prefill) 与解码 (Decode) 计算资源配比能够最大化单机用户承载上限 —— 在每个用户享受 101 Tokens/秒交互速度且每张 GPU 达到 100 输出 Tokens/秒的峰值效率下，每个预填充计算组可从容并发支撑 66 个独立会话。

> Targeting an interactivity goal of 100 end-to-end tokens per second per user, Prime determined that a 1:4 prefill-to-decode ratio maximized user capacity—achieving 66 sessions per prefill group at 101 tokens/sec per user and 100 output tokens/sec per GPU.

* **DEP8 预填充拓扑：** 在完全相同的硬件配置下，相比 TEP8 拓扑架构提供了约 5 倍的可复用前缀缓存 (Prefix-cache) 容量。
* **优化的预填充配额调度：** 将单张 GPU 每步处理的 Token 配额从 8K 减半降至 4K 后，排队等待时间中位数从 550 毫秒骤降至 110 毫秒，同时首字生成时间 (Time-to-First-Token, TTFT) 中位数亦缩减了约 20%。
* **NVFP4 KV 缓存压缩：** 将多头潜在注意力 (Multi-Head Latent Attention, MLA) 缓存的每行数据从 576 字节压缩至 352 字节，使单个解码节点可容纳的缓存 Token 数量从 1.09M 显著提升至 1.63M。
* **原生 Sparse-MLA 算子内核：** 在 15 个查询 Token (Query Tokens) 条件下耗时仅需约 12.0 微秒 (相比之下分阶段暂存方案为 17.7 微秒，FP8 方案为 13.7 微秒)，不过具体性能表现仍取决于实际工作负载特征。
* **BLHNC KV 内存布局优化：** 将传输描述符 (Transfer Descriptors) 的数量从 19,559 个大幅缩减至约 1,940 个，成功将平均数据传输耗时从 146 毫秒压缩至 78 毫秒。

> * **DEP8 Prefill Topology:** Yields roughly 5× more usable prefix-cache capacity than TEP8 on identical hardware.
> * **Optimized Prefill Budget:** Halving tokens per step from 8K to 4K per GPU decreased median queue wait times from 550 ms to 110 ms, while median time-to-first-token dropped by approximately 20%.
> * **NVFP4 KV Compression:** Reduced each MLA cache row from 576 bytes to 352 bytes, increasing cached tokens per decoder from 1.09M to 1.63M.
> * **Native Sparse-MLA Kernel:** Achieved ~12.0 µs at 15 query tokens (compared to 17.7 µs staged and 13.7 µs FP8), though performance remains workload-dependent.
> * **BLHNC KV Layout:** Reduced transfer descriptors from 19,559 to ~1,940, successfully lowering mean transfer times from 146 ms to 78 ms.

---

## 高度可靠的工具调用能力

> ## Reliable Tool Calls

在自主智能体 (Autonomous Agents) 的实际落地中，模型常常因为生成错误的工具名称或格式畸变的调用参数而导致整个执行流崩溃。为了从底层彻底消除这一痛点，Prime Intellect 团队专门针对 GLM 系列模型的工具调用格式，向 Dynamo 贡献了专用的结构化标签生成器 (Structural-tag Builder)。结合 vLLM 内部集成的 [xgrammar](https://github.com/mlc-ai/xgrammar) 结构化生成约束引擎，该系统能够在解码过程中动态屏蔽违背预期工具规范 (Schema) 的非法 Token，并修复了包括代码块内部 `&lt;` 等实体字符解码失真在内的多种下游解析缺陷。

> Autonomous agents frequently fail when tool calls contain incorrect names or malformed arguments. To solve this, Prime Intellect contributed a structural-tag builder to Dynamo specifically tailored to GLM’s tool format. Coupled with [xgrammar](https://github.com/mlc-ai/xgrammar) in vLLM, the system masks tokens that violate the expected tool schema and fixes downstream parsing bugs (such as improper decoding of `&lt;` entities inside code blocks).

---

## Prime Inference 与竞品对比

> ## Prime Inference vs. Competitors

| 功能特性 | Prime Inference | Together AI | Fireworks AI | Baseten |
| :--- | :--- | :--- | :--- | :--- |
| **无服务器模式 GLM-5.3** | 支持 ([来源](https://www.primeintellect.ai/blog/prime-inference)) | 支持 ([来源](https://docs.together.ai/docs/serverless-models)) | 支持 ([来源](https://artificialanalysis.ai/providers/fireworks)) | 支持 ([来源](https://www.baseten.co/resources/changelog/glm-53-available-on-baseten/)) |
| **GLM-5.3 价格 (每 1M Token 输入 / 输出)** | 尚未在官方文档公布 | $1.40 / $4.40 ([来源](https://docs.together.ai/docs/serverless-models)) | $1.40 / $4.40 ([追踪来源](https://computeprices.com/providers/fireworks-ai/models/glm-5-3)) | $1.40 / $4.40 ([追踪来源](https://computeprices.com/providers/baseten/models/glm-5-3)) |
| **专属或预留算力** | 支持预留算力；一键部署专属实例已列入路线图 | 专属模型端点 ([来源](https://www.together.ai/models-providers/zai-org)) | 按需专属 GPU 部署 ([来源](https://fireworks.ai/models/fireworks/glm-5p3-flash)) | 专属 GPU 部署 ([追踪来源](https://computeprices.com/providers/baseten/models/glm-5-3)) |
| **兼容 OpenAI 的 API** | 支持 | 支持 | 支持 | 支持 |
| **批处理推理** | 已列入路线图 | 支持 ([来源](https://www.together.ai/models-providers/zai-org)) | 此处未作对比 | 此处未作对比 |
| **公开的推理服务技术栈** | 开源方案：Dynamo, vLLM, Mooncake, FlashInfer | Together 自研推理研究技术栈 | Fireworks 自研推理技术栈 | Baseten 推理技术栈 ([来源](https://huggingface.co/docs/inference-providers/providers/baseten)) |

*(竞品价格数据核实于 2026 年 10 月 2 日。价格追踪平台数据由独立第三方价格追踪服务 ComputePrices 提供。)*

> *(Competitor prices verified October 2, 2026. Tracker figures provided via ComputePrices, an independent third-party price tracker.)*

---

## 核心要点总结

> ## Key Takeaways

* **生产就绪的基础设施：** Prime Inference 现已正式上线公测，为前沿开源大模型提供了高度定制的无服务器端点与专属预留算力选项。
* **GB200 极致工程优化：** 深度协同调度 Dynamo、vLLM、Mooncake 以及 FlashInfer，实现了 GLM-5.3 在 GB200 NVL72 集群上的超大规模稳定高效运行。
* **高吞吐架构能效：** 创新的 1:4 预填充/解码分离架构，可在每用户 101 Tokens/秒的高速交互下，支撑单预填充计算组并发承载 66 个会话。
* **显著扩展的内存容量：** 引入 NVFP4 格式的高性能 KV 缓存压缩技术，将单个解码节点容纳的缓存 Token 量从 1.09M 飞跃至 1.63M。
* **明确的未来演进路线：** 高效的大规模批处理推理 (Batch Inference) 功能与一键式专属硬件部署 (1-click Dedicated Deploys) 即将推出。

> * **Live Infrastructure:** Prime Inference is officially live, providing serverless and reserved serving options tailored for frontier open models.
> * **GB200 Optimization:** GLM-5.3 runs at scale on GB200 NVL72 infrastructure leveraging Dynamo, vLLM, Mooncake, and FlashInfer.
> * **High Efficiency:** A 1:4 prefill/decode architecture supports 66 sessions per prefill group at 101 tokens/sec per user.
> * **Expanded Memory Capacity:** NVFP4 KV cache integration expands caching capacity from 1.09M to 1.63M tokens per decoder.
> * **Roadmap:** Batch inference capabilities and one-click dedicated deployments are coming next.

---

## 相关资源与链接

> ## Resources & Links

* 阅读完整的官方 [技术细节解析博客](https://www.primeintellect.ai/blog/prime-inference)
* 查阅官方 [开发与集成文档](https://docs.primeintellect.ai/inference/overview)
* 查看发布在 X 上的 [官方公告推文](https://x.com/PrimeIntellect/status/2106146483003384253)

> * Read the complete [Technical Details](https://www.primeintellect.ai/blog/prime-inference)
> * Explore the [Official Documentation](https://docs.primeintellect.ai/inference/overview)
> * Read the [Announcement on X](https://x.com/PrimeIntellect/status/2106146483003384253)

***

*本文原载于 MarkTechPost。所有知识产权与研究成果均归原项目研究团队所有。*

> *Original post published by MarkTechPost. All credit belongs to the original project researchers.*
