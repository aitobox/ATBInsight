---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-16
hide:
- navigation
tags:
- 知识图谱
- 本体推理
- 神经符号学习
- OWL 2 EL
- 形式化验证
title: Moose：$mathcal{EL}^{++}$ 中具备推理捷径感知能力的潜在概念学习
---
### 文章背景与核心概要
OWL 2 EL 描述逻辑配置文件支撑了许多最大的生产级本体，例如基因本体（Gene Ontology）和 SNOMED CT。虽然现有的神经符号（NeSy）学习方法主要接受命题理论或 Datalog，但在本体设置中，推理捷径（Reasoning-Shortcut, RS）感知此前一直未得到研究。

本文介绍了 **Moose**，这是一种将 $\mathcal{EL}^{++}$ TBox（术语盒）和有限 ABox（断言盒）编译为句法决策图（Sentential Decision Diagram, SDD）的新方法。通过作为可微分的加权模型计数层——并在声明的穷举族上补充超出 $\mathcal{EL}^{++}$ 配置文件的闭包子句——Moose 克服了 $\mathcal{EL}^{++}$ 在部分监督下面临的表达能力受限问题。作者证明了该方法的终止性、可靠性、完备性以及多项式中间大小，并在 Lean 中验证了所有证明。此外，他们定义了 OWL EL 本体上的首个形式化部分监督潜在概念学习任务，并在 MNIST-with-ontology 和 Pizzaïolo 基准测试上对 Moose 进行了评估，证明其显著优于命题-神经符号、模糊逻辑和本体嵌入基线方法。

---

## 摘要 (Abstract)

> The OWL 2 EL profile is used in some of the largest production ontologies, including the Gene Ontology and SNOMED CT. Existing neuro-symbolic (NeSy) learning methods accept propositional theories or Datalog, and reasoning-shortcut (RS) awareness has not been investigated in ontology settings. We present Moose, a method that compiles an $\mathcal{EL}^{++}$ TBox and finite ABox to a Sentential Decision Diagram (SDD). The SDD acts as a differentiable weighted-model-counting layer, and we add closure clauses outside the $\mathcal{EL}^{++}$ profile on declared exhaustive families to overcome the limited expressivity of $\mathcal{EL}^{++}$ under partial supervision. We show termination, soundness, completeness, and polynomial intermediate sizes, and validate the proofs in Lean. We then define the first formal partial-supervision latent-concept-learning task over an OWL EL ontology, i.e., learning per-individual classifiers for latent concepts from observed ABox literals, and evaluate Moose on MNIST-with-ontology and Pizzaïolo. Moose improves over propositional-NeSy, fuzzy-logic, and ontology embedding baselines, and presents the first reasoning-shortcut analysis in an OWL EL setting.

OWL 2 EL 描述逻辑配置文件被用于一些最大的生产级本体中，包括基因本体（Gene Ontology）和 SNOMED CT。现有的神经符号（NeSy）学习方法主要接受命题理论或 Datalog，而在本体设置中尚未对推理捷径（RS）感知进行研究。我们提出了 Moose，这是一种将 $\mathcal{EL}^{++}$ TBox 和有限 ABox 编译为句法决策图（SDD）的方法。SDD 充当可微分的加权模型计数层，我们在声明的穷举族上添加了超出 $\mathcal{EL}^{++}$ 配置文件的闭包子句，以克服 $\mathcal{EL}^{++}$ 在部分监督下表达能力有限的问题。我们证明了其终止性、可靠性、完备性和多项式中间大小，并在 Lean 中验证了这些证明。随后，我们定义了 OWL EL 本体上的首个形式化部分监督潜在概念学习任务（即从观察到的 ABox 字面量中学习潜在概念的个体级分类器），并在 MNIST-with-ontology 和 Pizzaïolo 上评估了 Moose。Moose 优于命题-神经符号、模糊逻辑和本体嵌入基线，并首次在 OWL EL 设置中进行了推理捷径分析。

---

## 元数据与出版详情 (Metadata & Publication Details)

* **arXiv ID:** [arXiv:2608.12961](https://arxiv.org/abs/2608.12961) [cs.AI]
* **学科分类 (Subjects):** 人工智能 (`cs.AI`)
* **主要收录会场 (Primary Venue):** 已被 **ISWC 2026** 研究赛道（Research Track）接受
* **提交日期 (Submission Date):** 2026年8月13日
* **作者 (Authors):** 
  * Olga Mashkova
  * Asaad Mohammedsaleh
  * Fernando Zhapa-Camacho
  * Robert Hoehndorf

---

## 资源与链接 (Resources & Links)

* **全文访问 (Full-Text Access):** 
  * [查看 PDF (View PDF)](https://arxiv.org/pdf/2608.12961)
  * [HTML 版本 - 实验性 (HTML Version (Experimental))](https://arxiv.org/html/2608.12961v1)
  * [TeX 源码 (TeX Source)](https://arxiv.org/src/2608.12961)
* **许可证 (License):** [知识共享署名 4.0 国际许可协议 (Creative Commons Attribution 4.0 International)](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
* **外部引用与工具 (External Citations & Tools):**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.12961)
  * [谷歌学术 (Google Scholar)](https://scholar.google.com/scholar_lookup?arxiv_id=2608.12961)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.12961)