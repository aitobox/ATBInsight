---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- LLM推理
- 仿真框架
- AI智能体
- 系统架构
- 性能评估
title: Simthesizer：面向大模型推理服务系统的智能体驱动仿真框架
---
### 文章背景与核心概要
现代大语言模型（LLM）推理服务系统正经历着快速演进，这主要归功于智能体工作流（agentic workflows）和分离开源推理（disaggregated serving）等新兴机制的涌现。然而，传统的单体仿真器（monolithic simulators）难以跟上这种更迭速度，因为每一个新功能的引入都需要进行侵入式的、手动的重写，这导致实际部署的系统与仿真工具之间的差距日益扩大。

为了弥合这一差距，作者引入了 **Borg**（作为 *Simthesizer* 的核心），这是一个由智能体驱动的仿真框架。Borg 采用了一种可组合的仿真器基础设施，能够将完整的服务工作流和控制决策统一表示为一个动态图。通过引入受控的编码智能体（**Synthesizer 智能体**），该框架在严格的护栏和保真度验证下，将自然语言的功能请求自动转换为代码，从而允许单个共享的仿真器实现动态演进。

实证评估表明，基于 Borg 的扩展其平均吞吐量误差仅为 **2.51%**（相比之下，现有仿真器的误差为 6.03%）。此外，在模拟相同工作负载时，Borg 的速度比最先进的仿真器（分别为 LLMServingSim2.0 和 Vidur）快了 **284.96 倍** 和 **23.19 倍**。

---

## Summary

> Modern Large Language Model (LLM) serving systems evolve rapidly, driven by emerging mechanisms such as agentic workflows and disaggregated serving. Traditional monolithic simulators struggle to keep pace, as each new feature requires invasive manual rewrites, creating a widening gap between deployed systems and simulation tools. 

> To bridge this gap, the authors introduce **Borg** (featured in *Simthesizer*), an agent-driven simulation framework. Borg utilizes a composable simulator infrastructure that uniformly expresses complete serving workflows and control decisions as a unified dynamic graph. By employing a harnessed coding agent (**Synthesizer agent**), the framework translates natural-language feature requests into code under strict guardrails and fidelity validation, allowing a single shared simulator to evolve dynamically. 

> Empirical evaluations demonstrate that Borg-based extensions achieve an average throughput error of **2.51%** (compared to 6.03% for existing simulators). Furthermore, Borg simulates identical workloads up to **284.96×** and **23.19×** faster than state-of-the-art simulators (LLMServingSim2.0 and Vidur, respectively).

---

## Paper Metadata

> ## Paper Metadata

| Attribute | Details |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.24650](https://arxiv.org/abs/2608.24650) [cs.AR] |
| **Subjects** | Hardware Architecture (`cs.AR`); Artificial Intelligence (`cs.AI`) |
| **Submission Date** | August 25, 2026 |
| **Authors** | Wonung Kim, Hyunmin Choi, Minsu Kim, Jaehong Cho, Yeongwook Kim, Jongse Park |
| **DOI** | [10.48550/arXiv.2608.24650](https://doi.org/10.48550/arXiv.2608.24650) |

---

## Access Links & Resources

> ## Access Links & Resources

* **Full-Text:** [View PDF](https://arxiv.org/pdf/2608.24650) | [HTML (Experimental)](https://arxiv.org/html/2608.24650v1) | [TeX Source](https://arxiv.org/src/2608.24650)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
* **Citations & Metrics:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.24650) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.24650) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.24650)