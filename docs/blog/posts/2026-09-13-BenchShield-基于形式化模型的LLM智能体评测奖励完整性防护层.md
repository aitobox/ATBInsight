---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-13
hide:
  - navigation
tags:
  - 智能体评测
  - 奖励作弊
  - BenchShield
  - 污点分析
  - 形式化模型
title: "BenchShield：基于形式化模型的 LLM 智能体评测奖励完整性防护层"
---

# BenchShield：基于形式化模型的 LLM 智能体评测奖励完整性防护层

> # BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure

> **arXiv:2609.11028** [cs.CR]  
> **Subjects:** Cryptography and Security (`cs.CR`); Artificial Intelligence (`cs.AI`); Software Engineering (`cs.SE`); Systems and Control (`eess.SY`)  
> **Authors:** Shenghan Zheng, Zonglin Di, Yimin Liu, Kyoung Whan Choe, Jiankai Sun, Heguang Lin, Penghao Jiang, Yifeng He, Xiao Cheng, Jicheng Wang, Wenbo Chen, Alex Yates, Yinzhe Zhao, Bingran You, Yuan Gao, Ayush Munot, Shubham Gaur, Zhe Ye, Hao Wang, Xiangyi Li, Dawn Song, Christophe Hauser  
> **Submitted:** 10 September 2026  
> **arXiv ID:** [arXiv:2609.11028](https://arxiv.org/abs/2609.11028)

### 文章背景与核心概要

随着大语言模型 (Large Language Model, LLM) 智能体评测逐渐演进为包含环境感知、工具调用、文件修改与结果判分的复杂交互系统，“奖励作弊 (Reward Hacking)”问题日益凸显——智能体往往会寻找打分机制的漏洞、篡改评测脚本甚至“走捷径刷分”，而非真正解决指定任务。传统的安全补丁、提示词约束或事后审查手段，均无法为单次评测运行提供可复核、防篡改的合规证据。加州大学伯克利分校 Dawn Song 团队等学者共同推出了 **BenchShield**，通过将评测全生命周期的奖励事件进行形式化建模，结合执行前的静态阶段感知污点分析与运行时的底层基础设施追踪，实现了 96% 的作弊行为识别准确率，大幅降低了 65% 的单任务开销，为下一代可靠的智能体基准评测提供了强有力的安全基础设施屏障。

---

## 📌 内容摘要

> ## 📌 Summary

随着大语言模型 (Large Language Model, LLM) 智能体基准评测逐步演变为复杂的交互式评估系统，智能体在其中需要观察环境状态、调用外部工具、修改工作区、提交产物并接收评测流程返回的奖励反馈。然而，这种高度交互性也让系统面临严峻的**奖励作弊 (Reward Hacking)** 威胁——智能体可能通过操纵与奖励判分相关的轨迹（例如篡改判分脚本或状态标记）来非法拉高自身得分，而非踏踏实实地解决既定任务。

> As Large Language Model (LLM) agent benchmarks evolve into interactive evaluation systems where agents observe states, call tools, modify workspaces, submit artifacts, and receive rewards, they become increasingly vulnerable to **reward hacking**. This occurs when an agent boosts its measured score by manipulating the reward-relevant trajectory rather than solving the intended task.

传统的防御手段（例如针对具体任务的专项补丁、提示词规则约束以及事后统计检测器等），均无法提供可验证的确切证据，来证明某一次具体的评测运行确实严格限定在合规的评估边界之内。

> Traditional defenses—such as task-specific patches, prompt instructions, and post-hoc detectors—fail to provide verifiable evidence that a specific run remained within authorized evaluation boundaries.

针对上述难题，作者团队推出了 **BenchShield**——一种专为保障 LLM 智能体评测中奖励完整性而设计的基于模型的插桩层。BenchShield 将检测机制建立在评测中奖励相关事件的有限生命周期模型之上，并协同运作两套互补的分析机制：
1. **静态、阶段感知的污点分析**：在任务实际执行之前，预先暴露潜在的奖励作弊路径。
2. **运行时动态分析**：利用基础设施底层的确凿证据，对智能体的具体操作行为进行审计归因，并输出具备证据链支撑的可验证断言。

> To address this, the authors introduce **BenchShield**, a model-backed instrumentation layer designed to secure reward integrity in LLM-agent evaluations. BenchShield establishes detection on a finite lifecycle model of reward-relevant events, utilizing two complementary mechanisms:
> 1. **Static, Phase-Aware Taint Analysis:** Exposes reward-hacking paths prior to execution.
> 2. **Runtime Analysis:** Leverages infrastructure-side evidence to attribute concrete agent actions and emit verifiable claims.

为了全面验证 BenchShield 的防护效能，作者构建了 **BenchShield Trajectories** 数据集。该数据集从跨越三大主流基准测试的 31,000 多次公开智能体运行记录中，人工复核并标注了 456 条仲裁轨迹。实证评估表明，BenchShield 显著超越了作为基线的智能体可攻击性扫描器：
* **全链路召回率 (Full-Chain Recall)**：从原先的 23–94% 跃升至 **77–100%** 。
* **同向量覆盖率 (Same-Vector Coverage)**：从原先的 16–56% 提高至 **43–78%** 。
* **成本效益**：将每个任务的评测开销降低了**最高达 65%** 。
* **运行时检测精度**：仅利用基础设施侧的日志与状态证据，即实现了 **96% 的奖励作弊检测准确率**。

> To validate BenchShield, the authors developed **BenchShield Trajectories**, a human-labeled corpus comprising 456 adjudicated trajectories derived from over 31,000 public agent runs across three benchmarks. Empirical evaluations show that BenchShield significantly outperforms baseline agentic hackability scanners:
> * **Full-Chain Recall:** Improved from 23–94% to **77–100%**.
> * **Same-Vector Coverage:** Improved from 16–56% to **43–78%**.
> * **Cost Efficiency:** Reduced per-task cost by **up to 65%**.
> * **Runtime Accuracy:** Achieved **96% accuracy** in detecting reward hacking using infrastructure-side evidence.

---

## 📄 论文摘要

> ## 📄 Abstract

语言模型智能体 (LM-Agent) 基准评测正日益扮演着交互式评估基础设施的角色。智能体在环境中感知状态、调用工具、修改工作目录、提交任务成果，并由打分程序判定结果给予奖励。然而，这种深度交互性使得评测系统极易遭遇“奖励作弊”攻击：智能体往往会去利用和篡改与奖励判定相关的执行轨迹，而非真正解决目标任务，从而虚增评分。现有防御手段主要依赖特定任务补丁、提示词规则限定或事后检测器，这些方法无法为某次具体运行是否确实遵循了预期评测边界提供可复用的坚实证据。

> LM-agent benchmarks increasingly function as interactive evaluation infrastructure. Agents observe state, call tools, modify workspaces, submit artifacts, and receive rewards from outcome procedures. This interactivity makes evaluations vulnerable to reward hacking: an agent improves its measured score by exploiting the reward-relevant trajectory instead of solving the intended task. Existing defenses rely largely on task-specific patches, prompt instructions, or post-hoc detectors. They do not provide reusable evidence that a concrete run remained within its intended evaluation boundary.

本文提出了 BenchShield，一个专为保障 LLM 智能体评测中奖励完整性而打造的基于形式化模型的插桩防护层。BenchShield 将检测根基扎在评测生命周期内奖励相关事件的有限状态模型上。在基准评测基础设施内部，两项互补的分析技术基于该模型协同运转：其一，静态、阶段感知的污点分析能够在执行前暴露潜在的作弊攻击链；其二，动态运行时分析能够采集基础设施侧的深层证据，对智能体的实体动作进行确切归因，并生成经证据支撑的可信凭证。

> This paper presents BenchShield, a model-backed instrumentation layer for reward integrity in LLM-agent evaluation. BenchShield grounds detection in a finite lifecycle model of an evaluation's reward-relevant events. Within the benchmark infrastructure, two complementary analyses operate over this model. A static, phase-aware taint analysis exposes reward-hacking paths before a run. Its runtime counterpart uses infrastructure-side evidence to attribute concrete agent use and emit evidence-backed claims.

我们基于跨越三大基准的 31,000 多次公开智能体交互轨迹，构建了包含 456 条经人工仲裁标注的 BenchShield Trajectories 基准数据集。在相同任务和模型下与智能体可作弊性扫描器基线相比，BenchShield 将全链路召回率从 23–94% 提高至 77–100% ，将同向量覆盖率从 16–56% 提高至 43–78% ，并将单任务成本大幅削减了高达 65% 。其运行时分析模块仅凭基础设施侧证据，便实现了 96% 的高精度作弊检测率。

> We construct BenchShield Trajectories, a human-labeled corpus of 456 adjudicated trajectories from more than 31,000 public agent runs across three benchmarks. Compared with an agentic hackability scanner baseline on the same tasks and model, BenchShield improves full-chain recall from 23-94% to 77-100%, same-vector coverage from 16-56% to 43-78%, and reduces per-task cost by up to 65%. Its runtime analysis achieves 96% accuracy in detecting reward hacking from infrastructure-side evidence.

---

## 🔗 论文资源与相关链接

> ## 🔗 Links & Resources

* **全文获取通道**：[阅读 PDF 论文](https://arxiv.org/pdf/2609.11028) | [HTML 网页版](https://arxiv.org/html/2609.11028v1) | [TeX 源代码](https://arxiv.org/src/2609.11028)
* **开源许可**：[Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="vertical-align: middle; display: inline-block; margin-left: 4px;" />
* **文献引证与检索**：[Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.11028) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.11028) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.11028)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2609.11028) | [HTML Version](https://arxiv.org/html/2609.11028v1) | [TeX Source](https://arxiv.org/src/2609.11028)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" style="vertical-align: middle; display: inline-block; margin-left: 4px;" />
> * **Citations & Metrics:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.11028) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.11028) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.11028)
