---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- 金融机器学习
- 对抗鲁棒性
- FraudBench
- 模型评估
- 风险管理
title: FraudBench：金融风险评估中对抗鲁棒性的协议敏感型基准测试
---
### 文章背景与核心概要

FraudBench 是一个专门为解决金融机器学习模型在对抗鲁棒性评估中面临的独特挑战而设计的基准测试框架。研究指出，金融场景下的模型鲁棒性并非单纯的模型属性，而是与“评估协议”深度耦合。

该研究强调，传统的事后可行性检查（post-hoc feasibility checks）往往无法捕捉模型真实的脆弱性。通过对比无约束攻击、事后过滤以及部署感知约束集成攻击，研究揭示了评估协议的选择会显著改变模型的性能排名。作者主张，未来的研究应将领域约束直接集成到攻击生成过程中，并同时报告预测性能下降情况与攻击可行性。

---

## FraudBench：金融风险评估中对抗鲁棒性的协议敏感型基准测试

**作者：** Xitong Zeng, Zhaoge Bi, Yitian Yang, Huaming Chen, Quan Z. Sheng  
**日期：** 2026年8月25日  
**主题：** 机器学习 (cs.LG); 人工智能 (cs.AI)  
**arXiv ID:** [2608.24551](https://arxiv.org/abs/2608.24551)

---

## 摘要

> *FraudBench* is a novel benchmarking framework designed to address the unique challenges of evaluating adversarial robustness in financial machine learning models. The authors demonstrate that robustness in financial contexts is not merely a model property but is deeply tied to the **evaluation protocol**. 
>
> The research highlights that traditional post-hoc feasibility checks often fail to capture the true vulnerability of models. By comparing unconstrained attacks, post-hoc filtering, and deployment-aware constraint-integrated attacks, the study reveals that protocol choices can significantly alter model performance rankings. The authors advocate for a shift toward integrating domain constraints directly into the attack generation process and reporting both predictive degradation and attack feasibility.

---

## 关键发现

> *   **Protocol Sensitivity:** Robustness conclusions are highly sensitive to the evaluation protocol. For instance, on the *Lending Club* dataset, post-hoc filtering identified only 3.7 feasible-flipped examples, whereas in-attack projection identified 2,832.3 under the same budget.
> *   **Feasibility vs. Capability:** The study establishes that feasibility and attacker capability are distinct axes in adversarial evaluation.
> *   **Model Rankings:** The choice of evaluation protocol can fundamentally change the perceived ranking of different model families (neural, tree-based, and ensemble).
> *   **Methodological Recommendation:** The authors propose that future robustness evaluations in finance should:
>     1.  Report predictive degradation and attack feasibility jointly.
>     2.  Incorporate domain constraints into the attack generation phase rather than using them as post-processing filters.

---

## 访问与资源

> *   **[View PDF](https://arxiv.org/pdf/2608.24551)**
> *   **[HTML (Experimental)](https://arxiv.org/html/2608.24551v1)**
> *   **[TeX Source](https://arxiv.org/src/2608.24551)**
> *   **DOI:** [https://doi.org/10.48550/arXiv.2608.24551](https://doi.org/10.48550/arXiv.2608.24551)

---

## 提交历史

> *   **[v1]** Tue, 25 Aug 2026 13:36:42 UTC