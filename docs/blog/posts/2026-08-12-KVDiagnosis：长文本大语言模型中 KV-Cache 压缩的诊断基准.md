---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-12
hide:
- navigation
tags:
- KV-Cache
- 长文本大模型
- 模型压缩
- 基准测试
- AI诊断
title: KVDiagnosis：长文本大语言模型中 KV-Cache 压缩的诊断基准
---
### 文章背景与核心概要
在长文本大语言模型中，键值缓存（KV-Cache）压缩虽然成功降低了内存使用，但聚合的任务得分往往掩盖了具体执行失败的原因和方式。为此，本文推出了 **KVDiagnosis**——一个全面的诊断数据集与基准测试框架，旨在填补这一空白。

该论文主要有三大贡献：首先，建立了包含 25 种方法的分类体系，将压缩技术归纳为五个机制系列，并将其与 8 种经过验证的实现以及有效的诊断指标相连；其次，设计了强健的评估方案，针对每个受支持的方法配置，均采用按源划分的 `FullCache` 对照组进行评估，并隔离出 `FullCache` 正确但压缩后错误（`C-to-W`）的数据行，从而防止单一压缩器定义其他压缩器的测试集；最后，提出了统一的记录格式，将成对的输出和元数据与缓存、似然度、注意力和解码测量指标相关联，并明确了适用状态。在 `Qwen3-8B` 上的实证结果表明，诊断能有效区分成功压缩与失败，并展示了修复低证据注意力失败的定向干预措施。

---

## KVDiagnosis: A Diagnostic Benchmark for KV-Cache Compression in Long-Context Language Models

## Summary
While Key-Value (KV) cache compression successfully reduces memory usage in long-context language models, aggregate task scores often obscure why and how specific execution failures occur. **KVDiagnosis** introduces a comprehensive diagnostic dataset and benchmarking framework to address this gap. 

The paper makes three primary contributions:
1. **Taxonomy & Implementations:** A 25-method taxonomy grouping compression techniques into five mechanism families, linked to eight verified implementations and valid diagnostic measurements.
2. **Robust Evaluation Design:** Evaluates every supported method setting against a per-source `FullCache` control and isolates `FullCache`-correct/compressed-wrong (`C-to-W`) rows to prevent any single compressor from defining another's test set.
3. **Unified Record Format:** Links paired outputs and metadata with cache, likelihood, attention, and decoding measurements alongside explicit applicability states.

Key empirical findings on `Qwen3-8B` across four workloads include 59,800 supported compressed runs and 12,520 `C-to-W` rows. The study demonstrates that diagnostics can effectively separate successful compressions from failures and showcases targeted interventions to repair low-evidence-attention failures.

> 虽然键值（KV）缓存压缩成功降低了长上下文语言模型中的内存使用量，但聚合任务得分往往无法揭示特定执行失败发生的原因和方式。**KVDiagnosis** 引入了一个全面的诊断数据集和基准测试框架来填补这一空白。
> 
> 该论文作出了三项主要贡献：
> 1. **分类法与实现：** 提出了一个包含 25 种方法的分类法，将压缩技术分为五个机制系列，并将其与八个经过验证的实现和有效的诊断测量相关联。
> 2. **健壮的评估设计：** 针对每个支持的方法设置，根据每个源的 `FullCache` 对照组评估所有源，并为每个方法设置单独隔离出 `FullCache` 正确/压缩错误（`C-to-W`）行，防止任何单一压缩器定义其他压缩器的测试集。
> 3. **统一记录格式：** 将成对的输出和元数据与缓存、似然度、注意力和解码测量值以及显式适用性状态联系起来。
> 
> 在四个工作负载下的 `Qwen3-8B` 上的关键实证发现包括 59,800 个支持的压缩运行和 12,520 个 `C-to-W` 行。该研究表明，诊断可以有效地将成功的压缩与失败区分开来，并展示了修复低证据注意力失败的针对性干预措施。

---

## Paper Metadata

* **arXiv ID:** [arXiv:2608.09412](https://arxiv.org/abs/2608.09412) [cs.AI]
* **Authors:** Chen Qiu, Ziwu Liu, Chao Fei, Guozhong Li, Panos Kalnis
* **Submitted:** August 10, 2026
* **Primary Subject:** Artificial Intelligence (`cs.AI`)
* **Repository:** [GitHub - ChosenQC/KVDiagnosis](https://github.com/ChosenQC/KVDiagnosis)

> * **arXiv ID:** [arXiv:2608.09412](https://arxiv.org/abs/2608.09412) [cs.AI]
> * **作者：** Chen Qiu, Ziwu Liu, Chao Fei, Guozhong Li, Panos Kalnis
> * **提交时间：** 2026年8月10日
> * **主要主题：** 人工智能 (`cs.AI`)
> * **代码仓库：** [GitHub - ChosenQC/KVDiagnosis](https://github.com/ChosenQC/KVDiagnosis)

---

## Abstract

> KV-cache compression reduces long-context memory, but aggregate task scores reveal neither which correct executions fail nor why. We present KVDiagnosis, a diagnostic dataset and benchmark with three contributions. First, a 25-method taxonomy groups methods into five mechanism families and links them to eight verified implementations and their valid diagnostic measurements. Second, for every supported method setting, we evaluate all sources in each fixed split against a per-source FullCache control before selecting FullCache-correct/compressed-wrong (C-to-W) rows separately for each method-setting, so no compressor defines another's test set. Third, a common record format links paired outputs and run metadata to cache, likelihood, attention, and decoding measurements with explicit applicability states. On Qwen3-8B, four evidence-aware workloads yield 59 800 supported compressed runs over 2600 sources and 12 520 C-to-W rows. Under fixed diagnostic rules, 63.2% have low or partial measured/projected coverage. Only 19 rows (0.2%) combine high measured/projected coverage with strong likelihood drift; another 2,126 (17.0%) preserve structural position addressability, for which representation fidelity remains unknown, while showing the same drift. Against C-to-C success controls, all ten diagnostics separate failed from successful compression (stratified AUROC 0.684-0.871). Among 96 reproducible low-EAR failures, a controlled 4x evidence-attention boost repairs 29.2%, versus 6.3% under a count-matched sham intervention and 3.3% degradation on matched C-to-C controls.

> KV 缓存压缩减少了长上下文内存，但聚合任务得分既没有显示哪些正确的执行失败了，也没有显示原因。我们提出了 KVDiagnosis，一个具有三个贡献的诊断数据集和基准。首先，一个包含 25 种方法的分类法将方法分为五个机制系列，并将它们与八个经过验证的实现及其有效的诊断测量联系起来。其次，对于每个支持的方法设置，我们在每个固定拆分中针对每个源的 FullCache 控制评估所有源，然后为每个方法设置单独选择 FullCache 正确/压缩错误 (C-to-W) 行，因此没有压缩器定义另一个压缩器的测试集。第三，通用记录格式将成对的输出和运行元数据与具有显式适用性状态的缓存、似然度、注意力和解码测量值联系起来。在 Qwen3-8B 上，四个感知证据的工作负载在 2600 个源和 12 520 个 C-to-W 行上产生了 59 800 个支持的压缩运行。在固定的诊断规则下，63.2% 的测量/预测覆盖率低或部分。只有 19 行 (0.2%) 将高测量/预测覆盖率与强似然漂移结合起来；另外 2,126 行 (17.0%) 保留了结构位置可寻址性（其表示保真度未知），同时显示出相同的漂移。针对 C-to-C 成功对照，所有十个诊断将失败的压缩与成功的压缩区分开来（分层 AUROC 0.684-0.871）。在 96 个可重现的低 EAR 失败中，受控的 4 倍证据-注意力提升修复了 29.2%，而计数匹配的虚假干预修复率为 6.3%，匹配的 C-to-C 对照退化率为 3.3%。

---

## Access & Resources

* **Full-Text Options:** 
  * [View PDF](https://arxiv.org/pdf/2608.09412)
  * [HTML Version (Experimental)](https://arxiv.org/html/2608.09412v1)
  * [TeX Source](https://arxiv.org/src/2608.09412)
* **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
* **External Citations & Tools:**
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.09412)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.09412)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.09412)

> * **全文选项：** 
>   * [查看 PDF](https://arxiv.org/pdf/2608.09412)
>   * [HTML 版本（实验性）](https://arxiv.org/html/2608.09412v1)
>   * [TeX 源码](https://arxiv.org/src/2608.09412)
> * **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
> * **外部引用与工具：**
>   * [Google 学术](https://scholar.google.com/scholar_lookup?arxiv_id=2608.09412)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.09412)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.09412)