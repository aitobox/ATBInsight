---
authors:
- aitoboxrobot
categories:
- 产品发布
date: 2026-08-23
hide:
- navigation
tags:
- Git
- 分布式存储
- 架构设计
- S3
- Cursor
title: 大规模 Git 架构演进：Cursor 的 Continuity 架构解析
---
### 文章背景与核心概要
在大规模场景下托管 Git 仓库一直面临着独特的工程挑战，这是由 Git 的分布式架构以及对二进制包文件（packfiles）的强依赖所决定的。传统的分布式文件系统、分布式哈希表（DHT）或者诸如 GitHub Spokes 那样的基于三阶段提交（3PC）的应用层复制方案，在应对现代企业级超大单体仓库（Monorepos）以及 AI 智能体（Agent）驱动的大量短生命周期仓库时，逐渐暴露出可扩展性、可用性以及运维复杂度方面的严重瓶颈。

本文探讨了 Git 托管基础设施的演进历程，并重点介绍了由 Cursor 团队构建的全新 Git 架构 —— **Continuity**。该架构创新性地将预写日志（WAL）与对象存储（如 S3）相结合，将 S3 设定为唯一的真实数据源（Source of Truth）。通过这一设计，Continuity 实现了完全一致的水平扩展、轻松的压缩（Compaction）机制，以及针对现代复杂工作负载的零停机可靠性。

---

##  Git 难在哪里？

> Hosting Git repositories at scale is a well-known engineering hurdle. When Linus Torvalds designed Git, he created a **distributed** version control system intended to replace BitKeeper for the decentralized development of the Linux Kernel. In a distributed model, all instances of a repository are identical—there is nothing fundamentally unique about the repository on a server versus the one on a developer's laptop.
在规模化场景下托管 Git 仓库是一个众所周知的工程难题。当林纳斯·托瓦兹（Linus Torvalds）设计 Git 时，他创造了一个**分布式**版本控制系统，旨在取代 BitKeeper，用于 Linux 内核的去中心化开发。在分布式模型中，仓库的所有实例都是完全相同的 —— 服务器上的仓库与开发者笔记本电脑上的仓库在本质上没有任何区别。

> While this works wonderfully for local operations and offline workflows, modern software companies rely heavily on centralized hosting. Unfortunately, Git's underlying design makes server-side scaling remarkably difficult.
虽然这对于本地操作和离线工作流来说堪称完美，但现代软件公司高度依赖集中式托管。不幸的是，Git 的底层设计使得服务端扩展变得异常困难。

> Code and metadata are compressed and stored in **packfiles**—a binary serialization format optimized for local machine performance rather than distributed server management. Because packfiles must be transferred over the network and accessed on disk as large binary blobs, traditional approaches (like placing an HTTP server in front of on-disk repositories) quickly hit low scalability and availability ceilings.
代码和元数据被压缩并存储在**包文件（packfiles）**中 —— 这是一种针对本地机器性能而非分布式服务器管理优化的二进制序列化格式。由于包文件必须通过网络传输并在磁盘上以大型二进制大对象（Blob）的形式被访问，传统方法（例如在磁盘仓库前端放置 HTTP 服务器）很快就会触及可扩展性和可用性的低上限。

> Scaling server-side Git generally falls into three approaches of increasing complexity:
> 1. Distributing the filesystem
> 2. Distributing the packfiles (objects)
> 3. Distributing Git itself
扩展服务端 Git 通常分为三种复杂度逐渐递增的方法：
1. 分布式文件系统
2. 分布式包文件（对象）
3. 分布式 Git 本身

---

## 没有包文件的 Git

> Because Git is a content-addressable data store keyed by SHA-1 hashes, it theoretically maps well to a distributed key-value store. However, this approach fails in practice because Git's actual layout is a **Directed Acyclic Graph (DAG)**. 
由于 Git 是一个以 SHA-1 哈希为键的内容寻址数据存储，理论上它与分布式键值（Key-Value）存储有着良好的契合度。然而，这种方法在实践中行不通，因为 Git 的实际布局是一个**有向无环图（DAG）**。

> To perform even trivial operations—like listing recent changes—you must walk the commit history step-by-step. Each step yields a pointer to a tree, a file, or a parent commit. Because you cannot know the value of the next pointer without fetching the previous one, relying on a distributed store introduces prohibitive network latency. Previous attempts to store objects in Distributed Hash Tables (DHTs)—such as Google's JGit-based experiments—ultimately failed because the Git protocol still requires packfiles to be transmitted over the network, rendering `git clone` performance unacceptable.
为了执行哪怕是最简单的操作（例如列出最近的更改），你也必须一步步遍历提交历史。每一步都会产生一个指向树（tree）、文件或父提交的指针。由于在不获取前一个指针的情况下无法得知下一个指针的值，依赖分布式存储会引入不可接受的网络延迟。先前将对象存储在分布式哈希表（DHT）中的尝试（例如谷歌基于 JGit 的实验）最终都失败了，因为 Git 协议仍然要求通过网络传输包文件，这导致 `git clone` 的性能完全无法让人接受。

---

## GitHub 与文件系统

> When GitHub launched in 2008, it sought to make centralized Git hosting painless using a monolithic Ruby on Rails application with repositories stored locally on disk. As the platform grew, scaling the application meant deploying more instances, raising the question: *How do you deploy multiple copies of apps that need disk access to the same Git repositories?*
2008 年 GitHub 刚上线时，它试图通过一个单体 Ruby on Rails 应用程序来实现无痛的集中式 Git 托管，并将仓库直接存储在本地磁盘上。随着平台的发展，扩展应用程序意味着部署更多实例，这就引发了一个问题：*如何将需要访问磁盘的应用部署多份副本来操作相同的 Git 仓库？*

> Early engineers attempted to distribute the filesystem using NFS, GFS, and DRBD. All of these approaches failed due to:
> * **Filesystem assumptions:** Git assumes local filesystem semantics (locking, syncing, and tearing) that break down across networked filesystems.
> * **Random read patterns:** Because packfiles store objects as deltas spread randomly across compressed binaries, navigating the DAG requires random jumps across gigabytes of data. Networked filesystems crawl under these access patterns without local caching.
早期工程师曾尝试使用 NFS、GFS 和 DRBD 来实现文件系统分布式化。但所有这些方法都以失败告终，原因如下：
* **文件系统假设：** Git 假定具备本地文件系统语义（锁定、同步和防撕裂），而这些在网络文件系统中会失效。
* **随机读取模式：** 由于 packfiles 将对象存储为随机分布在压缩二进制文件中的增量（deltas），因此导航 DAG 需要在数 GB 的数据中进行随机跳转。在没有本地缓存的情况下，网络文件系统在面对这种访问模式时性能会急剧下降。

> Ultimately, GitHub abandoned distributed filesystems in favor of an RPC system where repositories lived on dedicated fileservers, accessed remotely by the Rails app.
最终，GitHub 放弃了分布式文件系统，转而采用一种 RPC 系统：仓库驻留在专用的文件服务器上，由 Rails 应用进行远程访问。

---

## Spokes 与一致性

> Developed around 2013, GitHub's **Spokes** pioneered application-level replication for Git repositories. It made three foundational choices:
> 1. It works at the **packfile level** rather than distributing Git internals.
> 2. It stores data as **plain Git repositories on local NVMe disks**.
> 3. It replicates data while keeping all copies **consistently in sync**.
GitHub 的 **Spokes** 开发于 2013 年左右，开创了 Git 仓库应用级复制的先河。它做出了三个基础性选择：
1. 它工作在**包文件（packfile）级别**，而不是分布式化 Git 的内部实现。
2. 它将数据存储为**本地 NVMe 磁盘上的纯 Git 仓库**。
3. 它在复制数据的同时，保持所有副本**高度一致地同步**。

### 三阶段提交（3PC）协议
> ### The Three-Phase Commit (3PC) Protocol
> Spokes uses a consensus-based approach powered by the Three-Phase Commit (3PC) protocol. When a user pushes code, Spokes fans out the heavy **packfile** to all replicas simultaneously without synchronization. Once received, it synchronizes the lightweight **reference transaction** (which updates branch pointers) using 3PC. A push is only accepted if a majority of nodes acknowledge it.
Spokes 使用由三阶段提交（3PC）协议驱动的基于共识的方法。当用户推送代码时，Spokes 会在没有同步的情况下，将庞大的**包文件**同时扇出（fans out）给所有副本。接收到后，它会使用 3PC 同步轻量级的**引用事务**（用于更新分支指针）。只有在大多数节点确认后，推送才会被接受。

### Spokes 在大规模场景下的局限性
> ### Limitations of Spokes at Scale
> While Spokes has been an industry standard for over a decade, modern demands expose two major flaws:
> * **The Tail at Scale:** 3PC latency is bound by the slowest server in a cluster. As enterprise monorepos require more replicas to handle CI workloads, push throughput degrades. Conversely, agent-driven workflows that generate countless tiny, throwaway repositories suffer because Spokes still demands three mostly idle replicas per repo.
> * **Operational Overhead:** Because NVMe disks act as the source of truth, repositories are treated as *pets, not cattle*. Maintaining complex routing tables, constant checksumming, and urgent repair jobs for corrupted replicas makes cluster maintenance fragile and prone to quorum loss.
尽管 Spokes 已经成为十多年来的行业标准，但现代需求暴露了它的两个主要缺陷：
* **规模化带来的长尾延迟：** 3PC 的延迟受限于集群中最慢的服务器。随着企业级单体仓库需要更多副本来处理 CI 工作负载，推送吞吐量会下降。相反，由 AI 智能体驱动的工作流会生成无数微小的、用完即弃的仓库，它们会因此受到影响，因为 Spokes 仍然要求每个仓库至少有三个大部分处于空闲状态的副本。
* **运维开销：** 由于 NVMe 磁盘充当真实数据源，仓库被视为“宠物而非牲畜”（pets, not cattle）。维护复杂的路由表、持续的校验和计算，以及对损坏副本进行紧急修复，使得集群维护变得脆弱且极易发生法定人数丢失（quorum loss）。

---

## Continuity

> Developed at Cursor, **Continuity** retains what made Spokes successful while eliminating its architectural bottlenecks. 
由 Cursor 开发的 **Continuity** 保留了 Spokes 成功的原因，同时消除了其架构瓶颈。

> Continuity relies on a **write-ahead log (WAL)** stored in S3-compatible object storage. 
> * Pushes are recorded as WAL entries in S3 simultaneously with being written to a local NVMe disk.
> * **A push is never acknowledged until it is fully persisted.**
> * Pushes become visible only after preparing the reference transaction on a local repository and recording a pointer in the S3 WAL index, **forcing all pushes to be linearizable**.
Continuity 依赖于存储在兼容 S3 的对象存储中的**预写日志（WAL）**。
* 推送在写入本地 NVMe 磁盘的同时，作为 WAL 条目记录在 S3 中。
* **在完全持久化之前，推送绝不会被确认。**
* 只有在本地仓库上准备好引用事务并在 S3 WAL 索引中记录指针后，推送才变得可见，**从而强制所有推送具有线性一致性（linearizable）**。

```
[ Git Push ] ---> [ Write to NVMe Disk ] & [ Upload WAL Entry to S3 ]
                         │
                         ▼
             [ Linearizable S3 WAL Index ] ---> [ Acknowledge to Client ]
```

### 共识
> ### Consensus
> Continuity eliminates complex routing tables and external databases. Repositories can live anywhere; the local disk acts merely as a warm cache, while **S3 remains the single source of truth**. 
> * Rendezvous hashing maps repository IDs to expected nodes.
> * If a node is missing a repository, it simply materializes it from the WAL.
> * Pushes use atomic compare-and-swap (CAS) operations on S3, allowing *any* server to act as a primary without leader election overhead.
Continuity 消除了复杂的路由表和外部数据库。仓库可以驻留在任何地方；本地磁盘仅充当热缓存，而 **S3 仍然是唯一的真实数据源**。
* 集合点哈希（Rendezvous hashing）将仓库 ID 映射到期望的节点。
* 如果某个节点缺少某个仓库，它只需从 WAL 中将其物化即可。
* 推送在 S3 上使用原子比较并交换（CAS）操作，这允许*任何*服务器充当主节点，而无需领导者选举（leader election）的开销。

### 复制
> ### Replication
> Continuity achieves horizontal scalability by leveraging S3 and lightweight **UDP gossip packets** for optimistic replication.
> * Replicas receive metadata via UDP and check for updates using conditional S3 requests (`ETags`).
> * If a UDP packet is dropped, a quick conditional GET (`304 Not Modified` or `200 OK` with the latest WAL index) ensures the replica catches up instantly.
> * This allows massive monorepos to scale to hundreds of read replicas for CI, while ephemeral agent repositories can scale down to a single replica (or zero when idle, since S3 preserves the state).
Continuity 通过利用 S3 和轻量级 **UDP 绯闻协议（gossip packets）** 进行乐观复制，实现了水平可扩展性。
* 副本通过 UDP 接收元数据，并使用条件 S3 请求（`ETags`）检查更新。
* 如果 UDP 数据包丢失，一次快速的条件 GET 请求（`304 Not Modified` 或带有最新 WAL 索引的 `200 OK`）可确保副本瞬间追赶上最新状态。
* 这使得超大单体仓库能够扩展到数百个用于 CI 的只读副本，而短暂的智能体仓库则可以缩减到单个副本（或者在空闲时缩减为零，因为 S3 保留了状态）。

### 压缩
> ### Compaction
> Unbounded WALs and fragmented Git packfiles require maintenance. In Continuity, **only the primary node performs compactions**. 
> * The compaction result is written to the on-disk repository and uploaded to S3.
> * Replicas avoid heavy CPU repacking entirely; they simply download the pre-compacted packfiles directly from S3, trading network bandwidth for compute power.
无限制增长的 WAL 和碎片化的 Git 包文件需要维护。在 Continuity 中，**只有主节点执行压缩（compaction）**。
* 压缩结果被写入磁盘上的仓库并上传到 S3。
* 副本完全避免了高 CPU 消耗的重新打包操作；它们只需直接从 S3 下载预先压缩好的 packfiles，从而用网络带宽换取计算能力。

### 规模
> ### Scale
> Through rigorous stress testing, Continuity demonstrates robust, predictable throughput:
> * **S3 Standard:** Sustains up to 120 pushes/s while continuously compacting and replicating.
> * **S3 Express One Zone:** Ingests over 300 pushes/s, where performance is bottlenecked solely by local Git compaction speeds rather than network storage latency.
经过严格的压力测试，Continuity 表现出了强大且可预测的吞吐量：
* **S3 Standard：** 在持续压缩和复制的同时，可维持高达 120 次推送/秒。
* **S3 Express One Zone：** 每秒可摄入超过 300 次推送，其性能瓶颈仅受限于本地 Git 压缩速度，而非网络存储延迟。

![Push and clone throughput comparison chart](./images/replica-throughput.png)

### WAL 即真理
> ### WAL as Truth
> By anchoring durability and consensus entirely in S3 rather than fragile on-disk state or external relational databases, Continuity guarantees global consistency. Every push has full provenance data, allowing the system to rewind, fast-forward, or debug corrupted states effortlessly using standard, off-the-shelf Git tooling.
通过将持久性和共识完全锚定在 S3 中，而不是脆弱的磁盘状态或外部关系型数据库中，Continuity 保证了全局一致性。每次推送都拥有完整的来源数据，使系统能够使用标准的、现成的 Git 工具轻松地进行回滚、快进（fast-forward）或调试受损状态。

---

## 根源 (Origin)

> Source code hosting is mission-critical infrastructure. With the rise of AI agents generating unprecedented volumes of code, pull requests, and CI runs, version control performance directly impacts developer velocity.
源代码托管是至关重要的关键基础设施。随着生成海量代码、拉取请求（PR）和 CI 运行的 AI 智能体的崛起，版本控制性能直接影响着开发者的效率。

> **Origin** is Cursor's production-grade Git storage platform built on Continuity. It is engineered to solve modern version control bottlenecks, providing unmatched reliability, linearizable performance, and seamless horizontal scale for teams of any size.
**Origin** 是 Cursor 基于 Continuity 构建的生产级 Git 存储平台。它旨在解决现代版本控制的瓶颈，为任何规模的团队提供无与伦比的可靠性、线性一致的性能以及无缝的水平扩展能力。