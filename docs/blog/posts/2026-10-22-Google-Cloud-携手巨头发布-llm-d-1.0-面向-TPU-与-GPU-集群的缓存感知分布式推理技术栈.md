---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-22
hide:
  - navigation
tags:
  - llm-d
  - Google Cloud
  - 分布式推理
  - TPU
  - GPU
  - vLLM
title: "Google Cloud 携手巨头发布 llm-d 1.0：面向 TPU 与 GPU 集群的缓存感知分布式推理技术栈"
---

# Google Cloud 携手巨头发布 llm-d 1.0：面向 TPU 与 GPU 集群的缓存感知分布式推理技术栈

> # Google Cloud Ships llm-d 1.0 With Cache-Authority and Cache-Aware Routing for TPU and GPU Fleets

### 文章背景与核心概要

随着大语言模型 (Large Language Model, LLM) 智能体与复杂强化学习 (Reinforcement Learning, RL) 任务的兴起，传统的轮询负载均衡策略在面对极度依赖上下文缓存的复杂请求时显得捉襟见肘，极易导致严重的显存浪费与高延迟。为了攻克这一工业界普遍痛点，Google Cloud 联合 Red Hat、IBM、CoreWeave 以及 NVIDIA 等行业巨头，正式推出了首个开源且云原生 (Kubernetes-native) 的分布式推理框架 llm-d 1.0。llm-d 打破了过去 vLLM 与 SGLang 等模型服务端各自为政的碎片化局面，创新性地引入了前缀感知智能路由、多级分层缓存解耦以及预填充/解码分离编排机制，将模型服务器统一纳管为协同工作的资源池。在高达 17,000 节点的 Google Kubernetes Engine (GKE) 超大规模集群测试中，llm-d 将总体吞吐量提升了 2.9 倍，并在 Ironwood 等新一代 TPU 芯片上将首字延迟削减逾 85%，标志着面向 AI 智能体时代的企业级分布式推理迈向了高可靠、超弹性的生产就绪阶段。

---

## 📌 执行摘要

> ## Executive Summary

Google Cloud 携手 Red Hat、IBM、CoreWeave 以及 NVIDIA，正式联合发布了 **llm-d 1.0**——这是其开源、云原生 (Kubernetes-native) 分布式推理技术栈的首个正式稳定版本。在北美 PyTorch 开发者大会 (PyTorch Conference North America) 上亮相的 llm-d，能够将碎片化的 vLLM 与 SGLang 模型服务器整合为一个统一协调的弹性资源池。传统轮询负载均衡在应对苛刻的私有化部署 AI 智能体 (AI Agent) 与强化学习工作负载时往往捉襟见肘，而 llm-d 专为此类场景量身打造，1.0 版本不仅带来了生产级别的稳定性，还引入了前沿的多租户流控机制以及跨多集群的企业级卓越性能。

> Google Cloud, in collaboration with Red Hat, IBM, CoreWeave, and NVIDIA, has officially released **llm-d 1.0**—the first stable version of its open-source, Kubernetes-native distributed inference stack. Announced at the PyTorch Conference North America, llm-d unifies fragmented vLLM and SGLang model servers into a single coordinated pool. Designed specifically to handle demanding self-hosted agent and reinforcement learning (RL) workloads where traditional round-robin load balancing fails, version 1.0 introduces production-grade reliability, advanced multi-tenant flow control, and enterprise-scale multi-cluster performance.

---

## 什么是 llm-d 1.0？

> ## What is llm-d 1.0?

**llm-d** 诞生于 2025 年，由 Red Hat、IBM 和 Google 联合主导发起，目前已迅速成长为一个蓬勃发展的开源生态，汇聚了来自 25 家以上机构的 500 多名贡献者。该项目于 2026 年 3 月 12 日被正式接纳为 **云原生计算基金会 (CNCF) 沙箱项目 (Sandbox project)**，并严格遵循 **Apache 2.0 开源许可协议**。

> Founded in 2025 and led jointly by Red Hat, IBM, and Google, **llm-d** has grown into a thriving ecosystem featuring over 500 contributors from 25+ organizations. It was accepted as a **CNCF Sandbox project** on March 12, 2026, and is licensed under the **Apache 2.0 license**.

尽管在早期的迭代版本中，团队已经陆续探索并引入了诸如前缀感知路由 (Prefix-Aware Routing)、键值缓存 (KV Cache) 卸载转储、预填充/解码分离解耦 (Prefill/Decode Disaggregation)、超宽专家并行 (Wide Expert Parallelism) 以及批量推理等基石特性，但 **1.0 正式版本** 的核心焦点在于对这些模块进行工业级加固，全面支撑企业在日常生产环境下的持续运维管理 (Day-2 Operations)。

> While earlier iterations introduced foundational features—such as prefix-aware routing, KV cache offloading, prefill/decode disaggregation, wide expert parallelism, and batch inference—**Version 1.0** focuses heavily on hardening these components for production environments (Day-2 operations).

---

## llm-d 1.0 带来哪些全新突破？

> ## What's New in llm-d 1.0?

* **多租户服务质量保障 (QoS)**：兼具优先级与公平感知的 [流量控制机制 (Flow Control)](https://llm-d.ai/docs/well-lit-paths/foundations/flow-control)，有效杜绝了偶发性迸发的智能体循环调用抢占算力、导致对延迟敏感的普通用户请求发生饥饿的现象。
* **稳固的 v1 核心基石**：全链路加固的请求调用路径与标准化的稳定 API，已在多种云平台环境以及异构硬件加速芯片上完成全方位生产验证。
* **零宕机平滑升级**：由热备方案保障的高可用路由网关，辅以创新的 [DisaggregatedSet](https://llm-d.ai/docs/dev/architecture/model-server-orchestration/disaggregatedset) 资源编排机制，支持预填充 (Prefill) 与解码 (Decode) 服务池的安全协同滚动更新。
* **智能体感知服务体系**：具备会话感知的路由策略、话轮优先级调度机制，以及原生的 Responses API 状态管理能力。
* **异步推理处理架构**：通过 [llm-d-async-processor](https://github.com/llm-d/llm-d-async) 处理器，能够自动从 Google Cloud Pub/Sub 或 Redis 中无缝拉取批处理作业，充分压榨集群中的闲置潮汐算力。
* **扩展的 TPU 原生支持**：深度集成 [TorchTPU](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/)，让 PyTorch 模型能够在 Google TPU 上的上游 vLLM 与 SGLang 实例中原生高能效运行。

> * **Multi-Tenant Quality of Service (QoS):** Priority and fairness-aware [flow control](https://llm-d.ai/docs/well-lit-paths/foundations/flow-control) prevents bursty agent loops from starving latency-sensitive user requests.
> * **Stable v1 Foundation:** Hardened request paths and stable APIs validated across multiple cloud environments and diverse hardware accelerators.
> * **Zero-Downtime Upgrades:** Router high availability backed by hot standby options, alongside the [DisaggregatedSet](https://llm-d.ai/docs/dev/architecture/model-server-orchestration/disaggregatedset) mechanism, which safely rolls prefill and decode pools together.
> * **Agent-Aware Serving:** Session-aware routing, turn-priority scheduling, and native Responses API state management.
> * **Asynchronous Inference:** The [llm-d-async-processor](https://github.com/llm-d/llm-d-async) pulls jobs seamlessly from Google Cloud Pub/Sub or Redis into available slack capacity.
> * **Expanded TPU Support:** [TorchTPU](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/) integration enables PyTorch models to run natively inside upstream vLLM and SGLang instances on Google TPUs.

---

## llm-d 如何进行智能请求路由？

> ## How Does llm-d Route Requests?

llm-d 路由器基于 Kubernetes Gateway API 推理扩展 (Inference Extension) 深度构建。它能够动态追踪并掌握各个副本节点分别缓存了哪些特定的上下文提示词前缀，结合当前各服务器的实际负载水线与预估延迟，将新传入的请求毫秒级精准投递至已驻留对应上下文的节点上。

> The llm-d router builds on top of the Kubernetes Gateway API Inference Extension. It dynamically tracks which replicas hold specific cached prefixes, factors in current server loads and predicted latencies, and routes requests precisely where the necessary context already lives. 

当硬件加速芯片的高带宽内存 (High Bandwidth Memory, HBM) 接近饱和时，KV Cache 会通过专用连接组件——如 vLLM 的 `OffloadingConnector`、`Mooncake` 或是 SGLang 的 `HiCache`——平滑转储至宿主机 CPU 内存、本地高速 NVMe SSD 乃至托管的 Lustre (Managed Lustre) 分布式存储中。此外，架构将算力密集的 **预填充 (Prefill)** 任务与显存带宽受限的 **解码 (Decode)** 任务进行彻底物理分离，分别部署在相互独立的优化资源池中，互不干扰。

> When accelerator HBM (High Bandwidth Memory) fills up, the KV cache seamlessly migrates to host CPU memory, local SSDs, or Managed Lustre storage using connectors like vLLM’s `OffloadingConnector`, `Mooncake`, or SGLang’s `HiCache`. Furthermore, compute-heavy **prefill** operations and memory-bound **decode** operations are split into distinct, optimized pools.

---

## 性能基准测试亮点

> ## Benchmark Highlights

已公布的基准测试结果（由 Google、Snap 以及 Zenteiq 官方实测披露）展现了惊人的性能跃升：

> Published benchmarks (self-reported by Google, Snap, and Zenteiq) highlight massive performance gains:

* **Ironwood TPU (TPU 7x)**：前缀感知路由与宿主机内存卸载技术的双剑合璧，将中位数首字延迟 (Time to First Token, TTFT) 大幅削减了 **85% 以上**；与标准 Kubernetes 服务相比，总体吞吐量实现了 **2.4 倍** 的飞跃。
* **Gemini 平台**：提示词前缀缓存命中率直接翻倍，从 **35% 飙升至 70%**。在代码编程智能体场景下，首字延迟降低了超过 35%；在突发高并发对话流量冲击下，P95 首字延迟更是下降了 **50% 以上**。
* **17,000 节点 GKE 超大集群部署**：在跨越 3 个独立计算集群的超大规模部署中，聚合吞吐量提升了 **2.9 倍**，在额外系统开销低于 1% 的前提下始终保持 **99.9% 的请求成功率**。
* **A3 Mega 服务器集群 (70B 模型实测)**：借助托管 Lustre 与宿主机 CPU RAM 内存卸载技术，在处理 50k 超长 Token 提示词时将 TTFT 缩短了 **约 40%**，端到端延迟降低 30%，整体 GPU 机时成本缩减近 60%。
* **强化学习时间片复用 (RL Time-Slicing)**：将推理任务巧妙穿插进强化学习训练的空闲周期中，使硬件加速芯片的有效占空比 (Duty Cycle) 从约 40% **跃升至 70% 以上**。

> * **Ironwood TPU (TPU 7x):** Prefix-aware routing combined with host memory offloading slashed median TTFT (Time to First Token) by **over 85%**, while boosting total throughput **2.4x** compared to standard Kubernetes services.
> * **Gemini Platform:** Prefix cache hit rates doubled from **35% to 70%**. TTFT dropped by over 35% for coding agents, and P95 TTFT fell **over 50%** under bursty chat traffic.
> * **17,000-Node GKE Deployment:** Scaled aggregate throughput **2.9x** across 3 distinct clusters, maintaining a **99.9% success rate** with under 1% overhead.
> * **A3 Mega (70B Model):** Managed Lustre and CPU RAM offloading improved TTFT by **~40%** on 50k-token prompts, reducing end-to-end latency by 30% and GPU-hours by nearly 60%.
> * **RL Time-Slicing:** Interleaving inference into idle reinforcement learning cycles lifted the accelerator duty cycle **above 70%** (up from ~40%).

早期采用者的实测数据同样印证了这些里程碑式的提升：**Snap** 报告其前缀缓存命中率攀升至 75%～80%；**Zenteiq** 实现了超过 **4 倍的吞吐量暴涨**（每 1,000 颗 TPU v6e 芯片的日处理 Token 量从 14.7 亿狂飙至 59.7 亿）；而 IBM 的一项实际演示更是成功并发支撑了 **3,000 个编程智能体** 同时高效运行，成本仅为传统标准商业 API 调用的极小一部分。

> Adopter results mirror these milestones: **Snap** reports prefix cache hit rates reaching 75–80%, **Zenteiq** achieved over **4x throughput** (surging from 1.47B to 5.97B daily tokens per 1,000 TPU v6e chips), and an IBM demonstration successfully served **3,000 concurrent coding agents** at a fraction of standard API pricing.

---

## 方案横向对比：llm-d vs. NVIDIA Dynamo vs. AIBrix

> ## Comparative Analysis: llm-d vs. NVIDIA Dynamo vs. AIBrix

| 特性维度 | llm-d 1.0 | NVIDIA Dynamo | AIBrix |
| :--- | :--- | :--- | :--- |
| **最新版本** | 1.0 (2026 年 10 月 20 日) | [v1.5.1 (2026 年 10 月 6 日)](https://docs.nvidia.com/dynamo/reference/compatibility) | [v0.7.0 (2026 年 6 月 16 日)](https://github.com/vllm-project/aibrix/releases/tag/v0.7.0) |
| **开源协议** | Apache 2.0 | Apache 2.0 | Apache 2.0 |
| **治理模式** | CNCF 沙箱项目 | NVIDIA 主导 (`ai-dynamo` 组织) | vLLM 项目组织 (源自 ByteDance) |
| **支持引擎** | vLLM, SGLang | SGLang, TensorRT-LLM, vLLM | vLLM, SGLang, TensorRT-LLM |
| **适配芯片** | [NVIDIA, AMD, Intel GPU 与 Google TPU](https://presentations.cncf.io/projects/llm-d/) | NVIDIA GPU (Blackwell, Hopper, Ada, Ampere) | 异构/混合 GPU 算力 |
| **缓存感知路由** | 支持 (前缀与负载联合感知) | 支持 (KV 感知) | 支持 (网关级路由) |
| **分层缓存体系** | HBM, CPU, SSD, Managed Lustre | GPU 显存, CPU, SSD, 远端存储 (KVBM) | 分布式 KV 缓存 |
| **P/D 预填充与解码解耦** | 支持 (`DisaggregatedSet`) | 支持 | 支持 |
| **代表性基准成果** | 17,000 节点下吞吐量提升 2.9 倍 (官方实测) | Qwen3-Coder 480B 首字延迟减半 ([Baseten](https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo/)) | 未披露 |

> | Feature | llm-d 1.0 | NVIDIA Dynamo | AIBrix |
> | :--- | :--- | :--- | :--- |
> | **Latest Version** | 1.0 (Oct 20, 2026) | [v1.5.1 (Oct 6, 2026)](https://docs.nvidia.com/dynamo/reference/compatibility) | [v0.7.0 (Jun 16, 2026)](https://github.com/vllm-project/aibrix/releases/tag/v0.7.0) |
> | **License** | Apache 2.0 | Apache 2.0 | Apache 2.0 |
> | **Governance** | CNCF Sandbox | NVIDIA-led (`ai-dynamo` org) | vLLM project org (ByteDance origin) |
> | **Engines** | vLLM, SGLang | SGLang, TensorRT-LLM, vLLM | vLLM, SGLang, TensorRT-LLM |
> | **Accelerators** | [NVIDIA, AMD, Intel GPUs, Google TPU](https://presentations.cncf.io/projects/llm-d/) | NVIDIA GPUs (Blackwell, Hopper, Ada, Ampere) | Mixed/Heterogeneous GPUs |
> | **Cache-Aware Routing** | Yes (Prefix & load-aware) | Yes (KV-aware) | Yes (Gateway routing) |
> | **KV Cache Tiers** | HBM, CPU, SSD, Managed Lustre | GPU, CPU, SSD, remote storage (KVBM) | Distributed KV cache |
> | **P/D Disaggregation** | Yes (`DisaggregatedSet`) | Yes | Yes |
> | **Headline Result** | 2.9x throughput, 17k nodes (self-reported) | 2x faster TTFT, Qwen3-Coder 480B ([Baseten](https://www.baseten.co/blog/how-baseten-achieved-2x-faster-inference-with-nvidia-dynamo/)) | Not disclosed |

*注：这些分布式推理框架之间是相互补充而非互斥割裂的关系。例如，像 CoreWeave 这样的 AI 云基础设施提供商已将 llm-d 与 Dynamo 协同部署，而 NVIDIA 也在积极将 Dynamo 中的优秀组件反哺贡献至 llm-d 开源生态中。*

> *Note: These tools are complementary rather than mutually exclusive. For instance, infrastructure providers like CoreWeave deploy llm-d alongside Dynamo, and NVIDIA actively contributes Dynamo components back into the llm-d ecosystem.*

---

## 如何上手部署 llm-d 1.0？

> ## How to Deploy llm-d 1.0

在 Google Cloud 平台上，[GKE 推理网关 (GKE Inference Gateway)](https://cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway#llm-d-router) 将 llm-d 路由能力包装为全托管云服务，原生支持跨越 [多个集群与不同可用区 (Multiple Clusters and Regions)](https://cloud.google.com/kubernetes-engine/docs/how-to/setup-multicluster-inference-gateway) 运行并提供全球故障转移容灾。系统结合 KEDA 与 HPA，根据任务排队深度与预估响应延迟动态弹性伸缩工作节点池，同时借助 Kueue 精细化管控每个具体模型的配额。

> On Google Cloud, the [GKE Inference Gateway](https://cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway#llm-d-router) provides the llm-d router as a fully managed service capable of spanning [multiple clusters and regions](https://cloud.google.com/kubernetes-engine/docs/how-to/setup-multicluster-inference-gateway) with global failover. KEDA and HPA scale worker pools based on queue depth and predicted latency, while Kueue manages granular per-model quotas. 

对于私有或自定义的 Kubernetes 基础架构环境，官方提供的经过生产验证的 Helm Charts 允许工程团队在统一接入端点后方，轻松快速拉起混合部署的 TPU 与 GPU 算力集群。Google 官方推荐采用循序渐进的分阶段落地策略：
1. **起步阶段**：首先在现有的 vLLM 或 SGLang 部署前端引入前缀感知路由层；
2. **深化阶段**：按需逐步叠加多租户流量控制、[多级分层 KV 缓存卸载转储](https://llm-d.ai/docs/well-lit-paths/foundations/tiered-prefix-cache) 以及预填充与解码解耦架构。

> For custom Kubernetes environments, verified Helm charts allow teams to spin up mixed TPU and GPU fleets behind a unified endpoint. Google recommends a staged adoption path:
> 1. Begin by placing prefix-aware routing in front of an existing vLLM deployment.
> 2. Incrementally layer in flow control, [tiered KV offloading](https://llm-d.ai/docs/well-lit-paths/foundations/tiered-prefix-cache), and prefill/decode disaggregation.

---

## 核心要点总结

> ## Key Takeaways

* **生产就绪的工业级基石**：llm-d 1.0 带来稳定的 v1 核心 API，专为应对复杂企业级 AI 智能体与大规模强化学习管线进行了深度优化。
* **高阶算力与服务编排**：全面解锁多租户流控保障、路由器高可用热备以及 `DisaggregatedSet` 预填充与解码协同滚动发布等关键架构能力。
* **超大规模实战验证**：在工业级海量负载中久经淬炼——成功将 Google Gemini 平台的提示词前缀缓存命中率翻倍至 70%，并在 17,000 个节点的 GKE 超大集群中斩获了 2.9 倍的吞吐量跃升。

> * **Production-Ready Foundation:** llm-d 1.0 delivers stable v1 APIs optimized for complex enterprise agent and RL pipelines.
> * **Advanced Orchestration:** Features new capabilities like multi-tenant flow control, router high availability, and `DisaggregatedSet` rollouts.
> * **Proven Scale:** Validated on massive deployments—doubling Gemini prefix cache hit rates to 70% and scaling a 17,000-node GKE cluster by 2.9x.

---

## 参考资料与相关链接

> ## References & Resources

* 阅读官方发布公告：[Google Cloud 官方博客](https://cloud.google.com/blog/topics/ai-infrastructure/llm-d-1-0-an-open-source-stack-for-distributed-inference) | [IBM Research 官方专栏](https://research.ibm.com/blog/llmd-1-0-is-ready-for-production-inference-serving)
* 探索开源代码：[GitHub 代码仓库](https://github.com/llm-d/llm-d)
* 查阅官方文档：[GKE 架构文档](https://llm-d.ai/docs/infrastructure/providers/gke) | [Prism 基准测试横向对比](https://prism.llm-d.ai/)

> * Read the official announcements: [Google Cloud Blog](https://cloud.google.com/blog/topics/ai-infrastructure/llm-d-1-0-an-open-source-stack-for-distributed-inference) | [IBM Research Post](https://research.ibm.com/blog/llmd-1-0-is-ready-for-production-inference-serving)
> * Explore the code: [GitHub Repository](https://github.com/llm-d/llm-d)
> * Official documentation: [GKE Docs](https://llm-d.ai/docs/infrastructure/providers/gke) | [Prism Benchmark Comparison](https://prism.llm-d.ai/)

*(原始报道发布于 [MarkTechPost](https://www.marktechpost.com/2026/10/20/llm-d-1-0-open-source-distributed-inference-stack/)。)*

> *(Original coverage published by [MarkTechPost](https://www.marktechpost.com/2026/10/20/llm-d-1-0-open-source-distributed-inference-stack/).)*
