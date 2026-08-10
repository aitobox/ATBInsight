---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-11
hide:
- navigation
tags:
- AI安全
- 智能体外壳
- 漏洞评估
- 持久化威胁
- Benchmark
title: HarnessSafe：评估智能体外壳中持久化载体的安全性
---
### 文章背景与核心概要
现代AI智能体外壳（Agent Harnesses）通常利用内存、技能、工具以及共享工件等持久化载体，在不同的任务和会话之间保持状态。虽然这种设计赋予了系统强大的功能，但也带来了延迟生效的安全隐患：受攻击者操控的内容可能会跨越系统边界，并在后续对良性用户请求造成危害。

为了弥补现有基准测试通常只关注孤立载体、且无法有效追踪风险传播的局限性，作者团队推出了 **HarnessSafe**。该基准包含覆盖七大持久化载体系列的328个可执行案例，并对主流的智能体外壳进行了全面评估。通过将攻击建模为“持久化风险生命周期”（Persistent-Risk Lifecycle）并采用多阶段、基于追踪的评估方法，本研究揭示了攻击遏制效果具有高度的载体特异性，且极大地依赖于所选择的外壳与大模型配置。

---

# HarnessSafe: Evaluating Safety Across Persistent Carriers in Agent Harnesses

## Summary
Modern AI agent harnesses often persist state across different tasks and sessions using persistent carriers such as memory, skills, tools, and shared artifacts. While powerful, this persistence creates delayed security risks: attacker-influenced content can cross system boundaries and eventually compromise benign user requests. 

To address the limitations of existing benchmarks—which typically focus on isolated carriers or harnesses and fail to track risk propagation—the authors introduce **HarnessSafe**. This benchmark includes 328 executable cases spanning seven persistent-carrier families and evaluates mainstream agent harnesses. By modeling attacks as a "Persistent-Risk Lifecycle" and employing a multi-stage, trace-based evaluation method, the study reveals that attack containment is highly carrier-specific and heavily dependent on the chosen harness-model configuration.

> 现代AI智能体外壳（Agent Harnesses）通常利用内存、技能、工具以及共享工件等持久化载体，在不同的任务和会话之间保持状态。虽然这种设计赋予了系统强大的功能，但也带来了延迟生效的安全隐患：受攻击者操控的内容可能会跨越系统边界，并在后续对良性用户请求造成危害。
> 
> 为了弥补现有基准测试（通常仅关注孤立的载体或外壳，且无法追踪风险传播）的局限性，作者团队推出了 **HarnessSafe**。该基准测试包含覆盖七大持久化载体系列的328个可执行案例，并对主流的智能体外壳进行了评估。通过将攻击建模为“持久化风险生命周期”（Persistent-Risk Lifecycle）并采用多阶段、基于追踪的评估方法，研究表明：攻击的遏制效果具有高度的载体特异性，且极大地依赖于所选择的外壳-模型配置。

---

## Paper Metadata

| Field | Details |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.06984](https://arxiv.org/abs/2608.06984) [cs.CR] |
| **Primary Subject** | Cryptography and Security (`cs.CR`) |
| **Secondary Subjects** | Artificial Intelligence (`cs.AI`) |
| **Authors** | Xiao Zhang, Yusheng Wang, Yuhao Fei, Dongyuan Li, Zian Liang, Liuyu Xiang, Hongxun Gu, Zhaofeng He |
| **Submitted** | August 7, 2026 |
| **Length** | 21 pages, 3 figures (Preprint) |
| **License** | [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png) |

> | 字段 | 详情 |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.06984](https://arxiv.org/abs/2608.06984) [cs.CR] |
| **主分类** | 密码学与安全 (`cs.CR`) |
| **次分类** | 人工智能 (`cs.AI`) |
| **作者** | Xiao Zhang, Yusheng Wang, Yuhao Fei, Dongyuan Li, Zian Liang, Liuyu Xiang, Hongxun Gu, Zhaofeng He |
| **提交时间** | 2026年8月7日 |
| **篇幅** | 21页，3张图表（预印本） |
| **许可协议** | [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png) |

---

## Abstract
Modern agent harnesses persist state across tasks and sessions through persistent carriers like memory, skills, tools, and shared artifacts. However, this capability creates delayed safety risks: attacker-influenced content can cross system boundaries and later affect the execution of a benign request. 

Existing benchmarks typically focus on a few carriers or harnesses, while end-to-end attack-success rates reveal little about how risks propagate. To this end, we present **HarnessSafe**, a benchmark comprising 328 executable cases across seven persistent-carrier families and evaluated on most mainstream agent harnesses. 

Each case is specified as a **Persistent-Risk Lifecycle** that traces attacker influence from its initial entry, through persistence across carriers and system boundaries, to a later benign trigger and an observable violation. We further introduce a multi-stage, trace-based evaluation that uses observable execution evidence to determine how far each attack chain progresses and where it is stopped. 

Experiments show that containment is carrier-specific and strongly depends on the harness-model configuration. Both the harness and model backend substantially shape containment outcomes, and attack success rates cannot reflect distinct lifecycle progression patterns.

> 现代智能体外壳通过内存、技能、工具和共享工件等持久化载体，在任务与会话之间保持状态。然而，这种能力也带来了延迟生效的安全风险：受攻击者影响的内容可以跨越系统边界，并在随后影响良性请求的执行。
> 
> 现有的基准测试通常仅关注少数载体或外壳，而端到端的攻击成功率无法揭示风险是如何传播的。为此，我们提出了 **HarnessSafe**，这是一个包含328个可执行案例的基准测试，涵盖七大持久化载体系列，并在大多数主流智能体外壳上进行了评估。
> 
> 每个案例都被指定为一个**持久化风险生命周期**，用于追踪攻击者影响力的全过程：从初始切入，到跨载体和系统边界的持久化，再到后来的良性触发以及可观察的违规行为。我们进一步引入了一种多阶段、基于追踪的评估方法，利用可观察的执行证据来确定每个攻击链推进到了多远、在何处被阻断。
> 
> 实验表明，风险遏制效果具有载体特异性，并且强烈依赖于外壳-模型配置。智能体外壳与模型后端共同显著影响着遏制结果，同时单纯的攻击成功率无法反映出不同的生命周期演变模式。

---

## Links & Resources
* **Access Paper:** 
  * [View PDF](https://arxiv.org/pdf/2608.06984)
  * [HTML Version (Experimental)](https://arxiv.org/html/2608.06984v1)
  * [TeX Source](https://arxiv.org/src/2608.06984)
* **Citations & Metrics:** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.06984)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.06984)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.06984)

> * **访问论文：** 
>   * [查看 PDF](https://arxiv.org/pdf/2608.06984)
>   * [HTML 版本（实验性）](https://arxiv.org/html/2608.06984v1)
>   * [TeX 源码](https://arxiv.org/src/2608.06984)
> * **引用与指标：** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.06984)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.06984)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.06984)