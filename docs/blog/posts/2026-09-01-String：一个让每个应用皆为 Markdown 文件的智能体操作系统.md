---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- AI Agent
- 操作系统
- Markdown
- 架构设计
- Token优化
title: String：一个让每个应用皆为 Markdown 文件的智能体操作系统
---
### 文章背景与核心概要
大语言模型（LLM）智能体正日益成为新型的软件用户，然而它们目前被迫在专为人类设计的图形界面或僵化的 API 架构中进行导航。这种错位导致智能体浪费了大量的 Token 去反复重新阅读整页内容和工具定义。为了解决这一痛点，研究人员推出了 **String**——一个专门为智能体用户设计的开源运行时操作系统。

String 通过一种名为 **SFMD（String-Flavored Markdown，String 风格 Markdown）** 的统一架构，将应用程序、文件、命令行（shell）以及网页融为一体。它将工具知识集中化管理，并通过两个核心动词（`/open` 用于查看，`/act` 用于执行）动态渲染局部视图，从而在大幅降低 Token 开销的同时，提升了任务执行的准确性、安全性和效率。在包含 87 个任务的基准测试中，String 在保持极高成功率的同时，使完成任务时的 Token 消耗减少了 33.5%，且常驻智能体接口在任何目录规模下均能稳定在 53 个 Token。

---

# String: An Agentic OS Where Every App Is a Markdown File

**arXiv ID:** [2608.28027](https://arxiv.org/abs/2608.28027)  
**Subject:** Artificial Intelligence (`cs.AI`)  
**Authors:** Jookyung Song, Nojun Kwak, Simyung Chang  
**Submitted:** August 28, 2026  

---

## 📌 Executive Summary

> Large Language Model (LLM) agents are increasingly acting as software users, but they are forced to navigate interfaces designed for humans or rigid API schemas. This mismatch forces agents to waste valuable tokens repeatedly re-reading full pages and tool definitions. 
> 
> To solve this, researchers present **String**, an open-source runtime operating system designed specifically for agentic users. String treats applications, files, shells, and the web through a unified architecture powered by **SFMD (String-Flavored Markdown)**. By centralizing tool knowledge and rendering partial views dynamically through two core verbs—`/open` (to view) and `/act` (to execute)—String dramatically reduces token overhead while improving task accuracy, security, and efficiency.

---

## 📄 Abstract

> LLM agents have become a new class of software user, but every surface they work through was designed for someone else. Pages are built for human eyes, which can skim and ignore; tool schemas for programs, which pay nothing to carry definitions they never call. An agent has neither luxury: it re-reads, and pays again for, everything it is shown on every turn. 
>
> We present **String**, an open-source runtime that gives this user an interface of its own and treats the job as an operating-systems problem. Tool knowledge moves out of the agent's context and into a common layer that renders it back one view at a time as Markdown. A single SFMD (String-Flavored Markdown) document declares an application's views, typed actions, navigation, and credentials, and the runtime handles discovery, validation, execution, state, and secrets behind two core verbs: `/open` to see and `/act` to do. 
>
> Web and app turn out to be two renderings of one architecture: an SFMD site serves styled HTML to browsers and the raw document to agents, so one grammar reaches apps, files, shells, and the web, even legacy HTML, with no per-site integration. Views stay partial by design, and the staging is causal: disclosing one tier of detail a single turn too early costs up to 23 accuracy points, while proper staging drops wrong-action selection from 28% to 2%. Privilege follows provenance: a remote page may call HTTP but never the shell, and caller-supplied text never expands a stored secret. 
>
> On an 87-task benchmark that pairs each task with curated skills, operationalizing those procedures as on-demand String apps yields comparable aggregate success across six models from frontier to small (+1.3pp) while using 33.5% fewer tokens among completed episodes, and the resident interface stays a constant 53 tokens at any catalog size. We report the design, the evaluation, and what three months of production use taught us.

---

## ⚙️ Core Architecture & Features

> - **Unified SFMD Grammar:** A single *String-Flavored Markdown* document declares an application's views, typed actions, navigation pathways, and credentials.
> - **Two Core Verbs:** 
>   - `/open`: Inspects and views current states or information.
>   - `/act`: Executes specified typed actions.
> - **Dual-Rendering Web & App Layer:** SFMD serves styled HTML natively to human web browsers while passing raw documents directly to AI agents—requiring zero per-site integration.
> - **Causal Staging & Partial Views:** Designed to prevent information overload. Disclosing details too early degrades accuracy by up to 23 points, whereas proper staging drops wrong-action selections from 28% down to 2%.
> - **Provenance-Based Security:** Strict boundary controls ensure remote pages can execute HTTP calls but are barred from accessing the shell, and untrusted text inputs can never accidentally expose stored secrets.

---

## 📊 Performance & Results

> Tested on an 87-task benchmark mapping curated skills to on-demand String applications:
> - **Success Rate:** Achieved comparable aggregate success across six distinct models (ranging from frontier to small-scale models, a +1.3 percentage point improvement).
> - **Token Efficiency:** Consumed **33.5% fewer tokens** across completed task episodes.
> - **Constant Footprint:** The resident agent interface maintained a static footprint of just **53 tokens**, regardless of the underlying catalog size.

---

## 🔗 Full-Text & Resources

> * [View PDF](https://arxiv.org/pdf/2608.28027)
> * [arXiv HTML (Experimental)](https://arxiv.org/html/2608.28027v1)
> * [TeX Source](https://arxiv.org/src/2608.28027)
> * [DOI Reference](https://doi.org/10.48550/arXiv.2608.28027)

<div class="abs-license">
<a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article">
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
<span>view license</span>
</a>
</div>