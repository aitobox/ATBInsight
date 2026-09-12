---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-13
hide:
  - navigation
tags:
  - IMO 竞赛
  - Nemotron
  - 数学推理
  - 测试时计算
  - 强化学习
title: "斩获 IMO 金牌的开源秘籍：面向奥林匹克数学的 Nemotron 训练实践"
---

# 斩获 IMO 金牌的开源秘籍：面向奥林匹克数学的 Nemotron 训练实践

> # An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics

> **arXiv ID:** [2609.10712](https://arxiv.org/abs/2609.10712)  
> **Subjects:** Artificial Intelligence (`cs.AI`)  
> **Submitted:** September 9, 2026  
> **Authors:** Ivan Moshkov, Stephen Ge, George Armstrong, Wei Du, Sadegh Mahdavi, Igor Gitman  
> **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)  
> *[View PDF](https://arxiv.org/pdf/2609.10712) | [TeX Source](https://arxiv.org/src/2609.10712)*  

### 文章背景与核心概要

国际数学奥林匹克竞赛 (IMO) 一直被视为检验人工智能最高阶复杂逻辑推理能力的试金石，而以往取得顶尖成绩的方案往往依赖闭源专有模型或形式化定理证明器。本文探索了如何通过模型后训练 (Post-Training) 与测试时计算 (Test-Time Compute) 设计，仅凭自然语言生成严密的奥数证明。以 **Nemotron 3 Ultra** 为基座，研究团队通过监督微调 (Supervised Fine-Tuning, SFT) 与强化学习 (Reinforcement Learning, RL) 训练了两个专家模型，并构建出一套无需任何形式化证明器、外部代码工具或互联网连接的全开源推理流水线。该系统在 **IMO 2026 中斩获 30 分（满分 42 分），成功达到金牌门槛**。为了推动开源社区发展，团队完整开源了两个专家权重、全部训练与推理代码、解题答卷以及包含 200 道原创奥数题的全新评测基准 Nemotron-IMO-Bench。

---

## 核心概要

> ## Summary

本文深入探讨了模型后训练 (Post-Training) 与测试时推理架构设计如何显著增强复杂奥林匹克数学竞赛中的自然语言证明生成能力。研究人员以 **Nemotron 3 Ultra** 为起点，利用监督微调 (Supervised Fine-Tuning, SFT) 和强化学习 (Reinforcement Learning, RL) 训练了两个专家模型检查点。

> This paper investigates how model post-training and test-time inference design enhance natural-language proof generation for complex Olympiad-level mathematics. Starting with **Nemotron 3 Ultra**, the researchers trained two specialist checkpoints utilizing supervised fine-tuning and reinforcement learning. 

他们提出了一套完全基于开源模型的测试时计算流水线，该流程全程以自然语言运作，完全无需形式化证明器、外部代码工具或互联网访问。利用三个 Nemotron 3 Ultra 检查点（通用模型与两个后训练专家模型），该系统通过迭代搜索来生成、验证并提炼候选证明，随后进入独立的高算力筛选阶段敲定最终解答。

> They present a fully open-model test-time-compute pipeline operating entirely in natural language—requiring no formal provers, external tools, or internet access. Using three Nemotron 3 Ultra checkpoints (the general model and two post-trained specialists), the system executes an iterative search to generate, verify, and refine candidate proofs, followed by a separate high-compute selection stage. 

**核心里程碑：** 该系统在 **IMO 2026 中斩获 42 分中的 30 分**，成功突破了**金牌分数线**。

> **Key Achievement:** The system achieved a score of **30 out of 42 points at IMO 2026**, successfully hitting the **gold-medal threshold**. 

作者团队已将以下成果全部公开发布：
* 两个后训练专家检查点权重
* 训练数据集与训练代码
* 推理部署代码
* 参赛提交的完整解题答案
* **Nemotron-IMO-Bench**，一个包含 200 道全新奥数级题目的评测基准

> The authors have publicly released:
> * The two post-trained checkpoints
> * Training data and code
> * Inference code
> * Submitted solutions
> * **Nemotron-IMO-Bench**, a novel benchmark consisting of 200 olympiad-level problems.

---

## 论文摘要

> ## Abstract

> 💬 [原文引用 / Original Quote]:
> We study how model post-training and test-time inference design affect natural-language proof generation for hard olympiad mathematics. Starting from Nemotron 3 Ultra, we train two specialist checkpoints using supervised fine-tuning and reinforcement learning, and evaluate checkpoint choice, verification, and refinement. Based on these findings, we present an open-model test-time-compute pipeline. The system operates entirely in natural language, with no formal prover, external tools, or internet access. Three Nemotron 3 Ultra checkpoints - the general-availability model and two post-trained specialists - power an iterative search that generates, verifies, and refines candidate proofs; a separate high-compute stage then selects each final submission. The system scored 30 out of 42 points at IMO 2026, reaching the gold-medal threshold. We release the two post-trained checkpoints as well as the training data, the training and inference code, the submitted solutions, and Nemotron-IMO-Bench, a new benchmark of 200 novel olympiad-level problems.

我们研究了模型后训练与测试时推理设计如何影响高难度奥林匹克数学中的自然语言证明生成。从 Nemotron 3 Ultra 出发，我们利用监督微调和强化学习训练了两个专用检查点，并系统评估了模型检查点选取、核验机制以及逐步提炼策略。基于这些发现，我们提出了一套开源模型的测试时计算流水线。该系统完全在自然语言环境中运作，既不需要形式化定理证明器，也不需要外部工具或互联网访问。三个 Nemotron 3 Ultra 检查点——通用公开模型与两个后训练专家模型——共同驱动迭代搜索，负责生成、核查并完善候选证明；随后通过独立的高算力评估阶段选定最终提交的解答。该系统在 IMO 2026 中获得 30 分（满分 42 分），成功跻身金牌门槛。我们公开发布了这两个后训练检查点权重，以及训练数据、训练与推理代码、提交的官方解答，并发布了包含 200 道原创奥数题目的全新基准测试 Nemotron-IMO-Bench。

---

## 相关资源与导航

> ## Associated Resources & Navigation

* **代码、数据与媒体资源：** 可通过 Hugging Face、DagsHub 以及 GitHub 集成平台获取。
* **文献与引用工具：** 可通过 NASA ADS、Google 学术、Semantic Scholar 和 BibTeX 访问。

> * **Code, Data & Media:** Available via Hugging Face, DagsHub, and GitHub integrations.
> * **Bibliographic Tools:** Accessible via NASA ADS, Google Scholar, Semantic Scholar, and BibTeX.

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="display:none;" />
