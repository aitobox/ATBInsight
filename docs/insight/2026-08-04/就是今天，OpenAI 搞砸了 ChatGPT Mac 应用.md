# 就是今天，OpenAI 搞砸了 ChatGPT Mac 应用

**背景与摘要：**
本文批评了 OpenAI 最近针对 macOS 桌面端 ChatGPT 应用的更新。原来小巧、原生的 ChatGPT 应用程序被降级为“ChatGPT Classic”，取而代之的是一个体积庞大、基于 Electron 框架构建的“超级应用”。新应用将多种工具（包括已停用的 Atlas 浏览器功能）强行拼凑在一起，不仅体积膨胀至 1.5GB，而且完全背离了原生 Mac 应用的设计美学，引发了用户的强烈不满。

> **Summary:** OpenAI’s latest sprawling product announcements have completely upended the macOS desktop experience. The beloved native ChatGPT app has been relegated to "Classic" status, replaced by a bloated 1.5 GB Electron "superapp" that awkwardly merges multiple tools—including remnants of the discontinued Atlas browser—while abandoning native Mac design principles.

---

## 全新的桌面生态系统

Zac Hall 在 [9to5Mac](https://openai.com/index/gpt-5-6/) 撰文，[总结了这场混乱的过渡](https://daringfireball.net/linked/2026/07/09/todays-the-day-openai-fucked-up-the-chatgpt-mac-app)：

> ## The New Desktop Ecosystem
> 
> Writing at [9to5Mac](https://openai.com/index/gpt-5-6/), Zac Hall [summarized the chaotic transition](https://daringfireball.net/linked/2026/07/09/todays-the-day-openai-fucked-up-the-chatgpt-mac-app):

> 总结一下今天的桌面应用变化：
> 
> * 现有的 ChatGPT 应用现在变成了 **ChatGPT Classic**。
> * **Codex** 现在成了新的 ChatGPT 桌面应用。它看起来仍然像 Codex，并且包含 Codex 图标作为一个选项，但现在它被称为 ChatGPT。
> * 用于桌面的 ChatGPT 包含 **ChatGPT Work** 和 **ChatGPT Codex**，两者共享插件。ChatGPT Codex 模式会显示更多 ChatGPT Work 向用户隐藏的技术细节。
> * 你可以同时安装 ChatGPT Classic、ChatGPT 和 Codex，但未来的发展方向似乎是只运行新的 ChatGPT 桌面应用。Codex 用户仍然可以使用 Codex 应用图标，但应用名称将变为 ChatGPT。

> > To summarize today’s desktop app changes:
> > 
> > * The existing ChatGPT app is now **ChatGPT Classic**.
> > * **Codex** is now the new ChatGPT desktop app. It still looks like Codex and includes the Codex icon as an option, but it’s now called ChatGPT.
> > * ChatGPT for desktop includes **ChatGPT Work** and **ChatGPT Codex**, which share plug-ins. ChatGPT Codex mode shows more technical details that ChatGPT Work abstracts away from the user.
> > * It’s possible to have ChatGPT Classic, ChatGPT, and Codex installed, but the way forward seems to be just running the new ChatGPT desktop app. Codex users can still use the Codex app icon, but the app will be called ChatGPT.

*看来我挑错了一周来戒掉吸胶水的恶习。*

> *Looks like I picked the wrong week to quit sniffing glue.*

---

## 原生优雅与 Electron 臃肿的对决

> ChatGPT Classic 应用程序看起来更像原生 Mac 风格，所以对用户来说这可能是一个问题。

> ## Native Elegance vs. Electron Bloat
> 
> > The ChatGPT Classic app looks more native Mac-like, so that might be an issue for users.

存在已久的原生 ChatGPT Mac 应用程序——也就是现在显然被称为 **ChatGPT Classic** 的那个——是一个仅有 **159 MB** 的小巧程序包。

> The longstanding native ChatGPT Mac app—the one apparently now called **ChatGPT Classic**—is a modest **159 MB** bundle. 

相比之下，新的 ChatGPT 超级应用——结合了简单的聊天机器人、[ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/)、Codex 以及[已停止独立的 Atlas Web 浏览器](https://9to5mac.com/2026/07/09/openai-is-discontinuing-chatgpt-atlas-its-standalone-desktop-browser/)的残余部分——膨胀成了一个体积达 **1.5 GB 的 Electron 怪物**，这听起来一点也不“超级”。

> In contrast, the new ChatGPT superapp—which combines the simple chatbot, [ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/), Codex, and the remnants of the [now-discontinued Atlas standalone web browser](https://9to5mac.com/2026/07/09/openai-is-discontinuing-chatgpt-atlas-its-standalone-desktop-browser/)—collapses into a svelte **1.5 GB Electron bundle**, which doesn’t sound "super" at all.

---

*来源：[Daring Fireball](https://daringfireball.net/linked/2026/07/09/todays-the-day-openai-fucked-up-the-chatgpt-mac-app)*

> *Source: [Daring Fireball](https://daringfireball.net/linked/2026/07/09/todays-the-day-openai-fucked-up-the-chatgpt-mac-app)*
