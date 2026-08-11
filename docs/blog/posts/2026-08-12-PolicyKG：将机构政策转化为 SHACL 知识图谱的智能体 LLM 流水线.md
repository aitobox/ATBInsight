---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-12
hide:
- navigation
tags:
- LLM
- SHACL
- 知识图谱
- 合规性
- 智能体
title: PolicyKG：将机构政策转化为 SHACL 知识图谱的智能体 LLM 流水线
---
### 文章背景与核心概要

机构政策通常以自然语言编写，这为需要机器可读约束的自动化合规系统造成了巨大的障碍。PolicyKG 通过提供一种智能体大语言模型（LLM）流水线，将政策文档转换为 SHACL（形状约束语言）知识图谱，从而有效解决了这一“合规鸿沟”。

该系统利用 LangGraph 状态机进行分阶段验证，以处理政策 PDF 文档。其核心创新在于“语料库适配器”（Corpus Adapter），这是一个基于 YAML 的词汇注册表，允许系统通过更换注册表而非重新训练模型，即可快速迁移至新的领域（例如从机构政策迁移到 GDPR）。

---

## 核心功能与方法论

### 四阶段流水线
该系统将句子分类为义务、许可或禁止，将其提升为一阶道义逻辑（First-order Deontic Logic），并最终生成 SHACL 约束。

> **Four-Stage Pipeline:** The system classifies sentences as obligations, permissions, or prohibitions, lifts them into first-order deontic logic, and emits SHACL constraints.

### 领域无关性
通过利用模块化的语料库适配器，该系统在切换领域时无需重新训练模型。

> **Domain Agnostic:** By utilizing a modular Corpus Adapter, the system avoids the need for model retraining when switching domains.

### 稳健的验证机制
流水线在每个阶段都集成了自动化验证器，以确保输出的高质量和一致性。

> **Robust Validation:** The pipeline incorporates automated validators at each stage to ensure high-quality output and consistency.

### 确定性输出
该系统旨在确保在多次重复运行中产生哈希值完全一致的 SHACL 输出。

> **Deterministic Output:** The system is designed to produce hash-identical SHACL outputs across repeated runs.

---

## 性能亮点

*   **道义分类：** 在亚洲理工学院（AIT）政策语料库上实现了 86.9% 的准确率（Cohen's kappa = .709）。
*   **SHACL 生成：** 在 69 个形状的子集上表现出 .866 的 F1 分数。
*   **逻辑处理：** 通过一阶逻辑（FOL）路径成功处理了 79.2% 的规则，其余部分则采用回退机制。
*   **适应性：** 将 AIT 注册表更换为 GDPR 注册表后，属性对齐能力显著提升（Fisher 精确检验 p < .001）。

> **Performance Highlights**
> *   **Deontic Classification:** Achieved 86.9% accuracy (Cohen's kappa = .709) on the Asian Institute of Technology (AIT) policy corpus.
> *   **SHACL Generation:** Demonstrated an F1 score of .866 on a 69-shape subset.
> *   **Logic Handling:** Successfully processed 79.2% of rules via the first-order logic (FOL) path, with a fallback mechanism for the remainder.
> *   **Adaptability:** Swapping the AIT registry for a GDPR registry significantly improved property alignment (Fisher's exact p < .001).

---

## 访问与资源

*   **[查看 PDF](https://arxiv.org/pdf/2608.09028)**
*   **[HTML (实验版)](https://arxiv.org/html/2608.09028v1)**
*   **[TeX 源码](https://arxiv.org/src/2608.09028)**

*正在接受 IJCKG 2026（泰国曼谷）审稿。*

> **Access & Resources**
> *   **[View PDF](https://arxiv.org/pdf/2608.09028)**
> *   **[HTML (Experimental)](https://arxiv.org/html/2608.09028v1)**
> *   **[TeX Source](https://arxiv.org/src/2608.09028)**
>
> *Under review at IJCKG 2026, Bangkok, Thailand.*