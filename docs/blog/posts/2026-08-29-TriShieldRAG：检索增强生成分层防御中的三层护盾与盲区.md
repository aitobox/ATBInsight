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
title: TriShieldRAG：检索增强生成分层防御中的三层护盾与盲区
---
### 文章背景与核心概要
检索增强生成（RAG）系统通过在查询时检索外部文档来为大语言模型（LLM）的响应提供支撑，但这使其系统可靠性容易受到受到污染或篡改的检索结果的影响。尽管先前的研究（如 *PoisonedRAG*）表明单阶段防御对污染文档的鲁棒性有限，但本文提出了 **TriShieldRAG**，这是一个旨在消除单点故障的综合三层防御框架。

然而，作者的评估揭示了分层防御范式中的致命漏洞：在标准评估下，TriShieldRAG 能够将攻击成功率大幅降低，但通过实施自适应攻击——仅修改文档格式而不改变污染文本或访问检索器——攻击者成功绕过了所有测试语料库中的第一道防御层。一旦初始防线被突破，下游各层便会集体失效，因为它们都依赖于同一份受损的证据。

---

# TriShieldRAG: 3 Rings, One Blind Spot in Layered Defenses for Retrieval-Augmented Generation

**Authors:** Susil Kumar Mohanty, Rohit Patel, Kosuru Yuvaraj, Jeenal Chaudhary, Disha Singhania  
**Primary Subject:** Cryptography and Security (`cs.CR`)  
**arXiv ID:** [arXiv:2607.23838 [cs.CR]](https://arxiv.org/abs/2607.23838) | **DOI:** [10.48550/arXiv.2607.23838](https://doi.org/10.48550/arXiv.2607.23838)  
**Submission History:** Submitted on 26 Jul 2026; Last revised 26 Aug 2026 (v2).  

---

## 📋 摘要

检索增强生成（RAG）系统通过在查询时检索到的文档来基础化大语言模型（LLM）的响应，从而使系统的可靠性容易受到受损或污染的检索结果的影响。虽然先前的研究如 *PoisonedRAG* 证明了单阶段防御对受污染文档的鲁棒性有限，但本文引入了 **TriShieldRAG**，这是一个全面的三层防御框架，旨在消除单点故障。

然而，作者的评估揭示了分层防御范式中的关键漏洞：
* **非自适应成功**：在对完整 Natural Questions (NQ) 语料库的标准评估下，TriShieldRAG 将攻击成功率从 $79 \pm 1.0\%$ 大幅降低至 $1 \pm 0.0\%$。
* **自适应漏洞**：通过实施自适应攻击——仅修改文档格式而不改变污染文本或访问检索器——攻击者成功绕过了所有测试语料库中的第一道防御层（500/500 个文档）。
* **分层防御的崩溃**：一旦初始防线被绕过，下游各层就会集体失效，因为它们依赖于相同的受损证据。此外，跨模型共识被证明具有误导性（在攻击成功率接近 $99\%$ 的同时，达成 $0.96$ 的一致性），并且少数污染阈值在很大程度上取决于语料库，而非具有普遍边界。

> Retrieval-Augmented Generation (RAG) systems ground Large Language Model (LLM) responses using query-time retrieved documents, leaving system reliability vulnerable to compromised or poisoned retrieval results. While prior work like *PoisonedRAG* demonstrated that single-stage defenses provide limited robustness against poisoned documents, this paper introduces **TriShieldRAG**, a comprehensive three-layered defense framework designed to eliminate single points of failure. 
>
> However, the authors' evaluation reveals critical vulnerabilities in layered defense paradigms:
> * **Non-Adaptive Success:** Under standard evaluation on the full Natural Questions (NQ) corpus, TriShieldRAG drastically reduced attack success rates from $79 \pm 1.0\%$ down to $1 \pm 0.0\%$.
> * **The Adaptive Vulnerability:** By implementing an adaptive attack—modifying only document formatting without altering poison text or accessing the retriever—attackers successfully bypassed the first defense layer across all tested corpora (500/500 documents). 
> * **Collapse of Layered Defenses:** Once the initial guard is bypassed, downstream layers fail collectively because they rely on the same compromised evidence. Furthermore, cross-model consensus proved misleading (reaching $0.96$ agreement while attack success approached $99\%$), and minority-poison thresholds proved to be corpus-dependent rather than universally bounded.

---

## 🛡️ TriShieldRAG 框架

TriShieldRAG 依赖于三道互补的保护环：
1. **第一环：摄入防护（Ingest Guard）** — 在摄入阶段执行文档级别的筛查。
2. **第二环：检索评分器（Retrieval Scorer）** — 应用具有信任感知能力的重排来过滤可疑的检索段落。
3. **第三环：跨大模型共识（Cross-LLM Consensus）** — 验证三个不同语言模型之间的输出一致性。

> ## 🛡️ The TriShieldRAG Framework
>
> TriShieldRAG relies on three complementary rings of protection:
> 1. **Ring 1: Ingest Guard** — Performs document-level screening during the ingestion phase.
> 2. **Ring 2: Retrieval Scorer** — Applies trust-aware re-ranking to filter suspicious retrieved passages.
> 3. **Ring 3: Cross-LLM Consensus** — Validates output consistency across three diverse language models.

---

## 📊 核心发现与第二版（v2）更新

* **语料库扩展**：扩大了跨大规模语料库的测试，包括 **Natural Questions (NQ)**、**HotpotQA** 和 **MS-MARCO**。
* **自适应评估**：展示了通过格式转变完全规避第一环（Ring 1）的过程。
* **指标修正**：撤回了先前的闭式阈值假设以及 v1 版本的核心声明（例如 91% 降至 13% 的缓解指标），确定少数污染阈值严格取决于语料库（根据数据集不同，分别为 $0.214$、$0.251$ 和 $0.558$）。

> ## 📊 Key Findings & Version 2 Updates
>
> * **Corpus Scaling:** Expanded testing across full-scale corpora, including **Natural Questions (NQ)**, **HotpotQA**, and **MS-MARCO**.
> * **Adaptive Evaluation:** Demonstrated complete evasion of Ring 1 through formatting shifts.
> * **Metric Corrections:** Retracted previous closed-form threshold assumptions and the v1 headline claims (such as the 91%-to-13% mitigation metric), establishing that minority-poison thresholds are strictly corpus-dependent ($0.214$, $0.251$, and $0.558$ depending on the dataset).

---

## 🔗 资源与链接

* **全文访问**：[查看 PDF](https://arxiv.org/pdf/2607.23838) | [实验性 HTML](https://arxiv.org/html/2607.23838v2) | [TeX 源码](https://arxiv.org/src/2607.23838)
* **许可证**：[知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/)
* **文献计量工具**：[谷歌学术](https://scholar.google.com/scholar_lookup?arxiv_id=2607.23838) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2607.23838)

> ## 🔗 Resources & Links
>
> * **Full Text Access:** [View PDF](https://arxiv.org/pdf/2607.23838) | [Experimental HTML](https://arxiv.org/html/2607.23838v2) | [TeX Source](https://arxiv.org/src/2607.23838)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/)
> * **Bibliographic Tools:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2607.23838) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2607.23838)

---
*[Preserved license asset marker from source document]*  
<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">