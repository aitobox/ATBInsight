---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-11-10
hide:
- navigation
tags:
- 分布式训练
- 大语言模型
- Google
- Pathways
- TPU
title: 什么是 Pathways？Google 大模型单控制器分布式训练系统深度解析
---
# 什么是 Pathways？Google 大模型单控制器分布式训练系统深度解析

**Published:** November 9, 2026  
**Authors:** Sujeeth Jinesh, Shaurya Gupta, Luke Baumann, Monica Song, Ivan Nardini, Akanksha Gupta, Anthony Owusu, Jing Yang, Sadi Kneipp, Yu Li

### 文章背景与核心概要
面对当今动辄数千亿参数的前沿大语言模型 (Large Language Model, LLM) ，传统的分布式训练架构正面临严峻的协同与通信瓶颈。Google 近日在 Google Cloud Platform (GCP) 上正式全面开放 (General Availability) 了其核心分布式训练引擎 —— Pathways，这项底层黑科技此前曾深度支撑了 Gemini 等顶级大模型的全流程训练。与业界主流的单程序多数据 (Single Program, Multiple Data, SPMD) 范式不同，Pathways 创新性地采用“单客户端 + 分布式运行时”的单控制器图计算架构，将模型构建逻辑与底层物理硬件彻底解耦。它不仅化解了跨节点同步带来的流水线空泡与数据中心网络阻塞，更实现了硬件单点故障时的秒级透明重映射与弹性容错，为超大规模异构 AI 训练树立了全新标杆。

---

## 概述与核心亮点

> ## Summary

Google 正式宣布在 Google Cloud Platform (GCP) 上全面商用 (General Availability) **Pathways** 服务。作为由 Google 专门打造的分布式计算系统，Pathways 是孕育出 Gemini 等超大规模旗舰模型的幕后功臣。本文将深入剖析 Pathways 是如何突破传统训练协同障碍的：它通过单一客户端将整个训练计算描述为一张计算图，并由底层的分布式运行时环境全权接管张量放置、通信路由、硬件设备利用率优化以及集群弹性容错等复杂任务。

> Google has announced the General Availability of **Pathways on Google Cloud Platform**. Pathways is the distributed system engineered by Google to train massive models like Gemini. This article explores how Pathways overcomes traditional coordination hurdles by using a single client to describe computations as a graph, while a distributed runtime handles tensor placement, routing, device utilization, and cluster resilience.

---

## 核心速览 (TL;DR)

> ## TL;DR

* **协同瓶颈的挑战**：传统的超大模型训练高度依赖单程序多数据 (Single Program, Multiple Data, SPMD) 架构 (例如 DDP 与 FSDP) 。在这种架构下，每个加速芯片都以“齐步走”的步调执行完全相同的代码。尽管 SPMD 在处理同构、规则的任务时行之有效，但在面对流水线并行或强化学习 (Reinforcement Learning, RL) 闭环等复杂拓扑时却捉襟见肘 —— 因为这些复杂场景往往需要不同程序同时并发运行并交叠执行。
* **硬件故障的沉重代价**：在 SPMD 模式下，集群中哪怕只有单台设备或单颗芯片发生硬件故障 (在 Gemini 2.5 训练期间，硬件故障甚至平均每小时就会发生数次) ，都会导致所有计算进程全面停摆，迫使整个训练任务回滚到上一个检查点 (Checkpoint) 重启。
* **Pathways 带来的破局解法**：Pathways 引入了单客户端架构，将整体计算建模为由计算块和张量组成的完整计算图。底层的分布式运行时能够将工作负载灵活分发到虚拟设备上，自主管理张量传输、实现弹性伸缩，并确保各类加速器始终维持在峰值吞吐量 (Throughput) 运转。

> * **The Coordination Challenge:** Traditional large-model training relies on Single Program, Multiple Data (SPMD) architectures (like DDP and FSDP), where every accelerator runs identical code in lockstep. While effective for uniform tasks, SPMD struggles with complex topologies like pipeline parallelism or reinforcement learning (RL) loops where different programs must run simultaneously and overlap.
> * **The Cost of Failures:** In SPMD models, a single hardware failure (which interrupted Gemini 2.5 training multiple times per hour) stops every process, requiring a rollback to the last checkpoint. 
> * **The Pathways Solution:** Pathways introduces a single client that models computations as a graph of blocks and tensors. A distributed runtime places workloads onto virtual devices, handles tensor transfers, scales elastically, and keeps accelerators operating at peak throughput.

---

## 当扩展规模遇上协同瓶颈

> ## When Scaling Becomes a Coordination Problem

如果你经常使用 PyTorch 训练模型，那么对 **分布式数据并行 (Distributed Data Parallel, DDP)** 和 **完全分片数据并行 (Fully Sharded Data Parallel, FSDP)** 一定不会感到陌生。这两种方式都遵循经典的 **单程序多数据 (SPMD)** 模型：系统中的每一个进程都执行完全相同的脚本，各自独立控制绑定的加速器，并通过 `AllReduce` 等集合通信原语保持同步。

> If you train PyTorch models, you are likely familiar with **Distributed Data Parallel (DDP)** and **Fully Sharded Data Parallel (FSDP)**. Both follow the **Single Program, Multiple Data (SPMD)** model, wherein every process executes an identical script, controls its accelerators continuously, and synchronizes via collectives like `AllReduce`.

这种模型逻辑直接、易于理解，但在算力集群规模呈指数级扩展时，却会撞上一道道难以逾越的高墙：

> While this model is straightforward, it encounters limitations at scale:

* **数据中心网络带宽瓶颈**：在单个加速器 Pod 或节点内部，依托专用超高速互连总线的组内通信成本极低；但一旦通信跨越数据中心网络，带宽就会断崖式下跌 (例如，TPU v5p 芯片内部互连带宽高达 1,200 GB/s，而跨数据中心网络带宽仅有约 6 GB/s 左右) 。由于 SPMD 模式下每个训练步都必须等待全局集合通信阻塞同步，当任务跨越多组设备时，单步训练延迟 (Latency) 会急剧攀升。
* **流水线气泡 (Pipeline Bubbles)**：在流水线并行模式下，模型的不同层被切分部署在不同的设备上，通过拆分微批次 (Micro-batch) 依次前向和反向传播。这导致许多设备在等待上游输入或下游梯度时不得不处于闲置状态，从而严重拉低了系统的整体吞吐量。
* **强化学习训练循环效率低下**：在基于强化学习的后训练 (Post-training) 阶段，工作流往往由采样器 (Sampler) 、奖励模型 (Reward Model) 以及策略训练器 (Trainer) 共同构成。如果按照传统串行方式运行，在某个组件执行时，其他大部分核心计算资源都只能被动空转等待。

> * **Datacenter Network Bottlenecks:** While intra-group communication over fast interconnects is cheap, crossing the datacenter network introduces severe bandwidth constraints (e.g., TPU v5p chips get 1,200 GB/s internally, but only ~6 GB/s across the datacenter network). Because every step blocks on collectives, step times inflate rapidly as jobs span more groups.
> * **Pipeline Bubbles:** In pipeline parallelism, models are split across devices running smaller micro-batches, leaving some devices idle while waiting for inputs and reducing overall throughput.
> * **Inefficient RL Loops:** Reinforcement learning post-training involves samplers, reward models, and trainers. Running these sequentially leaves major components idle while others execute.

### SPMD 范式的根本局限

> ### The Limits of SPMD

由于每个独立的工作节点 (Worker) 都缺乏对整个系统的全局视野，导致 SPMD 架构存在以下根本性缺陷：

> Because individual workers lack global visibility, SPMD architectures suffer from strict limitations:

1. **零容错能力 (Zero Fault Tolerance)**：集群中只要有一台机器发生掉线或宕机，就会造成全局死锁，迫使整个训练任务彻底中断；
2. **刚性算力分配 (Rigid Capacity Allocation)**：闲置或等待中的算力资源无法被动态重新调度给其他任务，导致硬件浪费严重；
3. **排障与调试极其复杂 (Complex Debugging)**：在数万个同时保持同步的独立进程中定位死锁、卡顿或性能瓶颈，犹如大海捞针。

> 1. **Zero Fault Tolerance:** A single dropped machine halts the entire job.
> 2. **Rigid Capacity Allocation:** Idle capacity cannot be dynamically reassigned.
> 3. **Complex Debugging:** Diagnosing hangs across thousands of synchronized, separate processes is notoriously difficult.

---

## 借助 Pathways 实现全图统筹协同计算

> ## Coordinating the Entire Computation with Pathways

**Pathways** 的核心哲学是将模型代码构建与底层物理硬件执行彻底解耦。开发者只需要在一台普通 CPU 机器上运行单个 Python 客户端程序，并以统一视角与一组抽象的 **虚拟设备 (Virtual Devices)** 进行交互。随后，Pathways 资源管理器 (Resource Manager) 会负责将这些虚拟设备动态映射到物理加速芯片上，并由底层的 Worker 运行时系统高效执行经过编译优化的计算任务。

> **Pathways** decouples model building from hardware execution. A single Python client runs on a standard CPU and interacts with **virtual devices**. A resource manager then maps these virtual devices onto physical chips, while a worker runtime executes the compiled code.

```
[ Python Client (Virtual Devices) ] 
               │
               ▼
   [ Pathways Resource Manager ]
               │
               ▼
[ Distributed Hardware / TPU Hosts ]
```

### Pathways 的核心架构能力

> ### Key Capabilities of Pathways:

* **弹性训练与故障自愈 (Elastic Training and Fault Recovery)**：一旦某台主机发生硬件故障，资源管理器能够在不重启整个作业的前提下，无缝将受影响的工作负载重新映射到健康的备用芯片上，使大模型训练得以丝滑继续。
* **集群算力动态共享 (Shared Cluster Capacity)**：借助 *Shared Pathways Service*，多个独立的客户端可以通过 Google Kubernetes Engine (GKE) 按需动态租用 TPU 算力池的不同切片，从而将超大硬件集群的整体利用率推向极致。
* **异步分发机制 (Asynchronous Dispatch)**：Pathways 运行时能够在上一阶段计算尚未完全结束 *之前*，就提前完成下游张量缓冲区的分配并调度数据传输。这种前瞻性的重叠调度机制，有效避免了单一 Python 控制端成为整个集群的性能瓶颈。
* **中心化协同调度 (Central Scheduling)**：内置的中心化调度器保证了各个设备组之间的算子能够以确定、一致的全局顺序严格执行，从数学和架构上根除了复杂异构流水线中可能出现的死锁隐患。

> * **Elastic Training and Fault Recovery:** If a host fails, the resource manager seamlessly remaps workloads onto healthy chips, allowing training to continue without a full job restart.
> * **Shared Cluster Capacity:** Using the *Shared Pathways Service*, multiple clients can dynamically lease slices of a TPU pool on-demand via GKE, maximizing hardware utilization.
> * **Asynchronous Dispatch:** The Pathways runtime allocates buffers and schedules transfers *before* upstream computations finish. This prevents the single client from becoming a performance bottleneck.
> * **Central Scheduling:** A centralized scheduler ensures operations execute in a consistent order across groups, preventing deadlocks during complex pipelines.

---

## 这难道不就是开源调度框架 Ray 所做的事吗？

> ## Isn't This What Ray Does?

虽然开源社区广受欢迎的 **Ray** 提供了出色的分布式集群编排能力 —— 能够在跨云环境中灵活调度任务 (Task) 、Actor 以及异构计算工作流，但它与 Pathways 所处的系统抽象层级截然不同：

> While **Ray** provides exceptional open-source cluster orchestration—scheduling tasks, actors, and heterogeneous workloads across clouds—it operates at a different layer than Pathways:

* **Ray 的核心定位**：专注于集群基础设施层面的编排与协作，主要负责数据加载、训练任务拉起、在线推理服务以及超参数调优等宏观流水线。而在每一个具体的 Ray Worker 内部，模型训练代码依然是跑在传统的 SPMD 框架之上。
* **Pathways 的核心定位**：深植于底层的执行引擎层，彻底重塑了单个训练任务与底层庞大加速芯片集群的交互方式。它原生支持多程序多数据 (Multiple Programs, Multiple Data, MPMD) 模式、秒级弹性故障恢复以及单控制器全局统筹调度。

> * **Ray's Role:** Orchestrates cluster-level infrastructure, managing data loading, training, serving, and tuning. Inside Ray workers, training code still executes via traditional SPMD frameworks.
> * **Pathways' Role:** Operates at the execution layer underneath, redefining how a training job interacts with clusters of chips to enable MPMD (Multiple Programs, Multiple Data) patterns, elastic recovery, and single-controller coordination. 

归根结底，Ray 与 Pathways 绝非相互竞争的替代品，而是能够强强联合的互补架构：Ray 可以负责统领全局的宏观集群拓扑与任务编排，而 Pathways 则在底层专注于极致高效的大模型分布式执行。

> Ultimately, Ray and Pathways are complementary: Ray can orchestrate the overall cluster topology while Pathways manages low-level training execution.

---

## 总结与延伸阅读

> ## Conclusion and Next Steps

Pathways 成功将大模型的程序构建与硬件执行分离，让算法工程师能够站在统揽整个超大规模算力集群的高度去思考与编程，而无需再被困在割裂孤立的硬件碎片中苦苦挣扎。

> Pathways separates model construction from execution, empowering developers to reason about entire clusters rather than isolated slices. 

如果你想进一步深入探索 Pathways 的技术细节与使用方法，可以参阅以下官方资源：

> To dive deeper into Pathways, check out the following resources:

* [Google Cloud 上的 Pathways 官方文档 (Pathways on Google Cloud Documentation)](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro)
* [学术论文：《Pathways: 面向机器学习的异步分布式数据流系统》(Pathways: Asynchronous Distributed Dataflow for ML)](https://arxiv.org/abs/2203.12533)
* [基于 Pathways 的高弹性容错训练技术文档 (Resilient Training with Pathways Documentation)](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
* [Pathways Utils 开源工具库 (GitHub Repository)](https://github.com/AI-Hypercomputer/pathways-utils)
* [MaxText 官方开源训练代码库 (GitHub Repository)](https://github.com/AI-Hypercomputer/maxtext)

> * [Pathways on Google Cloud Documentation](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro)
> * [Pathways: Asynchronous Distributed Dataflow for ML (Paper)](https://arxiv.org/abs/2203.12533)
> * [Resilient Training with Pathways Documentation](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
> * [Pathways Utils GitHub Repository](https://github.com/AI-Hypercomputer/pathways-utils)
> * [MaxText GitHub Repository](https://github.com/AI-Hypercomputer/maxtext)

---

*本文标签：AI, Cloud, Learn, Explore, Influence*

> *Posted in: AI, Cloud, Learn, Explore, Influence*
