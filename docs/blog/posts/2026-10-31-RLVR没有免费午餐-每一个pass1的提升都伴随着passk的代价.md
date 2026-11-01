---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-31
hide:
  - navigation
tags:
  - 强化学习
  - RLVR
  - pass@k
  - 熵坍塌
  - 理论研究
title: "RLVR 没有免费午餐：每一个 pass@1 的提升都伴随着 pass@k 的代价"
---

# RLVR 没有免费午餐：每一个 pass@1 的提升都伴随着 pass@k 的代价

> **arXiv:2610.39295** [cs.LG]  
> **Authors:** Yinuo Liu  
> **Submitted:** October 29, 2026  
> **Subjects:** Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`); Optimization and Control (`math.OC`); Machine Learning (`stat.ML`)  
> **Code:** [GitHub - yliusci/no-free-lunch-rlvr](https://github.com/yliusci/no-free-lunch-rlvr)

### 文章背景与核心概要

在以 DeepSeek-R1 和 OpenAI o1 为代表的推理大模型浪潮中，基于可验证奖励的强化学习 (Reinforcement Learning with Verifiable Rewards, RLVR) 凭借在数学与代码任务上的卓越表现成为了当之无愧的焦点。然而学界长期观察到一个诡异的“倒挂”现象：强化学习虽然能大幅提升模型的单次解题成功率 (`pass@1`)，但一旦放宽采样次数 (`pass@k`)，经过强化微调的模型在多次采样下的总体解题率反而落后于原始基座模型。这究竟是训练未收敛的暂时缺陷，还是不可逾越的底层法则？来自学者 Yinuo Liu 的最新研究通过严格的数学推导，正式确立了 RLVR 的“没有免费午餐定理”——每一次 `pass@1` 的指标跃升，都在数学层面上严格对应着某些困难提示词上解题能力的衰退与多样性损失。这一里程碑式的理论成果不仅揭示了强化学习并不能向外凭空拓宽模型的推理前沿，而且将“熵坍塌”与“熵-性能定律”统一在指数倾斜框架之下，为大模型推理优化的边界认知与评测方法树立了全新的理论基石。

---

## 执行摘要

> ## Executive Summary

基于可验证奖励的强化学习 (RLVR) 通常能显著提高语言模型初次尝试的成功率 (`pass@1`)，但当给予多次采样尝试 (`pass@k`) 时，其表现却往往会逊色于基座模型。

> Reinforcement Learning with Verifiable Rewards (RLVR) typically increases a language model's success rate on the first try (`pass@1`), but often causes it to underperform relative to the base model when given multiple sampling attempts (`pass@k`). 

来自 Yinuo Liu 的这篇论文平息了长期以来的争论：这种权衡取舍究竟只是训练过程中的暂态阶段，还是一种根本性的固有局限？通过最新建立的严格定理，作者从数学上证明了这种性能反转其实是一种精确的、受数学上界约束的必然代价：

> This paper by Yinuo Liu settles the ongoing debate over whether this trade-off is a transient training phase or a fundamental limitation. Through a newly established theorem, the author proves that this reversal is an exact, mathematically bounded cost:

* **权衡取舍具有根本性**：在排他性特化机制下，模型策略的每一次旨在提升 `pass@1` 的参数更新，都必定会严格降低某些提示词 (Prompt) 上的解题成功率。
* **紧致的数学上界**：性能曲线发生交叉反转的次数，受到各提示词成功率变化之符号变异数 (Sign Variation) 的严格约束 (这是一个全正且紧致的数学上界)。
* **统一的底层机制**：同一个指数倾斜恒等式 (Exponential Tilt Identity) 将强化学习中的“熵坍塌”与“熵-性能定律”纳入到了单一而优美的数学框架之中。

> * **The Trade-Off is Fundamental:** Every update that increases `pass@1` strictly lowers the success rate of some prompts under exclusive specialization.
> * **Tight Mathematical Bounds:** The number of crossovers is bounded by the sign variation of the shift in per-prompt success (a totally positive, tight bound).
> * **Unified Mechanism:** The same exponential tilt identity bridges entropy collapse and the entropy-performance law under a single mathematical framework.

归根结底，强化学习 (Reinforcement Learning) 并不能向外拓宽大语言模型 (Large Language Model, LLM) 的推理前沿；相反，它只是让模型沿着既有的能力边界移动，而且必须付出可精确量化的代价。

> Ultimately, reinforcement learning does not widen the reasoning frontier; rather, it allows models to move along it at a quantifiable price.

---

## 论文元数据

> ## Paper Metadata

* **arXiv 编号**：[arXiv:2610.39295 [cs.LG]](https://arxiv.org/abs/2610.39295)
* **论文作者**：Yinuo Liu
* **提交日期**：2026 年 10 月 29 日
* **主分类**：机器学习 (`cs.LG`)
* **次分类**：人工智能 (`cs.AI`)；优化与控制 (`math.OC`)；统计机器学习 (`stat.ML`)
* **代码与验证工具包**：已开源于 [GitHub](https://github.com/yliusci/no-free-lunch-rlvr) (全部 34/34 项自动化检查均已通过)

> * **arXiv ID:** [arXiv:2610.39295 [cs.LG]](https://arxiv.org/abs/2610.39295)
> * **Authors:** Yinuo Liu
> * **Submitted:** October 29, 2026
> * **Primary Subject:** Machine Learning (`cs.LG`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`); Optimization and Control (`math.OC`); Machine Learning (`stat.ML`)
> * **Code & Verification Package:** Available on [GitHub](https://github.com/yliusci/no-free-lunch-rlvr) (34/34 automated checks passed)

---

## 摘要

> ## Abstract

基于可验证奖励的强化学习 (RLVR) 往往会让语言模型陷入一种奇特的境地：它在“单次尝试”下的解题表现更加出色，但在“多次尝试”下的成功率反而下滑——换言之，强化学习大幅拉高了模型的 `pass@1`，但在采样预算 $k$ 较大时，未经微调的基座模型却能在 `pass@k` 上完成反超。这究竟暴露出强化学习未能真正赋予模型推理能力，还是仅仅是可以通过延长训练时间就能自然化解的暂态现象？本文通过建立一个严谨的数学定理彻底平息了这场争议。研究表明，这种性能反转绝非偶然失误，而是优化过程中必然付出的“代价”，并且我们在文中精确推导出了这一代价的定量速率。将 RLVR 建模为在跨提示词共享策略空间上对基座策略的“指数倾斜 (Exponential Tilt)”，我们证明在排他性特化 (Exclusive Specialization) 机制下，任何旨在提升 `pass@1` 的参数更新，都必定会严格降低某些提示词上的解题成功率；基于凸分析中的 Stiemke 对偶性 (Stiemke Duality)，提示词上存在严格正的边际代价，正是这种特化权衡的充分必要条件，并且数学证明表明，仅仅在某个提示词上成为最优策略，根本不足以抵消这种代价。当优化损失传导至难度最高的提示词时，便会不可避免地触发 `pass@k` 性能曲线的交叉反转，而曲线发生交叉反转的次数上限，受到各个提示词成功率变化向量之“符号变异数 (Sign Variation)”的严格约束；这是一个基于全正性 (Totally Positive) 的紧致数学上界，并且在保持偏序的特殊情形下，该定理完美还原了既有文献中所报道的“单次交叉”结论。这种性能交叉绝不是可以通过打补丁修复的工程缺陷：在受限优化路径下，参数更新轨迹精确勾勒出了 `pass@1` 与 `pass@k` 之间的能力帕累托前沿；如果强行要求完全消除这种交叉，就必须彻底牺牲掉模型在 `pass@1` 上取得的全部增益！此外，同一个指数倾斜恒等式还能自然导出“熵坍塌 (Entropy Collapse)”现象以及具有可辨识指数的“熵-性能定律 (Entropy-Performance Law)”，从而用同一套底层数学机制将两大独立的研究领域完美统一起来。强化学习无法向外拓展模型的推理前沿，它所能做的仅仅是沿着既有的能力边界滑动——我们还设计了一套诊断工具，只需分析任意评测日志，便可直接计算出理论边界、执行保序检验并量化实际代价。天下没有免费的午餐，一切皆有代价。

> Reinforcement learning with verifiable rewards (RLVR) makes a language model solve more problems on the first try and fewer when given many tries: it raises `pass@1` while the base model overtakes it at large sampling budget $k$. Is this a failure of RL to add reasoning, or a transient that more training removes? We settle the question with a theorem. The reversal is a price, and we compute its exact rate. Modeling RLVR as an exponential tilt of a base policy over strategies shared across prompts, we prove that under exclusive specialization every update that raises `pass@1` strictly lowers the success of some prompt; a strictly positive price on prompts (Stiemke duality) is the exact condition, and being merely the best strategy on a prompt is provably not enough. When the loss reaches the hardest prompts, it forces a `pass@k` crossover, and the number of crossings is at most the sign variation of the shift in per-prompt success, a totally positive bound that is tight and that recovers the known single-crossover result as its order-preserving case. The crossover is not a bug to patch: a constrained update traces the exact `pass@1` versus `pass@k` frontier, and removing the crossover entirely costs the entire `pass@1` gain. The same tilt identity yields entropy collapse and the entropy-performance law with an identifiable exponent, unifying two literatures under one mechanism. Reinforcement cannot widen the reasoning frontier; it can only move along it, at a price we make measurable by a diagnostic that reads the bound, the order-preserving test, and the price from any evaluation log. There is no free lunch, only a price.

---

## 核心结论与主要贡献

> ## Key Takeaways & Contributions

1. **精确量化代价速率**：将 RLVR 形式化建模为策略分布上的“指数倾斜”，从数学上严格证明了模型在简单或特定目标提示词上取得的性能提升，必定以牺牲其他提示词的成功率为严格代价。
2. **揭示 Stiemke 对偶条件**：严谨论证了在各个提示词上存在严格正的影子价格 (基于 Stiemke 对偶性)，是模型发生策略特化权衡取舍的充要条件。
3. **建立全正性数学紧界**：确立了 `pass@k` 性能曲线交叉反转的次数，受到每个提示词成功率变化向量之“符号变异数”的严格约束，给出了紧致的全正性数学上界。
4. **构建熵坍塌统一理论**：借助统一的指数倾斜恒等式，将强化学习策略优化中的权衡博弈、熵坍塌现象以及熵-性能经验定律无缝桥接在同一理论框架之下。

> 1. **Exact Rate Calculation:** Formulates RLVR as an exponential tilt of a base policy over strategies, proving that performance gains on easy or targeted prompts come at a strict cost to others.
> 2. **Stiemke Duality Condition:** Demonstrates that a strictly positive price on prompts is the exact condition for specialization trade-offs.
> 3. **Totally Positive Bound:** Establishes that the number of `pass@k` crossovers is tightly bounded by the sign variation of the shift in per-prompt success.
> 4. **Unified Theory of Entropy Collapse:** Connects policy optimization trade-offs with entropy collapse and the entropy-performance law via a unified tilt identity.
