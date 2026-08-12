---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-12
hide:
- navigation
tags:
- 具身智能
- 空间认知
- 变形测试
- 多模态大模型
- 评测基准
title: MetaSpace：面向具身智能体空间认知的变形测试框架
---
### 文章背景与核心概要
评估与物理环境交互的具身智能体（Embodied Agents）传统上依赖于劳动密集型的视觉问答（VQA）对或高层次的任务完成指标。然而，这些方法往往掩盖了关键的漏洞、低效性以及安全风险。为了应对任务执行过程中对稳健空间认知的根本需求，本文引入了 **MetaSpace**，这是一个受软件工程中变形测试（Metamorphic Testing）原则启发的新型评估框架。

MetaSpace 利用基于物理定律和逻辑规则预定义的变形关系（MRs，并在 Prolog 中编码为可执行规则），从实际执行轨迹中自动生成测试用例。在三个具身场景中，MetaSpace 成功识别了当前最先进（SOTA）的多模态大模型（MLLM）驱动智能体中的 90,422 个空间认知错误。为了量化性能，作者引入了**空间认知（SC）得分**，其中 SOTA 智能体的平均得分在 0.44 到 0.52 之间——远远落后于 0.96 的人类基准。

---

## 摘要 (Abstract)

具身智能体是一种通过实体与环境进行交互的智能实体。目前，具身智能体的评估主要依赖于两种范式：
1. 手工标注的视觉问答（VQA）对，以及
2. 高层次的任务完成指标，例如导航或操作的成功率。

前者耗费大量人力且易受标注质量波动的影响；后者则可能掩盖关键漏洞，允许智能体通过次优手段或违反安全规范的方式完成任务，从而隐藏安全风险与低效问题。鉴于空间认知是执行具身任务的基石，迫切需要评估具身智能体在任务执行期间是否具备稳健的空间认知。

受软件工程中变形测试原则的启发，我们提出了 **MetaSpace**，这是一个旨在评估智能体空间认知的新型框架。通过利用从实际执行轨迹中获取的时空多模态状态，MetaSpace 基于植根于逻辑规则和物理定律的预定义变形关系（MRs）自动生成测试用例。至关重要的是，我们将这些 MRs 编码为逻辑编程语言（Prolog）中的可执行规则。这些关系的违背即表明空间认知出现了故障。

我们在三个具身场景中进行的实证评估表明，MetaSpace 成功检测出最先进（SOTA）MLLM 驱动智能体中的 **90,422 个空间认知错误**。我们引入了**空间认知（SC）得分**来量化性能。结果表明，所有 SOTA 智能体的平均得分均在 **0.44 到 0.52** 之间，显著低于 **0.96** 的人类基准。

> An embodied agent is an intelligent entity that interacts with its environment through a physical body. Currently, the evaluation of embodied agents primarily relies on two paradigms: 
> 1. Manually annotated Visual Question Answering (VQA) pairs, and 
> 2. High-level task completion metrics, such as success in navigation or manipulation. 
> 
> The former is labor-intensive and subject to variability in annotation quality. The latter may obscure critical vulnerabilities, allowing agents to complete tasks through suboptimal means or safety violations, thereby concealing safety risks and inefficiencies. Given that spatial cognition is the cornerstone for executing embodied tasks, there is a pressing need to assess whether embodied agents possess robust spatial cognition during task execution.
> 
> Inspired by metamorphic testing principles in software engineering, we propose **MetaSpace**, a novel framework designed to evaluate the spatial cognition of agents. By leveraging spatiotemporal multimodal states derived from real execution trajectories, MetaSpace automatically generates test cases based on predefined metamorphic relations (MRs) grounded in logical rules and physical laws. Crucially, we encode these MRs as executable rules in a logic programming language (Prolog). Violations of these relations indicate failures in spatial cognition. 
> 
> Our empirical evaluation across three embodied scenarios demonstrates that MetaSpace successfully detects **90,422 spatial cognition errors** in state-of-the-art (SOTA) MLLM-driven agents. We introduce the **Spatial Cognition (SC) score** to quantify performance. Results indicate that all SOTA agents achieve average scores between **0.44 and 0.52**, significantly lower than the human benchmark of **0.96**.

---

## 文档元数据 (Document Metadata)

| 元数据字段 (Metadata Field) | 详情 (Details) |
| :--- | :--- |
| **arXiv ID** | [`arXiv:2608.07533`](https://arxiv.org/abs/2608.07533) [cs.AI] |
| **标题 (Title)** | MetaSpace: Metamorphic Testing for Spatial Cognition in Embodied Agents |
| **作者 (Authors)** | Gengyang Xu, Dongwei Xiao, Yiteng Peng, Shuai Wang |
| **提交日期 (Submitted On)** | 2026年7月26日 |
| **研究主题 (Subjects)** | 人工智能 (`cs.AI`)；软件工程 (`cs.SE`) |
| **期刊引用 (Journal Reference)** | Proceedings of the ACM on Programming Languages, Vol. 10, OOPSLA1 (April 2026), pp. 343–372 |
| **DOI** | [10.1145/3798212](https://doi.org/10.1145/3798212) |

> | Metadata Field | Details |
> | :--- | :--- |
> | **arXiv ID** | [`arXiv:2608.07533`](https://arxiv.org/abs/2608.07533) [cs.AI] |
> | **Title** | MetaSpace: Metamorphic Testing for Spatial Cognition in Embodied Agents |
> | **Authors** | Gengyang Xu, Dongwei Xiao, Yiteng Peng, Shuai Wang |
> | **Submitted On** | July 26, 2026 |
> | **Subjects** | Artificial Intelligence (`cs.AI`); Software Engineering (`cs.SE`) |
> | **Journal Reference** | Proceedings of the ACM on Programming Languages, Vol. 10, OOPSLA1 (April 2026), pp. 343–372 |
> | **DOI** | [10.1145/3798212](https://doi.org/10.1145/3798212) |

---

## 全文与资源 (Full-Text & Resources)

* **PDF 版本：** [查看 PDF](https://arxiv.org/pdf/2608.07533)
* **HTML 版本：** [HTML（实验性）](https://arxiv.org/html/2608.07533v1)
* **源码文件：** [TeX 源码](https://arxiv.org/src/2608.07533)
* **开源许可：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> * **PDF Version:** [View PDF](https://arxiv.org/pdf/2608.07533)
> * **HTML Version:** [HTML (experimental)](https://arxiv.org/html/2608.07533v1)
> * **Source Files:** [TeX Source](https://arxiv.org/src/2608.07533)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

---

## 引用与参考文献工具 (Citation & Reference Tools)

* **BibTeX 引用：** 可通过 arXiv 摘要页面或交互式文献目录探索工具获取。
* **外部引用：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07533) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07533) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.07533)

> * **BibTeX Citation:** Available via the arXiv abstract page or interactive bibliographic explorer tools.
> * **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.07533) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.07533) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.07533)