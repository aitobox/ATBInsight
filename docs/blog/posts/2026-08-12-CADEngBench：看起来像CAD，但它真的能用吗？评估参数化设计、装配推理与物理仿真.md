---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-12
hide:
- navigation
tags:
- CAD
- 评测基准
- 多模态模型
- 物理仿真
- 参数化设计
title: CADEngBench：看起来像CAD，但它真的能用吗？评估参数化设计、装配推理与物理仿真
---
### 文章背景与核心概要

计算机辅助设计（CAD）模型不能仅仅因为视觉上看起来正确就被视为工程级模型。现实世界中的CAD模型必须满足严格的设计规范、对参数修改做出可预测的响应、支持受控编辑、在物理载荷下表现正常，并通过有效的机械接头与其他组件无缝连接。为了弥补现有评估方法的局限性，本文作者引入了 **CADEngBench**，这是一个全面的双赛道基准测试，旨在评估先进的CAD能力。

该基准测试包含评估参数化设计的 CADEngBench-P 以及评估装配推理的 CADEngBench-A。通过对多模态和代码能力模型的测试，研究发现：当前的AI模型进行模型编辑比从头生成要容易得多，但在复杂结构编辑和匹配有限元分析（FEA）方面仍然极其困难，且在装配预测时经常无法准确恢复精确的关节或配合实体。*CADEngBench* 强调，AI在计算机辅助设计领域的评估必须从测试表面的视觉外观，转向严格测试其功能性的工程行为。

---

# CADEngBench: It Looks Like CAD, but Does It Work? Evaluating Parametric Design, Assembly Reasoning, and Physics Simulation

**Authors:** Harmanjot Singh, Abhra Dubey, Jorge Alejandro Amador Herrera  
**Published:** August 10, 2026  
**Primary Subject:** Artificial Intelligence (`cs.AI`)  
**arXiv ID:** [2608.09296](https://arxiv.org/abs/2608.09296) [cs.AI]  

---

## 📋 摘要 (Summary)

计算机辅助设计（CAD）模型不能仅仅因为视觉上看起来正确就被视为工程级模型。现实世界中的CAD模型必须满足严格的设计规范、对参数修改做出可预测的响应、支持受控编辑、在物理载荷下表现正常，并通过有效的机械接头与其他组件无缝连接。

> A computer-aided design (CAD) model cannot be considered engineering-grade merely because it appears visually correct. Real-world CAD models must satisfy strict design specifications, respond predictably to parameter modifications, support controlled editing, behave properly under physical loads, and connect seamlessly to other components through valid mechanical joints. 

为了解决现有评估方法的局限性，作者推出了 **CADEngBench**，这是一个全面的双赛道基准，旨在评估先进的CAD能力：
* **CADEngBench-P（参数化设计）：** 通过边界表示（B-Rep）有效性、工程和可制造性设计（DFM）检查、参数族扰动、功能编辑以及使用 CalculiX 的匹配线性静态有限元分析（FEA），评估 300 个参数化零件（总共 600 个任务：每个零件一个从零到CAD的任务和一个功能编辑任务）。
* **CADEngBench-A（装配推理）：** 使用排序关节检索、精确的面与边定位、关节坐标系预测和运动学验证来评估 150 对实体。

> To address the limitations of existing evaluation methods, the authors introduce **CADEngBench**, a comprehensive two-track benchmark designed to assess advanced CAD capabilities:
> * **CADEngBench-P (Parametric Design):** Evaluates 300 parametric parts (600 tasks total: one zero-to-CAD task and one functional-editing task per part) through boundary-representation (B-Rep) validity, engineering and Design for Manufacturability (DFM) checks, parameter-family perturbations, functional editing, and matched linear-static Finite Element Analysis (FEA) using CalculiX.
> * **CADEngBench-A (Assembly Reasoning):** Evaluates 150 body pairs using ranked joint retrieval, exact face-and-edge grounding, joint-frame prediction, and kinematic verification.

### 多模态与代码能力模型的主要发现：
1. **编辑与生成的对比：** 对于当前的模型来说，修改和编辑提供的CAD模型比从头生成要容易得多。
2. **复杂编辑与物理学：** 复杂的结构编辑和匹配的FEA仍然极其困难。
3. **装配局限性：** 装配预测经常能隔离出零件的正确大致区域，但始终无法准确恢复精确记录的关节或配合实体。

归根结底，*CADEngBench* 突显出，人工智能在计算机辅助设计（CAD）领域的评估必须从测试表面的视觉外观转变为严格测试其功能性的工程行为。

> ### Key Findings Across Multimodal & Code-Capable Models:
> 1. **Editing vs. Generation:** Modifying and editing supplied CAD models is significantly easier for current models than generating them from scratch.
> 2. **Complex Edits & Physics:** Complex structural edits and matched FEA remain exceptionally difficult.
> 3. **Assembly Limitations:** Assembly predictions frequently isolate the correct general region of a part, but consistently fail to accurately recover the precise recorded joint or mating entities.
> 
> Ultimately, *CADEngBench* highlights that AI evaluation for computer-aided design must transition from testing superficial visual appearance to rigorously testing functional engineering behavior.

---

## 🔗 快速链接 (Quick Links)

* [查看 PDF (View PDF)](https://arxiv.org/pdf/2608.09296)
* [TeX 源码 (TeX Source)](https://arxiv.org/src/2608.09296)
* [DOI 参考 (DOI Reference)](https://doi.org/10.48550/arXiv.2608.09296)

> ## 🔗 Quick Links
> 
> * [View PDF](https://arxiv.org/pdf/2608.09296)
> * [TeX Source](https://arxiv.org/src/2608.09296)
> * [DOI Reference](https://doi.org/10.48550/arXiv.2608.09296)