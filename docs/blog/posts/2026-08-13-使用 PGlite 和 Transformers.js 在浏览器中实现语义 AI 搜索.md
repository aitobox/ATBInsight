---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-13
hide:
- navigation
tags:
- PGlite
- Transformers.js
- 向量搜索
- 浏览器AI
- pgvector
title: 使用 PGlite 和 Transformers.js 在浏览器中实现语义 AI 搜索
---
### 文章背景与核心概要
本指南探讨了如何构建一个完全本地化、运行在浏览器中的语义搜索引擎。通过将 **PGlite**（用于在 IndexedDB 中运行本地 Postgres 存储）、**pgvector**（用于相似性搜索）以及 **Transformers.js**（用于生成嵌入向量）结合起来，你可以打造出高性能的搜索体验（例如商品推荐），并且完全不需要服务器进行任何往返通信。

这种纯客户端的架构不仅保护了用户隐私，还能在无网络连接的情况下离线运行。文章详细介绍了从安装依赖、配置数据库架构、向数据库填充种子数据，到利用 Web Worker 运行 Transformers.js 模型生成嵌入向量并执行内积搜索的全套完整流程。

---

## Install the Dependencies
To get started, initialize a React application and install the necessary packages:

> 安装依赖
> 要开始使用，请初始化一个 React 应用程序并安装必要的软件包：

```bash
npm create vite@latest
npm install @electric-sql/pglite @huggingface/transformers
```

## Create the Database Schema
Create a `utils/db.js` file to manage your PGlite instance and define the schema. We use a singleton pattern to ensure only one database instance exists.

> 创建数据库架构
> 创建一个 `utils/db.js` 文件来管理你的 PGlite 实例并定义架构。我们使用单例模式来确保只存在一个数据库实例。

```javascript
import { PGlite } from '@electric-sql/pglite'
import { vector } from '@electric-sql/pglite/vector'

let dbInstance
export async function getDB() {
  if (dbInstance) return dbInstance
  const metaDb = new PGlite('idb://supa-semantic-search', {
    extensions: { vector },
  })
  await metaDb.waitReady
  dbInstance = metaDb
  return metaDb
}

export const initSchema = async (db) => {
  return await db.exec(`
    create extension if not exists vector;
    create table if not exists embeddings (
      id bigint primary key generated always as identity,
      content text not null,
      embedding vector (384)
    );
    create index on embeddings using hnsw (embedding vector_ip_ops);
  `)
}
```

In your `App.jsx`, initialize the database and schema:

> 在你的 `App.jsx` 中，初始化数据库和架构：

```javascript
import { getDB, initSchema, countRows } from './utils/db'
// ... inside your component
useEffect(() => {
  const setup = async () => {
    db.current = await getDB()
    await initSchema(db.current)
    // ... seed logic
  }
  setup()
}, [])
```

## Seed the Database
For prototyping, you can manually seed your database. Add this `seedDb` method to `utils/db.js`:

> 填充数据库种子数据
> 对于原型开发，你可以手动向数据库中填充种子数据。将此 `seedDb` 方法添加到 `utils/db.js` 中：

```javascript
export const seedDb = async (db) => {
  return await db.exec(`
    insert into embeddings (content, embedding) values
      ('Bed', '[...]'),
      ('Car', '[...]'),
      ('Train', '[...]'),
      ('Cat', '[...]'),
      ('Dog', '[...]'),
      ('Apple', '[...]'),
      ('Boat', '[...]'),
      ('Mouse', '[...]'),
      ('Chair', '[...]'),
      ('Tomato', '[...]'),
      ('Desk', '[...]'),
      ('Banana', '[...]')
  `)
}
```

## Define the Inner Product Search
Use `pgvector` to perform an inner product search. This is highly efficient for finding similar items.

> 定义内积搜索
> 使用 `pgvector` 执行内积搜索。这对于查找相似项目非常高效。

```javascript
export const search = async (db, embedding, match_threshold = 0.8, limit = 3) => {
  const res = await db.query(
    `select * from embeddings
     where embeddings.embedding <#> $1 < $2
     order by embeddings.embedding <#> $1
     limit $3;`,
    [JSON.stringify(embedding), -Number(match_threshold), Number(limit)]
  )
  return res.rows
}
```

## Create Embeddings with Web Workers
To keep the UI responsive, run the `Transformers.js` pipeline in a Web Worker:

> 使用 Web Workers 创建嵌入向量
> 为了保持 UI 的响应速度，请在 Web Worker 中运行 `Transformers.js` 管道：

```javascript
// worker.js
import { pipeline } from '@huggingface/transformers'

class PipelineSingleton {
  static task = 'feature-extraction'
  static model = 'Supabase/gte-small'
  static instance = null
  static async getInstance(progress_callback = null) {
    if (this.instance === null) {
      this.instance = pipeline(this.task, this.model, {
        progress_callback,
        dtype: 'fp32',
        device: !!navigator.gpu ? 'webgpu' : 'wasm',
      })
    }
    return this.instance
  }
}

self.addEventListener('message', async (event) => {
  let classifier = await PipelineSingleton.getInstance()
  let output = await classifier(event.data.text, { pooling: 'mean', normalize: true })
  self.postMessage({ status: 'complete', embedding: Array.from(output.data) })
})
```

## Perform the Search
In your main `App.jsx`, listen for the `complete` status from the worker to trigger the database search:

> 执行搜索
> 在你的主 `App.jsx` 中，监听来自 worker 的 `complete` 状态以触发数据库搜索：

```javascript
case 'complete':
  const searchResults = await search(db.current, e.data.embedding)
  setResult(searchResults.map((x) => x.content))
  break
```

---

### More Supabase Resources
* [Learn how we've built database.build](https://database.build)
* [Learn about running LLMs locally with Mozilla Llamafile](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions)
* [Learn how to build semantic search with Supabase](https://supabase.com/docs/guides/ai/semantic-search)

> 更多 Supabase 资源
> * [了解我们是如何构建 database.build 的](https://database.build)
> * [了解如何使用 Mozilla Llamafile 在本地运行大语言模型](https://supabase.com/blog/mozilla-llamafile-in-supabase-edge-functions)
> * [了解如何使用 Supabase 构建语义搜索](https://supabase.com/docs/guides/ai/semantic-search)