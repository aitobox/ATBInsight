---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 大模型安全
- 红队测试
- 智能体
- 漏洞挖掘
- 技能演化
title: RedEvoAgent：基于经验驱动技能演化的自动化红队测试智能体
---
### 文章背景与核心概要

随着基于大语言模型（LLM）的智能体被广泛部署于生产级执行环境中，其面临的安全风险日益严峻。传统的红队测试方法多依赖固定的攻击模式，而新兴的智能体攻击者虽能通过轨迹检索协调多种越狱工具，但往往受限于检索偏差、工具归因模糊及高昂的上下文开销，导致攻击效率与可解释性不足。

RedEvoAgent 提出了一种创新的黑盒红队测试框架，旨在将跨案例的攻击轨迹提炼为简洁且可读的“攻击技能”。该系统通过工具有效性分析、决策工具归因更新以及验证棘轮机制，实现了攻击技能的持续演化，确保仅保留能带来可验证性能提升的更新。实验证明，该方法在多项基准测试中表现优异，显著提升了工具使用效率，并具备强大的跨模型与跨环境迁移能力。

---

## 摘要

> LLM-based agents are increasingly deployed in product-level execution harnesses, where jailbreaks can trigger harmful tool use and persistent state changes, creating greater risks than unsafe text generation alone. Existing automatic red-teaming methods often rely on fixed attacks, while recent agentic attackers coordinate multiple jailbreak tools and show stronger potential through trajectory-based retrieval. However, such retrieval can reuse misleading experiences due to retrieval bias and unclear tool credit, and full trajectories add context overhead while reducing interpretability. We propose RedEvoAgent, a black-box red-teaming agent that distills cross-case attack trajectories into a concise, human-readable attack skill. The attack skill adaptively evolves through tool-effectiveness profiling and Deciding-Tool Attribution for skill updates, and a validation ratchet that retains only updates improving validation performance. Experiments on multiple benchmarks, target models, and target execution harnesses show that RedEvoAgent outperforms fixed and agentic baselines, improves tool efficiency, and transfers across attacker models and target execution harnesses.

基于大语言模型的智能体正越来越多地被部署在生产级执行环境中，在这种环境下，越狱攻击可能触发有害的工具使用和持久的状态更改，从而产生比单纯的不安全文本生成更大的风险。现有的自动化红队测试方法通常依赖于固定的攻击，而近期的智能体攻击者通过基于轨迹的检索协调多种越狱工具，展现出了更强的潜力。然而，由于检索偏差和工具归因不清，这种检索方式可能会重复使用误导性的经验，且完整的轨迹增加了上下文开销，同时降低了可解释性。我们提出了 RedEvoAgent，这是一种黑盒红队测试智能体，它将跨案例的攻击轨迹提炼为简洁、人类可读的攻击技能。攻击技能通过工具有效性分析和用于技能更新的决策工具归因（Deciding-Tool Attribution）进行自适应演化，并采用验证棘轮机制，仅保留能提高验证性能的更新。在多个基准测试、目标模型和目标执行环境上的实验表明，RedEvoAgent 的表现优于固定的和基于智能体的基准方法，提高了工具效率，并能在攻击者模型和目标执行环境之间实现迁移。

---

## 元数据与参考信息

* **arXiv 标识符:** [arXiv:2608.27439](https://arxiv.org/abs/2608.27439) [cs.CR]
* **主要学科:** 密码学与安全 (`cs.CR`)
* **次要学科:** 人工智能 (`cs.AI`)
* **提交日期:** 2026年8月27日
* **DOI:** [10.48550/arXiv.2608.27439](https://doi.org/10.48550/arXiv.2608.27439)
* **许可协议:** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

---

## 作者

* Junjie Zhang
* Hui Liu
* Kecheng Chen
* Xianbo Mo
* Changsheng Chen
* Haoliang Li

---

## 全文与资源链接

* [查看 PDF](https://arxiv.org/pdf/2608.27439)
* [HTML 版本 (实验性)](https://arxiv.org/html/2608.27439v1)
* [TeX 源码](https://arxiv.org/src/2608.27439)

### 学术与文献工具
* [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.27439)
* [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.27439)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.27439)