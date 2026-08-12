---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-13
hide:
- navigation
tags:
- 数据库
- 性能优化
- PostgreSQL
- Supabase
- 架构设计
title: 何时选择只读副本（Read Replicas）与更大计算资源（Bigger Compute）
---
### 文章背景与核心概要

当数据库性能开始下降时，架构师通常面临一个核心抉择：是进行垂直扩展（增加计算资源）还是水平扩展（添加只读副本）。这两种方案并非万能，其适用性完全取决于当前的业务负载特征、预算限制以及性能瓶颈的本质。

本文旨在提供一套决策框架，帮助开发者通过分析查询模式和读写比例，判断何时应通过升级实例规格来提升处理能力，何时应通过引入只读副本实现负载隔离或地理分布。同时，文章还介绍了连接池（Supavisor）、数据管道（Pipelines）及分片技术（Multigres）等进阶扩展方案，为应对大规模数据挑战提供了技术参考。

---

## 1. 先诊断问题
在投入硬件成本之前，请先确定问题的根本原因，以避免资源浪费。

### 分析查询模式
使用 `pg_stat_statements` 视图来识别数据库时间主要消耗在何处：

> Use the `pg_stat_statements` view to identify where your database time is being spent:
```sql
select
  calls,
  mean_exec_time::numeric(10,2) as avg_ms,
  total_exec_time::numeric(10,2) as total_ms,
  query
from pg_stat_statements
order by total_exec_time desc
limit 20;
```

*   **慢查询：** 优先优化这些查询。
*   **大量快速查询：** 你可能需要更多的容量。
*   **分析任务与生产任务竞争：** 你需要进行工作负载隔离。

> *   **Slow queries:** Optimize these first.
> *   **Many fast queries:** You likely need more capacity.
> *   **Analytics competing with production:** You need workload isolation.

### 检查读写比例
只读副本仅能辅助处理读取流量。如果你的工作负载是写密集型的，副本将无法提供帮助。

> Read Replicas only assist with read traffic. If your workload is write-heavy, replicas will not provide relief.
```sql
select
  sum(seq_tup_read + idx_tup_fetch) as reads,
  sum(n_tup_ins + n_tup_upd + n_tup_del) as writes,
  round(100.0 * sum(seq_tup_read + idx_tup_fetch) / nullif(sum(seq_tup_read + idx_tup_fetch + n_tup_ins + n_tup_upd + n_tup_del), 0), 1) as read_percentage
from pg_stat_user_tables;
```

---

## 2. 何时选择更大计算资源（Bigger Compute）
垂直扩展是最简单的路径。它不需要更改代码，并能提供即时的性能缓解。

> Vertical scaling is the simplest path. It requires no code changes and provides immediate relief.

*   **写密集型工作负载：** 由于所有的 `INSERT`、`UPDATE` 和 `DELETE` 操作都必须在主库上执行，因此更大规格的实例是你唯一的选择。
*   **尚有余力的空间：** 如果你尚未达到 16XL 规格，升级通常只需一键操作。
*   **优化查询：** 始终确保你的查询已建立索引。使用 `EXPLAIN ANALYZE` 来识别顺序扫描（Sequential Scans）。有时，一个合理的索引比每月 200 美元的升级更有效。

> *   **Write-Heavy Workloads:** Since all `INSERT`, `UPDATE`, and `DELETE` operations must hit the primary, a larger instance is your only option.
> *   **Available Headroom:** If you are not yet at the 16XL tier, upgrading is a one-click operation.
> *   **Optimized Queries:** Always ensure your queries are indexed. Use `EXPLAIN ANALYZE` to identify sequential scans. Sometimes, a well-placed index is more effective than a $200/month upgrade.

---

## 3. 何时选择只读副本（Read Replicas）
只读副本引入了架构复杂性，但解锁了特定的扩展能力：

> Read Replicas introduce architectural complexity but unlock specific scaling capabilities:

*   **工作负载隔离：** 将繁重的分析任务（如 Metabase、Looker）转移到副本上，这样它们就不会耗尽生产 API 的资源。
*   **地理分布：** 将副本部署在离用户更近的地方，以减少网络延迟。
*   **规模化成本效益：** 在更高规格的层级中，添加一个较小的副本通常比将主实例规格翻倍更具成本效益。
*   **冗余：** 副本提供了热备用，如果主实例遇到问题，可以减少影响范围。

> *   **Workload Isolation:** Move heavy analytics (e.g., Metabase, Looker) to a replica so they don't starve your production API of resources.
> *   **Geo-Distribution:** Deploy replicas closer to your users to reduce network latency.
> *   **Cost Efficiency at Scale:** At higher tiers, adding a smaller replica is often more cost-effective than doubling the size of your primary instance.
> *   **Redundancy:** Replicas provide a warm standby, reducing the blast radius if your primary instance encounters issues.

---

## 4. 进阶扩展选项

### 连接池（Supavisor）
如果你达到了连接数限制但 CPU 使用率正常，请启用 **Supavisor**。它是免费的，并内置于每个 Supabase 项目中，用于多路复用连接。

> If you are hitting connection limits but CPU usage is healthy, enable **Supavisor**. It is free and built into every Supabase project to multiplex connections.

### Supabase Pipelines
如果你的分析查询需要扫描数百万行数据，即使是只读副本也可能吃力。**Supabase Pipelines** 使用变更数据捕获（CDC）将数据流式传输到专门的分析目的地，从而将操作型数据库与数据仓库需求分离开来。

> If your analytics queries scan millions of rows, even a Read Replica may struggle. **Supabase Pipelines** uses Change Data Capture (CDC) to stream data to a dedicated analytical destination, separating your operational database from your data warehousing needs.

### Multigres
对于即使最大计算规格也无法满足的超大规模场景，**Multigres** 是 Postgres 水平写扩展的未来，它为你的基础设施带来了 Vitess 风格的分片和自动路由功能。

> For massive scale where even the largest compute tier is insufficient, **Multigres** is the future of horizontal write scaling for Postgres, bringing Vitess-style sharding and automatic routing to your infrastructure.

---

## 5. 决策框架总结

| 因素 | 选择更大计算资源 | 选择只读副本 |
| :--- | :--- | :--- |
| **工作负载** | 写密集型或均衡型 | 读密集型 (80%+) |
| **当前层级** | 低于 16XL | 达到或接近 16XL |
| **复杂性** | 简单（无需更改） | 需要路由逻辑 |
| **主要用途** | 通用扩展 | 分析隔离、地理分布 |
| **代码更改** | 无需更改 | 极小（连接字符串） |

> | Factor | Choose Bigger Compute | Choose Read Replicas |
> | :--- | :--- | :--- |
> | **Workload** | Write-heavy or balanced | Read-heavy (80%+) |
> | **Current Tier** | Below 16XL | At or approaching 16XL |
> | **Complexity** | Simple (no changes) | Requires routing logic |
> | **Primary Use Case** | General scaling | Analytics isolation, Geo-distribution |
> | **Code Changes** | None required | Minimal (connection strings) |

**准备好扩展了吗？** 导航至 Supabase 控制台的 **Project Settings > Infrastructure**，即可升级你的计算资源或配置新的只读副本。

> **Ready to scale?** Navigate to **Project Settings > Infrastructure** in your Supabase Dashboard to upgrade your compute or provision a new Read Replica.