---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-09-15
hide:
  - navigation
tags:
  - NVIDIA OSMO
  - 具身智能
  - 编排调度
  - 物理AI
title: "NVIDIA 开源 OSMO：一份 YAML 编排物理 AI 训练、仿真与真机测试"
---

# NVIDIA 开源 OSMO：一份 YAML 编排物理 AI 训练、仿真与真机测试

> # NVIDIA Open-Sources OSMO: One YAML Orchestrates Physical AI Training, Simulation, and Robot Testing

### 文章背景与核心概要
物理 AI (Physical AI) 与具身智能机器人的研发流程极其复杂，传统上往往割裂在数据中心训练集群、工作站物理仿真环境以及机器人机载边缘计算硬件这三大异构层级之间，迫使工程师维护大量繁重的胶水脚本和孤立调度器。为破解这一“三电脑”难题，NVIDIA 正式开源了 Kubernetes 原生的工作流编排工具——OSMO。开发团队只需编写一份简洁的 YAML 配置文件，即可在统一控制平面下无缝调度从分布式训练、物理仿真到硬件在环真机测试的端到端管线。该工具的开源大幅降低了异构算力编排的技术门槛，为物理 AI 与机器人系统的规模化工程落地注入了强大动力。

---

## 概述

> ## Summary

在传统的机器人开发过程中，工程师们常常饱受“算力碎片化”的困扰：数据中心里的训练集群、工作站上的物理仿真环境，以及机器人机载的边缘计算硬件，往往各自为战，需要依赖五花八门的调度器和脆弱的“胶水脚本”强行串联。**NVIDIA OSMO** 正是为了化解这一痛点而生的开源云原生 (Kubernetes-native) 工作流编排调度工具。开发团队仅凭一份简洁的 YAML 配置文件，就能无缝协同跨越异构算力层级的物理 AI (Physical AI) 研发全链路——从模型训练、物理仿真再到硬件在环 (Hardware-in-the-Loop, HIL) 真机测试，彻底摆脱了编写繁琐底层基础设施代码的噩梦。

> Robot development traditionally suffers from a fragmented compute problem, requiring separate schedulers and glue scripts across data-center training clusters, workstation simulation environments, and edge hardware. **NVIDIA OSMO** solves this challenge as an open-source, Kubernetes-native workflow orchestrator. By leveraging a single YAML file, development teams can seamlessly orchestrate physical AI pipelines—spanning model training, physics simulation, and hardware-in-the-loop (HIL) robot testing—across heterogeneous compute tiers without writing complex infrastructure code.

---

## “三电脑”难题

> ## The Three Computer Problem

NVIDIA 将物理 AI 的开发挑战形象地归纳为 **“三电脑”难题 (Three Computer Problem)**：

> NVIDIA frames physical AI as a **three computer problem**:

1. **模型训练**：在数据中心级 GPU (如 GB200 或 H100 集群) 上大规模执行；
2. **物理仿真**：在工作站级 RTX 硬件上运行，用于物理动力学解算和传感器画面的高逼真渲染；
3. **部署与测试**：在 Jetson AGX Thor 等边缘端计算设备上运行，开展硬件在环验证。

> 1. **Training:** Executed on data-center GPUs (such as GB200 or H100 clusters).
> 2. **Simulation:** Handled on workstation-class RTX hardware for physics and sensor rendering.
> 3. **Deployment & Testing:** Run on edge devices like the Jetson AGX Thor for hardware-in-the-loop (HIL) validation.

在以往的工作流中，每个层级都高度依赖孤立的工具链，导致各阶段交接时摩擦不断，研发人员不得不编写大量脆弱的自定义编排脚本。**[NVIDIA OSMO](https://github.com/NVIDIA/OSMO)** 的破局思路在于：将这三大计算层级视为同一个统一控制平面下的不同后端资源。在工作流定义中，开发者只需指定特定的目标 *平台* (Platform) (例如 `gb200`、`rtx-pro-6000` 或 `jetson-agx-thor`)，便能彻底屏蔽底层繁杂的基础设施细节，由 OSMO 智能地将任务分发路由至最合适的计算资源池中。

> Traditionally, each tier relies on isolated tooling, resulting in friction-heavy handoffs and custom orchestration scripts. **[NVIDIA OSMO](https://github.com/NVIDIA/OSMO)** addresses this by treating all three tiers as backends under a unified control plane. Workflows abstract away underlying infrastructure by targeting a specific *platform* (e.g., `gb200`, `rtx-pro-6000`, or `jetson-agx-thor`), allowing OSMO to intelligently route tasks to appropriate compute pools.

---

## 工作流是如何运作的

> ## What a Workflow Looks Like

一个标准的 OSMO 管线可以在单份配置文件内无缝衔接不同阶段的串行任务与数据流：

> A canonical pipeline links data across sequential tasks within a single configuration:

* **`simulation`**：在 `rtx-pro-6000` 工作站硬件上运行 Isaac Sim 仿真容器；
* **`train-policy`**：在由 8 块 GPU 组成的 `gb200` 集群上启动 PyTorch 训练容器，直接消费并读取上游仿真任务输出的数据；
* **`evaluate-thor`**：将训练完成的策略部署到 `jetson-agx-thor` 边缘端设备上运行 ROS 应用程序，并将评测结果持久化记录到指定命名的数据集中。

> * **`simulation`**: Executes an Isaac Sim container on `rtx-pro-6000` hardware.
> * **`train-policy`**: Runs a PyTorch container on an 8-GPU `gb200` cluster, consuming the simulation task's output.
> * **`evaluate-thor`**: Deploys a ROS application on a `jetson-agx-thor` edge device using the trained policy, recording results to a named dataset.

在具体实现上，任务间的依赖关系通过 `inputs` 进行声明，数据持久化由 `outputs` 统筹，而硬件资源的精准分配则完全交由 `platform` 决定。根据 **[官方用户指南 (User Guide)](https://nvidia.github.io/OSMO/main/user_guide/)**，OSMO 还支持诸多高阶配置特性，包括串行与并行任务组、用于参数化管线的 Jinja 模板渲染、自动化失败重试策略，以及跨算力池的基于优先级的抢占式调度。

> Task dependencies are managed via `inputs`, persistence is handled through `outputs`, and resource allocation is determined by `platform`. The **[User Guide](https://nvidia.github.io/OSMO/main/user_guide/)** supports advanced configurations including serial and parallel task groups, Jinja templating for parameterized pipelines, automated retry policies, and priority-based preemption across compute pools.

---

## 核心能力

> ## Key Capabilities

* **跨平台可移植性**：实现“一次编写，随处部署”。无论是在笔记本电脑上通过 Docker/KIND 进行本地调试，还是无缝横向扩展至 EKS、AKS、GKE 以及完全物理隔离 (Air-gapped) 的本地私有集群。在 6.3.0 版本中，OSMO 还引入了支持多云提供商的 `deploy-k8s.sh` 脚本以简化集群部署，并深度集成了 MinIO、Azure Blob 及 AWS S3 等主流存储方案。
* **交互式开发体验**：开发者可以直接将本地的 VS Code、Jupyter 或 SSH 会话挂载连接至远程 GPU 节点，使用 `exec` 交互式进入正在运行的容器任务，并通过 `osmo workflow rsync download` 命令实现文件的近实时双向同步。
* **先进的智能调度**：在 **[NVIDIA KAI Scheduler](https://github.com/NVIDIA/KAI-Scheduler)** 的强力驱动下，OSMO 针对多 GPU 工作负载支持 NVLink 拓扑感知的计算放置，并提供细粒度的组级超时控制，防止某项停滞卡死的任务阻塞其他关联工作流。
* **企业级安全与身份认证**：具备完备的企业级安全管控体系，内置基于角色的访问控制 (RBAC) 授权 Sidecar 容器、OAuth2 代理集成、Envoy 网关处的 TLS 终端终止，并原生支持公有云工作负载身份认证机制 (如 Azure Workload Identity 与 AWS IRSA)。
* **AI 智能体原生集成**：通过专门的 **[AGENTS.md](https://github.com/NVIDIA/OSMO/blob/main/AGENTS.md)** 指南和模型上下文协议 (Model Context Protocol, MCP) 部署路径提供开箱即用的原生支持，OSMO 能够与 **Claude Code、OpenAI Codex 以及 Cursor** 等主流编程智能体深度融合，实现工作流的自动化提交、运行监控与故障排查。

> * **Portability:** Write once and deploy locally via Docker/KIND on a laptop, or scale out to EKS, AKS, GKE, and air-gapped on-premise clusters. The 6.3.0 release introduces a multi-provider `deploy-k8s.sh` script to streamline provisioning alongside storage integrations for MinIO, Azure Blob, and AWS S3.
> * **Interactive Development:** Developers can attach VS Code, Jupyter, or SSH sessions directly to remote GPU nodes, `exec` into active tasks, and utilize `osmo workflow rsync download` for real-time file synchronization.
> * **Advanced Scheduling:** Powered by the **[NVIDIA KAI Scheduler](https://github.com/NVIDIA/KAI-Scheduler)**, OSMO supports NVLink topology-aware placement for multi-GPU workloads and configurable per-group timeouts to prevent stalled tasks from blocking sibling workflows.
> * **Security and Identity:** Features robust enterprise controls including an RBAC authorization sidecar, OAuth2 proxy integration, TLS termination at the Envoy gateway, and cloud workload identity support (Azure Workload Identity, AWS IRSA).
> * **Agent Integration:** Featuring native support via **[AGENTS.md](https://github.com/NVIDIA/OSMO/blob/main/AGENTS.md)** and Model Context Protocol (MCP) deployment paths, OSMO integrates directly with coding agents like **Claude Code, OpenAI Codex, and Cursor** to automate workflow submission, monitoring, and debugging.

---

## 核心要点

> ## Key Takeaways

* **统一步调与协同编排**：只需一份统一的 YAML 配置，即可跨越不同的 Kubernetes 集群协调贯通模型训练、仿真渲染与边缘真机评测。
* **开箱即用，生产就绪**：基于 Apache-2.0 开源协议发布，可通过 NGC Helm Chart 一键部署，并提供基于 KIND 的本地快速上手工作流。
* **企业级特性全面加持**：依托 KAI Scheduler 实现具备 NVLink 拓扑感知的任务调度，配备细粒度超时控制与原生的 OAuth2/RBAC 安全认证体系。
* **生态成熟，久经实战**：已在 NVIDIA 内部的 GR00T、Isaac Lab、Isaac Sim 及 Isaac ROS 等前沿具身智能框架中历经高强度实战检验。
* **弃用与升级预警**：独立的 dataset 命令行工具与旧版 `/datasets` API 自 6.3 版本起已正式弃用，并将在 6.4 版本中彻底移除，全面转向由工作流原生接管的数据集输出机制。

> * **Unified Orchestration:** Coordinate training, simulation, and edge testing from a single YAML configuration across diverse Kubernetes clusters.
> * **Production Ready:** Apache-2.0 licensed, available via NGC Helm charts, and features a local KIND quickstart workflow.
> * **Enterprise Features:** Leverages KAI Scheduler with NVLink-aware placement, granular timeouts, and native OAuth2/RBAC security.
> * **Ecosystem Proven:** Battle-tested across frameworks like GR00T, Isaac Lab, Isaac Sim, and Isaac ROS.
> * **Deprecation Notice:** The standalone dataset CLI and legacy `/datasets` API are deprecated as of version 6.3 and removed in 6.4 in favor of workflow-managed dataset outputs.

---

## 相关资源与链接

> ## Resources & Links

* **[GitHub 开源仓库](https://github.com/NVIDIA/OSMO)**
* **[官方文档指南](https://nvidia.github.io/OSMO/main/user_guide/)**
* **[版本发布说明](https://github.com/NVIDIA/OSMO/releases)**
* **[Cookbook 实战范例](https://github.com/NVIDIA/OSMO/blob/main/cookbook)**
* **[NVIDIA OSMO 产品主页](https://developer.nvidia.com/osmo)**

> * **[GitHub Repository](https://github.com/NVIDIA/OSMO)**
> * **[Official Documentation](https://nvidia.github.io/OSMO/main/user_guide/)**
> * **[Release Notes](https://github.com/NVIDIA/OSMO/releases)**
> * **[Cookbook Examples](https://github.com/NVIDIA/OSMO/blob/main/cookbook)**
> * **[NVIDIA OSMO Product Page](https://developer.nvidia.com/osmo)**
