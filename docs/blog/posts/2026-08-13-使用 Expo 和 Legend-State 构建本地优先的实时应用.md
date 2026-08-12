---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-13
hide:
- navigation
tags:
- Expo
- React Native
- Legend-State
- Supabase
- Local-first
title: 使用 Expo 和 Legend-State 构建本地优先的实时应用
---
### 文章背景与核心概要
随着移动互联网对流畅体验和离线可用性的要求不断提高，“本地优先”（Local-first）架构逐渐成为现代应用开发的主流趋势。本文介绍如何结合 **Expo**、**React Native** 以及高性能状态与同步库 **Legend-State**，配合 **Supabase** 后端，构建一个具备极速响应和离线恢复能力的跨平台应用。

通过 Legend-State 的强力同步插件，开发者能够以极少的样板代码实现本地持久化、自动重试机制以及与 Supabase 实时频道的无缝对接。文章深入浅出地演示了从项目初始化、数据库模式配置、TypeScript 类型生成到数据读写及实时订阅的完整开发流程，为构建具有“多人协同”特性的现代化移动端与网页应用提供了宝贵的参考指南。

---

> **快速链接：**
> - 更喜欢视听学习？[观看视频指南！](https://supabase.link/local-first-expo-legend-state-yt)
> - 更喜欢代码？[直接跳到代码仓库](https://github.com/expo/examples/tree/master/with-legend-state-supabase)
> - 启动新项目：`npx create-expo-app --example with-legend-state-supabase`

---

## 执行摘要 (Executive Summary)

本指南探讨了如何使用 **Expo**、**React Native** 和 **Legend-State** 并集成 **Supabase**，来构建快速、响应迅速且具有弹性的本地优先应用程序。

Legend-State 充当了一个高性能的多合一状态与同步库。结合 Supabase 的后端、实时频道以及行级安全性（RLS），开发者可以轻松构建离线优先的移动端和网页应用，实现最少的样板代码和最高性能。

> **Executive Summary**
> This guide explores building fast, responsive, and resilient local-first applications using **Expo**, **React Native**, and **Legend-State** integrated with **Supabase**. 
> 
> Legend-State acts as a high-performance, all-in-one state and synchronization library. Combined with Supabase's backend, real-time channels, and Row Level Security (RLS), developers can effortlessly build offline-first mobile and web applications with minimal boilerplate and maximum performance.

---

## Legend-State 简介

[Legend-State](https://legendapp.com/open-source/state/v3/) 围绕四个主要目标设计：
1. 尽可能简单易用。
2. 提供最快的 React 状态库性能。
3. 实现细粒度响应式，以尽量减少重新渲染。
4. 提供强大的同步和持久化功能（原生支持 Supabase！）。

结合 Expo 和 React Native（通过 [React Native Async Storage](https://github.com/react-native-async-storage/async-storage)），它为本地优先架构提供了理想的技术栈。

> **Introduction to Legend-State**
> [Legend-State](https://legendapp.com/open-source/state/v3/) is designed around four primary goals:
> 1. Being as easy as possible to use.
> 2. Providing the fastest React state library performance.
> 3. Enabling fine-grained reactivity for minimal re-renders.
> 4. Offering powerful synchronization and persistence (with native Supabase support!).
> 
> Coupled with Expo and React Native (via [React Native Async Storage](https://github.com/react-native-async-storage/async-storage)), it provides an ideal stack for local-first architecture.

---

## 什么是本地优先架构？

在本地优先软件中，*“另一台计算机的可用性永远不应该妨碍你工作”*（[Martin Kleppmann](https://www.youtube.com/watch?v=NMq0vncHJvU)）。

用户直接在设备上的数据库中进行读写，从而确保应用在离线时也能无缝运行。重新连接后，数据会在各设备之间自动同步。在线时，这种架构支持强大的“多人”体验，正如 [Figma](https://www.figma.com/blog/how-figmas-multiplayer-technology-works/) 所普及的那样。

如需深入了解，请查看 [Expo 本地优先文档](https://docs.expo.dev/guides/local-first/)。

---

> **What is a Local-First Architecture?**
> In local-first software, *“the availability of another computer should never prevent you from working”* ([Martin Kleppmann](https://www.youtube.com/watch?v=NMq0vncHJvU)). 
> 
> Users read and write directly to an on-device database, ensuring the app functions seamlessly while offline. Once reconnected, data syncs automatically across devices. When online, this architecture supports robust "multiplayer" experiences, as popularized by [Figma](https://www.figma.com/blog/how-figmas-multiplayer-technology-works/).
> 
> For a deeper dive, check out the [Expo Local-First Docs](https://docs.expo.dev/guides/local-first/).

---

## Legend-State 如何实现这一目标

Legend-State 通过稳健的可观察对象（observable）生命周期自动处理持久化和同步：
1. 将待处理的更改保存到本地持久化存储。
2. 将更改保存到本地持久化存储。
3. 将更改保存到远程持久化存储（Supabase）。
4. 在成功保存到远程后更新可观察对象和本地存储（例如，更新时间戳如 `updated_at`）。
5. 从本地持久化存储中清除待处理的更改。

> **How Legend-State Makes It Work**
> Legend-State handles persistence and syncing automatically through a robust observable lifecycle:
> 1. Save pending changes to local persistence.
> 2. Save changes to local persistence.
> 3. Save changes to remote persistence (Supabase).
> 4. Update observables and local storage upon successful remote save (e.g., updating timestamps like `updated_at`).
> 5. Clear pending changes from local persistence.

---

## 设置项目

使用 CLI 初始化一个新的空白 Expo 应用：

```bash
npx create-expo-app@latest --template blank
```

> **Setting Up the Project**
> Initialize a new blank Expo app using the CLI:
> 
> ```bash
> npx create-expo-app@latest --template blank
> ```

### 安装依赖

使用 `expo install` 安装核心依赖：

```bash
npx expo install @legendapp/state@beta @supabase/supabase-js react-native-get-random-values @react-native-async-storage/async-storage
```

> ### Installing Dependencies
> Install the core dependencies using `expo install`:
> 
> ```bash
> npx expo install @legendapp/state@beta @supabase/supabase-js react-native-get-random-values @react-native-async-storage/async-storage
> ```

---

## 配置 Supabase

1. 在 [database.new](https://database.new) 创建一个项目。
2. 在根目录下创建一个 `.env.local` 文件，并从你的 [Supabase API 设置](https://supabase.com/dashboard/project/_/settings/api) 中添加项目凭证：

```env
EXPO_PUBLIC_SUPABASE_URL=
EXPO_PUBLIC_SUPABASE_ANON_KEY=
```

3. 在 `utils/SupaLegend.ts` 处创建一个工具文件来初始化 Supabase 客户端：

```typescript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.EXPO_PUBLIC_SUPABASE_URL,
  process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
)
```

> **Configuring Supabase**
> 1. Create a project at [database.new](https://database.new).
> 2. Create a `.env.local` file in your root directory and add your project credentials from your [Supabase API Settings](https://supabase.com/dashboard/project/_/settings/api):
> 
> ```env
> EXPO_PUBLIC_SUPABASE_URL=
> EXPO_PUBLIC_SUPABASE_ANON_KEY=
> ```
> 
> 3. Create a utility file at `utils/SupaLegend.ts` to initialize the Supabase client:
> 
> ```typescript
> import { createClient } from '@supabase/supabase-js'
> 
> const supabase = createClient(
>   process.env.EXPO_PUBLIC_SUPABASE_URL,
>   process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
> )
> ```

---

## 配置 Legend-State

扩展你的 `utils/SupaLegend.ts` 文件，将 `syncedSupabase` 与 Async Storage 和 Supabase 连接起来：

```typescript
import { createClient } from '@supabase/supabase-js'
import { observable } from '@legendapp/state'
import { syncedSupabase } from '@legendapp/state/sync-plugins/supabase'
import { configureSynced } from '@legendapp/state/sync'
import { observablePersistAsyncStorage } from '@legendapp/state/persist-plugins/async-storage'
import AsyncStorage from '@react-native-async-storage/async-storage'

const supabase = createClient(
  process.env.EXPO_PUBLIC_SUPABASE_URL,
  process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
)

// 创建一个配置好的同步函数
const customSynced = configureSynced(syncedSupabase, {
  // 使用 React Native Async Storage
  persist: {
    plugin: observablePersistAsyncStorage({
      AsyncStorage,
    }),
  },
  generateId,
  supabase,
  changesSince: 'last-sync',
  fieldCreatedAt: 'created_at',
  fieldUpdatedAt: 'updated_at',
  // 可选：启用软删除
  fieldDeleted: 'deleted',
})

export const todos$ = observable(
  customSynced({
    supabase,
    collection: 'todos',
    select: (from) => from.select('id,counter,text,done,created_at,updated_at,deleted'),
    actions: ['read', 'create', 'update', 'delete'],
    realtime: true,
    // 在本地持久化数据和待处理的更改
    persist: {
      name: 'todos',
      retrySync: true, // 持久化待处理的更改并重试
    },
    retry: {
      infinite: true, // 使用指数退避策略无限重试更改
    },
  })
)
```

> `syncedSupabase` 是用于 Supabase 的 Legend-State 同步插件，它为 `supabase-js` 提供了开箱即用的配置。

> **Configuring Legend-State**
> Extend your `utils/SupaLegend.ts` file to wire up `syncedSupabase` with Async Storage and Supabase:
> 
> ```typescript
> import { createClient } from '@supabase/supabase-js'
> import { observable } from '@legendapp/state'
> import { syncedSupabase } from '@legendapp/state/sync-plugins/supabase'
> import { configureSynced } from '@legendapp/state/sync'
> import { observablePersistAsyncStorage } from '@legendapp/state/persist-plugins/async-storage'
> import AsyncStorage from '@react-native-async-storage/async-storage'
> 
> const supabase = createClient(
>   process.env.EXPO_PUBLIC_SUPABASE_URL,
>   process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
> )
> 
> // Create a configured sync function
> const customSynced = configureSynced(syncedSupabase, {
>   // Use React Native Async Storage
>   persist: {
>     plugin: observablePersistAsyncStorage({
>       AsyncStorage,
>     }),
>   },
>   generateId,
>   supabase,
>   changesSince: 'last-sync',
>   fieldCreatedAt: 'created_at',
>   fieldUpdatedAt: 'updated_at',
>   // Optionally enable soft deletes
>   fieldDeleted: 'deleted',
> })
> 
> export const todos$ = observable(
>   customSynced({
>     supabase,
>     collection: 'todos',
>     select: (from) => from.select('id,counter,text,done,created_at,updated_at,deleted'),
>     actions: ['read', 'create', 'update', 'delete'],
>     realtime: true,
>     // Persist data and pending changes locally
>     persist: {
>       name: 'todos',
>       retrySync: true, // Persist pending changes and retry
>     },
>     retry: {
>       infinite: true, // Retry changes with exponential backoff
>     },
>   })
> )
> ```
> 
> > `syncedSupabase` is the Legend-State sync plugin for Supabase that provides out-of-the-box configuration for `supabase-js`.

---

## 设置数据库架构

使用 [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started) 在本地初始化你的 Supabase 项目：

```bash
supabase init
supabase migrations new init
```

打开 `supabase/migrations` 中新创建的迁移文件并添加以下 SQL 架构：

```sql
create table todos (
  id uuid default gen_random_uuid() primary key,
  counter bigint generated by default as identity,
  text text,
  done boolean default false,
  created_at timestamptz default now(),
  updated_at timestamptz default now(),
  deleted boolean default false -- 软删除所需
);

-- 启用实时功能
alter
  publication supabase_realtime add table todos;

-- Legend-State 辅助函数，用于促进“仅同步差异” (changesSince: 'last-sync') 模式
CREATE OR REPLACE FUNCTION handle_times()
    RETURNS trigger AS
    $$
    BEGIN
    IF (TG_OP = 'INSERT') THEN
        NEW.created_at := now();
        NEW.updated_at := now();
    ELSEIF (TG_OP = 'UPDATE') THEN
        NEW.created_at = OLD.created_at;
        NEW.updated_at := now();
    END IF;
    RETURN NEW;
    END;
    $$ language plpgsql;

CREATE TRIGGER handle_times
    BEFORE INSERT OR UPDATE ON todos
    FOR EACH ROW
EXECUTE PROCEDURE handle_times();
```

关联你的项目并推送数据库迁移：

```bash
supabase link
supabase db push
```

> **Setting Up the Database Schema**
> Initialize your Supabase project locally using the [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started):
> 
> ```bash
> supabase init
> supabase migrations new init
> ```
> 
> Open the newly created migration file in `supabase/migrations` and add the following SQL schema:
> 
> ```sql
> create table todos (
>   id uuid default gen_random_uuid() primary key,
>   counter bigint generated by default as identity,
>   text text,
>   done boolean default false,
>   created_at timestamptz default now(),
>   updated_at timestamptz default now(),
>   deleted boolean default false -- needed for soft deletes
> );
> 
> -- Enable realtime
> alter
>   publication supabase_realtime add table todos;
> 
> -- Legend-State helper to facilitate "Sync only diffs" (changesSince: 'last-sync') mode
> CREATE OR REPLACE FUNCTION handle_times()
>     RETURNS trigger AS
>     $$
>     BEGIN
>     IF (TG_OP = 'INSERT') THEN
>         NEW.created_at := now();
>         NEW.updated_at := now();
>     ELSEIF (TG_OP = 'UPDATE') THEN
>         NEW.created_at = OLD.created_at;
>         NEW.updated_at := now();
>     END IF;
>     RETURN NEW;
>     END;
>     $$ language plpgsql;
> 
> CREATE TRIGGER handle_times
>     BEFORE INSERT OR UPDATE ON todos
>     FOR EACH ROW
> EXECUTE PROCEDURE handle_times();
> ```
> 
> Link your project and push the database migration:
> 
> ```bash
> supabase link
> supabase db push
> ```

---

## 生成 TypeScript 类型

生成 TypeScript 定义，以保持 Supabase 和 Legend-State 之间的端到端类型安全：

```bash
supabase start
supabase gen types --lang=typescript --local > utils/database.types.ts
```

将类型导入并注入到 `utils/SupaLegend.ts` 中：

```typescript
import { createClient } from '@supabase/supabase-js'
import { Database } from './database.types'
// [...]

const supabase = createClient<Database>(
  process.env.EXPO_PUBLIC_SUPABASE_URL,
  process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
)
// [...]
```

> **Generating TypeScript Types**
> Generate TypeScript definitions to maintain end-to-end type safety between Supabase and Legend-State:
> 
> ```bash
> supabase start
> supabase gen types --lang=typescript --local > utils/database.types.ts
> ```
> 
> Import and inject the types into `utils/SupaLegend.ts`:
> 
> ```typescript
> import { createClient } from '@supabase/supabase-js'
> import { Database } from './database.types'
> // [...]
> 
> const supabase = createClient<Database>(
>   process.env.EXPO_PUBLIC_SUPABASE_URL,
>   process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
> )
> // [...]
> ```

---

## 获取数据并订阅实时更新

在组件内部通过 `observer` 包装器消费 `todos$` 可观察对象，以实现优化的渲染：

```tsx
import { observer } from '@legendapp/state/react'
import { todos$ as _todos$ } from './utils/SupaLegend'

const Todos = observer(({ todos$ }: { todos$: typeof _todos$ }) => {
  // 从状态中获取待办事项并订阅更新
  const todos = todos$.get()
  const renderItem = ({ item: todo }: { item: Tables<'todos'> }) => <Todo todo={todo} />
  
  if (todos)
    return <FlatList data={Object.values(todos)} renderItem={renderItem} style={styles.todos} />

  return <></>
})
```

> **Fetching Data and Subscribing to Realtime Updates**
> Consume the `todos$` observable inside your components using the `observer` wrapper for optimized rendering:
> 
> ```tsx
> import { observer } from '@legendapp/state/react'
> import { todos$ as _todos$ } from './utils/SupaLegend'
> 
> const Todos = observer(({ todos$ }: { todos$: typeof _todos$ }) => {
>   // Get the todos from the state and subscribe to updates
>   const todos = todos$.get()
>   const renderItem = ({ item: todo }: { item: Tables<'todos'> }) => <Todo todo={todo} />
>   
>   if (todos)
>     return <FlatList data={Object.values(todos)} renderItem={renderItem} style={styles.todos} />
> 
>   return <></>
> })
> ```

---

## 插入和更新数据

更新你的 `utils/SupaLegend.ts` 以通过 `uuid` 和 `react-native-get-random-values` 支持本地 ID 生成：

```typescript
// [...]
import 'react-native-get-random-values'
import { v4 as uuidv4 } from 'uuid'
// [...]

// 提供一个在本地生成 id 的函数
const generateId = () => uuidv4()

export function addTodo(text: string) {
  const id = generateId()
  // 通过 id 作为键添加到 todos$ 可观察对象中，以在 Supabase 中触发创建
  todos$[id].assign({
    id,
    text,
  })
}

export function toggleDone(id: string) {
  todos$[id].done.set((prev) => !prev)
}
```

在 `App.tsx` 中连接处理函数：

```tsx
import { useState } from 'react'
import { FlatList, StyleSheet, Text, TextInput, TouchableOpacity } from 'react-native'
// [...]
import { observer } from '@legendapp/state/react'
import { addTodo, todos$ as _todos$, toggleDone } from './utils/SupaLegend'
// [...]

const NOT_DONE_ICON = String.fromCodePoint(0x1f7e0)
const DONE_ICON = String.fromCodePoint(0x2705)

const NewTodo = () => {
  const [text, setText] = useState('')
  const handleSubmitEditing = ({ nativeEvent: { text } }) => {
    setText('')
    addTodo(text)
  }
  return (
    <TextInput
      value={text}
      onChangeText={(text) => setText(text)}
      onSubmitEditing={handleSubmitEditing}
      placeholder="今天想做点什么？"
      style={styles.input}
    />
  )
}

const Todo = ({ todo }: { todo: Tables<'todos'> }) => {
  const handlePress = () => {
    toggleDone(todo.id)
  }
  return (
    <TouchableOpacity
      key={todo.id}
      onPress={handlePress}
      style={[styles.todo, todo.done ? styles.done : null]}
    >
      <Text style={styles.todoText}>
        {todo.done ? DONE_ICON : NOT_DONE_ICON} {todo.text}
      </Text>
    </TouchableOpacity>
  )
}
```

> **Inserting and Updating Data**
> Update your `utils/SupaLegend.ts` to support local ID generation via `uuid` and `react-native-get-random-values`:
> 
> ```typescript
> // [...]
> import 'react-native-get-random-values'
> import { v4 as uuidv4 } from 'uuid'
> // [...]
> 
> // Provide a function to generate ids locally
> const generateId = () => uuidv4()
> 
> export function addTodo(text: string) {
>   const id = generateId()
>   // Add keyed by id to the todos$ observable to trigger a create in Supabase
>   todos$[id].assign({
>     id,
>     text,
>   })
> }
> 
> export function toggleDone(id: string) {
>   todos$[id].done.set((prev) => !prev)
> }
> ```
> 
> Wire up the handlers in `App.tsx`:
> 
> ```tsx
> import { useState } from 'react'
> import { FlatList, StyleSheet, Text, TextInput, TouchableOpacity } from 'react-native'
> // [...]
> import { observer } from '@legendapp/state/react'
> import { addTodo, todos$ as _todos$, toggleDone } from './utils/SupaLegend'
> // [...]
> 
> const NOT_DONE_ICON = String.fromCodePoint(0x1f7e0)
> const DONE_ICON = String.fromCodePoint(0x2705)
> 
> const NewTodo = () => {
>   const [text, setText] = useState('')
>   const handleSubmitEditing = ({ nativeEvent: { text } }) => {
>     setText('')
>     addTodo(text)
>   }
>   return (
>     <TextInput
>       value={text}
>       onChangeText={(text) => setText(text)}
>       onSubmitEditing={handleSubmitEditing}
>       placeholder="What do you want to do today?"
>       style={styles.input}
>     />
>   )
> }
> 
> const Todo = ({ todo }: { todo: Tables<'todos'> }) => {
>   const handlePress = () => {
>     toggleDone(todo.id)
>   }
>   return (
>     <TouchableOpacity
>       key={todo.id}
>       onPress={handlePress}
>       style={[styles.todo, todo.done ? styles.done : null]}
>     >
>       <Text style={styles.todoText}>
>         {todo.done ? DONE_ICON : NOT_DONE_ICON} {todo.text}
>       </Text>
>     </TouchableOpacity>
>   )
> }
> ```

---

## 下一步：添加身份验证

由于 Legend-State 依赖于 `supabase-js`，你可以轻松集成 [Supabase Auth](https://supabase.com/docs/guides/auth) 和 [行级安全性 (RLS)](https://supabase.com/docs/guides/database/postgres/row-level-security) 来保护用户数据。

请参考 [Expo 用户管理教程](https://supabase.com/docs/guides/getting-started/tutorials/with-expo-react-native) 获取完整的演练。

> **Up Next: Adding Authentication**
> Since Legend-State relies on `supabase-js`, you can easily integrate [Supabase Auth](https://supabase.com/docs/guides/auth) and [Row Level Security (RLS)](https://supabase.com/docs/guides/database/postgres/row-level-security) to secure user data. 
> 
> Refer to the [Expo User Management Tutorial](https://supabase.com/docs/guides/getting-started/tutorials/with-expo-react-native) for a complete walkthrough.

---

## 结论

Legend-State 和 Supabase 为在网页和移动平台上构建离线优先、实时应用程序提供了世界级的开发体验。

要了解更多信息，请浏览官方 [Legend-State 文档](https://legendapp.com/open-source/state/v3/) 并在 Twitter 上关注 [@jmeistrich](https://twitter.com/jmeistrich)。

> **Conclusion**
> Legend-State and Supabase provide a world-class developer experience for building offline-first, real-time applications across web and mobile platforms. 
> 
> To learn more, explore the official [Legend-State Documentation](https://legendapp.com/open-source/state/v3/) and follow [@jmeistrich](https://twitter.com/jmeistrich) on Twitter.

---

## 更多 Supabase 资源

- [Expo 用户管理教程](https://supabase.com/docs/guides/getting-started/tutorials/with-expo-react-native)
- [React Native 身份验证](https://supabase.com/blog/react-native-authentication)
- [React Native 文件上传](https://supabase.com/blog/react-native-storage)

> **More Supabase Resources**
> - [Expo User Management Tutorial](https://supabase.com/docs/guides/getting-started/tutorials/with-expo-react-native)
> - [React Native Authentication](https://supabase.com/blog/react-native-authentication)
> - [React Native File Upload](https://supabase.com/blog/react-native-storage)