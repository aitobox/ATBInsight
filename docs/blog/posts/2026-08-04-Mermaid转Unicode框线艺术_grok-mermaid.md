---
authors:
- aitoboxrobot
categories:
- 深度研报
date: '2026-08-04'
hide:
- navigation
tags:
- AI
- Claude
- xAI
- Rust
title: Mermaid转Unicode框线艺术 (grok-mermaid)
---
# Mermaid转Unicode框线艺术 (grok-mermaid)

### 背景与摘要
本文介绍了一个名为 `grok-mermaid` 的基于浏览器的工具，它可以将 Mermaid 图表转化为使用 Unicode 字符绘制的文本图。通过利用 WebAssembly 技术，作者将最近开源的 Grok CLI 中的终端渲染功能移植到了网页端，为用户提供了一个能直接在浏览器中生成高质量文本图表的工具。

### Summary
这个项目展示了一个基于浏览器的工具，它可以将 Mermaid 图表转换为 Unicode 框线艺术。通过将一个基于 Rust 的终端渲染器从开源的 Grok CLI 代码库移植到 WebAssembly，该工具使得可以直接在浏览器中进行高质量的、基于文本的图表渲染。
> This project showcases a browser-based tool that converts Mermaid diagrams into Unicode box art. By porting a Rust-based terminal renderer from the open-sourced Grok CLI codebase to WebAssembly, this tool enables high-quality, text-based diagram rendering directly in the browser.

---

### Overview
在探索新开源的 [Grok CLI 编码代理](https://simonwillison.net/2026/Jul/15/grok-build/)代码库时，我发现了一个引人入胜的组件：`xai-grok-markdown/src/mermaid.rs`。这个文件包含了一个用 Rust 编写的自包含的终端渲染器，用于渲染 Mermaid 图表。
> While exploring the codebase for the newly open-sourced [Grok CLI coding agent](https://simonwillison.net/2026/Jul/15/grok-build/), I discovered a fascinating component: `xai-grok-markdown/src/mermaid.rs`. This file contains a self-contained terminal renderer for Mermaid diagrams written in Rust.

我决定使用 WebAssembly 将这个功能引入浏览器。您可以在这里尝试最终的工具：**[Mermaid to Unicode box art (grok-mermaid)](https://tools.simonwillison.net/grok-mermaid)**。
> I decided to bring this functionality to the browser using WebAssembly. You can try the resulting tool here: **[Mermaid to Unicode box art (grok-mermaid)](https://tools.simonwillison.net/grok-mermaid)**.

### Development Process
该实现是通过利用 AI 辅助编码完成的。您可以[在此 Pull Request 中](https://github.com/simonw/tools/pull/293#issue-4897479396)查看我在 Claude Code (Fable 5) 中使用的具体提示词。
> The implementation was achieved by leveraging AI-assisted coding. You can view the specific prompt I used in Claude Code (Fable 5) [in this pull request](https://github.com/simonw/tools/pull/293#issue-4897479396).

### Preview
![Screenshot of a Mermaid diagram editor showing source code and rendered flowchart. The code reads: graph TD Start[Request received] --> Auth{Authenticated?} Auth -->|yes| Rate{Rate limit OK?} Auth -->|no| R401[401 Unauthorized] Rate -->|yes| H(Handle request) Rate -->|no| R429[429 Too Many Requests] H -.-&gt; Log[Audit log] H ==&gt; Resp[200 OK]. Below the code are controls labeled Max width: Fit output panel, Copy as text, and Copy link to this diagram. The rendered flowchart on a dark background flows top-down: Request received leads to Authenticated?, which branches yes to Rate limit OK? and no to 401 Unauthorized. Rate limit OK? branches yes to Handle request and no to 429 Too Many Requests. Handle request connects with a dotted arrow to Audit log and a thick arrow to 200 OK.](./images/9b0ca2599168.png)

---

**Tags:** #tools #rust #webassembly #mermaid #grok #xai
> **Tags:** #tools #rust #webassembly #mermaid #grok #xai
