---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 浏览器智能体
- 大模型
- 强化学习
- 智能体评估
- WebVoyager
title: Wuying-Browser-Agent：面向真实世界的长周期基础浏览器智能体
---
### 文章背景与核心概要
尽管现有的浏览器智能体（Browser Agents）在简短且干净的演示任务中表现优异，但在真实世界环境中部署时却面临着截然不同的挑战：智能体必须在活跃的真实网站上持续执行数十个决策步骤、导航复杂的图形用户界面（UI），并具备从错误中积极恢复的能力。

本文作者指出，要弥合这一差距，不能仅仅依赖模型的规模扩张，而是需要在整个处理链路的各个层面——包括执行、监督、优化和评估——实现全面对齐。为此，论文推出了 **Wuying-Browser-Agent** 统一框架，包含四个核心部分：1. 结构化浏览器封装（Structured Browser Harness），提供稳定的执行基元与面向决策的上下文管理；2. 反思与 UI 专用课程监督微调（RUIC-SFT），显式训练模型的错误恢复轨迹与复杂 UI 交互能力；3. 散度感知在线 GRPO（DAO-GRPO），通过基于势函数的奖励塑造与散度感知步骤加权，增强长周期信用分配；4. BrowserBench，这是一个全新的双语真实网络基准测试，包含 350 个任务、平均步数达 37.9 步，专门用于暴露长周期运行中的失效模式。

性能基准测试确立了 **Wuying-Browser-Agent-27B** 在浏览器使用任务上的开源最新技术水平（SOTA），同时其核心训练链路展现出超越网页浏览场景的强大通用智能体迁移能力。

---

**作者：** AIMAE Team (Tianxiang Chen, Yan Cheng, Zhangye Han, Xiaowei Li, Chang Liu, Cheng Liu, Zhongqiang Ma, Long Peng, Xiaobing Tu, Yinggui Wang, Hongliang Wei, Chen Wu, Daiping Xin, Kunyu Zhou, Pengyang Zhou, Peiyuan Chen, Ziyuan Chen, Yutao Deng, Chunyu Dong, Xiangyu Fu, Yicheng Feng, Ruian He, Haochen Li, Miancan Liu, Zhengqin Liu, Wei Peng, Jinkui Ren, Haoyu Tan, Dong Xiao, Rongkun Xue, Shujian Yang, Xianhang Ye, Ziqi Yuan, Ziyang Yu, Linghan Zhang, Xiantao Zhang, Xuanpu Zhao, Yinan Zhao, Zhenghui Zhao, Bin Zhu, Likai Zou)  
**提交时间：** 2026年8月18日  
**主要领域：** 人工智能 (`cs.AI`)  
**arXiv ID：** [arXiv:2608.17319](https://arxiv.org/abs/2608.17319) [cs.AI]  

---

## 执行摘要 (Executive Summary)

> While browser agents typically excel at short and clean demonstrations, deploying them in real-world environments presents fundamentally different challenges: agents must sustainably execute dozens of decisions on live websites, navigate complex UIs, and actively recover from mistakes. 

尽管浏览器智能体通常擅长简短、干净的演示，但在真实世界环境中部署它们面临着根本不同的挑战：智能体必须在活跃的网站上持续执行数十个决策，导航复杂的 UI，并从错误中积极恢复。

> The authors argue that overcoming this gap requires a holistic alignment across every level of the pipeline—execution, supervision, optimization, and evaluation—rather than relying on model scale alone. To address this, the paper introduces **Wuying-Browser-Agent**, a unified framework comprising:
> 1. **Structured Browser Harness:** Delivers stable execution primitives and decision-oriented context management.
> 2. **Reflection and UI-specialized Curriculum SFT (RUIC-SFT):** Explicitly trains models on recovery trajectories and complex-UI interactions.
> 3. **Divergence-Aware Online GRPO (DAO-GRPO):** Enhances long-horizon credit assignment using potential-based reward shaping and divergence-aware step weighting.
> 4. **BrowserBench:** A new bilingual, real-web benchmark featuring 350 tasks averaging 37.9 steps designed specifically to expose long-horizon failure modes.

作者认为，克服这一差距需要对整个流程的各个层面（执行、监督、优化和评估）进行整体对齐，而不是仅仅依靠模型规模。为了解决这个问题，论文推出了 **Wuying-Browser-Agent**，这是一个统一的框架，包含：
1. **结构化浏览器封装（Structured Browser Harness）：** 提供稳定的执行基元和面向决策的上下文管理。
2. **反思与 UI 专用课程监督微调（RUIC-SFT）：** 显式训练模型处理恢复轨迹和复杂 UI 交互。
3. **散度感知在线 GRPO（DAO-GRPO）：** 利用基于潜力的奖励塑造和散度感知步骤加权来增强长期信用分配。
4. **BrowserBench：** 一个新的双语真实网络基准测试，包含 350 个任务，平均 37.9 步，专门用于暴露长期失效模式。

> Performance benchmarks establish **Wuying-Browser-Agent-27B** as a new open-state-of-the-art across browser-use tasks, while its core pipeline demonstrates strong general agentic transfer capabilities beyond just web browsing.

性能基准确立了 **Wuying-Browser-Agent-27B** 在浏览器使用任务中的全新开源领先水平（SOTA），同时其核心流程展示了超越网页浏览的强大通用智能体迁移能力。

---

## 摘要 (Abstract)

> Browser agents perform well on short, clean demonstrations, but real deployment is fundamentally different: agents must sustain dozens of decisions on live websites while recovering from mistakes and navigating complex UIs. We argue that closing this gap requires alignment at every level of the pipeline, including execution, supervision, optimization, and evaluation, rather than scale alone. 

浏览器智能体在简短、干净的演示中表现良好，但实际部署有着根本的不同：智能体必须在活跃的网站上维持数十个决策，同时从错误中恢复并导航复杂的 UI。我们认为，要缩小这一差距，需要在流程的各个层面（包括执行、监督、优化和评估）进行对齐，而不仅仅是规模本身。

> We present **Wuying-Browser-Agent**, a unified framework that addresses each of these levels:
> * A structured browser harness provides stable execution primitives and decision-oriented context management.
> * Reflection and UI-specialized Curriculum SFT (RUIC-SFT) explicitly trains on recovery trajectories and complex-UI interactions.
> * Divergence-Aware Online GRPO (DAO-GRPO) improves long-horizon credit assignment through potential-based reward shaping and divergence-aware step weighting.
> * Finally, we introduce **BrowserBench**, a bilingual real-web benchmark of 350 tasks averaging 37.9 steps, because most existing benchmarks are too short to expose long-horizon failure modes.

我们提出了 **Wuying-Browser-Agent**，这是一个解决上述各个层面的统一框架：
* 结构化浏览器封装提供了稳定的执行基元和面向决策的上下文管理。
* 反思与 UI 专用课程监督微调（RUIC-SFT）对恢复轨迹和复杂 UI 交互进行显式训练。
* 散度感知在线 GRPO（DAO-GRPO）通过基于潜力的奖励塑造和散度感知步骤加权，改进了长期信用分配。
* 最后，我们推出了 **BrowserBench**，这是一个包含 350 个任务、平均 37.9 步的双语真实网络基准测试，因为大多数现有的基准测试太短，无法暴露出长期的失效模式。

> Wuying-Browser-Agent-27B achieves **80.6%** on WebVoyager, **66.7%** on Online-Mind2Web, and **65.1%** on BrowserBench, establishing a new open-source state of the art on browser-use benchmarks. The same pipeline also transfers beyond browser use, demonstrating strong general agentic ability and reaching an average score of **73.8** on Tau2-Bench, Claw-Eval, and BFCL-v4.

Wuying-Browser-Agent-27B 在 WebVoyager 上取得了 **80.6%** 的准确率，在 Online-Mind2Web 上取得了 **66.7%**，在 BrowserBench 上取得了 **65.1%**，在浏览器使用基准测试中确立了新的开源 SOTA。相同的流程也扩展到了浏览器使用之外的场景，展示了强大的通用智能体能力，在 Tau2-Bench、Claw-Eval 和 BFCL-v4 上平均分达到了 **73.8**。

---

## 核心性能指标 (Key Performance Metrics)

> | Benchmark / Dataset | Wuying-Browser-Agent-27B Score |
> | :--- | :--- |
> | **WebVoyager** | 80.6% |
> | **Online-Mind2Web** | 66.7% |
> | **BrowserBench** (New) | 65.1% |
> | **General Agentic Transfer** (Tau2-Bench, Claw-Eval, BFCL-v4 avg) | 73.8 |

| 基准测试 / 数据集 | Wuying-Browser-Agent-27B 得分 |
| :--- | :--- |
| **WebVoyager** | 80.6% |
| **Online-Mind2Web** | 66.7% |
| **BrowserBench** (新) | 65.1% |
| **通用智能体迁移** (Tau2-Bench, Claw-Eval, BFCL-v4 平均分) | 73.8 |

---

## 全文与资源链接 (Full-Text & Resources Links)

> * **View PDF:** [arXiv:2608.17319 PDF](https://arxiv.org/pdf/2608.17319)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.17319v1)
> * **TeX Source:** [arXiv e-Print Source](https://arxiv.org/src/2608.17319)
> * **License:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/) ![license icon](./images/079cd8198ba3.png)

* **查看 PDF：** [arXiv:2608.17319 PDF](https://arxiv.org/pdf/2608.17319)
* **HTML 版本：** [arXiv HTML (实验性)](https://arxiv.org/html/2608.17319v1)
* **TeX 源码：** [arXiv e-Print 源码](https://arxiv.org/src/2608.17319)
* **许可证：** [知识共享 署名-非商业性使用-相同方式共享 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/) ![license icon](./images/079cd8198ba3.png)