---
authors:
- aitoboxrobot
categories:
- 产品发布
date: 2026-08-13
hide:
- navigation
tags:
- Supabase
- Storage
- 性能优化
- 数据安全
- OpenTelemetry
title: Supabase Storage：性能、安全性与可靠性的重大更新
---
### 文章背景与核心概要
Supabase 近期为其全区域的 Storage（对象存储）服务推出了一系列重大更新。此次发布对对象列表（object listing）功能进行了彻底的架构重写，使深度分页速度最高提升了 14.8 倍；同时引入了强健的安全性增强功能（包括路径遍历防御和 SQL 删除保护）、防弹级的自愈迁移机制、OpenTelemetry 可观测性，以及针对企业级工作负载的关键错误修复。

对于管理海量文件和高并发请求的开发团队而言，这些改进显著提升了系统的吞吐能力与稳定性。新版本已在所有区域上线，开发者无需修改现有代码即可享受这些性能与安全红利。

---

## 📋 Table of Contents
- [Security](#security)
  - [Path Traversal Prevention](#path-traversal-prevention)
  - [Preventing Accidental Deletes via Direct SQL](#preventing-accidental-deletes-via-direct-sql)
- [Performance](#performance)
  - [Object Listing Rewrite](#object-listing-rewrite)
  - [Query Cancellation and Statement Timeouts](#query-cancellation-and-statement-timeouts)
- [Reliability](#reliability)
  - [Idempotent Migrations](#idempotent-migrations)
  - [TUS Zombie Lock Fix](#tus-zombie-lock-fix)
  - [Orphan Object Scanner Improvements](#orphan-object-scanner-improvements)
- [Observability](#observability)
  - [OpenTelemetry Metrics](#opentelemetry-metrics)
  - [Server Execution Time in Logs](#server-execution-time-in-logs)
- [Bug Fixes](#bug-fixes)
- [Get Started](#get-started)

---

## Security

### Path Traversal Prevention
文件后端现在无法再读取或写入配置存储路径之外的文件。此前，精心构造的路径可能会逃逸出存储根目录。这一漏洞现已完全堵上。([GitHub](https://github.com/supabase/storage/pull/818))

> ### Path Traversal Prevention
> The file backend can no longer read or write files outside the configured storage path. Previously, a crafted path could escape the storage root. This vulnerability is now fully closed. ([GitHub](https://github.com/supabase/storage/pull/818))

### Preventing Accidental Deletes via Direct SQL
在 SQL 中直接运行 `DELETE FROM storage.objects` 是导致孤儿对象（即数据库行被删除，但 S3 或文件后端中的文件残留）的最常见原因。现在引入了一个新的语句级触发器，除非将会话变量 `storage.allow_delete_query` 设置为 `true`，否则该触发器会拒绝 Storage 模式表上的 `DELETE` 查询。

存储 API 会自动设置此标志，这意味着正常操作完全不受影响，而直接通过 SQL 删除则默认会被阻止。([GitHub](https://github.com/supabase/storage/pull/817))

> ### Preventing Accidental Deletes via Direct SQL
> Running `DELETE FROM storage.objects` directly in SQL was the most common cause of orphan objects, where the database row was removed but the file in S3 or the file backend was left behind. A new statement-level trigger now rejects `DELETE` queries on Storage schema tables unless the session variable `storage.allow_delete_query` is set to `true`. 
> 
> The Storage API sets this flag automatically, meaning normal operations remain completely unaffected while direct SQL deletes are blocked by default. ([GitHub](https://github.com/supabase/storage/pull/817))

---

## Performance

### Object Listing Rewrite
旧的 `prefixes` 表需要在每次对象插入、更新和删除时进行写操作，以保持文件夹结构的同步。在高并发和大量对象的场景下，这造成了严重的瓶颈。管理 6000 万个或更多对象的企业客户经常触及写入吞吐量限制。

我们用一个混合的**跳跃扫描算法（skip-scan algorithm）**替换了整个系统，该算法直接从 `objects` 表中动态推导文件夹结构。此外，基于 OFFSET 的分页已被**基于游标的分页（cursor-based pagination）**所取代，无论深度如何，它都能在常量时间内运行。
* **基准测试结果：** 在拥有 6000 万行数据的表中，深度分页速度提升高达 **14.8 倍**，且没有任何写入性能惩罚。
* *注意：* 旧的 `prefixes` 表、`level` 列以及两个相关的索引已被完全废弃。虽然 API 会自动处理所有事务，但我们建议切换到 `listV2` 端点以最大化这些性能提升。

> ### Object Listing Rewrite
> The old prefixes table required a write operation on every object insert, update, and delete to keep the folder structure synchronized. At high concurrency and large object counts, this created a significant bottleneck. Enterprise customers managing 60 million or more objects were regularly hitting write-throughput limits.
> 
> We replaced the entire system with a hybrid **skip-scan algorithm** that derives folder structure on-the-fly directly from the `objects` table. Additionally, OFFSET-based pagination has been replaced with **cursor-based pagination**, running in constant time regardless of depth. 
> * **Benchmark Results:** On a table with 60 million rows, deep pagination is up to **14.8x faster** with zero write penalty. 
> * *Note:* The old prefixes table, level column, and two related indexes have been dropped entirely. While the API handles everything automatically, we recommend switching to the `listV2` endpoint to maximize these performance gains.

### Query Cancellation and Statement Timeouts
当客户端断开连接时，正在运行的 Postgres 查询现在会使用原生的 Postgres 取消协议（与 pgBouncer 完全兼容）被主动取消。此外，通过 `DB_STATEMENT_TIMEOUT` 环境变量引入了可配置的 30 秒查询语句超时限制。([GitHub](https://github.com/supabase/storage/pull/841))

> ### Query Cancellation and Statement Timeouts
> When a client disconnects, in-flight Postgres queries are now actively cancelled using the native Postgres cancel protocol (fully compatible with pgBouncer). Furthermore, a configurable 30-second query statement timeout has been introduced via the `DB_STATEMENT_TIMEOUT` environment variable. ([GitHub](https://github.com/supabase/storage/pull/841))

---

## Reliability

### Idempotent Migrations
所有 Storage 迁移现在都完全具备幂等性。您可以安全地清空 `storage.migrations` 表并重新运行整个迁移链，而不会遇到错误。CI 管道现在会执行两次完整的迁移套件并比较 `pg_dump` 输出以验证完整性，从而消除了关于卡住迁移的常见技术支持瓶颈。([GitHub](https://github.com/supabase/storage/pull/805))

> ### Idempotent Migrations
> All Storage migrations are now fully idempotent. You can safely clear the `storage.migrations` table and replay the entire migration chain without encountering errors. CI pipelines now execute the full migration suite twice and compare `pg_dump` outputs to verify integrity, eliminating common support bottlenecks regarding stuck migrations. ([GitHub](https://github.com/supabase/storage/pull/805))

### TUS Zombie Lock Fix
TUS 可恢复上传的 S3 锁中存在一个竞态条件（race condition），有时会留下一个永不过期的孤儿锁。这种情况发生在锁在续期周期内被释放时——具体是在 S3 的 `GET` 和 `PUT` 调用之间。现在的续期机制在最终确定之前会显式检查锁是否已经被释放，从而有效堵住了这个竞态条件。([GitHub](https://github.com/supabase/storage/pull/812))

> ### TUS Zombie Lock Fix
> A race condition in the S3 locker for TUS resumable uploads could occasionally leave an orphaned lock that never expired. This occurred if a lock was released during a renewal cycle—specifically between the S3 `GET` and `PUT` calls. The renewal mechanism now explicitly checks whether a lock was already released before finalizing, effectively closing this race condition. ([GitHub](https://github.com/supabase/storage/pull/812))

### Orphan Object Scanner Improvements
孤儿对象扫描器（orphan object scanner）迎来了多项重要升级：
* 在 S3 前缀中使用尾部斜杠，以防止误报匹配（例如，`images` 不再会错误匹配 `images2`）。
* 通过逗号分隔的 ID 添加了对多存储桶（buckets）的支持。
* 引入了可配置的 `DELETE_LIMIT` 环境变量，以更好地控制批处理。
([GitHub](https://github.com/supabase/storage/pull/830))

> ### Orphan Object Scanner Improvements
> The orphan object scanner has received several vital upgrades:
> * Uses trailing slashes in S3 prefixes to prevent false-positive matches (e.g., `images` will no longer incorrectly match `images2`).
> * Adds support for multiple buckets via comma-delimited IDs.
> * Introduces a configurable `DELETE_LIMIT` environment variable for better batch control. 
> ([GitHub](https://github.com/supabase/storage/pull/830))

---

## Observability

### OpenTelemetry Metrics
Storage 指标收集已从 `prom-client` 迁移到 **OpenTelemetry**。现在，指标可以推送至任何兼容 OTel 的后端，同时 Prometheus 抓取功能仍通过 OTel Prometheus 导出器在 `/metrics` 处原生可用。此次更新还附带了一个焕然一新的 Grafana 仪表盘以及预配置的 OTel Collector 设置。([GitHub](https://github.com/supabase/storage/pull/819))

> ### OpenTelemetry Metrics
> Storage has transitioned from `prom-client` to **OpenTelemetry** for metrics collection. Metrics can now be pushed to any OTel-compatible backend, while Prometheus scraping remains natively available at `/metrics` via the OTel Prometheus exporter. This update also ships with a revamped Grafana dashboard and a pre-configured OTel Collector setup. ([GitHub](https://github.com/supabase/storage/pull/819))

### Server Execution Time in Logs
请求日志现在包含详细的服务端执行指标，以帮助追踪性能下降问题。([GitHub](https://github.com/supabase/storage/pull/831))

> ### Server Execution Time in Logs
> Request logs now include detailed server-side execution metrics to help track performance degradation. ([GitHub](https://github.com/supabase/storage/pull/831))

---

## Bug Fixes

* **TUS 上传 URL 中的双斜杠：** 修复了 TUS 可恢复上传 URL 生成时带有双斜杠的问题。([GitHub](https://github.com/supabase/storage/pull/801))
* **PutVector 主体限制：** 将 `PutVector` 端点的主体大小限制从 1.6 MB 提高到 20 MB。([GitHub](https://github.com/supabase/storage/pull/820))
* **无效的 S3 响应标头覆盖：** 在 `response-content-type` 及类似覆盖中提供的无效值不再会导致请求崩溃；现在它们会被静默丢弃。([GitHub](https://github.com/supabase/storage/pull/839))
* **缺失 content-type 回退纠正：** 修正了一个拼写错误，即 S3 适配器回退到了拼写错误的 `application/octa-stream` 而非 `application/octet-stream`。([GitHub](https://github.com/supabase/storage/pull/840))
* **Linux 文件后端 xattr 冲突：** 在 Linux 上，文件后端以前对 content-type 和 etag 使用相同的扩展属性，导致分片上传意外覆盖 content-type。现在每个属性都使用不同的 `xattr` 名称。([GitHub](https://github.com/supabase/storage/pull/842))
* **迁移类型排序：** 生成的 `migration_types.ts` 文件现在能始终按 ID 对迁移进行排序。([GitHub](https://github.com/supabase/storage/pull/845))
* **AWS 流缓冲区修复：** 解决了 S3 适配器在分片上传过程中的流缓冲问题，这是支持 AWS SDK 升级所必需的。([GitHub](https://github.com/supabase/storage/pull/850))
* **列表 v1 中的大小写保留：** 修复了搜索优化带来的回归问题，该问题无意中将所有前缀强制转换为小写。现在可以成功保留原始大小写。([GitHub](https://github.com/supabase/storage/pull/851))

> ## Bug Fixes
> 
> * **Duplicate slash in TUS upload URLs:** Fixed an issue where TUS resumable upload URLs were generated with double slashes. ([GitHub](https://github.com/supabase/storage/pull/801))
> * **PutVector body limit:** Increased the body size limit for the `PutVector` endpoint from 1.6 MB to 20 MB. ([GitHub](https://github.com/supabase/storage/pull/820))
> * **Invalid S3 response header overrides:** Invalid values provided in `response-content-type` and similar overrides no longer crash requests; they are now silently dropped. ([GitHub](https://github.com/supabase/storage/pull/839))
> * **Missing content-type fallback:** Corrected a typo where the S3 adapter fell back to the misspelled `application/octa-stream` instead of `application/octet-stream`. ([GitHub](https://github.com/supabase/storage/pull/840))
> * **Linux file backend xattr collision:** On Linux, the file backend previously used the same extended attribute for both content-type and etag, causing multipart uploads to accidentally overwrite content-types. Each property now utilizes a distinct `xattr` name. ([GitHub](https://github.com/supabase/storage/pull/842))
> * **Migration type ordering:** Generated `migration_types.ts` files now consistently sort migrations by ID. ([GitHub](https://github.com/supabase/storage/pull/845))
> * **AWS stream buffer fix:** Resolved a stream buffering issue in the S3 adapter during multipart uploads, required to support the AWS SDK upgrade. ([GitHub](https://github.com/supabase/storage/pull/850))
> * **Case preservation in list v1:** Fixed a regression from search optimizations that inadvertently forced all prefixes to lowercase. Original casing is now successfully preserved. ([GitHub](https://github.com/supabase/storage/pull/851))

---

## Get Started

这些更改已在所有区域的所有项目中上线。您无需在端侧进行任何代码修改。

* [Storage 文档](https://supabase.com/docs/guides/storage)
* [启动新项目](https://supabase.com/dashboard)
* [自托管 Storage 指南](https://supabase.com/docs/guides/self-hosting/storage)

> ## Get Started
> 
> These changes are already live for all projects across all regions. No code modifications are necessary on your end.
> 
> * [Storage Documentation](https://supabase.com/docs/guides/storage)
> * [Start a New Project](https://supabase.com/dashboard)
> * [Self-Hosting Storage Guide](https://supabase.com/docs/guides/self-hosting/storage)