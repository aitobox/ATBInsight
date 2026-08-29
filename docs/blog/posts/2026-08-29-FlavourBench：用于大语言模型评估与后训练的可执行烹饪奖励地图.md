---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 大语言模型
- 模型评估
- 后训练
- 基准测试
- 强化学习
title: FlavourBench：用于大语言模型评估与后训练的可执行烹饪奖励地图
---
### 文章背景与核心概要
评估开放式大语言模型（LLM）通常依赖于主观的替代方法，例如在缺乏客观答案时使用另一个模型或小型偏好评审团。为了解决这一痛点，《FlavourBench》提出了一种严谨的替代方案：通过版本化的烹饪环境来编译密集的答案地图。这种方法不仅能够提供客观、确定的评估标准，还能有效应用到模型的后训练阶段。

在该基准测试中，每个任务要求从8个候选食材中选择一个由3种食材组成的组合（portfolio），所有56种可能的组合均由名为 *Epicure* 的环境进行预先评分。研究人员在534个相同的替代、搭配和约束任务上测试了27个前沿模型端点，汇集了14,418个完整的模型-任务观测数据。尽管 Grok 4.6 获得了最高的点估计值（65.1），但严格的统计检验表明并没有单一绝对最优的端点。

此外，本文探讨了一项预注册的后训练研究，在 `Qwen3-0.6B` 上使用 LoRA 监督微调（SFT）。在270个 Epicure 最优答案上进行训练，在未见过的（held-out）地图上取得了显著优于格式和标签匹配对照组的性能提升，充分证明了可执行奖励地图在模型评估和后训练中的巨大效用。

---

## 📋 执行摘要 (Executive Summary)

Evaluating open-ended language models typically relies on subjective proxy methods, such as utilizing another model or a small preference panel when an objective answer key is missing. **FlavourBench** proposes a rigorous alternative by compiling dense answer maps from a versioned culinary environment. 

> 评估开放式大语言模型通常依赖于主观的替代方法，例如在缺乏客观答案时使用另一个模型或小型偏好评审团。**FlavourBench** 提出了一种严谨的替代方案，通过从版本化的烹饪环境中编译密集的答案地图来解决这一问题。

In this benchmark, each task requires selecting a three-ingredient portfolio out of eight candidates, with all 56 possible portfolios pre-scored by an environment called *Epicure*. Testing 27 frontier endpoints across 534 identical substitution, pairing, and constraint tasks yields 14,418 complete model-task observations. While Grok 4.6 achieved the highest point estimate (65.1), rigorous statistical testing shows no single unique best endpoint. 

> 在此基准测试中，每个任务要求从8个候选食材中选择由3种食材组成的组合，所有56种可能的组合均由名为 *Epicure* 的环境进行预先评分。在534个相同的替代、搭配和约束任务上测试了27个前沿端点，产生了14,418个完整的模型-任务观测数据。尽管 Grok 4.6 实现了最高的点估计（65.1），但严格的统计检验表明并不存在单一独特的最佳端点。

Furthermore, the paper explores a preregistered post-training study using LoRA Supervised Fine-Tuning (SFT) on `Qwen3-0.6B`. Training on 270 Epicure-optimal answers yielded significant improvements over format- and label-matched controls on held-out maps, demonstrating the efficacy of executable reward maps for both evaluation and post-training.

> 此外，本文探讨了一项预注册的后训练研究，该研究在 `Qwen3-0.6B` 上使用了 LoRA 监督微调（SFT）。在270个 Epicure 最优答案上进行训练，在保留地图（held-out maps）上取得了相对于格式和标签匹配对照组的显著提升，证明了可执行奖励地图在模型评估和后训练中的有效性。

---

## 🔬 核心贡献与方法论 (Key Contributions & Methodology)

### 1. FlavourBench 框架 (The FlavourBench Framework)
* **Task Structure:** Models are tasked with choosing a 3-ingredient portfolio from 8 candidates. 
* **The Epicure Environment:** Before inference, Epicure scores all 56 candidate portfolios to establish a grounded, executable reward map.
* **Scale of Evaluation:** Evaluated 27 frontier language-model endpoints on 534 substitution, pairing, and constraint tasks, compiling 14,418 scored model-task cells.

> * **任务结构：** 模型需从8个候选食材中选择3种食材的组合。
> * **Epicure 环境：** 在推理之前，Epicure 对所有56个候选组合进行评分，以建立扎实的可执行奖励地图。
> * **评估规模：** 在534个替代、搭配和约束任务上评估了27个前沿大语言模型端点，汇集了14,418个带评分的模型-任务单元。

### 2. 统计严谨性与稳健性 (Statistical Rigor & Robustness)
* **Significance Testing:** Anchor-cluster bootstraps and multiplicity-controlled paired tests successfully resolved 101 out of 351 possible model contrasts.
* **Rank Stability:** The evaluation ranking remains robust across independently compiled panels, alternative metrics, task filters, family weights, and three distinct public Epicure checkpoints.

> * **显著性检验：** 锚点集群自助法（Anchor-cluster bootstraps）和多重性控制配对检验成功解析了351种可能的模型对比中的101种。
> * **排名稳定性：** 评估排名在独立编译的评审团、替代指标、任务过滤器、家族权重以及三个不同的公开 Epicure 检查点之间保持稳健。

### 3. 预注册后训练研究 (Preregistered Post-Training Study)
* **Controlled Reward Transfer:** Conducted a preregistered, 3-seed post-training study using LoRA SFT on a pinned `Qwen3-0.6B` checkpoint.
* **Performance Gains:** Fine-tuning on 270 Epicure-optimal answers improved scores on 84 anchor-disjoint maps by **13.30 points** over a control (95% CI: 6.52 to 20.29, $p = 0.000170$).
* **Replication:** The replication gain on all 534 public maps reached **11.73 points** (95% CI: 8.98 to 14.54), with both trained arms successfully parsing every response.

> * **受控奖励迁移：** 在固定的 `Qwen3-0.6B` 检查点上，使用 LoRA SFT 进行了预注册的、3随机种子的后训练研究。
> * **性能提升：** 在270个 Epicure 最优答案上进行微调，使84个锚点不相交地图上的得分比对照组提高了 **13.30分**（95% 置信区间：6.52 至 20.29，$p = 0.000170$）。
> * **复现：** 在所有534个公共地图上的复现增益达到了 **11.73分**（95% 置信区间：8.98 至 14.54），且两个训练分支均成功解析了所有响应。

---

## 📂 资源可用性 (Resource Availability)

The release package includes:
* Prompts and exhaustive reward maps
* Raw model responses
* Training and evaluation manifests
* Statistical plans and source code
* An offline verifier

> 发布包包括：
> * 提示词与详尽的奖励地图
> * 原始模型响应
> * 训练与评估清单
> * 统计计划与源代码
> * 离线验证器

<div class="abs-license"><a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article">
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
<span>查看许可证</span>
</a></div>