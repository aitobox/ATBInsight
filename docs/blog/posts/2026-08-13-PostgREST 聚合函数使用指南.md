---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-13
hide:
- navigation
tags:
- PostgREST
- PostgreSQL
- API
- 聚合函数
- 数据库安全
title: PostgREST 聚合函数使用指南
---
### 文章背景与核心概要
PostgREST v12 版本引入了对聚合函数（如 `avg()`、`count()`、`max()`、`min()` 和 `sum()`）的原生支持，使开发者能够直接通过 API 动态汇总和切片数据。该功能可以与垂直过滤、列重命名以及嵌套资源等现有特性无缝集成，极大地丰富了数据查询的灵活性。

然而，由于聚合函数通常需要跨越可能无限的行进行计算，且会绕过标准的分页限制，因此它们在默认情况下处于**禁用状态**。本文将详细介绍聚合函数的基础用法、与表关联的组合使用方法，以及如何通过 `pg_plan_filter_module` 等工具妥善保护数据库，防范性能瓶颈和拒绝服务（DoS）攻击。

---

## 聚合函数基础
## The Basics of Aggregate Functions

PostgREST 支持 PostgreSQL 中最常用的聚合函数：`avg()`、`count()`、`max()`、`min()` 和 `sum()`。
> PostgREST supports the most common aggregate functions from PostgreSQL: `avg()`, `count()`, `max()`, `min()`, and `sum()`. 

假设我们有一个名为 `movies` 的表，包含以下列：`name`、`release_year`、`genre` 和 `box_office_earnings`。若要查找所有电影中的最大和最小 `release_year`：
> Imagine we have a table called `movies` with the columns: `name`, `release_year`, `genre`, and `box_office_earnings`. To find the maximum and minimum `release_year` across all movies:

### cURL
### cURL
```bash
$ curl 'http://postgrest/movies?select=release_year.max(),release_year.min()'
```

### Supabase-js
### Supabase-js
```javascript
const { data, error } = await supabase
  .from('movies')
  .select('release_year.max(), release_year.min()')
```

### 响应结果
### Response
```json
[
  {
    "max": 2022,
    "min": 2018
  }
]
```

### 数据分组
### Grouping Data
无需显式编写 `GROUP BY` 子句，`select` 参数中任何**未**使用聚合函数的列都会自动充当分组列。例如，要按 `genre`（流派）分组获取最大和最小上映年份：
> Instead of explicitly writing a `GROUP BY` clause, any column in the `select` parameter *without* an aggregate function automatically acts as a grouping column. For example, to get the max and min release years grouped by `genre`:

### cURL
### cURL
```bash
$ curl 'http://postgrest/movies?select=genre,release_year.max(),release_year.min()'
```

### Supabase-js
### Supabase-js
```javascript
const { data, error } = await supabase
  .from('movies')
  .select('genre, release_year.max(), release_year.min()')
```

### 响应结果
### Response
```json
[
  {
    "genre": "Adventure",
    "max": 2021,
    "min": 2020
  },
  {
    "genre": "Horror",
    "max": 2022,
    "min": 2019
  },
  {
    "genre": "Sci-Fi",
    "max": 2022,
    "min": 2018
  },
  {
    "genre": "Mystery",
    "max": 2019,
    "min": 2019
  }
]
```

---

## 聚合函数与嵌套资源
## Aggregate Functions and Embedded Resources

聚合函数也可以与[嵌套资源（embedded resources）](https://postgrest.org/en/stable/references/api/resource_embedding.html)无缝配合。
> Aggregate functions also work seamlessly with [embedded resources](https://postgrest.org/en/stable/references/api/resource_embedding.html). 

假设我们有一个 `directors` 表（包含 `name`、`country`），它与 `movies` 表具有一对多关系。若要查找每个导演的最旧和最新电影上映年份：
> Suppose we have a `directors` table (`name`, `country`) with a one-to-many relationship to the `movies` table. To find the oldest and newest movie years for each director:

### cURL
### cURL
```bash
$ curl 'http://postgrest/directors?select=name,movies(newest_movie_year:release_year.max(),oldest_movie_year:release_year.min())'
```

### Supabase-js
### Supabase-js
```javascript
const { data, error } = await supabase.from('directors').select(`
		name,
		movies(
			newest_movie_year:release_year.max(),
			oldest_movie_year:release_year.min()
		)
`)
```

### 响应结果
### Response
```json
[
  {
    "name": "Maria Gonzalez",
    "movies": [
      {
        "newest_movie_year": 2022,
        "oldest_movie_year": 2018
      }
    ]
  },
  {
    "name": "John Smith",
    "movies": [
      {
        "newest_movie_year": 2022,
        "oldest_movie_year": 2019
      }
    ]
  },
  {
    "name": "Amit Patel",
    "movies": [
      {
        "newest_movie_year": 2021,
        "oldest_movie_year": 2019
      }
    ]
  }
]
```

### 展开嵌套资源
### Spreading Embedded Resources
你还可以使用[展开嵌套资源（spread embedded resources）](https://postgrest.org/en/stable/references/api/resource_embedding.html#spread-embedded-resource)按嵌套表的列对顶级聚合进行分组：
> You can also use [spread embedded resources](https://postgrest.org/en/stable/references/api/resource_embedding.html#spread-embedded-resource) to group top-level aggregates by an embedded table's columns:

### cURL
### cURL
```bash
$ curl 'http://postgrest/movies?select=avg_earnings:box_office_earnings.avg(),...directors(country)'
```

### Supabase-js
### Supabase-js
```javascript
const { data, error } = await supabase.from('movies').select(`
		avg_earnings:box_office_earnings.avg(),
    ...directors(country)
	`)
```

### 响应结果
### Response
```json
[
  {
    "avg_earnings": 10200000.38,
    "country": "Spain"
  },
  {
    "avg_earnings": 8933333.79,
    "country": "India"
  },
  {
    "avg_earnings": 8933333.84,
    "country": "United States"
  }
]
```

---

## 确保聚合函数的安全使用
## Staying Safe with Aggregate Functions

由于聚合函数是在实际上数量无限的行上运行（与分页查询不同），如果未建立索引或优化不当，它们可能会引入沉重的性能瓶颈，或者成为拒绝服务（DoS）攻击的突破口。
> Because aggregate functions operate across an effectively limitless number of rows (unlike paginated queries), they can introduce heavy performance bottlenecks or serve as vectors for Denial-of-Service (DoS) attacks if unindexed or poorly optimized.

正因如此，聚合函数在**默认情况下是禁用的**。
> For this reason, aggregate functions are **disabled by default**.

### 在 Supabase 中启用聚合
### Enabling Aggregates in Supabase
要启用此功能，请更新连接角色并重新加载服务器配置：
> To enable the feature, update the connection role and reload the server configuration:

```sql
ALTER ROLE authenticator SET pgrst.db_aggregates_enabled = 'true';
NOTIFY pgrst, 'reload config';
```

### 防范慢查询
### Protecting Against Slow Queries
你可以使用 [`pg_plan_filter_module`](https://github.com/pgexperts/pg_plan_filter) 扩展为 PostgREST 运行的查询设置执行成本的上限：
> You can use the [`pg_plan_filter_module`](https://github.com/pgexperts/pg_plan_filter) extension to set an upper limit on the execution cost of queries that PostgREST will run:

```sql
ALTER USER authenticator SET plan_filter.statement_cost_limit = 1e7;
```

### 设置按角色划分的限制
### Setting Per-Role Limits
你可以限制匿名用户只能运行低成本查询，同时为已认证用户赋予更高的阈值：
> You can restrict anonymous users to cheaper queries while giving authenticated users higher thresholds:

```sql
-- 匿名用户只能运行低成本查询
-- anonymous users can only run cheap queries
ALTER
  USER anon
SET
  plan_filter.statement_cost_limit = 10000;

-- 已认证用户可以运行成本更高的查询
-- authenticated users can more expensive queries
ALTER
  USER authenticated
SET
  plan_filter.statement_cost_limit = 1e6;
```

---

## 总结
## Summing Up

PostgREST v12 为聚合函数带来了深度集成，提供了一种强大的抽象能力，能够与过滤、重命名和资源嵌套等现有功能完美契合。由于其对性能的潜在影响，请记得有意识地启用它们，并使用诸如 `pg_plan_filter_module` 之类的工具实现查询成本的安全防护。有关完整详情，请参考[官方 PostgREST 聚合函数文档](https://postgrest.org/en/v12.0/references/api/aggregate_functions.html)。
> PostgREST v12 brings deep integration for aggregate functions, offering a powerful abstraction that fits smoothly alongside existing features like filtering, renaming, and resource embedding. Because of the performance implications, remember to enable them intentionally and implement query cost safeguards using tools like `pg_plan_filter_module`. For full details, consult the [official PostgREST aggregate functions documentation](https://postgrest.org/en/v12.0/references/api/aggregate_functions.html).