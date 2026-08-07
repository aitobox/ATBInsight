---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-07
hide:
- navigation
tags:
- 语言模型
- 意第绪语
- 低资源语言
- COLM
- 评估基准
title: MameLoshnLM：意第绪语语言模型与评估基准
---
### 文章背景与核心概要
意第绪语（Yiddish）拥有着丰富深厚的文字传统，但由于可靠数字资源的匮乏，以及通用多语言语料库中充斥着大量充满噪声的机器翻译数据，其在数字建模领域长期面临诸多挑战。为了突破这一技术瓶颈，研究人员推出了专为意第绪语设计、拥有 80 亿参数的开源语言模型 **MameLoshnLM**，该论文已被 2026 年语言建模会议（COLM）录用。

为了实现这一目标，作者团队打造了两大核心资源：一是结合了现代网络原生内容与传统文学资料的高质量预训练语料库 **Oytser**；二是涵盖翻译、语言学分析、信息提取及语言理解的综合性多任务评估基准 **Kashes**。通过基于这些资源对 *Llama 3.1 8B* 进行持续预训练，MameLoshnLM 在同等规模的开源基线模型中脱颖而出，能够比通用多语言模型更精准地捕捉意第绪语独特的词汇和形态学模式，这不仅为意第绪语自然语言处理（NLP）奠定了坚实基础，也为历史上底蕴深厚但数字化表现不足的语言模型开发提供了实用的实践范例。

---

## 论文元数据 (Paper Metadata)

* **arXiv ID:** [arXiv:2608.05850](https://arxiv.org/abs/2608.05850) [cs.CL]
* **DOI:** [10.48550/arXiv.2608.05850](https://doi.org/10.48550/arXiv.2608.05850)
* **主学科 (Primary Subject):** 计算与语言 (`cs.CL`)
* **次学科 (Secondary Subjects):** 人工智能 (`cs.AI`)
* **发表会场 (Publication Venue):** 2026年语言建模会议 (COLM) 录用
* **提交日期 (Submission Date):** 2026年8月6日

## 作者 (Authors)
* Uri Katz
* Omer Goldman
* Tomasz Limisiewicz
* Reut Tsarfaty
* Noah A. Smith

---

## 摘要 (Abstract)

我们推出了 MameLoshnLM，这是第一个专门针对意第绪语构建的开源 8B 参数语言模型。尽管意第绪语拥有丰富的文字传统，但其有限的数字存在感以及可靠评估资源的稀缺，一直制约着意第绪语语言建模的进展。现有的多语言语料库和基准测试通常无法很好地代表该语言，其中包含大量带有噪声的、机器翻译的和错误分类的文本。我们通过引入 Oytser（一个结合了当代网络原生来源和文学材料的高质量意第绪语预训练语料库）以及 Kashes（一个涵盖翻译、语言学分析、信息提取和语言理解的多任务基准）来填补这些空白。利用这些资源，我们继续对 Llama 3.1 8B 进行预训练，获得了 MameLoshnLM。在基准测试的各项任务中，MameLoshnLM 的表现优于同等规模的开源基线。我们的分析表明，这些提升不仅仅体现在数量上：相对于通用的多语言模型，MameLoshnLM 更好地捕捉了定义该语言的词汇和形态学模式，这指出了大规模网络多语言数据对于低资源语言的一个更广泛的失效模式。我们的结果既为意第绪语 NLP 奠定了基础，也为历史上丰富但数字化代表性不足的语言中的语言模型开发提供了实用的模板。

> We present MameLoshnLM, the first open-source 8B-parameter language model built specifically for Yiddish. Despite Yiddish's rich textual tradition, its limited digital presence and the scarcity of reliable evaluation resources have constrained progress in Yiddish language modeling. Existing multilingual corpora and benchmarks are often poor proxies for the language, containing substantial amounts of noisy, machine-translated, and misclassified text. We address these gaps by introducing Oytser, a high-quality Yiddish pretraining corpus that combines contemporary web-native sources with literary materials, and Kashes, a multi-task benchmark spanning translation, linguistic analysis, information extraction, and language understanding. Using these resources, we continue pretraining Llama 3.1 8B to obtain MameLoshnLM. Across the tasks in the benchmark, MameLoshnLM outperforms open baselines of similar scale. Our analyses show that these gains are not only quantitative: relative to general-purpose multilingual models, MameLoshnLM better captures language-defining lexical and morphological patterns, pointing to a broader failure mode of noisy web-scale multilingual data for low-resource languages. Our results provide both a foundation for Yiddish NLP and a practical template for language model development in historically rich but digitally underrepresented languages.

---

## 获取与资源 (Access & Resources)
* **全文选项 (Full-Text Options):** 
  * [查看 PDF (View PDF)](https://arxiv.org/pdf/2608.05850)
  * [HTML 版本 - 实验性 (HTML Version (Experimental))](https://arxiv.org/html/2608.05850v1)
  * [TeX 源码 (TeX Source)](https://arxiv.org/src/2608.05850)
* **许可协议 (License):** [知识共享署名-相同方式共享 4.0 国际许可协议 (Creative Commons Attribution-ShareAlike 4.0 International)](http://creativecommons.org/licenses/by-sa/4.0/) <img alt="license icon" role="presentation" src="./images/5283893486a4.png"/>