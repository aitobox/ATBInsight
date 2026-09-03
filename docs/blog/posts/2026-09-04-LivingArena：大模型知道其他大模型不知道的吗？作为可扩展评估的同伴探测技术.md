---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-04
hide:
- navigation
tags:
- 大语言模型
- 模型评估
- 自动化红蓝对抗
- 动态基准测试
- 多智能体协同
title: LivingArena：大模型知道其他大模型不知道的吗？作为可扩展评估的同伴探测技术
---
### 文章背景与核心概要
随着大语言模型（LLM）的飞速发展，传统的固定基准测试面临着更新成本高昂、难以适应模型特定弱点等严重局限。为了解决这一痛点，研究人员推出了 **LivingArena**——一个自动化的同伴探测（peer-probing）框架，让大模型轮流相互测试。通过分析交互历史，出题模型能够精准识别对手的弱点，并构建出有针对性且可验证的测试问题。

通过对十个模型进行长达 3,600 轮的竞技测试，研究发现同行探测不仅能有效揭示模型持续存在的、特定于模型自身的漏洞，还能独立评估模型的回答能力与可靠测试构建能力。该研究证明了自动化同伴探测作为一种可持续演进的评估方案，能够为模型开发、红蓝对抗以及具备能力感知的多智能体协同提供强大的“活体”基准支撑。

---

## 执行摘要 (Executive Summary)

大语言模型（LLM）的固定基准测试通常更新成本高昂，且难以适应模型特定的弱点。为了解决这一局限，研究人员引入了 **LivingArena**，这是一个自动化的同伴探测框架，其中 LLM 轮流相互测试。通过分析交互历史，出题者可以识别对手的弱点并构建有针对性的、可验证的测试问题。在十个模型之间进行的 3,600 轮竞技测试表明，同伴探测成功地揭示了持久的、特定于模型的漏洞，同时分别评估了回答能力和可靠的测试构建能力。

> ## Executive Summary
> Fixed benchmarks for Large Language Models (LLMs) are often expensive to update and struggle to adapt to model-specific weaknesses. To address this limitation, researchers introduce **LivingArena**, an automated peer-probing framework where LLMs take turns testing one another. By analyzing interaction history, questioners identify opponent weaknesses and construct targeted, verifiable test questions. A 3,600-round tournament among ten models demonstrated that peer probing successfully uncovers persistent, model-specific vulnerabilities while separately evaluating answering capabilities and reliable test construction.

---

## 论文元数据 (Paper Metadata)

* **arXiv ID:** [arXiv:2607.24780 [cs.AI]](https://arxiv.org/abs/2607.24780)
* **DOI:** [10.48550/arXiv.2607.24780](https://doi.org/10.48550/arXiv.2607.24780)
* **主分类:** 计算机科学 > 人工智能 (`cs.AI`)
* **作者:** Xingyu Chen, Rui Wang, Zhaopeng Tu, Liefeng Bo
* **提交日期:** 2026年6月19日提交；最后修订于2026年9月2日 (v2)
* **开源协议与资源:** 
  * [知识共享署名 4.0 (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
  * [GitHub 仓库 - LivingArena](https://github.com/galaxyChen/LivingArena)

> ---
> 
> ## Paper Metadata
> 
> * **arXiv ID:** [arXiv:2607.24780 [cs.AI]](https://arxiv.org/abs/2607.24780)
> * **DOI:** [10.48550/arXiv.2607.24780](https://doi.org/10.48550/arXiv.2607.24780)
> * **Primary Subject:** Computer Science > Artificial Intelligence (`cs.AI`)
> * **Authors:** Xingyu Chen, Rui Wang, Zhaopeng Tu, Liefeng Bo
> * **Submission Dates:** Submitted on June 19, 2026; Last revised September 2, 2026 (v2)
> * **License & Resources:** 
>   * [Creative Commons Attribution 4.0 (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
>   * [GitHub Repository - LivingArena](https://github.com/galaxyChen/LivingArena)
> 
> ---

---

## 摘要 (Abstract)

固定的基准测试更新成本高昂，且无法根据模型自身的失效情况调整问题。我们不禁要问：LLM 是否可以转而发现彼此的弱点，并将这些观察结果转化为评估过程？为了研究这个问题，我们引入了 **LivingArena**，这是一个自动化的同伴探测框架，模型在其中轮流对彼此进行测试。

利用交互历史，每个出题者都能识别出其对手的潜在弱点，并构建有针对性、可验证的问题来进行探测。对十个模型进行的 3,600 轮竞技测试揭示了一种清晰的角色不对称性：强大的回答者未必是可靠的出题者，因为他们可能会生成内部矛盾的测试，或者无法验证自己的参考答案。在出题者暴露了回答者的失败之后，它更有可能继续攻克同一能力领域，而回答者的弱点会在独立生成的问题（包括由不同模型编写的问题）中再次出现。

这些发现表明，同伴探测可以揭示持续存在的、特定于模型的弱点，同时还能分别评估回答能力和可靠的测试构建能力。通过自动化这一过程，并使测试难度随着模型能力不断演进，LivingArena 为模型开发、红蓝对抗以及具备能力感知的多智能体协同提供了一个“活体（living）”基准。

> ## Abstract
> 
> Fixed benchmarks are costly to renew and cannot adapt their questions to model-specific failures. We ask whether LLMs can instead discover one another's weaknesses and turn those observations into an evaluation process. To study this question, we introduce **LivingArena**, an automated peer-probing framework in which models take turns testing one another. 
> 
> Using the interaction history, each questioner identifies potential weaknesses of its opponent and constructs targeted, verifiable questions to probe them. A 3,600-round tournament of ten models reveals a clear role asymmetry: strong answerers are not always reliable questioners, because they may generate internally inconsistent tests or fail to verify their own reference answers. After a questioner exposes an answerer's failure, it is more likely to pursue the same capability domain, while the answerer's weakness recurs on independently generated questions, including questions written by different models. 
> 
> These findings show that peer probing can reveal persistent model-specific weaknesses while separately evaluating answering and reliable test construction. By automating this process and allowing test difficulty to evolve with model capabilities, LivingArena provides a "living" benchmark for model development, red-teaming, and capability-aware multi-agent coordination.

---

## 核心要点与发现 (Key Takeaways & Findings)

1. **角色不对称：** 强大的回答性能并不自动等同于可靠的测试构建能力。先进模型仍然可能产生内部矛盾的问题，或者无法验证其自身的参考答案。
2. **持续存在的弱点：** 当出题者暴露出回答者的某个特定失效点时，它往往会在该能力领域继续深入挖掘（加码）。此外，当由其他独立生成的模型进行测试时，这些相同的弱点会一致地再次出现。
3. **可扩展且不断演进的评估：** 通过自动化测试生成并让测试难度随着模型能力动态扩展，LivingArena 为模型开发和红蓝对抗提供了一个可持续的静态基准替代方案。

> ## Key Takeaways & Findings
> 
> 1. **Role Asymmetry:** Strong answering performance does not automatically equate to reliable test construction. Advanced models can still produce internally inconsistent questions or fail to verify their own reference answers.
> 2. **Persistent Weaknesses:** When a questioner exposes a specific failure in an answerer, it tends to double down on that capability domain. Furthermore, those same weaknesses recur consistently when tested by other, independently generated models.
> 3. **Scalable & Evolving Evaluation:** By automating test generation and letting difficulty scale dynamically with model capabilities, LivingArena serves as a sustainable alternative to static benchmarks for model development and red-teaming.