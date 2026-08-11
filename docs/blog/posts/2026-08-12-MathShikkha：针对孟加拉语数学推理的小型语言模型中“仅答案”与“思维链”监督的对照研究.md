---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-12
hide:
- navigation
tags:
- 大语言模型
- 数学推理
- 孟加拉语
- 思维链
- 模型微调
title: MathShikkha：针对孟加拉语数学推理的小型语言模型中“仅答案”与“思维链”监督的对照研究
---
### 文章背景与核心概要

本研究探讨了在针对孟加拉语等低资源语言进行小型语言模型（SLM）数学推理训练时，由教师生成的“思维链”（Chain-of-Thought, CoT）监督是否比普通的“仅答案”（Answer-only）监督微调具有性能优势。

为了进行深入分析，作者推出了 **MathShikkha** 数据集，这是一个包含由 GPT-5.4 生成的推理过程的孟加拉语数学推理数据集。研究人员在严格匹配的协议下，对四个参数规模在 4B 到 7B 之间的学生模型进行了微调。

研究发现，CoT 监督在领域内任务中对较强模型提升有限，但在领域外任务中表现出显著优势，且在增强模型对孟加拉语的遵循能力及推理过程的可解释性方面具有重要价值。

---

## 📌 摘要

本研究探讨了在针对孟加拉语等低资源语言进行小型语言模型（SLM）数学推理训练时，由教师生成的“思维链”（Chain-of-Thought, CoT）监督是否比普通的“仅答案”监督微调具有性能优势。

> This study investigates whether teacher-generated **Chain-of-Thought (CoT)** supervision provides performance benefits over ordinary answer-only supervised fine-tuning when training Small Language Models (SLMs) for mathematical reasoning in low-resource languages like Bangla.

为了进行此项分析，作者引入了 **MathShikkha**，这是一个全新的孟加拉语数学推理数据集，其中包含了由 GPT-5.4 生成的推理过程。研究人员在严格匹配的协议下，对四个参数规模在 4B 到 7B 之间的学生模型进行了微调。

> To conduct this analysis, the authors introduced **MathShikkha**, a new Bangla mathematical reasoning dataset featuring GPT-5.4-generated rationales. Four student models (4B–7B parameters) were fine-tuned under a rigorously matched protocol.

### 关键发现：
### Key Findings:

* **领域内性能：** 对于较强的基座模型，CoT 监督相比“仅答案”微调并未提供统计学意义上的显著提升（尽管其生成的 Token 数量增加了 15–52 倍）。然而，对于较弱的 4B 模型，CoT 确实带来了显著的性能提升（提高了 18.56 个百分点，$p < 0.0001$）。
> * **In-Domain Performance:** For stronger backbones, CoT supervision offered no statistically significant improvement over answer-only fine-tuning (despite generating 15–52× more tokens). However, it did provide a significant boost (18.56 points, $p < 0.0001$) for the weaker 4B model.

* **领域外性能：** 在经过污染审计的更大规模 *BanglaMATH* 基准测试中，CoT 在所有四个模型上均显著优于“仅答案”监督，提升幅度达 20.1–28.1 个百分点。“仅答案”微调经常导致领域外准确率下降至基线水平以下，而 CoT 则保持或增强了该性能。
> * **Out-of-Domain Performance:** On the larger, contamination-audited *BanglaMATH* benchmark, CoT significantly outperformed answer-only supervision across all four models by 20.1–28.1 points. Answer-only fine-tuning frequently degraded out-of-domain accuracy below baseline levels, whereas CoT preserved or enhanced it.

* **定性人工评估：** 人工及专家评估（$\kappa = 0.76\text{--}1.00$）显示，CoT 的主要价值不在于提高基础推理的有效性，而在于强制执行目标语言（孟加拉语）的规范性，并生成透明、可检查的推理步骤。
> * **Qualitative Human Evaluation:** Human and expert evaluations ($\kappa = 0.76\text{--}1.00$) revealed that CoT’s primary value lies not in improving underlying reasoning validity, but rather in enforcing target-language adherence (Bangla) and producing transparent, inspectable reasoning steps.