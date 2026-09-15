---
authors:
  - aitoboxrobot
categories:
  - 研究解读
date: 2026-09-16
hide:
  - navigation
tags:
  - Meta
  - 分布式系统
  - ZGateway
  - ZippyDB
  - 高性能代理
title: "Meta 推出 ZGateway：统一 ZippyDB 流量、每秒处理超 10 亿次请求的无状态代理层"
---

# Meta 推出 ZGateway：统一 ZippyDB 流量、每秒处理超 10 亿次请求的无状态代理层

> # Meta Introduces ZGateway: A Stateless Proxy Tier That Unifies ZippyDB Traffic and Handles Over 1 Billion Operations Per Second

### 文章背景与核心概要

在超大规模分布式架构中，客户端直连底层数据库集群极易导致连接数呈爆炸式膨胀。在 Meta 内部，支撑全系产品元数据、计数器与配置系统的分布式键值存储 ZippyDB，曾面临着上百万台客户端主机直连带来的严重连接蔓延 (Connection Sprawl) 与重连风暴危机。为了从根本上化解这一工程瓶颈，Meta 研发并上线了无状态代理层 ZGateway。它不仅解耦了客户端与底层存储节点，将单机连接数大幅缩减 97% 以上，更逐步演进为一个集动态请求合流、自适应负载分流、内存读缓存与跨地域容灾于一体的综合流量底座。如今，ZGateway 以仅约 6% 的极低计算开销，稳定承载着 ZippyDB 全网约 40% 的数据流量，每秒处理操作数突破 10 亿大关，为超大规模基础设施的代理层设计树立了全新标杆。

---

## 📌 执行摘要

> ## 📌 Executive Summary

Meta 正式发布了 **ZGateway**——这是一个架设在客户端应用程序与 [ZippyDB](https://engineering.fb.com/2021/08/06/core-infra/zippydb/) 之间的强大无状态代理层 (Stateless Proxy Tier)。ZippyDB 作为 Meta 内部广泛使用的分布式键值存储 (Key-Value Store)，承载着全系产品的核心元数据、计数器和配置系统。ZGateway 最初的诞生，是为了彻底解决上百万台客户端主机直连数据库所带来的严重连接蔓延 (Connection Sprawl) 难题；而如今，它已进化为一个功能完备的综合性流量平台，全面接管了请求批处理 (Batching)、准入控制 (Admission Control)、内存缓存 (Caching) 以及故障转移 (Failover) 等核心能力。目前，ZGateway 每秒处理的操作数已突破 **10 亿次**，在仅产生约 6% 极低计算开销的前提下，承载了整个 ZippyDB 全网约 40% 的流量。

> Meta has introduced **ZGateway**, a powerful stateless proxy tier positioned between client applications and [ZippyDB](https://engineering.fb.com/2021/08/06/core-infra/zippydb/), Meta's widely used key-value store powering product metadata, counters, and configurations. Originally designed to resolve severe connection sprawl across more than a million client hosts, ZGateway has evolved into a comprehensive platform handling batching, admission control, caching, and failover. Today, it processes over **1 billion operations per second** and carries roughly 40% of all ZippyDB traffic at a minimal computational overhead of about 6%.

---

## 为什么 ZippyDB 急需引入代理层

> ## Why ZippyDB Needed a Proxy

在传统的客户端直连架构 (Direct-Access Architecture) 下，每一个 ZippyDB 客户端都必须与它需要访问的所有数据库主机直接建立连接。由于单个客户端在业务周期内可能需要触达分散在数十万台主机上的数万个分片 (Shards)，导致客户端与数据库节点双方都背负了极其沉重的包袱——单机往往需要维系成千上万条持久的 TLS 连接。

> Under a direct-access architecture, every ZippyDB client directly connected to every database host it needed to reach. Because a single client could touch tens of thousands of shards across hundreds of thousands of hosts, both clients and database hosts carried massive burdens of tens of thousands of TLS connections. 

* **资源严重枯竭 (Resource Exhaustion)：** 哪怕只是空闲的静默连接，在链路两端也会持续霸占宝贵的内存、CPU 周期以及文件描述符 (File Descriptors)。
* **重连风暴频发 (Reconnection Storms)：** 随着客户端实例集群规模的膨胀，数据库端的入站连接数呈指数级蹿升，多次因文件描述符耗尽和内存溢出 (Out-Of-Memory, OOM) 导致服务进程直接崩溃。
* **灾难性的无限重启循环 (The Reboot Loop Incident)：** 在一次著名的系统事故中，一个路由 Bug 导致全网所有客户端对每一个分片都强行建立了一条独立连接，瞬时爆发的连接洪峰直接将整个数据库集群拖入了灾难性的死循环重启。
* **客户端治理寸步难行 (Client-Side Hurdles)：** 企图在客户端侧解决此问题完全不可行，因为全公司有数百个相互独立的业务团队各自维护着不同技术栈的客户端代码，推动统一改造犹如天方夜谭。

> * **Resource Exhaustion:** Each idle connection consumed valuable memory, CPU, and file descriptors on both ends.
> * **Reconnection Storms:** Inbound connection counts grew with every client cohort, leading to crashes from file descriptor exhaustion and out-of-memory (OOM) errors. 
> * **The Reboot Loop Incident:** During one notable incident, a routing bug caused every client to open a connection per shard, throwing the entire database fleet into a catastrophic reboot loop.
> * **Client-Side Hurdles:** Fixing this on the client side was completely impractical because hundreds of independent teams owned various parts of the client fleet.

---

## 什么是 ZGateway？

> ## What is ZGateway?

[ZGateway](https://engineering.fb.com/2026/09/03/core-infra/zgateway-proxy-zippydb-meta/) 是部署在 ZippyDB 客户端与底层 ZServer 数据库集群之间的一个无状态代理层。它作为区域服务层运行，通过 Meta 的自研服务网格 (Service Mesh) [ServiceRouter](https://atscaleconference.com/servicerouter-hyperscale-service-mesh-at-meta/) 实现服务发现与路由，主要提供两种工作形态：**纯透明代理 (Pure Proxy)** 与**直读缓存 (Read-Through Cache)**。

> [ZGateway](https://engineering.fb.com/2026/09/03/core-infra/zgateway-proxy-zippydb-meta/) is a stateless proxy tier deployed between ZippyDB clients and the ZServer database fleet. Running as regional tiers discovered via Meta’s service mesh, [ServiceRouter](https://atscaleconference.com/servicerouter-hyperscale-service-mesh-at-meta/), it operates in two primary flavors: **a pure proxy** and **a read-through cache**. 

在底层实现上，ZGateway 直接复用了 Meta 高度优化的厚客户端 (Thick Client) C++ ZippyDB 库，本质上相当于将一个功能强大的 ZippyDB 客户端封装成了一项云原生托管服务。

> Under the hood, ZGateway utilizes Meta's thick C++ ZippyDB client, effectively operating as a ZippyDB client run as a managed service. 

### 请求生命周期

> ### Request Lifecycle

1. **建连与安全终止 (Connection & Termination)：** 客户端通过粘性连接 (Sticky Connection) 将请求发送至所在区域的 ZGateway 节点，由网关统一进行 TLS 握手与连接终止。
2. **安全鉴权与流量整形 (Security & Shaping)：** 网关依据各业务场景的访问控制列表 (ACL) 执行鉴权，并对各个租户实施细粒度的准入控制与流量整形。
3. **路由解析与合并缓存 (Routing & Caching)：** 网关解析出目标分片，在开启缓存的服务层上检索本地缓存；若未命中，则将该请求与发往同一分片并在排队中的其他并发请求进行自动批处理合流。
4. **请求转发与回传 (Forwarding)：** 请求被转发至正确的存储副本节点，返回的响应数据再由网关反多路复用解包回传给对应客户端，同时全面采集指标监控、分布式追踪并记录配额消耗。

> 1. **Connection & Termination:** A client sends requests over a sticky connection to a regional ZGateway host, which terminates TLS.
> 2. **Security & Shaping:** The gateway authorizes requests against the use case's ACLs and applies per-tenant admission control and traffic shaping.
> 3. **Routing & Caching:** It resolves the target shard, checks the local cache (on caching tiers), and batches the request with other in-flight work destined for that shard.
> 4. **Forwarding:** Requests are forwarded to the correct replicas, and responses are demultiplexed back with metrics, traces, and quota usage recorded. 

---

## 扇入与扇出的数学建模解析

> ## The Fan-In and Fan-Out Math

Meta 工程师团队采用了经典的“球投入桶 (Balls-into-Bins)”概率模型对整个集群的连接分布进行了数学建模。当存在 $B$ 个分片和 $H$ 台主机时，主机被命中的期望值为：

> Meta models the fleet using a balls-into-bins probability model, where $B$ shards and $H$ hosts result in a host hit probability of:

$$\text{E}(H,B) = H \left(1 - e^{-B/h}\right)$$

基于包含 20 个可用大区 (Regions)、500,000 台数据库主机、30,000 台代理主机、1,000,000 个客户端实例以及每个客户端平均触达 50,000 个分片的仿真测算：

> Using simulated figures of 20 regions, 500,000 database hosts, 30,000 proxy hosts, 1,000,000 clients, and 50,000 shards per client:

* 单机连接数骤减了约 **97% 至 98%**。
* 全网持久连接总量暴跌了约 **19 倍**。
* **扩缩容维度的质变优势 (Scaling Advantage)：** 在客户端直连模式下，数据库的入站扇入 (Fan-In) 连接数会随着客户端数量呈严格线性增长；而在引入 ZGateway 后，数据库的扇入规模被彻底压缩至“大区数量 $\times$ 单机分片密度”的数量级——完全与客户端和数据库机器规模实现了解耦！

> * Per-host connection counts collapse by roughly **97% to 98%**.
> * Total persistent connections drop by about **19x**.
> * **Scaling Advantage:** Direct-access fan-in grows linearly with the number of clients, whereas ZGateway fan-in is reduced to roughly the number of regions times shard density per host—completely independent of both the client and database fleets.

---

## ZGateway 带来的核心系统能力

> ## Capabilities Enabled by ZGateway

* **平滑安全迁移 (Safe Migration)：** 针对每个具体服务和分片前缀精确配置的灰度开关，支持按比例线性切流、地域过滤以及一键熔断的全局紧急停机开关 (Global Kill Switches)。
* **差异化精准卸载 (Discriminant Load Shedding, DLS)：** 请求会映射至按优先级切分的租户级独立队列桶 (Buckets)，并通过轮询 (Round-Robin) 方式调度消费。在模拟的高载压力测试下 (在覆盖约 1,350 个租户队列且 CPU 超过 90% 的超载场景下)，系统仅精准丢弃突发滥用资源的“吵闹邻居 (Noisy Neighbors)”的流量；而其余正常租户的请求中 99.9% 畅通无阻、零拒绝，在仅耗费 8% CPU 开销的前提下维持了高达 97% 至 98% 的有效吞吐量 (Goodput)。
* **内存读缓存 (Read Caching)：** 缓存型网关集群能够在进程内直接响应高频热点读取；针对缓存未命中，采用基于键粒度的回填锁 (Per-Key Fill Locks) 防止缓存击穿，并通过变更数据捕获 (Change-Data-Capture, CDC) 事件在有界陈旧度契约 (Bounded-Staleness Contract) 下保障数据的新鲜度。
* **智能负载均衡 (Load Balancing)：** 网关集群混合部署了从约 26 核到 126 核不等的新老异构硬件，控制平面的负载均衡器会根据各主机近期的实际 CPU 负载，动态、逆向微调其在 ServiceRouter 中的权重配比。
* **跨区域容灾韧性 (Cross-Region Resilience)：** 借助全局路由、超大区域 (Mega-Regions) 以及环形拓扑 (Rings)，当某个区域的代理层因流量洪峰达到饱和时，能够以完全对上层透明的方式无缝转移至邻近的富余算力节点。
* **统一事务处理 (Transactions)：** 原本散落在客户端内部极其复杂的事务记账与状态维护逻辑被统一收拢至网关层，成功将繁琐的事务阶段集中管控，在零可靠性退化的情况下平稳接管了 100% 的分布式事务流量。

> * **Safe Migration:** Configuration flags scoped per service and shard prefix enable percentage-based traffic ramping, region filtering, and global kill switches.
> * **Discriminant Load Shedding (DLS):** Requests are mapped to per-tenant buckets split by priority that drain in a round-robin fashion. If a tenant floods the system during controlled overloads (above 90% CPU across ~1,350 tenant buckets), only the noisy neighbors shed load. The rest execute 99.9% of requests with zero rejections, holding goodput near 97% to 98% at an 8% CPU cost.
> * **Read Caching:** Caching tiers serve hot reads entirely in-process, utilizing per-key fill locks on misses and maintaining freshness via change-data-capture (CDC) events under a bounded-staleness contract.
> * **Load Balancing:** Tiers mix ~26-core to ~126-core hosts, where a control-plane balancer actively nudges each host's ServiceRouter weight inversely to its recent CPU load.
> * **Cross-Region Resilience:** Global routing, mega-regions, and rings allow a saturated regional tier to transparently fail over to healthy capacity nearby.
> * **Transactions:** Client-side transaction bookkeeping was successfully moved into the gateway, consolidating complex phases to handle 100% of transaction traffic with zero reliability regressions.

---

## 核心要点总结

> ## Key Takeaways

* **惊人的承载规模 (Massive Scale)：** ZGateway 每秒处理的操作数超过 **10 亿次**，以仅约 6% 的极小计算损耗承载了 ZippyDB 全网约 40% 的庞大流量。
* **有界的入站扇入 (Bounded Fan-In)：** 将数据库底层的扇入压力，从与客户端机器数绑定且无休止增长的线性模型，彻底转化为严格可控、具有确定上限的有界常数级指标。
* **高效的流量聚合 (Traffic Coalescing)：** 跨客户端的全局批处理机制有效化解了热点键引发的并发雪崩 (Hot-Key Stampedes)，同时淘汰了脆弱、分散且难以维护的厚客户端分发库。
* **极强的多租户隔离 (Robust Isolation)：** 差异化精准卸载在 CPU 极端重载下成功锁定了约 1,350 个租户中的 6 个异常吵闹租户并予以定向限流，同时确保了整体系统高达 97% 至 98% 的有效吞吐量。
* **经典的基础设施架构典范 (Architectural Pattern)：** 虽然 ZGateway 深度绑定了内部生态并未开源，但其分层解耦与流量统一治理的设计模式，为现代超大规模基础设施架构提供了极具指导意义的工程范式。

> * **Massive Scale:** ZGateway handles over **1B operations/sec** and carries ~40% of ZippyDB traffic with just ~6% overhead.
> * **Bounded Fan-In:** Converts database fan-in from a linear growth model tied to client counts into a strictly controlled, bounded metric.
> * **Traffic Coalescing:** Cross-client batching effectively neutralizes hot-key stampedes while retiring fragile, distributed client libraries.
> * **Robust Isolation:** Discriminant Load Shedding successfully isolated 6 noisy tenants out of ~1,350 during high CPU stress while maintaining 97–98% goodput.
> * **Architectural Pattern:** While not deployable externally outside of Meta, the structural patterns provide a blueprint for hyperscale infrastructure design.

---

## 参考资料与延伸阅读

> ## References & Further Reading

* 阅读官方原版 [Meta 技术博客文章 (Meta Engineering Blog Post)](https://engineering.fb.com/2026/09/03/core-infra/zgateway-proxy-zippydb-meta/)。
* 查看官方 [X (Twitter) 发布公告](https://x.com/Meta_Engineers/status/2099511815055270182)。
* 通过 [Twitter](https://x.com/intent/follow?screen_name=marktechpost) 与社区交流，加入拥有超过 15 万成员的 [ML Subreddit](https://www.reddit.com/r/machinelearningnews/)，订阅[时事通讯 (Newsletter)](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526?email={{email}})，或关注 [Telegram 频道](https://t.me/machinelearningresearchnews)。

> * Read the original [Meta Engineering Blog Post](https://engineering.fb.com/2026/09/03/core-infra/zgateway-proxy-zippydb-meta/).
> * View the [X (Twitter) Announcement](https://x.com/Meta_Engineers/status/2099511815055270182).
> * Connect with the community via [Twitter](https://x.com/intent/follow?screen_name=marktechpost), join the [150k+ ML Subreddit](https://www.reddit.com/r/machinelearningnews/), subscribe to the [Newsletter](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526?email={{email}}), or join the [Telegram Channel](https://t.me/machinelearningresearchnews).
