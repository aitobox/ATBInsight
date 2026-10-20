---
authors:
  - aitoboxrobot
categories:
  - 研究解读
date: 2026-10-21
hide:
  - navigation
tags:
  - Anthropic
  - Claude
  - 版本控制
  - Monorepo
  - Scion
  - AI 智能体
title: "Anthropic 重构版本控制系统：迈向智能体时代的自研系统 Scion"
---

# Anthropic 重构版本控制系统：迈向智能体时代的自研系统 Scion

> # Redesigning Source Control at Anthropic

*10 月 15 日更新：补充了在 Scion 所采用的多项核心技术中扮演先驱角色的相关开源项目细节。*

> *Updated October 15 to include more detail on the projects that pioneered many of the techniques we use in Scion.*

---

### 文章背景与核心概要
在 Anthropic 内部，以 Claude 为代表的自主 AI 编码智能体 (AI Agent) 彻底改变了软件工程的游戏规则，编写代码的速度与体量迎来指数级爆发——仅四个月间单体仓库 (Monorepo) 的日代码合并量便激增十倍以上，传统的分布式版本控制系统 Git 在面对数百 PB 流量与庞大历史记录时陷入全面过载。面对这一由 AI 带来的“甜蜜烦恼”，一个仅有 7 名工程师的小团队在 5 个月内从零研发出专为“智能体规模”设计的自研版本控制系统 Scion，并顺利完成了全量单体代码库的平滑迁移。Scion 颠覆了 Git 的全量离线克隆假设，将客户端默认设为“永远在线”，结合预写日志变更集 (WAL Changeset)、无锁化提交与分层内存缓存架构，将底层基础设施资源占用削减了 200 倍，并实现了以秒为单位的代码极速检出。这一突破不仅揭示了下一代 AI 原生软件工程的基础设施演进范式，更生动展示了人类工程师与 AI 紧密协作重构大型分布式系统的全新实践。

---

## 核心概要

> ## Summary

在 Anthropic，以 Claude 为代表的自主 AI 编码智能体 (AI Agent) 已经从根本上改变了软件工程的生产力瓶颈。如今，编写代码本身已不再是限制开发效率的核心因素；相反，过去专为人类协作节奏量身定制的开发者基础设施——尤其是版本控制系统、构建工具链与持续集成 (CI) 流水线——已经逼近了物理极限。在 2026 年 5 月至 9 月这短短几个月内，Anthropic 核心代码库中每日成功合并的代码变更数量从 2,500 次暴增至超过 30,000 次。

> At Anthropic, autonomous coding agents like Claude have fundamentally shifted the bottleneck of software engineering. Writing code is no longer the limiting factor; instead, developer infrastructure built for human scale—specifically source control, builds, and CI—has hit its limits. Between May and September 2026, daily merged code changes surged from 2,500 to over 30,000.

为了支撑这一爆发式增长，一支仅由 7 名工程师组成的核心团队从零构建了 **Scion**——一个专为“智能体规模 (Agent Scale)”打造的全新自研版本控制系统，并在短短五个月内将公司规模庞大的单体仓库 (Monorepo) 从 Git 全量无缝迁移完毕。本篇技术案例将深入剖析：为何像 Git 这样经典的分布式版本控制系统会在 AI 生产的代码浪潮下不堪重负，Scion 背后的六大核心架构原则是什么，以及工程师在与 Claude 并肩构建高性能开发者基础设施时所获得的深刻洞察。

> To support this exponential growth, a team of seven engineers built **Scion**, an in-house version control system designed from the ground up for "agent scale," and fully migrated their massive monorepo from Git in just five months. This case study details why traditional distributed systems like Git began to strain under the weight of AI-generated code, the core architectural principles behind Scion, and the lessons learned from building high-performance developer tooling alongside Claude.

---

## 极速扩张的单体仓库

> ## Growing Our Monorepo

在 Anthropic 内部，Claude 被广泛应用于闭环迭代前沿科研实验、深度微调复杂系统程序，以及从零开始快速搭建全新服务。这种前所未有的工作负载强度，使得 Anthropic 得以在整个行业遭遇该难题之前，提前数月遭遇极限扩展瓶颈。

> At Anthropic, Claude is utilized to iterate on research loops, micro-optimize complex programs, and build new services from the ground up. This unprecedented workload uncovers scaling bottlenecks long before they hit the broader industry.

```
2026 年 1 月至 9 月，单体代码库每日合并的代码变更量。
Changes merged to our monorepo per day, from January to September 2026.
```
![2026 年 1 月至 9 月，单体代码库每日合并的代码变更量](./images/1e2a750dba61.png)

### Git 面临的扩展瓶颈

> ### The Limitations of Git

Git 本质上是一个去中心化的分布式系统，每一次本地克隆 (Clone) 都是一个自包含的完整版本库，具备在完全离线状态下独立计算代码差异 (Diff)、提交历史和行修改溯源 (Blame) 的全套能力。这种模式虽然对于人类开发者极为理想，但在由智能体主导的超大规模工作场景下却彻底失灵：

> Git is a decentralized system where every clone is a self-contained repository capable of computing diffs, history, and blame offline. While ideal for human developers, this model breaks down at agent scale:

* **令人咋舌的庞大体量**：仅仅是主分支 (main branch) 的版本提交历史就逼近 100 GB，压缩后的工作副本体积也超过了 25 GB。
* **灾难性的网络流量过载**：CI 系统每天需要执行大约 2500 万次代码检出 (Checkout) 操作（这还不包括日常开发环境与科研作业），如果全部直接从原始 Git 仓库拉取，每天将产生超过 600 PB 的天量网络流量。
* **权宜措施难以为继**：尽管团队曾通过搭建内部 Git 镜像和定期制作仓库快照预热包 (Seeds) 来争取缓冲时间，但随着代码合并速率的指数级攀升，这些临时方案的运维成本和失效率正变得令人难以承受。

> * **Massive Scale:** The history of the main branch alone approaches 100 GB, with a compressed working copy exceeding 25 GB.
> * **Traffic Overload:** Performing roughly 25 million code checkouts per day for CI (exclusive of developer environments and research jobs) would generate over 600 PB of Git traffic daily if fetched naively.
> * **Degraded Workarounds:** While internal Git mirrors and repository snapshots (seeds) bought time, they became increasingly difficult to operate as merge rates spiked.

在意识到系统中几乎所有的客户端（包括 AI 智能体和自动化任务）在运行机制上都天然保持在线这一核心事实后，Anthropic 提出了一个颠覆性的根本问题：*如果我们从一开始就以“智能体永远保持在线”为前提来重新设计版本控制系统，它应该呈现出怎样的形态？*

> Recognizing that nearly all of their clients (agents and automated jobs) are online by definition, Anthropic asked a fundamental question: *If we designed source control with the assumption that agents are always online, what would it look like?*

---

## 面向智能体规模版本控制的六大设计原则

> ## Principles for Agent-Scale Source Control

从业界先驱系统（如 Google 的 Piper 以及 Meta 的 Sapling，特别是其服务端组件 Mononoke）中汲取灵感，Scion 确立了六项核心架构设计原则：

> Drawing inspiration from prior art like Google's Piper and Meta's Sapling (specifically its server component, Mononoke), Scion was built on several core principles:

1. **客户端永远保持在线 (Clients are always online)**：不再预设客户端处于脱机离线状态并需要本地维护全量代码拷贝，Scion 的协议设计默认服务端始终在线可达，客户端仅在需要时按需拉取数据。
2. **非对称的客户端/服务端职责划分 (Client-server asymmetry)**：与 Git 中“每个客户端皆可充当服务端”的设计不同，Scion 将历史计算、Blame 溯源、代码合并与 Rebase 变基等繁重计算全部收拢至服务端处理。客户端仅需维护一个体积受限的本地缓存、负责文件布局以及监听文件系统变更事件，本地数据存储量大幅缩减。
3. **以全功能 API 服务驱动新型工程应用 (Comprehensive service powering novel applications)**：所有版本控制核心查询均被封装为标准 API 暴露。自动化故障二分定位 (Bisect) 和自动回滚流水线等后台任务可以直接调用 API 查询仓库数据，而无需拉取或克隆庞大的本地副本。
4. **彻底的横向水平扩展能力 (Horizontal scalability)**：全系统任何地方都不再保存完全物化的完整仓库副本（即便是服务端本身也不例外），彻底摒弃了 Git Packfile 机制，从而消除了昂贵的周期性仓库垃圾回收与维护包袱。
5. **极度轻量、增量且无锁化的提交机制 (Cheap, incremental, and lock-free commits)**：提交操作全量在服务端完成，其开销仅与当前修改的文件体积成正比，而与整个代码库的总体规模完全脱钩。系统不鼓励使用全局引用锁 (Global Refs)，以消除跨服务器节点间的分布式协调瓶颈。
6. **按需稀疏物化的轻量工作区 (Optional and sparse working copies)**：在默认情况下，CI 任务彻底摆脱了全量拉取检出的沉重负担，仅依赖稀疏检出 (Sparse Checkout) 或按需虚拟化文件物化机制按需呈现文件。

> 1. **Clients are always online:** Instead of assuming clients work offline and need complete local copies, Scion protocols assume a reachable server from which clients fetch data on demand.
> 2. **Client-server asymmetry:** Unlike Git (where every client can act as a server), Scion handles history, blame, merges, and rebases on the server. The client maintains a bounded local cache, lays out files, and monitors filesystem changes—requiring far less local data.
> 3. **Comprehensive service powering novel applications:** Source control queries are exposed via API, allowing jobs (such as automated bisect and revert pipelines) to query repository data directly without maintaining local clones.
> 4. **Horizontal scalability:** There is no fully materialized copy of the repo anywhere—not even on the server—and no equivalent to Git packfiles, eliminating the need for repository maintenance.
> 5. **Cheap, incremental, and lock-free commits:** Operations happen server-side and scale with the size of the change rather than the repo's overall size. Global refs are discouraged to avoid cross-server coordination bottlenecks.
> 6. **Optional and sparse working copies:** By default, CI jobs avoid heavy checkouts entirely, relying on sparse checkouts or virtualized file materialization on demand.

```
用于扩展 Git 检出的典型系统架构。
The typical setup for scaling git checkouts.
```
![用于扩展 Git 检出的典型系统架构](./images/ff019752973f.png)

---

## Scion 的底层运作机制

> ## How Scion Works

### 核心数据结构

> ### Data Structures

在 Scion 的世界里，基础工作单元被称为**“变更集 (Changeset)”**——它是预写日志 (Write-Ahead Log, WAL) 中的一条不可变条目。

> In Scion, the unit of work is a **"changeset"**—an entry in a write-ahead log.

* 与传统 Git 中包含完整目录树 (Tree) 指针的 Commit 节点不同，Scion 的变更集仅记录相对于其第一父节点所发生修改的文件清单，同时附带指向对象存储 (Blob Storage) 中经压缩文件内容的按内容寻址指针。
* 系统的吞吐量 (Throughput) 达到了惊人的极高水准，这得益于它摒弃了 Packfile、消除了写锁争用，并摆脱了复杂的引用游标移动（引用指针仅由简单的 CAS 原语行独立管理）。

> * Unlike a Git commit pointing to a tree, a changeset stores a list of files changed relative to its first parent, alongside content-addressed pointers to compressed file contents in blob storage.
> * Throughput is exceptionally high because there are no packfiles, locking, or complex ref movements (refs are handled separately via simple compare-and-swap rows).

```
Scion 中变更集 (Changeset) 的数据模型结构。
The shape of a changeset in Scion.
```
![Scion 中变更集 (Changeset) 的数据模型结构](./images/71c83868210b.png)

为了极速响应文件修改溯源 (Blame) 或指定路径变更历史等复杂查询，Scion 会从变更集中递归构建**“派生数据 (Derived Data)”**。这种模块化解耦设计，使得系统可以在不变更或升级任何客户端的情况下，随时平滑引入全新的服务端索引机制（例如代码复制拷贝检测或基于路径的高速文件搜索）。

> To answer queries like file blame or path history quickly, Scion builds **"derived data"** recursively from changesets. This modular design allows new indices (such as copy-detection or path-based file search) to be added without modifying the client.

### Scion 的大规模水平扩展架构

> ### Scaling Scion

由大量 Scion 服务器构成的分布式集群，实际上扮演了一个超大规模、支持水平线性扩展的高性能缓存层，负责实时动态计算派生数据，并将处理结果写回底层的分布式数据库 Spanner 中。

> A fleet of Scion servers acts as a massive, horizontally scalable cache layer that computes derived data on the fly and writes results back to Spanner.

* **`scn` 客户端命令行工具**：它的运作模式是按内容寻址、按需精准索取客户端当前切实需要的文件树与 Blob 对象，而绝不会在本地与远端之间进行繁冗的全局状态握手协商。
* **分层缓存体系 (Tiered Caching)**：客户端首先与本地守护进程 (`scion-daemon`) 进行高速通信；该进程继而向就近的区域缓存服务器 (`scion-cache`) 发起查询，从内存中直接流式拉取对象数据；若缓存未命中，才最终逐级回退至具备权威数据的核心 `scion-servers` 存储集群。

> * **The `scn` Client:** Operates by requesting specific, content-addressed trees and blobs the client actually wants rather than negotiating existing local state.
> * **Tiered Caching:** Clients talk to a local daemon (`scion-daemon`), which queries regional cache servers (`scion-cache`) streaming objects directly from memory. If missing, caches fall back to authoritative `scion-servers`.

```
Scion 的代码检出架构设计。
Scion’s checkout architecture.
```
![Scion 的代码检出架构设计](./images/cba1eaaa6738.png)

在多层级协同作用下，系统的每一层缓存命中率均持续稳定在 99% 以上。最终，Scion 在 CPU 和内存等核心计算资源消耗上，相比原有的 Git 镜像体系实现了 **200 倍的显著缩减**；与此同时，CI 任务与科研实验的代码检出耗时，也从原先的漫长数分钟骤降至短短数秒之内。

> Each tier maintains a cache hit rate exceeding 99%. As a result, Scion’s infrastructure footprint is **200x smaller** than the previous Git mirroring setup in CPU and memory terms, while CI and research checkouts execute in seconds rather than minutes.

---

## 构建 Scion 的核心洞察与工程启示

> ## What We Learned Building Scion

在打造 Scion 的过程中，团队正值深度内测并使用 *Claude Mythos Preview* 与 *Claude Tag*，这种人机协同的全新研发形态彻底重塑了团队的日常工作方式：

> Building Scion concurrently with the release of *Claude Mythos Preview* and *Claude Tag* transformed how the team operated:

* **令人惊叹的开发加速度**：一支仅有 7 名工程师的小微团队，在短短 5 个月内不仅成功构建了 Scion 核心系统，还同步研发了名为 Antique 的全新定制代码审查工具以及半打配套周边系统，并完成了超大规模仓库的全量平稳割接。
* **工程角色的深刻跃迁**：虽然工程师不再需要亲手敲击每一行具体代码，但人类的专业经验在顶层架构设计、约束边界划定，以及规避智能体发生“过度工程化 (Over-engineering)”或逾越系统边界方面，依然起到了不可替代的舵手作用。
* **极高的系统质量与算法优化深度**：Claude 协助团队产出了经过极为严格的单元测试、模糊测试 (Fuzzing) 以及严密安全加固的高质量代码库，并屡次自主挖掘出诸多复杂的底层算法优化方案——这些优化如果是人工调优，往往需要资深领域专家耗费数周时间苦思冥想。

> * **Rapid Development:** A small team of seven engineers built Scion, Antique (a custom code review tool), and half a dozen related systems while migrating fully in five months.
> * **Shifting Engineering Roles:** While engineers no longer needed to write every line of code manually, their expertise remained vital for defining high-level architecture, setting constraints, and steering agents away from over-engineering or violating system boundaries.
> * **Substantial Quality & Optimization:** Claude helped produce heavily tested, fuzzed, and secure codebases, frequently discovering complex algorithmic optimizations that would have otherwise taken human experts weeks to tune.

```
2026 年 1 月至 9 月，Scion 与 Antique 代码库每周合并的代码变更数量。
Merged changes to the Scion and Antique codebases per week, from January to September 2026.
```
![2026 年 1 月至 9 月，Scion 与 Antique 代码库每周合并的代码变更数量](./images/dd9129671920.png)

* **前沿的单体仓库目录级权限管控**：Scion 原生提供了精细到单个文件目录的严密访问控制策略，在捍卫高度敏感代码安全的同时，完整保留了单体大仓库带来的跨团队协作红利。
* **基于“超级粉丝 (Superfans)”的卓越运维实践**：借助 Claude Tag，团队在 Slack 中建立了由 AI 智能体充当“超级粉丝”的专属监控频道，AI 智能体全天候不间断巡检组件健康状态、系统遥测指标与运行日志，敏锐捕捉人类极难察觉的细微异常。
* **对传统软件工程教条的重新审视**：在合并队列中使用全局仓库锁等传统防御范式正在被彻底颠覆，转而走向基于合入后与部署前的全自动测试验证体系；因为在遇到并发代码冲突时，Claude 往往能在人类工程师反应过来之前，便已极速完成了自动冲突裁决与代码修复。

> * **Advanced Monorepo Security:** Scion supports rich access controls down to individual directories to safeguard sensitive code while preserving the benefits of a unified monorepo.
> * **Operational Excellence via "Superfans":** Using Claude Tag, dedicated Slack channels were set up with AI agents acting as "superfans" monitoring component health, telemetry, and logs around the clock to detect subtle anomalies.
> * **Re-evaluating Priors:** Traditional paradigms like global repository locks on merge queues give way to post-merge and pre-deploy automated testing, as concurrent merge conflicts can be resolved by Claude faster than humans can identify them.

```
在原生 Scion 代码库上观察到的显著性能提升指标。
Observed performance improvements on native Scion repos.
```
![在原生 Scion 代码库上观察到的显著性能提升指标](./images/c706fa6efb4b.png)

---

## 为更广阔的开发者生态提供启示

> ## Contributing to the Wider Ecosystem

尽管 Scion 是专门针对 Anthropic 独特的单体仓库规模与 Token 生成吞吐量量身定制的，但整个软件开发者生态系统很可能在未来 6 到 12 个月内，普遍遭遇类似的扩展瓶颈与性能压力。

> While Scion is tailored specifically to Anthropic's unique monorepo scale and token capacity, the broader developer ecosystem will likely encounter similar scaling pressures over the next 6 to 12 months.

Anthropic 撰写并分享这些实战工程经验，并非呼吁整个行业盲目推倒 Git 进行重写，而是希望以此启发更广泛的业界思考：探索新一代服务端分布式架构、制定适用于 Git 代码托管平台 (Git Forges) 的标准化服务端 RPC 规范，并进一步促进 Git 原生稀疏与浅层检出特性的深度组合演进。

> Rather than advocating for a universal rewrite away from Git, Anthropic hopes to share these insights to encourage new server architectures, standardized server-side RPCs for git forges, and better composition of sparse and shallow Git features.

---

## 补充注释

> ## Footnotes

1. 将变更文件相对于合并的第一父节点进行存储是一种风格层面的工程权衡；在实践中我们发现，在基于主干开发的单体仓库模式下，团队通常只关注主干线上提交的历史演进或修改归属。
2. 特别要提及 Sapling 的服务端组件 [Mononoke](https://github.com/facebook/sapling/blob/main/eden/mononoke/README.md)。它开创了我们在 Scion 中采用的诸多核心技术先河，尤其是其标志性的 [Bonsai](https://github.com/facebook/sapling/blob/79071c2a3ea20c36ed71332608535e5801101bba/eden/mononoke/mononoke_types/serialization/bonsai.thrift#L50) 数据模型。

> 1. Storing changed files relative to the first parent of a merge is a stylistic choice; in practice, we’ve found that people only care about history or blame for commits on the main line in trunk-based development in a monorepo.
> 2. Specifically, the server component of Sapling, [Mononoke](https://github.com/facebook/sapling/blob/main/eden/mononoke/README.md). It pioneered many of the techniques we use in Scion, in particular the [Bonsai](https://github.com/facebook/sapling/blob/79071c2a3ea20c36ed71332608535e5801101bba/eden/mononoke/mononoke_types/serialization/bonsai.thrift#L50) data model.

---

## 作者与致谢

> ## Authors & Acknowledgments

**致谢：** 本文由 Nick G. 联合版本控制工程团队共同撰写：S.G., R.K., Dan C., Garrett H., Ben L., Colin M., Joe P.。特别感谢 Vilas J. 与 Sergiu D. 在这一雄心勃勃的技术探索征程中对版本控制团队的坚定支持，以及 Amir O. 早期对 Antique 工具做出的杰出贡献。

> **Acknowledgements:** Written by Nick G. and the source control team: S.G., R.K., Dan C., Garrett H., Ben L., Colin M., Joe P. Special thanks to Vilas J. and Sergiu D. for supporting the source control team on this ambitious journey, and Amir O. for early contributions to Antique.
