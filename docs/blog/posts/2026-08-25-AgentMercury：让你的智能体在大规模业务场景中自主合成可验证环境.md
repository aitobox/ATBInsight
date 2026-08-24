---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- AI Agent
- 环境合成
- 强化学习
- 业务场景
- 泛化能力
title: AgentMercury：让你的智能体在大规模业务场景中自主合成可验证环境
---
### 文章背景与核心概要
训练人工智能智能体（AI Agent）通常依赖于手动构建的环境或绑定在预定义场景上的以任务为中心的基准。这种传统方法难以扩展，且无法反映现实、不断演变的复杂工作流。为了克服这一局限性，本文作者推出了 **AgentMercury**——一个可扩展的框架，能够直接从高层业务场景中合成可执行、可验证的环境。AgentMercury 没有为孤立的任务构建环境，而是实例化包含实体、服务、工具、状态以及跨服务不变量的持久世界，从而让多样化的任务和交互轨迹自然涌现。

该研究构建了覆盖 14 个行业和 50 个国家的 4,783 个可执行环境，并将其用作强化学习的训练底层。实验证明，尽管在生成时并未针对特定的评估基准，但在 AgentMercury 环境上训练出的策略在企业工作流以及涵盖推理、编码、科学计算和工具使用的域外任务中均表现出显著的性能提升。此外，通过在构建轨迹上微调模型，可执行世界的编写成功率从 3.3% 大幅提升至 83.3%，这表明环境合成本身也可以成为一项可学习的能力。

---

# AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Scenarios at Scale

**Authors:** Minbyul Jeong, Chanwoong Yoon  
**arXiv:** [arXiv:2608.20634 [cs.CL]]  
**Submitted:** August 21, 2026  
**Primary Subject:** Computation and Language (`cs.CL`)  
**Secondary Subjects:** Artificial Intelligence (`cs.AI`)  
**DOI:** [10.48550/arXiv.2608.20634](https://doi.org/10.48550/arXiv.2608.20634)  

---

## 📌 Summary

Training AI agents typically relies on manually constructed environments or task-centric benchmarks tied to predefined scenarios. This approach struggles to scale and fails to reflect the complexity of realistic, evolving workflows. 

To overcome this limitation, the authors introduce **AgentMercury**, a scalable framework that synthesizes executable, verifiable environments directly from high-level business scenarios. Rather than building environments for isolated tasks, AgentMercury instantiates persistent worlds complete with entities, services, tools, states, and cross-service invariants, allowing diverse tasks and interaction trajectories to naturally emerge.

### Key Highlights
* **Massive Scale:** The framework constructs 4,783 executable environments spanning 14 industries and 50 countries.
* **Broad Generalization:** Despite not being explicitly trained on evaluation benchmarks, policies trained on AgentMercury environments show substantial performance gains across enterprise workflows and out-of-domain tasks (including reasoning, coding, scientific computing, and tool use).
    * *Qwen3.5-4B* improved from **12.3 to 15.7** on `EnterpriseOps-GYM`.
    * *Qwen3.5-4B* improved from **45.9 to 56.0** on `AIME26`.
* **Learnable Construction:** Fine-tuning *Qwen3.5-35B-A3B* on construction traces dramatically increased executable-world authoring success from **3.3% to 83.3%** on held-out business scenarios, demonstrating that environment synthesis itself can become a learnable capability.

---

## 📄 Abstract

> Agents learn to act through interaction with environments, yet the environments used for training are often manually constructed or synthesized around predefined tasks and benchmarks. This task-centric paradigm makes it difficult to scale environments that reflect realistic and evolving workflows where diverse tasks can naturally emerge from the underlying world. We introduce AgentMercury, a scalable framework for synthesizing executable environments from high-level business scenarios. Rather than constructing an environment for a specific task, AgentMercury first instantiates a persistent world with entities, services, tools, state, and executable cross-service invariants, from which diverse tasks and interaction trajectories can subsequently emerge. We construct 4,783 executable environments spanning 14 industries and 50 countries, and use them as training substrates for reinforcement learning. Despite being generated without targeting the evaluation benchmarks, policies trained on these business-oriented environments improve substantially on both enterprise workflows and out-of-domain benchmarks spanning reasoning, coding, scientific computing, and tool use. In our experiments, Qwen3.5-4B improves from 12.3 to 15.7 on EnterpriseOps-GYM and from 45.9 to 56.0 on AIME26 after training on AgentMercury environments. We further show that the construction process itself can be learned: fine-tuning Qwen3.5-35B-A3B on construction traces increases executable-world authoring success from 3.3% to 83.3% on held-out business scenarios. These results show that scenario-grounded environments can provide useful and generalizable learning signals beyond benchmark-specific training, while their construction can itself become a learnable capability.

---

## 🔗 Links & Resources

* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.20634) | [HTML (Experimental)](https://arxiv.org/html/2608.20634v1) | [TeX Source](https://arxiv.org/src/2608.20634)
* **License:** [Creative Commons Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/) *(License icon preserved below per instructions)*:  
  <img alt="license icon" role="presentation" src="./images/5283893486a4.png" width="20" />
* **External Bibliographic Tools:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.20634) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.20634) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.20634)