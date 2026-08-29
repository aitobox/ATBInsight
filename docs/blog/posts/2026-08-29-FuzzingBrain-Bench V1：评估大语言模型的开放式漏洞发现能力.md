---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 大语言模型
- 软件测试
- 模糊测试
- 漏洞发现
- 基准测试
title: FuzzingBrain-Bench V1：评估大语言模型的开放式漏洞发现能力
---
### 文章背景与核心概要
大语言模型（LLM）在软件工程领域的应用日益广泛，其中评估其发现软件漏洞的能力成为了研究热点。然而，传统的基准测试通常采用预定义目标漏洞的方式，这往往会忽略模型在实际测试中发现的其他合法但未预料到的崩溃，从而无法准确反映模型的真实能力。

为了克服这一局限性，研究人员推出了 **FuzzingBrain-Bench**。这是一个旨在评估大语言模型在真实开放环境中发现软件漏洞能力的基准测试。在该基准测试中，模型需要在包含开源项目和净化器（Sanitizer）插桩测试封装的独立 Docker 环境中，尽可能多地生成触发不同崩溃的输入。

FuzzingBrain-Bench V1 版本涵盖了来自 43 个开源项目的 77 个挑战任务（包括 36 个 C 语言、32 个 C++ 语言以及 9 个 Java/JVM 挑战）。通过对 Claude Opus 4.8 等顶尖模型的评估表明，该基准能够有效衡量模型在开放式漏洞发现方面的真实水平。

---

# FuzzingBrain-Bench V1: Evaluating Open-Ended Bug Discovery by LLMs

## Summary

> **FuzzingBrain-Bench** is a benchmark designed to evaluate the capability of Large Language Models (LLMs) to discover software bugs in an open-ended, real-world setting. Traditional benchmarks often rely on generating proof-of-concept inputs targeting predefined vulnerabilities, which can overlook valid alternative crashes discovered by the model. 
>
> To overcome this limitation, FuzzingBrain-Bench tasks models with generating inputs that trigger as many distinct crashes as possible within self-contained Docker environments containing open-source projects and sanitizer-instrumented harnesses. Version 1 of the benchmark features **77 challenges** across **43 open-source projects** (36 C, 32 C++, and 9 Java/JVM challenges). Evaluations of state-of-the-art models like Claude Opus 4.8 demonstrate its effectiveness in measuring open-ended bug discovery capabilities.

---

## Paper Metadata
## 论文元数据

* **arXiv 标识符:** [arXiv:2608.25158](https://arxiv.org/abs/2608.25158) [cs.AI]
* **提交日期:** 2026年8月25日
* **主学科:** 人工智能 (`cs.AI`)
* **次学科:** 密码学与安全 (`cs.CR`)、机器学习 (`cs.LG`)、软件工程 (`cs.SE`)
* **作者:** 
  * Ze Sheng (同等贡献)
  * Aleksandar Kezic (同等贡献)
  * Zhicheng Chen
  * Jeff Huang

> * **arXiv Identifier:** [arXiv:2608.25158](https://arxiv.org/abs/2608.25158) [cs.AI]
> * **Submission Date:** August 25, 2026
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Secondary Subjects:** Cryptography and Security (`cs.CR`), Machine Learning (`cs.LG`), Software Engineering (`cs.SE`)
> * **Authors:** 
>   * Ze Sheng (equal contribution)
>   * Aleksandar Kezic (equal contribution)
>   * Zhicheng Chen
>   * Jeff Huang

---

## Abstract
## 摘要

评估大语言模型（LLM）发现软件漏洞的能力变得愈发重要。现有的基准测试通常通过要求模型生成针对预定义目标漏洞的概念验证（PoC）输入来评估这种能力。然而，这种设置可能会忽视模型发现的、与预定义目标不匹配的其他有效崩溃。因此，这种评估可能无法真实反映模型的实际能力。

我们提出了 FuzzingBrain-Bench，这是一个用于评估人工智能模型在开源软件中发现漏洞能力的基准测试。模型将在一个自包含的 Docker 镜像中获得一个开源项目和一个经过净化器插桩的测试封装（harness）。它们的目标是通过该封装生成能够触发尽可能多不同崩溃的输入。模型在每个挑战中的表现根据其产生的不同崩溃签名数量进行评分，并设定了预定义上限，同时通过难度系数进行加权。

FuzzingBrain-Bench V1 包含来自 43 个开源项目的 77 个挑战，其中包括 36 个 C、32 个 C++ 和 9 个 Java/JVM 挑战。我们在整个基准测试上评估了 Claude Haiku 4.5、Claude Sonnet 4.6 和 Claude Opus 4.8。其中 Claude Opus 4.8 表现最好，在 77 个挑战中的 60 个里触发了崩溃，并在 579 分的总分中取得了 196 分。三个模型在其中的 13 个挑战中均未触发任何崩溃。

> Evaluating the ability of large language models (LLMs) to discover software bugs is increasingly important. Existing benchmarks typically evaluate this capability by asking the model to generate a proof-of-concept input that triggers a predefined target vulnerability. However, this setup may overlook valid crashes discovered by the model when they do not match the predefined target. As a result, the evaluation may not reflect the model's real capability.
>
> We present FuzzingBrain-Bench, a benchmark for assessing AI models' ability to discover bugs in open-source software. Models are given an open-source project and a sanitizer-instrumented harness in a self-contained Docker image. Their goal is to generate inputs that trigger as many distinct crashes as possible through the harness. A model's performance on each challenge is scored based on the number of distinct crash signatures it produces, capped at a predefined maximum and weighted by a difficulty coefficient.
>
> FuzzingBrain-Bench V1 consists of 77 challenges drawn from 43 open-source projects, with 36 C, 32 C++, and 9 Java/JVM challenges. We evaluate Claude Haiku 4.5, Claude Sonnet 4.6, and Claude Opus 4.8 on the full benchmark. Claude Opus 4.8 performs best, triggering crashes in 60 of 77 challenges and achieving a score of 196 out of 579. None of the three models triggers a crash in 13 challenges.

---

## Resources & Links
## 资源与链接

* **全文 PDF:** [查看 PDF](https://arxiv.org/pdf/2608.25158)
* **HTML 版本:** [arXiv HTML (实验性)](https://arxiv.org/html/2608.25158v1)
* **基准测试语料库与封装:** [GitHub 仓库](https://github.com/fuzzingbrain/FuzzingBrain-Bench)
* **DOI:** [10.48550/arXiv.2608.25158](https://doi.org/10.48550/arXiv.2608.25158)

> * **Full-Text PDF:** [View PDF](https://arxiv.org/pdf/2608.25158)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.25158v1)
> * **Benchmark Corpus & Harnesses:** [GitHub Repository](https://github.com/fuzzingbrain/FuzzingBrain-Bench)
> * **DOI:** [10.48550/arXiv.2608.25158](https://doi.org/10.48550/arXiv.2608.25158)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/>