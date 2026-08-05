---
authors:
- aitoboxrobot
categories:
- 商业动态
date: '2026-08-04'
hide:
- navigation
tags:
- AI
- OpenAI
- GPT
- Rust
title: 围绕“ChatGPT Classic”的困惑
---
# 围绕“ChatGPT Classic”的困惑

**背景与摘要：**
OpenAI 向其全新的 macOS 桌面版“超级”应用过渡的过程充满了文档说明前后矛盾以及令人沮丧的安装体验。尽管官方支持文档暗示用户可以将新应用与旧版的“ChatGPT Classic”同时运行，但真实世界中的测试却暴露出了一个非确定性的过程：安装程序往往会完全覆盖旧版本，让用户很难保留或恢复原有的经典界面。

> ### Summary
> OpenAI’s transition to its new "super" desktop app for macOS has been marked by inconsistent documentation and a frustrating installation experience. While official support documents suggest that users can run the new app alongside the legacy "ChatGPT Classic," real-world testing reveals a non-deterministic process that often overwrites the old version entirely, leaving users unable to easily retain or recover the classic interface.

---

### 官方立场

根据 OpenAI 帮助中心的说法，这次过渡本应该是无缝的。系统会指示用户按照应用内的提示下载新版本。官方文档声称，这款集成了 Chat、Work 和 Codex 等功能的新应用可以与现有应用程序并排安装，允许两者共存：

> ### The Official Stance
> According to OpenAI’s Help Center, the transition should be seamless. Users are instructed to follow an in-app prompt to download the new version. The documentation claims that the new app—which includes integrated Chat, Work, and Codex features—may install alongside the existing application, allowing both to coexist:

*   **ChatGPT:** 功能丰富的新版桌面应用程序。
*   **ChatGPT Classic:** 上一个版本，该版本将继续接收模型更新、安全补丁和错误修复，尽管它可能缺乏最新的基于智能体的功能。

> *   **ChatGPT:** The new, feature-rich desktop application.
> *   **ChatGPT Classic:** The previous version, which continues to receive model updates, security patches, and bug fixes, though it may lack the latest agent-based features.

### 升级的现实情况

与官方文档相反，实际的用户体验充满了技术上的不一致：

> ### The Reality of the Upgrade
> Contrary to the official documentation, the actual user experience is fraught with technical inconsistencies:

*   **缺失提示:** 在旧版应用中点击“检查更新 (Check for Updates)”命令，并不会触发下载全新“超级”应用的提示；它只是单纯地将经典版应用更新到了它的最新迭代。
*   **安装冲突:** 通过磁盘映像手动下载新应用并不会如预期般运作。当旧版应用正在运行时，安装程序无法正确部署新版本。
*   **强制覆盖:** 当旧版应用关闭时，安装程序往往会彻底替换掉经典版本，而不是将新应用与它并排安装。结果就是，“ChatGPT Classic”应用被移到了废纸篓，导致用户无法还原，也无法同时运行这两者。

> *   **Missing Prompts:** The "Check for Updates" command in the legacy app does not trigger a prompt to download the new "super" app; it simply updates the classic app to its latest iteration.
> *   **Installation Conflicts:** Manually downloading the new app via a disk image does not behave as expected. When the old app is running, the installer fails to properly deploy the new version.
> *   **Forced Overwrites:** When the old app is closed, the installer often replaces the classic version entirely rather than installing the new app alongside it. Consequently, the "ChatGPT Classic" app is moved to the Trash, leaving the user with no way to revert or run both simultaneously.

### 缺乏清晰度

OpenAI 措辞上的模棱两可——使用诸如“可能会安装 (may install)”和“如果两者都保持安装状态 (if both remain installed)”之类的表述——表明，甚至连开发者自己也不确定安装时的具体行为。

> ### A Lack of Clarity
> The ambiguity in OpenAI’s language—using terms like "may install" and "if both remain installed"—suggests that even the developers are uncertain about the installation behavior. 

对于一款拥有如此庞大用户基础的产品来说，这次重大更新的推出让人感觉脱节且不连贯。对于那些尚未安装“Classic”版本但希望保留经典体验的用户而言，目前没有一条清晰且可靠的途径，整个更新过程依然是一个令人沮丧的、充满不确定性的盲盒。

> For a product with such a massive user base, the rollout of this major update feels disjointed. There is currently no clear, reliable path for users who wish to retain the "Classic" experience if they do not already have it installed, and the update process remains frustratingly non-deterministic.

***

*来源：[Daring Fireball](https://daringfireball.net/linked/2026/07/11/can-someone-explain-to-me-how-to-get-chatgpt-classic)*

> ***
> 
> *Source: [Daring Fireball](https://daringfireball.net/linked/2026/07/11/can-someone-explain-to-me-how-to-get-chatgpt-classic)*
