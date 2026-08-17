---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-18
hide:
- navigation
tags:
- 多模态RAG
- 信息检索
- 文档结构理解
- 大语言模型
- 知识检索
title: HAM-RAG：面向结构保真交错生成的层级感知多模态RAG
---
### 文章背景与核心概要

现有的多模态检索增强生成（RAG）系统通常将结构化文档扁平化处理为孤立的文本和图像单元。这种降维处理削弱了原始文档的组织结构以及准确选择和放置证据所必需的局部图文上下文。为了解决这一局限性，本文作者推出了 **HAM-RAG**（层级感知多模态RAG），这是一个专为结构保真交错生成设计的新型框架。HAM-RAG 在检索和生成阶段均将文档层级作为主要的基准定位信号，通过这种方式，它不仅能够使图文证据更具上下文关联性，还能直接在提示词中保留源文档的位置信息和局部关系。

此外，该论文还推出了 **HAM-Bench**，这是一个涵盖悟空（Wukong）、维基（Wiki）、arXiv 和食谱（Recipe）数据集的综合基准测试，横跨游戏攻略、网页、科学论文和分步食谱等多种场景。实验表明，HAM-RAG 的多模态平均准确率较最强的非层级基线提升了 **17.3%**，并在局部图文对齐方面展现出卓越的性能，证明了其在技术手册、维护指南和工业标准操作程序（SOP）等依赖结构化文档的应用场景中的强大可靠性。

> Existing multimodal Retrieval-Augmented Generation (RAG) systems typically flatten structured documents into isolated text and image units. This reduction weakens the original document organization and local text-image context necessary for accurate evidence selection and placement. 
> 
> To address this limitation, the authors introduce **HAM-RAG** (Hierarchy-Aware Multimodal RAG), a novel framework designed for structure-faithful interleaved generation. HAM-RAG leverages document hierarchy as a primary grounding signal during both retrieval and generation stages. By doing so, it contextualizes textual and visual evidence while preserving source positioning and local relationships directly within the prompt. 
> 
> Additionally, the paper introduces **HAM-Bench**, a comprehensive benchmark spanning Wukong, Wiki, arXiv, and Recipe datasets across game walkthroughs, web pages, scientific papers, and step-wise recipes.

---

# HAM-RAG: Hierarchy-Aware Multimodal RAG for Structure-Faithful Interleaved Generation

> # HAM-RAG: Hierarchy-Aware Multimodal RAG for Structure-Faithful Interleaved Generation

**arXiv ID:** [2608.14032](https://arxiv.org/abs/2608.14032) [cs.IR]  
**Submitted:** August 14, 2026  
**Authors:** Yin Li, Ziyang Hu, Zhiyu Guo, Xiangyu Liu, Wenbin Li, Boo-Ho Yang, Rav Lawana, Ziyue Li, Wei Zeng, Fugee Tsung  
**Links:** [View PDF](https://arxiv.org/pdf/2608.14032) | [HTML Version](https://arxiv.org/html/2608.14032v1) | [GitHub Repository](https://github.com/MCCodeAI/HAM-RAG.git)

> **arXiv ID:** [2608.14032](https://arxiv.org/abs/2608.14032) [cs.IR]  
> **Submitted:** August 14, 2026  
> **Authors:** Yin Li, Ziyang Hu, Zhiyu Guo, Xiangyu Liu, Wenbin Li, Boo-Ho Yang, Rav Lawana, Ziyue Li, Wei Zeng, Fugee Tsung  
> **Links:** [View PDF](https://arxiv.org/pdf/2608.14032) | [HTML Version](https://arxiv.org/html/2608.14032v1) | [GitHub Repository](https://github.com/MCCodeAI/HAM-RAG.git)

---

## 📌 Summary

> ## 📌 Summary

现有的大模型多模态检索增强生成（RAG）系统通常将结构复杂的文档切分为孤立的文本和图像片段。这种粗暴的简化破坏了文档原有的组织结构以及局部图文上下文，而这些上下文对于精准的证据选择和排版至关重要。

> Existing multimodal Retrieval-Augmented Generation (RAG) systems typically flatten structured documents into isolated text and image units. This reduction weakens the original document organization and local text-image context necessary for accurate evidence selection and placement. 

为了克服这一缺陷，作者提出了 **HAM-RAG**（层级感知多模态RAG）这一创新框架，专门用于实现结构保真的交错生成。HAM-RAG 在检索与生成两个关键阶段，均将文档的层级结构作为核心的对齐锚点。通过这种机制，它能够在提示词内部直接关联文本与视觉证据，同时完美保留源文档的空间位置以及局部的关联关系。

> To address this limitation, the authors introduce **HAM-RAG** (Hierarchy-Aware Multimodal RAG), a novel framework designed for structure-faithful interleaved generation. HAM-RAG leverages document hierarchy as a primary grounding signal during both retrieval and generation stages. By doing so, it contextualizes textual and visual evidence while preserving source positioning and local relationships directly within the prompt. 

此外，该论文还推出了 **HAM-Bench**，这是一个涵盖 Wukong、Wiki、arXiv 以及 Recipe 等多个数据集的综合性评测基准，广泛覆盖了游戏攻略、网页、学术论文和分步食谱等多种实际文档形态。

> Additionally, the paper introduces **HAM-Bench**, a comprehensive benchmark spanning Wukong, Wiki, arXiv, and Recipe datasets across game walkthroughs, web pages, scientific papers, and step-wise recipes.

### 核心发现与性能表现：
* **总体准确率：** 在多种底层模型（backbones）的测试中，相较于最强的非层级基线模型，HAM-RAG 的多模态平均准确率大幅提升了 **17.3%**。
* **局部对齐能力：** 在 Wukong 数据集上，HAM-RAG 的 *Img-CBS* 指标相较于最强非层级基线提升了 **24.2%**，充分证明了其卓越的局部图文对齐精度。
* **实际应用价值：** 在高度依赖结构化文档的业务场景中展现出极高的可靠性，例如技术手册、设备维护指南以及工业标准操作程序（SOP）。

> ### Key Findings & Performance:
> * **Overall Accuracy:** HAM-RAG improves the main multimodal average by **17.3%** over the strongest non-hierarchical baseline across multiple backbones.
> * **Local Alignment:** On the Wukong dataset, HAM-RAG improves *Img-CBS* by **24.2%** over the strongest non-hierarchical baseline, proving superior local text-image alignment.
> * **Practical Applications:** Demonstrates strong reliability for applications relying heavily on structured documents, such as technical manuals, maintenance guides, and industrial Standard Operating Procedures (SOPs).

---

## 📋 Additional Metadata

> ## 📋 Additional Metadata

* **主要学科：** 信息检索 (`cs.IR`)
* **次要学科：** 人工智能 (`cs.AI`)
* **DOI：** [10.48550/arXiv.2608.14032](https://doi.org/10.48550/arXiv.2608.14032)
* **开源许可：** [知识共享 署名-非商业性使用-禁止演绎 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-nd/4.0/)

> * **Primary Subject:** Information Retrieval (`cs.IR`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`)
> * **DOI:** [10.48550/arXiv.2608.14032](https://doi.org/10.48550/arXiv.2608.14032)
> * **License:** [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/)