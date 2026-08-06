---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-06
hide:
- navigation
tags:
- Claude
- AI Agent
- 游戏开发
- Three.js
- Vibe Coding
title: 一次性成功搞定“浣熊大劫案”：使用 Claude Fable 5 构建游戏
---
# 一次性成功搞定“浣熊大劫案”：使用 Claude Fable 5 构建游戏

> # One-Shotting a Raccoon Heist: Building a Game with Claude Fable 5

### 文章背景与核心概要
本文记录了知名开发者 Simon Willison 在 2022 年实验四周年来临之际，使用 **Claude Fable 5**（通过网页版 Claude Code）复现并构建“浣熊大劫案”（Raccoon Heist）游戏的全新尝试。仅凭借四年前由 GPT-3 生成的产品描述提示词与 DALL-E 概念图，AI Agent 全自主创建了一个包含 3D 渲染、过程化生成的 WebAudio 爵士音效、移动端触控及动态警犬寻路机制的完整网页游戏。尽管从游戏性设计角度而言其娱乐性依然需要人类经验雕琢，但该实验充分展现了 AI Agent 极强的全自主快速原型构建与“Vibe Coding”能力。

---

### 概要

> ### Summary

在 2022 年一项实验的四周年之际（当时作者使用 GPT-3 和 DALL-E 构思了一个“浣熊大劫案”游戏概念），Simon Willison 向 **Claude Fable 5**（通过网页版 Claude Code）发起挑战，要求仅根据那些原始提示词直接构建出实际的游戏。最终的结果是一个功能完整、基于浏览器的 3D 游戏，具备过程化音频、触控操作和 AI 生成的资产——所有这一切均由 AI Agent 自主创建完成。

> On the fourth anniversary of a 2022 experiment where GPT-3 and DALL-E were used to conceptualize a "Raccoon Heist" game, Simon Willison challenged **Claude Fable 5** (via Claude Code for web) to build the actual game from those original prompts. The result is a fully functional, 3D browser-based game featuring procedural audio, touch controls, and AI-generated assets—all created autonomously by the agent.

---

### 缘起

> ### The Origin Story

2022 年 8 月，作者仅使用了一条简单的 GPT-3 提示词（“写一份详细的电脑游戏产品描述，讲述一队浣熊去搞抢劫的故事”）和一张 DALL-E 图片需求，构思出了一款游戏的雏形。四年后，作者的目标是看看 AI Agent 能否在无需人类设计干预的情况下，将这些静态产物直接转化为可玩的现实游戏。

> In August 2022, a simple GPT-3 prompt ("Write a detailed product description of a computer game where a team of raccoons go on heists") and a DALL-E image request were used to prototype a game concept. Four years later, the goal was to see if an AI agent could take those static artifacts and turn them into a playable reality without human design intervention.

---

### 构建过程

> ### The Build Process

该项目结合使用 **Claude Code for web** 与 **GitHub Pages** 以实现快速迭代。通过创建一个代码仓库并指示 Agent“尽可能频繁地 commit 并 push”，开发者可以实时预览游戏的演进过程。

> The project utilized **Claude Code for web** combined with **GitHub Pages** for rapid iteration. By setting up a repository and instructing the agent to "commit and push as often as possible," the developer could preview the game's evolution in real-time.

**关键工作流步骤：**
1. **仓库搭建：** 创建了一个全新的 GitHub 仓库。
2. **Agent 自主权：** 提供提示词指示 Agent 独立工作，管理其用于生成图像的 API 密钥，并维护一个 `notes.md` 文件以保持透明度。
3. **迭代测试：** Agent 使用 **Playwright** 执行“冒烟测试”，为其自己的工作成果截屏，以调试移动端响应式布局和游戏核心机制。

> **Key workflow steps:**
> 1. **Repository Setup:** Created a new GitHub repo.
> 2. **Agent Autonomy:** Provided a prompt instructing the agent to work independently, manage its own API keys for image generation, and maintain a `notes.md` file for transparency.
> 3. **Iterative Testing:** The agent used **Playwright** to perform "smoke tests," taking screenshots of its own work to debug mobile responsiveness and gameplay mechanics.

---

### 技术亮点

> ### Technical Highlights

*   **引擎：** 使用 [Three.js](https://threejs.org/) 构建。
*   **资产：** 使用 `gpt-image-2` 生成纹理和标题艺术图。
*   **音频：** 实现了过程化生成的 WebAudio 原声带（潜行爵士乐）和音效，无需任何外部音频文件。
*   **游戏玩法：** 包含针对移动端的动态触控摇杆、“冲刺”机制，以及包含会追踪气味的看门犬在内的难度递增系统。

> *   **Engine:** Built using [Three.js](https://threejs.org/).
> *   **Assets:** Used `gpt-image-2` to generate textures and title art.
> *   **Audio:** Implemented a procedural WebAudio soundtrack (sneaky jazz) and sound effects, requiring zero external audio files.
> *   **Gameplay:** Includes a dynamic touch joystick for mobile, a "dash" mechanic, and an escalating difficulty system featuring a scent-tracking guard dog.

---

### 思考：“Vibe Coding”是未来吗？

> ### Reflection: Is "Vibe Coding" the Future?

尽管最终生成的游戏在技术上令人印象深刻——拥有 3D 渲染、过程化音频和移动端兼容性——但作者指出，从单纯的游戏玩法角度来看，它依然显得“平庸”。

> While the resulting game is technically impressive—featuring 3D rendering, procedural audio, and mobile compatibility—the author notes that it remains "mediocre" from a pure gameplay perspective.

> “事实证明，设计出*好玩*的游戏仍然是人类独有的特质，这需要比 Claude 或我所能提供的多得多的技巧与经验。”

> > "It turns out designing games that are *fun* remains a uniquely human trait, and one which requires significantly more skill and experience than either Claude or I can bring to bear."

尽管如此，该实验凸显了 AI Agent 作为快速原型设计工具的巨大潜力。它作为一种低风险、高回报探索 Agentic 能力的方式，证明了虽然 AI 可能还不是大师级游戏设计师，但它绝对是一个能力超群的“Vibe Coder”。

> Despite this, the experiment highlights the incredible potential of AI agents as rapid prototyping tools. It serves as a low-risk, high-reward way to explore agentic capabilities, proving that while AI may not yet be a master game designer, it is an exceptionally capable "vibe coder."

---

### 相关资源

> ### Resources

*   **[开始体验游戏](https://simonw.github.io/raccoon-heist/)**
*   **[GitHub 代码仓库](https://github.com/simonw/raccoon-heist/)**
*   **[完整构建过程记录](https://simonw.github.io/raccoon-heist/transcript/page-001.html)**

> *   **[Play the Game](https://simonw.github.io/raccoon-heist/)**
> *   **[GitHub Repository](https://github.com/simonw/raccoon-heist/)**
> *   **[Full Build Transcript](https://simonw.github.io/raccoon-heist/transcript/page-001.html)**
