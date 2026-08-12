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
- Apache Iceberg
- 数据库
- 分析存储
- SQL
title: Supabase 推出支持 Iceberg 的分析存储桶（Analytics Buckets）
---
### 文章背景与核心概要
本文介绍了 Supabase 正在私测阶段推出的全新功能——Supabase 分析存储桶（Analytics Buckets）。该解决方案专为大规模分析而优化，并内置了对 Apache Iceberg 开放表格式的支持。它通过直接集成到 Supabase Studio 中，并借助全新的 Supabase Iceberg Wrapper，让开发者能够通过标准 SQL 查询分析数据，同时确保完全的数据可移植性和对开放标准的合规性。

文章详细阐述了 Supabase 选择 Iceberg 的原因（如无底数据模型、快照与版本控制、架构演进及开放标准）、分析存储桶的架构区别、创建命名空间与表的具体代码示例、如何通过 SQL 查询分析数据，以及目前的 Alpha 阶段限制和未来路线图。

---

# Supabase Analytics Buckets with Iceberg Support

## Summary
Supabase is launching **Supabase Analytics Buckets** in private alpha—a new storage solution optimized for large-scale analytics with built-in support for the [Apache Iceberg](https://iceberg.apache.org/) open table format. Integrated directly into Supabase Studio and powered by the new **Supabase Iceberg Wrapper**, these buckets allow you to query analytical data via standard SQL while ensuring full data portability and open standards compliance.

> Supabase 正在私测阶段推出 **Supabase Analytics Buckets**——这是一种针对大规模分析进行优化的全新存储解决方案，内置了对 [Apache Iceberg](https://iceberg.apache.org/) 开放表格式的支持。通过直接集成到 Supabase Studio 并由全新的 **Supabase Iceberg Wrapper** 提供支持，这些存储桶允许您通过标准 SQL 查询分析数据，同时确保完全的数据可移植性和对开放标准的合规性。

---

## Why Iceberg?
[Apache Iceberg](https://iceberg.apache.org/) is a high-performance, open table format for large-scale analytics on object storage. It brings database-like features to the flexibility of flat files. 

Supabase chose Iceberg for several key reasons:
* **Bottomless Data Model:** Append-only and immutable history.
* **Snapshotting & Versioning:** Built-in time travel capabilities.
* **Schema Evolution:** Seamless adaptation to changing data structures.
* **Open Standards:** Prevents vendor lock-in, aligning with Supabase's commitment to [open standards and portability](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg).

> ## 为什么选择 Iceberg？
> [Apache Iceberg](https://iceberg.apache.org/) 是一种高性能的开放表格式，用于在对象存储上进行大规模分析。它将类似数据库的功能带给平面文件的灵活性。
> 
> Supabase 选择 Iceberg 的几个关键原因包括：
> * **无底数据模型（Bottomless Data Model）：** 仅追加（Append-only）且不可变的歷史记录。
> * **快照与版本控制（Snapshotting & Versioning）：** 内置时间旅行（Time Travel）功能。
> * **架构演进（Schema Evolution）：** 无缝适应不断变化的数据结构。
> * **开放标准（Open Standards）：** 防止供应商锁定，这符合 Supabase 对[开放标准和可移植性](https://supabase.com/blog/open-data-standards-postgres-otel-iceberg)的承诺。

---

## Setting up Analytics Buckets
Once your project is accepted into the private alpha, you can create an Analytics Bucket via Supabase Studio by navigating to `Storage > New bucket`.

### Key Differences & Storage Architecture
* Analytics buckets are entirely separate from standard Supabase Storage buckets; file types cannot be mixed between the two.
* They are stored in a new system table: `storage.buckets_iceberg` (isolated from `storage.buckets` and `storage.objects`).
* The `listBuckets()` endpoint returns a merged list of both standard and analytics buckets for UI and API consistency.

### Creating an Iceberg Namespace and Table
After creating the bucket, copy the `WAREHOUSE`, `VAULT_TOKEN`, and `CATALOG_URI` connection details. You can then use tools like `pyiceberg` to create your namespaces and tables:

```python
import datetime
import pyarrow as pa
from pyiceberg.catalog.rest import RestCatalog
from pyiceberg.exceptions import NamespaceAlreadyExistsError, TableAlreadyExistsError

# Define catalog connection details (replace variables)
WAREHOUSE = ...
VAULT_TOKEN = ...
CATALOG_URI = ...

# Connect to Supabase Data Catalog
catalog = RestCatalog(
    name="catalog",
    warehouse=WAREHOUSE,
    uri=CATALOG_URI,
    token=VAULT_TOKEN,
)

# Schema and Table Names
namespace_name = "market"
table_name = "prices"

# Create default namespace
catalog.create_namespace(namespace_name)

df = pa.table({
    "tenant_id": pa.array([], type=pa.string()),
    "store_id": pa.array([], type=pa.string()),
    "item_id": pa.array([], type=pa.string()),
    "price": pa.array([], type=pa.float64()),
    "timestamp": pa.array([], type=pa.int64()),
})

# Create an Iceberg table
table = catalog.create_table(
    (namespace_name, table_name),
    schema=df.schema,
)
```

Back in Supabase Studio, you will see your newly created namespace. Click **Connect** and select a **Target Schema** (it is recommended to use a standalone schema rather than `public` to prevent exposing your analytical tables over the project's REST API).

> ## 设置分析存储桶
> 一旦您的项目通过了私测申请，您就可以通过 Supabase Studio 导航至 `Storage > New bucket` 来创建分析存储桶。
> 
> ### 关键区别与存储架构
> * 分析存储桶与标准的 Supabase 存储桶完全隔离；两者之间不能混用文件类型。
> * 它们存储在新的系统表中：`storage.buckets_iceberg`（与 `storage.buckets` 和 `storage.objects` 隔离）。
> * `listBuckets()` 端点将返回标准存储桶和分析存储桶的合并列表，以保持 UI 和 API 的一致性。
> 
> ### 创建 Iceberg 命名空间与表
> 创建存储桶后，复制 `WAREHOUSE`、`VAULT_TOKEN` 和 `CATALOG_URI` 连接详细信息。然后，您可以使用诸如 `pyiceberg` 的工具来创建命名空间和表：
> 
> ```python
> import datetime
> import pyarrow as pa
> from pyiceberg.catalog.rest import RestCatalog
> from pyiceberg.exceptions import NamespaceAlreadyExistsError, TableAlreadyExistsError
> 
> # Define catalog connection details (replace variables)
> WAREHOUSE = ...
> VAULT_TOKEN = ...
> CATALOG_URI = ...
> 
> # Connect to Supabase Data Catalog
> catalog = RestCatalog(
>     name="catalog",
>     warehouse=WAREHOUSE,
>     uri=CATALOG_URI,
>     token=VAULT_TOKEN,
> )
> 
> # Schema and Table Names
> namespace_name = "market"
> table_name = "prices"
> 
> # Create default namespace
> catalog.create_namespace(namespace_name)
> 
> df = pa.table({
>     "tenant_id": pa.array([], type=pa.string()),
>     "store_id": pa.array([], type=pa.string()),
>     "item_id": pa.array([], type=pa.string()),
>     "price": pa.array([], type=pa.float64()),
>     "timestamp": pa.array([], type=pa.int64()),
> })
> 
> # Create an Iceberg table
> table = catalog.create_table(
>     (namespace_name, table_name),
>     schema=df.schema,
> )
> ```
> 
> 回到 Supabase Studio 中，您将看到刚刚创建的命名空间。点击 **Connect（连接）** 并选择一个 **Target Schema（目标 Schema）**（建议使用独立的 Schema 而不是 `public`，以防止通过项目的 REST API 暴露您的分析表）。

---

## Querying Analytics Buckets
Viewing an analytics bucket in Supabase Studio redirects you to the Table Editor, where a table explorer powered by the [Supabase Iceberg Wrapper](https://fdw.dev/catalog/) displays your data instead of raw Parquet files.

You can query your analytical data directly using SQL:

```sql
select
  *
from market_analytics.prices;
```

> ## 查询分析存储桶
> 在 Supabase Studio 中查看分析存储桶会将您重定向到表编辑器（Table Editor），在这里，由 [Supabase Iceberg Wrapper](https://fdw.dev/catalog/) 驱动的表浏览器将显示您的数据，而不是原始的 Parquet 文件。
> 
> 您可以直接使用 SQL 查询您的分析数据：
> 
> ```sql
> select
>   *
> from market_analytics.prices;
> ```

---

## Writing to Analytics Buckets
Writing data natively is currently a work in progress. For now, you can populate Analytics Buckets using your own ingestion pipelines or Iceberg-compatible tooling. 

Native write capabilities will be added to the Supabase Iceberg Wrapper as soon as write support lands in the upstream [iceberg-rust client library](https://github.com/apache/iceberg-rust), completing a seamless **write → store → query** workflow entirely inside Supabase.

> ## 写入分析存储桶
> 原生写入数据目前正在开发中。目前，您可以使用自己的摄取管道或与 Iceberg 兼容的工具来填充分析存储桶。
> 
> 一旦上游的 [iceberg-rust 客户端库](https://github.com/apache/iceberg-rust) 落地了写入支持，原生写入功能将立即添加到 Supabase Iceberg Wrapper 中，从而在 Supabase 内部完整实现无缝的 **写入 → 存储 → 查询** 工作流。

---

## Alpha Launch Limits
During the private alpha, Analytics Buckets are subject to the following constraints:
* Two analytics buckets per project
* Up to five namespaces per bucket
* Ten tables per namespace
* Pricing details will be announced in the coming weeks
* Standard objects cannot be stored in analytics buckets

> ## Alpha 发布限制
> 在私测（Alpha）阶段，分析存储桶受以下限制：
> * 每个项目两个分析存储桶
> * 每个存储桶最多五个命名空间
> * 每个命名空间最多十张表
> * 定价详情将在未来几周内公布
> * 标准对象不能存储在分析存储桶中

---

## Roadmap and What's Next
This launch is the first step toward robust analytical capabilities in Supabase. Upcoming milestones include:
* **SQL Catalog Support:** Explore Iceberg table metadata directly from the database.
* **Deeper Studio Integration:** Enhanced schema inspection, column-level filtering, and time-travel query tools.
* **HTAP Backend Realization:** A fully unified environment to write, store, and query analytical data seamlessly.

> ## 路线图与下一步计划
> 此次发布是 Supabase 迈向强大分析能力的第一步。接下来的里程碑包括：
> * **SQL Catalog 支持：** 直接从数据库中探索 Iceberg 表元数据。
> * **更深度的 Studio 集成：** 增强的 Schema 检查、列级过滤和时间旅行查询工具。
> * **HTAP 后端实现：** 一个完全统一的环境，用于无缝地写入、存储和查询分析数据。

---

## Try It Out
[Join the waitlist here](https://forms.supabase.com/analytics-buckets) to secure early access and start working with bottomless, time-travel-capable analytics data inside Supabase.

> ## 立即试用
> [在此处加入候补名单](https://forms.supabase.com/analytics-buckets)，以获得早期访问权限，并开始在 Supabase 内部使用无底的、具备时间旅行能力的分析数据。