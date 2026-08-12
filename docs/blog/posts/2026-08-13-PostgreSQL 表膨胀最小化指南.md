---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-13
hide:
- navigation
tags:
- PostgreSQL
- 数据库调优
- Vacuum
- 性能优化
- 数据库维护
title: PostgreSQL 表膨胀最小化指南
---
### 文章背景与核心概要
在 PostgreSQL 数据库的日常运行中，表膨胀（Table Bloat）是一个常见但容易被忽视的性能杀手。当表经历大量的更新（UPDATE）和删除（DELETE）操作时，旧的行版本（Tuple）会残留在数据页中，导致物理文件占用空间不断膨胀，进而降低查询效率。虽然 PostgreSQL 提供了 `VACUUM` 和 `autovacuum` 机制来自动清理这些死元组，但由于长事务阻塞、严格锁冲突或默认阈值不合理，自动清理机制往往会失效。

本文深入探讨了 PostgreSQL 底层的数据存储方式（Heap 结构与 8KB 数据页）、`VACUUM` 的工作原理，以及导致表膨胀的常见核心原因。文章结合实用的 SQL 命令与 Supabase CLI 工具，详细介绍了如何监控死元组、调整 `autovacuum` 阈值、处理长事务与锁冲突，并提供了使用 `VACUUM FULL` 和 `pg_repack` 回收文件系统空间的最佳实践，帮助开发者和DBA打造健康高效的数据库环境。

---

## How Data of Postgres Tables Stored
## Postgres 表中的数据是如何存储的

By default, all table data in Postgres are physically stored using the "heap" method. So every database is a set of 1GB files ("segments") and each file is logically split into 8KB pages. Actual table rows are put into any page with enough free space.
> 默认情况下，Postgres 中的所有表数据都使用“堆（heap）”方法进行物理存储。因此，每个数据库都是一组 1GB 大小的文件（称为“段”），并且每个文件在逻辑上被分割为 8KB 大小的页面。实际的表行被放置在任何具有足够空闲空间的页面中。

When the row data is updated, a new version of a whole row is constructed and written (to any free space). The old one remains because, at the time of the update, the transaction is not completed and can be rolled back in the future. When the transaction is completed we’ll have two or several versions of the same row in the table. Cleaning old ones is done by an asynchronous process called vacuum (and autovacuum).
> 当行数据被更新时，会构建整行的一个新版本并将其写入（任何有空闲空间的地方）。旧版本之所以保留，是因为在更新时事务尚未完成，未来可能还会回滚。当事务完成后，表中就会出现同一行的两个或多个版本。清理旧版本的工作由一个称为清理（vacuum 和 autovacuum）的异步进程来完成。

---

## How Does the Vacuum Work?
## 清理（Vacuum）是如何工作的？

Vacuum goes through all table files looking for row versions that were updated or deleted by already completed transactions and frees the space on the pages.
> Vacuum 会遍历所有的表文件，寻找已被已完成事务所更新或删除的行版本，并释放页面上的空间。

Then it updates the table’s free-space-map to reflect that some page has a certain amount of free space for row inserts.
> 随后，它会更新表的空闲空间映射（free-space-map），以反映某些页面拥有特定数量的空闲空间，可用于插入新行。

It also updates the visibility map for a page. It marks that all remaining rows are visible. So index scans can skip visibility checks, which is not the case for the modified page before vacuuming. This significantly increases the speed of queries using indexes.
> 它还会更新页面的可见性映射（visibility map），标记出所有剩余的行都是可见的。因此，索引扫描可以跳过可见性检查（在 vacuum 之前，被修改的页面并非如此）。这显著提高了使用索引的查询速度。

In many cases, vacuum runs automatically, cleans everything, and requires little care. But in some scenarios, we need to go deeper and tune the autovacuum parameters or run the vacuum manually.
> 在许多情况下，vacuum 会自动运行，清理所有内容，几乎不需要人工干预。但在某些场景下，我们需要深入了解并调整 autovacuum 参数，或者手动运行 vacuum。

---

## Cleaning Relation Files
## 清理关系文件

Vacuum marks space in a relation file as free to use for future row inserts or updates. And it’s not a problem unless we insert many rows, delete many rows at once, and then don’t make any inserts or updates. Space remains reserved in a file but we don’t use it.
> Vacuum 会将关系文件中的空间标记为可供将来行插入或更新使用的空闲空间。这本身不是问题，除非我们插入了许多行、一次性删除了大量行，之后又没有任何插入或更新操作。此时，空间仍然在文件中被保留，但我们却没有使用它。

In this case, we could free actual filesystem space by running a more aggressive mode:
> 在这种情况下，我们可以通过运行更激进的模式来释放实际的文件系统空间：

```sql
VACUUM FULL mytable;
```

It will rebuild the table from live rows and they will be placed compactly so that filesystem space will be freed. The downside is that it needs an exclusive lock and you won’t be able to modify the table while `VACUUM FULL` does its work. It’s wise to execute that process when the database is least accessed, e.g., at night.
> 它将根据存活的行重建表，并使它们紧凑地排列，从而释放文件系统空间。缺点是它需要排他锁（exclusive lock），并且在 `VACUUM FULL` 工作期间你将无法修改该表。明智的做法是在数据库访问量最少的时候（例如夜间）执行此过程。

An alternative way that doesn’t need full locks is using the `pg_repack` extension:
> 另一种不需要完全锁的替代方法是使用 `pg_repack` 扩展：

```bash
pg_repack --table mytable test
```

`pg_repack` operates similarly to `VACUUM FULL` for the database `test` and table `mytable`.
> 对于数据库 `test` 和表 `mytable`，`pg_repack` 的运行方式与 `VACUUM FULL` 类似。

---

## Table Bloating and Autovacuum
## 表膨胀与自动清理（Autovacuum）

To see database bloat via the [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started) run:
> 要通过 [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started) 查看数据库膨胀情况，请运行：

```bash
$ supabase inspect db bloat
```

Or query the metrics directly:
> 或者直接查询指标：

```sql
-- Number of dead rows
-- 死元组数量
SELECT
	n_dead_tup
FROM
	pg_stat_user_tables
WHERE
	relname = 'mytable';

-- Number of live rows
-- 存活行数
SELECT
	count(*)
FROM
	mytable;
```

If the numbers differ by more than 2x, chances are that the autovacuum didn’t start or hasn’t completed for a table. There could be several legitimate reasons for this.
> 如果这两个数字相差超过 2 倍，那么该表的 autovacuum 很可能没有启动，或者尚未完成。这背后可能有几个合法的原由。

You can view information for the last successful autovacuum by running:
> 你可以通过运行以下命令查看最后一次成功执行 autovacuum 的信息：

```bash
$ supabase inspect db vacuum-stats
```

Or via SQL:
> 或者通过 SQL 查询：

```sql
SELECT
	last_vacuum,
	last_autovacuum
FROM
	pg_stat_user_tables
WHERE
	relname = 'mytable';
```

Let’s turn on autovacuum logging so that all autovacuum events land in the log:
> 让我们开启 autovacuum 日志记录，以便所有 autovacuum 事件都被记录到日志中：

```sql
ALTER TABLE mytable SET log_autovacuum_min_duration = 0;
```

There are two primary reasons you might encounter table bloat:
* Autovacuum hasn’t started.
* Autovacuum did start (possibly multiple times) but never succeeded.

> 你可能会遇到表膨胀的两个主要原因：
> * Autovacuum 尚未启动。
> * Autovacuum 已经启动（可能多次），但从未成功完成。

---

### Autovacuum Hasn’t Started for a Table
### 表的 Autovacuum 尚未启动

Autovacuum starts based on several configuration parameters like timeout and patterns of access to a particular table. Its execution depends on these thresholds:
> Autovacuum 的启动取决于若干配置参数（如超时时间）以及对特定表的访问模式。它的执行取决于以下阈值：

* `autovacuum_vacuum_threshold` — Number of rows updated or deleted in a table to invoke autovacuum.
* `autovacuum_vacuum_insert_threshold` — Number of rows inserted into a table to invoke autovacuum.
* `autovacuum_vacuum_scale_factor` — A fraction of the table modified by updates or deletes to invoke autovacuum.
* `autovacuum_vacuum_insert_scale_factor` — A fraction of the table modified by inserts to invoke autovacuum.

> * `autovacuum_vacuum_threshold` — 触发 autovacuum 所需的表中更新或删除的行数。
> * `autovacuum_vacuum_insert_threshold` — 触发 autovacuum 所需的表中插入的行数。
> * `autovacuum_vacuum_scale_factor` — 触发 autovacuum 所需的被更新或删除修改的表行数比例。
> * `autovacuum_vacuum_insert_scale_factor` — 触发 autovacuum 所需的被插入修改的表行数比例。

With all these parameters set, autovacuum will start if the number of rows updated or deleted exceeds:
> 在设置了所有这些参数后，如果更新或删除的行数超过以下公式计算的值，autovacuum 就会启动：

$$\text{autovacuum\_vacuum\_scale\_factor} \times \text{size\_of\_table} + \text{autovacuum\_vacuum\_threshold}$$

The same logic applies to inserts. Default scale factors are 20% of a table, which could be too high for big tables. If we want autovacuum to occur on large tables more frequently and take less time per run, decrease the default values for these tables, e.g.:
> 插入操作也遵循相同的逻辑。默认的比例因子是表的 20%，对于大表来说，这个值可能太高了。如果我们希望在大表上更频繁地触发 autovacuum 且每次运行耗时更短，可以减小这些表的默认值，例如：

```sql
ALTER TABLE mytable SET (autovacuum_vacuum_scale_factor = 0.05);
```

* `autovacuum_naptime` (default 1 min) — Every 1 minute, the autovacuum daemon checks the state of all tables in the database and decides whether to start autovacuum for a table. Most often, this parameter does not need to be modified.
> * `autovacuum_naptime`（默认 1 分钟）— 每隔 1 分钟，autovacuum 守护进程会检查数据库中所有表的状态，并决定是否为某个表启动 autovacuum。大多数情况下，不需要修改此参数。

To see global vacuum settings for your cluster, run:
> 要查看集群的全局 vacuum 设置，请运行：

```sql
SELECT * FROM pg_settings WHERE category LIKE 'Autovacuum';
```

To see current settings for a table (which override global settings), run:
> 要查看表的当前设置（它会覆盖全局设置），请运行：

```sql
SELECT relname, reloptions FROM pg_class WHERE relname = 'mytable';
```

---

### Autovacuum Started but Couldn’t Succeed
### Autovacuum 已启动但无法成功完成

The most common reason autovacuum doesn’t succeed is long-running open transactions that access old row versions. In that case, Postgres recognizes that the row versions are still needed, meaning any row versions created after that point cannot be marked as dead. One common cause is interactive sessions left open by accident. When tuples can’t be marked as dead, the database begins to bloat.
> autovacuum 无法成功的最常见原因是有访问旧行版本的长期运行的未提交事务。在这种情况下，Postgres 识别到这些行版本仍然被需要，这意味着在该时间点之后创建的任何行版本都不能被标记为死元组。一个常见的原因是交互式会话被意外保持打开状态。当元组无法被标记为死元组时，数据库便开始膨胀。

To see all open transactions, run:
> 要查看所有打开的事务，请运行：

```sql
SELECT xact_start, state FROM pg_stat_activity;
```

To close transactions found to be idling:
> 要关闭发现处于闲置状态的事务：

```sql
SELECT pg_cancel_backend(pid) FROM pg_stat_activity WHERE xact_start = '<value from previous query>';
```

For automatically closing idle transactions in a session:
> 若要自动关闭会话中处于闲置状态的事务：

```sql
SET idle_in_transaction_session_timeout TO '10000s';
```

This parameter can also be set per role or database as needed.
> 根据需要，也可以按角色或按数据库设置此参数。

Another, less likely, possibility is that autovacuum can’t succeed due to locks. If some of your processes take the `SHARE UPDATE EXCLUSIVE` lock (e.g., via an `ALTER TABLE` clause), this lock will prevent vacuum from processing a table. Lock conflicts in your ordinary transactions could cause `SHARE UPDATE EXCLUSIVE` to be held for a long time. A good recipe when this happens is to cancel all open transactions and run `VACUUM` for the table manually (or wait until the next autovacuum cycle):
> 另一种可能性（较小）是由于锁的原因导致 autovacuum 无法成功。如果你的某些进程获取了 `SHARE UPDATE EXCLUSIVE` 锁（例如通过 `ALTER TABLE` 子句），该锁将阻止 vacuum 处理表。常规事务中的锁冲突可能会导致 `SHARE UPDATE EXCLUSIVE` 被长时间持有。发生这种情况时的一个有效对策是取消所有打开的事务，并手动为该表运行 `VACUUM`（或者等待下一个 autovacuum 周期）：

```sql
SELECT pg_cancel_backend(pid) FROM pg_stat_activity WHERE state = 'active';
VACUUM mytable;
```

---

## Other Vacuum Optimizations
## 其他 Vacuum 优化措施

There could be too few autovacuum workers, or each worker could operate slowly due to a low `autovacuum_work_mem` setting.
> 可能是 autovacuum 工作进程（workers）太少，或者由于 `autovacuum_work_mem` 设置过低导致每个工作进程运行缓慢。

* `autovacuum_max_workers` (default 3) — Number of parallel workers performing autovacuum for tables. When you have enough CPU cores, increasing the default value is worthwhile. Note that this will decrease the number of available backends or regular parallel workers running at a time.
* `autovacuum_work_mem` (default equal to `maintenance_work_mem` or 64MB) — Work memory used per autovacuum worker. If logs indicate that autovacuum starts for tables but takes a long time, increasing this value can speed it up. This parameter can only be modified in the configuration file (`postgresql.conf`).

> * `autovacuum_max_workers`（默认 3）— 为表执行 autovacuum 的并行工作进程数量。当你拥有足够的 CPU 核心时，增加默认值是值得的。请注意，这会减少同时运行的可用后端进程或常规并行工作进程的数量。
> * `autovacuum_work_mem`（默认等于 `maintenance_work_mem` 或 64MB）— 每个 autovacuum 工作进程使用的内存。如果日志表明 autovacuum 在表上启动但耗时很长，增加该值可以加速其运行。此参数只能在配置文件（`postgresql.conf`）中进行修改。

---

## Conclusion
## 结论

Vacuum and autovacuum are efficient tools for maintaining tables without bloat, featuring several parameters that allow for granular tuning. Understanding how the database operates can help prevent issues where autovacuum becomes problematic and bloat increases, such as:
> Vacuum 和 autovacuum 是用于维护表免受膨胀影响的高效工具，它们具有多个允许进行精细调优的参数。了解数据库的运作方式有助于防止出现 autovacuum 发生故障和膨胀加剧的问题，例如：

* Long open transactions
* Stuck locks
* Insufficient resources allocated to vacuuming
* Space not freed at the filesystem level after massive table modifications

> * 长时间运行的未提交事务
> * 锁阻塞
> * 为清理分配的资源不足
> * 大规模修改表后，文件系统层面的空间未被释放

### Reference Links
### 参考链接

* [Full official documentation for vacuum](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-BASICS)
* [Per-table vacuum parameters](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS)
* [Global autovacuum parameters](https://www.postgresql.org/docs/current/runtime-config-autovacuum.html) *(most require modifying `postgresql.conf`, but can be overridden by per-table parameters)*
* [Supabase CLI reference](https://supabase.com/docs/reference/cli/global-flags)

> * [Vacuum 官方完整文档](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-BASICS)
> * [按表设置的 vacuum 参数](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS)
> * [全局 autovacuum 参数](https://www.postgresql.org/docs/current/runtime-config-autovacuum.html) *（大多数需要修改 `postgresql.conf`，但可以被表级参数覆盖）*
> * [Supabase CLI 参考](https://supabase.com/docs/reference/cli/global-flags)