---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-08
hide:
- navigation
tags:
- Text-to-SQL
- 自我博弈
- 大语言模型
- GRPO
- 强化学习
title: SQL-Zero：自我进化的 Text-to-SQL
---
### 文章背景与核心概要

传统的 Text-to-SQL 智能体训练严重依赖昂贵且特定领域的、由人工标注的自然语言与 SQL 配对数据，这在扩展到新数据库时构成了巨大的瓶颈。

**SQL-Zero** 表明，完全可以通过**零标注配对数据**来训练具有竞争力的 SQL 求解器。通过利用新颖的**“出题者-求解者”自我博弈框架**（proposer-solver self-play framework），挑战者和求解者均从同一个基础大语言模型（LLM）出发实现共同进化。真实标签（Ground truth）完全通过针对数据库本身的执行结果来确立。

---

## SQL-Zero: Self-Evolving Text-to-SQL

**arXiv:** [2609.04697 [cs.AI]]  
**Submitted:** September 4, 2026  
**Authors:** Daniel Machado Pedrozo, Julia Soares Dollis, Bryan Lincoln Marques de Oliveira, Vinicius Alboneti Aguiar, Sávio Salvarino Teles de Oliveira, Telma Woerle de Lima Soares  
**Full-Text Links:** [View PDF](https://arxiv.org/pdf/2609.04697) | [HTML Version](https://arxiv.org/html/2609.04697v1) | [TeX Source](https://arxiv.org/src/2609.04697)

---

### 执行摘要

> Training competitive Text-to-SQL agents traditionally relies heavily on expensive, domain-specific, human-annotated natural-language and SQL pairs, creating a significant bottleneck when scaling to new databases. 

> **SQL-Zero** demonstrates that a competitive solver can be trained with **zero annotated pairs**. By utilizing a novel **proposer-solver self-play framework**, both a challenger and a solver evolve starting from the same base Large Language Model (LLM). Ground truth is established purely through execution against the database itself.

---

## 核心方法论

> ## Key Methodology

* **出题者-求解者自我博弈：** 挑战者动态生成与求解者当前难度水平相匹配的 SQL 对（专门针对“困难但可解”的查询）。
  > * **Proposer-Solver Self-Play:** The challenger generates SQL pairs dynamically calibrated to the solver's current difficulty level (specifically targeting "hard but solvable" queries).
* **交替更新：** 两个角色通过 **GRPO**（群组相对策略优化，Group Relative Policy Optimization）进行交替迭代更新。
  > * **Alternating Updates:** Both roles are updated iteratively using **GRPO** (Group Relative Policy Optimization) in alternating turns.
* **多样性保障机制：** 对挑战者应用模板级的重复惩罚，以防止生成过程中出现多样性崩溃。
  > * **Diversity Safeguards:** A template-level repetition penalty is applied to the challenger to prevent diversity collapse during generation.

---

## 结果与性能

> ## Results & Performance

* **BIRD 数据库性能提升（零标注）：** 在 BIRD 开发集上，自我博弈训练使零样本（zero-shot）基础模型的性能在 **3B 参数量下提升了 6.6 个百分点**，在 **7B 参数量下提升了 7.3 个百分点**。
  > * **BIRD Database Improvements (Zero-Labels):** Self-play training improves performance over the zero-shot base model on the BIRD development set by **6.6 points at 3B parameters** and **7.3 points at 7B parameters**.
* **与人类标注黄金标准（Gold Standards）的对比：** SQL-Zero 的得分高于使用完全相同的配方在相同数据库的人类 BIRD 黄金数据上训练的对照组（尽管精确的配对测试并未明确解决该差距）。
  > * **Comparison to Human-Annotated Gold Standards:** SQL-Zero scores higher than a matched control trained using the exact same recipe on human BIRD gold data across the same databases (though an exact paired test does not definitively resolve that margin).
* **跨数据库泛化能力：** 迁移能力在很大程度上取决于模型规模：
  > * **Cross-Database Transfer:** Transfer capabilities depend heavily on model scale:
  * **在 3B 规模下：** 每次迭代在未见过的 Spider 数据库上以及词汇扰动（Spider-Syn）下均优于基础模型，其性能退化幅度小于 BIRD-gold 对照组。
    > * **At 3B:** Every iteration outperforms the base model on unseen Spider databases and under lexical perturbation (Spider-Syn), degrading less than the matched BIRD-gold control.
  * **在 7B 规模下：** 仅有第一次迭代成功保持了迁移性能。
    > * **At 7B:** Only the first iteration successfully preserves transfer performance.

---

## 附加信息

> ## Additional Information

* **主要学科：** 人工智能 (`cs.AI`)
  > * **Primary Subject:** Artificial Intelligence (`cs.AI`)
* **许可协议：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/)
  > * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)
* **许可图标：** <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/> [查看协议](http://creativecommons.org/licenses/by/4.0/)
  > * **License Icon:** <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"/> [view license](http://creativecommons.org/licenses/by/4.0/)