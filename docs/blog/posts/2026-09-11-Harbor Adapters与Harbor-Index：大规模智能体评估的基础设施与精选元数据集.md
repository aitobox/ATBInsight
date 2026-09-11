---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-11
hide:
- navigation
tags:
- 智能体评估
- 大语言模型
- 基准测试
- Harbor-Index
- 基础设施
title: Harbor Adapters与Harbor-Index：大规模智能体评估的基础设施与精选元数据集
---
### 文章背景与核心概要
在大语言模型（LLM）智能体生态系统快速扩张的背景下，跨日益增多的基准测试对智能体进行评估变得异常困难，这主要是由于复杂的运行环境和零散的智能体集成方式所导致的。本文推出了 **Harbor Adapters**（Harbor 适配器），这是一种统一的评估基础设施，成功将 80 多个基准测试移植以支持任意智能体。基于该基础设施，作者对 54 个基准测试中的 8 个模型进行了大规模评估。

在此基础上，本文提出了 **Harbor-Index**，这是一个高质量、经过精心筛选的元数据集，包含跨越 29 个基准测试的 82 个具有挑战性的任务。Harbor-Index 旨在保持极高的严谨性和难度（即使是最强大的评估模型与框架组合——搭载 Codex 的 GPT-5.5，其通过率也仅为 28.0%），同时为大规模智能体评估提供了一个经济高效的框架。

---

## 📌 执行摘要 (Executive Summary)

> Evaluating large language model (LLM) agents across a rapidly expanding ecosystem of benchmarks is exceptionally difficult due to complex environments and fragmented agent integrations. This paper introduces **Harbor Adapters**, a unified evaluation infrastructure that successfully ports over 80 benchmarks to support arbitrary agents. Using this infrastructure, the authors perform a massive evaluation of 8 models across 54 benchmarks. 
> 
> Building upon these findings, the paper presents **Harbor-Index**, a high-quality, curated meta-dataset of 82 challenging tasks spanning 29 benchmarks. Harbor-Index is specifically designed to remain rigorous and difficult—even the strongest evaluated model-harness configuration (GPT-5.5 with Codex) tops out at a 28.0% pass rate—while offering an affordable framework for large-scale agentic evaluation.

在快速扩展的基准测试生态系统中评估大语言模型（LLM）智能体异常困难，因为这通常需要复杂的环境和零散的智能体集成。本文推出了 **Harbor Adapters**，这是一个用于智能体基准测试的统一评估基础设施。我们的工作做出了三项贡献。首先，我们开发了基准适配器，将 80 多个基准移植以评估任意智能体，并通过严格的代码审查和对等实验对其进行了验证。其次，我们对 54 个基准测试中的 8 个不同能力层级的模型进行了大规模评估；每个模型都通过 Terminus-2 以及 3 个原生框架之一运行。这使得对智能体能力和失败模式的分析比以往任何时候都更加深入。第三，我们推出了 **Harbor-Index**，这是一个精选的包含 82 个困难、多样且高质量任务的集合，横跨 29 个基准测试，这些任务是从适配后的测试集中经过难度过滤、AI与人工审计以及审计-修复循环精炼而成的。Harbor-Index 保留了大尺度智能体评估的挑战性和广度，同时运行成本经济实惠；没有任何评估的模型-框架配置超过 30% 的通过率，最强者（搭载 Codex 的 GPT-5.5）达到了 28.0%。我们将适配器、评估结果、深入分析和 Harbor-Index 作为开源成果发布，以支持对语言模型智能体进行更可靠、更全面的评估。

---

## 👥 作者 (Authors)

> **Lead Authors:** Lin Shi, Haowei Lin, Zixuan Zhu, Xiaoyue Zhou, Xiang Li, Xiangning Lin, Yaxuan Deng, Han Xu, Yuangang Li, Shanda Li, Zizhao Chen, Hanwen Xing, Harsh Raj, Bo Chen, Quan Shi, Steven Dillmann, Yipeng Gao, Puneesh Khanna, Ruofan Lu, Chao Beyond Zhou, Michael Yang, Robert Zhang, Siyuan Chai, Jiayu Chang, Yizhao Chen, Xiaokun Chen, Yiwei Dai, Wenting Yang, Hange Liu, Minghao Liu, Zihan Wang, Adnan El Assadi, Benedikt Stroebl, E. Kelly Buchanan, Han Meng, Junwei He, Longxuan Yu, Radin Shayanfar, Yukyung Lee, Zhikang Dong, Allen G Hart, Anjiang Wei, Anurag Kashyap, Arpandeep Khatua, Audrey Jixin Zheng, Chengrui Ma, David Heineman, Dubing Chen, Hai-Anh Trinh, Haishuo Fang, Hefan Zhang, Hui Shen, Issa Sugiura, Jiankai Sun, Jiechao Gao, Junhong Lin, Junnan Li, Kai Yang, Lei Hsiung, Maoyu Wang, Mengze Tang, Nabil Omi, Negin Raoof, Nicholas Edwards, Octavia Guo, Orfeas Menis Mastromichalakis, Pengliang Ji, Przemysław Hejman, Qi Qi, Qunshu Lin, Richard Zhuang, Rui Yang, Ruichen Zheng, Ryan Marten, Shaghayegh Fazliani, Shizheng Hou, Sicong Jiang, Sijie Li, Boqin Yuan, Michael Glass, Song Bian, Terry Yue Zhuo, Tianqing Wu, Tom Tang, Wanjia Zhao, Weihao Xuan, Wenhua Liang, Xian Liu, Xin Lan, Xuan Zhang, Xuandong Zhao, Yanchuan Tang, Yifan Jiang, Yijiang Li, Yitong Guan, Yizhi Li, Yonghui Liu, Yuheng Tang, Yujun (Audrey) Mao, and Yunfei Zhao *(along with 25 additional co-authors, including Andy Konwinski, Alex Dimakis, Nicholas Carlini, Ludwig Schmidt, and others)*.

**主要作者：** Lin Shi, Haowei Lin, Zixuan Zhu 等（共计百余位作者，包含 Andy Konwinski、Alex Dimakis、Nicholas Carlini、Ludwig Schmidt 等 25 位联合作者）。

---

## 🔍 核心贡献 (Key Contributions)

> 1. **Harbor Adapters Infrastructure:** Development of unified benchmark adapters capable of porting more than 80 distinct benchmarks to evaluate arbitrary agents. These adapters are validated via rigorous code review and parity experiments.
> 2. **Large-Scale Multi-Model Evaluation:** Comprehensive evaluation of 8 models spanning multiple capability tiers across 54 benchmarks. Each model was executed using Terminus-2 alongside one of 3 native harnesses, enabling deep insight into agent capabilities and failure modes.
> 3. **Harbor-Index Meta-Dataset:** Introduction of a curated suite of 82 difficult, diverse, and high-quality tasks across 29 benchmarks. Filtered through rigorous difficulty criteria, AI/human audits, and an iterative audit-and-fix loop, Harbor-Index preserves evaluation rigor while maintaining practical cost-efficiency.

1. **Harbor Adapters 基础设施：** 开发了统一的基准适配器，能够移植 80 多个不同的基准来评估任意智能体。这些适配器通过严格的代码审查和对等实验得到了验证。
2. **大规模多模型评估：** 对跨多个能力层级的 8 个模型在 54 个基准测试中进行了全面评估。每个模型都使用 Terminus-2 结合 3 个原生框架之一运行，从而对智能体能力和失败模式提供了深入的见解。
3. **Harbor-Index 元数据集：** 推出了精选的 82 个困难、多样且高质量的任务套件，横跨 29 个基准。通过严格的难度标准、AI/人工审计以及迭代的审计-修复循环进行过滤，Harbor-Index 在保持评估严谨性的同时，兼具了实用的成本效益。

---

## 📊 摘要 (Abstract)

> Evaluating agents on the growing number of agentic benchmarks is challenging because they often require complex environments and agent integrations. We introduce Harbor Adapters, a unified evaluation infrastructure for agentic benchmarks. Our work makes three contributions. First, we develop benchmark adapters that port more than 80 benchmarks to evaluate arbitrary agents, and validate them through rigorous code review and parity experiments. Second, we conduct a large-scale evaluation of 8 models spanning capability tiers across 54 benchmarks; every model is run with Terminus-2 and with one of 3 native harnesses. This enables a broader analysis of agent capabilities and failure modes than was previously possible. Third, we introduce Harbor-Index, a curated set of 82 difficult, diverse, and high-quality tasks spanning 29 benchmarks, refined from the adapted suite through difficulty filtering, AI and human audit, and an audit-and-fix loop. Harbor-Index preserves the challenge and breadth of large-scale agentic evaluations while being affordable to run; no evaluated model-harness configuration exceeds 30% pass rate, and the strongest (GPT-5.5 with Codex) reaches 28.0%. We release the adapters, evaluation results, in-depth analysis, and Harbor-Index as open-source artifacts to support more reliable and comprehensive evaluation of language-model agents.

（详见上文“执行摘要”段落）

---

## 🔗 链接与资源 (Links & Resources)

* [在 arXiv 上查看 PDF](https://arxiv.org/pdf/2609.04298)
* [实验性 HTML 版本](https://arxiv.org/html/2609.04298v3)
* [TeX 源代码](https://arxiv.org/src/2609.04298)
* [DOI 引用](https://doi.org/10.48550/arXiv.2609.04298)