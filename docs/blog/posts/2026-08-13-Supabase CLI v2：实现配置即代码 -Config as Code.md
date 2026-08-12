---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-13
hide:
- navigation
tags:
- Supabase
- CLI
- DevOps
- CI/CD
- 配置即代码
title: Supabase CLI v2：实现配置即代码 (Config as Code)
---
### 文章背景与核心概要

Supabase 近期发布了 CLI v2 版本，正式引入了强大的“配置即代码”（Configuration as Code）支持。这一更新允许开发者将所有项目和分支的配置设置纳入版本控制系统（如 Git），从而确保整个团队开发环境的一致性与可复现性。

CLI v2 的设计核心在于 CI/CD 集成，旨在满足日益增长的自动化部署需求。通过使用人类可读的 `config.toml` 文件，开发者可以轻松管理身份验证、边缘函数、存储对象及数据库设置。该版本不仅简化了从预览环境到生产环境的部署流程，还通过配置漂移检测等功能，进一步提升了基础设施管理的可靠性。

---

## 在 CI/CD 流水线中使用 CLI
Supabase CLI 最初旨在让开发者能够在本地机器上引导整个 Supabase 技术栈，并使用与托管平台完全相同的基础设施。

> The Supabase CLI started as a way to bootstrap the entire Supabase stack on your local machine using the exact same infrastructure as the hosted platform. 

在过去两年中，CLI 的每周安装量已超过 180,000 次，其中近 85% 来自 GitHub Actions 等持续集成/持续部署 (CI/CD) 环境。常见的应用场景包括迁移生产数据库、部署函数以及运行 pgTAP 测试。这种转变促使 v2 版本将 CLI 的核心定位为一款全面的部署工具。

> Over the last 2 years, the CLI has grown to more than 180,000 weekly installs, with nearly 85% coming from Continuous Integration/Deployment (CI/CD) environments like GitHub Actions. Popular use cases include migrating production databases, deploying functions, and running pgTAP tests. This shift inspired a core focus on the CLI as a deployment tool for the v2 release.

---

## 使用 Supabase CLI 实现配置即代码
CLI 的“配置即代码”功能依赖于一种规范化的设置，即使用人类可读的 `config.toml` 文件。通过将 Edge Functions、存储对象及其他服务从预览环境无缝提升至测试和生产环境，您可以实现部署的一致性和可重复性。

> The CLI’s Configuration as Code feature relies on an opinionated setup using a human-readable `config.toml` file. You can make deployments consistent and repeatable by promoting Edge Functions, Storage objects, and other services seamlessly from preview environments to staging and production.

> **注意：检测配置漂移**
> 在更改任何项目配置之前，最好先验证远程配置是否发生了漂移。这可以通过在本地运行 `supabase link` 命令来完成，该命令会将您的整个本地 `config.toml` 与远程项目设置进行对比。

> **Note: Detecting config drift**
> Before changing any project configuration, it’s a good idea to verify that your remote config has not drifted. This can be done by running the `supabase link` command locally, which diffs your entire local `config.toml` with your remote project settings.

### 管理身份验证 (Auth) 配置
为了配置 Supabase 分支的 Auth 服务以支持任何 Vercel 预览 URL 的登录，我们在 auth 配置中为 `additional_redirect_urls` 声明了一个通配符：

> To configure the Auth service of Supabase branches to support login for any Vercel preview URL, we declare a wildcard for the `additional_redirect_urls` in the auth config:

```toml
[auth]
additional_redirect_urls = [
  "https://*-supabase.vercel.app/*/*",
  "https://supabase.com/*/*",
  "http://localhost:3000/*/*",
]
```

查看 [Auth 配置文档](/docs/guides/local-development/cli/config#auth-config)。

> View the [Auth config docs](/docs/guides/local-development/cli/config#auth-config).

### 管理边缘函数 (Edge Functions)
Supabase 网站使用多个 [Edge Functions](https://github.com/supabase/supabase/tree/master/supabase/functions) 来处理 AI 文档、搜索嵌入和图像生成。要配置 `search-embeddings` 函数的自动部署，请将以下代码块添加到 `config.toml` 中：

> The Supabase website uses several [Edge Functions](https://github.com/supabase/supabase/tree/master/supabase/functions) for AI docs, search embeddings, and image generation. To configure automatic deployment of the `search-embeddings` function, add the following block to `config.toml`:

```toml
[functions.search-embeddings]
verify_jwt = false
```

如果您使用的是 monorepo（例如 [@supabase/supabase](https://github.com/supabase/supabase) GitHub 仓库），您可能还需要自定义函数入口点和导入映射文件的路径。

> If you are using a monorepo (like the [@supabase/supabase](https://github.com/supabase/supabase) GitHub repository), you may also want to customize the paths to your function’s entrypoint and import map files.

> **注意：设置边缘函数密钥**
> 截至本版本，边缘函数密钥必须手动添加到分支中。我们计划在不久的将来支持在部署时设置函数密钥。

> **Note: Setting Edge Function secrets**
> Edge Function secrets must be manually added to branches as of this release. We plan to support setting Function secrets at deploy time in the near future.

查看 [Edge Functions 配置文档](/docs/guides/local-development/cli/config#edge-functions-config)。

> View the [Edge Functions config docs](/docs/guides/local-development/cli/config#edge-functions-config).

### 管理存储对象 (Storage Objects)
用于发布周门票的 [图像和字体](https://supabase.com/dashboard/project/xguihxuzqibwxjnimxev/storage/buckets/images) 存储在 Supabase Storage 中，并分发到全球 CDN。

> [Images and fonts](https://supabase.com/dashboard/project/xguihxuzqibwxjnimxev/storage/buckets/images) for launch week tickets are stored in Supabase Storage and distributed to global CDNs. 

在本地开发时，请在 `config.toml` 中添加一个 `[storage.buckets]` 代码块，以便 `supabase/assets` 目录中的文件自动上传到 Supabase Storage：

> When developing locally, add a `[storage.buckets]` block to `config.toml` so files in the `supabase/assets` directory automatically upload to Supabase Storage:

```toml
[storage.buckets.assets]
objects_path = "./assets"
```

1MB 以下的资源可以安全地提交并由 Git 跟踪以进行预览分支管理。像视频这样的大文件，最好通过 AWS S3 CLI 上传到 Supabase Storage。

> Assets under 1MB can be safely committed and tracked in Git for preview branching. Larger files like videos are best uploaded to Supabase Storage via the AWS S3 CLI.

查看 [Storage 配置文档](/docs/guides/local-development/cli/config#storage-config)。

> View the [Storage config docs](/docs/guides/local-development/cli/config#storage-config).

### 管理数据库设置和 Webhooks
虽然 Supabase 会根据您的数据库计算大小管理默认的 Postgres 设置，但您可以通过 `config.toml` 轻松更新和跟踪自定义数据库设置：

> While Supabase manages default Postgres settings based on your database compute size, you can easily update and track custom database settings via `config.toml`:

```toml
[db.settings]
track_commit_timestamp = true
```

管理 API 会自动判断参数是否需要重启数据库。如果不需要，配置将通过向 Postgres 进程发送 `SIGHUP` 信号来应用。

> The Management API automatically figures out if parameters require a database restart. If not, the config applies by sending `SIGHUP` to the Postgres process.

此外，您可以使用 `[experimental]` 配置块启用数据库 Webhooks，让您的数据库直接从 Postgres 函数调用 HTTP 端点：

> Additionally, you can enable database webhooks using the `[experimental]` config block to let your database call HTTP endpoints directly from Postgres functions:

```toml
[experimental.webhooks]
enabled = true
```

查看 [数据库配置文档](/docs/guides/local-development/cli/config#database-config)。

> View the [Database config docs](/docs/guides/local-development/cli/config#database-config).

---

## 管理分支和多个“远程”环境
如果您启用了 [分支功能 (Branching)](https://supabase.com/docs/guides/deployment/branching#enable-supabase-branching)，`config.toml` 中的设置将通过 Git 分支与 Supabase 分支之间的一对一映射，自动同步到所有临时分支。

> If you have [Branching](https://supabase.com/docs/guides/deployment/branching#enable-supabase-branching) enabled, your settings in `config.toml` automatically sync to all ephemeral branches via a one-to-one mapping between your Git branch and Supabase branch.

要配置特定的持久化分支，请通过提供其项目 ID 使用 `[remotes]` 代码块来声明设置：

> To configure a specific persistent branch, declare settings using the `[remotes]` block by providing its project ID:

```toml
[remotes.staging]
project_id = "your-project-ref"

[remotes.staging.db.seed]
sql_paths = ["./seeds/staging.sql"]
```

请务必先使用 CLI 命令配置持久化分支，以便将返回的项目 ID 添加到 `config.toml` 中：

> Always provision a persistent branch first using the CLI command so you can add the returned project ID to `config.toml`:

```bash
$ supabase --experimental branches create --persistent
Do you want to create a branch named develop? [Y/n]
```

---

## 入门指南
要开始使用“配置即代码”，请按照 [Supabase 指南](https://supabase.com/docs/guides/deployment/branching#how-to-use-supabase-branching) 连接 GitHub 仓库并启用分支功能。

> To start using configuration as code, follow the [Supabase guide](https://supabase.com/docs/guides/deployment/branching#how-to-use-supabase-branching) to connect a GitHub repository and enable Branching. 

或者，直接使用 Supabase CLI 开始：

> Alternatively, get started directly with the Supabase CLI:

```bash
supabase config push
```

### 安装
安装 Supabase CLI：[文档](/docs/guides/local-development/cli/getting-started#installing-the-supabase-cli)。

> Installing the Supabase CLI: [Documentation](/docs/guides/local-development/cli/getting-started#installing-the-supabase-cli).

### 升级
升级您的 CLI：[文档](/docs/guides/local-development/cli/getting-started#updating-the-supabase-cli)。

> Upgrade your CLI: [Documentation](/docs/guides/local-development/cli/getting-started#updating-the-supabase-cli).

### 重大变更
v2 版本中**没有重大变更**。

> There are **no breaking changes** in v2.

### 贡献者
* **CLI 团队：** Qiao ([@sweatybridge](https://github.com/sweatybridge)), Andrew ([@avallete](https://github.com/avallete))
* **Supabase 团队：** Bobbie, Lakshan, Joel, Filipe, TzeYiing, Div, Ant, Thor, Wen Bo, Kangming, Ivan, Kevin, Long, Stojan, Kamil, Inian, Greg, Fabrizio, Chris, Julien, Terry, Egor, Joshen, Steve, Guilherme, Crispy, Bo, Rodrigo, Beng, Copple
* **贡献者：** 庞大的开源社区。

> * **The CLI Team:** Qiao ([@sweatybridge](https://github.com/sweatybridge)), Andrew ([@avallete](https://github.com/avallete))
> * **The Supabase Team:** Bobbie, Lakshan, Joel, Filipe, TzeYiing, Div, Ant, Thor, Wen Bo, Kangming, Ivan, Kevin, Long, Stojan, Kamil, Inian, Greg, Fabrizio, Chris, Julien, Terry, Egor, Joshen, Steve, Guilherme, Crispy, Bo, Rodrigo, Beng, Copple
> * **With contributions from:** The extensive open-source community.

---

## 结论
当您的整个后端运行在 Supabase 上时，管理项目环境的意义远不止于模式迁移。借助 Supabase CLI v2，您可以使用配置文件高效管理开发环境，从而确保本地、测试和生产服务之间的一致性。

> Managing your project environments goes far beyond schema migrations when your entire backend runs on Supabase. With Supabase CLI v2, you can efficiently manage development environments using a configuration file to guarantee consistency across local, staging, and production services.