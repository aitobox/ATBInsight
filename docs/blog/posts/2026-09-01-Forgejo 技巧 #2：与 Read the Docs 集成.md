---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-09-01
hide:
- navigation
tags:
- Forgejo
- Read the Docs
- Webhook
- CI/CD
- 文档管理
title: 'Forgejo 技巧 #2：与 Read the Docs 集成'
---
### 文章背景与核心概要
本文是 Forgejo 技巧系列的第二篇，主要介绍如何将自托管的 Forgejo Git 仓库连接到 Read the Docs 平台，从而实现每次提交代码时自动构建文档，达到与原生 GitHub 集成相似的效果。

由于 Read the Docs 目前尚未对 Forgejo 仓库提供原生支持，我们需要通过手动配置 Webhook 的方式来变通实现这一集成。通过本文的步骤，你可以轻松将原有的 GitHub 集成迁移到自托管的 Forgejo 实例上，保持自动化文档工作流的顺畅运行。

---

## 摘要 (Summary)

> Learn how to connect a self-hosted Forgejo Git repository to [Read the Docs](https://readthedocs.org) to enable automatic documentation builds on every commit, mimicking native GitHub integration.

了解如何将自托管的 Forgejo Git 仓库连接到 [Read the Docs](https://readthedocs.org)，以便在每次提交时启用自动文档构建，从而模拟原生的 GitHub 集成。

---

## 什么是 Read the Docs？ (What is Read the Docs?)

> Read the Docs is a fantastic platform for hosting documentation for open-source projects.

Read the Docs 是一个用于托管开源项目文档的出色平台。

> When working with GitHub, Read the Docs automatically creates an integration that triggers documentation rebuilds every time a new commit is pushed. However, since Read the Docs does not currently offer native support for Forgejo-hosted repositories, this connection must be built manually.

当使用 GitHub 时，Read the Docs 会自动创建一个集成，在每次推送新提交时触发文档重新构建。然而，由于 Read the Docs 目前不提供对 Forgejo 托管仓库的原生支持，因此必须手动建立这种连接。

---

## Read the Docs 端配置 (The Read the Docs Side)

> To build a manual integration with functionality similar to GitHub's:

要构建一个功能类似于 GitHub 的手动集成：

> 1. Log in to your [Read the Docs dashboard](https://app.readthedocs.org/dashboard/) (assuming your project already exists and has an active GitHub integration to migrate).
> 2. Click on your project, select **Settings**, and click **Integrations** on the left sidebar.
> 3. If an integration named **GitHub incoming webhook** exists, delete it using the trashcan icon to disconnect your old GitHub repository.

1. 登录你的 [Read the Docs 仪表盘](https://app.readthedocs.org/dashboard/)（假设你的项目已经存在并且有一个需要迁移的活跃 GitHub 集成）。
2. 点击你的项目，选择 **Settings**（设置），然后点击左侧边栏上的 **Integrations**（集成）。
3. 如果存在名为 **GitHub incoming webhook** 的集成，请使用垃圾桶图标将其删除，以断开与旧 GitHub 仓库的连接。

<img alt="Delete GitHub integration" src="/static/images/readthedocs-delete-github.png"/>

> 4. Go back to **Settings**, update the **Repository** section by checking **Use manually configured repository URL**, and enter your repository's URL. Scroll to the bottom and click **Save**.

4. 返回 **Settings**（设置），勾选 **Use manually configured repository URL**（使用手动配置的仓库 URL）来更新 **Repository**（仓库）部分，并输入你的仓库 URL。滚动到页面底部并点击 **Save**（保存）。

<img alt="Update repository URL" src="/static/images/readthedocs-update-url.png"/>

> 5. Return to **Settings** > **Integrations** and click **Add Integration**. 
> 6. Since Forgejo isn't a natively supported option yet, select **GitHub incoming webhook** as the type to trick Read the Docs, then click **Add Integration**.
> 7. Close the big red warning claiming the git provider is unsupported (Forgejo uses a GitHub-compatible webhook format, so everything will still work).

5. 返回 **Settings** > **Integrations** 并点击 **Add Integration**（添加集成）。
6. 由于 Forgejo 尚不是原生支持的选项，请选择 **GitHub incoming webhook** 作为类型来“欺骗” Read the Docs，然后点击 **Add Integration**。
7. 关闭那个声称 git 提供商不受支持的大红色警告（Forgejo 使用与 GitHub 兼容的 Webhook 格式，因此一切仍将正常工作）。

> Keep this page open to grab the webhook URL and secret in the next step.

保持此页面打开，以便在下一步中获取 Webhook URL 和密钥。

<img alt="Add integration" src="/static/images/readthedocs-add-integration.png"/>

---

## Forgejo 端配置 (The Forgejo Side)

> Next, configure the webhook on your self-hosted Forgejo instance:

接下来，在你的自托管 Forgejo 实例上配置 Webhook：

> 1. Open your Forgejo repository in your browser, go to **Settings** > **Webhooks**, click **Add webhook**, and select **Forgejo** from the dropdown.

1. 在浏览器中打开你的 Forgejo 仓库，转到 **Settings**（设置）> **Webhooks**，点击 **Add webhook**（添加 Webhook），然后从下拉菜单中选择 **Forgejo**。

<img alt="Forgejo add webhook" src="/static/images/readthedocs-forgejo-webhook.png"/>

> 2. Copy the URL and secret from the Read the Docs webhook page into the corresponding Forgejo webhook fields.
> 3. Ensure the **HTTP method** is set to **POST** and **Trigger on** is set to **Push events**.
> 4. Scroll to the bottom and click **Add webhook** to save.

2. 将 Read the Docs Webhook 页面中的 URL 和密钥复制到相应的 Forgejo Webhook 字段中。
3. 确保 **HTTP method**（HTTP 方法）设置为 **POST**，**Trigger on**（触发条件）设置为 **Push events**（推送事件）。
4. 滚动到底部并点击 **Add webhook** 以保存。

<img alt="Forgejo webhook configuration" src="/static/images/readthedocs-forgejo-webhook-configured.png"/>

> That's it! Pushing to your repository will now trigger a notification to Read the Docs to build your documentation.

就是这样！现在，推送到你的仓库将触发向 Read the Docs 发送通知以构建你的文档。

---

## GitHub 端清理 (The GitHub Side)

> While technically optional, you can clean up your old GitHub repository for neatness:
> 1. Navigate to your old repository on GitHub.
> 2. Go to **Settings** > **Webhooks**.
> 3. Locate and delete the webhook pointing to *readthedocs.org* (which was invalidated when you deleted it on the Read the Docs side).

虽然从技术上讲是可选的，但你可以清理旧的 GitHub 仓库以保持整洁：
1. 导航到 GitHub 上的旧仓库。
2. 转到 **Settings** > **Webhooks**。
3. 找到并删除指向 *readthedocs.org* 的 Webhook（该 Webhook 在你在 Read the Docs 端删除它时已经失效）。

---

## 结论 (Conclusion)

> I hope this guide has been useful! Please share your thoughts on this solution, or let me know if you have an even better one.

希望本指南对你有所帮助！请分享你对这个解决方案的想法，或者如果你有更好的方法，请让我知道。