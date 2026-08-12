---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-13
hide:
- navigation
tags:
- Postgres
- Supabase Wrappers
- Rust
- FDW
- 异步流式传输
title: 为 Postgres 外部数据包装器（FDW）添加异步流式传输支持
---
### 文章背景与核心概要
传统的 Postgres 外部数据包装器（FDW）长期受限于同步、基于拉取（pull-based）的模型，往往需要获取完整的结果集或固定大小的批处理数据，这会导致巨大的内存压力以及后端进程的空闲等待。通过 **Supabase Wrappers**，一套用 Rust 构建的全新异步流式架构成功在 Postgres 与现代分析型数据库（如 ClickHouse、BigQuery、Snowflake）之间架起了桥梁。

通过将 I/O 操作卸载至异步运行时，并让数据行通过有界且限流的通道（channel）进行传递，Wrappers 在遵循 Postgres 同步执行模型的同时，实现了可预测的受控内存占用以及显著更快的首条结果返回速度。本文深入探讨了这一架构的设计理念、底层实现方式及其对现代开发者构建高效数据管道的重要意义。

---

## 传统 FDW 的工作原理

大多数 FDW（包括 `postgres_fdw` 和 `mysql_fdw`）均运行在**同步、基于拉取的模型**下：

1. 在远程数据源上执行查询。
2. **一次性获取所有**行或通过**固定大小的批次**（例如使用游标）获取行。
3. 在等待每个批次到达时阻塞 Postgres 后端。
4. 在继续之前，将获取到的行转换为 Postgres 元组。

> Most FDWs, including `postgres_fdw` and `mysql_fdw`, operate in a **synchronous, pull-based model**:
> 
> 1. Execute a query on the remote source.
> 2. Fetch rows either **all at once** or in **fixed-size batches** (e.g., using cursors).
> 3. Block the Postgres backend while waiting for each batch to arrive.
> 4. Convert the fetched rows into Postgres tuples before continuing.

虽然分批获取避免了一开始将所有数据加载到内存中，但在 I/O 期间 Postgres 仍然处于阻塞状态，并且在每个批次完全接收并处理完毕之前，执行器无法继续运行。对于针对 ClickHouse 等旨在扫描数十亿行系统的分析型工作负载而言，这会导致：

* **高内存压力** — 尤其是在批处理大小较大或无边界的情况下。
* **糟糕的交互性** — 用户必须等待第一个批次返回后才能看到第一行数据。
* **低效的资源利用率** — 后端在网络等待期间处于空闲状态。

简而言之，传统的 FDW 是专为**批处理式集成**而设计的，而不是**流式数据管道**。它们缺乏真正的非阻塞 I/O，并且在远程数据开始流动之前无法开始返回结果——即便开始流动后，它们也会在批次之间停顿。

> While batched fetching avoids loading all data into memory upfront, Postgres still blocks during I/O, and the executor can’t proceed until each batch is fully received and processed. For analytical workloads against systems like ClickHouse, designed to scan billions of rows, this leads to:
> 
> * **High memory pressure** — especially if batch sizes are large or unbounded.
> * **Poor interactivity** — users wait for the first row until the first batch returns.
> * **Inefficient resource usage** — the backend is idle during network waits.
> 
> In short, traditional FDWs were designed for **batch-oriented integration**, not **streaming data pipelines**. They lack true non-blocking I/O and can’t start returning results until remote data begins flowing—and even then, they stall between batches.

---

## 我们构建的成果：Rust 中的异步流式传输

我们最新版本的 ClickHouse FDW 引入了**异步流式传输（asynchronous streaming）**，即使面对海量结果集，也能实现高效、内存安全的查询。

运作方式如下：

1. 后台异步任务随着数据通过网络到达，从 ClickHouse 增量获取数据行。
2. 这些行通过一个**有界、限容的通道**（默认容量：1024 行）传递给 Postgres 后端。
3. FDW 逐个消费该通道中的数据行，将其转换为 Postgres 的格式并发出，**而无需在内存中完整缓冲整个结果集**。

> The latest version of our ClickHouse FDW introduces **asynchronous streaming**, enabling efficient, memory-safe queries, even over massive result sets.
> 
> Here’s how it works:
> 
> 1. A background async task fetches rows from ClickHouse incrementally, as they arrive over the network.
> 2. These rows are passed to the Postgres backend through a **bounded, size-limited channel** (default capacity: 1024 rows).
> 3. The FDW consumes rows from this channel one at a time, converting and emitting them to Postgres **without buffering the full result set in memory**.

这意味着只要第一批数据可用，Postgres 就可以开始返回结果，从而大大降低内存压力并提高查询响应速度，即使对于海量的分析工作负载也是如此。

通过将 Rust 的内存安全性和异步运行时功能与 Postgres 的 FDW 接口相结合，Wrappers 在尊重 Postgres 同步执行模型的同时，实现了真正的流式传输语义。

> This means Postgres can start returning results **as soon as the first rows are available**, dramatically reducing memory pressure and improving query responsiveness, even for massive analytical workloads.
> 
> By combining Rust’s memory safety and async runtime capabilities with Postgres’s FDW interface, Wrappers delivers true streaming semantics while respecting Postgres’s synchronous execution model.

---

## 为什么它在 Postgres 生态系统中独一无二

这种流式传输能力不仅仅是 ClickHouse 的专属功能；它是内置于 Wrappers 中的可复用模式的首个实现。

与在 Postgres 同步模型中运行的传统 C 语言 FDW 不同——它们通常会加载完整的结果集或在批量获取期间阻塞——Wrappers 允许 FDW 从远程源增量流式传输数据。通过将 I/O 卸载到 Rust 的异步运行时，并通过有界通道向 Postgres 提供数据，它带来了：

* 可预测、有界的内存使用量 —— 即使对于十亿行级别的扫描。
* 更快的首个结果返回时间。
* 跨 BigQuery、Snowflake、S3 和 REST API 等各种后端的一致性能。

借助 Wrappers，FDW 可以安全、高效地将 Postgres 连接到现代数据栈，而不会牺牲稳定性或可扩展性。

> This streaming capability isn’t just a ClickHouse feature; it’s the first implementation of a reusable pattern built into Wrappers.
> 
> Unlike traditional C-based FDWs that operate within Postgres’s synchronous model—often loading full result sets or blocking during batched fetches—Wrappers enables FDWs to stream data incrementally from remote sources. By offloading I/O to Rust’s async runtime and feeding rows to Postgres through a bounded channel, it delivers:
> 
> * Predictable, bounded memory usage—even for billion-row scans.
> * Faster time-to-first-result.
> * Consistent performance across diverse backends like BigQuery, Snowflake, S3, and REST APIs.
> 
> With Wrappers, FDWs can safely and efficiently bridge Postgres to the modern data stack without compromising stability or scalability.

---

## 工作原理

以往，FDW 会预先获取整个结果集或固定的批次：

```rust
// Old approach: load all rows into memory
let rows = client.query(query).fetch_all()?;
for row in rows {
    writer.write_row(row)?;
}
```

现在，数据通过异步任务和有界通道进行增量流式传输：

```rust
// New approach: stream rows with bounded buffering
let (sender, receiver) = bounded_channel(1024);

spawn_async_task(async move {
    let mut stream = client.query(query).stream().await?;
    while let Some(row) = stream.next().await {
        let _ = sender.send(row).await;
    }
});

// Postgres consumes rows as they arrive
while let Some(row) = receiver.blocking_recv() {
    writer.write_row(row)?;
}
```

> **注意：** 这是简化的伪代码。实际实现使用了 Wrappers 的内部异步运行时和错误处理机制。

> Previously, the FDW fetched the entire result set or fixed batches upfront:
> 
> ```rust
> // Old approach: load all rows into memory
> let rows = client.query(query).fetch_all()?;
> for row in rows {
>     writer.write_row(row)?;
> }
> ```
> 
> Now, data is streamed incrementally using an async task and a bounded channel:
> 
> ```rust
> // New approach: stream rows with bounded buffering
> let (sender, receiver) = bounded_channel(1024);
> 
> spawn_async_task(async move {
>     let mut stream = client.query(query).stream().await?;
>     while let Some(row) = stream.next().await {
>         let _ = sender.send(row).await;
>     }
> });
> 
> // Postgres consumes rows as they arrive
> while let Some(row) = receiver.blocking_recv() {
>     writer.write_row(row)?;
> }
> ```
> 
> > **Note:** This is simplified pseudocode. The actual implementation uses Wrappers’ internal async runtime and error handling.

FDW 会生成一个异步任务，随着远程源的数据可用，将其拉取并发送到**大小受限的通道**中。然后，主要的 Postgres 后端**以同步但增量的方式**从该通道读取数据，确保内存使用保持在有界范围内，并且能够快速到达第一批结果——即使对于海量扫描也是如此。

这种混合模型尊重了 Postgres 的同步执行模型，同时通过 Rust 的异步功能解锁了高效的流式数据访问。

> The FDW spawns an async task that pulls rows from the remote source as they become available and sends them through a **size-limited channel**. The main Postgres backend then reads from this channel **synchronously but incrementally**, ensuring memory usage stays bounded and the first results arrive quickly—even for massive scans.
> 
> This hybrid model respects Postgres’s synchronous execution model while unlocking efficient, streaming data access through Rust’s async capabilities.

---

## 这对开发者意味着什么

如果您正在使用 Supabase Wrappers 进行开发，您可以：

* 创建能够流式传输海量结果集且具有有界内存的 FDW。
* 安全地将 Postgres 连接到分析系统（如 ClickHouse、BigQuery、Snowflake）、云存储（S3）以及各种 API（Stripe、Airtable、Notion 等）。
* 利用 Rust 的异步生态系统构建快速、安全且可维护的集成——无需编写 C 语言或进行手动内存管理。

这种流式传输模式将 FDW 转变为真正的数据管道组件，让 Postgres 能够参与到现代分析工作流中——同时将所有操作保持在 SQL 语法之内。

> If you’re building with Supabase Wrappers, you can:
> 
> * Create FDWs that stream massive result sets with bounded memory.
> * Safely connect Postgres to analytical systems (like ClickHouse, BigQuery, Snowflake), cloud storage (S3), and APIs (Stripe, Airtable, Notion, and more).
> * Leverage Rust’s async ecosystem to build fast, safe, and maintainable integrations—without writing C or manual memory management.
> 
> This streaming pattern turns FDWs into true data pipeline components, letting Postgres participate in modern analytics workflows—while keeping everything in SQL.

---

## 下一步计划

我们正将异步流式传输逐步推广到整个 Wrappers 生态系统中。针对 BigQuery、Snowflake、S3、Stripe 等连接器将采用相同的流式传输架构——使 Postgres 能够大规模查询远程数据源，并具备低延迟和受控的内存消耗。

通过 Wrappers，Postgres 成为真正通用的数据网关：一个连接分析型数仓、云存储、SaaS API 和实时数据库的单一 SQL 接口。现在，借助异步流式传输，即使数据量达到数十亿行，它也能高效完成任务。

* **探索 Wrappers：** [github.com/supabase/wrappers](https://github.com/supabase/wrappers)
* **构建您自己的 FDW：** [fdw.dev](https://fdw.dev/)

> We’re rolling out async streaming across the Wrappers ecosystem. Connectors for BigQuery, Snowflake, S3, Stripe, and more will adopt the same streaming architecture—enabling Postgres to query remote data sources at scale, with low latency and bounded memory usage.
> 
> With Wrappers, Postgres becomes a true universal data gateway: one SQL interface to analytical warehouses, cloud storage, SaaS APIs, and real-time databases. And now, thanks to async streaming, it can do it efficiently—even when the data runs into billions of rows.
> 
> * **Explore Wrappers:** [github.com/supabase/wrappers](https://github.com/supabase/wrappers)
> * **Build your own FDW:** [fdw.dev](https://fdw.dev/)