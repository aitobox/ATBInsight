---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 人工智能
- 软件工程
- 自动写作
- 编译验证
- 事实核查
title: PatchWrite：一行而非一节——面向AI撰写文稿的编译门控与有效性保持编辑框架
---
### 文章背景与核心概要

自动化科学文稿生成流程通常在修复局部缺陷时会重写整个章节。然而，这种方法往往会无意中修改无关的指标、引用和文本，即使最终生成的文档能够成功编译，也会导致数据一致性受损。

为了解决这一问题，PatchWrite 引入了一种精确且保持有效性的编辑框架。该框架摒弃了全章节重写，转而采用受限的行级编辑，并由两项严格的验证机制进行管控：一是“编译门控”（Compile Gates），通过致命日志检查确保编辑不会破坏文档编译；二是“证据锁定”（Evidence Locks），要求所有引用的键值和实验数值必须经过权威参考注册表或实验日志的严格验证。

实验结果表明，PatchWrite 在保持高质量文风的同时，成功保留了关键的实验室基础事实和格式，在性能上远超传统的章节级AI重写流程。

---

## 摘要

自动化文稿生成流程通常会重写整个章节以修复局部缺陷，这导致即使生成的PDF文件能够正常构建，无关的指标和引用也可能发生改变。

**PatchWrite** 则通过限制候选编辑提交至文稿状态的方式来解决这一问题：它复用了受限的 `EDIT N M` 编辑与回滚机制，但通过致命日志检查加强了编译验收标准，并增加了证据锁定机制，要求每一个引用的键值和实验数值都必须由参考注册表或实验日志进行验证。未能通过任一检查的候选内容将被拒绝，并保留之前的 HEAD 版本。

### 关键实证发现：
* **Oracle压力测试：** 在一项包含24份文稿 × 8种故障的Oracle压力测试中（共768项任务，均匀分布在编译中断故障和内容错误故障中），全槽位重写在每种情况下都变动了无关的“12层”行（192次中0次保留；数值Jaccard系数为0.6667），而 PatchWrite 在 **192/192 次**中均成功保留了该行。
* **消融实验结果：** 移除编译门控导致接受率为0，而移除证据门控则导致虚构的引用通过了验证（这一模式在所有八种故障中均成立）。
* **生成性能：** 当由写作模型提出编辑建议（而非使用Oracle编辑）时，候选内容的接受率为 **75%**。几乎所有的拒绝都源于一种单一的可复现失败模式，即模型试图使用当前语法不支持的空替换来删除一行。
* **准确性：** 每个被接受的候选内容都通过了两个门控，且 **93.75%** 的案例修复了注入的故障（其余案例涉及技术上有效但句子语境不合适的引用，以及一次标记变更的微小失误）。
* **人类评估：** 在对16对PDF进行的盲测评估中，两位人类评审员均强烈倾向于 PatchWrite，认为其在保留实验室基础事实方面表现更佳（C1李克特量表 5.0 vs 2.0），同时对文风质量的评价几乎一致。来自193项产品内起草任务的日志证实，这些失败类别在实践中同样存在。

> Automated manuscript pipelines often regenerate an entire section to repair a local defect, allowing unrelated metrics and citations to change even when the resulting PDF still builds. 
>
> **PatchWrite** instead constrains how candidate edits become committed manuscript states: it reuses bounded `EDIT N M` editing and rollback, but tightens compilation acceptance with fatal-log checks and adds evidence locks that require every cited key and experimental numeric token to be attested by a reference registry or experimental log. Candidates that fail either check are rejected and the previous HEAD is retained. 
>
> ### Key Empirical Findings:
> * **Oracle Stress Test:** On a 24-manuscript × 8-fault oracle stress test (768 jobs, evenly split between compile-breaking and content-only faults), whole-slot rewriting mutated an unrelated "12-layer" line in every case ($0/192$ preserved; numeric Jaccard $0.6667$), whereas PatchWrite preserved it in **$192/192$ cases**. 
> * **Ablation Results:** Removing the compile gate reduced acceptance to $0$, while removing the evidence gate allowed a hallucinated citation to pass (a pattern that held across all eight faults).
> * **Generation Performance:** When the writer model proposed edits (rather than using oracle edits), candidates were accepted in **$75\%$ of cases**. Nearly all rejections stemmed from a single reproducible failure mode where the model attempted to delete a line using an empty replacement unsupported by the current grammar.
> * **Accuracy:** Every accepted candidate passed both gates, and **$93.75\%$ fixed the injected fault** (the remaining cases involved a technically valid but sentence-inappropriate citation and one markup-changing near-miss).
> * **Human Evaluation:** In a blind evaluation of sixteen PDF pairs, both human raters strongly preferred PatchWrite for preserving lab-grounded facts (C1 Likert $5.0$ vs. $2.0$), while rating prose quality nearly identically. Logs from 193 in-product drafting tasks confirm these same failure classes occurring in practice.

---

## 导航与资源

* **全文链接：** [查看 PDF](https://arxiv.org/pdf/2608.23001) | [HTML (实验性)](https://arxiv.org/html/2608.23001v1) | [TeX 源码](https://arxiv.org/src/2608.23001)
* **许可协议：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
* **外部文献工具：** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23001)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23001)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23001)

> * **Full-Text Links:** [View PDF](https://arxiv.org/pdf/2608.23001) | [HTML (Experimental)](https://arxiv.org/html/2608.23001v1) | [TeX Source](https://arxiv.org/src/2608.23001)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
> * **External Bibliographic Tools:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23001)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23001)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23001)