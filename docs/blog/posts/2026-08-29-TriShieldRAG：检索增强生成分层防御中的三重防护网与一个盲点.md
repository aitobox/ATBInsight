---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- RAG安全
- 对抗攻击
- 大语言模型
- 检索增强生成
- 模型防御
title: TriShieldRAG：检索增强生成分层防御中的三重防护网与一个盲点
---
### 文章背景与核心概要
检索增强生成（RAG）系统通过在查询时检索外部文档来支撑大语言模型（LLM）的回答，但这也使得系统可靠性容易受到受到污染或篡改的检索结果的威胁。尽管先前的工作（如 *PoisonedRAG*）表明单阶段防御对受污染文档的鲁棒性有限，本文仍提出了 **TriShieldRAG**，这是一个旨在消除单点故障的全面三层防御框架。

然而，作者的评估揭示了分层防御范式中的关键漏洞：在标准评估下，TriShieldRAG 将攻击成功率从 $79 \pm 1.0\%$ 大幅降至 $1 \pm 0.0\%$；但通过实施自适应攻击（仅修改文档格式而不改变投毒文本或访问检索器），攻击者成功绕过了所有测试语料库中的第一道防御层。一旦初始防护被绕过，下游防御层便会集体失效，因为它们依赖于相同的受损证据，这凸显了当前分层防御在面对自适应攻击时的局限性。

---

# TriShieldRAG: 3 Rings, One Blind Spot in Layered Defenses for Retrieval-Augmented Generation

**Authors:** Susil Kumar Mohanty, Rohit Patel, Kosuru Yuvaraj, Jeenal Chaudhary, Disha Singhania  
**Primary Subject:** Cryptography and Security (`cs.CR`)  
**arXiv ID:** [arXiv:2607.23838 [cs.CR]](https://arxiv.org/abs/2607.23838) | **DOI:** [10.48550/arXiv.2607.23838](https://doi.org/10.48550/arXiv.2607.23838)  
**Submission History:** Submitted on 26 Jul 2026; Last revised 26 Aug 2026 (v2).  

---

## 📋 Summary

检索增强生成（RAG）系统通过在查询时检索外部文档来支撑大语言模型（LLM）的回答，从而使系统可靠性容易受到受损或投毒检索结果的影响。尽管先前的研究（如 *PoisonedRAG*）表明单阶段防御对投毒文档的鲁棒性有限，但本文引入了 **TriShieldRAG**，这是一个旨在消除单点故障的综合三层防御框架。

> Retrieval-Augmented Generation (RAG) systems ground Large Language Model (LLM) responses using query-time retrieved documents, leaving system reliability vulnerable to compromised or poisoned retrieval results. While prior work like *PoisonedRAG* demonstrated that single-stage defenses provide limited robustness against poisoned documents, this paper introduces **TriShieldRAG**, a comprehensive three-layered defense framework designed to eliminate single points of failure. 

然而，作者的评估揭示了分层防御范式中的关键漏洞：
* **非自适应成功**：在对完整 Natural Questions (NQ) 语料库的标准评估下，TriShieldRAG 将攻击成功率从 $79 \pm 1.0\%$ 剧烈降低至 $1 \pm 0.0\%$。
* **自适应漏洞**：通过实施自适应攻击——仅修改文档格式而不改变投毒文本或访问检索器——攻击者成功在所有测试语料库中绕过了第一道防御层（500/500 个文档）。
* **分层防御崩溃**：一旦初始防护被绕过，下游防御层便会集体失效，因为它们依赖于相同的受损证据。此外，跨模型共识被证明具有误导性（在攻击成功率接近 $99\%$ 时，其一致性达到了 $0.96$），并且少数投毒阈值被证明依赖于具体语料库，而非具有普遍的边界。

> However, the authors' evaluation reveals critical vulnerabilities in layered defense paradigms:
> * **Non-Adaptive Success:** Under standard evaluation on the full Natural Questions (NQ) corpus, TriShieldRAG drastically reduced attack success rates from $79 \pm 1.0\%$ down to $1 \pm 0.0\%$.
> * **The Adaptive Vulnerability:** By implementing an adaptive attack—modifying only document formatting without altering poison text or accessing the retriever—attackers successfully bypassed the first defense layer across all tested corpora (500/500 documents). 
> * **Collapse of Layered Defenses:** Once the initial guard is bypassed, downstream layers fail collectively because they rely on the same compromised evidence. Furthermore, cross-model consensus proved misleading (reaching $0.96$ agreement while attack success approached $99\%$), and minority-poison thresholds proved to be corpus-dependent rather than universally bounded.

---

## 🛡️ The TriShieldRAG Framework

TriShieldRAG 依赖于三道互补的保护环：
1. **第 1 环：摄入防护（Ingest Guard）** — 在摄入阶段执行文档级筛选。
2. **第 2 环：检索评分器（Retrieval Scorer）** — 应用感知信任的重新排序来过滤可疑的检索段落。
3. **第 3 环：跨 LLM 共识（Cross-LLM Consensus）** — 验证三个不同语言模型之间的输出一致性。

> TriShieldRAG relies on three complementary rings of protection:
> 1. **Ring 1: Ingest Guard** — Performs document-level screening during the ingestion phase.
> 2. **Ring 2: Retrieval Scorer** — Applies trust-aware re-ranking to filter suspicious retrieved passages.
> 3. **Ring 3: Cross-LLM Consensus** — Validates output consistency across three diverse language models.

---

## 📊 Key Findings & Version 2 Updates

* **语料库扩展**：扩大了在全尺寸语料库上的测试，包括 **Natural Questions (NQ)**、**HotpotQA** 和 **MS-MARCO**。
* **自适应评估**：展示了通过格式转换完全绕过第 1 环（Ring 1）的情况。
* **指标修正**：撤回了先前的闭式阈值假设以及 v1 版的核心声明（例如从 91% 降至 13% 的缓解指标），确立了少数投毒阈值严格依赖于语料库（根据数据集的不同分别为 $0.214$、$0.251$ 和 $0.558$）。

> * **Corpus Scaling:** Expanded testing across full-scale corpora, including **Natural Questions (NQ)**, **HotpotQA**, and **MS-MARCO**.
> * **Adaptive Evaluation:** Demonstrated complete evasion of Ring 1 through formatting shifts.
> * **Metric Corrections:** Retracted previous closed-form threshold assumptions and the v1 headline claims (such as the 91%-to-13% mitigation metric), establishing that minority-poison thresholds are strictly corpus-dependent ($0.214$, $0.251$, and $0.558$ depending on the dataset).

---

## 🔗 Resources & Links

* **全文访问**：[查看 PDF](https://arxiv.org/pdf/2607.23838) | [实验性 HTML](https://arxiv.org/html/2607.23838v2) | [TeX 源码](https://arxiv.org/src/2607.23838)
* **许可证**：[知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/)
* **文献计量工具**：[谷歌学术](https://scholar.google.com/scholar_lookup?arxiv_id=2607.23838) | [语义学者](https://api.semanticscholar.org/arXiv:2607.23838)

> * **Full Text Access:** [View PDF](https://arxiv.org/pdf/2607.23838) | [Experimental HTML](https://arxiv.org/html/2607.23838v2) | [TeX Source](https://arxiv.org/src/2607.23838)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)
> * **Bibliographic Tools:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2607.23838) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2607.23838)

---
*[Preserved license asset marker from source document]*  
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">