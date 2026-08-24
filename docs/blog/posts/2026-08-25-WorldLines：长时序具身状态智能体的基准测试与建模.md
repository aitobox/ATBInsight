---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-25
hide:
- navigation
tags:
- 具身智能
- 长效记忆
- 基准测试
- 智能体规划
- EMNLP2026
title: WorldLines：长时序具身状态智能体的基准测试与建模
---
### 文章背景与核心概要
为了在现实环境中长期有效地辅助人类，具身AI智能体需要具备强大的机制来追踪用户的日常生活习惯、动态的世界状态以及历史交互记录。传统的基准测试往往只关注纯语言驱动的信息检索（忽略了物理上下文），或是短时序的任务执行（忽略了长期记忆）。

本文推出了 **WorldLines**，这是一个专为长时序具身家庭辅助而设计的主题驱动型基准测试。该基准构建了时间跨度较长的家庭交互轨迹，涵盖对话、动作、执行反馈以及状态变化（如物体和设备属性的修改），并将其转化为包含证据链的 **记忆问答（Memory QA）** 与 **具身任务规划（Embodied Task Planning）** 样本。此外，作者还提出了 **ObsMem**，这是一种基于观察者锚定的记忆框架，通过维护具备可见性感知（visibility-aware）的记忆和动作原生状态轨迹（action-native state trails），从而为状态感知的决策提供有力支撑。

---

## 摘要 (Abstract)

> 为了在真实的家庭环境中长期协助人类，具身智能体必须记住用户的日常生活习惯、世界状态以及过往的交互。现有的长期记忆基准测试主要评估以语言为中心的检索和问答，而具身基准测试则通常侧重于短时序的任务执行，并未在动态环境中测试长期记忆的使用情况。我们推出了 WorldLines，这是一个针对长时序具身家庭辅助的项目驱动型基准测试。它构建了包含对话、动作、执行反馈、物体及设备状态变化在内的、时间跨度延伸的家庭交互轨迹，并将其转换为用于记忆问答和具身任务规划的证据链样本。我们进一步提出了 ObsMem，这是一个基于观察者锚定的记忆框架，它维护了具可见性感知的记忆和动作原生的状态轨迹，以实现状态感知的决策。实验揭示了在部分可观测性、被覆盖的世界状态以及将长期记忆转化为具身计划方面持续存在的挑战，而 ObsMem 为该场景提供了一个更强大的参考架构。

> To assist humans over extended periods in real homes, embodied agents must remember user routines, world states, and past interactions. Existing long-term memory benchmarks mainly evaluate language-centric retrieval and question answering, while embodied benchmarks often focus on short-horizon task execution without testing long-term memory use in dynamic environments. We introduce WorldLines, a project-driven benchmark for long-horizon embodied household assistance. It constructs temporally extended household traces with dialogues, actions, execution feedback, object and device state changes, and converts them into evidence-linked samples for Memory QA and Embodied Task Planning. We further propose ObsMem, an observer-grounded memory framework that maintains visibility-aware memories and action-native state trails for state-aware decisions. Experiments reveal persistent challenges in partial observability, overwritten world states, and translating long-term memory into embodied plans, while ObsMem offers a stronger reference architecture for this setting.

---

## 论文元数据 (Paper Metadata)

* **arXiv ID:** [arXiv:2606.18847](https://arxiv.org/abs/2606.18847) [cs.AI]
* **主要学科:** 人工智能 (`cs.AI`)
* **会议收录:** 已被 **EMNLP 2026** 录用
* **提交日期:** 2026年6月17日提交；2026年8月21日修订 (v2)
* **DOI:** [10.48550/arXiv.2606.18847](https://doi.org/10.48550/arXiv.2606.18847)

> * **arXiv ID:** [arXiv:2606.18847](https://arxiv.org/abs/2606.18847) [cs.AI]
> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Conference Acceptance:** Accepted to **EMNLP 2026**
> * **Submission Dates:** Submitted June 17, 2026; Revised August 21, 2026 (v2)
> * **DOI:** [10.48550/arXiv.2606.18847](https://doi.org/10.48550/arXiv.2606.18847)

---

## 作者列表 (Authors)

* Yehang Zhang
* Jianchong Su
* Haojian Huang
* Yifan Chang
* Tianhao Zhou
* Xinli Xu
* Yingjie Xu
* Yinchuan Li
* Zexi Li
* Ying-Cong Chen

> * Yehang Zhang
> * Jianchong Su
> * Haojian Huang
> * Yifan Chang
> * Tianhao Zhou
> * Xinli Xu
> * Yingjie Xu
> * Yinchuan Li
> * Zexi Li
> * Ying-Cong Chen

---

## 核心贡献与发现 (Key Contributions & Findings)

* **WorldLines 基准测试：** 一项新颖的主题驱动型基准测试，通过时间延展的家庭场景，将长期记忆与具身任务执行有机桥接。
* **ObsMem 框架：** 一种观察者锚定的记忆架构，利用可见性感知记忆与动作原生状态轨迹，增强了状态感知的决策能力。
* **评估洞察：** 实验凸显了在应对部分可观测性、管理被覆盖的世界状态以及成功将长期记忆转化为可执行具身计划方面所面临的持续挑战。

> * **WorldLines Benchmark:** A novel project-driven benchmark bridging long-term memory and embodied task execution via temporally extended household scenarios.
> * **ObsMem Framework:** An observer-grounded memory architecture leveraging visibility-aware memories and action-native state trails for enhanced state-aware decision-making.
> * **Evaluation Insights:** Experiments highlight ongoing challenges in handling partial observability, managing overwritten world states, and successfully translating long-term memory into executable embodied plans.

---

## 访问与资源 (Access & Resources)

* **全文链接：** [查看 PDF](https://arxiv.org/pdf/2606.18847) | [HTML (实验性)](https://arxiv.org/html/2606.18847v2) | [TeX 源码](https://arxiv.org/src/2606.18847)
* **开源许可：** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/) *(查看许可图标：![license icon](./images/345c7ad61f1b.png))*
* **引用与工具：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2606.18847) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.18847) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.18847)

> * **Full-Text Links:** [View PDF](https://arxiv.org/pdf/2606.18847) | [HTML (Experimental)](https://arxiv.org/html/2606.18847v2) | [TeX Source](https://arxiv.org/src/2606.18847)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) *(View License Image: ![license icon](./images/345c7ad61f1b.png))*
> * **Citations & Tools:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2606.18847) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2606.18847) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2606.18847)