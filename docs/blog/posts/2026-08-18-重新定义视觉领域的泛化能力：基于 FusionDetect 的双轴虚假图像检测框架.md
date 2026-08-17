---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-18
hide:
- navigation
tags:
- 虚假图像检测
- 计算机视觉
- 深度学习
- FusionDetect
- OmniGen
title: 重新定义视觉领域的泛化能力：基于 FusionDetect 的双轴虚假图像检测框架
---
### 文章背景与核心概要
随着生成式人工智能的爆发式增长，业界迫切需要强大的合成图像检测方法。当前的研究主要集中在“跨生成器”的泛化能力上，而本文指出，“跨域（cross-domain）”泛化能力同样至关重要。为了解决这一问题，作者推出了 **Fusion`Detect** 这一创新框架，它利用了来自两个冻结基础模型（**CLIP** 和 **Dinov2**）的内聚特征空间。通过结合这些互补模型，FusionDetect 对内容和生成器设计都实现了极佳的适应性。

此外，该研究还引入了 **OmniGen Benchmark**（全能生成基准），这是一个包含 12 个先进生成器的综合数据集，用于在现实且多样化的条件下评估检测器的性能。该论文在准确率和精确度上均超越了现有模型，展现出对抗常见图像扰动的卓越鲁棒性。

> ### 文章背景与核心概要
> The proliferation of generative AI has necessitated robust methods for synthetic image detection. While current research primarily focuses on "cross-generator" generalization, this paper argues that "cross-domain" generalization is equally critical. To address this, the authors introduce **FusionDetect**, a novel framework that leverages a cohesive feature space derived from two frozen foundation models—**CLIP** and **Dinov2**. By combining these complementary models, FusionDetect achieves superior adaptability to both content and generator design. The study also introduces the **OmniGen Benchmark**, a comprehensive dataset featuring 12 state-of-the-art generators, to evaluate detector performance under realistic, diverse conditions.

---

# Redefining Generalization in Visual Domains: ATwo-Axis Framework for Fake Image Detection with FusionDetect

> # Redefining Generalization in Visual Domains: A Two-Axis Framework for Fake Image Detection with FusionDetect

**Authors:** Amirtaha Amanzadi, Zahra Dehghanian, Hamid Beigy, Hamid R. Rabiee  
**arXiv:** [2510.05740](https://arxiv.org/abs/2510.05740) [cs.CV]  
**Submitted:** 7 Oct 2025 (v1), 14 Aug 2026 (v2)

> **Authors:** Amirtaha Amanzadi, Zahra Dehghanian, Hamid Beigy, Hamid R. Rabiee  
> **arXiv:** [2510.05740](https://arxiv.org/abs/2510.05740) [cs.CV]  
> **Submitted:** 7 Oct 2025 (v1), 14 Aug 2026 (v2)

---

## Summary

> ## Summary

生成式 AI 的泛滥使得构建可靠的合成图像检测方法变得必不可少。尽管目前的研究主要集中在“跨生成器”（cross-generator）的泛化能力上，但本文认为“跨域”（cross-domain）泛化同样至关重要。为了应对这一挑战，作者引入了 **FusionDetect**，这是一个新颖的框架，它利用了来自两个冻结基础模型（**CLIP** 和 **Dinov2**）的内聚特征空间。通过结合这些互补的模型，FusionDetect 对内容和生成器设计均实现了卓越的适应性。该研究还推出了 **OmniGen Benchmark**，这是一个包含 12 个最先进生成器的综合数据集，用于评估检测器在真实且多样化条件下的性能。

> The proliferation of generative AI has necessitated robust methods for synthetic image detection. While current research primarily focuses on "cross-generator" generalization, this paper argues that "cross-domain" generalization is equally critical. To address this, the authors introduce **FusionDetect**, a novel framework that leverages a cohesive feature space derived from two frozen foundation models—**CLIP** and **Dinov2**. By combining these complementary models, FusionDetect achieves superior adaptability to both content and generator design. The study also introduces the **OmniGen Benchmark**, a comprehensive dataset featuring 12 state-of-the-art generators, to evaluate detector performance under realistic, diverse conditions.

---

## Key Contributions

> ## Key Contributions

*   **双轴泛化框架：** 作者通过同时解决跨生成器和跨域泛化问题，重新定义了虚假图像检测的问题。
*   **FusionDetect 方法：** 一种全新的检测架构，它融合了 CLIP 和 Dinov2 的特征，构建出一个强大且统一的特征空间。
*   **OmniGen 基准：** 一个整合了 12 个最先进生成模型的新评估标准，用于在真实世界场景中测试检测器的性能。
*   **最先进的性能表现：** 
    *   在现有基准上，准确率提升了 **3.87%**，精确度提升了 **6.13%**。
    *   在全新的 OmniGen 基准上，准确率提升了 **4.48%**。
    *   展现出对常见图像扰动的杰出鲁棒性。

> *   **Two-Axis Generalization Framework:** The authors redefine the problem of fake image detection by addressing both cross-generator and cross-domain generalization.
> *   **FusionDetect Method:** A new detection architecture that fuses features from CLIP and Dinov2 to create a robust, unified feature space.
> *   **OmniGen Benchmark:** A new evaluation standard incorporating 12 state-of-the-art generative models to test detector performance in real-world scenarios.
> *   **State-of-the-Art Performance:** 
>     *   Outperforms existing models by **3.87% in accuracy** and **6.13% in precision** on established benchmarks.
>     *   Achieves a **4.48% increase in accuracy** on the new OmniGen benchmark.
>     *   Demonstrates exceptional robustness against common image perturbations.

---

## Resources & Links

> ## Resources & Links

*   **项目代码与数据集：** [GitHub 仓库](http://github.com/amir-aman/FusionDetect)
*   **完整论文 (PDF)：** [查看 PDF](https://arxiv.org/pdf/2510.05740)
*   **实验 HTML：** [查看 HTML](https://arxiv.org/html/2510.05740v2)
*   **DOI：** [10.48550/arXiv.2510.05740](https://doi.org/10.48550/arXiv.2510.05740)

> *   **Project Code & Dataset:** [GitHub Repository](http://github.com/amir-aman/FusionDetect)
> *   **Full Paper (PDF):** [View PDF](https://arxiv.org/pdf/2510.05740)
> *   **Experimental HTML:** [View HTML](https://arxiv.org/html/2510.05740v2)
> *   **DOI:** [10.48550/arXiv.2510.05740](https://doi.org/10.48550/arXiv.2510.05740)

---

## Subjects

> ## Subjects

*   **主分类：** 计算机视觉与模式识别 (cs.CV)
*   **次分类：** 人工智能 (cs.AI)

> *   **Primary:** Computer Vision and Pattern Recognition (cs.CV)
> *   **Secondary:** Artificial Intelligence (cs.AI)