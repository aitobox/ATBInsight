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
- Edge Functions
- WebSocket
- 边缘计算
- 后端开发
title: Supabase Edge Functions 重磅更新：引入后台任务、临时存储与 WebSocket 支持
---
### 文章背景与核心概要
Supabase 近期在其边缘函数（Edge Functions）中正式推出了三项重大功能，旨在突破传统边缘计算在运行时间、本地文件处理以及实时双向通信方面的限制。这些新特性包括用于执行长时间运行任务的后台任务（Background Tasks）、用于高效处理临时中间文件的 `/tmp` 临时存储（Ephemeral Storage），以及支持直接在边缘函数中建立安全入站与出站连接的 WebSockets。

这三项功能的推出，极大地扩展了 Supabase Edge Functions 的应用边界。开发者现在不仅可以编写简单的 API 路由，还能够处理诸如大文件解压上传、调用 OpenAI 实时 API（Realtime API）等更为复杂的业务逻辑。配合免费层高达 150 秒、付费层高达 400 秒的执行限额，Supabase 正在让边缘函数向功能更全、性能更强的后端全能计算单元演进。

---

## Supabase Edge Functions: Introducing Background Tasks, Ephemeral Storage, and WebSockets

> Supabase Edge Functions: Introducing Background Tasks, Ephemeral Storage, and WebSockets

## Summary

> Supabase has officially announced three major features for its Edge Functions, available immediately across all projects:
> 
> 1. **Background Tasks:** Execute long-running workloads (up to 150 seconds for free tiers and 400 seconds for paid plans) without terminating the function prematurely, utilizing the new `EdgeRuntime.waitUntil` method.
> 2. **Ephemeral Storage:** Safely read and write temporary intermediate files and results using the `/tmp` directory.
> 3. **WebSockets:** Establish both inbound (server) and outbound (client) WebSocket connections directly inside Edge Functions to handle real-time communications securely.

---

## 背景任务

有时，后端逻辑不仅需要对传入的请求做出即时响应，还需要完成诸如处理批量文件、将结果上传至 Supabase Storage 或读取数据库行以生成嵌入向量等工作。

借助于**后台任务（Background Tasks）**，运行这些工作负载变得异常简单：
* **`EdgeRuntime.waitUntil(promise)`**：接收一个 Promise，确保边缘函数工作线程（worker）在任务完成之前保持活跃状态。
* **执行限制**：免费项目可运行长达 **150 秒（2分30秒）** 的任务，而付费项目最高可达 **400 秒（6分40秒）**。
* **生命周期事件**：监听 `beforeunload` 事件，以便在函数工作线程终止前捕获清理步骤或最终日志。

在 [后台任务指南](/docs/guides/functions/background-tasks) 中阅读更多详细信息。

> ## Background Tasks
> 
> Sometimes backend logic needs to do more than just respond instantly to an incoming request—such as processing batch files, uploading results to Supabase Storage, or reading database rows to generate embeddings. 
> 
> With **Background Tasks**, running these workloads is simple:
> * **`EdgeRuntime.waitUntil(promise)`**: Accepts a promise to ensure the Edge Function worker stays active until the task completes.
> * **Execution Limits**: Free projects can run tasks for up to **150 seconds (2m 30s)**, while paid projects get up to **400 seconds (6m 40s)**.
> * **Lifecycle Events**: Listen to the `beforeunload` event to capture clean-up steps or final logging right before the function worker terminates.
> 
> Read more details in the [Background Tasks Guide](/docs/guides/functions/background-tasks).

---

## 临时存储

边缘函数的调用现在可以通过 `/tmp` 目录直接访问临时存储。这在结合后台任务进行读取和写入临时中间文件时特别有用。

阅读关于如何访问 [临时存储](/docs/guides/functions/ephemeral-storage) 的指南。

> ## Ephemeral Storage
> 
> Edge Function invocations now have direct access to ephemeral storage via the `/tmp` directory. This is particularly useful alongside background tasks for reading and writing intermediate files.
> 
> Read the guide on how to access [Ephemeral Storage](/docs/guides/functions/ephemeral-storage).

### 示例：解压 Zip 文件并上传至 Supabase Storage

想象一下，你正在构建一个相册应用，用户可以上传包含多张图片的 `.zip` 压缩包。

> ### Example: Extracting a Zip File and Uploading to Supabase Storage
> 
> Imagine building a photo album application where users upload a `.zip` archive containing multiple images. 

#### 1. 流式处理方法（内存密集型）
虽然直接流式传输适用于小型压缩包，但当尝试处理大于 100MB 的 zip 文件时，由于会将所有文件同时保留在内存中，会触发内存限制错误：

> #### 1. The Streaming Approach (Memory-Intensive)
> While streaming directly can work for small archives, attempting to process zip files larger than 100MB will trigger memory limit errors because it holds all files simultaneously in memory:

```typescript
import { ZipReaderStream } from 'https://deno.land/x/zipjs/index.js'
import { createClient } from 'jsr:@supabase/supabase-js@2'

const supabase = createClient(
  Deno.env.get('SUPABASE_URL'),
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')
)

Deno.serve(async (req) => {
  const uploadId = crypto.randomUUID()

  const { error } = await supabase.storage.createBucket(uploadId, {
    public: false,
  })

  for await (const entry of await req.body.pipeThrough(new ZipReaderStream())) {
    // write file to Supabase Storage
    const { error } = await supabase.storage
      .from(uploadId)
      .upload(entry.filename, entry.readable, {})

    console.log('uploaded', entry.filename)
  }

  return new Response(
    JSON.stringify({
      uploadId,
    }),
    {
      headers: {
        'content-type': 'application/json',
      },
    }
  )
})
```

#### 2. 优化方法（使用临时存储与后台任务）
通过将传入的 zip 文件直接写入 `/tmp` 并利用后台任务，我们只需要在需要时将压缩包的部分内容读入内存：

> #### 2. The Optimized Approach (Using Ephemeral Storage & Background Tasks)
> By writing the incoming zip file directly to `/tmp` and utilizing a background task, we only read parts of the archive into memory as needed:

```typescript
import { BlobWriter, ZipReader, ZipReaderStream } from 'https://deno.land/x/zipjs/index.js'

import { createClient } from 'jsr:@supabase/supabase-js@2'

const supabase = createClient(
  Deno.env.get('SUPABASE_URL'),
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')
)

let numFilesUploaded = 0

async function processZipFile(uploadId, filepath) {
  const file = await Deno.open(filepath, { read: true })
  const zipReader = new ZipReader(file.readable)
  const entries = await zipReader.getEntries()

  await supabase.storage.createBucket(uploadId, {
    public: false,
  })

  await Promise.all(
    entries.map(async (entry) => {
      // read file entry
      const blobWriter = new BlobWriter()
      const blob = await entry.getData(blobWriter)

      if (entry.directory) {
        return
      }

      // write file to Supabase Storage
      await supabase.storage.from(uploadId).upload(entry.filename, blob, {})

      numFilesUploaded += 1
      console.log('uploaded', entry.filename)
    })
  )

  await zipReader.close()
}

// you can add a `beforeunload` event listener to be notified
// when Function Worker is about to terminate.
// use this to do any logging, save states.
globalThis.addEventListener('beforeunload', (ev) => {
  console.log('function about to terminate: ', ev.detail.reason)
  console.log('number of files uploaded: ', numFilesUploaded)
})

async function writeZipFile(filepath, stream) {
  Deno.writeFile(filepath, stream)
}

Deno.serve(async (req) => {
  const uploadId = crypto.randomUUID()
  await writeZipFile('/tmp/' + uploadId, req.body)

  // process zip file in a background task
  // calling EdgeRuntime.waitUntil() would ensure
  // function worker wouldn't exit until the promise is completed.
  EdgeRuntime.waitUntil(processZipFile(uploadId, '/tmp/' + uploadId))

  return new Response(
    JSON.stringify({
      uploadId,
    }),
    {
      headers: {
        'content-type': 'application/json',
      },
    }
  )
})
```

---

## WebSockets

边缘函数现在支持建立**入站（服务器）**和**出站（客户端）** WebSocket 连接，这在无需外部基础设施的情况下开启了全新的交互范例。

> ## WebSockets
> 
> Edge Functions now support establishing both **inbound (server)** and **outbound (client)** WebSocket connections, unlocking entirely new interactive paradigms without external infrastructure.

### 示例：构建指向 OpenAI 实时 API 的认证中继

OpenAI 的 [实时 API (Realtime API)](https://openai.com/index/introducing-the-realtime-api/) 使用了 WebSockets。如果完全在客户端实现这一点，会暴露你的私有 OpenAI API 密钥，因此 OpenAI [建议](https://platform.openai.com/docs/guides/realtime/overview?text-generation-quickstart-example=audio) 构建一个安全的服务器代理。

借助 Supabase Edge Functions 和 WebSockets，你可以安全地代理此连接并集成 [Supabase Auth](https://supabase.com/docs/guides/auth) 来验证用户身份，保护你的 API 免遭滥用：

> ### Example: Building an Authenticated Relay to the OpenAI Realtime API
> 
> OpenAI's [Realtime API](https://openai.com/index/introducing-the-realtime-api/) uses WebSockets. Implementing this strictly client-side exposes your secret OpenAI API keys, so OpenAI [recommends](https://platform.openai.com/docs/guides/realtime/overview?text-generation-quickstart-example=audio) building a secure server proxy.
> 
> With Supabase Edge Functions and WebSockets, you can safely proxy this connection and integrate [Supabase Auth](https://supabase.com/docs/guides/auth) to authenticate users and protect your API usage from abuse:

```typescript
import { createClient } from 'jsr:@supabase/supabase-js@2'

const supabase = createClient(
  Deno.env.get('SUPABASE_URL'),
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')
)
const OPENAI_API_KEY = Deno.env.get('OPENAI_API_KEY')

Deno.serve(async (req) => {
  const upgrade = req.headers.get('upgrade') || ''

  if (upgrade.toLowerCase() != 'websocket') {
    return new Response("request isn't trying to upgrade to websocket.")
  }

  // WebSocket browser clients does not support sending custom headers.
  // We have to use the URL query params to provide user's JWT.
  // Please be aware query params may be logged in some logging systems.
  const url = new URL(req.url)
  const jwt = url.searchParams.get('jwt')
  if (!jwt) {
    console.error('Auth token not provided')
    return new Response('Auth token not provided', { status: 403 })
  }
  const { error, data } = await supabase.auth.getUser(jwt)
  if (error) {
    console.error(error)
    return new Response('Invalid token provided', { status: 403 })
  }
  if (!data.user) {
    console.error('user is not authenticated')
    return new Response('User is not authenticated', { status: 403 })
  }

  const { socket, response } = Deno.upgradeWebSocket(req)

  socket.onopen = () => {
    // initiate an outbound WebSocket connection to OpenAI
    const url = 'wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview-2024-10-01'

    // openai-insecure-api-key isn't a problem since this code runs in an Edge Function
    const openaiWS = new WebSocket(url, [
      'realtime',
      `openai-insecure-api-key.${OPENAI_API_KEY}`,
      'openai-beta.realtime-v1',
    ])

    openaiWS.onopen = () => {
      console.log('Connected to OpenAI server.')

      socket.onmessage = (e) => {
        console.log('socket message:', e.data)
        // only send the message if openAI ws is open
        if (openaiWS.readyState === 1) {
          openaiWS.send(e.data)
        } else {
          socket.send(
            JSON.stringify({
              type: 'error',
              msg: 'openAI connection not ready',
            })
          )
        }
      }
    }

    openaiWS.onmessage = (e) => {
      console.log(e.data)
      socket.send(e.data)
    }

    openaiWS.onerror = (e) => console.log('OpenAI error: ', e.message)
    openaiWS.onclose = (e) => console.log('OpenAI session closed')
  }

  socket.onerror = (e) => console.log('socket errored:', e.message)
  socket.onclose = () => console.log('socket closed')

  return response // 101 (Switching Protocols)
})
```

---

## 性能与稳定性

在过去的几个月中，Supabase 针对边缘函数推出了多项[性能、稳定性](https://supabase.com/blog/edge-functions-faster-smaller)以及[开发者体验（DX）的改进](https://github.com/orgs/supabase/discussions/30307)。虽然这些升级通常在底层进行，但它们为今天发布的新功能奠定了至关重要的基础。

> ## Performance and Stability
> 
> Over the past few months, Supabase has rolled out numerous [performance, stability,](https://supabase.com/blog/edge-functions-faster-smaller) and [DX improvements](https://github.com/orgs/supabase/discussions/30307) to Edge Functions. While these upgrades often occur under the hood, they form the critical foundation enabling today's feature releases.

---

## 未来展望

2025 年的路线图令人期待，其核心重点是引入可定制的计算限制（内存、CPU 和执行持续时间）。请密切关注本周发布的更多更新！

> ## What's Next?
> 
> An exciting roadmap is planned for 2025, with a primary focus on introducing customizable compute limits (memory, CPU, and execution duration). Stay tuned for more updates throughout the week!