---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-21
hide:
- navigation
tags:
- 计算机操作智能体
- ComponentBench
- 基准测试
- UI组件
- 故障诊断
title: ComponentBench：诊断电脑操作智能体的组件级故障
---
### 文章背景与核心概要
当前的电脑操作智能体（Computer-Use Agents）评估方法呈现两极分化状态，主要集中在长周期工作流基准测试和原子级 GUI 接地测试（GUI-grounding tests）之间。**ComponentBench** 正是为了填补这一“缺失的中层（missing middle）”而提出的——它专注于真实、以组件为中心的交互，既具备足够的复杂度以反映现代 UI 的挑战，又足够精简以支持精准的诊断分析。

研究人员开发了一个与框架无关的包含 97 个规范 UI 组件的本体库（ontology），并据此构建了 2,910 个经过程序验证的任务。通过对七个主流模型（包括 GPT-5.4、Gemini 3 和 Qwen3-VL）的评估，该研究表明，观测与动作空间的设计选择可以使任务成功率发生超过 30% 的波动，这凸显了当前智能体在感知和交互数字界面时存在的显著瓶颈。

---

# ComponentBench: Diagnosing Component-Level Failures in Computer-Use Agents

**Authors:** Tianchen Guan, Xinlei Lin, Royce Cheng-Yue, Xiangjun Wang, Shuyan Zhou  
**Published:** August 18, 2026 (Accepted at COLM 2026)  
**arXiv ID:** [2608.18307](https://arxiv.org/abs/2608.18307)

---

## Summary
Current evaluation methods for computer-use agents are polarized between long-horizon workflow benchmarks and atomic GUI-grounding tests. **ComponentBench** addresses the "missing middle"—the need for realistic, component-centered interactions that are complex enough to reflect modern UI challenges but concise enough to allow for precise diagnostic analysis.

The researchers developed a library-agnostic ontology of 97 canonical UI components, resulting in 2,910 programmatically verified tasks. By evaluating seven major models (including GPT-5.4, Gemini 3, and Qwen3-VL), the study reveals that observation and action space design choices can shift task success rates by over 30%, highlighting significant bottlenecks in how current agents perceive and interact with digital interfaces.

> 当前的电脑操作智能体（Computer-Use Agents）评估方法呈现两极分化状态，主要集中在长周期工作流基准测试和原子级 GUI 接地测试（GUI-grounding tests）之间。**ComponentBench** 正是为了填补这一“缺失的中层（missing middle）”而提出的——它专注于真实、以组件为中心的交互，既具备足够的复杂度以反映现代 UI 的挑战，又足够精简以支持精准的诊断分析。
> 
> 研究人员开发了一个与框架无关的包含 97 个规范 UI 组件的本体库（ontology），并据此构建了 2,910 个经过程序验证的任务。通过对七个主流模型（包括 GPT-5.4、Gemini 3 和 Qwen3-VL）的评估，该研究表明，观测与动作空间的设计选择可以使任务成功率发生超过 30% 的波动，这凸显了当前智能体在感知和交互数字界面时存在的显著瓶颈。

---

## Key Features of ComponentBench
*   **Comprehensive Ontology:** 97 canonical UI components across widely used libraries.
*   **Scalable Diagnostic Pipeline:** Enables auditing of structural difficulty and synthesis of failure analyses across different component families.
*   **Human-Centric Benchmarking:** Includes cleaned human reference trajectories to evaluate both task success and interaction efficiency.
*   **Performance Insights:** Demonstrates that even the most advanced models take 3.7x longer than humans to complete tasks, with spatial manipulation remaining a persistent challenge.

> ## ComponentBench 的核心特性
> *   **全面的本体库：** 涵盖主流UI库中的 97 个规范 UI 组件。
> *   **可扩展的诊断流水线：** 能够审查结构难度，并综合分析不同组件系列的故障。
> *   **以人为本的基准测试：** 包含清洗过的人类参考轨迹，用于评估任务成功率和交互效率。
> *   **性能洞察：** 表明即使是最先进的模型，完成任务所需的时间也是人类的 3.7 倍，空间操作仍然是一个长期的挑战。

---

## Model Performance & Observations
The study evaluated seven models across four distinct observation and action spaces. A critical finding is the sensitivity of model performance to input representation:
*   **GPT-5 mini:** Achieved **83.1%** success using accessibility-tree observations, which plummeted to **48.9%** when restricted to coordinate-only pixel control.
*   **Efficiency Gap:** Even the most optimized configurations significantly lag behind human performance, requiring nearly 4x the time to complete identical tasks.

> ## 模型性能与观察
> 该研究在四种不同的观测和动作空间下评估了七个模型。一个关键发现是模型性能对输入表示形式高度敏感：
> *   **GPT-5 mini：** 在使用无障碍树（accessibility-tree）观测时取得了 **83.1%** 的成功率，而当受限于纯坐标像素控制时，成功率骤降至 **48.9%**。
> *   **效率差距：** 即使是最优化的配置，也明显落后于人类表现，完成相同任务所需的时间接近人类的 4 倍。

---

## Resources
*   **Website:** [componentbench.com](https://componentbench.com)
*   **Code:** [GitHub Repository](https://github.com/TianchenGuan/ComponentBench)
*   **Data:** [Hugging Face Dataset](https://huggingface.co/datasets/TianchenGuan/ComponentBench)

> ## 相关资源
> *   **官方网站：** [componentbench.com](https://componentbench.com)
> *   **代码仓库：** [GitHub Repository](https://github.com/TianchenGuan/ComponentBench)
> *   **数据集：** [Hugging Face Dataset](https://huggingface.co/datasets/TianchenGuan/ComponentBench)

---

## Metadata
*   **Subjects:** Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Human-Computer Interaction (cs.HC)
*   **DOI:** [10.48550/arXiv.2608.18307](https://doi.org/10.48550/arXiv.2608.18307)
*   **Format:** 30 pages (10 pages main text), 10 figures, 15 tables.

> ## 元数据
> *   **学科分类：** 人工智能 (cs.AI)；计算与语言 (cs.CL)；人机交互 (cs.HC)
> *   **DOI：** [10.48550/arXiv.2608.18307](https://doi.org/10.48550/arXiv.2608.18307)
> *   **篇幅格式：** 30 页（10 页正文），10 张图表，15 个表格。