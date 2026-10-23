---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-24
hide:
  - navigation
tags:
  - 扩散语言模型
  - 约束解码
  - DConstrain
  - 语法引导生成
  - 编译优化
title: "DConstrain：通过编译上下文参数化状态转移实现扩散语言模型约束解码"
---

# DConstrain：通过编译上下文参数化状态转移实现扩散语言模型约束解码

> # DConstrain: Compiling Context-Parameterized Transitions for Diffusion Language Model Constrained Decoding

> **ArXiv ID:** [arXiv:2610.30920](https://arxiv.org/abs/2610.30920) [cs.AI]  
> **Authors:** Shidong Cao, Jing Ma, Wenhao Chai, Yuchen Tian, Lun Du, Da Zheng  
> **Subject:** Artificial Intelligence (`cs.AI`)  
> **Submitted:** 22 October 2026  
> **DOI:** [10.48550/arXiv.2610.30920](https://doi.org/10.48550/arXiv.2610.30920)  
> **Links:** [View PDF](https://arxiv.org/pdf/2610.30920) | [HTML Version](https://arxiv.org/html/2610.30920v1) | [TeX Source](https://arxiv.org/src/2610.30920) | [License](http://creativecommons.org/licenses/by/4.0/)

### 文章背景与核心概要

随着文本生成技术的发展，扩散语言模型 (Diffusion Language Model, DLM) 凭借全序列并行生成的超高吞吐潜力引起了学术界与工业界的广泛关注；但在实际结构化数据输出 (如 JSON 或工具调用) 场景中，由于缺乏自回归的时序因果约束，并行生成的各个 Token 往往会产生语法冲突，导致难以严格遵循预设的数据架构 (Schema)。以往的精确约束解码方法试图离线枚举所有解析状态，但这会导致解析栈与字段历史的状态空间呈指数级爆炸，迫使开发者不得不强制固定字段顺序并牺牲合法的输出多样性。

为了打破这一严峻瓶颈，来自多所顶尖研究机构的学者联手推出了创新解码框架 **DConstrain**。该框架开创性地将语法架构编译为“上下文参数化状态转移程序”，通过冷编译将解析逻辑符号化、温编译在模型前向计算的同时重叠构建合法转移图，并在运行时动态追踪字段状态，巧妙规避了离线状态爆炸问题。实验表明，DConstrain 在权威工具调用基准测试 BFCL 架构下不仅达成了 100% 的完备编译率，并将端到端解码延迟降低了 6.65 至 46.26 倍，更将 DiffusionGemma 模型的任务准确率从 37.27% 跃升至 81.56%，为非自回归与扩散模型的工业级结构化应用奠定了坚实基石。

---

## 摘要概要

> ## Abstract Summary

扩散语言模型 (DLM) 能够同时并行生成多个 Token，但这种机制往往会导致生成的单个 Token 虽然在局部完全合法，组合在一起时却违反给定数据架构 (Schema) 的语法约束。虽然基于语法图进行精确联合推断能够确保严格的语法合规性，但该方法通常需要在海量的假想解析器配置中追踪由 Token 标注的后继状态。由于在编译状态中直接编码解析栈和字段历史会导致状态数量发生指数级爆炸，以往的精确解码器不得不强制限制属性的出现顺序，从而无端排除了许多原本合法的有效输出。

> Diffusion language models (DLMs) generate multiple tokens in parallel, which can often result in individually valid tokens that are incompatible under a given schema. While exact joint inference over a grammar graph enforces strict compatibility, doing so typically requires tracking token-labeled successors across a massive number of hypothetical parser configurations. Because encoding stacks and field histories directly into compiled states leads to exponential growth, previous exact decoders have had to restrict property orders and exclude valid outputs.

为了克服这些局限性，作者团队推出了 **DConstrain**——一种将语法架构编译为*上下文参数化状态转移程序 (Context-Parameterized Transition Programs)* 的全新框架：

> To overcome these limitations, the authors introduce **DConstrain**, a novel framework that compiles schemas into *context-parameterized transition programs*:

* **冷编译 (Cold Compilation)**：将 Token 消耗特化到局部语法状态，同时以符号形式保留上下文相关的调用栈操作、环境守卫以及由调用方决定的延迟解析。通过将字段历史作为运行时数值进行动态追踪，该方法可在无需离线枚举所有字段子集的情况下，完整支持任意属性顺序。
* **温编译 (Warm Compilation)**：将推理时实际触达的运行时配置绑定到这些状态转移程序，从而构建出精确的后继状态图。由于该图构建过程完全不需要依赖模型的预测打分，因此它可以直接与模型前向计算重叠并行执行。
* **Token 效应分组 (Token-Effect Grouping)**：在绑定运行时上下文之前，先将编译后具有相同状态转移效应的 Token 进行合并。即便这些 Token 的具体后继状态互不相同，这些分组也能在各种解析栈和环境之间实现高效复用。

> * **Cold Compilation:** Specializes token consumption to local grammar states while retaining context-dependent stack operations, environment guards, and caller-dependent deferred parsing symbolically. By tracking field histories as runtime values, it supports arbitrary property orders without requiring offline enumeration of field subsets.
> * **Warm Compilation:** Binds reached runtime configurations to these transition programs to construct exact successors. This process overlaps directly with the model's forward pass because graph construction does not require model scores.
> * **Token-Effect Grouping:** Merges tokens with identical compiled effects prior to binding runtime contexts. These groups can then be reused across various stacks and environments, even when their concrete successors differ.

### 核心成果

> ### Key Results

* **鲁棒的架构编译能力**：在任意属性顺序下，成功实现了 **100% 的 BFCL 架构**编译 (相比之下，经过深度优化的有限状态自动机基线仅能达成 71.30%–85.81%)。
* **显著降低端到端延迟**：在支持任意属性顺序并保持 100% 架构合规性的前提下，将 BFCL 端到端解码延迟大幅降低了 **6.65 至 46.26 倍**。
* **大幅提振生成准确率**：将 DiffusionGemma 模型在 BFCL 上的生成准确率从固定顺序下的 **37.27%** 强力跃升至 **81.56%**。

> * **Robust Schema Compilation:** Successfully compiles **100% of BFCL schemas** under arbitrary property orders (whereas an optimized finite-state baseline manages only 71.30–85.81%).
> * **Latency Reduction:** Reduces BFCL end-to-end decoding latency by **6.65 to 46.26 times** under arbitrary property orders while maintaining 100% schema validity.
> * **Accuracy Boost:** Raises DiffusionGemma's BFCL accuracy from **37.27%** (under fixed order) to **81.56%**.

---

## 附加信息

> ## Additional Information

* **论文备注**：全文共 39 页，包含 6 张插图与 12 张表格
* **DOI 标识符**：[10.48550/arXiv.2610.30920](https://doi.org/10.48550/arXiv.2610.30920)
* **音频总结**：[收听音频解读](/audio/2610.30920)

> * **Comments:** 39 pages, 6 figures, 12 tables
> * **DOI:** [10.48550/arXiv.2610.30920](https://doi.org/10.48550/arXiv.2610.30920)
> * **Audio Summary:** [Listen to Audio Summary](/audio/2610.30920)

[![license icon](./images/345c7ad61f1b.png) License](http://creativecommons.org/licenses/by/4.0/)
