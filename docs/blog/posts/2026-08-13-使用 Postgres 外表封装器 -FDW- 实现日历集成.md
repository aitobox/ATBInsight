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
- Supabase
- Cal.com
- FDW
- WebAssembly
title: 使用 Postgres 外表封装器 (FDW) 实现日历集成
---
### 文章背景与核心概要

Supabase 近期发布了针对 **Cal.com** 的外表封装器 (Foreign Data Wrapper, FDW)，使开发者能够在 PostgreSQL 数据库中直接查询、管理并创建日历预约，且所有操作均可在单一事务中完成。

该集成基于 Supabase 的 Wrappers 框架，利用 WebAssembly (Wasm) 技术，实现了数据库操作与日历调度系统的无缝同步。通过此方案，开发者可以将用户注册、订单处理等业务逻辑与日历预约流程直接关联，极大地简化了跨系统数据交互的复杂性。

---

## 什么是 Cal.com？

[Cal.com](https://cal.com/) 是一个开源的调度平台，专为个人和企业设计，用于预订和管理预约。从个人使用场景到企业级系统，它提供了一套强大的开发者工具包，用于嵌入和处理各种调度工作流。

> [Cal.com](https://cal.com/) is an open-source scheduling platform designed for individuals and businesses to book and manage appointments. Ranging from personal use cases to enterprise-grade systems, it provides a robust developer toolkit for embedding and handling scheduling workflows.

---

## 使用 Postgres 创建事件预约

开发者最常见的场景之一是自动创建新的日历事件（例如，在客户购买门票或注册服务之后）。使用 Supabase 和 Postgres 外表封装器，你可以轻松实现这一目标。

> One of the most common developer scenarios is automatically creating a new calendar event (for instance, after a customer purchases a ticket or registers for a service). Using Supabase and Postgres Foreign Data Wrappers, you can achieve this effortlessly.

### 1. 设置 Cal.com 账户
* 在 [Cal.com](https://cal.com/) 注册。
* 导航至 [Settings -> Developer -> API keys](https://app.cal.com/settings/developer/api-keys) 生成 API 密钥。

> * Sign up on [Cal.com](https://cal.com/).
> * Navigate to [Settings -> Developer -> API keys](https://app.cal.com/settings/developer/api-keys) to generate an API key.

### 2. 设置 Supabase 账户
* 在 [supabase.com](https://supabase.com) 注册。
* 创建一个新项目或打开现有项目。
* 前往 [Supabase Database Extensions Dashboard](https://supabase.com/dashboard/project/_/database/extensions) 启用 `wrappers` 扩展。

> * Sign up on [supabase.com](https://supabase.com).
> * Create a new project or open an existing one.
> * Go to the [Supabase Database Extensions Dashboard](https://supabase.com/dashboard/project/_/database/extensions) to enable the `wrappers` extension.

### 3. 创建 Wasm 封装器和外部服务器
打开 [Supabase SQL Editor](https://supabase.com/dashboard/project/_/sql/new) 并执行以下 SQL 来创建 Wasm 外表封装器：

> Open the [Supabase SQL Editor](https://supabase.com/dashboard/project/_/sql/new) and execute the following SQL to create the Wasm foreign data wrapper:

```sql
create foreign data wrapper wasm_wrapper
  handler wasm_fdw_handler
  validator wasm_fdw_validator;
```

接下来，使用你的 API 密钥为 Cal.com 连接创建一个外部服务器：

> Next, create a foreign server for your Cal.com connection using your API key:

```sql
create server cal_server
  foreign data wrapper wasm_wrapper
  options (
    fdw_package_url 'https://github.com/supabase/wrappers/releases/download/wasm_cal_fdw_v0.1.0/cal_fdw.wasm',
    fdw_package_name 'supabase:cal-fdw',
    fdw_package_version '0.1.0',
    fdw_package_checksum '4afe4fac8c51f2caa1de8483b3817d2cec3a14cd8a65a3942c8b4ff6c430f08a',
    api_key '<your Cal.com API key>'
  );
```

> **注意：** 请在官方文档 [fdw.dev/catalog/cal](https://fdw.dev/catalog/cal) 中查找最新的包版本和校验和。

> **Note:** Find the latest package version and checksum in the official documentation at [fdw.dev/catalog/cal](https://fdw.dev/catalog/cal).

### 4. 设置外表
为你的外表创建一个专用模式：

> Create a dedicated schema for your foreign tables:

```sql
create schema if not exists cal;
```

为 [Event Types](https://app.cal.com/event-types) 创建一个外表：

> Create a foreign table for [Event Types](https://app.cal.com/event-types):

```sql
create foreign table cal.event_types (
  attrs jsonb
)
  server cal_server
  options (
    object 'event-types'
  );
```

为 [Bookings](https://app.cal.com/bookings/upcoming) 创建另一个外表：

> Create another foreign table for [Bookings](https://app.cal.com/bookings/upcoming):

```sql
create foreign table cal.bookings (
  attrs jsonb
)
  server cal_server
  options (
    object 'bookings',
    rowid_column 'attrs'
  );
```

> **注意：** 如果你打算向 `cal.bookings` 表中插入数据，则必须使用 `rowid_column` 选项。

> **Note:** The `rowid_column` option is required if you intend to insert data into the `cal.bookings` table.

---

## 从 Cal.com 查询事件类型和预约
从 Cal.com API 返回的所有调度信息都存储在 JSON `attrs` 列中，这使你可以轻松提取特定字段。

> All scheduling information returned from the Cal.com API is stored inside the JSON `attrs` column, allowing you to easily extract specific fields.

### 提取事件类型
> ### Extract Event Types

```sql
-- extract event types
select
  etg->'profile'->>'name' as profile,
  et->>'id' as id,
  et->>'title' as title
from cal.event_types t
  cross join json_array_elements((attrs->'eventTypeGroups')::json) etg
  cross join json_array_elements((etg->'eventTypes')::json) et;
```

### 提取预约
> ### Extract Bookings

```sql
-- extract bookings
select
  bk->>'id' as id,
  bk->>'title' as title,
  bk->'responses'->>'name' as name,
  bk->>'startTime' as start_time
from cal.bookings t
  cross join json_array_elements((attrs->'bookings')::json) bk;
```

---

## 从 Supabase 在 Cal.com 上进行预约
要直接从 Postgres 进行预约，只需将记录插入到 `cal.bookings` 外表中，并将事件详情格式化为 JSON：

> To make a booking directly from Postgres, simply insert a record into the `cal.bookings` foreign table with the event details formatted as JSON:

```sql
-- make a 15 minutes meeting with Elon Musk
insert into cal.bookings(attrs)
values (
  '{
     "start": "2025-01-01T23:30:00.000Z",
     "eventTypeId": 1398027,
     "attendee": {
       "name": "Elon Musk",
       "email": "elon.musk@x.com",
       "timeZone": "America/New_York"
     }
  }'::jsonb
);
```

`eventTypeId`（本例中为 `1398027`）对应于你特定的事件类型 ID，你可以通过查询 `cal.event_types` 表找到它。一旦插入，预约将立即出现在你的 Cal.com 即将到来的列表中，并可在从 Postgres 查询 `cal.bookings` 时看到。

> The `eventTypeId` (`1398027` in this example) corresponds to your specific event type ID, which you can find by querying the `cal.event_types` table. Once inserted, the booking will immediately appear in your upcoming list on Cal.com and become visible when querying `cal.bookings` from Postgres.

---

## 基于 Wrappers 构建
Cal.com FDW 是使用 **Wrappers** 构建的，这是一个用于 PostgreSQL 外表封装器的开源框架。最新版本利用 [Wasm (WebAssembly)](https://webassembly.org/) 极大地简化了基于 API 的数据连接器的开发。

> The Cal.com FDW is built using **Wrappers**, an open-source framework for PostgreSQL Foreign Data Wrappers. The latest release leverages [Wasm (WebAssembly)](https://webassembly.org/) to drastically simplify the development of API-based data connectors.

## 探索更多
Supabase 在 [fdw.dev](https://fdw.dev/) 上提供了多种封装器，涵盖了从 [Stripe](https://stripe.com/) 和 [Notion](https://www.notion.com/) 等 SaaS 工具，到 [ClickHouse](https://clickhouse.com/) 和 [BigQuery](https://cloud.google.com/bigquery) 等数据库。

> Supabase offers a wide variety of wrappers on [fdw.dev](https://fdw.dev/), ranging from SaaS tools like [Stripe](https://stripe.com/) and [Notion](https://www.notion.com/) to databases like [ClickHouse](https://clickhouse.com/) and [BigQuery](https://cloud.google.com/bigquery). 

查看 [完整目录](https://fdw.dev/catalog/) 并在 [database.new](https://database.new) 上启动你的下一个数据库。

> Check out the [full catalog](https://fdw.dev/catalog/) and spin up your next database at [database.new](https://database.new).