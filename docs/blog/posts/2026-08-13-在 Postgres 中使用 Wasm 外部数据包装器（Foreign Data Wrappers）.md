---
authors:
- aitoboxrobot
categories:
- 产品发布
date: 2026-08-13
hide:
- navigation
tags:
- PostgreSQL
- WebAssembly
- Supabase
- FDW
- Rust
title: 在 Postgres 中使用 Wasm 外部数据包装器（Foreign Data Wrappers）
---
### 文章背景与核心概要
Supabase 近期为其开源的 Rust 框架 Wrappers 引入了 **WebAssembly (Wasm)** 支持，该框架用于创建 PostgreSQL 外部数据包装器（FDW）。这项新功能使开发者能够安全、模块化且高效地将 Postgres 连接到外部第三方服务，并像查询本地原生表一样对其进行查询。Wasm 包装器可以轻松打包并通过 GitHub 或 AWS S3 等可通过 URL 访问的存储进行分发，而无需深入了解复杂的 Postgres 内部 API。目前，该功能已在所有新建的 Supabase 项目中推出公开 Alpha 版本，并附带针对 Snowflake 和 Paddle 等平台的内置模板与集成。

---

## 什么是外部数据包装器？
> [Foreign Data Wrappers (FDWs)](https://wiki.postgresql.org/wiki/Foreign_data_wrappers) are a powerful feature of Postgres that allows you to connect to and query external data sources as if they were regular tables. 

[外部数据包装器（FDWs）](https://wiki.postgresql.org/wiki/Foreign_data_wrappers)是 Postgres 的一项强大功能，允许你连接并查询外部数据源，就像它们是常规数据表一样。

> [Wrappers](https://github.com/supabase/wrappers) is an open-source project that simplifies the creation of Postgres Foreign Data Wrappers using [Rust](https://www.rust-lang.org/).

[Wrappers](https://github.com/supabase/wrappers) 是一个开源项目，它简化了使用 [Rust](https://www.rust-lang.org/) 创建 Postgres 外部数据包装器的过程。

---

## 为什么选择 WebAssembly？
> [WebAssembly (Wasm)](https://webassembly.org/) is a binary instruction format that enables secure and high-performance execution of code. Originally designed for web browsers, it can now be utilized in server-side environments like Postgres.

[WebAssembly (Wasm)](https://webassembly.org/) 是一种二进制指令格式，能够实现安全且高性能的代码执行。它最初是为网页浏览器设计的，现在已被应用到诸如 Postgres 等服务器端环境中。

> Key benefits of Wasm FDWs include:
> * **Improved Security:** Wasm's sandboxed execution runtime with minimal interfaces enhances the security of FDWs.
> * **Simplified Development:** Developers can use [Rust](https://www.rust-lang.org/) to create complex FDWs without diving deep into internal Postgres APIs.
> * **Simplified Distribution:** Easily distribute your Wasm FDW through any URL-accessible storage (such as GitHub or S3).
> * **Enhanced Performance:** Wasm's near-native speed ensures FDWs operate with minimal overhead.
> * **Increased Modularity:** Each Wasm FDW is an isolated package that is dynamically loaded and executed individually by Wrappers.

Wasm FDW 的核心优势包括：
* **更高的安全性：** Wasm 的沙盒化执行运行时具有最简接口，增强了 FDW 的安全性。
* **简化开发：** 开发者可以使用 [Rust](https://www.rust-lang.org/) 构建复杂的 FDW，而无需深入研究 Postgres 内部 API。
* **简化分发：** 通过任何可通过 URL 访问的存储（如 GitHub 或 S3）轻松分发你的 Wasm FDW。
* **性能增强：** Wasm 接近原生运行的速度确保了 FDW 在极低的开销下运行。
* **提高模块化：** 每个 Wasm FDW 都是一个独立的包，由 Wrappers 动态加载和独立执行。

---

## 架构
> The architecture of Wasm FDWs consists of the following key components:

Wasm FDW 的架构包含以下核心组件：

> 1. **Supabase Wrappers Extension (Host):** Runs within Postgres and includes:
>    * **Wasm Runtime:** Provides the environment to execute the Wasm FDW package.
>    * **HTTP Interface:** Manages communication with external data sources through HTTP.
>    * **Utilities:** Helper tools and functions to support FDW operations.
>    * **Additional Modules:** Specific functionalities such as JWT and stats.
> 2. **Wasm FDWs (Guests):** Isolated, dynamically loaded Wasm packages that fetch and process data in a sandboxed environment (e.g., Snowflake Wasm FDW, Paddle Wasm FDW).
> 3. **Web Storage:** External storage services like GitHub or S3 where Wasm packages are stored publicly.
> 4. **External Data Source:** External systems accessed via RESTful APIs (e.g., Snowflake, Paddle).

1. **Supabase Wrappers 扩展（宿主机）：** 运行在 Postgres 内部，包含：
   * **Wasm 运行时：** 提供执行 Wasm FDW 包的环境。
   * **HTTP 接口：** 通过 HTTP 管理与外部数据源的通信。
   * **实用工具：** 支持 FDW 操作的辅助工具和函数。
   * **附加模块：** 如 JWT 和统计信息等特定功能。
2. **Wasm FDW（客体机）：** 隔离的、动态加载的 Wasm 包，在沙盒环境中获取和处理数据（例如 Snowflake Wasm FDW、Paddle Wasm FDW）。
3. **网络存储：** 存放 Wasm 包的外部存储服务（如公开存储在 GitHub 或 S3 上）。
4. **外部数据源：** 通过 RESTful API 访问的外部系统（例如 Snowflake、Paddle）。

---

## 数据获取
> Wasm FDWs are loaded dynamically when the first request is made. The interaction flow follows these steps:

Wasm FDW 在发起第一次请求时会被动态加载。其交互流程如下：

> 1. **Wasm Download:** The package is dynamically downloaded from web storage (like GitHub or S3) and cached locally the first time a `SELECT` statement is initiated.
> 2. **Initialization and Execution:** The Wasm FDW runs within an embedded, sandboxed runtime environment isolated from the main Postgres system.
> 3. **Data Fetching via RESTful API:** Wasm FDWs interact with external data sources using RESTful APIs.
> 4. **Query Handling and Integration:** Postgres invokes the appropriate Wasm FDW, fetches and processes the data, and integrates it back into the query execution pipeline.

1. **Wasm 下载：** 当首次执行 `SELECT` 语句时，该包会从网络存储（如 GitHub 或 S3）中动态下载并缓存在本地。
2. **初始化与执行：** Wasm FDW 在独立于主 Postgres 系统的嵌入式沙盒运行时环境中运行。
3. **通过 RESTful API 获取数据：** Wasm FDW 使用 RESTful API 与外部数据源进行交互。
4. **查询处理与集成：** Postgres 调用相应的 Wasm FDW，获取并处理数据，然后将其重新集成到查询执行管道中。

> > **Note:** The Wasm FDW currently only supports data sources with HTTP(S)-based JSON APIs. Other sources, such as TCP/IP-based DBMS or local files, are not yet supported.
> 
> **注意：** Wasm FDW 目前仅支持基于 HTTP(S) 的 JSON API 数据源。其他来源（如基于 TCP/IP 的 DBMS 或本地文件）暂不支持。

---

## 开发你自己的 Wasm FDW
> A major benefit of Wasm FDW is the ability to build and deploy custom wrappers. To get started, clone the [Postgres Wasm FDW [Template](https://github.com/supabase-community/postgres-wasm-fdw)]. 

Wasm FDW 的一大优势是能够构建和部署自定义包装器。要开始使用，请克隆 [Postgres Wasm FDW 模板](https://github.com/supabase-community/postgres-wasm-fdw)。

> Visit the [Wrappers docs and guides](https://fdw.dev/guides/create-wasm-wrapper/) to learn more.

访问 [Wrappers 文档与指南](https://fdw.dev/guides/create-wasm-wrapper/)以了解更多信息。

> [!NOTE]
> As Wasm FDWs can access external data sources, you should **never** install Wasm Wrappers from untrusted sources. Always use official Supabase FDWs or trusted sources with full visibility and control.

> [!NOTE]
> 由于 Wasm FDW 可以访问外部数据源，你**绝不应该**从不受信任的来源安装 Wasm Wrappers。请务必使用官方的 Supabase FDW 或具有完全可见性和控制权的受信任来源。

---

## 立即在 Supabase 上体验
> The Wasm FDW feature is available today on the Supabase platform, featuring built-in support for [Snowflake](https://supabase.com/docs/guides/database/extensions/wrappers/snowflake) and [Paddle](https://supabase.com/docs/guides/database/extensions/wrappers/paddle).

Wasm FDW 功能现已在 Supabase 平台上架，并内置了对 [Snowflake](https://supabase.com/docs/guides/database/extensions/wrappers/snowflake) 和 [Paddle](https://supabase.com/docs/guides/database/extensions/wrappers/paddle) 的支持。

### 1. 启用 Wasm Wrappers
> Inside the [SQL editor](https://supabase.com/dashboard/project/_/sql/new), enable the feature:

在 [SQL 编辑器](https://supabase.com/dashboard/project/_/sql/new) 中启用该功能：

```sql
-- install Wrappers extension
create extension if not exists wrappers with schema extensions;

-- create Wasm foreign data wrapper
create foreign data wrapper wasm_wrapper
  handler wasm_fdw_handler
  validator wasm_fdw_validator;
```

### 2. 获取你的 Paddle 凭据
> Sign up for [a sandbox account](https://developer.paddle.com/api-reference/overview#base-url) and generate an API key via the [Paddle sandbox dashboard](https://sandbox-vendors.paddle.com/authentication-v2).

注册一个[沙盒账户](https://developer.paddle.com/api-reference/overview#base-url)，并通过 [Paddle 沙盒控制面板](https://sandbox-vendors.paddle.com/authentication-v2)生成 API 密钥。

### 3. 保存凭据并创建外部服务器
> Create a Paddle server in Postgres using the Wasm FDW:

使用 Wasm FDW 在 Postgres 中创建一个 Paddle 服务器：

```sql
-- create Paddle foreign server
create server paddle_server
  foreign data wrapper wasm_wrapper
  options (
    -- check all available versions at
    -- https://fdw.dev/catalog/paddle/#available-versions
    fdw_package_url 'https://github.com/supabase/wrappers/releases/download/wasm_paddle_fdw_v0.1.1/paddle_fdw.wasm',
    fdw_package_name 'supabase:paddle-fdw',
    fdw_package_version '0.1.1',
    fdw_package_checksum 'c5ac70bb2eef33693787b7d4efce9a83cde8d4fa40889d2037403a51263ba657',

    -- save your Paddle credentials
    api_url 'https://sandbox-api.paddle.com',
    api_key '<your Paddle sandbox API key>'
  );
```

### 4. 设置外部表
> Create a dedicated schema and table for your Paddle data:

为你的 Paddle 数据创建一个专用的架构和表：

```sql
-- create dedicated schema for Paddle foreign tables
create schema if not exists paddle;

-- create foreign table
create foreign table paddle.customers (
  id text,
  name text,
  email text,
  status text,
  custom_data jsonb,
  created_at timestamp,
  updated_at timestamp,
  attrs jsonb
)
server paddle_server
options (
  object 'customers',
  rowid_column 'id'
);
```

### 5. 从 Postgres 查询 Paddle
> Query the foreign table directly from SQL:

直接通过 SQL 查询外部表：

```sql
select id, name, email, status
from paddle.customers;
```

> For more detailed guides, check out the [Supabase Wrappers documentation](https://fdw.dev/).

有关更详细的指南，请查看 [Supabase Wrappers 文档](https://fdw.dev/)。

---

## 感谢我们的社区贡献者
> This innovation was made possible by the relentless efforts of our vibrant community. Special thanks to:
> * [Aayushya Vajpayee](https://github.com/AayushyaVajpayee)
> * [Romain Graux](https://github.com/romaingrx)

这项创新离不开充满活力的社区成员们的不懈努力。特别感谢：
* [Aayushya Vajpayee](https://github.com/AayushyaVajpayee)
* [Romain Graux](https://github.com/romaingrx)

> Want to join the Supabase Wrappers community contributors? [Check out the contribution docs](https://fdw.dev/contributing/core/).

想要加入 Supabase Wrappers 社区贡献者的行列？[请查看贡献文档](https://fdw.dev/contributing/core/)。