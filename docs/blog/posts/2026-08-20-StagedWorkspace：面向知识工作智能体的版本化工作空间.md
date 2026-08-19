---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-20
hide:
- navigation
tags:
- AI Agent
- 知识工作
- 版本控制
- 工作空间
- 大模型评测
title: StagedWorkspace：面向知识工作智能体的版本化工作空间
---
### 文章背景与核心概要
在当前的AI应用中，智能体（Agents）越来越多地被用于处理复杂的知识工作，例如生成和修改持久化的数字工件（如代码库、文档、电子表格、幻灯片和报告）。然而，实际操作中往往存在一个严重的割裂问题：智能体搜索时解析出的视图、它们编辑的本地原生文件、它们审查的修改内容，以及它们最终提交的工件，常常指向同一工作产品的不同且未同步的版本。

为了解决这一痛点，本文作者推出了 **StagedWorkspace**，这是一个专为知识工作智能体设计的版本化工作空间框架。该框架将解析记录和审查差异直接绑定到演进中的原生文件的内容哈希上。在 *OfficeQA Pro* 和 *APEX-Agents* 上的实验评估表明，双解析/原生访问模式显著优于单一视图的局限性，在多个模型上大幅提升了任务通过率和评分标准（rubric）得分。

---

## StagedWorkspace: A Versioned Workspace for Knowledge-Work Agents

**arXiv:** [2608.18050 [cs.AI]]  
**DOI:** [10.48550/arXiv.2608.18050](https://doi.org/10.48550/arXiv.2608.18050)  
**Submitted:** August 18, 2026 (Under Review)  
**Authors:** Yining Hua, Hongbin Na, Yifan Zhou, Akshay Kalose, Cyrus Ayubcha, Levi Lian  

> **arXiv:** [2608.18050 [cs.AI]]  
> **DOI:** [10.48550/arXiv.2608.18050](https://doi.org/10.48550/arXiv.2608.18050)  
> **Submitted:** August 18, 2026 (Under Review)  
> **Authors:** Yining Hua, Hongbin Na, Yifan Zhou, Akshay Kalose, Cyrus Ayubcha, Levi Lian  

---

## Executive Summary

AI agents are increasingly used for knowledge work, such as producing and modifying persistent digital artifacts like code repositories, documents, spreadsheets, slides, and reports. However, a major disconnect often occurs: the parsed views agents search, the native files they edit, the changes they review, and the final artifacts they submit frequently refer to different, unsynchronized versions of the same work product. 

To solve this, the authors introduce **StagedWorkspace**, a versioned workspace framework that binds parsed records and review diffs directly to the content hashes of native files as they evolve. Experimental evaluations on *OfficeQA Pro* and *APEX-Agents* demonstrate that dual parsed/native access significantly outperforms single-view limitations, substantially boosting pass rates and rubric scores across multiple models.

> ## 执行摘要
> 
> 人工智能智能体正越来越多地被用于知识工作，例如生产和修改持久化的数字工件，如代码仓库、文档、电子表格、幻灯片和报告。然而，经常会出现一个主要的割裂现象：智能体搜索的解析视图、它们编辑的原生文件、它们审查的变更以及它们最终提交的工件，往往指向同一工作产品的不同且未同步的版本。
> 
> 为了解决这个问题，作者推出了 **StagedWorkspace**，这是一个版本化的工作空间框架，它将解析后的记录和审查差异直接绑定到随着演进的原生文件的内容哈希上。在 *OfficeQA Pro* 和 *APEX-Agents* 上的实验评估表明，双解析/原生访问显著优入了单视图的局限性，在多个模型中大幅提升了通过率和评分标准（rubric）得分。

---

## Abstract

AI agents increasingly perform knowledge work (i.e., produce and modify persistent digital artifacts such as code repositories, documents, spreadsheets, slides, reports), yet the parsed views they search, the native files they edit, the changes they review, and the artifacts they submit can refer to different versions of the same work product. 

We formulate this as a **workspace-state contract**: every view should be explicitly tied to a version of the evolving workspace state. Coding agents partly address this need through repository contracts for search, diffs, and tests, whereas an analogous contract is less explicit for PDFs, spreadsheets, slides, notebooks, and mixed-format project folders. 

We propose **StagedWorkspace**, a versioned workspace for knowledge-work agents. The workspace binds parsed records and review diffs to content hashes of the native files as they change. 

> ## 摘要
> 
> AI智能体越来越多地执行知识工作（即生产和修改持久的数字工件，如代码仓库、文档、电子表格、幻灯片、报告），然而它们搜索的解析视图、编辑的原生文件、审查的变更以及提交的工件可能会指向同一工作产品的不同版本。
> 
> 我们将其定义为一个**工作空间状态契约（workspace-state contract）**：每个视图都应该显式地绑定到演进中的工作空间状态的一个版本。编程智能体通过用于搜索、差异对比和测试的仓库契约部分满足了这一需求，而对于PDF、电子表格、幻灯片、记事本和混合格式的项目文件夹，类似的契约则不够明确。
> 
> 我们提出了 **StagedWorkspace**，一个面向知识工作智能体的版本化工作空间。该工作空间将解析记录和审查差异绑定到随其变化的原生文件的内容哈希上。

### Key Findings & Results
* **Performance Boost:** In fixed-harness ablations on *OfficeQA Pro* and *APEX-Agents*, dual parsed/native access achieved the highest point estimate for every tested model. 
* **Metric Improvements:** Relative to more limiting single views, StagedWorkspace improves:
  * **OfficeQA Pass@1** by **8.3–12.1 points**.
  * **APEX mean rubric score** by **4.7–9.2 points**.
* **Benchmark Comparisons:** 
  * `SW-AGENT` scores **63.9%** with *Gemini 3.1 Pro* on OfficeQA (compared to a published same-model score of 29.3%).
  * `SW-AGENT` scores **42.1** with *GPT-5.4 Nano* on APEX (compared to a published same-model score of 25.5).
* **Review-Axis Ablation:** A paired ablation on 57 file-editing tasks revealed higher observed scores when change diffs are visible.

These results establish workspace state as a crucial experimental variable in knowledge-work agents, encouraging future benchmarks to score evidence, staged edits, and submitted artifacts as explicit state transitions.

> ### 关键发现与结果
> * **性能提升：** 在 *OfficeQA Pro* 和 *APEX-Agents* 的固定框架消融实验中，双解析/原生访问在所有测试模型中均取得了最高点估计。
> * **指标改进：** 与限制更多的单视图相比，StagedWorkspace 实现了以下提升：
>   * **OfficeQA Pass@1** 提升了 **8.3–12.1 个百分点**。
>   * **APEX 平均评分标准得分** 提升了 **4.7–9.2 分**。
> * **基准测试对比：**
>   * `SW-AGENT` 在 OfficeQA 上配合 *Gemini 3.1 Pro* 获得了 **63.9%** 的分数（相比之下，已发表的同模型得分为 29.3%）。
>   * `SW-AGENT` 在 APEX 上配合 *GPT-5.4 Nano* 获得了 **42.1** 的分数（相比之下，已发表的同模型得分为 25.5）。
> * **审查轴消融实验：** 对 57 个文件编辑任务进行的成对消融实验表明，当变更差异（diffs）可见时，观察到的得分更高。
> 
> 这些结果确立了工作空间状态作为知识工作智能体中一个至关重要的实验变量，鼓励未来的基准测试将证据、阶段性编辑和提交的工件作为显式的状态转换进行评分。

---

## Metadata & Links

* **Primary Subject:** Artificial Intelligence (`cs.AI`)
* **Full-Text & Access Options:**
  * [View PDF](https://arxiv.org/pdf/2608.18050)
  * [HTML Version (Experimental)](https://arxiv.org/html/2608.18050v1)
  * [TeX Source](https://arxiv.org/src/2608.18050)
  * [License](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)
* **External Bibliographic Tools:**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.18050)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.18050)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.18050)

> ## 元数据与链接
> 
> * **主要主题：** 人工智能 (`cs.AI`)
> * **全文与访问选项：**
>   * [查看 PDF](https://arxiv.org/pdf/2608.18050)
>   * [HTML 版本（实验性）](https://arxiv.org/html/2608.18050v1)
>   * [TeX 源码](https://arxiv.org/src/2608.18050)
>   * [许可证](http://arxiv.org/licenses/nonexclusive-distrib/1.0/)
> * **外部文献计量工具：**
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.18050)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.18050)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.18050)