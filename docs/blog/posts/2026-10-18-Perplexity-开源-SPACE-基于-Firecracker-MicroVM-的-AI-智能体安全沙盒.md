---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-18
hide:
  - navigation
tags:
  - Perplexity
  - SPACE
  - Firecracker
  - AI 智能体沙盒
  - 微虚拟机
title: "Perplexity 开源 SPACE：基于 Firecracker MicroVM 的 AI 智能体安全沙盒"
---

# Perplexity 开源 SPACE：基于 Firecracker MicroVM 的 AI 智能体安全沙盒

> # Perplexity Open-Sources SPACE, a Firecracker MicroVM Sandbox for AI Agents

### 文章背景与核心概要

随着自主 AI 智能体 (AI Agent) 越来越多地承担编写代码、执行系统命令等复杂任务，如何防止不受信任的代码或模型意外破坏宿主系统甚至发生“越狱”，成了当下的关键安全瓶颈。Perplexity 正式开源了其用于支撑 Perplexity Computer 背后的生产级沙盒平台 —— SPACE。该平台基于轻量级微虚拟机 (MicroVM) 技术 Firecracker 构建，并采用 Rust 语言编写，实现了系统级的高隔离性、极低启动延迟与严格的外发网络管控。在针对 9 款顶尖前沿模型的实战红蓝攻防测试中，SPACE 实现了零宿主机逃逸，为开发者自建安全自主智能体运行环境提供了极具参考价值的开源基础设施方案。

---

## 核心速览

> ## Summary

Perplexity 正式开源了经过大规模生产环境验证的沙盒平台 **SPACE** (Sandboxed Platform for Agentic Code Execution，意为“用于智能体代码执行的沙盒平台”)，该平台正是支撑 Perplexity Computer 中每一项复杂任务的核心底层架构。SPACE 基于 Rust 语言构建并在 Apache 2.0 协议下开源，它将每个 AI 智能体任务深度隔离在独立的 Firecracker 微虚拟机 (MicroVM) 中，确保敏感凭据和所有出站网络流量完全由客户机环境外部进行统一管控。凭借优异的性能、超低的启动延迟，以及历经 9 款前沿大模型实测考验的坚固安全性，SPACE 现已面向所有希望为代码编写与网页浏览智能体自建安全执行层的开发团队开放使用。

> Perplexity has open-sourced **SPACE** (Sandboxed Platform for Agentic Code Execution), the production-tested sandbox platform powering every task in Perplexity Computer. Built with Rust under the Apache 2.0 license, SPACE isolates each AI agent task inside its own Firecracker microVM, keeping credentials and outbound traffic strictly controlled from outside the guest environment. Featuring high performance, low latency, and robust security tested against 9 frontier models, SPACE is now available for teams looking to self-host secure execution layers for coding and browsing agents.

---

## 一分钟要点概览

> ## TL;DR

* **代码规模与技术栈**：纯 Rust 代码库，以 [0.8.0](https://github.com/perplexityai/SPACE/blob/main/docs/versioning.md) 版本作为首发公开基线，提供完善的 HTTP API 以及用于实时传输流式输出的服务器发送事件 (Server-Sent Events, SSE) 机制。
* **运行环境需求**：需要搭载 KVM 硬件虚拟化支持的 [Linux x86_64 宿主机](https://github.com/perplexityai/SPACE/blob/main/docs/installation.md)，依赖 `/dev/kvm`、btrfs 文件系统和 Docker。支持本地 Kind (Kubernetes) 集群部署或直接宿主机模式 (不支持 macOS)。
* **性能表现**：在实际生产环境中，与 Perplexity 之前使用的第三方供应商相比，沙盒创建的中位数延迟从 [185 毫秒大幅降至 60 毫秒](https://www.perplexity.ai/hub/blog/making-space-secure-and-efficient-runtimes-for-long-running-agents)。
* **安全隔离性**：在针对 9 款顶尖前沿模型的红蓝对抗攻防测试中，[108 次虚拟机逃逸尝试全部失败 (0/108)](https://www.perplexity.ai/hub/blog/escaping-space-part-i)，无一成功突破至宿主机。
* **修复前漏洞情况**：在应用安全补丁之前，在部分网络开放测试中，AI 智能体在 [54 次测试中有 11 次 (11/54)](https://www.perplexity.ai/hub/blog/escaping-space-part-i) 成功绕过了出站流量策略。

> * **Size:** Rust codebase, release [0.8.0](https://github.com/perplexityai/SPACE/blob/main/docs/versioning.md) as the public baseline, featuring an HTTP API plus server-sent events.
> * **Runs on:** A [Linux x86_64 host with KVM](https://github.com/perplexityai/SPACE/blob/main/docs/installation.md), `/dev/kvm`, btrfs, and Docker. Supports local Kind (Kubernetes) or direct mode (No macOS support).
> * **Performance:** In production, median create latency dropped from [185 ms to 60 ms](https://www.perplexity.ai/hub/blog/making-space-secure-and-efficient-runtimes-for-long-running-agents) compared to Perplexity’s previous provider.
> * **Security:** [0 of 108](https://www.perplexity.ai/hub/blog/escaping-space-part-i) VM-to-host escape attempts succeeded across 9 frontier models.
> * **Vulnerabilities (Pre-fix):** Before security patches, agents bypassed the egress policy in [11 of 54](https://www.perplexity.ai/hub/blog/escaping-space-part-i) partial-network runs.

---

## 什么是 Perplexity SPACE？

> ## What is Perplexity SPACE?

SPACE (Sandboxed Platform for Agentic Code Execution) 是 Perplexity 专为在隔离微虚拟机中执行智能体代码而打造的核心平台。上层应用程序只需调用其 [HTTP API](https://github.com/perplexityai/SPACE)，即可快速创建 Linux 运行环境、执行各类命令并实时流式接收执行输出。

> SPACE (Sandboxed Platform for Agentic Code Execution) is Perplexity’s platform for running agent code in isolated microVMs. Applications call its [HTTP API](https://github.com/perplexityai/SPACE) to create Linux environments, execute commands, and stream output.

* **模板 (Template)**：为沙盒提供初始化的基础文件系统映像。
* **沙盒 (Sandbox)**：基于特定模板实例化的独立运行环境，拥有专属于自己的独立虚拟机和可写磁盘。在单个沙盒生命周期内，支持按序连续执行多条命令。

> * **Template:** Supplies the starting filesystem.
> * **Sandbox:** An individual instance of a template featuring its own VM and writable disk. Multiple commands can run sequentially inside a single sandbox.

Perplexity 在其官方发布的 [推文串 (Launch Thread)](https://x.com/perplexity_ai/status/2110778478312481167) 中重点阐述了该系统的核心设计初衷：允许智能体在沙盒*内部*以 root 管理员权限自由运行命令、安装依赖软件包并调用各类网络服务；与此同时，严格确保宿主机器在物理层面完全脱离客户机虚拟机的控制范围。鉴于智能体的工作流通常具有长时间运行、多轮有状态演进以及多分支探索等特点，整个平台在底层架构设计上全面支持重启容灾与状态无损恢复。

> Perplexity’s [launch thread](https://x.com/perplexity_ai/status/2110778478312481167) highlights the primary design goal: allowing agents to run commands, install packages, and call services with root privileges *inside* the sandbox while ensuring the host remains completely out of the guest’s control. Because agent workflows are long-running, stateful, and branching, the platform is designed to survive restarts.

---

## SPACE 如何对智能体实现严密隔离？

> ## How Does SPACE Isolate Agents?

在架构层面，每一个沙盒都是一个轻量级的 [Firecracker](https://www.usenix.org/conference/nsdi20/presentation/agache) 微虚拟机，拥有完全独立的客户机操作系统内核。同时，宿主机上为每个沙盒分别配备了专属的网络网关，对虚拟机的每一笔外发连接严格执行出站访问安全策略。

> Each sandbox is a [Firecracker](https://www.usenix.org/conference/nsdi20/presentation/agache) microVM complete with its own guest kernel. A per-sandbox network gateway on the host enforces strict egress policies on every outbound connection.

任何核心机密或访问凭据绝不直接流入客户机内部。根据 Perplexity 在 [7 月份发布的技术工程博文](https://www.perplexity.ai/hub/blog/making-space-secure-and-efficient-runtimes-for-long-running-agents)，敏感凭据全部在宿主机网络层进行安全透明注入。该凭据管理中心支持多层级作用域划分、高精度速率限制以及全方位的操作审计日志。

> Secrets never enter the guest. According to Perplexity’s [July engineering post](https://www.perplexity.ai/hub/blog/making-space-secure-and-efficient-runtimes-for-long-running-agents), credentials are injected securely at the network layer. The credential store provides hierarchical scoping, strict rate limits, and comprehensive audit logging.

官方发布的 [架构设计指南 (Architecture Guide)](https://github.com/perplexityai/SPACE/blob/main/docs/architecture.md) 将系统解构为四大核心组件：
1. 基于 PostgreSQL 存储的 API 服务层
2. 控制器集群 (Controllers)
3. 工作节点服务 (Worker Services)
4. 数据平面 (Data Plane)

> The [architecture guide](https://github.com/perplexityai/SPACE/blob/main/docs/architecture.md) divides the system into four core components:
> 1. PostgreSQL-backed API
> 2. Controllers
> 3. Worker services
> 4. Data plane

工作节点服务负责统筹管理虚拟机生命周期、虚拟网络、存储卷、模板以及凭据分发，并充分利用 btrfs 文件系统的写时复制 (Copy-on-Write, CoW) 特性，以极高效率瞬间分发每个沙盒的根文件系统。

> Worker services manage VMs, networking, volumes, templates, and credentials, utilizing btrfs copy-on-write functionality to provision each root filesystem efficiently.

---

## 暂停、休眠挂起与状态恢复是如何运作的？

> ## How Do Pause, Suspend, and Restore Work?

在整个运行生命周期中，沙盒会在四种截然不同的状态之间流转切换：**运行中 (Running)**、**已暂停 (Paused)**、**已休眠挂起 (Suspended)** 以及 **已删除 (Deleted)**。

> Sandboxes transition through four distinct states: **running**, **paused**, **suspended**, and **deleted**.

* **运行中 (Running)**：各类进程正在活跃执行；实时虚拟机内存与可写文件系统均处于就绪保持状态。
* **已暂停 (Paused)**：代码执行立即中断，但虚拟机的内存数据依然驻留在工作节点内存中 (此时并非持久化快照)。
* **已休眠挂起 (Suspended)**：将虚拟机内存、运行时系统状态以及根文件系统全部持久化保存为快照，并彻底释放所有占用的活跃计算资源。
* **默认空闲策略 (Idle Default)**：当沙盒持续处于空闲状态超过 6 小时后，系统将对其 [执行自动休眠挂起](https://github.com/perplexityai/SPACE/blob/main/docs/architecture.md)。

> * **Running:** Processes execute actively; live VM memory and the writable filesystem are preserved.
> * **Paused:** Execution stops and VM memory stays resident on the worker (not a durable snapshot).
> * **Suspended:** VM memory, runtime state, and the root filesystem are snapshotted, and active resources are released. 
> * **Idle Default:** Sandboxes [suspend automatically after 6 hours](https://github.com/perplexityai/SPACE/blob/main/docs/architecture.md) of inactivity.

为了实现极致的极速供给，在 Kubernetes 生产部署环境下，系统利用预先引导就绪的沙盒构建了 [预热池 (Warm Pools)](https://github.com/perplexityai/SPACE/blob/main/docs/warm-pools.md)；而在单节点开发测试环境中，则依托 [基础快照 (Base Snapshots)](https://github.com/perplexityai/SPACE/blob/main/docs/base-snapshots.md) 机制实现秒级启动。在实际生产场景中，沙盒创建延迟的第 90 百分位数 (P90) 从 [447 毫秒大幅降至 89 毫秒](https://www.perplexity.ai/hub/blog/making-space-secure-and-efficient-runtimes-for-long-running-agents)，目前 Perplexity Computer 的会话已 100% 全量运行在 SPACE 平台之上。

> For rapid provisioning, Kubernetes deployments utilize [warm pools](https://github.com/perplexityai/SPACE/blob/main/docs/warm-pools.md) of pre-booted sandboxes, whereas single-node setups rely on [base snapshots](https://github.com/perplexityai/SPACE/blob/main/docs/base-snapshots.md). In production, the 90th-percentile create latency dropped from [447 ms to 89 ms](https://www.perplexity.ai/hub/blog/making-space-secure-and-efficient-runtimes-for-long-running-agents), with 100% of Perplexity Computer sessions running on SPACE.

---

## SPACE 能经受住红蓝对抗安全测试吗？

> ## Did SPACE Survive a Red-Team Test?

Perplexity 在发布的 [*逃逸 SPACE：第一部分 (Escaping SPACE: Part I)*](https://www.perplexity.ai/hub/blog/escaping-space-part-i) 深度安全测试报告中，对赋予了客户机内部 root 最高权限的 9 款主流模型展开了总计 216 次实战渗透运行评估：

> Perplexity’s [*Escaping SPACE: Part I*](https://www.perplexity.ai/hub/blog/escaping-space-part-i) report evaluated 9 models with root access inside the guest across 216 runs:

* **沙盒突破逃逸 (Sandbox Escape)**：在总共 108 次实战测试中，成功窃取宿主机核心机密的次数为 0 (0/108)。
* **纯无网络环境绕过 (No-network Bypass)**：在 54 次测试中，成功绕过网络封锁的次数为 0 (0/54)。
* **部分联网环境绕过 (Partial-network Bypass)**：在安全补丁上线*之前*，54 次测试中有 11 次 (11/54) 出现了策略绕过 (Claude Opus 5.0、GPT-5.6 Sol、GPT-5.6 Cyber 以及 Kimi K3 等模型成功利用了 DNS 欺骗与共享 CDN IP 地址的漏洞)。

> * **Sandbox escape:** 0 of 108 runs reached the host-side secret.
> * **No-network bypass:** 0 of 54 runs succeeded.
> * **Partial-network bypass:** 11 of 54 runs succeeded *before* fixes were implemented (models like Claude Opus 5.0, GPT-5.6 Sol, GPT-5.6 Cyber, and Kimi K3 successfully exploited DNS spoofing and shared CDN IP addresses).

### 安全补丁与加固机制

> ### Security Fixes

针对发现的潜在安全隐患，Perplexity 迅速引入了基于 `nftables` 的源地址严格校验机制。现在的网络网关会在宿主机侧主动终结 TLS 连接，并对客户端发送的 SNI (服务器名称指示) 与 HTTP Host 请求头进行白名单严格交叉校验。随后的全面复测显示，**所有被测模型实现了 0 次成功绕过**。此外，研究人员针对 10 个第三方主流沙盒平台展开了平行对照测试，发现其中 8 个平台均存在类似的网络策略绕过缺陷，Perplexity 已遵循负责任漏洞披露原则向对应厂商进行了通报。

> Following these findings, Perplexity integrated source-address validation via `nftables`. The gateway now terminates TLS and validates both the SNI and HTTP host against an approved allowlist. A subsequent retest yielded **0 verified model bypasses**. Additionally, tests across 10 third-party platforms revealed network-policy bypasses in 8 of them, which Perplexity responsibly disclosed to the affected vendors.

---

## SPACE 与其他开源智能体沙盒对比

> ## How Does SPACE Compare with Other Open Sandboxes?

| 功能特性 | **Perplexity SPACE** | [E2B Runtime](https://github.com/e2b-dev/infra) | [microsandbox](https://github.com/zerocore-ai/microsandbox) | [Daytona](https://github.com/daytonaio/daytona) |
| :--- | :--- | :--- | :--- | :--- |
| **隔离机制** | [每个沙盒独立 Firecracker 微虚拟机](https://github.com/perplexityai/SPACE) | [每个沙盒独立 Firecracker 微虚拟机](https://github.com/e2b-dev/infra) | [libkrun 微虚拟机](https://github.com/zerocore-ai/microsandbox) | [每个沙盒独占独立内核](https://github.com/daytonaio/daytona) |
| **开源协议** | [Apache 2.0](https://github.com/perplexityai/SPACE/blob/main/LICENSE) | [Apache 2.0](https://github.com/e2b-dev/infra) | [Apache 2.0](https://github.com/zerocore-ai/microsandbox) | 公开仓库，[自 2026 年 6 月起停止维护](https://github.com/daytonaio/daytona) |
| **开发语言** | [Rust](https://github.com/perplexityai/SPACE) | [Go](https://github.com/e2b-dev/infra) | [Rust](https://github.com/zerocore-ai/microsandbox) | 未披露 |
| **宿主机要求** | [Linux x86_64 + KVM](https://github.com/perplexityai/SPACE/blob/main/docs/installation.md) | 未披露 | [支持 KVM 的 Linux](https://github.com/zerocore-ai/microsandbox) | 未披露 |
| **出站控制** | 独立沙盒专属网关、TLS 终结拦截 | [nftables 防火墙、SNI/Host 域名清单](https://github.com/e2b-dev/infra) | 未披露 | 未披露 |
| **Perplexity 出站绕过测试** | [修复后 0 次绕过](https://www.perplexity.ai/hub/blog/escaping-space-part-i) | [存在 HTTPS 绕过漏洞，已计划缓解方案](https://www.perplexity.ai/hub/blog/escaping-space-part-i) | [存在 HTTP 与 HTTPS 绕过，已于 v0.6.18 修复](https://www.perplexity.ai/hub/blog/escaping-space-part-i) | [存在 HTTPS 绕过漏洞，已发布缓解方案](https://www.perplexity.ai/hub/blog/escaping-space-part-i) |
| **E2B SDK 兼容性** | [支持，通过 ECW 兼容包装层](https://github.com/perplexityai/SPACE/blob/main/docs/ecw.md) | 原生支持 | 未披露 | 未披露 |

---

## 开发者该如何部署与使用 SPACE？

> ## How Do Developers Deploy SPACE?

根据官方提供的 [安装部署文档 (Installation Guide)](https://github.com/perplexityai/SPACE/blob/main/docs/installation.md)，开发者可以将 SPACE 便捷地部署至本地的 Kind (Kubernetes in Docker) 集群中。宿主机环境需要支持 `/dev/kvm` 硬件虚拟化接口、`/dev/net/tun` 虚拟网络设备、loop 挂载设备以及 btrfs 文件系统 (如果开发者在已有的虚拟机内部进行嵌套运行，则必须开启嵌套虚拟化支持)。

> The [installation guide](https://github.com/perplexityai/SPACE/blob/main/docs/installation.md) deploys SPACE into a local Kind cluster. The host environment requires `/dev/kvm`, `/dev/net/tun`, loop devices, and btrfs (running inside a VM requires nested virtualization).

对于已经在使用 E2B 的研发团队，可以直接利用项目提供的 [E2B 兼容包装层 (E2B Compatibility Wrapper, ECW)](https://github.com/perplexityai/SPACE/blob/main/docs/ecw.md) 实现无缝平替迁移，该组件已针对 Python 依赖包 `e2b==2.21.1` 完成了严格的兼容性验证。此外，代码仓库中还贴心地附带了一套面向企业级上云的 AWS EKS 参考部署配置。

> Teams already utilizing E2B can leverage the [E2B Compatibility Wrapper](https://github.com/perplexityai/SPACE/blob/main/docs/ecw.md), tested against the Python package `e2b==2.21.1`. A reference AWS EKS deployment is also included in the repository.

---

## 总结与核心结论

> ## Key Takeaways

* SPACE 将每一个 AI 智能体任务封装在独立隔离的 Firecracker 微虚拟机内执行。
* 敏感凭据注入与出站网络安全策略全部由宿主机外部强力执行，与客户机虚拟机环境实现物理层隔离。
* 在严苛的高强度红蓝对抗渗透测试中，108 次虚拟机逃逸尝试无一攻破宿主机系统 (0/108)。
* 修复前的部分出站网络绕过漏洞 (在打补丁前的 54 次测试中存在 11 次绕过) 在引入 `nftables` 严格源校验与 TLS 终结拦截后，成功降至 0 次绕过。
* 全面采用 **Rust** 语言编写，遵循 **Apache 2.0** 开源许可协议，宿主环境需具备支持 KVM 的 **Linux x86_64** 硬件系统。

> * SPACE executes each agent task within an isolated Firecracker microVM.
> * Credentials and egress policies are enforced externally, remaining entirely outside the guest VM.
> * In rigorous red-team tests, 0 out of 108 escape attempts successfully compromised the host.
> * Egress bypass vulnerabilities (found in 11 of 54 runs prior to patches) were reduced to 0 following the integration of `nftables` validation and TLS termination checks.
> * Built with **Rust** under the **Apache 2.0** license, requiring a **Linux x86_64 host with KVM**.

---

欢迎深入探索其 [**GitHub 开源仓库**](https://github.com/perplexityai/SPACE)，查阅官方完整的 [**技术开发文档**](https://space.docs.perplexity.ai/guide/index.html)，并研读详细的 [**红蓝对抗安全评估报告**](https://www.perplexity.ai/hub/blog/escaping-space-part-i)。

> Explore the [**GitHub Repository**](https://github.com/perplexityai/SPACE), read the [**Documentation**](https://space.docs.perplexity.ai/guide/index.html), and review the [**Red-Team Report**](https://www.perplexity.ai/hub/blog/escaping-space-part-i). 

*特此向本项目的所有研究人员与开源开发者致敬。欢迎在 [**Twitter**](https://x.com/intent/follow?screen_name=marktechpost) 上关注最新动态，加入拥有 [**15 万+成员的机器学习 Reddit 社区**](https://www.reddit.com/r/machinelearningnews/)，订阅 [**精选时事通讯**](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526)，或关注其 [**Telegram 频道**](https://t.me/machinelearningresearchnews)。*

> *All credit goes to the researchers and developers of this project. Feel free to follow on [**Twitter**](https://x.com/intent/follow?screen_name=marktechpost), join the [**150k+ ML SubReddit**](https://www.reddit.com/r/machinelearningnews/), subscribe to the [**Newsletter**](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526), or join the [**Telegram Channel**](https://t.me/machinelearningresearchnews).*

*本文原刊载于 [MarkTechPost](https://www.marktechpost.com)，原文题为《[Perplexity Open-Sources SPACE, a Firecracker MicroVM Sandbox for AI Agents](https://www.marktechpost.com/2026/10/16/perplexity-open-sources-space-firecracker-microvm-sandbox-ai-agents/)》。*

> *The post [Perplexity Open-Sources SPACE, a Firecracker MicroVM Sandbox for AI Agents](https://www.marktechpost.com/2026/10/16/perplexity-open-sources-space-firecracker-microvm-sandbox-ai-agents/) appeared first on [MarkTechPost](https://www.marktechpost.com).*
