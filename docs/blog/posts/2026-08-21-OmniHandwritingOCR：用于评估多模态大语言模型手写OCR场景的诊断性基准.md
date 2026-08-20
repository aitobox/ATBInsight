---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-21
hide:
- navigation
tags:
- 多模态大语言模型
- OCR
- 手写识别
- 数学公式识别
- 基准测试
title: OmniHandwritingOCR：用于评估多模态大语言模型手写OCR场景的诊断性基准
---
### 文章背景与核心概要

随着多模态大语言模型（MLLMs）在文档和知识处理流程中日益被用作光学字符识别（OCR）系统，它们准确转录现实世界手写字迹的能力在很大程度上仍未得到充分探索。现有的 OCR 基准测试主要集中于打印文本或干净的单行输入，这导致在多语言内容、书写错误以及复杂数学公式等真实手写场景中存在显著的评估空白。

为了解决这一问题，本文作者推出了 **OmniHandwritingOCR**，这是一个全面的诊断性基准，旨在评估 MLLMs 和传统 OCR 系统的性能。该基准包含 77.57K 张带标签的图像，涵盖手写文本识别（HTR）和手写数学表达式识别（HMER）两大类别的 6 个子任务及 12 个子集。评估结果表明，当前模型在复杂多-行公式上性能急剧下降，且普遍存在“幻觉”现象，为诊断多模态模型在真实世界手写 OCR 场景中的失效模式提供了严格的测试平台。

---

# OmniHandwritingOCR: A Diagnostic Benchmark for Evaluating Multimodal LLMs in Handwritten OCR Scenarios

**Authors:** Zinuo Guo, Min Zhang, Bo Jiang  
**Published:** August 19, 2026 (CIKM 2026)  
**Subjects:** Computer Vision and Pattern Recognition (`cs.CV`), Artificial Intelligence (`cs.AI`)  
**arXiv:** [2608.18586 [cs.CV]](https://arxiv.org/abs/2608.18586) | **DOI:** [10.48550/arXiv.2608.18586](https://doi.org/10.48550/arXiv.2608.18586)

> Multimodal Large Language Models (MLLMs) are increasingly utilized as Optical Character Recognition (OCR) systems in document and knowledge-processing pipelines. However, their capability to faithfully transcribe real-world handwriting remains largely underexplored. Existing OCR benchmarks primarily focus on printed text or clean single-line inputs, leaving a significant gap in realistic handwriting scenarios such as multilingual content, writer errors, and complex mathematical formulas.
> 
> To address this, the authors introduce **OmniHandwritingOCR**, a comprehensive diagnostic benchmark designed to evaluate MLLMs and traditional OCR systems. 

---

## 📌 Summary

多模态大语言模型（MLLMs）在文档和知识处理流程中越来越多地被用作光学字符识别（OCR）系统。然而，它们准确转录真实世界手写内容的能力在很大程度上仍未得到充分探索。现有的 OCR 基准测试主要集中在打印文本或干净的单行输入上，这使得在多语言内容、书写者错误以及复杂数学公式等现实手写场景中存在明显的空白。
为了解决这一问题，作者推出了 **OmniHandwritingOCR**，这是一个全面的诊断性基准，旨在评估 MLLMs 和传统 OCR 系统。

> Multimodal Large Language Models (MLLMs) are increasingly utilized as Optical Character Recognition (OCR) systems in document and knowledge-processing pipelines. However, their capability to faithfully transcribe real-world handwriting remains largely underexplored. Existing OCR benchmarks primarily focus on printed text or clean single-line inputs, leaving a significant gap in realistic handwriting scenarios such as multilingual content, writer errors, and complex mathematical formulas.
> 
> To address this, the authors introduce **OmniHandwritingOCR**, a comprehensive diagnostic benchmark designed to evaluate MLLMs and traditional OCR systems.

---

## 🔍 Key Highlights of OmniHandwritingOCR

- **规模与范围：** 包含 **77.57K 张带标签的图像**，来源于公共数据集以及新收集的学生手写样本。
- **涵盖任务：** 跨越 6 个子任务和 12 个子集，重点关注：
  - 手写文本识别（HTR）
  - 手写数学表达式识别（HMER）
- **结构复杂度：** 引入了一个难度分层的多行公式语料库，专门用于在不断增加的结构复杂度下对模型的鲁棒性进行压力测试。
- **评估协议：** 在统一的测试协议下，使用五个互补的指标评估了 13 个开源和闭源系统。

> - **Scope & Scale:** Comprises **77.57K labeled images** sourced from public datasets and newly collected student writings.
> - **Tasks Covered:** Spans 6 subtasks and 12 subsets, focusing on:
>   - Handwritten text recognition (HTR)
>   - Handwritten mathematical expression recognition (HMER)
> - **Structural Complexity:** Features a difficulty-stratified multi-line formula corpus explicitly built to stress-test model robustness under increasing structural complexity.
> - **Evaluation Protocol:** Evaluates 13 open- and closed-source systems using five complementary metrics under a unified testing protocol.

---

## 📊 Key Findings

1. **性能差距：** 当前的 MLLMs 和 OCR 系统距离实现准确转录仍有很大差距，在复杂的多行公式上面临性能急剧下降的问题。
2. **排名不一致：** 在不同的语言和公式设置下，模型的鲁棒性和排名表现出显着差异。
3. **幻觉问题：** 几个生成式模型经常“幻觉”出看似合理的修正结果，但这些修正缺乏实际源图像的视觉依据。

OmniHandwritingOCR 为诊断多模态模型在现实手写 OCR 场景中的语言、内容、结构和视觉基础（visual-grounding）失效模式提供了一个严格的测试平台。

> 1. **Performance Gap:** Current MLLMs and OCR systems remain far from achieving faithful transcription, experiencing sharp performance drops on complex multi-line formulas.
> 2. **Inconsistent Rankings:** Model robustness and rankings vary significantly across different language and formula settings.
> 3. **Hallucination Issues:** Several generative models frequently "hallucinate" plausible-looking corrections that are visually unsupported by the actual source images.
> 
> OmniHandwritingOCR serves as a rigorous testbed for diagnosing language, content, structural, and visual-grounding failure modes of multimodal models in real-world handwritten OCR scenarios.

---

## 🔗 Quick Links & Full-Text Access

- **查看 PDF：** [arXiv:2608.18586 PDF](https://arxiv.org/pdf/2608.18586)
- **代码与数据集成：** 通过 [Hugging Face](https://huggingface.co/huggingface)、[Papers with Code / CatalyzeX](https://www.catalyzex.com) 和 [alphaXiv](https://alphaxiv.org/) 探索相关代码库。
- **许可证：** [知识共享署名 4.0 国际许可协议 (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/)  
  <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" width="80" />

> - **View PDF:** [arXiv:2608.18586 PDF](https://arxiv.org/pdf/2608.18586)
> - **Code & Data Integration:** Explore associated repositories via [Hugging Face](https://huggingface.co/huggingface), [Papers with Code / CatalyzeX](https://www.catalyzex.com), and [alphaXiv](https://alphaxiv.org/).
> - **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)  
>   <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png" width="80" />