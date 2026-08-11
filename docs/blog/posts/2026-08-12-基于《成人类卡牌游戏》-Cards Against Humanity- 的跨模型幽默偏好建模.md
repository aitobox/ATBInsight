---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-12
hide:
- navigation
tags:
- 大语言模型
- 幽默偏好
- 心智理论
- 人机交互
- 模型对齐
title: 基于《成人类卡牌游戏》(Cards Against Humanity) 的跨模型幽默偏好建模
---
### 文章背景与核心概要

本文探讨了大型语言模型（LLM）是否能够通过受控的《成人类卡牌游戏》（Cards Against Humanity）任务，成功模拟并适应另一个模型的幽默偏好。研究者通过让 GPT-4o 担任“裁判”（Czar），Claude Opus-4.5 担任“玩家”（Player），在二元幽默选择任务中筛选出 244 组双方偏好确定且截然相反的案例，旨在探究模型对齐的驱动因素。

研究发现，仅依靠角色指令或模型身份提示（Framing）对跨模型对齐的提升微乎其微。相反，当模型能够获取对方的行为证据（Prior choices），尤其是结合了推理过程（Rationales）时，其模拟对方偏好的能力显著增强。这一结果展示了一种操作层面的“类心智理论”（theory-of-mind-like）行为，为理解模型间的交互与偏好对齐提供了重要参考。

---

## 跨模型幽默偏好建模：基于《成人类卡牌游戏》

> # Cross-Model Humor Preference Modeling with Cards Against Humanity
>
> **Authors:** Victor Winter, Farhan Lakhany  
> **Submitted:** June 9, 2026  
> **Primary Subject:** Human-Computer Interaction (`cs.HC`)  
> **arXiv ID:** [2608.07481](https://arxiv.org/abs/2608.07481) [cs.HC]  
> **DOI:** [10.48550/arXiv.2608.07481](https://doi.org/10.48550/arXiv.2608.07481)

---

## 执行摘要

本文研究了一个大语言模型（LLM）是否可以通过受控的《成人类卡牌游戏》风格任务，成功近似并适应另一个模型的幽默偏好。

> ## Executive Summary
>
> This paper investigates whether one Large Language Model (LLM) can successfully approximate and adapt to the humor preferences of another using a controlled *Cards Against Humanity*-style task. 

通过测试 **GPT-4o**（担任“裁判”）和 **Claude Opus-4.5**（担任“玩家”）在二元幽默选择任务中的表现，研究人员筛选出了 244 组双方偏好确定但截然相反的案例。研究通过五个分级条件对“玩家”进行评估，以确定是框架（指令和模型身份）还是行为证据（先前的选择和理由）更能推动跨模型对齐。

> By testing **GPT-4o** (acting as the "Czar") and **Claude Opus-4.5** (acting as the "Player") across a binary humor-selection task, the researchers isolated 244 hands where both models held deterministic yet opposite preferences. The Player was evaluated across five graded conditions to determine whether framing (instructions and model identity) or behavioral evidence (prior choices and rationales) drives better cross-model alignment. 

结果表明，简单的角色指令仅能带来微不足道的收益，而获取行为证据——特别是在伴随推理说明的情况下——极大地提高了“玩家”模拟“裁判”偏好的能力，展示了一种操作层面的“类心智理论”行为。

> The results demonstrate that simple role instructions yield only negligible gains, whereas access to behavioral evidence—particularly when accompanied by rationales—drastically improves the Player's ability to mirror the Czar's preferences, showcasing an operational form of "theory-of-mind-like" behavior.

---

## 方法论与实验设计

为了防止成功依赖于自我偏好，研究人员建立了一个严格的评估流程：

> ## Methodology & Experimental Design
>
> To prevent success from relying on self-preference, the researchers established a rigorous evaluation pipeline:

1. **模型角色：**
   * **裁判 (Czar)：** GPT-4o
   * **玩家 (Player)：** Claude Opus-4.5
2. **任务结构：** 基于《成人类卡牌游戏》的二元幽默选择任务。
3. **数据过滤：** 通过反射单元稳定性程序过滤掉不稳定的迭代，得出 **244 手** 偏好确定且相反的案例。这些案例被划分为：
   * **97 手上下文池**
   * **147 手留出测试池**
4. **分级评估条件：** “玩家”在五个渐进式信息条件下进行测试，以区分 *框架效应* 与 *直接行为证据*：
   * **条件 1：** 默认自我偏好（基准）。
   * **条件 2：** 通用裁判建模指令（仅框架）。
   * **条件 3：** 模型识别裁判（带身份的框架）。
   * **条件 4：** 先前的裁判选择（引入行为证据）。
   * **条件 5：** 先前的裁判选择配以理由（行为证据 + 推理）。

> 1. **Model Roles:** 
>    * **Czar:** GPT-4o
>    * **Player:** Claude Opus-4.5
> 2. **Task Structure:** A binary humor-selection task framed around *Cards Against Humanity*.
> 3. **Data Filtering:** A reflected-cell stability procedure filtered out unstable iterations, yielding **244 hands** of deterministic, opposite preferences. These were partitioned into:
>    * A **97-hand context pool**
>    * A **147-hand held-out test pool**
> 4. **Graded Evaluation Conditions:** The Player was tested across five progressively informative conditions to separate *framing effects* from *direct behavioral evidence*:
>    * **Condition 1:** Default self-preference (baseline).
>    * **Condition 2:** Generic Czar-modeling instruction (framing only).
>    * **Condition 3:** Model-identified Czar (framing with identity).
>    * **Condition 4:** Prior Czar selections (behavioral evidence introduced).
>    * **Condition 5:** Prior Czar selections paired with rationales (behavioral evidence + reasoning).

---

## 主要发现

* **准确率进展：**
  * “玩家”的基准准确率从 **0.7%** 开始（条件 1）。
  * 仅框架条件显示出适度的改进，分别上升至 **19.0%**（条件 2）和 **25.9%**（条件 3）。
  * 一旦引入行为证据，准确率显著跃升至 **72.8%**（条件 4），并在条件 5 中达到 **82.3%** 的峰值。
* **统计显著性：** 通过 Cochran's Q 检验以及随后的成对 McNemar 检验，证实了评估梯度上的每一步提升都产生了统计学上显著的性能改进。

> ## Key Findings
>
> * **Accuracy Progression:** 
>   * The Player's baseline accuracy began at **0.7%** (Condition 1).
>   * Framing-only conditions showed modest improvements, rising to **19.0%** (Condition 2) and **25.9%** (Condition 3).
>   * Once behavioral evidence was introduced, accuracy jumped significantly to **72.8%** (Condition 4) and peaked at **82.3%** (Condition 5).
> * **Statistical Significance:** An omnibus Cochran's Q test, followed by pairwise McNemar tests, confirmed that every single step upward along the evaluation gradient produced a statistically significant improvement in performance.

---

## 结论与启示

研究结果表明，角色指令和了解 AI 模型的身份对跨模型对齐仅提供微小的辅助。在建模另一个模型的主观品味时，真正的预测成功需要 **直接的行为证据**，特别是在辅以 **推理说明** 时。

> ## Conclusion & Implications
>
> The findings indicate that role instructions and knowing an AI model's identity provide only minor aids in cross-model alignment. True predictive success in modeling another model's subjective tastes requires **direct behavioral evidence**, especially when augmented with **rationales**. 

作者将这些结果解释为一种操作层面的 **类心智理论行为**：玩家从其固有的自我偏好转向了另一个代理所展示的偏好，并在没有暗示任何字面意义上的心理状态内部表征的情况下成功运作。

> The authors interpret these results as an operational form of **theory-of-mind-like behavior**: the Player shifts away from its inherent self-preference toward the demonstrated preferences of another agent, operating successfully without implying any literal internal representation of mental states.