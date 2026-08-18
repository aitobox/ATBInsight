---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 大模型智能体
- 技能演进
- 强化学习
- 知识库
- 行为验证
title: SkillCommit：通过行为验证的范围扩展实现智能体技能演进
---
### 文章背景与核心概要
随着大语言模型（LLM）智能体在复杂任务中的广泛应用，如何让智能体在不更新模型参数的前提下实现持续自主学习和技能演进，成为了当前AI领域的研究热点。传统方法往往依赖于表层的语义相似度或大模型自身的判断，这容易导致行为不相容的策略被错误合并，从而降低智能体的稳定性和泛化能力。

为了解决这一痛点，本文提出了 **SkillCommit** 这一全新的在线技能演进框架。该框架通过“行为验证的范围扩展”机制，将历史经验转化为可复用的分层程序化知识库。其核心流程包括：首先将新经验存储为特定于实例的补丁以保留局部验证的行为；接着通过嵌入检索寻找相关候选技能；然后利用跨实例重放和基于LLM的机制进行严格的行为检查；最后将合格的候选技能抽象为更高层次的技能，并在成功保持所有组成技能已验证行为的前提下进行“提交”（Commit）。

在 *RuleArena*、*OpenExempt* 和 *KOR-Bench* 等多个基准测试上的实验表明，SkillCommit 能够在不同领域持续提升智能体的性能，并有效促进跨模型的经验迁移，为构建自适应、可扩展的智能体系统提供了强有力的技术支撑。

---

# SkillCommit: Evolving Agent Skills through Behaviorally Validated Scope Expansion

> **SkillCommit: Evolving Agent Skills through Behaviorally Validated Scope Expansion**

**Authors:** Yu He, Weikai Yang  
**arXiv:** [arXiv:2608.15165](https://arxiv.org/abs/2608.15165) [cs.AI]  
**Submitted:** August 15, 2026  

> **Authors:** Yu He, Weikai Yang  
> **arXiv:** [arXiv:2608.15165](https://arxiv.org/abs/2608.15165) [cs.AI]  
> **Submitted:** August 15, 2026  

---

## 📌 Summary

> ## 📌 Summary

**SkillCommit** is a novel online skill evolution framework designed to help Large Language Model (LLM) agents continually improve without requiring parameter updates. By transforming historical experiences into a hierarchical library of reusable procedural knowledge, SkillCommit overcomes the limitations of traditional methods (which often rely on superficial semantic similarity or LLM judgments that can merge behaviorally incompatible strategies). 

> **SkillCommit** is a novel online skill evolution framework designed to help Large Language Model (LLM) agents continually improve without requiring parameter updates. By transforming historical experiences into a hierarchical library of reusable procedural knowledge, SkillCommit overcomes the limitations of traditional methods (which often rely on superficial semantic similarity or LLM judgments that can merge behaviorally incompatible strategies). 

The framework operates through **behaviorally validated scope expansion**:
1. **Instance-Specific Patches:** New experiences are initially stored as context-specific patches to retain locally validated behaviors.
2. **Embedding Retrieval:** Incoming skills use embedding-based retrieval to find related candidate skills.
3. **Behavioral Checks:** Cross-instance replay and LLM-based mechanisms ensure that candidates transfer across cases and share a common underlying mechanism.
4. **Abstraction & Commitment:** Qualified candidates are abstracted into higher-level skills and committed only if they successfully preserve the validated behavior of all constituent skills.

> The framework operates through **behaviorally validated scope expansion**:
> 1. **Instance-Specific Patches:** New experiences are initially stored as context-specific patches to retain locally validated behaviors.
> 2. **Embedding Retrieval:** Incoming skills use embedding-based retrieval to find related candidate skills.
> 3. **Behavioral Checks:** Cross-instance replay and LLM-based mechanisms ensure that candidates transfer across cases and share a common underlying mechanism.
> 4. **Abstraction & Commitment:** Qualified candidates are abstracted into higher-level skills and committed only if they successfully preserve the validated behavior of all constituent skills.

Experiments across benchmarks such as *RuleArena*, *OpenExempt*, and *KOR-Bench* demonstrate that SkillCommit consistently boosts agent performance across diverse domains and facilitates cross-model experience transfer.

> Experiments across benchmarks such as *RuleArena*, *OpenExempt*, and *KOR-Bench* demonstrate that SkillCommit consistently boosts agent performance across diverse domains and facilitates cross-model experience transfer.

---

## 🔗 Quick Links & Resources

> ## 🔗 Quick Links & Resources

* **Full-Text Access:**
  * [View PDF](https://arxiv.org/pdf/2608.15165)
  * [HTML Version (Experimental)](https://arxiv.org/html/2608.15165v1)
  * [TeX Source](https://arxiv.org/src/2608.15165)
* **Citations & References:**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.15165)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.15165)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.15165)
* **Metadata:**
  * **DOI:** [10.48550/arXiv.2608.15165](https://doi.org/10.48550/arXiv.2608.15165)
  * **Primary Subject:** Artificial Intelligence (`cs.AI`)

> * **Full-Text Access:**
>   * [View PDF](https://arxiv.org/pdf/2608.15165)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.15165v1)
>   * [TeX Source](https://arxiv.org/src/2608.15165)
> * **Citations & References:**
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.15165)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.15165)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.15165)
> * **Metadata:**
>   * **DOI:** [10.48550/arXiv.2608.15165](https://doi.org/10.48550/arXiv.2608.15165)
>   * **Primary Subject:** Artificial Intelligence (`cs.AI`)