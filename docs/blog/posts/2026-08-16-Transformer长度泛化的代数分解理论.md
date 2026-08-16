---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-16
hide:
- navigation
tags:
- Transformer
- 长度泛化
- 代数理论
- 形式语言学
- Krohn-Rhodes分解
title: Transformer长度泛化的代数分解理论
---
### 文章背景与核心概要
尽管基于Transformer的语言模型展现出了向超出其训练分布的序列长度进行泛化的能力，但这一能力的理论边界目前仍未被充分理解。本文首次对Transformer能够实现长度泛化的正则语言进行了完整刻画。

作者引入了一种多项式时间的判定算法，用于确定某个正则语言是否属于此类。通过将经典的Krohn-Rhodes分解理论（作者证明该理论本身不足以解决此问题）推广至整数的无限加法群，他们建立了一个全新的代数框架。该框架通过迭代交织积（iterated wreath products）对被称为 **C-RASP** 的形式体系进行了表征，为理解Transformer的行为提供了比以往更精确的模型。

---

# Algebraic Decomposition Theory for Transformer Length Generalization

**arXiv:** [2608.13433](https://arxiv.org/abs/2608.13433)  
**Date:** August 13, 2026  
**Subjects:** Formal Languages and Automata Theory (cs.FL); Artificial Intelligence (cs.AI)

> # Algebraic Decomposition Theory for Transformer Length Generalization
> 
> **arXiv:** [2608.13433](https://arxiv.org/abs/2608.13433)  
> **Date:** August 13, 2026  
> **Subjects:** Formal Languages and Automata Theory (cs.FL); Artificial Intelligence (cs.AI)

---

## Summary

尽管基于Transformer的语言模型展现出了向超出其训练分布的序列长度进行泛化的能力，但这一能力的理论边界目前仍未被充分理解。本文首次对Transformer能够实现长度泛化的正则语言进行了完整刻画。

作者引入了一种多项式时间的判定算法，用于确定某个正则语言是否属于此类。通过将经典的Krohn-Rhodes分解理论（作者证明该理论本身不足以解决此问题）推广至整数的无限加法群，他们建立了一个全新的代数框架。该框架通过迭代交织积对被称为 **C-RASP** 的形式体系进行了表征，为理解Transformer的行为提供了比以往更精确的模型。

> ## Summary
> While Transformer-based language models demonstrate an ability to generalize to sequence lengths beyond their training distribution, the theoretical boundaries of this capability remain poorly understood. This paper provides the first complete characterization of the regular languages on which Transformers can achieve length generalization. 
> 
> The authors introduce a polynomial-time decision algorithm for determining if a regular language falls within this class. By extending classical Krohn-Rhodes decomposition theory—which the authors prove is insufficient for this problem—to the infinite additive group of integers, they establish a new algebraic framework. This framework characterizes the formalism known as **C-RASP** through iterated wreath products, offering a more precise model of Transformer behavior than previously available.

---

## Key Contributions

### 1. 形式化刻画
本项研究确立了对允许Transformer模型进行长度泛化的正则语言的明确分类。这解决了在理解Transformer架构计算极限方面的一个基础性空白。

> ### 1. Formal Characterization
> The research establishes a definitive classification of regular languages that admit length generalization in Transformer models. This addresses a foundational gap in understanding the computational limits of the Transformer architecture.

### 2. 算法判定程序
基于语言的句法么半群（syntactic monoid）的大小，作者提供了一个可证明的、用于判定这些语言成员资格的多项式时间算法。

> ### 2. Algorithmic Decision Procedure
> The authors provide a provable, polynomial-time algorithm to determine membership for these languages, based on the size of the language's syntactic monoid.

### 3. 代数创新
该研究指出了经典工具（Krohn-Rhodes分解）为何无法捕捉C-RASP行为的原因：
*   **经典理论的局限性：** 触发器（flip-flops）和简单群等基本构建块无法在C-RASP中表达。
*   **无界计数的作用：** C-RASP的核心机制——无界计数——无法被有限半群所捕获。
*   **新框架：** 通过将分解理论推广到整数的无限加法群，作者成功通过迭代交织积对C-RASP进行了表征。

> ### 3. Algebraic Innovation
> The study identifies why classical tools (Krohn-Rhodes decomposition) fail to capture the behavior of C-RASP:
> *   **Limitations of Classical Theory:** Basic building blocks like flip-flops and simple groups are not expressible in C-RASP.
> *   **The Role of Unbounded Counting:** The core mechanism of C-RASP—unbounded counting—is not captured by finite semigroups.
> *   **New Framework:** By generalizing decomposition theory to the infinite additive group of integers, the authors successfully characterize C-RASP via iterated wreath products.

### 4. 实证验证
理论发现在广泛的正则语言套件上得到了测试，证明了这种新的代数方法比现有的分类方法能更准确地捕捉Transformer的长度泛化行为。

> ### 4. Empirical Validation
> The theoretical findings were tested against a broad suite of regular languages, demonstrating that this new algebraic approach captures the length-generalization behavior of Transformers more accurately than existing classification methods.

---

## Authors
*   **Andy Yang**
*   **Blerta Veseli**
*   **Corentin Barloy**
*   **Michaël Cadilhac**
*   **Andreas Krebs**
*   **Charles Paperman**
*   **Howard Straubing**
*   **Michael Hahn**

> ## Authors
> *   **Andy Yang**
> *   **Blerta Veseli**
> *   **Corentin Barloy**
> *   **Michaël Cadilhac**
> *   **Andreas Krebs**
> *   **Charles Paperman**
> *   **Howard Straubing**
> *   **Michael Hahn**

---

## Accessing the Paper
*   [查看 PDF](https://arxiv.org/pdf/2608.13433)
*   [HTML (实验性)](https://arxiv.org/html/2608.13433v1)
*   [TeX 源码](https://arxiv.org/src/2608.13433)

> ## Accessing the Paper
> *   [View PDF](https://arxiv.org/pdf/2608.13433)
> *   [HTML (Experimental)](https://arxiv.org/html/2608.13433v1)
> *   [TeX Source](https://arxiv.org/src/2608.13433)