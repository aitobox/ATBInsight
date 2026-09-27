---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-25
hide:
  - navigation
tags:
  - QuantWM
  - 世界模型
  - 视频生成
  - KV Cache 量化
  - 时序一致性
  - arXiv论文
title: "QuantWM：面向世界模型与视频生成的时序一致性 2-Bit KV Cache 量化技术"
---

### 文章背景与核心概要
在视频生成与物理世界模型中，用于保存历史上下文的键值缓存 (KV Cache) 显存开销随着生成时长的增加而急剧膨胀，成为模型在实际部署中的关键瓶颈。尽管现有的 2-bit KV Cache 极限量化方案在静态基准测试 (如 VBench) 上表现优异，但在实际视频生成中仍频繁出现严重的画面闪烁与时序不一致问题。针对这一难题，新加坡管理大学等机构的研究团队深入探究了注意力机制的误差分布特性，提出了严格因果且免训练的 2-bit KV Cache 量化框架 —— QuantWM。该方案创新性地结合量化敏感度感知聚类 (QSAC) 与主子空间注意力补偿 (PSAC) 算法，精准稳定了注意力输出并锁定时空 Token 选取。实验表明，QuantWM 在实现高达 6.20 倍显存压缩的同时显著提升了生成画面的时序连贯性与视觉品质，为长视频实时生成与具身智能世界模型的高效落地提供了强大的技术支撑。

---

# QuantWM：面向世界模型与视频生成的时序一致性 2-Bit KV Cache 量化技术

> # QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation

**作者：** Jiaqi Zhao, Xiaobin Hu, Bo Yin, Junpeng Jiang, Miao Zhang, Shuicheng Yan  
**研究领域：** 计算机视觉与模式识别 (`cs.CV`)；人工智能 (`cs.AI`)  
**arXiv：** [2609.26425 [cs.CV]](https://arxiv.org/abs/2609.26425) | **DOI：** [10.48550/arXiv.2609.26425](https://doi.org/10.48550/arXiv.2609.26425)  
**提交历史：** 于 2026 年 9 月 22 日提交；最后修订于 2026 年 9 月 23 日 (v2)。

> **Authors:** Jiaqi Zhao, Xiaobin Hu, Bo Yin, Junpeng Jiang, Miao Zhang, Shuicheng Yan  
> **Subjects:** Computer Vision and Pattern Recognition (`cs.CV`); Artificial Intelligence (`cs.AI`)  
> **arXiv:** [2609.26425 [cs.CV]](https://arxiv.org/abs/2609.26425) | **DOI:** [10.48550/arXiv.2609.26425](https://doi.org/10.48550/arXiv.2609.26425)  
> **Submission History:** Submitted on 22 Sep 2026; last revised 23 Sep 2026 (v2).

---

## 📌 内容概要

> ## 📌 Summary

对于现代视频生成大模型与世界模型而言，键值缓存 (Key-Value Cache, KV Cache) 极其庞大的显存开销已成为落地部署的核心瓶颈。尽管现有的 2-bit KV Cache 量化技术在诸如 VBench 等标准基准测试 (Benchmark) 中看似取得了“近乎无损”的分数，但在实际生成连续视频时，画面依然存在严重的**时序闪烁**与**画质劣化**。

> Key-Value (KV) cache memory is a significant deployment bottleneck for modern video generation models and world models. While existing 2-bit KV cache quantization methods achieve near-lossless performance on standard benchmarks (such as VBench), they still suffer from severe **temporal flickering** and **visual degradation**. 

**核心发现与洞察：**

> **Key Findings & Insights:**

* **Key 与 Value 扰动对比：** 深入分析表明，尽管 Key 向量量化带来的数值重构误差实际上小于 Value 向量，但令人意外的是，它所引发的最终生成质量劣化反而要严重得多。
* **注意力机制的关键影响：** Key 向量中即便极其微小的量化扰动，也会直接改变注意力分数的计算结果 ($QK^\top$)，进而导致 Query 在检索历史信息时所选取的时空 Token 发生漂移，最终彻底打破了视频帧之间的时序一致性。

> * **Key vs. Value Perturbations:** Deeper investigations reveal that Key quantization produces smaller reconstruction errors than Value quantization, yet surprisingly leads to significantly larger output degradation. 
> * **The Role of Attention:** Small Key perturbations alter attention logits ($QK^\top$), shifting the temporal-spatial tokens selected by Queries and breaking temporal consistency.

**解决方案 (`QuantWM`)：**  
为了在无需重新训练模型的前提下，显式保护注意力分数与 Token 选取的准确性，作者团队推出了名为 **QuantWM** 的免训练、严格因果 2-bit KV Cache 量化框架。QuantWM 核心依赖两项相辅相成的关键技术：

> **Proposed Solution (`QuantWM`):**  
> To explicitly preserve attention logits and token selection without requiring model training, the authors introduce **QuantWM**, a training-free, strictly causal 2-bit KV cache quantization framework. QuantWM relies on two complementary techniques:

1. **量化敏感度感知聚类 (Quantization-Sensitivity-Aware Clustering, QSAC)：** 综合考量历史 Query 的敏感度分布与残差动态范围，精心筛选适合 INT2 表示的 Key 聚类质心，最大限度减少对注意力计算起决定性作用的敏感通道上的量化误差。
2. **主子空间注意力补偿 (Principal-Subspace Attention Compensation, PSAC)：** 通过低秩投影技术，沿着起主导作用的 Query 主子空间精确补偿 Key 的剩余量化误差，以极高的计算效率直接稳定注意力分数的输出。

> 1. **Quantization-Sensitivity-Aware Clustering (QSAC):** Jointly considers historical Query sensitivity and residual ranges to select INT2-friendly Key centroids, minimizing quantization errors in attention-critical channels.
> 2. **Principal-Subspace Attention Compensation (PSAC):** Restores remaining Key errors along the dominant Query subspace via low-rank projections, directly stabilizing attention logits efficiently.

---

## 🔬 实验结果

> ## 🔬 Experimental Results

在包括 **Causal-Forcing**、**LingBot-World-v2**、**HY-World 1.5**、**Matrix-Game-2** 以及 **Longcat-Video** 在内的多种业界主流架构上开展的广泛评估表明，`QuantWM` 能够：

> Extensive evaluations across multiple prominent architectures—including **Causal-Forcing**, **LingBot-World-v2**, **HY-World 1.5**, **Matrix-Game-2**, and **Longcat-Video**—demonstrate that `QuantWM`:

* 大幅改善生成视频的视觉品质与时序一致性；
* 在图像级与视频级质量评测指标上均全面超越现有方法；
* 在引入极小额外计算开销的前提下，实现高达 **6.20 倍的 KV Cache 显存压缩**。

> * Substantially improves visual quality and temporal consistency.
> * Outperforms existing methods across both image and video quality metrics.
> * Achieves up to **6.20× KV cache memory compression** with minimal additional computational overhead.

---

## 🔗 论文链接与相关资源

> ## 🔗 Links & Resources

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2609.26425) | [在线 HTML (实验性)](https://arxiv.org/html/2609.26425v2) | [TeX 源码](https://arxiv.org/src/2609.26425)
* **授权协议：** [知识共享署名 4.0 国际许可协议 (Creative Commons Attribution 4.0)](http://creativecommons.org/licenses/by/4.0/) *(根据说明保留下方协议图标)*：

<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2609.26425) | [HTML (Experimental)](https://arxiv.org/html/2609.26425v2) | [TeX Source](https://arxiv.org/src/2609.26425)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) *(License icon preserved below per instructions)*:
