---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-07
hide:
- navigation
tags:
- 大语言模型
- 代码库理解
- 基准测试
- 软件工程
- RepoProbe
title: RepoProbe：使用检查表评估架构感知的代码库理解能力
---
### 文章背景与核心概要
随着大语言模型（LLM）从函数级的代码生成向代码库级别的智能辅助过渡，评估其对复杂代码库的真实理解能力变得至关重要。现有的基准测试通常依赖于错误报告和 GitHub Issue，这使得模型可以通过对错误日志进行模式匹配来走捷径，同时还饱受“编辑偏差”（即跳过架构分析而过早生成代码）的困扰。此外，传统的“大模型作为裁判”（LLM-as-a-Judge）标量评分方法存在高方差和低可解释性的问题。

**RepoProbe** 是一种旨在评估仓库级代码理解能力的新型基准测试，它通过源自 GitHub Discussions 的开放式问答来评估模型，重点关注架构层面的探讨而非缺陷报告。为了确保客观可靠的评估，作者引入了一种**基于检查表的验证协议**（Checklist-Based Verification Protocol），将答案分解为原子化的、可验证的事实。对最先进大语言模型的评估证实了编辑偏差的普遍存在，并表明所提出的验证协议显着提高了评估的可靠性，超越了传统的标量评分。

---

## 论文详情 (Paper Details)

* **arXiv ID:** [arXiv:2608.04783](https://arxiv.org/abs/2608.04783) [cs.SE]
* **作者:** Yuexi Yang, Alyssa Wu, Ji Luo, Richeng Xuan, Zhichao Hu, Yuhong Liu, Zhen Qin
* **会议:** 已被第41届 IEEE/ACM 国际自动化软件工程会议（ASE 2026）接受
* **提交时间:** 2026年8月5日（修订于：2026年8月6日）
* **复现包与代码:** [GitHub 仓库](https://github.com/Tencent-Hunyuan/RepoProbe)

> * **arXiv ID:** [arXiv:2608.04783](https://arxiv.org/abs/2608.04783) [cs.SE]
> * **Authors:** Yuexi Yang, Alyssa Wu, Ji Luo, Richeng Xuan, Zhichao Hu, Yuhong Liu, Zhen Qin
> * **Conference:** Accepted to the 41st IEEE/ACM International Conference on Automated Software Engineering (ASE 2026)
> * **Submitted:** August 5, 2026 (Revised: August 6, 2026)
> * **Replication Package & Code:** [GitHub Repository](https://github.com/Tencent-Hunyuan/RepoProbe)

---

## 核心创新与发现 (Key Innovations & Findings)

* **转向架构探究:** 利用 GitHub Discussions 而非 GitHub Issues，以测试真实的代码库理解能力，而非简单的修补程序模式匹配。
* **基于检查表的验证协议:** 将复杂的答案分解为原子化的、可验证的事实，用客观验证替代主观标量评分，大幅减少评估方差。
* **编辑偏差的量化:** 证明了 SOTA（当前最先进的）LLM 经常遭受编辑偏差的影响——它们往往优先进行过早的代码修改，而不是进行彻底的架构分析。
* **可靠性:** 证明了基于事实的分解和验证在一致性和可解释性方面显著优于传统的“大模型作为裁判”评分范式。

> * **Shift to Architectural Inquiries:** Utilizes GitHub Discussions instead of GitHub Issues to test true repository comprehension rather than simple bug-fixing pattern matching.
> * **Checklist-Based Verification Protocol:** Decomposes complex answers into atomic, verifiable facts to replace subjective scalar ratings with objective verification, vastly reducing evaluation variance.
> * **Quantification of Edit Bias:** Proves that SOTA LLMs frequently suffer from edit bias—prioritizing premature code modifications over thorough architectural analysis.
> * **Reliability:** Demonstrates that factual decomposition and verification significantly outperform traditional LLM-as-a-Judge grading paradigms in consistency and interpretability.

---

## 全文与访问链接 (Full-Text & Access Links)

* **PDF 文档:** [查看 PDF](https://arxiv.org/pdf/2608.04783)
* **HTML 版本:** [arXiv HTML (实验性)](https://arxiv.org/html/2608.04783v2)
* **源码:** [TeX 源码](https://arxiv.org/src/2608.04783)
* **DOI:** [10.48550/arXiv.2608.04783](https://doi.org/10.48550/arXiv.2608.04783)

> * **PDF:** [View PDF](https://arxiv.org/pdf/2608.04783)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.04783v2)
> * **Source:** [TeX Source](https://arxiv.org/src/2608.04783)
> * **DOI:** [10.48550/arXiv.2608.04783](https://doi.org/10.48550/arXiv.2608.04783)