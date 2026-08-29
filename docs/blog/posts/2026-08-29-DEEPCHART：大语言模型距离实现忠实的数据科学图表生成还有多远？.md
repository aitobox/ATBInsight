---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 大语言模型
- 数据可视化
- 幻觉检测
- 基准测试
- 多模态学习
title: DEEPCHART：大语言模型距离实现忠实的数据科学图表生成还有多远？
---
### 文章背景与核心概要

在真实的数据科学工作流中，生成忠实于原始数据的图表要求模型能够从分散的证据中提取信息、计算出正确的绘图数值，并进行精确渲染。尽管现代大语言模型（LLM）能够生成视觉上看似合理且符合基本指令的图表，但在长文本、噪声干扰及多模态环境下，数据层面的“幻觉”问题依然难以察觉且难以根除。

为了系统性地衡量这一差距，研究人员提出了 **DEEPCHART** 基准测试。该基准包含 1,482 个源自真实科学论文、财务报告和生态报告的任务条件图表生成实例。DEEPCHART 将图表生成过程拆解为“提取-推理-可视化”（Extract–Reason–Visualize）流水线，从而分阶段评估模型在源数据提取、派生数据推理以及图表渲染方面的表现。

---

## 📌 总结

在真实的数据科学工作流中，生成忠实的图表需要模型将可视化建立在分散的证据之上，计算出准备就绪的图表数据，并准确地呈现它们。虽然现代大语言模型（LLM）可以生成视觉上合理且符合基本指令的图表，但在长文本、噪声和多模态背景下，数据层面的幻觉仍然是一个持续存在且难以检测的问题。

> Generating faithful charts in real-world data-science workflows requires models to ground visualizations in scattered evidence, compute correct chart-ready quantities, and render them accurately. While modern Large Language Models (LLMs) can produce visually plausible charts that comply with basic instructions, data-level hallucinations remain a persistent and hard-to-detect problem in long, noisy, and multimodal contexts. 

为了系统地衡量这一差距，作者引入了 **DEEPCHART**，这是一个由专家标注的基准测试，包含 1,482 个任务条件图表生成实例，这些实例来源于真实的科学论文、财务文件和生态报告。DEEPCHART 将图表生成过程分解为“提取-推理-可视化”（Extract–Reason–Visualize）流水线，分阶段评估源数据提取、派生数据推理和图表渲染。

> To systematically measure this gap, the authors introduce **DEEPCHART**, an expert-annotated benchmark comprising 1,482 task-conditioned chart-generation instances sourced from real scientific papers, financial filings, and ecosystem reports. DEEPCHART breaks down the chart generation process into an **Extract–Reason–Visualize** pipeline, evaluating source-data extraction, derived-data reasoning, and chart rendering stage by stage.

---

## 🔍 关键发现

* **隐蔽的幻觉：** 视觉上合理的图表往往掩盖了严重的数据层面幻觉。
* **流水线瓶颈：** 在现实的长文本和多模态设置中，源数据提取和定量推理经常出现错误。
* **上下文限制：** 仅仅扩大上下文窗口是不够的；忠实的图表生成需要在渲染阶段之前具备强大的证据提取和定量推理能力。

> * **Hidden Hallucinations:** Visually plausible charts often conceal significant data-level hallucinations.
> * **Pipeline Bottlenecks:** Errors in source-data extraction and quantitative reasoning are frequent in realistic, long-context, and multimodal settings.
> * **Context Limitations:** Simply scaling up context windows is insufficient; faithful chart generation requires robust evidence extraction and quantitative reasoning capabilities prior to the rendering phase.

---

## 📄 摘要

在真实的数据科学工作流中，忠实的图表生成要求将可视化建立在分散的证据之上，计算出图表所需的数值，并准确地进行渲染。现代 LLM 可以生成视觉上合理且符合指令的图表，但在长文本、噪声和多模态环境下，数据层面的幻觉仍然难以检测。为了衡量这一差距，我们引入了 **DEEPCHART**，这是一个由专家标注的基准测试，包含 1,482 个任务条件图表生成实例，均取自真实的科学论文、财务文件和生态报告。

> Faithful chart generation in real-world data-science workflows requires grounding visualizations in scattered evidence, computing chart-ready quantities, and rendering them accurately. Modern LLMs can produce visually plausible, instruction-compliant charts, yet data-level hallucinations remain difficult to detect in long, noisy, and multimodal contexts. To measure this gap, we introduce **DEEPCHART**, an expert-annotated benchmark of 1,482 task-conditioned chart-generation instances drawn from real-world scientific papers, financial filings, and ecosystem reports. 

DEEPCHART 将图表生成制定为“提取-推理-可视化”流水线，并分阶段评估源数据提取、派生数据推理和图表渲染。对最先进模型的实验表明，视觉上合理的图表往往掩盖了数据层面的幻觉，且提取和推理错误在现实的长文本和多模态设置中很常见。这些发现表明，仅靠更大的上下文窗口是不够的；忠实的图表生成还需要在渲染前具备可靠的证据提取和定量推理能力。

> DEEPCHART formulates chart generation as an **Extract–Reason–Visualize** pipeline and evaluates source-data extraction, derived-data reasoning, and chart rendering stage by stage. Experiments with state-of-the-art models show that visually plausible charts often conceal data-level hallucinations, with extraction and reasoning errors common in realistic long and multimodal settings. These findings suggest that larger context windows alone are insufficient; faithful chart generation also requires reliable evidence extraction and quantitative reasoning before rendering.

---

## 🔗 链接与全文访问

* **arXiv 摘要：** [arXiv:2608.26757](https://arxiv.org/abs/2608.26757)
* **PDF 版本：** [下载 PDF](https://arxiv.org/pdf/2608.26757)
* **HTML 版本：** [arXiv HTML (实验性)](https://arxiv.org/html/2608.26757v1)
* **源代码与数据：** [GitHub - DeepChart](https://github.com/tangdouer1005/DeepChart)