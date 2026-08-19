---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- 自动特征工程
- 大语言模型
- SHAP
- 特征选择
- 机器学习
title: SIGMA：面向无元数据 LLM 自动特征工程的 SHAP 引导隐式轨迹生成
---
### 文章背景与核心概要

自动特征工程（AutoFE）领域近期通过利用大语言模型（LLM）的语义理解能力和轨迹提示（Trajectory-based prompting）取得了显著进展。然而，在长周期优化任务中，该方法面临两大核心瓶颈：一是实际应用场景中往往缺乏必要的语义元数据；二是随着优化轨迹的累积，提示词长度迅速膨胀，极易触及上下文窗口限制，而若舍弃轨迹信息，则会导致模型陷入局部最优并产生大量重复特征。

为了解决上述挑战，本文提出了 SIGMA（SHAP-enhanced Implicit-trajectory Generation for Metadata-free AutoFE），这是一个具备可扩展性的恒定上下文优化框架。该框架通过引入 SHAP 值替代缺失的语义元数据，并采用“隐式轨迹”方法，在保持提示词长度近乎恒定的前提下，显著提升了特征生成的效率与质量，在减少特征冗余的同时达到了行业领先的性能水平。

---

## 📌 摘要

> Recent advancements in Automated Feature Engineering (AutoFE) leverage Large Language Models (LLMs) via semantic descriptions and trajectory-based prompting. However, two major hurdles limit their scalability and applicability in long-horizon optimization:
> 1. **Lack of Metadata:** Semantic metadata is frequently unavailable in practical settings.
> 2. **Context Window Limitations:** Accumulating trajectories increases prompt length and risks exceeding context limits. Conversely, omitting trajectories leads to instability, local optima traps, and high feature duplication rates.
> 
> To address these challenges, the authors propose **SIGMA** (SHAP-enhanced Implicit-trajectory Generation for Metadata-free AutoFE), a scalable, constant-context optimization framework. 

近期自动特征工程（AutoFE）的进展利用大语言模型（LLM）通过语义描述和基于轨迹的提示进行优化。然而，两个主要障碍限制了它们在长周期优化中的可扩展性和适用性：
1. **元数据缺失：** 在实际应用中，语义元数据往往不可用。
2. **上下文窗口限制：** 累积轨迹会增加提示词长度，并有超出上下文限制的风险。相反，省略轨迹会导致不稳定性、陷入局部最优以及高特征重复率。

为了应对这些挑战，作者提出了 **SIGMA**（SHAP 增强的无元数据 AutoFE 隐式轨迹生成），这是一个可扩展的、恒定上下文的优化框架。

### 核心贡献：
> ### Key Contributions:
> * **SHAP-Guided Generation:** Replaces unavailable semantic metadata with SHAP values to provide task-aware signals that guide group feature generation.
> * **Implicit Trajectory Approach (EXIT):** Introduces the *EXposed-feature Implicit Trajectory (EXIT)* method, where exposed features in the prompt implicitly represent the optimization trajectory.
> * **Empirical Performance:** 
>   * Matches state-of-the-art (SOTA) LLM baseline performance using a nearly constant prompt length.
>   * Significantly reduces the feature duplication ratio from **37.2% down to 6.8%**.
>   * Achieves traditional SOTA performance with an average of only **5.4 features**, demonstrating exceptional feature utilization efficiency.

* **SHAP 引导生成：** 用 SHAP 值替代不可用的语义元数据，提供任务感知信号，从而引导组特征的生成。
* **隐式轨迹方法 (EXIT)：** 引入了“暴露特征隐式轨迹”（EXposed-feature Implicit Trajectory, EXIT）方法，通过提示词中暴露的特征隐式地表示优化轨迹。
* **实证表现：**
    * 在使用近乎恒定的提示词长度的情况下，匹配了当前最先进（SOTA）LLM 基线的性能。
    * 将特征重复率从 **37.2%** 显著降低至 **6.8%**。
    * 平均仅使用 **5.4 个特征**即达到了传统 SOTA 的性能，展现了卓越的特征利用效率。

---

## 🔗 全文与资源

> ## 🔗 Full-Text & Resources
> 
> * **[View PDF](https://arxiv.org/pdf/2608.17948)**
> * **[Experimental HTML](https://arxiv.org/html/2608.17948v1)**
> * **[TeX Source](https://arxiv.org/src/2608.17948)**
> 
> <div align="center">
>   <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" />
>   <br>
>   <a href="http://creativecommons.org/licenses/by/4.0/">View License (CC BY 4.0)</a>
> </div>

* **[查看 PDF](https://arxiv.org/pdf/2608.17948)**
* **[实验 HTML](https://arxiv.org/html/2608.17948v1)**
* **[TeX 源码](https://arxiv.org/src/2608.17948)**

<div align="center">
  <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" />
  <br>
  <a href="http://creativecommons.org/licenses/by/4.0/">查看许可协议 (CC BY 4.0)</a>
</div>