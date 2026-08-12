---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-13
hide:
- navigation
tags:
- ChatGPT
- Supabase
- Edge Functions
- MCP
- 软件开发
title: 使用 Supabase Edge Functions 和 mcp-use 构建 ChatGPT 应用
---
### 文章背景与核心概要
随着 OpenAI 推出 ChatGPT Apps 市场，开发者迎来了将聊天机器人转变为交互式平台的新机遇。本文深入探讨了如何利用 **Supabase Edge Functions** 与开源 TypeScript SDK **`mcp-use`** 从零构建自定义的 ChatGPT 应用。通过将后端 MCP 服务器部署在 Supabase 边缘计算环境中，并结合丰富的 React UI 组件（如数据库架构浏览器、状态查看器等），开发者可以实现将复杂的业务逻辑与前端展示完美隔离。

文章系统地介绍了整个开发全流程：从使用 `mcp-use` 初始化项目、配置单文件与多文件 UI addWidget 组件（区分纯展示型和数据获取型组件），到编写强大的 MCP 工具、使用一键脚本将服务部署至 Supabase Edge Functions，最后在 ChatGPT 开发者模式下进行联调。无论是扩展数据库交互能力，还是打造开箱即用的智能化应用，这套现代化的技术栈都为开发者提供了高效、无缝的解决方案。

---

## 什么是 ChatGPT Apps？
(What Are ChatGPT Apps?)

ChatGPT 应用扩展了 ChatGPT 的能力。它不再仅仅局限于回答问题，现在还可以展示交互式界面并连接外部服务。

> ChatGPT apps extend what ChatGPT can do. Instead of just answering questions, ChatGPT can now show interactive interfaces and connect to external services.

每个 ChatGPT 应用都包含两个部分：
* **MCP 服务器：** 这是你的后端。它定义了应用提供的工具和功能。当用户要求 ChatGPT 执行某项操作时，ChatGPT 会调用你的 MCP 服务器来获取数据或执行操作。
* **Web 组件：** 这是你的前端。它在 ChatGPT 内部以 iframe 的形式渲染。你的 MCP server 可以返回 UI 元数据，告诉 ChatGPT 显示哪个组件以及向其传递什么数据。

> Every ChatGPT app has two parts:
> * **MCP server:** This is your backend. It defines the tools and capabilities your app provides. When a user asks ChatGPT to do something, ChatGPT calls your MCP server to get the data or perform the action.
> * **Web component:** This is your frontend. It renders inside ChatGPT as an iframe. Your MCP server can return UI metadata that tells ChatGPT which component to display and what data to pass to it.

MCP 服务器和 Web 组件协同工作，而 ChatGPT 则充当桥梁。当用户提出问题时，ChatGPT 会判断应该调用哪个工具。你的 MCP server 运行该工具，并同时返回数据和 UI 指令。接着，ChatGPT 会带上数据渲染你的组件。

> The MCP server and web component work together. ChatGPT acts as the bridge. When a user asks a question, ChatGPT figures out which tool to call. Your MCP server runs the tool and returns both data and UI instructions. ChatGPT then renders your component with the data.

这种架构非常强大，因为它将应用的功能与其外观解耦。你的 MCP server 负责处理所有逻辑，组件负责所有展示，而 ChatGPT 则负责对话。

> This architecture is powerful because it separates what your app can do from how it looks. Your MCP server handles all the logic. Your components handle all the display. ChatGPT handles the conversation.

---

## 什么是 mcp-use？
(What Is mcp-use?)

`mcp-use` 是一个用于构建 MCP 服务器的开源 TypeScript SDK。它解决了一个特定问题：官方的 MCP SDK 使用的是 Express，而 Express 依赖于无法在 Supabase Edge Functions 等边缘环境中运行的 Node.js 特性。

> `mcp-use` is an open-source TypeScript SDK for building MCP servers. It solves a specific problem: the official MCP SDK uses Express, which depends on Node.js features that do not work in edge environments like Supabase Edge Functions.

`mcp-use` 使用 Hono 代替了 Express。Hono 是一个专为边缘运行时设计的轻量级 Web 框架。这意味着你的 MCP 服务器可以运行在 Supabase Edge Functions、Cloudflare Workers 以及其他无服务器平台上。

> `mcp-use` uses Hono instead of Express. Hono is a lightweight web framework designed for edge runtimes. This means your MCP server can run on Supabase Edge Functions, Cloudflare Workers, and other serverless platforms.

以下是 `mcp-use` 为你带来的特性：
* **边缘运行时支持：** 适用于 Deno、Cloudflare Workers 和 Supabase Edge Functions。
* **OpenAI Apps SDK 集成：** 内置对 ChatGPT 应用小部件（widgets）和 UI 组件的支持。
* **Supabase Auth 集成：** 原生支持使用 Supabase Auth 进行用户身份验证。
* **完全符合 MCP 标准：** 在官方 MCP 一致性测试中获得 100/100 的高分。

> Here is what `mcp-use` gives you:
> * **Edge runtime support:** Works on Deno, Cloudflare Workers, and Supabase Edge Functions.
> * **OpenAI Apps SDK integration:** Built-in support for ChatGPT app widgets and UI components.
> * **Supabase Auth integration:** Native support for authenticating users with Supabase Auth.
> * **Full MCP compliance:** Scores 100/100 on the official MCP conformance tests.

---

## 为什么选择 Supabase Edge Functions？
(Why Supabase Edge Functions?)

Supabase Edge Functions 是托管 MCP 服务器的绝佳选择，原因如下：
* **一切尽在一个地方：** 你的数据库、身份验证和服务器代码都存放在同一个 Supabase 项目中。你的 MCP server 可以直接查询数据库，并使用 Supabase Auth 检查用户权限。无需管理单独的服务或配置它们之间的连接。
* **快速冷启动：** Edge Functions 运行在 Deno 之上且启动迅速。当 ChatGPT 调用你的 MCP server 时，用户无需等待容器启动。
* **内置身份验证：** Supabase Auth 与 `mcp-use` 可以开箱即用。你可以要求用户在使用应用前登录、检查其角色和权限，并将数据访问权限限定在特定用户范围内。
* **部署简单：** 只需一条命令即可部署你的 MCP server。Supabase 会自动处理扩缩容、HTTPS 和基础设施。

> Supabase Edge Functions are a good fit for MCP servers for several reasons:
> * **Everything in one place:** Your database, authentication, and server code all live in the same Supabase project. Your MCP server can query your database directly. It can check user permissions using Supabase Auth. There is no need to manage separate services or configure connections between them.
> * **Fast cold starts:** Edge Functions run on Deno and start quickly. When ChatGPT calls your MCP server, users do not wait for a container to spin up.
> * **Built-in authentication:** Supabase Auth works out of the box with `mcp-use`. You can require users to log in before using your app, check their roles and permissions, and scope data access to specific users.
> * **Simple deployment:** A single command deploys your MCP server. Supabase handles scaling, HTTPS, and infrastructure.

---

## 你将构建什么？
(What You Will Build)

你将构建一个用于浏览 Supabase 数据库的 ChatGPT 应用。该应用提供四个工具：
* **列出表格（List tables）：** 通过交互式的架构浏览器小部件显示数据库中的所有表格。
* **显示表格（Show table）：** 具有排序和过滤功能，展示特定表格的数据。
* **执行 SQL（Execute SQL）：** 运行只读 SQL 查询并通过语法高亮显示结果。
* **Supabase 状态（Supabase status）：** 显示 Supabase 服务的当前状态和最近的故障记录。

每个工具都会返回数据和 React 小部件。ChatGPT 用户看到的将是交互式界面，而不仅仅是文本回复。

> You will build a ChatGPT app that explores Supabase databases. The app provides four tools:
> * **List tables:** Shows all tables in your database with an interactive schema explorer widget.
> * **Show table:** Displays data from a specific table with sorting and filtering.
> * **Execute SQL:** Runs read-only SQL queries and shows results with syntax highlighting.
> * **Supabase status:** Shows the current status of Supabase services and recent incidents.
> 
> Each tool returns both data and a React widget. ChatGPT users see interactive interfaces, not just text responses.

> 📦 **完整实现：** 有关完整的实现，请访问或克隆代码仓库：[github.com/mcp-use/supabase-mcp-server](https://github.com/mcp-use/supabase-mcp-server)
> 
> > 📦 **Full Implementation:** For the complete implementation, please visit or clone the repository: [github.com/mcp-use/supabase-mcp-server](https://github.com/mcp-use/supabase-mcp-server)

---

## 项目设置
(Project Setup)

首先使用 `mcp-use` 创建一个新项目：

> Start by creating a new project with `mcp-use`:

```bash
npx create-mcp-use-app my-supabase-app --template apps-sdk
cd my-supabase-app
npm install
```

这将创建一个包含你所需一切的项目：`mcp-use` SDK、小部件模板以及用于 Supabase Edge Functions 的构建配置。

> This creates a project with everything you need: the `mcp-use` SDK, widget templates, and build configuration for Supabase Edge Functions.

> ⚠️ **注意：** 默认的 `apps-sdk` 模板包含一个“水果店”演示，用于展示小部件的工作原理。**你需要修改或替换这些文件**，使其符合本指南中描述的 Supabase 浏览器工具。
> 
> > ⚠️ **Note:** The default `apps-sdk` template includes a "fruit shop" demo to show how widgets work. **You will need to modify or replace these files** to align with the Supabase explorer tools described in this guide.

接下来，在你的项目中初始化 Supabase：

> Next, initialize Supabase in your project:

```bash
supabase init
supabase login
supabase link --project-ref YOUR_PROJECT_ID
```

你可以在 Supabase 仪表板的“项目设置”（Project Settings）下找到你的项目 ID。

> You can find your project ID in your Supabase dashboard under Project Settings.

---

## 构建 MCP 服务器
(Building the MCP Server)

打开 `index.ts` 并设置你的 MCP 服务器：

> Open `index.ts` and set up your MCP server:

```typescript
// index.ts
import { error, MCPServer, object, text, widget } from 'mcp-use/server'

const server = new MCPServer({
  name: 'supabase-explorer',
  version: '1.0.0',
  description: 'A Supabase MCP server with Apps SDK widgets',
})
```

---

## 添加 UI 小部件
(Adding UI Widgets)

小部件可以通过两种方式组织：**单文件小部件（single-file widgets）** 或 **文件夹式小部件（folder-based widgets）**。请选择最符合小部件复杂度的组织风格。

> Widgets can be organized in two ways: **single-file widgets** or **folder-based widgets**. Choose the organization style that best fits your widget's complexity.

```text
├── index.ts                # Main server file using mcp-use
├── resources/              # React widget components
│   ├── components/         # Reusable UI components
│   ├── schema-explorer/    # Schema explorer widget (in this article)
│   ├── table-viewer/       # Table viewer widget
│   └── query-results/      # Query results widget
│   └── supabase-status.tsx # 1 file widget
└── package.json            # Dependencies
```

查看 [此处的小部件实现](https://github.com/mcp-use/supabase-mcp-server/tree/main/resources) 以及 [小部件文档](https://mcp-use.com/docs/typescript/server/ui-widgets)。

> Check out the widgets [implementation here](https://github.com/mcp-use/supabase-mcp-server/tree/main/resources) and the [widget docs](https://mcp-use.com/docs/typescript/server/ui-widgets).

### 两种类型的小部件
(Two Types of Widgets)
`mcp-use` SDK 支持两种小部件模式：
1. 纯展示型小部件
2. 展示并返回数据型小部件

> The `mcp-use` SDK supports two widget patterns:
> 1. Display-only widgets
> 2. Display and return data widgets

#### 1. 纯展示型小部件
(1. Display-Only Widgets)

**纯展示型小部件**不会在服务器上获取数据。它们接收工具参数作为 props 并渲染 UI。`supabase-status` (`resources/supabase-status.tsx`) 小部件就是这种工作方式。它在 React 组件中从 Supabase 状态 API 客户端获取状态数据。

> **Display-only widgets** do not fetch data on the server. They receive tool parameters as props and render UI. The `supabase-status` (`resources/supabase-status.tsx`) widget works this way. It fetches status data client-side from the Supabase status API in the React component.

你无需在 `index.ts` 中将该小部件注册为工具，因为 `mcp-use` 会自动将 `resources/` 文件夹中的所有**纯展示型小部件**注册为 MCP 工具。

> You don't need to register the widget as a tool in `index.ts` because `mcp-use` automatically registers all **display-only widgets** in the `resources/` folder as MCP tools.

```tsx
// resources/supabase-status.tsx
import { McpUseProvider, useWidget, type WidgetMetadata } from "mcp-use/react";
import React, { useEffect, useState } from "react";
import z from "zod/v4";
import "./styles.css";

// Tool args that will be passed to the widget props
const propSchema = z.object({
  daysBack: z.number().default(7).describe("Number of days back to show incidents"),
});

// Define widget metadata - auto-generates tool
export const widgetMetadata: WidgetMetadata = {
  description: "Display Supabase service status and recent incidents from the status page",
  props: propSchema,
  exposeAsTool: true, // Important for display-only widgets, that are auto registered
  annotations: { readOnlyHint: true },
  appsSdkMetadata: {
    "openai/widgetCSP": {
      connect_domains: ["https://status.supabase.com"],
      resource_domains: ["https://*.supabase.com"],
    },
  },
};

// Your widget component
const SupabaseStatusWidget: React.FC = () => {
  // Get props from mcp-use hook: useWidget -> Everything you need in one hook!
  const { props, isPending } = useWidget<z.infer<typeof propSchema>>();
  const [incidents, setIncidents] = useState<Incident[]>([]);

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        setLoading(true);
        const response = await fetch("https://status.supabase.com/history.rss");
        // ... Fetch APIs from the widget
      }
    };
    fetchStatus();
  }, [props.daysBack]);

  return (
    <McpUseProvider viewControls="fullscreen" autoSize>
      <Card className="relative p-6 rounded-3xl w-full">
        <div className="mb-6">
          <div className="flex items-center justify-between mb-2">
            <div>
              <h2 className="text-3xl font-bold text-[hsl(var(--foreground))] mb-1">
                Supabase Status
              </h2>
              <p className="text-sm text-foreground-muted">
                Last {props.daysBack} days
              </p>
            </div>
          </div>
        </div>
        {/* Full component implementation: https://github.com/mcp-use/supabase-mcp-server/blob/main/resources/supabase-status.tsx */}
      </Card>
    </McpUseProvider>
  );
};

export default SupabaseStatusWidget;
```

正如在 `widgetMetadata` 的 props (`daysBack`) 中所定义的，MCP 工具期望接收一个参数，由 LLM 指定用于获取故障记录的天数。

> As defined in the `widgetMetadata` props (`daysBack`), the MCP tool expects an argument specifying the number of days to retrieve incidents from the LLM.

#### 2. 展示并返回数据型小部件
(2. Display and Return Data Widgets)

**展示并返回数据型小部件**在服务器端获取数据，并将其传递给 LLM 和小部件。`list-tables` 工具就是这种工作方式。服务器查询数据库，将数据返回给 ChatGPT 进行推理，并将相同的数据传递给小部件进行显示。

> **Display and return data widgets** fetch data server-side and pass it to both the LLM and the widget. The `list-tables` tool works this way. The server queries the database, returns data to ChatGPT for reasoning, and passes the same data to the widget for display.

这种分离非常有用：有时你希望向用户展示的内容比告诉 LLM 的要多，或者告诉 LLM 的内容比向用户展示的要多。你可以独立控制这两者。

> This separation is useful: sometimes you want to show the user more than you tell the LLM, or tell the LLM more than you show the user. You control both independently.

---

## 添加工具
(Adding Tools)

工具定义了你的应用可以执行的操作。每个工具都有名称、参数和一个回调函数。对于返回 UI 小部件的工具，请指定 `widget` 参数，并使小部件名称与 `resources/` 中的组件相匹配（在此例中为 `"schema-explorer"`）。

> Tools define what your app can do. Each tool has a name, parameters, and a callback function. For tools that return UI widgets, specify the `widget` argument and set the widget name matching the component in `resources/` (in this case, `"schema-explorer"`).

以下是返回 `schema-explorer` 小部件的 **`list-tables`** 工具：

> Here is the **`list-tables`** tool returning the `schema-explorer` widget:

```typescript
// index.ts
server.tool(
  {
    name: 'list-tables',
    description: 'List all tables in your Supabase database',
    schema: z.object({
      schemas: z.array(z.string()).optional().describe('Schemas to include (default: all)'),
    }),
    widget: {
      name: 'schema-explorer',
      invoking: 'Loading database tables...',
      invoked: 'Tables loaded successfully',
    },
    annotations: { readOnlyHint: true },
  },
  async ({ schemas }) => {
    try {
      const result = await supabaseClient?.callTool('list_tables', { schemas: ['public'] })
      const content = result?.content[0]
      let tables: any[] = []

      if (content?.type === 'text') {
        const data = extractJsonFromResponse(content?.text ?? '')
        tables = Array.isArray(data) ? data : []
      }

      return widget({
        // Props passed to the React component in /resources folder
        props: {
          tables,
          schemas: schemas || ['public'],
        },
        // Output returned by the MCP tool to the LLM (what the LLM sees)
        output: object({
          tables: tables.map((table) => ({
            name: table.name,
          })),
        }),
      })
    } catch (err) {
      return error(`Error listing tables: ${err instanceof Error ? err.message : String(err)}`)
    }
  }
)
```

该工具查询数据库以获取表格信息，为 LLM 返回文本内容，并为 UI 返回小部件元数据。

> The tool queries your database for table information, returning text content for the LLM and widget metadata for the UI.

---

## 部署到 Supabase
(Deploying to Supabase)

Supabase Edge Functions 为托管你的服务器提供了一个绝佳的场所：快速、可扩展且易于管理。

> Supabase Edge Functions provide a great place to host your server: fast, scalable, and easy to manage.

> 📚 有关完整的逐步指南，请参阅 [Supabase 部署文档](https://mcp-use.com/docs/typescript/server/deployment-supabase#supabase)。
> 
> > 📚 For the complete step-by-step guide, see the [Supabase deployment documentation](https://mcp-use.com/docs/typescript/server/deployment-supabase#supabase).

**前提条件：** 部署前请确保 Docker 正在运行。

> **Prerequisite:** Ensure Docker is running before deployment.

```bash
# Verify Docker is running, otherwise install it
docker info
```

`mcp-use` 包含一个处理所有操作的部署脚本：

> `mcp-use` includes a deployment script that handles everything:

```bash
curl -fsSL https://url.mcp-use.com/supabase | bash
```

此脚本会检查你的身份验证、构建应用程序、设置环境变量并将其部署到 Supabase Edge Functions。

> This script checks your authentication, builds your application, sets environment variables, and deploys to Supabase Edge Functions.

部署后，你的 MCP 服务器将在线运行于：

> After deployment, your MCP server is live at:
```text
https://<YOUR_PROJECT_ID>.supabase.co/functions/v1/<YOUR_FUNCTION_NAME>/mcp
```

---

## 连接到 ChatGPT
(Connecting to ChatGPT)

请参考 [官方开发者模式指南](https://platform.openai.com/docs/guides/developer-mode) 在你的 ChatGPT 个人资料中启用它。

> Refer to the [Official Developer Mode Guide](https://platform.openai.com/docs/guides/developer-mode) to enable it in your ChatGPT profile.

要在 ChatGPT 中使用你的应用：
1. **启用开发者模式：** 前往 [设置 → 应用和连接器](https://chatgpt.com/#settings/Connectors) → **高级 → 开发者模式**。
2. 点击 **“创建应用”**（Create App）添加 MCP 服务器，并输入你的 Edge Function URL（以 `/mcp` 结尾）。

> To use your app in ChatGPT:
> 1. **Enable developer mode:** Go to [Settings → Apps & Connectors](https://chatgpt.com/#settings/Connectors) → **Advanced → Developer mode**.
> 2. Click on **"Create App"** to add the MCP server and enter your Edge Function URL with `/mcp` at the end.

要打开你的新 ChatGPT 应用：
1. 点击 `+` 按钮添加一个新连接器。
2. 选择 **“更多”**（More），然后选择你刚刚添加的 MCP 服务器。

> To open your new ChatGPT App:
> 1. Click the `+` button to add a new connector.
> 2. Select **"More"** and then select the MCP Server you just added.

现在你可以开始新对话并使用你的工具了。让 ChatGPT 列出你的表格、显示特定表格中的数据或运行 SQL 查询。ChatGPT 将调用你的 MCP server 并显示交互式小部件。

> Now you can start a new chat and use your tools. Ask ChatGPT to list your tables, show data from a specific table, or run a SQL query. ChatGPT will call your MCP server and display the interactive widgets.

---

## 下一步
(Next Steps)

你现在拥有了一个由 Supabase Edge Functions 驱动的可运行 ChatGPT 应用。以下是一些扩展它的方法：
* 添加更多与你的特定数据库表进行交互的工具。
* 为你的数据类型构建自定义小部件。
* 通过适当的授权检查实现写入操作。
* 添加工具链（tool chaining），以便 ChatGPT 可以组合多个操作。

> You now have a working ChatGPT app powered by Supabase Edge Functions. Here are some ways to extend it:
> * Add more tools that interact with your specific database tables.
> * Build custom widgets for your data types.
> * Implement write operations with proper authorization checks.
> * Add tool chaining so ChatGPT can combine multiple operations.

### 资源
(Resources)
* [mcp-use 文档](https://mcp-use.com/docs/typescript/server/deployment-supabase)
* [mcp-use GitHub 仓库](https://github.com/mcp-use/mcp-use)
* [Supabase Edge Functions 指南](https://supabase.com/docs/guides/functions)
* [完整实现仓库](https://github.com/mcp-use/supabase-mcp-server)

> ### Resources
> * [mcp-use Documentation](https://mcp-use.com/docs/typescript/server/deployment-supabase)
> * [mcp-use GitHub Repository](https://github.com/mcp-use/mcp-use)
> * [Supabase Edge Functions Guide](https://supabase.com/docs/guides/functions)
> * [Full Implementation Repository](https://github.com/mcp-use/supabase-mcp-server)