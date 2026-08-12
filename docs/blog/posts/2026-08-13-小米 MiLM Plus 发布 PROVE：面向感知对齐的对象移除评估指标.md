---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-13
hide:
- navigation
tags:
- 小米
- 计算机视觉
- 视频修复
- 模型评估
- 开源
title: 小米 MiLM Plus 发布 PROVE：面向感知对齐的对象移除评估指标
---
### 文章背景与核心概要
来自**小米集团 MiLM Plus** 的研究团队推出了 **PROVE**（Perceptual RemOVal cohErence，感知移除一致性）评估框架，旨在解决现有对象移除评估指标的局限性。该研究已被 **ACM MM 2026** 接收，PROVE 提供了两个感知对齐的指标——**RC-S**（空间一致性）和 **RC-T**（时间一致性），并配套了一个两级真实世界视频基准测试 **PROVE-Bench**。通过在 DINOv2 特征上利用滑动窗口最大均值差异（MMD），PROVE 为评估视频修复模型提供了一种强健且无需参考（Reference-free）的方法，其性能显著优于 PSNR、SSIM 和 CFD 等传统指标。

---

# 小米 MiLM Plus 发布 PROVE：面向感知对齐的对象移除评估指标

> Xiaomi’s MiLM Plus Releases PROVE: Perception-Aligned Object Removal Metrics

### 摘要

来自**小米集团 MiLM Plus** 的研究团队推出了 **PROVE**（Perceptual RemOVal cohErence），这是一个旨在解决现有对象移除指标局限性的评估框架。PROVE 已被 **ACM MM 2026** 接受，它提供了两个感知对齐的指标——**RC-S**（空间一致性）和 **RC-T**（时间一致性），以及一个两级真实世界视频基准测试 **PROVE-Bench**。通过在 DINOv2 特征上利用滑动窗口最大均值差异（MMD），PROVE 提供了一种强健、无需参考的方法来评估视频修复模型，其性能显著优于 PSNR、SSIM 和 CFD 等传统指标。

> A research team from **MiLM Plus, Xiaomi Inc.** has introduced **PROVE** (Perceptual RemOVal cohErence), an evaluation framework designed to address the limitations of existing object removal metrics. Accepted at **ACM MM 2026**, PROVE provides two perception-aligned metrics—**RC-S** (spatial coherence) and **RC-T** (temporal consistency)—alongside a two-tier real-world video benchmark, **PROVE-Bench**. By utilizing sliding-window Maximum Mean Discrepancy (MMD) over DINOv2 features, PROVE offers a robust, reference-free way to evaluate video inpainting models, significantly outperforming traditional metrics like PSNR, SSIM, and CFD.

---

## 它能否落地部署？

> ## Is it Deployable?

**可以——作为评估测试工具（evaluation harness）。** PROVE 以 Apache 2.0 许可证的 PyTorch 代码库形式发布。它专为 CI/CD 流水线、模型基准测试和训练数据过滤而设计。

> **Yes—as an evaluation harness.** PROVE is released as an Apache 2.0 PyTorch repository. It is designed for CI/CD pipelines, model benchmarking, and training data filtering.

*   **行业应用：** 智能手机相册应用、VFX 后期制作、电商图片清理以及隐私遮挡。
*   **性能表现：** 在 RTX 4090 上，RC-S 的运行速度约为 134.6 毫秒/帧，这使其对于自动化的夜间测试非常具有实用性。
*   **运行要求：** Python 3.10+、PyTorch 2.6+ 以及 DINOv2-giant 权重。它需要一个指示被移除对象的掩码（mask）。
*   **局限性：** 不适合实时的端侧打分；在处理明显超出评估裁剪区域的大面积阴影或反射时可能会遇到困难。

> *   **Industry Applications:** Smartphone gallery apps, VFX post-production, e-commerce cleanup, and privacy redaction.
> *   **Performance:** RC-S runs at ~134.6 ms/frame on an RTX 4090, making it highly practical for automated nightly testing.
> *   **Requirements:** Python 3.10+, PyTorch 2.6+, and DINOv2-giant weights. It requires a mask indicating the removed object.
> *   **Limitations:** Not suitable for real-time on-device scoring; may struggle with large shadows or reflections extending significantly beyond the evaluation crop.

## 传统指标已被记录的失效模式

> ## Documented Failure Modes of Traditional Metrics

现有指标往往会失效，因为对象移除是一个“病态的、一对多”的任务，其中并不存在单一的真实标准（ground truth）。

> Existing metrics often fail because object removal is an "ill-posed, one-to-many" task where no single ground truth exists.

1.  **全参考偏差（Full-Reference Bias）：** 诸如 PSNR 和 SSIM 之类的指标奖励像素级的完美重建，这往往会偏爱“复制-粘贴”伪影，而不是真正的基于扩散模型的擦除。
2.  **无参考盲区（No-Reference Blind Spots）：** 现有的诸如 ReMOVE 和 CFD 之类的指标经常无法对模糊区域进行惩罚，有时甚至给它们的评分比未编辑的输入还要高。
3.  **时间不敏感性（Temporal Insensitivity）：** 当前的时间指标运行在全帧特征上，这使得它们对编辑区域内的小型、局部伪影基本处于失明状态。

> 1.  **Full-Reference Bias:** Metrics like PSNR and SSIM reward pixel-perfect reconstruction, often favoring "copy-paste" artifacts over genuine diffusion-based erasure.
> 2.  **No-Reference Blind Spots:** Existing metrics like ReMOVE and CFD often fail to penalize blurred regions, sometimes even scoring them higher than unedited inputs.
> 3.  **Temporal Insensitivity:** Current temporal metrics operate on full-frame features, making them largely blind to small, localized artifacts within the edited region.

## RC-S 与 RC-T：方法论

> ## RC-S and RC-T: The Methodology

PROVE 将范式从全局聚合转变为了**深度特征空间中的局部分布匹配**。

> PROVE shifts the paradigm from global aggregation to **local distribution matching in deep feature space.**

*   **RC-S（空间一致性）：** 使用连通域分析来隔离目标。滑动窗口利用 DINOv2 嵌入计算掩码区域与局部背景特征之间的 MMD。
*   **RC-T（时间一致性）：** 通过裁剪其掩码的并集并计算交集内的 MMD 来评估相邻帧，确保专门在发生恢复的位置衡量时间一致性。

> *   **RC-S (Spatial):** Uses connected-component analysis to isolate targets. A sliding window computes the MMD between masked regions and local background features using DINOv2 embeddings.
> *   **RC-T (Temporal):** Evaluates adjacent frames by cropping the union of their masks and computing MMD within the intersection, ensuring that temporal consistency is measured specifically where the restoration occurs.

## 实验结果

> ## Results

与现有基准相比，PROVE 表现出与人类判断更优越的相关性：

> PROVE demonstrates superior correlation with human judgment compared to existing benchmarks:

*   **人类相关性：** RC-S 达到了 **0.59 的平均肯德尔 τ 系数（Kendall’s τ）**，显著优于 ReMOVE（0.26）和 CFD（0.16）。
*   **鲁棒性：** 在扰动测试（如模糊）中，RC-S 100% 的情况下更偏爱干净的图像，而竞品则频繁失效。
*   **效率：** RC-S 比 CFD 快 13.7 倍。

> *   **Human Correlation:** RC-S achieves **0.59 average Kendall’s τ**, significantly outperforming ReMOVE (0.26) and CFD (0.16).
> *   **Robustness:** In perturbation tests (e.g., blurring), RC-S prefers clean images 100% of the time, whereas competitors frequently fail.
> *   **Efficiency:** RC-S is 13.7× faster than CFD.

## PROVE-Bench 基准测试

> ## PROVE-Bench

该基准测试包含两个不同的层级：

> The benchmark consists of two distinct tiers:

*   **PROVE-M：** 80 个配对的、经过运动增强的视频（三脚架拍摄），带有高质量、经帧精炼的 SAM3 掩码。
*   **PROVE-H：** 100 个“困难”的真实世界视频（包含人群、流动的水、快速运动），没有真实标准（ground truth），旨在对模型的鲁棒性进行压力测试。

> *   **PROVE-M:** 80 paired, motion-augmented videos (tripod-captured) with high-quality, frame-refined SAM3 masks.
> *   **PROVE-H:** 100 "hard" real-world videos (crowds, flowing water, fast motion) without ground truth, designed to stress-test model robustness.

---

## 核心要点

> ## Key Takeaways

*   **无需参考：** RC-S 和 RC-T 不需要真实视频作为参考，这使其非常适合真实世界的生产环境。
*   **卓越的准确性：** RC-S 提供了与人类排名高达 0.59 的 Kendall’s τ 相关性，远超当前的行业标准。
*   **高效性：** 高性能评估，适用于 CI/CD 流水线和大规模模型比拼。
*   **开源：** 项目可通过 [GitHub](https://github.com/xiaomi-research/prove) 获取，数据集托管在 [Hugging Face](https://huggingface.co/datasets/HigherHu/PROVE-Bench)。

> *   **Reference-Free:** RC-S and RC-T do not require ground truth videos, making them ideal for real-world production environments.
> *   **Superior Accuracy:** RC-S provides a 0.59 Kendall’s τ correlation with human rankings, far exceeding current industry standards.
> *   **Efficiency:** High-performance evaluation suitable for CI/CD pipelines and large-scale model bake-offs.
> *   **Open Source:** The project is available via [GitHub](https://github.com/xiaomi-research/prove), with datasets hosted on [Hugging Face](https://huggingface.co/datasets/HigherHu/PROVE-Bench).

---

*欲了解更多详情，请访问[项目主页](https://xiaomi-research.github.io/prove/)或阅读[论文](https://arxiv.org/abs/2605.14534)。*

> *For more details, visit the [Project Page](https://xiaomi-research.github.io/prove/) or read the [Paper](https://arxiv.org/abs/2605.14534).*