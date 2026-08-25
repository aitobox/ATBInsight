---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 大语言模型
- 推理优化
- 缓存机制
- 模型加速
- 程序思维
title: CacheSpec：在大语言模型中为小模型寻找最佳平衡点
---
### 文章背景与核心概要

CacheSpec 是一种创新的推理优化框架，旨在降低大语言模型（LLM）在程序辅助推理、智能体决策及结构化任务执行过程中的高昂运营成本。该研究观察到，许多请求在计算结构上具有高度相似性，仅输入内容存在差异。为此，CacheSpec 将“思维程序”（Program-of-Thoughts, PoT）转化为可复用的缓存对象，从而实现计算资源的有效利用。

该框架的核心在于利用单一的小型模型承担双重角色：在缓存命中路径上进行语义变量提取，并在目标大模型生成过程中执行推测性草稿（Speculative Drafting）。实验结果表明，CacheSpec 在保持或超越现有基准任务质量的同时，实现了高达 3.1 倍的延迟加速和约 2.8 倍的吞吐量提升。这一发现强调了小模型在大型模型系统中作为轻量级、结构化及可验证辅助组件的巨大潜力。

---

# CacheSpec：在大语言模型中为小模型寻找最佳平衡点

## 摘要

CacheSpec 是一种创新的推理优化框架，旨在降低大语言模型（LLM）在程序辅助推理、智能体决策及结构化任务执行过程中的高昂运营成本。研究认识到，许多请求在计算结构上具有相似性，但输入内容各异。CacheSpec 将“思维程序”（PoT）转化为可复用的缓存对象。它利用单一的小型模型执行双重角色：在缓存命中路径上进行**语义变量提取**，并在目标 LLM 生成期间进行**推测性草稿**。

> **CacheSpec** is an innovative inference optimization framework designed to reduce the high operational costs associated with Large Language Models (LLMs) during program-aided reasoning, agentic decision-making, and structured task execution. Recognizing that many requests share similar computational structures with varying inputs, CacheSpec transforms Program-of-Thoughts (PoT) programs into reusable cache objects. It leverages a single small model to perform dual roles: **semantic variable extraction** on cache-hit paths and **speculative drafting** during target-LLM generation. 

实验证明，CacheSpec 在保持或超越现有基准任务质量的同时，实现了高达 **3.1 倍的延迟加速**，并将服务吞吐量提高了约 **2.8 倍**。研究结果强调，小模型的最佳用途并非进行独立的复杂推理，而是在大模型系统中承担轻量级、结构化且可验证的辅助操作。

> Experiments demonstrate that CacheSpec achieves up to a **3.1$\times$ latency speedup** and improves serving throughput by roughly **2.8$\times$**, all while maintaining or exceeding the task quality of existing baselines. The findings highlight that smaller models are best utilized not for independent complex reasoning, but for lightweight, structured, and verifiable auxiliary operations within large-model systems.

---

## 论文元数据

* **arXiv ID:** [arXiv:2607.20507](https://arxiv.org/abs/2607.20507) [cs.AI]
* **作者:** Jingquan Chen, Jie Feng, Jinghua Piao, Shaogang Hu, Yong Li
* **主要学科:** 人工智能 (`cs.AI`) / 机器学习 (`cs.LG`)
* **会议录用:** 已被 **EMNLP 2026** 录用
* **提交日期:** 2026年7月3日提交；2026年8月22日最后修订 (v2)
* **许可与资源:** 
  * [查看 PDF](https://arxiv.org/pdf/2607.20507)
  * [官方代码仓库](https://github.com/chenjqQAQ/CacheSpec)
  * ![license icon](./images/345c7ad61f1b.png) [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/)

> ## Paper Metadata
>
> * **arXiv ID:** [arXiv:2607.20507](https://arxiv.org/abs/2607.20507) [cs.AI]
> * **Authors:** Jingquan Chen, Jie Feng, Jinghua Piao, Shaogang Hu, Yong Li
> * **Primary Subject:** Artificial Intelligence (`cs.AI`) / Machine Learning (`cs.LG`)
> * **Conference Acceptance:** Accepted by **EMNLP 2026**
> * **Submission Dates:** Submitted on July 3, 2026; Last revised on August 22, 2026 (v2)
> * **License & Resources:** 
>   * [View PDF](https://arxiv.org/pdf/2607.20507)
>   * [Official Code Repository](https://github.com/chenjqQAQ/CacheSpec)
>   * ![license icon](./images/345c7ad61f1b.png) [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)

---

## 核心贡献与框架概述

* **程序级缓存：** 将一次性推理产物（PoT 风格程序）转换为可复用的缓存对象，能够处理具有不同变量、约束或上下文的新请求。
* **双角色小模型集成：** 重复利用同一个轻量级模型执行两项关键性能任务：
  1. 缓存命中路径上的*语义变量提取*。
  2. 加速目标 LLM 生成的*推测性草稿*。
* **评估数据集：** 在购物风格请求数据集、WebShop、Formula 和 CodeTAT-QA 上进行了广泛验证。
* **性能提升：** 
  * 推理延迟降低高达 **3.1 倍**。
  * 与传统的 PoT 风格方法相比，并行服务吞吐量提高了约 **2.8 倍**。

> ## Key Contributions & Framework Overview
>
> * **Program-Level Caching:** Converts one-time reasoning artifacts (PoT-style programs) into reusable cache objects capable of handling new requests with differing variables, constraints, or contexts.
> * **Dual-Role Small Model Integration:** Reuses the same lightweight model for two crucial performance tasks:
>   1. *Semantic variable extraction* along the cache-hit path.
>   2. *Speculative drafting* to accelerate target-LLM generation.
> * **Evaluated Datasets:** Validated extensively across shopping-style request datasets, WebShop, Formula, and CodeTAT-QA.
> * **Performance Gains:** 
>   * Up to **3.1$\times$** reduction in inference latency.
>   * Around **2.8$\times$** increase in parallel serving throughput compared to traditional PoT-style methods.