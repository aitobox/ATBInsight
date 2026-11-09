---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-11-10
hide:
  - navigation
tags:
  - Git
  - AI智能体
  - 基础设施
  - Rust
title: "Reason Machines 开源专为 AI 智能体设计的 Git 服务器 Aspen"
---

# Reason Machines 开源专为 AI 智能体设计的 Git 服务器 Aspen

### 文章背景与核心概要
随着编程智能体等 AI 应用的爆发式增长，成百上千个 AI 智能体同时高频提交代码，导致传统 Git 服务器因单仓库锁排队和重复打包历史而频繁遭遇性能瓶颈。针对这一痛点，Reason Machines 正式开源了专为 AI 智能体打造的轻量级 Git 服务器 Aspen。Aspen 借鉴了 OpenAI 内部系统 Pando 的架构理念，颠覆性地将写入粒度从“单仓库”拆解为“单分支”，结合单二进制 Rust 架构、PostgreSQL 元数据与 S3 兼容对象存储，在单台 8 核服务器上实现了高达每秒 567 次持续推送的强悍吞吐量。该项目的开源为解决 AI 规模化编码中的版本控制基础设施瓶颈提供了全新的开放式解决方案。

---

## 核心内容摘要

> ## Summary

Reason Machines 正式发布了开源 Git 服务器 **Aspen**，专门用于从容应对高并发的 AI 智能体 (AI Agent) 流量。当成百上千个自主运行的智能体试图同时推送代码更新时，传统 Git 服务器往往会因全局排队写入仓库、以及每次拉取都需要重新打包历史记录而沦为严重瓶颈。Aspen 针对 OpenAI 的 *Pando* 架构进行了一套独立的开源实现，将写入扩展粒度由“单仓库”彻底解耦为“单分支”。Aspen 采用 Rust 语言编写，以单一独立可执行文件的方式分发；它将分支历史路由至 PostgreSQL (或 SQLite) 中管理，并将 Git 数据包无缝写入对象存储，在官方基准测试中展现出惊人的性能表现——单台 8 核服务器即可支撑每秒 567 次的高速持续推送。

> Reason Machines has released **Aspen**, an open-source Git server designed specifically to handle high-frequency AI agent traffic. Traditional Git servers bottleneck when hundreds of autonomous agents attempt to push updates simultaneously because they queue repository writes and re-pack history for every fetch. Aspen provides an independent open-source implementation of the architecture described in OpenAI’s *Pando*, scaling writes per branch rather than per repository. Written in Rust and distributed as a single binary, it routes branch history through PostgreSQL (or SQLite) and packs to object storage, achieving impressive self-reported benchmarks such as 567 sustained pushes per second on an 8-core server.

---

## 极速速览 (TL;DR)

> ## TL;DR

* **架构设计**：采用单个 Rust 二进制文件构建。分支由 PostgreSQL (或 SQLite) 进行轻量管理，Git 数据包 (Pack) 则直接保存在兼容 S3 的对象存储中。
* **部署方式**：支持本地秒级启动 (`aspen dev`)、Docker Compose 一键部署，或通过 Helm 与 Terraform 云端编排交付。
* **性能表现**：推送到不同分支的操作互不阻塞、完全并发，代码拉取操作能高效复用已存储的数据包。
* **主要优势 (官方报告)**：在单台 8 核服务器上，能连续 5 分钟稳定保持每秒 567 次的高频推送。
* **局限性与不足**：当前处于 Pre-alpha 初期阶段，尚未发布正式版本；主干分支 (`main`) 的写入仍受限于约每秒 4 次，且目前暂未提供完整的 Web 管理界面。
* **核心总结**：Aspen 创新地通过单分支原子写入机制打破了传统单仓库推送的性能天花板，尽管它目前仍处于早期探索与开发阶段。

> * **Architecture:** A single Rust binary. Branches are managed via PostgreSQL (or SQLite), while Git packs live in object storage (S3-compatible).
> * **Deployment Options:** Run locally (`aspen dev`), via Docker Compose, or through Helm and Terraform clouds.
> * **Performance:** Pushes to different branches never block each other, and fetches efficiently reuse stored packs.
> * **Pros (Self-Reported):** Sustained 567 pushes per second for 5 minutes on a single 8-core server.
> * **Cons & Limitations:** Pre-alpha status with no official releases yet, landing on `main` is limited to ~4 per second, and a complete web UI is currently missing.
> * **Bottom Line:** Aspen eliminates the per-repository push ceiling via per-branch writes, though it remains in early pre-alpha development.

---

## 什么是 Aspen？

> ## What is Aspen?

Aspen 是一款可私有化自托管的 Git 服务器，其核心创新在于将写操作的并发能力按“单个分支”而非“整个仓库”进行水平扩展。它通过标准的 HTTPS 和 SSH 协议与常规 Git 客户端通信，将底层的原始 Git 数据包存入兼容 S3 的对象存储中，同时在 PostgreSQL 中以极轻量的结构记录并维护各分支的历史演进。

> Aspen is a self-hostable Git server that scales writes per branch rather than per repository. It communicates using standard Git protocols over HTTPS and SSH, storing raw Git packs in S3-compatible object storage while keeping branch histories lightweight inside PostgreSQL.

---

## 传统 Git 服务器为何难以招架 AI 智能体？

> ## Why Classic Git Servers Struggle with AI Agents

AI 编程智能体通常每隔几分钟就会高频推送一次代码变更，并紧接着触发持续集成 (CI) 流水线。据 [Reason Machines](https://reasonmachines.com/blog/aspen) 介绍，传统的 Git 服务器在处理并发推送时，会将针对同一代码仓库的所有推送请求排进全局锁队列中，形成严重的共享瓶颈；并且每当收到客户端的拉取请求时，服务器都需要动态重新打包生成全新的 packfile。这种机制导致服务器在面对成百上千个并发客户端时，工作负载急剧恶化、扩展能力严重受限。

> AI coding agents push code changes every few minutes, triggering continuous integration (CI) pipelines immediately afterward. According to [Reason Machines](https://reasonmachines.com/blog/aspen), classic Git servers queue all concurrent pushes to a single repository into a shared bottleneck and construct fresh packfiles for every incoming fetch request. As a result, server workloads scale poorly as client counts grow.

当 [OpenAI 遭遇这道同样的扩展壁垒](https://openai.com/index/scaling-git-at-openai/) 时，他们自主研发了内部系统 *Pando*，成功将代码推送的中位数延迟降低了近 5 倍，如今每天支撑着数 PB 级的高峰数据流量。Aspen 的底层架构设计正是直接取材于这一工业级突破。

> When [OpenAI faced this exact scaling barrier](https://openai.com/index/scaling-git-at-openai/), they engineered *Pando*, which reduced median push latency by nearly 5x and now handles petabytes of daily traffic. Aspen directly models its architecture on this design.

---

## Aspen 的底层运作原理解析

> ## How Does Aspen Work?

Aspen 大胆打破了传统 Git 服务器始终恪守的两项底层设计假设：

> Aspen bypasses two fundamental assumptions maintained by traditional Git servers:

### 1. 基于单分支的“比较并交换” (CAS) 并发控制

> ### 1. Per-Branch Compare-and-Swap

Aspen 不再锁定整个仓库，而是将每个独立分支维护为 PostgreSQL 表中单一行记录里的版本链条。当智能体推送修改时，服务器直接上传数据包，并仅通过单次**比较并交换 (Compare-and-Swap, CAS)** 操作原子化更新分支指针。
* 推送到不同分支的操作彼此完全独立，无需相互排队等待。
* 若有两个并发推送在同一瞬间恰好指向完全相同的分支，其中一个会立即成功，另一个则会收到标准 Git 的“请先拉取最新代码” (fetch first) 冲突提示。

> Rather than locking an entire repository, each branch is maintained as a chain of versions inside a single PostgreSQL row. When an agent pushes changes, it uploads the pack and updates the branch reference using a single **compare-and-swap** operation. 
> * Pushes to separate branches execute independently without waiting on one another.
> * If two concurrent pushes target the exact same branch simultaneously, one succeeds while the other receives Git's standard "fetch first" error.

### 2. 存储即用型数据包，告别服务端动态重打包

> ### 2. Stored Packs Instead of Per-Client Packs

Aspen 绝不对传入的推送数据包执行繁重的解包操作。相反，它仅负责快速校验 packfile 的完整性、补全缺失的基础对象，然后原封不动地直接存入对象存储中。此后若有客户端发起代码拉取，Aspen 会直接将这些已存储的数据包流式传输给客户端，彻底省去了耗费大量 CPU 资源的服务器端重新压缩与重打包过程。甚至还可以借助带签名的预签名 URL，让客户端直接通过 CDN 极速下载数据包。

> Aspen never unpacks incoming pushes. Instead, it validates the packfile, resolves any missing base objects, and stores it in object storage precisely as received. Subsequent fetches stream these stored packs directly to clients without any expensive server-side recompression. Signed URLs can even serve these packs directly from a CDN.

### 3. 仅通告主干引用与后台分层压缩整合

> ### 3. Trunk-Only Advertisement and Compaction

当客户端与服务器进行引用协商时，客户端默认仅能看到主干分支 (Trunk Branch)——这一机制即使在仓库中同时管理数百万个并发活跃分支时，也能让网络握手协商保持在极低开销。与此同时，后台压缩任务会按照日志结构合并树 (Log-Structured Merge Tree, LSM) 的分层策略定期合并存储的数据包，确保进度落后的客户端在拉取历史时只需获取数量适度的数据包集合，避免陷入下载成千上万个碎片小包的困境。

> When clients negotiate references, they only see the trunk branch—keeping negotiations lightweight even when managing millions of branches. Background compaction merges stored packs in log-structured merge tree levels, ensuring clients lagging behind retrieve a manageable number of packs rather than thousands.

---

## Aspen 的实测性能表现如何？

> ## How Fast Is Aspen?

在一项基准测试中，测试环境配置为单台 8 核服务器、标准 S3 存储以及 4 核 PostgreSQL 实例，测试仓库选用包含约 4,500 个文件和 75,000 次提交的 `git.git` 代码库副本：
* **持续高吞吐量**：在持续 5 分钟的压测中，稳定实现了每秒 567 次推送，且实现了零错误率。
* **超低延迟**：代码推送的中位数延迟仅为 **208 ms**，第 99 百分位 (P99) 延迟仅为 **314 ms**。
* **极速可见性**：其他并发客户端在中位数仅 **30 ms** 内即可实时感知并观测到最新推送的代码更新。
* **极致拉取效率**：在 depth-1 浅拉取风暴压力测试下，网络传输字节数仅为原生 `git upload-pack` 的 **1.029 倍**。

> In benchmark testing utilizing a single 8-core server, S3 Standard storage, and a 4-core PostgreSQL instance against a copy of `git.git` (~4,500 files and 75,000 commits):
> * **Sustained Throughput:** 567 pushes per second for 5 minutes straight with zero errors.
> * **Latency:** Median push latency hit **208 ms**, with the 99th percentile at **314 ms**.
> * **Visibility:** Other clients could observe pushed updates within **30 ms** at the median.
> * **Fetch Efficiency:** A depth-1 fetch storm required just **1.029x the bytes** compared to stock `git upload-pack`.

作为横向对比，[Cursor 官方披露](https://cursor.com/blog/git-at-any-scale) 其自研架构 *Origin* 在标准 S3 上最高能支撑每秒 120 次推送；而在配置多副本集群并采用 S3 Express One Zone 极速存储时，吞吐量可扩展至每秒 300 次以上。

> For comparison, [Cursor reports](https://cursor.com/blog/git-at-any-scale) up to 120 pushes per second for *Origin* on standard S3, scaling past 300+ on S3 Express One Zone using a replicated cluster setup.

---

## 架构特性对比：面向智能体规模的 Git 后端一览

> ## Feature Comparison: Agent-Scale Git Backends

| 特性对比 (Feature) | [Aspen](https://github.com/reason-machines/aspen) | [Cursor Origin](https://cursor.com/blog/git-at-any-scale) | [OpenAI Pando](https://openai.com/index/scaling-git-at-openai/) | [GitHub Spokes](https://cursor.com/blog/git-at-any-scale) |
| :--- | :--- | :--- | :--- | :--- |
| **可用性 (Availability)** | 开源、支持自托管 | Cursor 商业平台专有 | OpenAI 内部专有系统 | GitHub 内部专有系统 |
| **开源许可证 (License)** | Apache 2.0 | 未公开 | 未公开 | 未公开 |
| **推送排序策略 (Push Ordering)** | 基于单分支 (比较并交换, CAS) | 基于单仓库 (在 S3 中维护 WAL) | 基于单分支 | 跨副本三阶段提交 (3PC) |
| **引用存储 (Ref Storage)** | PostgreSQL 或 SQLite | S3 中的预写日志索引，无需关系型数据库 | 专用元数据存储引擎 | 部署于 NVMe 固态硬盘上的本地 Git 仓库 |
| **拉取服务机制 (Fetch Serving)** | 直接复用已存储数据包 (拼接或 URI 重定向) | NVMe 本地 Git 仓库缓存 | 直接复用已存储数据包 | Git 仓库副本直连服务 |
| **已披露推送速率 (Published Push Rate)** | 567 次/秒 (标准 S3，单台服务器) | 120 次/秒 (标准 S3)；300+ 次/秒 (S3 Express) | 未披露 | 未披露 |
| **其他关键指标 (Additional Metrics)** | P99 推送延迟：314 ms | 读性能随副本数线性扩展至 100 个节点 | 推送中位数延迟降低约 5 倍 | 未披露 |

---

## 如何部署 Aspen？

> ## How to Deploy Aspen

Aspen 可以直接使用 Rust 从源码进行编译构建。
* 本地快速体验与开发：直接执行 `aspen dev`，底层会自动通过本地目录与 SQLite 驱动。
* 团队协同部署：可以使用随附的 **Docker Compose** 方案 (集成了 PostgreSQL 与 MinIO)，或采用官方 **Helm 图表** 在 Kubernetes 中快速编排。
* 云端基础设施：提供适用于 AWS、Google Cloud、Azure 以及 Hetzner 的 **Terraform** 基础设施编排模块。
* 无缝评估体验：支持独特的 **镜像模式 (Mirror mode)**，可以在不迁移现有代码库的前提下，作为 GitHub 或 GitLab 的透明反向代理进行快速评估与验证。

> Aspen can be built directly from source using Rust. 
> * Use `aspen dev` for local development backed by SQLite and a local directory.
> * Teams can utilize **Docker Compose** (bundled with PostgreSQL and MinIO) or official **Helm charts**.
> * **Terraform** integrations are available for AWS, Google Cloud, Azure, and Hetzner.
> * A **Mirror mode** allows you to front GitHub or GitLab transparently for trial evaluations without a full migration.

---

## 核心亮点与总结

> ## Key Takeaways

* **Apache 2.0 宽松开源协议**：专为高并发 AI 智能体流量量身定制的专用 Git 服务器。
* **源自 Pando 架构灵感**：对 OpenAI 大规模 Git 基础设施架构理念的独立开源落地。
* **卓越的高并发性能**：能够在极低毫秒级延迟下，轻松应对每秒数百个并发分支的高频写入更新。
* **即插即用的无缝兼容性**：无需对本地开发者和智能体的 Git 客户端进行任何改造配置；原生的 `git` 命令即可通过 HTTPS 和 SSH 顺畅执行。

> * **Apache 2.0 Open Source:** A purpose-built Git server optimized for high-volume AI agent traffic.
> * **Pando-Inspired:** An independent open implementation of OpenAI's scalable Git infrastructure.
> * **High Performance:** Capable of handling hundreds of concurrent branch updates per second with low millisecond latency.
> * **Drop-In Compatibility:** Requires zero changes to local client setups; standard `git` commands work seamlessly over HTTPS and SSH.

---

欲了解更多技术细节与源码实现，欢迎查阅 [GitHub 代码仓库](https://github.com/reason-machines/aspen) 以及官方的 [发布公告原文](https://reasonmachines.com/blog/aspen)。

> *Check out the [GitHub repository](https://github.com/reason-machines/aspen) and the [launch post](https://reasonmachines.com/blog/aspen) for more details.*
