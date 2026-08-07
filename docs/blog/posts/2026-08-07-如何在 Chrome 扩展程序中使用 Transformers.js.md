---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-07
hide:
- navigation
tags:
- Chrome扩展
- Transformers.js
- 本地大模型
- WebGPU
- 插件开发
title: 如何在 Chrome 扩展程序中使用 Transformers.js
---
### 文章背景与核心概要

随着端侧大模型（Edge AI）和 WebGPU 技术的成熟，开发者无需依赖昂贵的云端 API，即可在浏览器内部直接运行复杂的本地 AI 模型。本文基于开源项目 Transformers.js Gemma 4 浏览器助手（Gemma 4 Browser Assistant），深入探讨了如何在 Manifest V3 (MV3) 约束下，利用 **Transformers.js** 在 Chrome 扩展程序中完美运行本地 AI 模型。

文章从 Chrome 扩展程序的架构设计切入，详细剖析了后台 Service Worker、侧边栏聊天 UI 以及内容脚本（Content Script）之间的职责分离与消息通信机制。同时，核心内容还涵盖了模型下载与缓存管理、基于 WebGPU 的推理生命周期、工具调用（Tool-calling）循环的实现方式，以及跨上下文的数据持久化策略。对于希望构建高性能、零隐私泄漏且具备复杂浏览器自动化能力的 AI 插件开发者而言，这是一份极具参考价值的架构指南。

---

## 谁适合阅读本文 (Who This Is For)

本指南专为希望在 Manifest V3 约束下，于 Chrome 扩展程序中使用 Transformers.js 运行本地 AI 功能的开发者而写。

读完本文后，你将掌握该项目所采用的核心架构：一个托管模型的后台 Service Worker、一个侧边栏聊天 UI，以及一个用于页面级操作的内容脚本。

> This guide is for developers who want to run local AI features in a Chrome extension with Transformers.js under Manifest V3 constraints.
>
> By the end, you will have the same architecture used in this project: a background service worker that hosts models, a side panel chat UI, and a content script for page-level actions.

---

## 我们将构建什么 (What We Will Build)

在本指南中，我们将参考已发布的扩展程序并以开源代码库为实现蓝图，重构 **Transformers.js Gemma 4 浏览器助手** 的核心架构。

* **线上扩展程序：** [Chrome Web Store](https://chromewebstore.google.com/detail/transformerjs-gemma-4-bro/dhaknnnkcdkjhcclchmnfdhddoehoool)
* **源码地址：** [github.com/nico-martin/gemma4-browser-extension](https://github.com/nico-martin/gemma4-browser-extension)
* **最终成果：** 一个后台托管的 Transformers.js 引擎、一个侧边栏聊天 UI，以及用于页面提取和高亮显示的内容脚本。

> In this guide, we will recreate the core architecture of **Transformers.js Gemma 4 Browser Assistant**, using the published extension as a reference and the open-source codebase as the implementation map.
>
> * **Live extension:** [Chrome Web Store](https://chromewebstore.google.com/detail/transformerjs-gemma-4-bro/dhaknnnkcdkjhcclchmnfdhddoehoool)
> * **Source code:** [github.com/nico-martin/gemma4-browser-extension](https://github.com/nico-martin/gemma4-browser-extension)
> * **End result:** A background-hosted Transformers.js engine, a side panel chat UI, and a content script for page extraction and highlighting.

---

## 1. Chrome 扩展程序架构 (MV3)

在深入探讨之前，先做个简要说明：本文不会深入讨论 React UI 层或 Vite 构建配置。这里的重点是高层架构决策：每个 Chrome 运行环境中运行什么，以及这些部分如何进行编排。

如果你对 Manifest V3 还不太了解，请先阅读这篇简短的概述：[什么是 Manifest V3？](https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3)。

> Before diving in, a quick scope note: I will not go deep on the React UI layer or Vite build configuration. The focus here is the high-level architecture decisions: what runs in each Chrome runtime and how those pieces are orchestrated.
>
> If Manifest V3 is new to you, read this short overview first: [What is Manifest V3?](https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3).

### 1.1 运行上下文与入口点

在 MV3 中，你的架构始于 [`public/manifest.json`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/public/manifest.json)。该项目定义了三个入口点：

* `background.service_worker = background.js`，构建自 [`src/background/background.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/background.ts)。
* `side_panel.default_path = sidebar.html`，构建自 [`src/sidebar/index.html`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/sidebar/index.html)。
* `content_scripts[].js = content.js`，带有 `matches: http(s)://*/*` 和 `run_at: document_idle`，构建自 [`src/content/content.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/content/content.ts)。

后台 Service Worker 还通过 `chrome.action.onClicked` 处理点击事件，为活动标签页打开侧边栏。你也可以使用 `action.default_popup` 定义弹窗以实现快速操作。本项目使用侧边栏进行持续聊天，但编排模式保持不变。

> In MV3, your architecture starts in [`public/manifest.json`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/public/manifest.json). This project defines three entry points:
>
> * `background.service_worker = background.js`, built from [`src/background/background.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/background.ts).
> * `side_panel.default_path = sidebar.html`, built from [`src/sidebar/index.html`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/sidebar/index.html).
> * `content_scripts[].js = content.js` with `matches: http(s)://*/*` and `run_at: document_idle`, built from [`src/content/content.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/content/content.ts).
>
> The background service worker also handles `chrome.action.onClicked` to open the side panel for the active tab. A popup can also be defined with `action.default_popup` for quick actions. This project uses a side panel for persistent chat, but the orchestration pattern remains identical.

### 1.2 各部分运行位置

核心设计决策是将繁重的编排任务放在后台，保持 UI 和页面逻辑轻量化。

* **后台 (Background)** ([`src/background/background.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/background.ts)) 是控制平面：负责代理生命周期、模型初始化、工具执行以及特征提取等共享服务。
* **侧边栏 (Side panel)** ([`src/sidebar/*`](https://github.com/nico-martin/gemma4-browser-extension/tree/main/src/sidebar)) 是交互层：负责聊天输入/输出、流式更新和设置控制。
* **内容脚本 (Content script)** ([`src/content/content.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/content/content.ts)) 是页面桥梁：负责 DOM 提取和高亮操作。

对话历史存储在后台（`Agent.chatMessages`）。UI 发送诸如 `AGENT_GENERATE_TEXT` 的事件，后台追加消息、运行推理，并向侧边栏发射 `MESSAGES_UPDATE` 事件。这可以防止重复加载模型、保持 UI 的响应速度，并遵守 Chrome 关于 DOM 访问的安全边界。

> The key design decision is to keep heavy orchestration in the background and keep UI/page logic thin.
>
> * **Background** ([`src/background/background.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/background.ts)) is the control plane: agent lifecycle, model initialization, tool execution, and shared services like feature extraction.
> * **Side panel** ([`src/sidebar/*`](https://github.com/nico-martin/gemma4-browser-extension/tree/main/src/sidebar)) is the interaction layer: chat input/output, streaming updates, and setup controls.
> * **Content script** ([`src/content/content.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/content/content.ts)) is the page bridge: DOM extraction and highlight actions.
>
> Conversation history lives in the background (`Agent.chatMessages`). The UI sends events like `AGENT_GENERATE_TEXT`, the background appends the message, runs inference, and emits `MESSAGES_UPDATE` back to the side panel. This prevents duplicate model loads, keeps the UI responsive, and respects Chrome's security boundaries regarding DOM access.

### 1.3 消息通信契约

一旦运行上下文被分离，消息传递就成了支柱。所有消息都通过 [`src/shared/types.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/shared/types.ts) 中的枚举进行类型约束。

* **侧边栏 -> 后台 (`BackgroundTasks`)：**
  * `CHECK_MODELS`, `INITIALIZE_MODELS`
  * `AGENT_INITIALIZE`, `AGENT_GENERATE_TEXT`, `AGENT_GET_MESSAGES`, `AGENT_CLEAR`
  * `EXTRACT_FEATURES`
* **后台 -> 侧边栏 (`BackgroundMessages`)：**
  * `DOWNLOAD_PROGRESS`, `MESSAGES_UPDATE`
* **后台 -> 内容脚本 (`ContentTasks`)：**
  * `EXTRACT_PAGE_DATA`, `HIGHLIGHT_ELEMENTS`, `CLEAR_HIGHLIGHTS`

**典型请求流程：**
1. 侧边栏发送 `AGENT_GENERATE_TEXT`。
2. 后台将其追加到 `Agent.chatMessages` 并运行模型/工具步骤。
3. 后台发射 `MESSAGES_UPDATE`。
4. 侧边栏根据更新后的消息列表重新渲染。

> Once runtimes are separated, messaging becomes the backbone. All messages are typed through enums in [`src/shared/types.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/shared/types.ts).
>
> * **Side panel -> Background (`BackgroundTasks`):**
>   * `CHECK_MODELS`, `INITIALIZE_MODELS`
>   * `AGENT_INITIALIZE`, `AGENT_GENERATE_TEXT`, `AGENT_GET_MESSAGES`, `AGENT_CLEAR`
>   * `EXTRACT_FEATURES`
> * **Background -> Side panel (`BackgroundMessages`):**
>   * `DOWNLOAD_PROGRESS`, `MESSAGES_UPDATE`
> * **Background -> Content (`ContentTasks`):**
>   * `EXTRACT_PAGE_DATA`, `HIGHLIGHT_ELEMENTS`, `CLEAR_HIGHLIGHTS`
>
> **Typical Request Flow:**
> 1. Side panel sends `AGENT_GENERATE_TEXT`.
> 2. Background appends to `Agent.chatMessages` and runs model/tool steps.
> 3. Background emits `MESSAGES_UPDATE`.
> 4. Side panel re-renders from the updated message list.

---

## 2. Transformers.js 集成详情

### 2.1 模型与职责

在 [`src/shared/constants.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/shared/constants.ts) 中，该扩展程序使用了两种模型角色：

* **文本生成 / 大语言模型 (TextGeneration / LLM)：** [`onnx-community/gemma-4-E2B-it-ONNX`](https://huggingface.co/onnx-community/gemma-4-E2B-it-ONNX) (`text-generation`, `q4f16`)
* **向量嵌入 (VectorEmbeddings)：** [`onnx-community/all-MiniLM-L6-v2-ONNX`](https://huggingface.co/onnx-community/all-MiniLM-L6-v2-ONNX) (`feature-extraction`, `fp32`)

Gemma 4 负责推理和工具决策，而 MiniLM 则为 `ask_website` 和 `find_history` 中的语义相似度搜索生成向量嵌入。

> In [`src/shared/constants.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/shared/constants.ts), this extension uses two model roles:
>
> * **TextGeneration / LLM:** [`onnx-community/gemma-4-E2B-it-ONNX`](https://huggingface.co/onnx-community/gemma-4-E2B-it-ONNX) (`text-generation`, `q4f16`)
> * **VectorEmbeddings:** [`onnx-community/all-MiniLM-L6-v2-ONNX`](https://huggingface.co/onnx-community/all-MiniLM-L6-v2-ONNX) (`feature-extraction`, `fp32`)
>
> Gemma 4 handles reasoning and tool decisions, while MiniLM generates vector embeddings for semantic similarity search in `ask_website` and `find_history`.

### 2.2 推理运行位置

所有推理都在后台运行 ([`src/background/background.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/background.ts))：
* 通过 `pipeline("text-generation", ...)` 进行文本生成，并通过 `DynamicCache` 类启用一致的 KV 缓存。
* 通过 `pipeline("feature-extraction", ...)` 结合向量归一化来生成嵌入。

这确保了所有标签页共享单个模型宿主，减少了内存开销，并将产物缓存在扩展程序来源下 (`chrome-extension://<extension-id>`)。*注意：MV3 Service Worker 可能会被挂起和重启，因此必须将运行时状态视为可恢复的，并在必要时重新初始化。*

> All inference runs in the background ([`src/background/background.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/background.ts)):
> * Text generation via `pipeline("text-generation", ...)` with consistent KV Caching enabled via the `DynamicCache` class.
> * Embeddings via `pipeline("feature-extraction", ...)` combined with vector normalization.
>
> This ensures a single model host for all tabs, reduces memory overhead, and caches artifacts under the extension origin (`chrome-extension://<extension-id>`). *Note: MV3 service workers can be suspended and restarted, so runtime state must be treated as recoverable and re-initialized when necessary.*

### 2.3 下载与缓存生命周期

模型的生命周期是显式的：
* `CHECK_MODELS` 检查缓存的资源并估算剩余的下载大小。
* `INITIALIZE_MODELS` 下载/初始化模型，向 UI 发射 `DOWNLOAD_PROGRESS` 更新。
* 设置完成后重用长生命周期实例：
  * [`src/background/agent/Agent.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/agent/Agent.ts) 中的生成管道
  * [`src/background/utils/FeatureExtractor.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/utils/FeatureExtractor.ts) 中的嵌入管道

[`public/manifest.json`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/public/manifest.json) 中的权限请求了 `sidePanel`、`storage`、`scripting`、`tabs` 以及针对 `http(s)://*/*` 的 `host_permissions`。仅请求绝对必要的权限，以维护用户信任并简化 Chrome 网上应用店的审核。

> The model lifecycle is explicit:
> * `CHECK_MODELS` inspects cached assets and estimates remaining download size.
> * `INITIALIZE_MODELS` downloads/initializes models, emitting `DOWNLOAD_PROGRESS` updates to the UI.
> * Long-lived instances are reused post-setup:
>   * Generation pipeline in [`src/background/agent/Agent.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/agent/Agent.ts)
>   * Embedding pipeline in [`src/background/utils/FeatureExtractor.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/utils/FeatureExtractor.ts)
>
> Permissions in [`public/manifest.json`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/public/manifest.json) request `sidePanel`, `storage`, `scripting`, `tabs`, and `host_permissions` for `http(s)://*/*`. Request only what is strictly necessary to preserve user trust and streamline Chrome Web Store reviews.

---

## 3. 智能体与工具执行循环

### 3.1 工具调用基础

模型的工具调用将消息与工具架构（`name`、`description` 和 `parameters`）一起传递。Transformers.js 利用模型的聊天模板来格式化提示词。对于 Gemma-4 样式的模板，模型在触发工具时会发出特定的工具调用 Token 块：

```ts
import { pipeline } from "@huggingface/transformers";

const generator = await pipeline(
  "text-generation",
  "onnx-community/gemma-4-E2B-it-ONNX",
  {
    dtype: "q4f16",
    device: "webgpu",
  },
);

const messages = [{ role: "user", content: "What's the weather in Bern?" }];

const output = await generator(messages, {
  max_new_tokens: 128,
  do_sample: false,
  tools: [
    {
      type: "function",
      function: {
        name: "getWeather",
        description: "Get the weather in a location",
        parameters: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "The location to get the weather for",
            },
          },
          required: ["location"],
        },
      },
    },
  ],
});
```

模型输出可能如下所示：
```text
<|tool_call>call:getWeather{location:<|"|>Bern<|"|>}<tool_call|>
```
归一化层（`webMcp`）和解析器（`extractToolCalls`）将此输出转换为确定性的工具执行。

> Model tool calling passes messages alongside tool schemas (`name`, `description`, and `parameters`). Transformers.js formats the prompt utilizing the model's chat template. For Gemma-4-style templates, the model emits a specific tool-call token block when triggering a tool:
>
> ```ts
> import { pipeline } from "@huggingface/transformers";
>
> const generator = await pipeline(
>   "text-generation",
>   "onnx-community/gemma-4-E2B-it-ONNX",
>   {
>     dtype: "q4f16",
>     device: "webgpu",
>   },
> );
>
> const messages = [{ role: "user", content: "What's the weather in Bern?" }];
>
> const output = await generator(messages, {
>   max_new_tokens: 128,
>   do_sample: false,
>   tools: [
>     {
>       type: "function",
>       function: {
>         name: "getWeather",
>         description: "Get the weather in a location",
>         parameters: {
>           type: "object",
>           properties: {
>             location: {
>               type: "string",
>               description: "The location to get the weather for",
>             },
>           },
>           required: ["location"],
>         },
>       },
>     },
>   ],
> });
> ```
>
> Model output may look like this:
> ```text
> <|tool_call>call:getWeather{location:<|"|>Bern<|"|>}<tool_call|>
> ```
> A normalization layer (`webMcp`) and parser (`extractToolCalls`) convert this output into deterministic tool executions.

### 3.2 本项目中的工具接口

[`src/background/agent/webMcp.tsx`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/agent/webMcp.tsx) 将扩展程序工具归一化为模型友好的形态（`name`、`description`、`inputSchema`、`execute`）。支持的工具包括 `get_open_tabs`、`go_to_tab`、`open_url`、`close_tab`、`find_history`、`ask_website` 和 `highlight_website_element`。

> [`src/background/agent/webMcp.tsx`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/agent/webMcp.tsx) normalizes extension tools into a model-friendly shape (`name`, `description`, `inputSchema`, `execute`). Supported tools include `get_open_tabs`, `go_to_tab`, `open_url`, `close_tab`, `find_history`, `ask_website`, and `highlight_website_element`.

### 3.3 循环设计 (`Agent.runAgent`)

内部模型消息与面向 UI 的聊天消息保持了清晰的分离：
1. 用户输入被添加到 `chatMessages` 中，在流式传输 Token 的同时创建一个占位助手消息。
2. 流式传输/最终的模型输出通过 [`extractToolCalls.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/agent/extractToolCalls.ts) 解析为 `{ message, toolCalls }`。
3. 工具调用在后台执行，同时 UI 显示纯文本更新。
4. 工具结果被附加到工具元数据中，并反馈回下一轮提示词中。
5. 循环持续进行，直到没有剩余的工具调用，最终确定助手响应。

> Internal model messages are cleanly separated from UI-facing chat messages:
> 1. User input is added to `chatMessages`, creating a placeholder assistant message while streaming tokens.
> 2. Streamed/final model output is parsed via [`extractToolCalls.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/agent/extractToolCalls.ts) into `{ message, toolCalls }`.
> 3. Tool calls execute in the background while the UI displays plain text updates.
> 4. Tool results are appended to tool metadata and fed back into the next prompt turn.
> 5. The loop repeats until no tool calls remain, finalizing the assistant response.

---

## 4. 数据边界与持久化

状态的放置根据生命周期和访问模式进行拆分：
* **对话状态：** 后台内存（`Agent.chatMessages`），用于按轮次进行编排。
* **工具首选项：** `chrome.storage.local`，用于持久化用户设置。
* **语义历史向量：** IndexedDB（`VectorHistoryDB`），用于本地检索数据。
* **提取的页面内容：** 后台缓存（`WebsiteContentManager`），以活动 URL 为键。

> State placement is split by lifecycle and access patterns:
> * **Conversation State:** Background memory (`Agent.chatMessages`) for turn-by-turn orchestration.
> * **Tool Preferences:** `chrome.storage.local` for persistent user settings.
> * **Semantic History Vectors:** IndexedDB (`VectorHistoryDB`) for local retrieval data.
> * **Extracted Page Content:** Background cache (`WebsiteContentManager`) keyed by active URL.

---

## 5. 构建与打包注意事项

Manifest V3 要求每个运行时上下文具有可预测的输出格式。多入口打包在 [`vite.config.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/vite.config.ts) 中进行配置：
* [`src/sidebar/index.html`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/sidebar/index.html)
* [`src/background/background.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/background.ts)
* [`src/content/content.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/content/content.ts)

请确保输出名称与 [`public/manifest.json`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/public/manifest.json) 中指定的路径匹配。

> Manifest V3 requires predictable output formats per runtime context. Multi-entry bundling is configured in [`vite.config.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/vite.config.ts):
> * [`src/sidebar/index.html`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/sidebar/index.html)
> * [`src/background/background.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/background/background.ts)
> * [`src/content/content.ts`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/src/content/content.ts)
>
> Ensure output names match the paths specified in [`public/manifest.json`](https://github.com/nico-martin/gemma4-browser-extension/blob/main/public/manifest.json).

---

## 最终总结

使用 Transformers.js 构建高效扩展程序的核心原则是严格的关注点分离：**后台处理编排和推理，UI 表面保持轻量，内容脚本管理页面级交互。**

决定你的状态保存在哪里（`global`、`tabId` 还是站点作用域），将推理和数据管理集中在后台服务中，并让你的 UI 组件充当轻量级客户端。

> The core principle behind building an efficient extension with Transformers.js is strict separation of concerns: **the background handles orchestration and inference, UI surfaces remain thin, and content scripts manage page-level interactions.** 
>
> Decide where your state lives (`global`, `tabId`, or site-scoped), keep inference and data management centralized in background services, and let your UI components act as lightweight clients.