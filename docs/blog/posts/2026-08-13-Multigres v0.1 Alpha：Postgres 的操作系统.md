---
authors:
- aitoboxrobot
categories:
- 产品发布
date: 2026-08-13
hide:
- navigation
tags:
- Postgres
- Multigres
- 数据库扩展
- 高可用
- 连接池
title: Multigres v0.1 Alpha：Postgres 的操作系统
---
### 文章背景与核心概要
Multigres 发布了其首个公开开源里程碑版本 —— **v0.1 Alpha**，为 Postgres 带来了 Vitess 级别的水平扩展、高可用性和操作简便性。作为专为 Postgres 设计的可扩展操作系统，该初始版本引入了高级连接 pooling（连接池）、基于共识的自动故障转移以及 Kubernetes 运营商（Operator），为未来的分片（sharding）功能奠定了基础。（注：针对 Supabase 的专属版本即将推出）。

---

# Multigres v0.1 Alpha: An Operating System for Postgres

> **Summary:** Multigres has released its first public open-source milestone—**v0.1 Alpha**—bringing Vitess-grade horizontal scaling, high availability, and operational simplicity to Postgres. Designed as a scalable operating system for Postgres, this initial release introduces advanced connection pooling, automatic consensus-based failovers, and a Kubernetes operator, laying the groundwork for future sharding capabilities. *(Note: A dedicated release for Supabase is coming soon).*

---

## 什么是 Multigres？

Multigres 是一个用于 Postgres 的可扩展操作系统，能够整体管理数据库实例，并提供内置的：
* 分片（即将推出的旗舰功能）
* 连接池
* 自动故障转移
* 备份编排

大规模运行 Postgres 会带来显著的运营复杂性，包括管理只读副本、故障转移、连接限制和备份。Multigres 将这些繁琐工作作为一个统一的整体系统进行处理，使您能够在需要时将数据库水平扩展。

**v0.1 Alpha** 具体引入了：
* 高级连接池
* 自动故障转移
* 用于部署的 Kubernetes 运营商（Operator）

> ## What is Multigres?
> 
> Multigres is a scalable operating system for Postgres that holistically manages your database instances, providing built-in:
> * Sharding (upcoming flagship feature)
> * Connection pooling
> * Automatic failover
> * Backup orchestration
> 
> Running Postgres at scale introduces significant operational complexity, including the management of read replicas, failovers, connection limits, and backups. Multigres handles these chores as a single cohesive system, empowering you to scale your database horizontally when needed.
> 
> The **v0.1 Alpha** specifically introduces:
> * Advanced connection pooling
> * Automatic failovers
> * A Kubernetes operator for deployment

---

## Multigres 运营商（Operator）

Kubernetes Multigres Operator 允许您在 Kubernetes 上原生部署和管理 Multigres 集群。

* **前提条件：** 要[开始使用](https://multigres.com/blog/deploying-the-multigres-operator)，您需要一个 Kubernetes 集群和一个配置好的备份存储位置（例如共享文件系统或云存储桶，如 AWS S3）。
* **本地测试：** 您也可以在 Kind 集群上本地运行 Multigres。
* **可用性：** 运行 Multigres 所需的所有容器镜像均已公开可用。

> ## The Multigres Operator
> 
> The Kubernetes Multigres Operator allows you to deploy and manage Multigres clusters natively on Kubernetes. 
> 
> * **Prerequisites:** To [get started](https://multigres.com/blog/deploying-the-multigres-operator), you need a Kubernetes cluster and a configured location for backups (such as a shared file system or a cloud storage bucket like AWS S3).
> * **Local Testing:** You can also run Multigres locally on a Kind cluster.
> * **Availability:** All necessary container images for running Multigres are publicly available.

---

## 高可用性

Multigres 将高可用性（HA）视为一个共识问题，在不丢失成功提交的前提下成功解决了脑裂（split-brain）场景。其协议构建于通用共识之上，提供了独特的灵活性：

* **基于未经修改的 Postgres 复制：** 使用标准 Postgres 复制满足基于共识系统的一切严格一致性要求。
* **用户定义的持久性策略：** 定义任意复杂的持久性策略，而不受限制性多数派法定人数（majority quorum）规则的约束。例如，您可以强制要求跨可用区（cross-zone）持久性，同时将备用节点部署在三个以上的可用区中。
* **动态副本：** 在集群运行时安全地向上和向下扩展副本，而不会损害性能或正确性。

### 高可用性推荐阅读
* [从第一原理看高可用](https://multigres.com/blog/high-availability-from-first-principles)
* [使用共识处理边缘情况](https://multigres.com/blog/handling-edge-cases-using-consensus)

> ## High Availability
> 
> Multigres treats High Availability (HA) as a consensus problem, successfully resolving split-brain scenarios without losing successful commits. Its protocol is built on generalized consensus, offering unique flexibility:
> 
> * **Built on Unmodified Postgres Replication:** Satisfies all strict consistency requirements of a consensus-based system using standard Postgres replication.
> * **User-Defined Durability Policies:** Define arbitrarily complex durability policies without being constrained by restrictive majority quorum rules. For example, you can mandate cross-zone durability while deploying standbys across more than three zones.
> * **Dynamic Replicas:** Safely scale replicas up and down while the cluster is running without hurting performance or correctness.
> 
> ### Recommended Reading on HA
> * [High availability from first principles](https://multigres.com/blog/high-availability-from-first-principles)
> * [Handling edge cases using consensus](https://multigres.com/blog/handling-edge-cases-using-consensus)

---

## 连接池

Multigres 采用基于双服务架构的自定义连接池解决方案：
1. **Multigateway：** 接受客户端连接并路由查询。
2. **Multipooler：** 管理后端数据库连接。

与传统的单进程连接池相比，这种架构具有几个明显的优势：

* **智能流量路由：** 与 HA 系统无缝集成，将连接路由到当前的主要是节点（primary）。在故障转移期间，它可以暂缓请求，直到提升新的主节点，从而将错误降至最低。它还支持跨多个副本的读负载均衡。
* **上下文感知连接池：** 具有内置的解析器，能够理解请求的影响，从而无需选择僵化的连接池模式（如事务级或会话级）。有状态的请求（如事务）会被固定到专用连接，直到完成。
* **按用户划分的连接池：** 为每个用户维护单独的、公平共享的连接池，无需共享池或 `SET ROLE` 模拟。
* **预编译语句合并（Prepared Statement Consolidation）：** 跨网关对预编译语句进行去重，因此 Postgres 对给定语句只需进行一次解析、计划和缓存。

### 连接池推荐阅读
* [无需选择模式的连接池](https://multigres.com/blog/pooling-without-choosing-a-mode)
* [公平共享的按用户连接池](https://multigres.com/blog/per-user-pools-that-share-fairly)
* [双职能、双进程：为什么 Multigres 有自己的连接池](https://multigres.com/blog/two-jobs-two-processes)

> ## Connection Pooling
> 
> Multigres features a custom connection pooling solution built on a two-service architecture:
> 1. **Multigateway:** Accepts client connections and routes queries.
> 2. **Multipooler:** Manages backend database connections.
> 
> This architecture delivers several distinct advantages over traditional single-process poolers:
> 
> * **Intelligent Traffic Routing:** Seamlessly integrates with the HA system to route connections to the current primary. During failovers, it can hold requests until a new primary is promoted, minimizing errors. It also supports read-load balancing across multiple replicas.
> * **Context-Aware Pooling:** Features a built-in parser that understands request effects, eliminating the need to choose rigid pooling modes (like transaction or session-level). Stateful requests (like transactions) are pinned to a dedicated connection until complete.
> * **Per-User Pools:** Maintains separate, fairly shared connection pools per user without shared pools or `SET ROLE` impersonation.
> * **Prepared Statement Consolidation:** Deduplicates prepared statements across gateways so Postgres only parses, plans, and caches a given statement once.
> 
> ### Recommended Reading on Pooling
> * [Pooling without choosing a mode](https://multigres.com/blog/pooling-without-choosing-a-mode)
> * [Per-user pools that share fairly](https://multigres.com/blog/per-user-pools-that-share-fairly)
> * [Two jobs, two processes: why Multigres has its own connection pooler](https://multigres.com/blog/two-jobs-two-processes)

---

## 备份

Multigres 利用 **pgBackRest** 进行可靠的备份，主要从副本执行备份，以避免给主数据库带来负载。

* **三种备份类型：**
  * **完全备份（Full）：** 在检查点复制整个数据目录。
  * **增量备份（Incremental）：** 仅复制自上次备份以来更改的文件。
  * **差异备份（Differential）：** 复制自上次完全备份以来的更改。
* **按需与定时：** CLI 允许您列出备份、触发手动备份以及启动恢复。通过集群规范实现的定时备份即将推出。
* **自动引导（Automated Bootstrap）：** 自动识别主节点，执行备份，并使用它来初始化其他副本，无需人工干预即可启动准备就绪的集群。

### 引导推荐阅读
* [Multigres 集群是如何引导的](https://multigres.com/blog/multigres-cluster-bootstrap)

> ## Backups
> 
> Multigres leverages **pgBackRest** for reliable backups, executing them primarily from replicas to avoid putting load on the primary database.
> 
> * **Three Backup Types:**
>   * **Full:** Copies the entire data directory at a checkpoint.
>   * **Incremental:** Copies only files changed since the previous backup.
>   * **Differential:** Copies changes since the last full backup.
> * **On-Demand and Scheduled:** The CLI allows you to list backups, trigger manual backups, and initiate restores. Scheduled backups via the cluster spec are arriving soon.
> * **Automated Bootstrap:** Automatically identifies a primary, performs a backup, and uses it to initialize other replicas, bringing up a ready-to-run cluster without manual intervention.
> 
> ### Recommended Reading on Bootstrapping
> * [How a Multigres Cluster Bootstraps](https://multigres.com/blog/multigres-cluster-bootstrap)

---

## “Alpha”意味着什么

版本 0.1 已经足够稳定以供实验和反馈，但**尚未准备好用于生产环境的工作负载**。请牢记以下几点：

* 还有一些[已知问题](https://github.com/multigres/multigres/issues)需要解决。
* **分片**未包含在此版本中（v0.1 是一个具有 HA 和连接池功能的单分片集群）。
* **不保证**未来版本能够向后兼容。
* 自定义资源（CR）API 不稳定，在 v1.0 之前可能会发生更改。
* 性能基准测试目前正在进行中，将在后续文章中发布。

> ## What "Alpha" Means
> 
> Version 0.1 is stable enough for experimentation and feedback, but **not yet ready for production workloads**. Keep the following in mind:
> 
> * There are [known issues](https://github.com/multigres/multigres/issues) that still need to be addressed.
> * **Sharding** is not included in this release (v0.1 is a single-shard cluster with HA and pooling).
> * Future releases are **not guaranteed to be backward compatible**.
> * The Custom Resource (CR) API is unstable and subject to change before v1.0.
> * Performance benchmarks are currently in progress and will be published in a follow-up post.

---

## 立即体验 Multigres

1. **[部署您的第一个集群](https://multigres.com/blog/deploying-the-multigres-operator)：** 使用自定义资源搭建一个最小的 3 节点 HA 集群。
2. **加入社区：** 
   * 在 [GitHub](https://github.com/multigres/multigres) 上提交问题并请求新功能。
   * 在 [GitHub 讨论区](https://github.com/multigres/multigres/discussions)中讨论功能并获取帮助。

> ## Try Multigres Today
> 
> 1. **[Deploy your first cluster](https://multigres.com/blog/deploying-the-multigres-operator):** Stand up a minimal 3-node HA cluster using a custom resource.
> 2. **Join the community:** 
>    * File issues and request features on [GitHub](https://github.com/multigres/multigres).
>    * Discuss features and get help in [GitHub Discussions](https://github.com/multigres/multigres/discussions).