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
- Realtime
- RLS
- 安全授权
- 实时应用
title: Supabase Realtime：广播与在线状态的授权机制
---
### 文章背景与核心概要
Supabase 近期为其 Realtime（实时）服务的**广播（Broadcast）**和**在线状态（Presence）**功能正式引入了**授权（Authorization）**机制。借助 PostgreSQL 的行级安全性（Row Level Security, RLS），开发者现在可以为实时频道定义精细化的访问控制，从而确保只有经过授权的用户才能发送或接收临时消息以及状态更新。

这一新特性的推出解决了以往实时通道安全性不足的痛点。通过将数据库作为真理之源（Source of Truth），并利用创新的回滚事务检查与内存缓存策略，Supabase 在实现了严格权限控制的同时，依然保持了实时应用所需的极低延迟。该功能目前已进入公开测试阶段（Public Beta），极大扩展了 Supabase 在协作类、聊天类应用中的安全构建能力。

---

# Supabase Realtime: Broadcast and Presence Authorization

> Supabase has introduced **Authorization for Realtime's Broadcast and Presence** features. By leveraging PostgreSQL's Row Level Security (RLS), developers can now define granular access control for real-time channels, ensuring that only authorized users can send or receive ephemeral messages and presence updates.

---

## Overview

概述

> Supabase provides three core extensions for real-time applications:
> 1. **[Broadcast](https://supabase.com/docs/guides/realtime/broadcast):** Send ephemeral, low-latency messages between users.
> 2. **[Presence](https://supabase.com/docs/guides/realtime/presence):** Track online status and share state between users.
> 3. **[Postgres Changes](https://supabase.com/docs/guides/realtime/postgres-changes):** Listen to database changes in real-time.

Supabase 为实时应用提供了三个核心扩展：
1. **[广播 (Broadcast)](https://supabase.com/docs/guides/realtime/broadcast)：** 在用户之间发送临时的、低延迟的消息。
2. **[在线状态 (Presence)](https://supabase.com/docs/guides/realtime/presence)：** 追踪在线状态并在用户之间共享状态。
3. **[Postgres 变更 (Postgres Changes)](https://supabase.com/docs/guides/realtime/postgres-changes)：** 实时监听数据库的变更。

> This release allows you to secure Broadcast and Presence channels using the `realtime.messages` table within your database.

通过本次发布的新版本，你可以使用数据库中的 `realtime.messages` 表来保护广播和在线状态频道的安全。

## How Realtime Works Without Authorization

在没有授权机制时 Realtime 是如何工作的

> By default, any authenticated client can subscribe to any public channel to send and receive messages:

默认情况下，任何经过身份验证的客户端都可以订阅任何公共频道来发送和接收消息：

```javascript
import { createClient } from '@supabase/supabase-js'

// Prepare client with authenticated user
const client = createClient('<url>', '<anon_key>')
client.realtime.setAuth(token)

// Prepare the realtime channel
const channel = client.channel('topic')

channel.subscribe((status: string, err: any) => {
  if (status === 'SUBSCRIBED') {
    console.log('Connected')
  }
})
```

## Adding Authorization to Realtime Channels

为实时频道添加授权

> To secure your channels, follow these two steps:

要保护你的频道，请遵循以下两个步骤：

### 1. Create RLS Policies

1. 创建 RLS 策略

> You can define `SELECT` (receive) and `INSERT` (send) policies on the `realtime.messages` table. You can also use the `realtime.topic()` function to restrict access to specific channel names.

你可以在 `realtime.messages` 表上定义 `SELECT`（接收）和 `INSERT`（发送）策略。你还可以使用 `realtime.topic()` 函数来限制对特定频道名称的访问。

**Example: Restricting access to a 'locked' topic**

**示例：限制对“锁定”主题的访问**

```sql
create policy "authenticated users can only read from 'locked' topic"
on "realtime"."messages"
as permissive
for select   -- read only
to authenticated
using (
  realtime.topic() = 'locked'  -- access the topic name
);
```

### 2. Enabling Authorization on Channels

2. 在频道上启用授权

> When subscribing from the client, set the `private` configuration flag to `true`.

当从客户端进行订阅时，将 `private` 配置标志设置为 `true`。

```javascript
// With an authenticated user
supabase.realtime
  .channel('locked', { config: { private: true } })
  .subscribe((status: string, err: any) => {
    if (status === 'SUBSCRIBED') {
      console.log('Connected!')
    } else {
      console.error(err.message)
    }
  })
```

## How It Works

工作原理

> *   **Database as Source of Truth:** When a user subscribes, Realtime performs a check against the `realtime.messages` table. These checks are performed within a transaction that is immediately rolled back, ensuring no data is persisted.
> *   **Performance:** To maintain low latency, policies are cached in memory on the server for the duration of the connection or until the JWT expires.
> *   **Context:** The server maps policies to the user's connection, ensuring that authorization is verified at the moment of subscription and refreshed upon token updates.

*   **以数据库作为真理之源：** 当用户订阅时，Realtime 会针对 `realtime.messages` 表执行检查。这些检查是在一个会立即回滚的事务中进行的，从而确保不会持久化任何数据。
*   **性能表现：** 为了保持低延迟，策略会在服务器内存中进行缓存，缓存时间持续至连接断开或 JWT 过期。
*   **上下文环境：** 服务器将策略映射到用户的连接上，确保在订阅时验证授权，并在令牌更新时进行刷新。

## Performance and Security

性能与安全

> *   **Minimal Latency:** Policy checks occur only during the initial subscription. Subsequent messages pass through the server with minimal overhead.
> *   **Caching:** Policies are cached close to the user on the global network.
> *   **Postgres Changes:** Note that this authorization method currently applies only to **Broadcast** and **Presence**. Postgres Changes already supports RLS natively on the tables being observed.

*   **极低延迟：** 策略检查仅在初始订阅期间发生。后续消息通过服务器时几乎没有额外开销。
*   **缓存机制：** 策略缓存在全球网络中靠近用户的位置。
*   **Postgres 变更：** 请注意，此授权方法目前仅适用于**广播（Broadcast）**和**在线状态（Presence）**。Postgres 变更（Postgres Changes）已经对正在观察的表原生支持了 RLS。

## Availability

可用性

> Broadcast and Presence Authorization is currently in **Public Beta**. For complex use cases, refer to the [Next.js Authorization Demo](https://github.com/supabase/supabase/tree/master/examples/realtime/nextjs-authorization-demo) or the [Flutter Figma Clone](https://github.com/supabase/supabase/tree/master/examples/realtime/flutter-figma-clone). 

广播和在线状态授权目前处于**公开测试（Public Beta）**阶段。对于复杂的用例，请参考 [Next.js 授权示例](https://github.com/supabase/supabase/tree/master/examples/realtime/nextjs-authorization-demo) 或 [Flutter Figma 仿制版示例](https://github.com/supabase/supabase/tree/master/examples/realtime/flutter-figma-clone)。

> Please share your feedback in the [official GitHub discussion](https://github.com/orgs/supabase/discussions/22484).

请在[官方 GitHub 讨论区](https://github.com/orgs/supabase/discussions/22484)分享你的反馈。