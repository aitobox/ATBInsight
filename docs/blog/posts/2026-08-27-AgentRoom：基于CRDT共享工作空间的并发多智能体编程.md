---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- 多智能体协作
- 软件工程
- CRDT
- 大语言模型
- 协同编辑
title: AgentRoom：基于CRDT共享工作空间的并发多智能体编程
---
### 文章背景与核心概要
并发多智能体编程旨在通过分工、冗余和跨多个文件的并行探索来改进软件生成。然而，传统系统受到大语言模型（LLM）逐词（token-by-token）生成限制的瓶颈制约，迫使智能体要么通过阶段交接串行运行，要么在缺乏适当协调的孤立池中运行。因此，单个智能体往往会失败或放弃复杂的任务。

本文介绍了 **AgentRoom**，这是一种专门为并发编程智能体设计的实时协作编辑协议。通过在基于冲突无关复制数据类型（CRDT）合并的共享文件系统之上，将文件级别的声明、状态和广播公开为模型上下文协议（MCP）工具，AgentRoom成功协调了多智能体工作流。在Python DevBench和Rust+axum的任务中，对五个前沿编程CLI模型进行的评估表明，协调——而不是单纯的并行性或CRDT合并——才是提高任务完成率和可靠性的关键驱动力。

---

# AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared Workspace

**Authors:** Seonglae Cho, Donghyun Lee  
**Submitted on:** 24 August 2026  
**Subjects:** Artificial Intelligence (`cs.AI`); Software Engineering (`cs.SE`)  
**arXiv:** [2608.23740 [cs.AI]](https://arxiv.org/abs/2608.23740) | **DOI:** [10.48550/arXiv.2608.23740](https://doi.org/10.48550/arXiv.2608.23740)

> **Authors:** Seonglae Cho, Donghyun Lee  
> **Submitted on:** 24 August 2026  
> **Subjects:** Artificial Intelligence (`cs.AI`); Software Engineering (`cs.SE`)  
> **arXiv:** [2608.23740 [cs.AI]](https://arxiv.org/abs/2608.23740) | **DOI:** [10.48550/arXiv.2608.23740](https://doi.org/10.48550/arXiv.2608.23740)

---

## 📌 Summary

Concurrent multi-agent coding aims to improve software generation through division of labor, redundancy, and parallel exploration across multiple files. However, traditional systems are bottlenecked by the token-by-token generation limits of Large Language Models (LLMs), forcing agents to run either sequentially through phase handoffs or in isolated pools without proper coordination. As a result, single agents often fail or abandon complex tasks.

This paper introduces **AgentRoom**, a real-time collaborative editing protocol designed specifically for concurrent coding agents. By exposing file-level claims, statuses, and broadcasting as Model Context Protocol (MCP) tools on top of a Conflict-free Replicated Data Type (CRDT)–merged shared filesystem, AgentRoom successfully coordinates multi-agent workflows. Evaluations across five frontier coding-CLI models on tasks using Python DevBench and Rust+axum demonstrate that coordination—rather than raw parallelism or CRDT-merging alone—is the key driver of improved task completion and reliability.

> ## 📌 Summary
> 
> Concurrent multi-agent coding aims to improve software generation through division of labor, redundancy, and parallel exploration across multiple files. However, traditional systems are bottlenecked by the token-by-token generation limits of Large Language Models (LLMs), forcing agents to run either sequentially through phase handoffs or in isolated pools without proper coordination. As a result, single agents often fail or abandon complex tasks.
> 
> This paper introduces **AgentRoom**, a real-time collaborative editing protocol designed specifically for concurrent coding agents. By exposing file-level claims, statuses, and broadcasting as Model Context Protocol (MCP) tools on top of a Conflict-free Replicated Data Type (CRDT)–merged shared filesystem, AgentRoom successfully coordinates multi-agent workflows. Evaluations across five frontier coding-CLI models on tasks using Python DevBench and Rust+axum demonstrate that coordination—rather than raw parallelism or CRDT-merging alone—is the key driver of improved task completion and reliability.

---

## 🧭 Abstract

Concurrent multi-agent coding promises division of labor across modules, robustness through redundancy, and parallel exploration at the natural granularity of multi-file projects. Realtime collaborative editing protocols solve this coordination problem for human teams via Conflict-free Replicated Data Types (CRDTs), but the LLMs underneath generate one token at a time and existing multi-agent coding systems inherit this serial limit: they either sequence agents through phase handoffs or pool independent samples without coordination, and a single agent abandons up to half of hard tasks with a one-file stub-and-exit. 

AgentRoom is a realtime collaborative editing protocol for concurrent coding agents. Its runtime layer exposes file-level claim, status, and broadcast as MCP tools on a CRDT-merged shared filesystem. Five frontier coding-CLI models ran four backend coding tasks, with cross-language checks in Python DevBench and Rust+axum. For CLI-stable models, AgentRoom with 2 agents abandons fewer tasks than Solo and has less run-to-run variation. At matched-compute, one positive mean LLM-judge contrast puts AgentRoom over parallel-merge. The other contrast, a bundle probe, puts full AgentRoom above each partial case: an ordering rather than a percentage split. Coordination, not parallelism or CRDT-merge, bears the load.

> ## 🧭 Abstract
> 
> Concurrent multi-agent coding promises division of labor across modules, robustness through redundancy, and parallel exploration at the natural granularity of multi-file projects. Realtime collaborative editing protocols solve this coordination problem for human teams via Conflict-free Replicated Data Types (CRDTs), but the LLMs underneath generate one token at a time and existing multi-agent coding systems inherit this serial limit: they either sequence agents through phase handoffs or pool independent samples without coordination, and a single agent abandons up to half of hard tasks with a one-file stub-and-exit. 
> 
> AgentRoom is a realtime collaborative editing protocol for concurrent coding agents. Its runtime layer exposes file-level claim, status, and broadcast as MCP tools on a CRDT-merged shared filesystem. Five frontier coding-CLI models ran four backend coding tasks, with cross-language checks in Python DevBench and Rust+axum. For CLI-stable models, AgentRoom with 2 agents abandons fewer tasks than Solo and has less run-to-run variation. At matched-compute, one positive mean LLM-judge contrast puts AgentRoom over parallel-merge. The other contrast, a bundle probe, puts full AgentRoom above each partial case: an ordering rather than a percentage split. Coordination, not parallelism or CRDT-merge, bears the load.

---

## 🔗 Links & Resources

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.23740) | [HTML (Experimental)](https://arxiv.org/html/2608.23740v1) | [TeX Source](https://arxiv.org/src/2608.23740)
* **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) *(License icon preserved below per instructions)*:  
  <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> ## 🔗 Links & Resources
> 
> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.23740) | [HTML (Experimental)](https://arxiv.org/html/2608.23740v1) | [TeX Source](https://arxiv.org/src/2608.23740)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) *(License icon preserved below per instructions)*:  
>   <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">