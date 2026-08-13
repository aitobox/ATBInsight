---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- HPC
- 智能体工作流
- 代码现代化
- GAMESS
- Fortran
title: 面向遗留HPC现代化的智能体工作流：GAMESS双电子积分核心的转换
---
### 文章背景与核心概要
在计算科学领域，对历史悠久的Fortran代码库进行现代化改造是一项庞大且劳动强度极高的挑战，往往长期遭到搁置。本文介绍了一种专为自动化改造大规模遗留高性能计算（HPC）系统而设计的**智能体工作流（agentic workflow）**。

研究人员成功将**GAMESS**（一个拥有48年历史的量子化学软件包）的双电子积分核心从固定格式的Fortran 77转换为了自由格式的Fortran 2008。通过利用专门的AI智能体角色、版本控制的规范说明以及严格的领域专用验证预言机（verification oracle），该团队在56,448行代码和225个子程序中实现了逐位（bit-for-bit）精确度，且未引入任何与化学计算相关的误差。

---

# 面向遗留HPC现代化的智能体工作流：GAMESS双电子积分核心的转换

**作者：** Yuzhong Shen, Masha Sosonkina, Peng Xu, Mark S. Gordon  
**日期：** 2026年8月12日  
**标识符：** [arXiv:2608.12249](https://arxiv.org/abs/2608.12249) [cs.AI]

---

## 摘要

> Modernizing legacy Fortran codebases is a massive, labor-intensive challenge that often remains unaddressed in computational science. This paper introduces an **agentic workflow** designed to automate the modernization of large-scale legacy High-Performance Computing (HPC) systems. 
> 
> The researchers successfully converted the two-electron-integral core of **GAMESS** (a 48-year-old quantum chemistry package) from fixed-form Fortran 77 to free-form Fortran 2008. By utilizing specialized AI agent roles, version-controlled specifications, and a rigorous domain-specific verification oracle, the team achieved bit-for-bit accuracy across 56,448 lines of code and 225 subroutines without introducing any chemistry-relevant errors.

现代化改造遗留的Fortran代码库是一项巨大且繁重的挑战，在计算科学中往往长期无人问津。本文介绍了一种**智能体工作流（agentic workflow）**，旨在实现大规模遗留高性能计算（HPC）系统现代化改造的自动化。
> 固定格式的 Fortran 77代码通过专用智能体工作流成功转换为自由格式的 Fortran 2008。研究人员成功将 **GAMESS**（一个拥有 48 年历史的量子化学软件包）的双电子积分核心从固定格式的 Fortran 77 转换为了自由格式的 Fortran 2008。通过利用专门的 AI 智能体角色、版本控制的技术规范以及严格的领域特定验证预言机，该团队在 56,448 行代码和 225 个子程序中实现了逐位精确度（bit-for-bit accuracy），且未引入任何与化学相关的错误。

---

## 关键方法论

> *   **Agentic Roles:** The workflow employed three prompt-specialized agent roles operating within isolated worktrees.
> *   **Human-in-the-Loop:** Humans acted as "gates" for critical decisions, while the agents authored and revised their own technical specifications.
> *   **Verification Oracle:** The team leveraged the existing GAMESS standard test suite as a "bit-for-bit" verification oracle. Any deviation in the twelfth decimal place of calculated energies was treated as a failure.
> *   **Scalability:** The project spanned four generations of Claude models, demonstrating the adaptability of the workflow to evolving AI capabilities.

*   **智能体角色：** 该工作流采用了三个在隔离工作树（worktrees）中运行的、具备提示词专长的智能体角色。
*   **人在回路（Human-in-the-Loop）：** 人类充当关键决策的“关卡”，而智能体则负责撰写和修改其自身的技术规范。
*   **验证预言机：** 团队利用现有的 GAMESS 标准测试套件作为“逐位”验证预言机。计算能量在小数点后第十二位的任何偏差都被视为失败。
*   **可扩展性：** 该项目跨越了四代 Claude 模型，展示了该工作流对不断演进的 AI 能力的适应性。

---

## 实验结果

> *   **Scope:** 12 source files, 56,448 lines of code, and 225 subroutines.
> *   **Validation:** All files passed a 51-test battery (49 standard tests + 2 additional calculations).
> *   **Accuracy:** Across 612 test runs, the number of chemistry-relevant differences was **zero**.
> *   **Integration:** Every converted file successfully passed the Jenkins continuous integration tests used by the GAMESS development group.

*   **范围：** 12个源文件，56,448行代码，225个子程序。
*   **验证：** 所有文件均通过了51项测试矩阵（49项标准测试 + 2项附加计算）。
*   **准确性：** 在612次测试运行中，与化学计算相关的差异数量为 **零**。
*   **集成：** 每个转换后的文件都成功通过了 GAMESS 开发小组使用的 Jenkins 持续集成测试。

---

## 获取与资源

> *   **Full-Text PDF:** [View PDF](https://arxiv.org/pdf/2608.12249)
> *   **DOI:** [https://doi.org/10.48550/arXiv.2608.12249](https://doi.org/10.48550/arXiv.2608.12249)
> *   **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)

*   **全文 PDF：** [查看 PDF](https://arxiv.org/pdf/2608.12249)
*   **DOI：** [https://doi.org/10.48550/arXiv.2608.12249](https://doi.org/10.48550/arXiv.2608.12249)
*   **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/)

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">