---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- CodeQL
- 漏洞检测
- 大语言模型
- 代码分析
- C/C++
title: ARQ：用于C/C++漏洞检测的智能体CodeQL查询优化框架
---
### 文章背景与核心概要

静态分析工具（如 CodeQL）在识别 C/C++ 软件中的安全漏洞方面发挥着至关重要的作用，但它们长期面临着**误报（False Positives, FP）**（将安全代码误标记为漏洞）和**漏报（False Negatives, FN）**（未能检测出实际漏洞）的双重挑战。

为了解决这一痛点，本文推出了 **ARQ**——一个基于执行落地证据（execution-grounded evidence）自动优化 C/C++ CodeQL 查询的智能体框架。该方法的核心见解在于：通过合成特定的 C/C++ 程序，当程序的实际执行行为与查询的判定结果产生冲突时，就能暴露出查询逻辑的缺陷。如果程序确实存在漏洞但查询却保持沉默，说明该查询存在漏报缺陷；反之，如果程序是安全的但查询却发出警报，则存在误报缺陷。在此基础上，ARQ 运行一个基于大语言模型（LLM）的优化循环，利用这些不一致性作为真实地面证据（ground truth）来修复底层查询，且完全不依赖标注数据集、提交历史或预定义的模板。

实验结果表明，在集成商业大模型（GPT-5.4、Claude-Sonnet-4.6 和 Gemini-3.5-flash）对 12 个官方 CodeQL 查询进行优化后，ARQ 成功将真实正向检测率提升了高达 **119.8%**，同时维持了至少 **98.0%** 的准确率（Precision）。此外，ARQ 还成功解决了官方 CodeQL 仓库中长期未决（长达 27 个月）的三个 GitHub Issue，并在真实世界库（`libpng` 和 `zlib`）中发现了两个先前未知的漏洞。

---

## 📌 摘要与概览 (Summary)

> Static analyzers like CodeQL are crucial for identifying vulnerabilities in C/C++ software, but they frequently suffer from **False Positives (FPs)** (flagging safe code) and **False Negatives (FNs)** (missing actual vulnerabilities). 
> 
> This paper introduces **ARQ**, an automated, agentic framework designed to refine C/C++ CodeQL queries using execution-grounded evidence. By utilizing synthesized C/C++ programs, ARQ detects disagreements between program execution behavior and query verdicts. It then leverages an LLM-based refinement loop to patch the underlying queries without relying on labeled datasets, commit histories, or predefined templates. 
> 
> Tested across commercial LLMs (GPT-5.4, Claude-Sonnet-4.6, and Gemini-3.5-flash) on 12 official CodeQL queries, ARQ successfully increased true positive detection by up to **119.8%** while maintaining a precision rate of at least **98.0%**. Furthermore, ARQ resolved three long-standing GitHub issues (open for up to 27 months) in the official CodeQL repository and discovered two previously unknown bugs in real-world libraries (`libpng` and `zlib`).

像 CodeQL 这样的静态分析器对于识别 C/C++ 软件中的漏洞至关重要，但它们经常遭受**误报 (FP)**（标记安全代码）和**漏报 (FN)**（遗漏实际漏洞）的困扰。

本文介绍了 **ARQ**，这是一个自动化的智能体框架，旨在利用来自合成 C/C++ 程序的基于执行落地的证据来优化 C/C++ CodeQL 查询。通过利用合成的 C/C++ 程序，ARQ 可以检测程序执行行为与查询判定之间的不一致。然后，它利用基于 LLM 的优化循环来修补底层查询，而无需依赖标注数据集、提交历史或预定义模板。

在商业 LLM（GPT-5.4、Claude-Sonnet-4.6 和 Gemini-3.5-flash）上对 12 个官方 CodeQL 查询进行测试时，ARQ 成功将真阳性检测率提高了最多 **119.8%**，同时保持了至少 **98.0%** 的准确率。此外，ARQ 解决了官方 CodeQL 仓库中三个长期存在的 GitHub 问题（长达 27 个月），并在真实世界的库（`libpng` 和 `zlib`）中发现了两个以前未知的漏洞。

---

## 📄 论文摘要 (Abstract)

> Static analyzers have been widely adopted for vulnerability detection in C/C++ programs. Query-based static analyzers (e.g., CodeQL) encode vulnerable code patterns in detection queries and match them against source code. However, existing queries still suffer from false positives (FPs, incorrectly flagging benign code as vulnerable) and false negatives (FNs, missing real vulnerabilities). We present ARQ, an agentic framework that automatically refines C/C++ CodeQL queries using execution-grounded evidence from synthesized C/C++ programs. Our key insight is that a synthesized program exposes a query's weakness whenever its execution disagrees with the query's verdict. If the program is genuinely vulnerable but the query stays silent, the query has an FN weakness; if the program is safe but the query fires anyway, it has an FP weakness. ARQ then runs an LLM-based refinement loop that repairs the query using these disagreements as ground truth. Unlike previous query refining methods, ARQ requires no labeled datasets, no commit history, and no vulnerability-specific templates. We demonstrate the effectiveness of ARQ by refining 12 official CodeQL queries using three commercial LLMs (GPT-5.4, Claude-Sonnet-4.6, and Gemini-3.5-flash). We compare both ARQ-refined and original CodeQL queries on the Juliet v1.3 and FormAI v2 datasets and show that ARQ-refined queries detect substantially more true positives, by up to 119.8%, with a Precision of at least 98.0% throughout. ARQ successfully fixed three unresolved GitHub issues raised in the official CodeQL query repository that had remained open for as long as \textit{27 months}. The refined queries also exposed two previously undiscovered bugs in the real-world libraries libpng and zlib.

静态分析器已被广泛用于 C/C++ 程序中的漏洞检测。基于查询的静态分析器（例如 CodeQL）将漏洞代码模式编码到检测查询中，并将其与源代码进行匹配。然而，现有的查询仍然存在误报（FP，将良性代码错误标记为漏洞）和漏报（FN，遗漏真实漏洞）的问题。我们提出了 ARQ，这是一个智能体框架，它利用来自合成 C/C++ 程序的基于执行落地的证据自动优化 C/C++ CodeQL 查询。我们的核心见解是，当合成程序的执行与查询的判定不一致时，该程序就会暴露出查询的弱点。如果程序确实存在漏洞，但查询保持静默，则查询具有漏报弱点；如果程序是安全的，但查询依然触发，则它具有误报弱点。然后，ARQ 运行一个基于 LLM 的优化循环，使用这些不一致性作为真实地面来修复查询。与以往的查询优化方法不同，ARQ 不需要标注数据集、提交历史或特定于漏洞的模板。我们通过使用三个商业 LLM（GPT-5.4、Claude-Sonnet-4.6 和 Gemini-3.5-flash）优化 12 个官方 CodeQL 查询，证明了 ARQ 的有效性。我们在 Juliet v1.3 和 FormAI v2 数据集上比较了经 ARQ 优化的查询和原始 CodeQL 查询，结果表明经 ARQ 优化的查询检测到的真阳性明显更多，提升高达 119.8%，并且在整个过程中精确度保持在至少 98.0%。ARQ 成功修复了官方 CodeQL 查询仓库中提出的三个未解决的 GitHub 问题，这些问题悬而未决的时间长达 \textit{27 个月}。优化后的查询还暴露了真实世界库 libpng 和 zlib 中两个以前未发现的漏洞。

---

## 🔗 全文与资源 (Full-Text & Resources)

* **阅读论文 (Read the Paper):** [查看 PDF (View PDF)](https://arxiv.org/pdf/2608.20637) | [HTML 版本 (HTML Version)](https://arxiv.org/html/2608.20637v1)
* **源代码 (Source Code):** [TeX 源码 (TeX Source)](https://arxiv.org/src/2608.20637)
* **许可证 (License):** [知识共享零标示 1.0 通用协议 (Creative Commons Zero v1.0 Universal)](http://creativecommons.org/publicdomain/zero/1.0/)  
  <img alt="license icon" role="presentation" src="./images/d7507cd66373.png"/>

---

## 📚 外部参考与工具 (External References & Tools)

* **文献计量工具 (Bibliographic Tools):** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.20637) | [谷歌学术 (Google Scholar)](https://scholar.google.com/scholar_lookup?arxiv_id=2608.20637) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.20637)
* **代码与演示 (Code & Demos):** [alphaXiv](https://alphaxiv.org/) | [CatalyzeX](https://www.catalyzex.com) | [Hugging Face](https://huggingface.co/huggingface)