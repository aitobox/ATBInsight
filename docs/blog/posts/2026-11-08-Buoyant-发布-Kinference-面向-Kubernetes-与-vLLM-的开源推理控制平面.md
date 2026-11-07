---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-11-08
hide:
  - navigation
tags:
  - Buoyant
  - Kinference
  - Kubernetes
  - vLLM
  - KV-Cache
  - AI推理
title: "Buoyant 发布 Kinference：面向 Kubernetes 与 vLLM 的开源推理控制平面"
---

# Buoyant 发布 Kinference：面向 Kubernetes 与 vLLM 的开源推理控制平面

> # Buoyant Releases Kinference: An Open Source Inference Control Plane for Kubernetes and vLLM

### 文章背景与核心概要
著名服务网格 Linkerd 的幕后公司 Buoyant 近日正式开源了 Kinference，这是一款专为在 Kubernetes 上构建高性能大模型推理平台打造的控制平面。在大语言模型推理集群中，不同计算节点的显存缓存状态差异巨大，传统的四层或七层无状态负载均衡往往会导致宝贵的键值缓存无法复用。Kinference 坐落于模型服务器集群前方，将 vLLM 视作数据平面，自身充当控制平面，通过深度感知键值缓存分布、声明式路由策略与多租户隔离治理，使前缀重合场景下的首字延迟大幅降低约 95%，为企业内部多模型、多租户的 AI 推理平台化运营提供了全新解法。

---

著名服务网格 Linkerd 的母公司 Buoyant 正式[发布了 Kinference](https://www.buoyant.io/blog/introducing-kinference)，这是一个专门用于在 Kubernetes 上构建高性能 AI 推理平台的开源项目。Kinference 定位于面向 Kubernetes 和 vLLM 的推理控制平面 (Inference Control Plane)，它部署在一组 [vLLM](https://vllm.ai/) 工作节点前方，负责智能化地统筹与分发推理请求。通过在单一架构层中统一集成路由策略、Token 速率限制、键值缓存 (KV-Cache) 感知负载均衡以及多租户指标统计，Kinference 专注于模型服务器之上的基础设施层——特别适合需要向企业内部众多业务方同时提供多款开源权重模型的研发团队。

> Buoyant, the company behind Linkerd, has [released Kinference](https://www.buoyant.io/blog/introducing-kinference), an open-source project designed for building high-performance inference platforms on Kubernetes. Acting as an inference control plane for Kubernetes and vLLM, Kinference sits in front of a fleet of [vLLM](https://vllm.ai/) workers to intelligently govern request distribution. By applying routing policies, token rate limits, KV-cache-aware load balancing, and per-tenant metrics within a single layer, it targets the infrastructure layer above the model server—ideal for development teams serving multiple open-weight models to various internal clients.

该项目已在 [GitHub 上基于 Apache 2.0 协议开源](https://github.com/Kinference-AI/kinference)，当前发布的版本为 [v0.1.0-alpha.7](https://kinference.ai/docs/getting-started/)。

> The project is [Apache 2.0 licensed on GitHub](https://github.com/Kinference-AI/kinference), and its current release is [v0.1.0-alpha.7](https://kinference.ai/docs/getting-started/).

---

## 📌 核心概述

> ## 📌 Executive Summary

* **项目定位：** 版本为 `v0.1.0-alpha.7`，采用 Rust 语言编写并基于 Apache 2.0 协议开源，完全通过 5 个 Kubernetes 自定义资源定义 (Custom Resource Definition, CRD) 进行声明式配置。
* **运行环境：** 面向任何搭载 GPU 且运行 vLLM 的 Kubernetes 集群 (Buoyant 在基准测试中为每个推理池配置了 3 张 L40S GPU)。
* **性能收益：** 相较于原生 Kubernetes Service 路由，在具有大量共享前缀的高负载场景下带来了显著的性能飞跃。
* **最佳表现：** 在共享前缀的工作负载中，首字延迟 (Time-to-First-Token, TTFT) 中位数从 6.88 秒断崖式下降至 0.31 秒，大幅降低约 95%。
* **最差表现：** 对于完全没有共享前缀的提示词请求，中位数 TTFT 未见明显改善 (6.92 秒对比 6.83 秒)。

> * **Project Scope:** Version `v0.1.0-alpha.7`, written in Rust under the Apache 2.0 license, configured via 5 Kubernetes Custom Resource Definitions (CRDs).
> * **Environment:** Designed for any GPU-enabled Kubernetes cluster running vLLM (Buoyant's benchmarks utilized 3 L40S GPUs per pool).
> * **Performance Impact:** Significant gains on prefix-heavy traffic compared to standard Kubernetes Service routing.
> * **Best Case:** Median Time-to-First-Token (TTFT) dropped dramatically from 6.88s to 0.31s (~95% reduction) on shared-prefix workloads.
> * **Worst Case:** No notable median TTFT improvement for prompts lacking shared prefixes (6.92s vs 6.83s).

---

## 什么是 Kinference？

> ## What is Kinference?

Kinference 是一个由策略驱动的控制平面，能够将原生的 Kubernetes 和 vLLM 部署转化为一套功能完备的多租户 AI 推理平台。正如 [Buoyant 官方 FAQ](https://kinference.ai/) 所精辟总结的那样：**vLLM 充当数据平面，而 Kinference 则充当控制平面。**

> Kinference is a policy-driven control plane that transforms standard Kubernetes and vLLM deployments into a comprehensive, multi-tenant inference platform. As [Buoyant’s FAQ](https://kinference.ai/) puts it: **vLLM acts as the data plane, while Kinference acts as the control plane.**

---

## Kinference 的工作原理是什么？

> ## How Does Kinference Work?

整个系统的底层架构主要由两大核心组件构成：**流量网关 (Traffic Gateway)** 与**推理处理器 (Inference Handler)**。根据其 [GitHub README](https://github.com/Kinference-AI/kinference) 介绍，处理器对外暴露了一个 gRPC 接口，用于细致评估所有流入的请求，在完成判断后不仅会返回最佳的目标服务终端节点 (Endpoint)，还会根据策略需要对请求体进行动态修改。该组件能够与诸如 [Buoyant Gateway](https://github.com/BuoyantIO/gateway/) 这类网关代理实现无缝配合。

> The system architecture consists of two main components: a **traffic gateway** and an **inference handler**. According to the [GitHub README](https://github.com/Kinference-AI/kinference), the handler exposes a gRPC interface that evaluates incoming requests and returns a chosen endpoint alongside a potentially mutated body. This pairs seamlessly with a proxy such as the [Buoyant Gateway](https://github.com/BuoyantIO/gateway/).

Kinference 会主动监听 vLLM 的 KV-Cache 事件以及底层引擎的各项实时指标，并在内部借助 NVIDIA 的 `dynamo-kv-router` 库高效处理缓存事件。系统的全部配置均通过 5 个专用的 CRD 进行统一纳管：

> Kinference actively monitors vLLM KV-cache events and engine metrics, leveraging NVIDIA’s `dynamo-kv-router` crate for cache event processing. Configuration is managed entirely through 5 specialized CRDs:

* `GatewayBackend`
* `InferencePolicy`
* `InferencePool`
* `InferenceProvider`
* `InferenceWorkerSet`

> * `GatewayBackend`
> * `InferencePolicy`
> * `InferencePool`
> * `InferenceProvider`
> * `InferenceWorkerSet`

### 深入理解推理策略 (Inference Policies)

> ### Understanding Inference Policies

推理策略提供了极其灵活的声明式规则，能够根据租户身份、请求的目标模型、GPU 推理池的实时健康状态以及自定义语义标签等多维度条件，精准决定请求该如何调度或直接拒绝。项目官方给出的[策略示例](https://kinference.ai/)展示了五种经典的核心路由范式：

> Inference policies provide declarative rules determining how requests are routed or rejected based on criteria like tenant identification, requested model, GPU pool state, and semantic tags. [Example policies](https://kinference.ai/) from the project showcase five core routing patterns:

* **简单任务降本路由 (Simple to Cheaper)：** 将复杂度较低的提示词路由到更小、成本更低的模型上；除非大模型节点上存在高度重合的缓存能够让大模型处理得更快。
* **突发流量外溢上云 (Burst to Cloud)：** 当本地工作节点的排队请求数超过 2 个时自动跳过，平滑降级外溢至外部云服务提供商 (例如 Amazon Bedrock)。
* **隐私数据本地驻留 (PII Stays Local)：** 一旦触发个人身份信息 (Personally Identifiable Information, PII) 标签，立即剥离所有外部云端提供商，并在无可用本地节点时采用严格的熔断拒绝策略 (`onEmpty: Reject`)。
* **空闲 GPU 批处理 (Batch on Idle GPUs)：** 将非实时的批量推理请求精准定向到 KV-Cache 显存占用率低于 70% 的低负载工作节点。
* **模型别名解耦 (Model Aliasing)：** 对外暴露一个全局统一的稳定服务名称 (例如 `standard-model`)，底层则动态挂载并调度多个不同版本的实际模型。

> * **Simple to Cheaper:** Route low-complexity prompts to a smaller model, unless cache overlap makes a larger model faster.
> * **Burst to Cloud:** Skip workers with more than 2 queued prompts and fall back to external providers like Bedrock.
> * **PII Stays Local:** Strip external providers when a PII tag is triggered, failing closed with `onEmpty: Reject`.
> * **Batch on Idle GPUs:** Direct batch requests exclusively to workers operating under 70% KV-cache usage.
> * **Model Aliasing:** Expose a single stable name (e.g., `standard-model`) backed dynamically by multiple underlying models.

绝大多数策略规则最终都会以 `minimize: PredictedTTFT` 作为决策目标。Kinference 通过综合评估各候选节点的缓存重叠率 (Cache Overlap) 与当前队列排队深度，智能预估出每个候选节点的首字延迟。所有策略文件均可通过 Git 实行声明式版本管理 (GitOps)，并支持在离线状态下使用 `kinfctl` 命令行工具进行语法与逻辑校验。

> Most rules conclude with `minimize: PredictedTTFT`. Kinference predicts the time-to-first-token for each candidate endpoint by calculating cache overlap and queue depth. Policies are maintained directly in Git and can be validated offline using the `kinfctl` CLI.

---

## 基准测试性能表现

> ## Benchmark Performance

Buoyant 在官方发布的[对比基准测试中，将 Kinference 与原生 Kubernetes 负载均衡进行了全面对照](https://www.buoyant.io/blog/distributed-inference-benchmarks-kinference-vs-plain-kubernetes)。在各组测试配置中，均部署了 3 个 vLLM 0.31.0 Pod 实例，分别独占一张 L40S GPU 并加载 [Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) 模型；测试请求负载由 [GuideLLM](https://github.com/vllm-project/guidellm) 0.8.1 工具模拟生成。基准对照组 (Baseline) 采用了标准的 Kubernetes ClusterIP Service，依赖底层 `kube-proxy` 对每个连接进行随机轮询分发。

> Buoyant evaluated Kinference in a [comparative benchmark against plain Kubernetes load balancing](https://www.buoyant.io/blog/distributed-inference-benchmarks-kinference-vs-plain-kubernetes). Each test configuration utilized three vLLM 0.31.0 pods, running on individual L40S GPUs serving the [Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) model under workloads generated by [GuideLLM](https://github.com/vllm-project/guidellm) 0.8.1. The baseline relied on a standard ClusterIP Service using `kube-proxy` for random pod routing per connection.

### 低负载延迟测试结果 (TTFT 中位数)

> ### Unloaded Latency Results (Median TTFT)

| 工作负载 | Kubernetes Service | Kinference | 性能变化 |
| :--- | :--- | :--- | :--- |
| **对照组 (无共享前缀)** | 6.92 s | 6.83 s | 无显著差异 |
| **共享前缀** | 6.88 s | 0.31 s | 约降低 95% |
| **多轮对话 (Multiturn)** | 1.70 s | 0.59 s | 约降低 65% |

此外，共享前缀场景下的端到端延迟中位数降低了 45%，多轮对话场景下降低了 32%。而在完全无共享前缀的对照流量中，95 分位 (P95) 的 TTFT 从 21.46 秒大幅优化至 12.33 秒，Buoyant 将这一提升归功于 Kinference 具备的智能排队感知负载均衡机制。

> Additionally, median end-to-end latency dropped by 45% for shared-prefix workloads and 32% for multiturn. For control traffic, the 95th percentile TTFT improved from 21.46s down to 12.33s, which Buoyant attributes to intelligent, queue-aware balancing.

在衡量有效吞吐量 (Goodput，即满足严格 TTFT 服务等级目标 SLO 的每分钟完成请求数) 的集群容量压力测试中：

* **共享前缀峰值有效吞吐量：** 达到 103.0 req/min，而原生模式仅为 14.0 req/min (提升约 7.4 倍)。
* **多轮对话峰值有效吞吐量：** 达到 82.7 req/min，原生模式为 23.8 req/min (提升约 3.5 倍)。
* *注：* 在所有测试的并发梯度下，原生的 Kubernetes Service 基准均未能达成既定的 SLO 目标。

> In capacity tests measuring goodput (requests per minute meeting a strict TTFT Service Level Objective):
> * **Shared-prefix peak goodput:** 103.0 vs. 14.0 req/min (~7.4x increase).
> * **Multiturn peak goodput:** 82.7 vs. 23.8 req/min (~3.5x increase).
> * *Note:* The standard Service baseline failed to meet the target SLO at any tested concurrency level.

*(声明：上述基准测试指标均为官方自测数据，且基准对照组仅对比了随机路由方案，并未与 `llm-d` 或 `Dynamo` 等其他缓存感知路由方案进行横向评测。此外，测试中选取的 8 秒与 4 秒 SLO 阈值更偏向于离线批处理与 AI 智能体工作负载，而非超低延迟的实时对话场景。)*

> *(Disclaimer: These metrics are self-reported, and the baseline relies on random routing rather than alternative cache-aware routers like `llm-d` or `Dynamo`. Furthermore, the chosen SLOs of 8s and 4s are oriented toward offline batch/agent workloads rather than real-time chat.)*

---

## 特性横向对比：Kinference vs. llm-d、Dynamo 与 Production Stack

> ## Feature Comparison: Kinference vs. llm-d, Dynamo, and Production Stack

| 特性对比 | Kinference | [llm-d](https://github.com/llm-d/llm-d) | [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo) | [vLLM Production Stack](https://github.com/vllm-project/production-stack) |
| :--- | :--- | :--- | :--- | :--- |
| **主导机构 / 赞助方** | [Buoyant](https://www.buoyant.io/blog/introducing-kinference) | CNCF Sandbox (Red Hat, Google Cloud, IBM, CoreWeave, NVIDIA) | NVIDIA | vLLM 官方项目组 |
| **开源协议** | Apache 2.0 | Apache 2.0 | Apache 2.0 | Apache 2.0 |
| **成熟度** | v0.1.0-alpha.7 | v0.7 (2026 年 5 月) | 1.x (1.5.1 容器镜像) | 参考架构规范 (Reference Stack) |
| **支持的推理引擎** | vLLM *(已规划 SGLang 与 TensorRT-LLM)* | vLLM, SGLang | vLLM, SGLang, TensorRT-LLM | vLLM |
| **KV-Cache 感知路由** | 支持，基于预估 TTFT | 支持，基于前缀缓存与预估延迟 | 支持，集成 KV 感知路由器 | 基于会话 *(前缀感知开发中)* |
| **声明式路由策略 CRD** | 支持 (`InferencePolicy`) | README 中未作说明 | README 中未作说明 | README 中未作说明 |
| **外溢至第三方云服务** | 支持 (`InferenceProvider`) | README 中未作说明 | README 中未作说明 | README 中未作说明 |
| **预填充/解码分离 (Disaggregated Prefill/Decode)** | 暂未披露 | 支持 | 支持 | 处于规划路线图中 |
| **多租户管控能力** | 支持按租户指标监控 *(速率限制规划中)* | 支持多租户服务的流量控制 | 支持通过 GAIE 实现网关级速率限制 | README 中未作说明 |
| **核心基准测试表现** | 相较于 kube-proxy 降低 95% TTFT 中位数 (3x L40S) | 相较于轮询机制提升 3 倍吞吐量、TTFT 加速 2 倍 (4x MI300X) | 借助 KV 感知路由实现 TTFT 加速 2 倍 (Baseten 测试) | 暂未披露 |

Kinference 最独特的核心竞争优势在于其对平台**治理与管控**的高度聚焦——提供了完善的高级路由策略、模型别名抽象、外部云提供商降级外溢以及细粒度多租户审计统计能力；而相比之下，`llm-d` 和 Dynamo 则更多聚焦于底层的极致执行性能、Prefill/Decode 分离架构以及更广泛的底层推理引擎适配。

> Kinference’s unique differentiator is its focus on governance—providing advanced policies, model aliasing, external provider fallbacks, and tenant accounting—whereas `llm-d` and Dynamo specialize primarily in raw execution performance, disaggregation, and broader engine support.

---

## 部署指南与快速上手

> ## Deployment and Availability

根据[官方文档指南](https://kinference.ai/docs/getting-started/)，快速上手仅需执行以下几个清晰简单的步骤：

1. 安装 Gateway API v1.5.1 版本的 CRD 资源；
2. 部署 Buoyant 网关的 Helm Chart；
3. 安装部署 Kinference 的 Helm Chart。

> Getting started requires a few straightforward steps outlined in the [official guide](https://kinference.ai/docs/getting-started/):
> 1. Install Gateway API v1.5.1 CRDs.
> 2. Deploy the Buoyant gateway Helm chart.
> 3. Install the Kinference chart.

Kinference 原生暴露了标准的 Prometheus 监控指标，并开箱即用地提供了预置的 [Grafana 仪表盘看板](https://kinference.ai/docs/guides/monitoring/)。其核心监控指标涵盖了首字延迟 (TTFT)、字间延迟 (Inter-Token Latency, ITL)、端到端总延迟，以及提示词中命中缓存与未命中缓存的 Token 比例分布，且主要按照租户维度进行多层级切分与展示。

> Kinference exposes native Prometheus metrics and comes equipped with pre-built [Grafana dashboards](https://kinference.ai/docs/guides/monitoring/). Tracked metrics include TTFT, Inter-Token Latency (ITL), end-to-end latency, and ratios of cached versus uncached prompt tokens, broken down primarily on a per-tenant basis.

---

## 💡 核心要点总结

> ## Key Takeaways

* **聚焦控制平面：** Kinference 是由 Linkerd 缔造者 Buoyant 打造的开源项目 (基于 Apache 2.0 协议)，专注于为运行在 Kubernetes 上的 vLLM 集群提供专门优化的推理控制平面。
* **声明式策略管控：** 通过 `InferencePolicy` CRD 实现高灵活度的复杂路由编排，涵盖模型精细调度、云端外溢降级、PII 隐私防护以及批处理任务准入控制。
* **显著的性能飞跃：** 官方基准测试表明，在共享前缀工作负载下，相较于 Kubernetes 原生的 `kube-proxy` 路由，TTFT 中位数大幅缩减了 95%。
* **有效吞吐量倍增：** 在满足严格 SLO 条件下，共享前缀场景的峰值有效吞吐量提升约 7.4 倍，多轮对话场景提升约 3.5 倍。
* **项目处于早期阶段：** 目前该项目仍处于 Alpha 预览阶段，更精细的速率限制策略、深度分类器集成以及对 Anthropic API 的完整兼容仍处于规划路线图中。

> * **Control Plane Focus:** Kinference serves as an Apache 2.0 control plane tailored for vLLM on Kubernetes, developed by Linkerd creators Buoyant.
> * **Declarative Policies:** The `InferencePolicy` CRD handles complex routing logic including model selection, provider bursting, PII handling, and batch admission.
> * **Substantial Performance Boosts:** Self-reported benchmarks show a 95% reduction in median TTFT for shared-prefix traffic compared to native `kube-proxy` routing.
> * **Goodput Scaling:** Peak goodput improved by roughly 7.4x on shared-prefix tests and 3.5x on multiturn workloads.
> * **Early Stage Development:** As an alpha release, features like granular rate-limiting, deep classifiers, and full Anthropic API support are still on the horizon.

---

## 资源与社区链接

> ## Resources & Community

* **探索项目源码：** [GitHub 代码仓库](https://github.com/Kinference-AI/kinference) | [官方技术文档](https://kinference.ai/docs/)
* **延伸阅读推荐：** [Kinference 发布官方博客](https://www.buoyant.io/blog/introducing-kinference) | [分布式基准测试深度报告](https://www.buoyant.io/blog/distributed-inference-benchmarks-kinference-vs-plain-kubernetes)
* **关注与交流：** 在 [Twitter](https://x.com/intent/follow?screen_name=marktechpost) 关注最新动态，加入 [150k+ 成员的 ML Subreddit 社区](https://www.reddit.com/r/machinelearningnews/)，订阅 [技术周刊](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526)，或加入 [Telegram 频道](https://t.me/machinelearningresearchnews)。
* **商务合作推广：** 如需推广 GitHub 开源项目、Hugging Face 模型或商业产品，可[联系 MarkTechPost 团队](https://promotions.marktechpost.com/)。

> * **Explore the Project:** [GitHub Repository](https://github.com/Kinference-AI/kinference) | [Official Documentation](https://kinference.ai/docs/)
> * **Read More:** [Launch Blog Post](https://www.buoyant.io/blog/introducing-kinference) | [Distributed Benchmark Report](https://www.buoyant.io/blog/distributed-inference-benchmarks-kinference-vs-plain-kubernetes)
> * **Connect & Partner:** Follow updates on [Twitter](https://x.com/intent/follow?screen_name=marktechpost), join the [150k+ ML Subreddit](https://www.reddit.com/r/machinelearningnews/), subscribe to the [Newsletter](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526), or join the [Telegram Channel](https://t.me/machinelearningresearchnews). 
> * **Promotions:** Looking to promote a GitHub repo, Hugging Face model, or product release? [Connect with the MarkTechPost team](https://promotions.marktechpost.com/).
