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
- 数据库设计
- 范围类型
- SQL优化
title: 使用范围列（Range Columns）简化基于时间的查询
---
### 文章背景与核心概要

在开发预订系统或日历应用时，管理事件的开始与结束时间是核心需求。传统方案通常使用两个独立的列（`start_at` 和 `end_at`）来存储时间段，这种做法不仅会导致查询逻辑冗长且易出错，还难以在数据库层面强制执行防重叠约束。

本文介绍了 PostgreSQL 的“范围类型”（Range Types）功能，它允许将时间跨度视为单个数据点（如 `tstzrange`）。通过使用内置的重叠运算符（`&&`）和排除约束（Exclusion Constraints），开发者可以显著简化查询逻辑，并从数据库底层确保数据的一致性与完整性，从而构建出更加健壮的调度系统。

---

## 传统日期列存在的问题

传统上，开发者使用两个独立的列来表示时间段：

> Traditionally, developers represent periods using two independent columns:
>
> ```sql
> create table reservations (
>   id serial primary key,
>   title text,
>   start_at timestamptz,
>   end_at timestamptz
> );
> ```

虽然这种方法可行，但存在两个主要缺点：
1. **查询复杂性：** 查找重叠事件或在特定时间范围内受限的事件，需要编写冗长且容易出错的条件逻辑。
2. **数据完整性：** 在数据库层面防止重复预订或重叠预订非常困难。

> While functional, this approach presents two major drawbacks:
> 1. **Querying Complexity:** Finding overlapping events or events constrained within a specific timeframe requires verbose and error-prone conditional logic.
> 2. **Data Integrity:** Preventing double-bookings or overlapping reservations is difficult to guarantee at the database level.

---

## 引入范围类型

Postgres 范围类型将范围的开始和结束存储在单个列中。
* 基类型 `int4` $\rightarrow$ `int4range`
* 基类型 `timestamptz` $\rightarrow$ `tstzrange`
* 基类型 `date` $\rightarrow$ `daterange`

范围使用方括号 `[]`（包含）或圆括号 `()`（不包含）来表示边界。例如，`int4range` 的 `[2,5)` 表示从 2（包含）到 5（不包含）的整数，即：**2、3 和 4**。

> Postgres range types store the beginning and end of a range within a single column. 
> * Base type `int4` $\rightarrow$ `int4range`
> * Base type `timestamptz` $\rightarrow$ `tstzrange`
> * Base type `date` $\rightarrow$ `daterange`
>
> Ranges use boundaries denoted by brackets `[]` (inclusive) or parentheses `()` (exclusive). For example, an `int4range` of `[2,5)` represents integers starting at 2 (inclusive) up to 5 (exclusive)—namely: **2, 3, and 4**.

### 查询范围列

重构我们的架构以使用范围列（`duration`）：

> Refactoring our schema to use a range column (`duration`):
>
> ```sql
> create table reservations (
>   id serial primary key,
>   title text,
>   duration tstzrange
> );
> ```

使用 `tstzrange`，我们可以使用重叠运算符（`&&`）无缝查询重叠条目：

> Using `tstzrange`, we can seamlessly query for overlapping entries using the overlap operator (`&&`):
>
> ```sql
> select *
> from reservations
> where duration && '[2024-07-04 16:00, 2024-07-04 19:00)';
> ```

* **匹配：** 跨度为 `[2024-07-04 18:00, 2024-07-04 21:00)` 的预订（重叠）。
* **不匹配：** 跨度为 `[2024-07-04 20:00, 2024-07-04 22:00)` 的预订（无重叠）。

> * **Matches:** A reservation spanning `[2024-07-04 18:00, 2024-07-04 21:00)` (overlaps).
> * **Does not match:** A reservation spanning `[2024-07-04 20:00, 2024-07-04 22:00)` (no overlap).

*（有关更多运算符，请查阅官方 [PostgreSQL 范围函数文档](https://www.postgresql.org/docs/9.3/functions-range.html)。）*

> *(For more operators, consult the official [PostgreSQL Range Functions Documentation](https://www.postgresql.org/docs/9.3/functions-range.html).)*

---

## 在范围列上添加约束

### 1. 全局重叠预防
为了确保表中没有任何预订在全局范围内重叠，我们可以添加一个排除约束：

> ### 1. Global Overlap Prevention
> To ensure *no* reservations overlap globally across the table, we can add an exclusion constraint:
>
> ```sql
> alter table reservations
> 	add constraint exclude_duration exclude
> 	using gist (duration with &&)
> ```

现在，尝试插入重叠的预订将导致数据库错误：

> Attempting to insert an overlapping reservation will now result in a database error:
>
> ```sql
> -- Add a first reservation (Succeeds)
> insert into reservations (title, duration)
> values ('Tyler Dinner', '[2024-07-04 18:00, 2024-07-04 21:00)');
>
> -- The following insert fails because the duration overlaps
> insert into reservations (title, duration)
> values ('Thor Dinner', '[2024-07-04 20:00, 2024-07-04 22:00)');
> ```

### 2. 多资源重叠预防（特定表）
在现实世界中，一家餐厅有多张桌子。预订一张桌子不应阻塞整个餐厅。我们可以通过外键标识符（`table_id`）和范围一起使用，将排除约束的作用范围限定在特定资源上。

首先，更新架构并确保启用了 [`btree_gist`](https://www.postgresql.org/docs/current/btree-gist.html) 扩展：

> ### 2. Multi-Resource Overlap Prevention (Table-Specific)
> In the real world, a single restaurant has multiple tables. Booking one table should not block out the entire establishment. We can scope our exclusion constraint to match specific resources using a foreign identifier (`table_id`) alongside the range.
>
> First, update the schema and ensure the [`btree_gist`](https://www.postgresql.org/docs/current/btree-gist.html) extension is enabled:
>
> ```sql
> -- Enable the btree_gist index required for multi-column constraints
> create extension btree_gist;
>
> create table reservations (
>   id serial primary key,
>   title text,
>   table_id int4,
>   duration tstzrange
> );
>
> -- Add a constraint to prevent overlaps only when the table_id matches
> alter table reservations
>   add constraint exclude_duration
>   exclude using gist (table_id WITH =, duration WITH &&);
> ```

现在，只要重叠发生在不同的桌子上，就允许重叠的时间：

> Now, overlapping times are permitted **as long as they occur on different tables**:
>
> ```sql
> -- Add a first reservation for Table 1
> insert into reservations (title, table_id, duration)
> values ('Tyler Dinner', 1, '[2024-07-04 18:00, 2024-07-04 21:00)');
>
> -- Insert fails because Table 1 is already booked during this timeframe
> insert into reservations (title, table_id, duration)
> values ('Thor Dinner', 1, '[2024-07-04 20:00, 2024-07-04 22:00)');
>
> -- Insert succeeds because Table 2 is available
> insert into reservations (title, table_id, duration)
> values ('Thor Dinner', 2, '[2024-07-04 20:00, 2024-07-04 22:00)');
> ```

---

## 结论

PostgreSQL 范围列为处理时间数据和区间数据提供了一种简洁、稳健的解决方案。通过使用 `&&` 等专用运算符简化查询逻辑，并通过排除约束保证绝对的数据完整性，开发者可以用更少的应用代码构建出防弹级别的调度和预订系统。

> ## Conclusion
>
> PostgreSQL range columns offer a clean, robust solution for handling temporal and interval data. By simplifying query logic with specialized operators like `&&` and guaranteeing absolute data integrity via exclusion constraints, developers can build bulletproof scheduling and reservation systems with significantly less application code.

---

## 更多资源

* 📺 [观看范围列视频指南](https://youtu.be/eG_9lZrrbEY?si=MtTQsKZrzMinU536)
* 📺 [查看约束视频指南](https://youtu.be/hjrQb029LEE?si=wJ8ztryZP6K6EKmW)
* 🗺️ [使用 Protomaps 在 Supabase 存储上自托管地图](https://supabase.link/protomaps-storage-yt)
* 🔒 [Supabase 行级安全性 (RLS) 指南](https://supabase.com/docs/guides/database/postgres/row-level-security)

> ## Additional Resources
>
> * 📺 [Watch the video guide for range columns](https://youtu.be/eG_9lZrrbEY?si=MtTQsKZrzMinU536)
> * 📺 [Check constraint video guide](https://youtu.be/hjrQb029LEE?si=wJ8ztryZP6K6EKmW)
> * 🗺️ [Self-host Maps on Supabase Storage with Protomaps](https://supabase.link/protomaps-storage-yt)
> * 🔒 [Supabase Row Level Security (RLS) Guide](https://supabase.com/docs/guides/database/postgres/row-level-security)