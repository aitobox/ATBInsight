---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 交通模拟
- 终身学习
- AI智能体
- 大语言模型
- SUMO
title: SimSkill：用于自主掌握交通模拟的终身学习AI智能体
---
### 文章背景与核心概要

随着大语言模型（LLM）能力的不断增强，其长期价值日益取决于如何将过往经验和积累的知识转化为持久、可复用的能力，而不仅仅是解决孤立的请求。本文介绍了 **SimSkill**，这是一个围绕城市流动性模拟（SUMO）交通模拟器构建的自进化AI智能体。SimSkill 通过终身学习框架运行：1. **差距识别**：检测交通模拟工作流中的能力差距；2. **任务执行**：生成并解决基于环境的任务；3. **行动-评论循环**：迭代验证解决方案；4. **记忆巩固**：将学到的见解存储到情景、程序和语义记忆中，而无需更新底层的骨干LLM模型。

在两个保留基准（held-out benchmarks）上使用三个骨干LLM并通过独立的基于制品的验证进行评估，SimSkill 将验证通过率**提升了多达25个百分点**。消融实验突出了程序记忆和语义记忆的互补贡献，尽管性能提升仍然取决于具体的骨干模型和Token预算。最终，SimSkill 展示了一种范式：自然语言保留了计算能力，而可执行的工具和代码则确保了精确、可复现的执行。

---

**arXiv:** [arXiv:2609.03753](https://arxiv.org/abs/2609.03753) [cs.AI]  
**Subjects:** 人工智能 (`cs.AI`); 多智能体系统 (`cs.MA`)  
**Authors:** Qi Liu, Qinzheng Wang, Yiming Bie  
**Submitted:** 3 September 2026  
**Links:** [查看 PDF](https://arxiv.org/pdf/2609.03753) | [HTML 版本](https://arxiv.org/html/2609.03753v1) | [GitHub 仓库](https://github.com/qiliuchn/SimSkill-V1)  
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" /> *(许可证: [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/))*

---

## 执行摘要

随着大语言模型（LLM）能力的不断增强，其长期价值日益取决于如何将过往经验和积累的知识转化为持久、可复用的能力，而不仅仅是解决孤立的请求。

> As large language models (LLMs) grow more capable, their long-term value increasingly relies on converting past experience and accumulated knowledge into durable, reusable competence rather than just solving isolated requests.

本文介绍了 **SimSkill**，这是一个围绕城市流动性模拟（SUMO）交通模拟器构建的自进化AI智能体。SimSkill 通过终身学习框架运行：
1. **差距识别：** 检测交通模拟工作流中的能力差距。
2. **任务执行：** 生成并解决基于环境的任务。
3. **行动-评论循环：** 迭代验证解决方案。
4. **记忆巩固：** 将学到的见解存储到情景、程序和语义记忆中，而无需更新底层的骨干LLM模型。

> This paper introduces **SimSkill**, a self-evolving AI agent built around the Simulation of Urban MObility (SUMO) traffic simulator. SimSkill operates through a lifelong learning framework:
> 1. **Gap Identification:** Detects capability gaps in the traffic simulation workflow.
> 2. **Task Execution:** Generates and solves environment-grounded tasks.
> 3. **Action-Critic Loop:** Verifies solutions iteratively.
> 4. **Memory Consolidation:** Stores learned insights into episodic, procedural, and semantic memory without updating the underlying backbone LLM model.

在两个保留基准（held-out benchmarks）上使用三个骨干LLM并通过独立的基于制品的验证进行评估，SimSkill 将验证通过率**提升了多达25个百分点**。消融实验突出了程序记忆和语义记忆的互补贡献，尽管性能提升仍然取决于具体的骨干模型和Token预算。最终，SimSkill 展示了一种范式：自然语言保留了计算能力，而可执行的工具和代码则确保了精确、可复现的执行。

> Evaluated on two held-out benchmarks using three backbone LLMs with independent artifact-based verification, SimSkill improves verified completion rates by **up to 25 percentage points**. Ablation studies highlight the complementary contributions of procedural and semantic memory, though performance gains remain dependent on the specific backbone model and token budget. Ultimately, SimSkill demonstrates a paradigm where natural language preserves computational capabilities while executable tools and code ensure precise, reproducible execution.