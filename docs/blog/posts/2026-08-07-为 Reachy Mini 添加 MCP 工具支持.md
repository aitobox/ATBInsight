---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-07
hide:
- navigation
tags:
- Reachy Mini
- MCP
- Hugging Face
- 机器人开发
- 语音交互
title: 为 Reachy Mini 添加 MCP 工具支持
---
### 文章背景与核心概要
本文介绍了 Reachy Mini 机器人对话应用程序的一项重大更新：通过模型上下文协议（Model Context Protocol, MCP）集成托管在公开 Hugging Face Spaces 上的远程工具。在此之前，扩展机器人的能力往往需要修改核心应用代码或在本地下载外部代码。现在，用户只需通过简单的命令行指令，就能让机器人瞬间获得网络搜索或天气查询等全新功能。

文章深入探讨了内置工具的工作原理、如何通过配置文件（Profiles）管理激活的工具、远程 Spaces 如何通过命名空间无缝集成，并分享了发布您自己的兼容 MCP 的工具 Spaces 的最佳实践。这一功能的推出，标志着 Reachy Mini 成功将本地物理具身能力与可扩展的远程智能完美结合。

---

# 为 Reachy Mini 添加 MCP 工具支持

*发布时间：2026年6月3日*  
*作者：Alina Lozovskaya*

![Reachy Mini looking out the window](./images/9f8fdf04a966.jpg)
*Reachy Mini 终于不用再只靠望向窗外来告诉你天气了*

---

## 摘要 (Summary)

Reachy Mini 对话应用程序现已支持通过模型上下文协议（MCP）集成托管在公共 Hugging Face Spaces 中的远程工具。用户无需修改核心应用代码或在本地下载外部代码，即可通过简单的命令行指令瞬间赋予机器人新的能力——例如网页搜索或天气查询。本文探讨了内置工具的工作原理、配置文件如何控制活动工具、远程 Spaces 如何通过命名空间实现无缝集成，以及发布您自己的兼容 MCP 的工具 Spaces 的最佳实践。

> The Reachy Mini conversation app now supports integrating remote tools hosted in public Hugging Face Spaces via the Model Context Protocol (MCP). Instead of modifying core app code or downloading external code locally, users can instantly grant their robot new capabilities—such as web search or weather checking—via simple CLI commands. This article explores how built-in tools function, how profiles govern active tools, how remote Spaces integrate seamlessly through namespacing, and best practices for publishing your own MCP-compatible tool Spaces.

---

## 引言 (Introduction)

Reachy Mini 对话应用程序不仅仅是一个简单的语音界面；它构建了一个动态系统，使机器人能够对对话做出身体和语言上的双重响应。

添加一项新的远程功能只需一条命令：

```bash
reachy-mini-conversation-app tool-spaces add pollen-robotics/reachy-mini-weather-tool
```

然后，像往常一样启动应用程序：

```bash
reachy-mini-conversation-app
```

现在你可以直接发问：
> *巴黎今天天气怎么样？*

> The Reachy Mini conversation app goes beyond a simple voice interface; it creates a dynamic system where the robot responds physically and verbally to a conversation. 
>
> Adding a new remote capability takes just one command:
>
> ```bash
> reachy-mini-conversation-app tool-spaces add pollen-robotics/reachy-mini-weather-tool
> ```
>
> Then, start the app as usual:
>
> ```bash
> reachy-mini-conversation-app
> ```
>
> Now you can simply ask:
> > *What's the weather in Paris today?*

---

## 内置工具 (Built-in Tools)

工具代表模型在对话过程中可以执行的操作：播放情感、移动头部或通过摄像头捕捉图像。每个工具都有一个名称和简短描述，模型通过读取这些信息来决定何时调用它。

目前，大多数工具都随应用程序在本地发布，主要关注机器人的硬件：

| 工具 (Tool) | 作用 (What it does) |
| :--- | :--- |
| `move_head` | 排队执行头部姿态更改 |
| `dance` / `stop_dance` | 从舞蹈库中播放或清除舞蹈 |
| `play_emotion` / `stop_emotion` | 播放或清除录制的情感片段 |
| `head_tracking` | 切换头部追踪偏移量 |
| `camera` | 捕获帧并进行分析 |
| `idle_do_nothing` | 在空闲轮次中明确保持空闲 |

> A tool represents an action the model can execute during a conversation: playing an emotion, moving the head, or capturing an image through the camera. Each tool has a name and a short description that the model reads to determine when to call it.
>
> Today, most tools ship locally within the app and focus primarily on the robot's hardware:
>
> | Tool | What it does |
> | :--- | :--- |
> | `move_head` | Queue a head pose change |
> | `dance` / `stop_dance` | Play or clear a dance from the dances library |
> | `play_emotion` / `stop_emotion` | Play or clear a recorded emotion clip |
> | `head_tracking` | Toggle head-tracking offsets |
> | `camera` | Capture a frame and analyze it |
> | `idle_do_nothing` | Explicitly stay idle on an idle turn |

---

## 配置文件如何控制工具 (How Profiles Control Tools)

只有在**配置文件（Profile）**中启用工具，该工具才可被使用。配置文件是一个包含 `instructions.txt`（提示词）和 `tools.txt`（启用工具列表）的文件夹。

`default` 配置文件启用了完整的内置工具集：

```text
# profiles/default/tools.txt
dance
stop_dance
play_emotion
stop_emotion
camera
idle_do_nothing
head_tracking
move_head
```

如果在 `tools.txt` 中省略了某个工具的名称，模型将无法调用它。

> A tool is only usable if it is enabled inside a **profile**—a folder containing `instructions.txt` (the prompt) and `tools.txt` (the enabled tool list).
>
> The `default` profile enables the full built-in set:
>
> ```text
> # profiles/default/tools.txt
> dance
> stop_dance
> play_emotion
> stop_emotion
> camera
> idle_do_nothing
> head_tracking
> move_head
> ```
>
> If a tool's name is omitted from `tools.txt`, the model cannot invoke it.

---

## 本地工具的局限性 (The Limits of Local Tools)

完全依赖本地 Python 文件对于像 `move_head` 这样的硬件交互效果很好，但对于网络搜索或天气查询等非物理功能来说，会带来沉重的摩擦：
* 共享工具需要发送原始的 Python 文件。
* 更新需要手动重新分发文件。
* 功能与应用程序代码紧密耦合。

> Relying exclusively on local Python files works well for hardware interactions like `move_head`, but introduces heavy friction for non-physical capabilities like web searches or weather lookups:
> * Sharing a tool requires sending raw Python files.
> * Updates require manual file redistribution.
> * Capabilities remain tightly coupled to the application code.

---

## 从 Spaces 调用工具 (Calling Tools from Spaces)

远程工具引入了一种轻量级、可共享的替代方案，完全托管在公共 Hugging Face Spaces 中：
* **内置机器人工具**保持本地化且受信任。
* **可共享的远程工具**托管在公共 Hugging Face Spaces 中。
* **自定义本地工具**仍然可以通过 `external_tools/` 使用。

目前有两个用于测试完整工作流的测试工具（Canary tools）：
* [pollen-robotics/reachy-mini-search-tool](https://huggingface.co/spaces/pollen-robotics/reachy-mini-search-tool)
* [pollen-robotics/reachy-mini-weather-tool](https://huggingface.co/spaces/pollen-robotics/reachy-mini-weather-tool)

要同时使用这两个工具，请将每个 Space 添加到您的配置文件中：

```bash
reachy-mini-conversation-app tool-spaces add pollen-robotics/reachy-mini-search-tool
reachy-mini-conversation-app tool-spaces add pollen-robotics/reachy-mini-weather-tool
```

> Remote tools introduce a lightweight, shareable alternative hosted entirely inside public Hugging Face Spaces:
> * **Built-in robot tools** remain local and trusted.
> * **Shareable remote tools** live in public Hugging Face Spaces.
> * **Custom local tools** remain available via `external_tools/`.
>
> Two canary tools are available to test the complete workflow:
> * [pollen-robotics/reachy-mini-search-tool](https://huggingface.co/spaces/pollen-robotics/reachy-mini-search-tool)
> * [pollen-robotics/reachy-mini-weather-tool](https://huggingface.co/spaces/pollen-robotics/reachy-mini-weather-tool)
>
> To use both simultaneously, add each Space to your profile:
>
> ```bash
> reachy-mini-conversation-app tool-spaces add pollen-robotics/reachy-mini-search-tool
> reachy-mini-conversation-app tool-spaces add pollen-robotics/reachy-mini-weather-tool
> ```

---

## 管理工具 Spaces（安装、列出、移除）(Managing Tool Spaces (Install, List, Remove))

```bash
# 在活动配置文件中安装并启用
reachy-mini-conversation-app tool-spaces add <owner/space-name>
 
# 在特定配置文件中启用
reachy-mini-conversation-app tool-spaces add <owner/space-name> --profile <NAME>
 
# 仅安装不启用
reachy-mini-conversation-app tool-spaces add <owner/space-name> --install-only
 
# 列出已安装的 spaces
reachy-mini-conversation-app tool-spaces list
 
# 移除已安装的 space
reachy-mini-conversation-app tool-spaces remove <owner/space-name>
```

> **注意：** `tools.txt` 充当守门人：远程工具只有在其 ID 明确列在配置文件的 `tools.txt` 中时才是活动的。

### 清单存放位置
已安装的源持久化保存在：
* 受管应用模式下的 `installed_tool_spaces.json`。
* 终端模式下的 `external_content/installed_tool_spaces.json`。

> ```bash
> # Install + enable in the active profile
> reachy-mini-conversation-app tool-spaces add <owner/space-name>
>  
> # Enable in a specific profile
> reachy-mini-conversation-app tool-spaces add <owner/space-name> --profile <NAME>
>  
> # Install without enabling
> reachy-mini-conversation-app tool-spaces add <owner/space-name> --install-only
>  
> # List installed spaces
> reachy-mini-conversation-app tool-spaces list
>  
> # Remove an installed space
> reachy-mini-conversation-app tool-spaces remove <owner/space-name>
> ```
>
> > **Note:** `tools.txt` acts as the gatekeeper: a remote tool is only active if its ID is explicitly listed inside the profile's `tools.txt`.
>
> ### Where the Manifest Lives
> Installed sources persist in:
> * `installed_tool_spaces.json` in managed app mode.
> * `external_content/installed_tool_spaces.json` in terminal mode.

---

## 工具命名与命名空间 (Tool Naming and Namespacing)

每个安装的 Space 都会被分配一个从其短名称（slug）派生的本地别名，该别名将连字符、点和斜杠转换为下划线：
```text
pollen-robotics/reachy-mini-search-tool → pollen_robotics_reachy_mini_search_tool
```

远程工具使用双下划线命名空间结构：
```text
pollen_robotics_reachy_mini_search_tool__search_web
pollen_robotics_reachy_mini_weather_tool__get_day_brief
```

> Each installed Space is assigned a local alias derived from its slug, converting hyphens, dots, and slashes into underscores:
> ```text
> pollen-robotics/reachy-mini-search-tool → pollen_robotics_reachy_mini_search_tool
> ```
>
> Remote tools use a double-underscore namespace structure:
> ```text
> pollen_robotics_reachy_mini_search_tool__search_web
> pollen_robotics_reachy_mini_weather_tool__get_day_brief
> ```

---

## 配置文件示例 (Example Profiles)

### 1. 网页搜索配置文件
```text
# profiles/canary_web_search/tools.txt
play_emotion
stop_emotion
idle_do_nothing
move_head
pollen_robotics_reachy_mini_search_tool__search_web
```

### 2. 搜索与天气配置文件
```text
# profiles/canary_web_search_weather/tools.txt
play_emotion
stop_emotion
idle_do_nothing
move_head
pollen_robotics_reachy_mini_search_tool__search_web
pollen_robotics_reachy_mini_weather_tool__get_day_brief
```

> ### 1. Web Search Profile
> ```text
> # profiles/canary_web_search/tools.txt
> play_emotion
> stop_emotion
> idle_do_nothing
> move_head
> pollen_robotics_reachy_mini_search_tool__search_web
> ```
>
> ### 2. Search & Weather Profile
> ```text
> # profiles/canary_web_search_weather/tools.txt
> play_emotion
> stop_emotion
> idle_do_nothing
> move_head
> pollen_robotics_reachy_mini_search_tool__search_web
> pollen_robotics_reachy_mini_weather_tool__get_day_brief
> ```

---

## 为什么提示词很重要 (Why Prompts Matter)

提示词指令决定了模型利用多个工具的效率。例如，一个结合了天气和活动的查询：
> *"我今天在波尔多需要带外套吗，市区今晚有什么重大活动吗？"*

通过精确的提示词工程，可以优化为在同一轮次中并行调用这两个工具：

### `canary_web_search_weather/instructions.txt`
```text
[default_prompt]

## CANARY SEARCH AND WEATHER RULES
You have two remote tools:
- a weather brief tool for compact day weather at a location
- a web search tool for broader current web information

When the user's question mixes a weather part and a current-info part, call both tools in parallel in the same turn. Merge the results into a single short answer, covering weather first. Keep responses short and spoken-style.
```

> Prompt instructions dictate how efficiently the model leverages multiple tools. For instance, a query combining weather and events:
> > *"Should I bring a jacket in Bordeaux today, and is there anything major happening downtown tonight?"*
>
> Can be optimized to call both tools in parallel via precise prompt engineering:
>
> ### `canary_web_search_weather/instructions.txt`
> ```text
> [default_prompt]
>
> ## CANARY SEARCH AND WEATHER RULES
> You have two remote tools:
> - a weather brief tool for compact day weather at a location
> - a web search tool for broader current web information
>
> When the user's question mixes a weather part and a current-info part, call both tools in parallel in the same turn. Merge the results into a single short answer, covering weather first. Keep responses short and spoken-style.
> ```

---

## 功能矩阵：目前支持哪些功能 (Feature Matrix: What Works Today)

| 功能 (Capability) | 是否支持 (Supported) |
| :--- | :---: |
| 通过 slug 安装公开的、兼容 MCP 的 Gradio Spaces (`/gradio_api/mcp/`) | ✅ |
| 同时使用多个 Spaces | ✅ |
| 通过 `tools.txt` 进行每个配置文件维度的启用 | ✅ |
| 带命名空间的远程工具 ID | ✅ |
| 后端无关的注册（OpenAI、Gemini、Hugging Face） | ✅ |
| 不在本地下载任何任意代码 | ✅ |
| 私有或需认证的 Spaces | ❌ |
| 非 Gradio Spaces | ❌ |
| 任意原始 MCP URL 或非 Hugging Face MCP 服务器 | ❌ |
| 保证并行的工具编排 | ❌ |

> | Capability | Supported |
> | :--- | :---: |
> | Install by slug for public, MCP-compatible Gradio Spaces (`/gradio_api/mcp/`) | ✅ |
> | Multiple Spaces at once | ✅ |
> | Per-profile enablement via `tools.txt` | ✅ |
> | Namespaced remote tool IDs | ✅ |
> | Backend-agnostic registration (OpenAI, Gemini, Hugging Face) | ✅ |
> | No arbitrary code downloaded locally | ✅ |
> | Private or authenticated Spaces | ❌ |
> | Non-Gradio Spaces | ❌ |
> | Arbitrary raw MCP URLs or non-Hugging Face MCP servers | ❌ |
> | Guaranteed parallel tool orchestration | ❌ |

---

## 发布工具 Space 的提示 (Tips for Publishing a Tool Space)

为了让您的工具易于发现和使用：
1. 将您的工具发布为公开的 Gradio Space，并公开标准的 MCP 端点。
2. 保持工具无状态（stateless），以确保可靠的网络性能。
3. 为您的 Space 打上 `reachy-mini-tool` 和 `mcp` 标签。

> To make your tools easily discoverable and usable:
> 1. Publish your tool as a public Gradio Space exposing the standard MCP endpoint.
> 2. Keep your tools stateless to ensure reliable network performance.
> 3. Tag your Space with `reachy-mini-tool` and `mcp`.

---

## 结论 (Conclusion)

Reachy Mini 现在将本地具身性与可扩展的远程智能联系在了一起。通过将内置硬件控制与远程 MCP 工具空间相结合，开发者可以无缝自定义和扩展助手的功能。

*致谢：非常感谢 [Fabien Danieau](https://huggingface.co/FabienDanieau)、[Andres Marafioti](https://huggingface.co/andito)、[Remi Fabre](https://huggingface.co/RemiFabre) 以及 Pollen Robotics 团队提供的宝贵反馈和测试。*

> Reachy Mini now bridges local embodiment with scalable remote intelligence. By combining built-in hardware controls with remote MCP tool spaces, developers can customize and expand assistant capabilities seamlessly. 
>
> *Acknowledgements: Many thanks to [Fabien Danieau](https://huggingface.co/FabienDanieau), [Andres Marafioti](https://huggingface.co/andito), [Remi Fabre](https://huggingface.co/RemiFabre), and the Pollen Robotics team for their invaluable feedback and testing.*