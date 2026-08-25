---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 科学智能体
- 地球系统
- 基准测试
- 自然灾害
- 人工智能
title: EarthVerse：跨动态地球系统与自然灾害的科学智能体基准测试
---
### 文章背景与核心概要
地球系统分析需要利用在来源、尺度、时间和模态上各不相同的异构观测数据来重建不断变化的物理过程。自然灾害的存在进一步放大了这一挑战的利害关系，因为不完整的证据可能会严重扭曲对灾害严重程度、暴露度以及物理机制的评估。

为了检验人工智能系统处理这些复杂问题的能力，本文作者推出了 **EarthVerse**——一个用于通过包范围调查（package-scoped investigations）评估科学智能体的综合基准测试。EarthVerse 建立在 199 个记录在案的事件和 19 个灾害类别基础之上，包含 **405 个可复现任务**，旨在测试智能体在以下方面的能力：检查复杂的事件包、选择兼容的证据、执行透明的计算、调和不同数据源之间的差异，并在最终答案中保持科学溯源性。

---

# EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards

**arXiv ID:** [2608.23525](https://arxiv.org/abs/2608.23525)  
**Primary Subject:** Artificial Intelligence (`cs.AI`)  
**Submitted:** August 24, 2026  
**Authors:** Zhiqing Cui, Xinxiang Yin, Yihong Tang, Xinglang Zhang, Yuanzhe Hu, Siru Zhong, Weidong Tang, Yuxuan Liang, Weijia Li, Ming Jin, Shirui Pan, Yuhao Kang, Dingyi Zhuang, Jinhua Zhao  

> Earth-system analysis requires reconstructing changing physical processes using heterogeneous observations that vary by source, scale, timing, and modality. Natural hazards heighten the stakes of this challenge, as incomplete evidence can severely distort estimates of severity, exposure, and physical mechanisms. 
> 
> To address how well AI systems handle these complexities, the authors introduce **EarthVerse**, a comprehensive benchmark for evaluating scientific agents through package-scoped investigations. Grounded in 199 documented events and 19 hazard families, EarthVerse features **405 reproducible tasks** that test an agent's ability to:
> * Inspect complex event packages
> * Select compatible evidence
> * Execute transparent calculations
> * Reconcile discrepancies between data sources
> * Preserve scientific provenance in final answers

---

## 🛠️ 基准测试设计与方法论

EarthVerse 提供了一个可执行的基础真值（ground truth），将每个任务分解为细粒度的答案单元。它采用了专门设计的任务评估标准（rubrics），旨在评估底层研究过程，同时保持足够的灵活性以适应多种有效的解题路径。

> ## 🛠️ Benchmark Design & Methodology
> 
> EarthVerse provides an executable ground truth that decomposes each task into fine-grained answer units. It utilizes task-specific rubrics designed to evaluate the underlying research process while remaining flexible enough to accommodate multiple valid problem-solving paths.

### 关键评估结果
作者在受控的工具使用协议下评估了 **25 个模型与智能体系统**，发现其性能存在显著差距：
* **平均答案单元准确率（Mean Answer-Unit Accuracy）：** 顶尖系统最高达到 **84.65%**。
* **Strict@95 准确率：** 暴跌至最高 **34.81%**。

这一巨大的性能差距表明，尽管当前的人工智能智能体能够成功完成孤立的、单个的步骤，但它们在跨证据类型、物理尺度、单位、计算以及整体科学解释时，始终难以保持连贯且可靠的推理链。最终，EarthVerse 为衡量动态地球系统中端到端科学可靠性提供了一个强大且可复现的标准。

> ### Key Evaluation Findings
> The authors evaluated **25 model and agent systems** under a controlled tool-using protocol, identifying significant gaps in performance:
> * **Mean Answer-Unit Accuracy:** Reached up to **84.65%** across top-performing systems.
> * **Strict@95 Accuracy:** Dropped drastically to a maximum of **34.81%**.
> 
> This stark performance gap indicates that while current AI agents can successfully complete isolated, individual steps, they consistently struggle to maintain a coherent, reliable chain of reasoning across evidence types, physical scales, units, calculations, and overall scientific interpretation. EarthVerse ultimately provides a robust, reproducible standard for measuring end-to-end scientific reliability in dynamic Earth systems.

---

## 🔗 链接与资源

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2608.23525) | [实验性 HTML](https://arxiv.org/html/2608.23525v1) | [TeX 源码](https://arxiv.org/src/2608.23525)
* **数字对象唯一标识符 (DOI)：** [10.48550/arXiv.2608.23525](https://doi.org/10.48550/arXiv.2608.23525)
* **许可协议：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)

> ## 🔗 Links & Resources
> 
> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.23525) | [Experimental HTML](https://arxiv.org/html/2608.23525v1) | [TeX Source](https://arxiv.org/src/2608.23525)
> * **Digital Object Identifier (DOI):** [10.48550/arXiv.2608.23525](https://doi.org/10.48550/arXiv.2608.23525)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)