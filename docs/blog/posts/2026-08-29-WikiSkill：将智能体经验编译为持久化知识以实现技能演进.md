---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- AI Agent
- 技能演进
- 知识库
- 模型扩展
- 跨模型迁移
title: WikiSkill：将智能体经验编译为持久化知识以实现技能演进
---
### 文章背景与核心概要
本文介绍了 **WikiSkill** 这一创新框架，旨在通过将可执行的智能体技能与持久化的知识库（wiki）进行协同演进，来全面提升AI智能体的能力。传统的技能演进方法通常将优化见解散落于原始执行历史中，难以实现系统性的复用。而 WikiSkill 通过清晰分离原始执行经验、累积知识和可执行技能，有效解决了这一痛点。

研究表明，WikiSkill 在各项基准测试和不同模型中均持续超越当前最先进的技能演进基线。此外，技能演进与模型规模扩展呈现出良好的协同效应：更大规模的模型能够更有效地利用演进后的技能，而配备了 WikiSkill 的较小模型甚至可以超越缺乏技能的、体量大得多的模型。消融实验进一步证实，在 wiki 中持续进行知识整合对于高效的技能开发至关重要。

---

## 摘要 (Summary)

**WikiSkill** is an innovative framework designed to enhance AI agent capabilities by co-evolving executable agent skills with a persistent knowledge base (wiki). Traditional skill-evolution methods often scatter optimization insights across raw execution histories, preventing systematic reuse. WikiSkill addresses this by clearly separating raw execution experience, accumulated knowledge, and executable skills. 

> **WikiSkill** is an innovative framework designed to enhance AI agent capabilities by co-evolving executable agent skills with a persistent knowledge base (wiki). Traditional skill-evolution methods often scatter optimization insights across raw execution histories, preventing systematic reuse. WikiSkill addresses this by clearly separating raw execution experience, accumulated knowledge, and executable skills. 

Key findings from the paper include:
* **Superior Performance:** WikiSkill consistently outperforms state-of-the-art skill-evolution baselines across diverse benchmarks and models.
* **Model Scaling Synergy:** Skill evolution complements model scaling—larger models leverage evolved skills more effectively, while smaller models equipped with WikiSkill can outperform significantly larger models that lack them.
* **Cross-Model Transferability:** Evolved skills transfer seamlessly across models and model families, and skills evolved by other models can even surpass self-evolved skills.
* **Persistent Knowledge Value:** Ablation studies confirm that continuous knowledge consolidation in the wiki is crucial for effective skill development.

> Key findings from the paper include:
> * **Superior Performance:** WikiSkill consistently outperforms state-of-the-art skill-evolution baselines across diverse benchmarks and models.
> * **Model Scaling Synergy:** Skill evolution complements model scaling—larger models leverage evolved skills more effectively, while smaller models equipped with WikiSkill can outperform significantly larger models that lack them.
> * **Cross-Model Transferability:** Evolved skills transfer seamlessly across models and model families, and skills evolved by other models can even surpass self-evolved skills.
> * **Persistent Knowledge Value:** Ablation studies confirm that continuous knowledge consolidation in the wiki is crucial for effective skill development.

---

## 论文元数据 (Paper Metadata)

* **arXiv ID:** `arXiv:2608.27454` [cs.AI]
* **Subject Areas:** Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`)
* **Submission Date:** August 27, 2026
* **Authors:** Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu
* **DOI:** [10.48550/arXiv.2608.27454](https://doi.org/10.48550/arXiv.2608.27454)

> * **arXiv ID:** `arXiv:2608.27454` [cs.AI]
> * **Subject Areas:** Artificial Intelligence (`cs.AI`), Computation and Language (`cs.CL`)
> * **Submission Date:** August 27, 2026
> * **Authors:** Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu
> * **DOI:** [10.48550/arXiv.2608.27454](https://doi.org/10.48550/arXiv.2608.27454)

---

## 摘要详情 (Abstract)

Agent skills package specialized knowledge and workflows into reusable resources that extend AI agent capabilities. Recent work automatically discovers such skills from agent experience, which enables agents to progressively adapt through interaction. However, the insights that guide skill development typically remain scattered across optimization histories, limiting their systematic reuse across iterations. 

> Agent skills package specialized knowledge and workflows into reusable resources that extend AI agent capabilities. Recent work automatically discovers such skills from agent experience, which enables agents to progressively adapt through interaction. However, the insights that guide skill development typically remain scattered across optimization histories, limiting their systematic reuse across iterations. 

We introduce **WikiSkill**, a framework that co-evolves agent skills with a persistent knowledge base (wiki). At a high level, WikiSkill separates raw execution experience, accumulated knowledge, and executable skills, while continuously consolidating experience into the wiki, which subsequent skill updates can build on. Across diverse benchmarks and models, WikiSkill consistently outperforms state-of-the-art skill-evolution methods and improves over no-skill baselines in most model-benchmark settings. We find that skill evolution complements model scaling: larger models generally benefit more from evolved skills, while smaller models with skills can outperform substantially larger models without them. We also find that evolved skills transfer effectively across models and model families, and skills evolved by other models can outperform self-evolved skills. Finally, our ablation studies confirm that persistent knowledge accumulation in the wiki is critical for effective skill evolution. These results demonstrate the benefits of systematically accumulating and refining agent experience for developing reusable and transferable skills.

> We introduce **WikiSkill**, a framework that co-evolves agent skills with a persistent knowledge base (wiki). At a high level, WikiSkill separates raw execution experience, accumulated knowledge, and executable skills, while continuously consolidating experience into the wiki, which subsequent skill updates can build on. Across diverse benchmarks and models, WikiSkill consistently outperforms state-of-the-art skill-evolution methods and improves over no-skill baselines in most model-benchmark settings. We find that skill evolution complements model scaling: larger models generally benefit more from evolved skills, while smaller models with skills can outperform substantially larger models without them. We also find that evolved skills transfer effectively across models and model families, and skills evolved by other models can outperform self-evolved skills. Finally, our ablation studies confirm that persistent knowledge accumulation in the wiki is critical for effective skill evolution. These results demonstrate the benefits of systematically accumulating and refining agent experience for developing reusable and transferable skills.

---

## 资源与链接 (Resources & Links)

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.27454) | [HTML Version](https://arxiv.org/html/2608.27454v1) | [TeX Source](https://arxiv.org/src/2608.27454)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
* **External Bibliographic Tools:** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.27454)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.27454)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.27454)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.27454) | [HTML Version](https://arxiv.org/html/2608.27454v1) | [TeX Source](https://arxiv.org/src/2608.27454)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
> * **External Bibliographic Tools:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.27454)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.27454)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.27454)