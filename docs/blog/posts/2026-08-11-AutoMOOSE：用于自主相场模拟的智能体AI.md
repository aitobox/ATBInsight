---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-11
hide:
- navigation
tags:
- 人工智能
- 相场模拟
- MOOSE
- 多智能体系统
- 材料科学
title: AutoMOOSE：用于自主相场模拟的智能体AI
---
### 文章背景与核心概要
相场模拟是现代材料科学中研究微观结构演化（如晶粒生长和旋节分解）的核心计算方法，但其涉及的复杂计算工作流、输入文件构建以及参数校准通常需要极高的专业门槛。为了突破这一瓶颈，由 Sukriti Manna 等人提出的 AutoMOOSE 框架应运而生。它是首个专为 MOOSE 多物理场计算环境设计的开源多智能体系统，能够将自然语言规范转化为完整的自主相场模拟生命周期。

该技术的核心在于由六个专业智能体组成的协作团队（包括架构师、输入编写器、运行器、审查员、可视化专家以及具备物理基础的“怀疑论者”）。通过这种独特的智能体编排与对抗性验证机制，AutoMOOSE 不仅能够自动化完成代码生成与计算，还能严格确保模拟结果符合物理守恒定律、标度关系及渐进极限。研究表明，该系统在铜晶粒生长和铁铬旋节分解等经典任务中展现出了极高的准确性与鲁棒性，为材料科学自动化计算开辟了新的道路。

---

# AutoMOOSE: An Agentic AI for Autonomous Phase-Field Simulation

**Authors:** Sukriti Manna, Henry Chan, Subramanian K.R.S. Sankaranarayanan  
**arXiv:** [2603.20986](https://arxiv.org/abs/2603.20986) [cs.AI]  
**Submitted:** March 22, 2026 (Last revised: August 7, 2026)

> **Authors:** Sukriti Manna, Henry Chan, Subramanian K.R.S. Sankaranarayanan  
> **arXiv:** [2603.20986](https://arxiv.org/abs/2603.20986) [cs.AI]  
> **Submitted:** March 22, 2026 (Last revised: August 7, 2026)

---

## Summary
**AutoMOOSE** 是一个创新的开源多智能体框架，旨在自动化 MOOSE 多物理场环境中相场模拟的整个生命周期。通过弥合自然语言规范与复杂计算工作流之间的鸿沟，AutoMOOSE 消除了手动输入构建、计算任务管理和结果验证的需求。该系统利用由六个专业智能体组成的团队——**架构师（Architect）、输入编写器（Input Writer）、运行器（Runner）、审查员（Reviewer）、可视化专家（Visualization）以及具物理基础的怀疑论者（Skeptic）**——来确保模拟不仅得以执行，还能针对守恒定律、标度关系和渐进极限进行严格验证。

> **Summary**
> **AutoMOOSE** is an innovative, open-source multi-agent framework designed to automate the entire lifecycle of phase-field simulations within the MOOSE multiphysics environment. By bridging the gap between natural-language specifications and complex computational workflows, AutoMOOSE eliminates the need for manual input construction, campaign management, and result validation. The system utilizes a specialized team of six agents—**Architect, Input Writer, Runner, Reviewer, Visualization, and a physics-grounded Skeptic**—to ensure that simulations are not only executed but also rigorously validated against conservation laws, scaling relations, and asymptotic limits.

---

## Key Features & Methodology
*   **智能体编排：** 该框架通过单个自然语言提示词管理模拟生命周期，处理从初始设置到对抗性测试的一切事务。
*   **物理基础验证：** “怀疑论者”智能体执行对抗性测试，以确保结果遵守物理约束（如守恒定律和热力学稳定性）。
*   **领域通用性：** 已在两个主要领域得到验证：
    *   **非守恒型：** 铜晶粒生长（Allen-Cahn 动力学）。
    *   **守恒型：** Fe-Cr 旋节分解（Cahn-Hilliard 动力学）。
*   **性能表现：** 在 25 项任务的晶粒生长基准测试中，AutoMOOSE 成功为所有任务生成了有效的输入，其中 15 个结果满足严格的动力学标准（$R^2 \geq 0.90$）并通过了“怀疑论者”的证伪测试。
*   **可靠性：** 该流程将随机生成转化为一致且可复现的结果，通过对照消融实验证明，与原始生成相比，其成功率显著提高。

> **Key Features & Methodology**
> *   **Agentic Orchestration:** The framework manages the simulation lifecycle from a single natural-language prompt, handling everything from initial setup to adversarial testing.
> *   **Physics-Grounded Validation:** The "Skeptic" agent performs adversarial testing to ensure results adhere to physical constraints, such as conservation laws and thermodynamic stability.
> *   **Domain Versatility:** Validated across two primary domains:
>     *   **Non-conserved:** Copper grain growth (Allen-Cahn dynamics).
>     *   **Conserved:** Fe-Cr spinodal decomposition (Cahn-Hilliard dynamics).
> *   **Performance:** In a 25-task grain-growth benchmark, AutoMOOSE successfully generated valid inputs for all tasks, with 15 results meeting strict kinetic criteria ($R^2 \geq 0.90$) and passing Skeptic falsification.
> *   **Reliability:** The pipeline transforms stochastic generation into consistent, reproducible results, with controlled ablations demonstrating a significant increase in success rates compared to raw generation.

---

## Access & Resources
*   **[查看 PDF (View PDF)](https://arxiv.org/pdf/2603.20986)**
*   **[HTML 页面（实验性）(HTML (Experimental))](https://arxiv.org/html/2603.20986v2)**
*   **[TeX 源码 (TeX Source)](https://arxiv.org/src/2603.20986)**

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> **Access & Resources**
> *   **[View PDF](https://arxiv.org/pdf/2603.20986)**
> *   **[HTML (Experimental)](https://arxiv.org/html/2603.20986v2)**
> *   **[TeX Source](https://arxiv.org/src/2603.20986)**
> 
> <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## Citation
如果您使用了本工作，请通过 [arXiv DOI](https://doi.org/10.48550/arXiv.2603.20986) 进行引用。

> **Citation**
> If you use this work, please cite it via the [arXiv DOI](https://doi.org/10.48550/arXiv.2603.20986).