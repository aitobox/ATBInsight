---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-19
hide:
  - navigation
tags:
  - 形式化验证
  - Lean 4
  - AI 证明智能体
  - 量子复杂性
  - MIP*=RE
title: "FormalFlow：面向 MIP* = RE 核心定理的长程自动化形式化证明"
---

### 文章背景与核心概要

在理论计算机科学与量子物理的交叉领域，著名的 $\text{MIP}^* = \text{RE}$ 定理证明了多证明者量子纠缠交互式证明系统等价于所有递归可枚举语言，从根本上颠覆了人们对可计算性与量子纠缠的认知，其证明过程极其宏大繁琐，传统纯人工的形式化检验几乎需要顶尖专家团队耗费数年心血。为了攻克长程数学证明自动化中的“命题漂移”与“证明拼接”等关键瓶颈，本文研究团队创新性地提出了 **FormalFlow** 系统，巧妙引入现代软件工程开发思想，依托全局共享蓝图引导多个 AI 证明智能体 (AI proving agents) 在人类监督下开展嵌套规划、机器证明与严谨代码审查。借助该系统，团队历时 63 天成功在 Lean 4 中完成了 $\text{MIP}^* = \text{RE}$ 底层核心定理——“经典低单变量度数测试的量子可靠性”的完全形式化，产出超过 12.6 万行完全由 AI 智能体生成的代码，并在验证中精准排查与修复了原论文手写证明中存在的隐蔽缺陷与边界条件。这项突破不仅为深奥的量子复杂性理论构筑了经计算机验证的坚实基石，更生动展示出小规模科研团队借助自主 AI 智能体低成本、高质量验证重大科学猜想与顶尖数学证明的广阔前景。

---

# 面向 MIP* = RE 核心定理的长程自动化形式化证明

> # Long-Horizon Autoformalization of a Core Theorem Underlying MIP* = RE

## 核心概要

> ## Summary

里程碑式的数学形式化验证往往需要顶尖专家团队投入数年心血才能完成。本文提出了 **FormalFlow** 系统，在人类专家的统筹监督下协同多个 AI 证明智能体 (AI proving agents) ，共同攻克长程形式化验证 (long-horizon formalization) 中尤为棘手的命题漂移 (statement drift) 与证明拼接 (proof composition) 等核心挑战。FormalFlow 汲取了现代软件工程的研发思想，依托一份全局共享的蓝图 (shared blueprint) 来引导“规划—证明—评审”的嵌套闭环，并由智能体在全流程中持续强化严格的形式化验证。

> Landmark mathematical formalizations typically require specialist teams years of dedicated work to complete. This paper introduces **FormalFlow**, a system that coordinates AI proving agents under human supervision to overcome key challenges in long-horizon formalization, such as statement drift and proof composition. Inspired by software engineering principles, FormalFlow utilizes a shared blueprint to steer nested planning, proving, and review loops, with agents continuously reinforcing verification. 

借助该系统，作者团队成功完成了经典低单变量度数测试 (classical low individual-degree test) 量子可靠性 (quantum soundness) 在 Lean 4 中的机器检验形式化证明——该定理正是著名的量子计算里程碑成果 $\text{MIP}^* = \text{RE}$ 的底层基石。整个形式化开发历时 63 天完成 (若引入更大规模的并行机制，这一周期还可进一步大幅压缩) ，最终产出的代码库包含 126,367 行完全由智能体自主生成的 Lean 代码。在严苛的机器检验过程中，系统成功识别并修正了原手写论文中存在的附加约束条件漏洞与中间推演谬误，同时在修正后的假设前提下依然完好保持了已发表论文中的最终误差界。这项突破不仅为量子复杂性理论 (quantum complexity theory) 奠定了经计算机完全验证的坚实基石，更展示出了一条极具扩展潜力的全新路径，使小规模科研团队也有能力以极高的性价比对重大前沿研究证明开展严格的形式化验证。

> Using this system, the authors completed a machine-checked Lean 4 proof for the quantum soundness of the classical low individual-degree test—a foundational theorem underlying the celebrated $\text{MIP}^* = \text{RE}$ result. Developed over 63 days (a timeline that could be further compressed through parallelism), the resulting library contains 126,367 lines of entirely agent-generated Lean code. The formalization process successfully identified and corrected side conditions and intermediate errors while maintaining the published final error bound. This achievement establishes a verified foundation for quantum complexity theory and demonstrates a scalable path toward the affordable verification of major research proofs by small teams.

---

## 文档元数据

> ## Document Metadata

* **arXiv 编号：** [arXiv:2609.19814](https://arxiv.org/abs/2609.19814)
* **主学科分类：** 量子物理 (Quantum Physics, `quant-ph`) 
* **次学科分类：** 人工智能 (Artificial Intelligence, `cs.AI`) 、计算机科学中的逻辑 (Logic in Computer Science, `cs.LO`) 
* **MSC 数学分类：** 68V20, 68V15, 81P68, 68Q15
* **提交日期：** 2026 年 9 月 17 日
* **论文作者：** Sirui Lu, Ruixuan Deng, Yanqiao Zhu, Zhengfeng Ji

> * **arXiv ID:** [arXiv:2609.19814](https://arxiv.org/abs/2609.19814)
> * **Primary Subject:** Quantum Physics (`quant-ph`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`), Logic in Computer Science (`cs.LO`)
> * **MSC Classes:** 68V20, 68V15, 81P68, 68Q15
> * **Submission Date:** September 17, 2026
> * **Authors:** Sirui Lu, Ruixuan Deng, Yanqiao Zhu, Zhengfeng Ji

---

## 论文摘要

> ## Abstract

以往，完成里程碑式的数学形式化验证往往需要顶尖专家团队耗费数年时间。我们提出了 FormalFlow 系统，在人类专家的监督下协同多个 AI 证明智能体 (AI proving agents) ，有效解决长程形式化过程中面临的命题漂移与证明拼接两大核心难题。该系统借鉴现代软件工程的原理与实践，利用一份全局共享的蓝图指导规划、证明与评审的嵌套闭环；智能体在整个形式化生命周期中持续强化形式验证与严格审查。基于该系统，我们成功完成了经典低单变量度数测试量子可靠性的机器检验 Lean 4 形式化证明，该定理正是支撑著名成果 $\text{MIP}^* = \text{RE}$ 的核心基石之一。整个证明开发历时 63 天；若借助更高并发度的并行机制，研发周期有望进一步缩短。最终生成的证明代码库包含 126,367 行 Lean 代码，且全部由智能体自主生成。在严格的形式化过程中，系统成功修正了原论文中的附加约束条件与中间推演谬误，同时在修正后的假设下依然完好保持了此前已发表的最终误差界。本项工作不仅为量子复杂性理论建立了经机器全面验证的严谨基石，更展示出了一条切实可行的技术路径，使小规模研究团队也能以低成本实现重大前沿科研证明的形式化验证。

> Landmark mathematical formalizations have taken specialist teams years to complete. We present FormalFlow, a system that coordinates AI proving agents under human supervision to address statement drift and proof composition in long-horizon formalization. Drawing on software engineering principles and practices, it uses a shared blueprint to guide nested planning, proving and review loops. Agents strengthen verification and review throughout formalization. We completed a machine-checked Lean 4 proof of the quantum soundness of the classical low individual-degree test, a core theorem underlying $\text{MIP}^* = \text{RE}$. Developing the proof took 63 days; greater parallelism could further reduce this time. The final library contains 126,367 lines of Lean code, all generated by agents. The formalization corrects side conditions and intermediate errors while preserving the published final error bound under corrected assumptions. This work provides a verified foundation for quantum complexity and demonstrates a route to affordable verification of major research proofs by small teams.

---

## 补充信息与资源

> ## Supplementary Information & Resources

* **论文篇幅：** 全文共 72 页 (正文共 13 页，包含 4 幅图和 1 张表；补充附录共 57 页，包含 9 幅图和 17 张表；以及参考文献) 。
* **Lean 4 代码仓库：** [GitHub - LionSR/MIPStarRE](https://github.com/LionSR/MIPStarRE)
* **获取全文：** 
  * [查看 PDF](https://arxiv.org/pdf/2609.19814)
  * [HTML 在线版本 (实验性) ](https://arxiv.org/html/2609.19814v1)
  * [TeX 源码](https://arxiv.org/src/2609.19814)

> * **Paper Length:** 72 pages total (13-page main text featuring 4 figures and 1 table; 57-page supplementary appendices featuring 9 figures and 17 tables; references).
> * **Lean 4 Code Repository:** [GitHub - LionSR/MIPStarRE](https://github.com/LionSR/MIPStarRE)
> * **Access Full-Text:** 
>   * [View PDF](https://arxiv.org/pdf/2609.19814)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2609.19814v1)
>   * [TeX Source](https://arxiv.org/src/2609.19814)
