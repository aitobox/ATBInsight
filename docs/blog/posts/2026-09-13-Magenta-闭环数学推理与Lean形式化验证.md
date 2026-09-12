---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-13
hide:
  - navigation
tags:
  - 数学推理
  - 形式化验证
  - Lean 4
  - AI 智能体
  - 自动定理证明
title: "Magenta：闭环数学推理与 Lean 形式化验证"
---

# Magenta：闭环数学推理与 Lean 形式化验证

> # Magenta: Closing the Loop Between Mathematical Reasoning and Lean Verification

> **arXiv:** [2609.11319](https://arxiv.org/abs/2609.11319) [cs.AI]  
> **Submitted:** 10 September 2026  
> **Authors:** Joshua Ong Jun Leang, Haonan Li, Zheng Zhao, Xinyi Shang, Wenda Li, Zhengzhong Liu, Erix Xing, Shay Cohen, Eleonora Giunchiglia  

### 文章背景与核心概要

人类数学交流大多依赖自然语言，大语言模型 (Large Language Model, LLM) 虽擅长自然语言推理，但容易在推导细节中产生细微错误，无法提供像交互式定理证明助手那样百分之百可验证的严格保证。为了解决这一痛点，本文提出了 **Magenta**——一个无需额外训练的智能体流水线 (Agentic Pipeline)，它将大语言模型的自然语言非形式化推理与 Lean 4 形式化验证环境无缝打通。Magenta 仅需自然语言题目，便能自动生成解答、将其转化为 Lean 4 命题并构建经由机器检验的形式化证明，同时通过命题裁判防范虚假命题，并通过错误归因裁判引导精准修正。该方法在 AIME 2025、AIME 2026 及 HMMT 2026 等奥数基准上均取得 100% 的满分成绩，并与开源模型 K2-Horizon-7B 配合攻克了 IMO 2026 全部题目，展现了机器严密验证与大模型推理结合的巨大潜力。

---

## 📌 核心摘要

> ## 📌 Summary

尽管大语言模型 (LLM) 在借助自然语言进行非形式化数学推理方面表现优异，但它们往往缺乏机器可检验证明助手所具备的严格性与离散验证能力。

> While large language models (LLMs) perform well in informal mathematical reasoning using natural language, they often miss out on the rigor and discrete verification capabilities offered by machine-checkable proof assistants.

本文介绍了 **Magenta**，这是一种用于连接非形式化推理与形式化推理的免训练智能体流水线 (Agentic Pipeline)。在仅给定自然语言数学问题的前提下，Magenta 能够：
1. 生成解答。
2. 将问题和解答形式化表达为一个 **Lean 4 命题**。
3. 构建一段**经由机器检验的形式化证明**。

> This paper introduces **Magenta**, a training-free agentic pipeline that bridges informal and formal reasoning. Given a natural-language mathematical problem, Magenta:
> 1. Generates an answer.
> 2. Expresses the problem and answer as a **Lean 4 statement**.
> 3. Constructs a **machine-checked proof**.

Magenta 采用了专门设计的裁判机制：其中**命题裁判 (Statement Judge)** 用于确保形式化后的陈述完整保留原始题意（防止产生虚假证明证书），而**错误归因裁判 (Error-Attribution Judge)** 则负责将证明失败的尝试精准路由至数学重新推导或本地 Lean 代码修复。

> Magenta utilizes specialized judges: a **statement judge** to ensure formalizations preserve the original problem (preventing false certificates), and an **error-attribution judge** to route failures either to mathematical re-derivation or local Lean repair.

### 核心成果

> ### Key Results

* 在评估的所有奥林匹克数学基准测试中均斩获 **100% 的准确率**，包括 **AIME 2025、AIME 2026 和 HMMT 2026 年 2 月赛题**。
* 当与开源权重推理模型 K2-Horizon-7B 搭配使用时，成功解答了 **IMO 2026 全部六道竞赛题**。
* 实验表明，在面对高难度难题时，基于反馈引导的自我修正策略显著优于独立的重采样基线。

> * Achieves **100% accuracy** across evaluated olympiad benchmarks, including **AIME 2025, AIME 2026, and HMMT February 2026**.
> * Successfully solves all six **IMO 2026 problems** when paired with the open-weight K2-Horizon-7B reasoner.
> * Demonstrates that feedback-guided correction significantly outperforms independent resampling on difficult problems.

---

## 作者与隶属机构

> ## Authors & Affiliations

* **Joshua Ong Jun Leang**
* **Haonan Li**
* **Zheng Zhao**
* **Xinyi Shang**
* **Wenda Li**
* **Zhengzhong Liu**
* **Erix Xing**
* **Shay Cohen**
* **Eleonora Giunchiglia**

> * **Joshua Ong Jun Leang**
> * **Haonan Li**
> * **Zheng Zhao**
> * **Xinyi Shang**
> * **Wenda Li**
> * **Zhengzhong Liu**
> * **Erix Xing**
> * **Shay Cohen**
> * **Eleonora Giunchiglia**

---

## 论文摘要

> ## Abstract

> 💬 [原文引用 / Original Quote]:
> Most of mathematical knowledge has been communicated through so-called informal use of mathematics and natural language. With large language models (LLMs) being highly adept in using natural language, they achieve strong performance, yet not perfect, in informal mathematical reasoning. Restraining LLMs to informal reasoning misses out on the opportunity to use the discrete verification abilities that machines offer through machine-checkable proofs. In this paper, we bridge the gap between informal and formal reasoning by integrating Lean signals into the informal reasoning process. We introduce Magenta, a training-free agentic pipeline that, given only a natural-language problem, produces an answer, expresses it as a Lean 4 statement, and constructs a machine-checked proof. A statement judge verifies whether the formalisation preserves the original problem, while an error-attribution judge routes failed attempts either to mathematical re-derivation or local Lean repair. Magenta achieves 100% accuracy across all evaluated olympiad benchmarks, including AIME 2025, AIME 2026, and HMMT February 2026. When paired with the open-weight K2-Horizon-7B reasoner, it solves all six IMO 2026 problems. Our analysis shows that statement adjudication is essential for preventing false certificates and that feedback-guided correction outperforms independent resampling on difficult problems.

人类的绝大多数数学知识历来都是通过所谓的非形式化数学和自然语言进行交流传播的。由于大语言模型 (LLM) 高度擅长自然语言处理，它们在非形式化数学推理中展现出强劲的表现，但依然未能做到尽善尽美。如果仅将大语言模型局限于非形式化推理，就会错失借助机器可检验证明所提供的离散验证能力的良机。在本文中，我们通过将 Lean 的形式化反馈信号融入非形式化推理过程，弥合了非形式化推理与形式化推理之间的鸿沟。我们推出了 Magenta，这是一种免训练的智能体流水线：在仅输入自然语言题目的前提下，它能够推导出答案、将其表达为 Lean 4 命题，并构建出经由机器严格检验的形式化证明。其中，命题裁判用于核验形式化表述是否完整保留了原问题意图，而错误归因裁判则能将失败的尝试精准路由至数学推导重写或本地 Lean 修复。Magenta 在所评估的所有奥林匹克数学基准测试中均取得了 100% 的准确率，涵盖 AIME 2025、AIME 2026 和 HMMT 2026 年 2 月赛题。当与开源权重推理模型 K2-Horizon-7B 协同工作时，它完整攻克了 IMO 2026 的全部六道试题。我们的分析表明，命题裁决机制对于防范虚假证明证书至关重要，并且在攻克高难度难题时，由反馈驱动的定向修正表现显著优于独立的重新采样。

---

## 补充信息

> ## Additional Information

* **主要学科领域：** 人工智能 (`cs.AI`)
* **引用方式：** [arXiv:2609.11319](https://doi.org/10.48550/arXiv.2609.11319) [cs.AI]
* **授权协议：** [知识共享署名 4.0 国际许可协议 (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Cite as:** [arXiv:2609.11319](https://doi.org/10.48550/arXiv.2609.11319) [cs.AI]
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

---

## 全文与相关资源

> ## Full-Text & Resources

* [查看 PDF](https://arxiv.org/pdf/2609.11319)
* [网页版 (实验性)](https://arxiv.org/html/2609.11319v1)
* [TeX 源码](https://arxiv.org/src/2609.11319)
* [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.11319)
* [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2609.11319)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.11319)

> * [View PDF](https://arxiv.org/pdf/2609.11319)
> * [HTML Version (Experimental)](https://arxiv.org/html/2609.11319v1)
> * [TeX Source](https://arxiv.org/src/2609.11319)
> * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.11319)
> * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.11319)
> * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.11319)
