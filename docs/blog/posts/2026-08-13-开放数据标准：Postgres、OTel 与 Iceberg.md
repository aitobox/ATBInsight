---
authors:
- aitoboxrobot
categories:
- 商业动态
date: 2026-08-13
hide:
- navigation
tags:
- Postgres
- OpenTelemetry
- Apache Iceberg
- 对象存储
- 架构设计
title: 开放数据标准：Postgres、OTel 与 Iceberg
---
### 文章背景与核心概要
随着数据技术生态的不断演进，三大开放标准正逐渐崭露头角，分别应对数据生命周期的核心阶段：用于联机事务处理（OLTP）的 **Postgres**、用于可观测性的 **OpenTelemetry (OTel)**，以及用于联机分析处理（OLAP）的 **Apache Iceberg**。

凭借卓越的可扩展性和开源治理模式，Postgres 已经取得了广泛的主导地位，而 OTel 和 Iceberg 正在沿着完全相同的蓝图发展。在厂商中立性和严格的开源原则支持下，这些标准越来越多地将 **AWS S3（及对象存储）** 作为其底层基础设施。通过优先考虑数据可移植性和互操作性，这些标准消除了厂商锁定，迫使企业在产品体验上展开纯粹的竞争。

---

## 开源的三大信条
## The Three Tenets of Open Source

开发者通常通过三个关键维度来评估任何项目的“开源程度”：

> Developers typically assess the "open sourceness" of any project through three critical dimensions:

1. **许可证：** 该许可证是否经过 [OSI 批准](https://opensource.org/licenses)？
2. **自托管：** 自托管*整个产品*的可行性有多高？
3. **商业化：** 该项目是否没有商业掣肘且保持厂商中立？或者——更好的是——受到*多家*相互竞争的商业实体的支持？

> 1. **License:** Is the license [OSI-approved](https://opensource.org/licenses)?
> 2. **Self-Hosting:** How feasible is it to self-host the *entire product*?
> 3. **Commercialization:** Is the project commercially unencumbered and vendor-neutral, or—even better—backed by *many* competing commercial entities?

Postgres 的成功不仅因为它是一款优秀的产品，更因为它不归属于任何单一实体。其治理模式很像国际空间站——一个由多个商业巨头共同推动的协作成果，正是因为没有任何人单独拥有它。

> Postgres succeeded not just because it is a great product, but because it cannot be owned by any single entity. Its governance model acts much like the International Space Station—a collaborative achievement driven by multiple commercial giants precisely because no one owns it.

---

## 三类数据用户画像
## The Three Data Personas

数据领域通常服务于三类主要用户画像，其工具链随着数据生命周期不断扩展（`1 → 2 → 3`）：

> The data space generally serves three primary personas, with tools scaling alongside the data lifecycle (`1 → 2 → 3`):

1. **OLTP 数据库：** 由*开发者*用于构建应用程序。
2. **遥测技术：** 由 *SRE* 用于管理基础设施并优化应用程序。
3. **OLAP / 数据仓库：** 由*数据工程师和科学人员*用于提取洞察。

> 1. **OLTP Databases:** Used by *developers* to build applications.
> 2. **Telemetry:** Used by *SREs* to manage infrastructure and optimize applications.
> 3. **OLAP / Warehousing:** Used by *data engineers and scientists* to draw insights.

随着现代数据库变得更具可扩展性，行业仍在继续“左移”（Shift Left），赋能开发者和初创公司在无需专门团队的情况下，更早地处理可观测性和数据仓库业务。

> As modern databases become more scalable, the industry continues to "shift left," empowering developers and startups to handle observability and data warehousing much earlier without needing specialized teams.

---

## 三大开放数据标准
## The Three Open Data Standards

围绕这些主要用例，三大开放数据标准正在涌现，这映射了标准（如 HTML）与工具（如浏览器）之间的动态关系：

> Around these primary use cases, three open data standards are emerging, mirroring the dynamic between standards (like HTML) and tools (like browsers):

* **OLTP：** Postgres
* **遥测（Telemetry）：** OpenTelemetry (OTel)
* **OLAP：** Iceberg

> * **OLTP:** Postgres
> * **Telemetry:** OpenTelemetry (OTel)
> * **OLAP:** Iceberg

这为科技行业创造了一种强大的颠覆性动态：如果商业实体拒绝采用开放标准，它们就会错过庞大的市场趋势；如果它们选择采用，则会降低厂商锁定效应。归根结底，**可移植性迫使企业在体验上展开竞争**。

> This creates a powerful disruptive dynamic for the tech industry: if commercial entities refuse to adopt open standards, they miss out on massive market trends; if they do adopt them, they reduce vendor lock-in. Ultimately, **portability forces companies to compete on experience**.

### 1. Postgres 是开放的 OLTP 标准
### 1. Postgres is the open OLTP standard

虽然 Postgres 本质上是一个工具，但它实际上已经成为了一个标准。几乎每个现代数据库都以[与 Postgres 线协议兼容](https://www.postgresql.org/docs/current/protocol.html)为目标。由于它采用宽松的许可证（功能上等同于 MIT）且不属于任何单一公司，因此每个主流云厂商——甚至包括甲骨文云（Oracle Cloud）——都被迫对其提供支持。如果遭遇厂商锁定，用户可以轻松通过 `pg_dump` 导出数据并迁移服务商。

> While Postgres is fundamentally a tool, it has effectively become a standard. Nearly every modern database aims for [Postgres wire compatibility](https://www.postgresql.org/docs/current/protocol.html). Because it uses a permissive license (functionally equivalent to MIT) and isn't owned by a single corporation, every major cloud provider—and even Oracle Cloud—is forced to support it. Users can easily `pg_dump` their data and migrate providers if they experience vendor lock-in.

### 2. OTel 是开放的遥测标准
### 2. OTel is the open telemetry standard

[OpenTelemetry (OTel)](https://opentelemetry.io/) 采用 Apache 2.0 许可证且完全厂商中立。各大遥测平台——包括 [Datadog](https://docs.datadoghq.com/integrations/otel/)、[Honeycomb](https://docs.honeycomb.io/send-data/opentelemetry/)、[Grafana Labs](https://grafana.com/grafana/dashboards/15983-opentelemetry-collector/) 以及 [Elastic](https://www.elastic.co/docs/solutions/observability/apm/use-opentelemetry-with-apm)——都在积极采用 OTel。对于自托管，开发者则依赖于诸如 [SigNoz](https://github.com/SigNoz/signoz)、[OpenObserve](https://github.com/openobserve/openobserve) 以及核心的 [OTel Collector](https://github.com/open-telemetry/opentelemetry-collector) 等开源解决方案。

> [OpenTelemetry (OTel)](https://opentelemetry.io/) is Apache 2.0-licensed and completely vendor-neutral. Major telemetry platforms—including [Datadog](https://docs.datadoghq.com/integrations/otel/), [Honeycomb](https://docs.honeycomb.io/send-data/opentelemetry/), [Grafana Labs](https://grafana.com/grafana/dashboards/15983-opentelemetry-collector/), and [Elastic](https://www.elastic.co/docs/solutions/observability/apm/use-opentelemetry-with-apm)—are actively adopting OTel. For self-hosting, developers rely on open-source solutions like [SigNoz](https://github.com/SigNoz/signoz), [OpenObserve](https://github.com/openobserve/openobserve), and the core [OTel Collector](https://github.com/open-telemetry/opentelemetry-collector).

### 3. Iceberg 是开放的 OLAP 标准
### 3. Iceberg is the open OLAP standard

[开放表格式（Open Table Formats）](https://www.startdataengineering.com/post/what_why_table_format/)为组织海量分析数据集提供了一种公认的格式，允许任何工具对其进行无缝查询。尽管存在 [DeltaLake](https://delta.io/) 和 [Hudi](https://hudi.apache.org/) 等替代方案，但 [Apache Iceberg](https://iceberg.apache.org/) 已成为无可争议的领导者。

> [Open Table Formats](https://www.startdataengineering.com/post/what_why_table_format/) provide an agreed-upon format for organizing massive analytical datasets, allowing any tool to query them seamlessly. While alternatives like [DeltaLake](https://delta.io/) and [Hudi](https://hudi.apache.org/) exist, [Apache Iceberg](https://iceberg.apache.org/) has emerged as the clear leader. 

主流数据仓库如 [Databricks](https://docs.databricks.com/aws/en/delta/uniform)、[Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg) 和 [ClickHouse](https://clickhouse.com/docs/engines/table-engines/integrations/iceberg) 都已拥抱 Iceberg。至关重要的是，AWS 随着 [S3 Tables](https://aws.amazon.com/blogs/aws/new-amazon-s3-tables-storage-optimized-for-analytics-workloads/) 的推出巩固了这一标准，使得直接在 S3 中使用 Iceberg 格式存储分析数据变得轻而易举。

> Major data warehouses like [Databricks](https://docs.databricks.com/aws/en/delta/uniform), [Snowflake](https://docs.snowflake.com/en/user-guide/tables-iceberg), and [ClickHouse](https://clickhouse.com/docs/engines/table-engines/integrations/iceberg) have all embraced Iceberg. Crucially, AWS cemented this standard with the launch of [S3 Tables](https://aws.amazon.com/blogs/aws/new-amazon-s3-tables-storage-optimized-for-analytics-workloads/), making it trivial to store analytics data natively in S3 using the Iceberg format.

---

## S3 是终极的数据基础设施
## S3 is the Ultimate Data Infrastructure

对象存储的成本已经变得如此低廉，以至于它现在成为了所有三个开放数据标准的底层基石。AWS 不断推出加速“S3 作为数据库”的功能，包括[条件写入（Conditional Writes）](https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-s3-conditional-writes/)和 [S3 Express One Zone](https://aws.amazon.com/blogs/aws/new-amazon-s3-express-one-zone-high-performance-storage-class/)（它以极低的成本提供极致的性能）。

> Object storage has become so affordable that it now serves as the foundational substrate for all three open data standards. AWS continues to roll out features that accelerate "S3 as a database," including [Conditional Writes](https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-s3-conditional-writes/) and [S3 Express One Zone](https://aws.amazon.com/blogs/aws/new-amazon-s3-express-one-zone-high-performance-storage-class/), which offers extreme performance at significantly reduced costs.

S3 的互操作性因用例而异：
* **对于 OLTP 数据库：** 性能需求意味着专用的“磁盘”层（NVMe SSD）仍然是必需的。然而，S3 的互操作性使得 ZeroETL 和分层存储（Tiered Storage）成为可能，从而卸载“冷”数据。Postgres 通过诸如 [`pg_mooncake`](https://github.com/Mooncake-Labs/pg_mooncake)、[`pg_duckdb`](https://github.com/duckdb/pg_duckdb) 和 [Iceberg 外部数据包装器（FDW）](https://github.com/supabase/wrappers/pull/462) 等扩展实现了这一点。
* **对于遥测和数据仓库：** 随着 S3 成本的下降，企业在存算分离（Decoupled Storage-and-Compute）架构中存储了呈指数级增长的数据。这推动了诸如 [DuckDB](https://duckdb.org/2021/10/29/duckdb-wasm.html)、云端托管 [SQLite](https://sqlite.org/cloudsqlite/doc/trunk/www/index.wiki)、[turbopuffer](https://turbopuffer.com/)、[SlateDB](https://slatedb.io/) 和 [Tonbo](https://tonbo.io/) 等嵌入式计算层数据库的激增。

> Interoperability with S3 varies by use case:
> * **For OLTP Databases:** Performance requirements mean a dedicated "disk" layer (NVMe SSDs) remains necessary. However, S3 interoperability enables ZeroETL and Tiered Storage to offload "cold" data. Postgres achieves this via extensions like [`pg_mooncake`](https://github.com/Mooncake-Labs/pg_mooncake), [`pg_duckdb`](https://github.com/duckdb/pg_duckdb), and [Iceberg Foreign Data Wrappers](https://github.com/supabase/wrappers/pull/462).
> * **For Telemetry and Warehousing:** As S3 costs drop, businesses store exponentially more data in decoupled storage-and-compute architectures. This has driven a surge in embedded compute-layer databases like [DuckDB](https://duckdb.org/2021/10/29/duckdb-wasm.html), cloud-backed [SQLite](https://sqlite.org/cloudsqlite/doc/trunk/www/index.wiki), [turbopuffer](https://turbopuffer.com/), [SlateDB](https://slatedb.io/), and [Tonbo](https://tonbo.io/).

---

## Supabase 的数据实践
## Data at Supabase

Supabase 广为人知的是一个 Postgres 平台，多年来一直致力于为开发者构建无缝的数据库体验。然而，Supabase 的愿景不仅局限于数据库，而是涵盖了更广阔的数据生命周期。这包括：

> Supabase is widely recognized as a Postgres platform, having spent years building a seamless database experience for developers. However, Supabase's vision extends beyond just a database to encompass the broader data lifecycle. This includes:

* 将 OTel 集成到所有维护的开源工具中。
* 为 [Supabase Storage](https://supabase.com/storage) 添加原生的 Iceberg 支持。
* 探索托管途径，在保持开放格式和操作隔离的同时，将 Postgres 数据无缝流式传输到分析系统中。
* 通过扩展和 FDW 直接在 Postgres 中实现强大的 Iceberg 读/写能力。

> * Integrating OTel into all maintained open-source tools.
> * Adding native Iceberg support to [Supabase Storage](https://supabase.com/storage).
> * Exploring managed pathways to seamlessly stream Postgres data into analytical systems while preserving open formats and operational isolation.
> * Implementing robust Iceberg read/write capabilities directly within Postgres via extensions and FDWs.

归根结底，Supabase 的未来与三大开放标准——**Postgres、OTel 和 Iceberg** 紧密相连。

> Ultimately, Supabase's future is firmly aligned with the three Open Data Standards: **Postgres, OTel, and Iceberg**.