---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- Spec-Driven Development
- 软件工程
- AI编码代理
- 数据集
- GitHub
title: SpecMine：大规模规范驱动开发（SDD）工件语料库
---
### 文章背景与核心概要
规范驱动开发（Spec-Driven Development, 简称 SDD）是近年来在软件工程领域迅速兴起的一种实践。在这种模式下，由开发者编写或（更常见地）由 AI 工具起草并经开发者人工审校的结构化自然语言规范，将直接指导 AI 编码代理（AI coding agent）的代码实现。自 2025 年以来，随着 GitHub Spec Kit、OpenSpec、AWS Kiro 等一系列相关工具的涌现，该领域的实践生态正在快速扩张，然而此前业界一直缺乏对这些 SDD 工件进行大规模研究的高质量数据集。

为了填补这一空白，本文介绍了 **SpecMine** —— 一个全面且大规模的语料库，旨在捕获公共 GitHub 仓库中的 SDD 实践。该语料库通过“广泛普查（Broad Census）”与“Kiro 普查（Kiro Census）”收集了数十万个规范文件，并结合了完整的仓库元数据与提交历史。此外，论文还通过对数千个拉取请求（Pull Request）的追踪以及数百万个强类型引用（typed references）的索引，深入展示了规范如何一步步转化为实际代码。SpecMine 的发布为学术界和工业界在 AI 代理时代研究软件规范化开发提供了首个大规模的开源支撑。

> **SpecMine** is a comprehensive, large-scale corpus capturing Spec-Driven Development (SDD)—a rapidly emerging software engineering practice where structured natural-language specifications (created by developers or curated via AI tools) guide AI coding agents. Following an explosion of SDD tooling since 2025 (such as GitHub Spec Kit, OpenSpec, and AWS Kiro), this dataset addresses the lack of large-scale studies on SDD artifacts. 
> 
> The corpus aggregates data through multiple censuses:
> * **Broad Census:** Covers 470,795 `specs.md` files across 73,030 repositories, spanning 17 named tools.
> * **Kiro Census:** Captures 98,574 files across 12,910 repositories featuring distinct requirements/design/tasks layouts.
> * **Pull Request & Reference Tracking:** Sweeps 5,992 pull requests across 581 repositories (with $\ge$ 10 stars) to observe direct transformations from specs to code, alongside a census-wide index of 2.4 million typed references linking documentation directly to implementations.

---

## 文档元数据

* **arXiv ID:** [arXiv:2608.25202](https://arxiv.org/abs/2608.25202) [cs.SE]
* **DOI:** [10.48550/arXiv.2608.25202](https://doi.org/10.48550/arXiv.2608.25202)
* **主要学科:** 软件工程 (`cs.SE`)
* **次要学科:** 人工智能 (`cs.AI`)
* **作者:** Shyam Agarwal, Bogdan Vasilescu
* **提交历史:** 
  * [v1] 2026年8月25日（星期二）
  * [v2] 2026年8月27日（星期四）*(当前版本)*

> ## Document Metadata
> 
> * **arXiv ID:** [arXiv:2608.25202](https://arxiv.org/abs/2608.25202) [cs.SE]
> * **DOI:** [10.48550/arXiv.2608.25202](https://doi.org/10.48550/arXiv.2608.25202)
> * **Primary Subject:** Software Engineering (`cs.SE`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`)
> * **Authors:** Shyam Agarwal, Bogdan Vasilescu
> * **Submission History:** 
>   * [v1] Tue, 25 Aug 2026
>   * [v2] Thu, 27 Aug 2026 *(current version)*

---

## 摘要

规范驱动开发（SDD）是一种快速兴起的开发实践。在此实践中，由开发人员编写或（更常见地）由 AI 工具起草、再经由开发人员审校的结构化自然语言规范，驱动着 AI 编码代理的代码实现。自 2025 年以来，涌现出了一波相关工具浪潮（例如 GitHub Spec Kit [3]、OpenSpec [4]、AWS Kiro [5] 以及其他数十种工具），然而这些工具所产出的工件此前从未在宏观规模上被系统研究过。

我们提出了 SpecMine，这是一个通过两次普查来捕获公共 GitHub 仓库中 SDD 实践的语料库：广泛普查涵盖了大多数工具的 [specs.md](http://spec.md/specs.md) 文件（分布在 73,030 个仓库中的 470,795 个文件，归属于 17 个具名工具），而 Kiro 普查则捕获了其独特的需求/设计/任务布局（分布在 12,910 个仓库中的 98,574 个文件）。每个规范都丰富了完整的仓库元数据、完整的提交历史以及解析后的文档结构。

规范如何演变为代码本身是一个开放性问题。因此，针对 11 种工具，我们检索了其在获得至少 10 颗星的仓库中所有触及规范的拉取请求（PR），捕获了 581 个仓库中的 5,992 个此类 PR 及其变更集。这使得最简单的开发工作流（规范与实现在一个 PR 中共同变更）变得可以直接观测；同时，包含 2,421,323 个类型引用的普查级索引（其中 1.28M 指向代码文件，863k 指向同级文档，152k 指向 PR，62k 指向引用，43k 指向分支，22k 指向 Issue）提供了从规范到代码的第二条独立链接。SpecMine 让社区得以在 AI 代理时代首次深入研究软件规范化的具体方式。

> ## Abstract
> 
> Spec-Driven Development (SDD) is a fast-emerging practice in which a structured natural-language specification, written by a developer, or (more often) drafted by an AI tool and then curated by the developer, drives an AI coding agent's implementation. A wave of tooling (GitHub Spec Kit [3], OpenSpec [4], AWS Kiro [5], and dozens of others) has appeared since 2025, yet the artifacts these tools produce have never been studied at scale. 
> 
> We present SpecMine, a corpus that captures SDD in public GitHub repositories through two censuses: a broad census of [specs.md](http://spec.md/specs.md) files covering most tools (470,795 files across 73,030 repositories, attributed to 17 named tools), and a Kiro census of its distinct requirements/design/tasks layout (98,574 files across 12,910 repositories). Each spec is enriched with full repository metadata, complete commit history, and parsed document structure. 
> 
> How a spec becomes code is itself an open question, so for 11 tools we sweep every pull request that touches a spec in their repositories with at least ten stars, capturing 5,992 such PRs across 581 repositories with their changesets. That makes the simplest workflow, spec and implementation changing together in one PR, directly observable, and a census-wide index of 2,421,323 typed references (1.28M to code files, 863k to sibling documents, 152k to PRs, 62k refs, 43k branches, 22k issues) gives a second, independent link from spec to code. SpecMine lets the community study, for the first time, how software is specified in the age of AI agents.

---

## 全文与访问链接

* **PDF 文档:** [查看 PDF](https://arxiv.org/pdf/2608.25202)
* **HTML 版本:** [arXiv HTML (实验性)](https://arxiv.org/html/2608.25202v2)
* **源码文件:** [TeX 源码](https://arxiv.org/src/2608.25202)
* **开源许可:** [知识共享署名 4.0 国际许可协议 (Creative Commons Attribution 4.0 International)](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"></a>

> ## Full-Text & Access Links
> 
> * **PDF:** [View PDF](https://arxiv.org/pdf/2608.25202)
> * **HTML Version:** [arXiv HTML (Experimental)](https://arxiv.org/html/2608.25202v2)
> * **Source Files:** [TeX Source](https://arxiv.org/src/2608.25202)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"></a>

---

## 外部参考与引用

* [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.25202)
* [Google Scholar (谷歌学术)](https://scholar.google.com/scholar_lookup?arxiv_id=2608.25202)
* [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.25202)

> ## External References & Citations
> 
> * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.25202)
> * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.25202)
> * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.25202)