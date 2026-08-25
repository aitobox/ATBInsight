---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 大模型安全
- 红蓝对抗
- 心理学说服
- 多轮攻击
- 提示词越狱
title: PsychJail：通过大模型策略的多轮说服探索心理学越狱
---
### 文章背景与核心概要
随着大语言模型（LLM）越来越多地在教育、医疗和政策咨询等互动场景中担任持续的社会对话者，传统的单轮提示词优化已难以应对新兴的安全风险。

本文引入了 **PsychJail**，这是一个新型红蓝对抗框架，它利用基于心理学的多轮说服技术来攻击已对齐的 LLM。通过将*说服知识模型（PKM）*付诸实践，PsychJail 将每次攻击交互结构化为：1. **意义转变分析**；2. **策略选择**；3. **受害者可见消息**。

利用受 PKM 门控的轨迹级强化学习，PsychJail 在四个已对齐的受害者模型上取得了令人瞩目的 **87.3% 平均攻击成功率**，超越了标准的单轮和多轮基线。此外，作者分析了受害者模型独特的行为“指纹”，将其分类为候选心理画像：*理性主义者*、*信誉驱动型*、*单一叙事型*和*广泛易说服型*。

---

* **arXiv ID:** [arXiv:2608.23028](https://arxiv.org/abs/2608.23028) [cs.AI]
* **Authors:** Zeyu Feng, Qingyu Wu, Yuzhe Luo, Hua Cheng
* **Submitted:** August 24, 2026
* **Links:** [View PDF](https://arxiv.org/pdf/2608.23028) | [HTML Version](https://arxiv.org/html/2608.23028v1) | [DOI](https://doi.org/10.48550/arXiv.2608.23028)

---

## 摘要 (Summary)

随着大语言模型（LLM）越来越多地部署在教育、医疗、政策咨询和其他互动环境中（在此类环境中，用户将其作为持续的社会对话者而非单次查询引擎），越狱行为正成为日益严重的安全性威胁。然而，大多数研究仍侧重于单轮提示词优化或迭代攻击精炼，从而导致对基于心理学的多轮漏洞探索不足。

> As large language models (LLMs) increasingly act as sustained social interlocutors in interactive domains (such as education, healthcare, and policy advising), traditional single-turn prompt optimization falls short of capturing emerging security risks. 

我们提出了 PsychJail，这是一个由心理学引导的框架，旨在通过理论基础的多轮说服来对已对齐的 LLM 进行红蓝对抗。PsychJail 将既定的社会心理学说服技术映射到受策略条件约束的攻击策略中。它将攻击者的每一个行动分解为意义转变分析、策略选择和受害者可见消息，从而付诸实践了说服知识模型（PKM）。该策略通过使用 PKM 门控奖励的轨迹级强化学习进行精炼，该奖励仅在每一轮都包含结构良好的意义转变分析时，才对早期的越狱成功给予奖励。

> This paper introduces **PsychJail**, a novel red-teaming framework that exploits psychologically grounded, multi-turn persuasion techniques against aligned LLMs. By operationalizing the *Persuasion Knowledge Model (PKM)*, PsychJail structures each attack interaction into:
> 1. A **Change-of-Meaning analysis**
> 2. **Tactic selection**
> 3. A **victim-visible message**

在四个已对齐的受害者模型中，PsychJail 实现了最高的平均攻击成功率（87.3%），并在每个模型上都表现得优于强单轮和多轮基线。我们还通过打破每个受害者防御的行动来衡量其易感性，揭示了四个不同的模型级指纹，这些指纹确定了哪些说服杠杆会影响每个模型及其影响的广泛程度。这些指纹有助于解释跨模型迁移的不对称性。我们将它们解释为四种候选心理画像——理性主义者、信誉驱动型、单一叙事型和广泛易说服型——同时将这种解释视作需要未来验证的猜想。我们的研究结果确立了心理学越狱作为日益互动的 LLM 的一个独特的红蓝对抗前沿领域。

> Using trajectory-level reinforcement learning gated by PKM, PsychJail achieves an impressive **87.3% average attack success rate** across four aligned victim models, outperforming standard single-turn and multi-turn baselines. Furthermore, the authors analyze the distinct behavioral "fingerprints" of victim models, categorizing them into candidate psychological profiles: *rationalist*, *credibility-driven*, *narrative-monoculture*, and *broadly persuadable*.

---

## 文档元数据 (Document Metadata)

| 字段 (Field) | 详情 (Details) |
| :--- | :--- |
| **主要学科 (Primary Subject)** | 人工智能 (`cs.AI`) |
| **提交历史 (Submission History)** | [v1] 2026年8月24日 周一 09:33:26 UTC (481 KB) |
| **许可证 (License)** | [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) |

---

## 摘要原文 (Abstract)

> Large language models (LLMs) are increasingly deployed in education, healthcare, policy advising, and other interactive settings, where users engage them as sustained social interlocutors rather than one-shot query engines. This shift makes jailbreaks a growing safety threat, yet most research emphasizes single-turn prompt optimization or iterative attack refinement, leaving psychologically grounded multi-turn vulnerabilities underexplored. 
>
> We present PsychJail, a psychology-guided framework for red teaming aligned LLMs through theory-grounded, multi-turn persuasion. PsychJail maps established social-psychological persuasion techniques into a tactic-conditioned attack policy. It factorizes each attacker action into a Change-of-Meaning analysis, tactic selection, and victim-visible message, operationalizing the Persuasion Knowledge Model (PKM). The policy is refined with trajectory-level reinforcement learning using a PKM-gated reward that credits early jailbreak success only when every turn contains a well-formed Change-of-Meaning analysis. 
>
> Across four aligned victim models, PsychJail achieves the highest average attack success rate (87.3%) and outperforms strong single-turn and multi-turn baselines on every model. We also measure susceptibility at the action that breaks each victim, revealing four distinct model-level fingerprints that identify which persuasion levers affect each model and how broadly. These fingerprints help explain cross-model transfer asymmetry. We interpret them as four candidate psychological profiles—rationalist, credibility-driven, narrative-monoculture, and broadly persuadable—while treating this interpretation as a conjecture requiring future validation. Our findings establish psychological jailbreaks as a distinct red-teaming frontier for increasingly interactive LLMs.

---

## 附加资源与工具 (Additional Resources & Tools)

* **代码、数据与媒体 (Code, Data & Media):** [Hugging Face](https://huggingface.co/huggingface), [CatalyzeX](https://www.catalyzex.com), [DagsHub](https://dagshub.com/)
* **文献检索工具 (Bibliographic Tools):** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23028), [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23028), [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23028)
* **交互式演示 (Interactive Demos):** [Replicate](https://replicate.com/docs/arxiv/about), [Hugging Face Spaces](https://huggingface.co/docs/hub/spaces), [TXYZ.AI](https://txyz.ai)

---

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" />