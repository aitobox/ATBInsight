---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- AI Agent
- Claude Code
- 软件工程
- 实证研究
- 插件市场
title: 智能体插件的维护与共演化：Claude Code 插件市场的实证研究
---
### 文章背景与核心概要
随着 AI 编码智能体（AI Coding Agents）的迅猛发展，插件市场已成为扩展智能体能力的核心生态。然而，由自然语言指令、脚本和配置文件共同组成的 AI 智能体插件，其维护模式与共演化规律在学术界和工业界尚属空白。本文针对 Claude Code 插件市场进行了首个大规模实证研究，分析了数千个市场、插件及提交记录，深入探讨了插件的生命周期特征。

研究发现，AI 插件市场正处于爆发式增长阶段，软件工程任务占据了主导地位。与传统开源软件（OSS）相比，插件开发呈现出显著的“功能驱动”特征，且 AI 参与共创的比例极高（Claude 参与了近 35% 的提交）。此外，研究揭示了一种传统软件工程中从未有过的全新维护依赖：技能目录（skills directories）中的自然语言指令文件与实现脚本之间存在高达 78% 的功能耦合共演化。该研究为理解和优化未来的 AI 智能体工程提供了重要的理论依据和数据支撑。

---

# On the Maintenance and Co-evolution of Agent Plugins: An Empirical Study of Claude Code Plugin Marketplaces

**Authors:** Ahmed Hereiz, Yingzhe Lyu, Hao Li, Bram Adams, Ahmed E. Hassan  
**Subjects:** Software Engineering (`cs.SE`); Artificial Intelligence (`cs.AI`)  
**arXiv:** [2608.28497 [cs.SE]](https://arxiv.org/abs/2608.28497)  
**Submitted:** 28 August 2026 (Under review)

---

## 📌 Summary

本文呈现了首个针对**AI 编码智能体插件市场**（特别聚焦于托管 Claude Code 插件市场的 1,926 个代码库）的结构、维护与共演化动态的实证研究。

与纯粹由源代码构建的传统软件包不同，智能体插件结合了**自然语言指令文件、脚本和配置文件**。作者分析了 **8,351 个插件、77,773 次提交以及 2,018 个市场**，旨在确定这些插件究竟是得到积极维护的产物，还是仅仅是一次性的脚本。

主要发现包括：
* **市场迅猛增长：** 在 2025 年 10 月发布后的六个月内，涉及插件的提交活动激增了 **8.8 倍**。软件工程任务占据统治地位，占所有插件的 **61.3%**。
* **功能驱动开发：** 插件开发严重倾向于功能驱动，功能类提交的发生率是传统开源软件（OSS）的两倍以上（39.6% 对比 17.2%）。
* **AI 共同署名：** Claude 参与共创了所有提交中的 **34.9%**。此外，与传统软件相比，传统的提交类型（`docs`、`perf`、`style` 和 `refactor`）在智能体插件代码库中具有根本不同的含义。
* **一类新型维护依赖：** 尽管大多数组件类型是独立演化的，但技能目录（skills directories）内的自然语言指令与实现脚本以高于随机概率的频率共演化（具有 **78% 的功能耦合**）——这代表了一种完全独特、在传统 AI 智能体工程中未曾见过的维护依赖关系。

> This paper presents the first empirical study investigating the structure, maintenance, and co-evolution dynamics of **AI coding agent plugin marketplaces** (specifically focusing on 1,926 repositories hosting Claude Code plugin marketplaces). 
>
> Unlike traditional software packages built purely with source code, agent plugins combine **natural-language instruction files, scripts, and configuration files**. The authors analyzed **8,351 plugins, 77,773 commits, and 2,018 marketplaces** to determine whether these plugins are actively maintained artifacts or merely one-off scripts. 
>
> Key findings include:
> * **Rapid Marketplace Growth:** Plugin-touching commit activity surged **8.8x** within the six months following its October 2025 launch. Software Engineering tasks dominate, accounting for **61.3%** of all plugins.
> * **Feature-Driven Development:** Plugin development is heavily feature-driven, with feature commits occurring at more than **twice the rate** of conventional open-source software (OSS) (39.6% vs. 17.2%).
> * **AI Co-Authorship:** Claude co-authors **34.9%** of all commits. Furthermore, traditional commit types (`docs`, `perf`, `style`, and `refactor`) carry fundamentally different meanings in agent plugin repositories compared to legacy software.
> * **A New Class of Maintenance Dependency:** While most component types evolve independently, natural-language instructions and implementation scripts within *skills directories* co-evolve at above-chance rates (**78% functional coupling**)—representing a maintenance dependency completely unique to AI agent engineering.

---

## 📋 Document Details & Links

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2608.28497) | [HTML 版本](https://arxiv.org/html/2608.28497v1) | [TeX 源码](https://arxiv.org/src/2608.28497)
* **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
* **文献计量工具：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.28497) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.28497) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.28497)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2608.28497) | [HTML Version](https://arxiv.org/html/2608.28497v1) | [TeX Source](https://arxiv.org/src/2608.28497)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
> * **Bibliographic Tools:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.28497) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.28497) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.28497)

---

## 🔍 Abstract

AI 编码智能体（通过推理和工具调用自动化开发任务的软件工具）正日益通过插件市场进行功能扩展，然而这些新兴代码库的结构、维护和共演化动态在经验上仍属未知。与通过源代码交付功能的传统软件包不同，智能体插件通过自然语言指令文件、脚本和配置文件的组合来交付功能，这就引发了一个问题：这些插件是跨组件共演化且得到维护的产物，还是开发者写过一次便无需再回顾的一次性制品？

为了研究智能体插件的维护和共演化，我们对托管 Claude Code 插件市场的 1,926 个代码库进行了实证研究，分析了跨越 2,018 个市场的 8,351 个插件和 77,773 次提交。我们发现，该市场正在迅速扩张，在 2025 年 10 月发布后的六个月内，涉及插件的提交活动增长了 8.8 倍，针对软件工程任务的插件占所有插件的 61.3%。插件开发主要由功能驱动，功能类提交的发生率是传统开源软件（OSS）的两倍以上（39.6% 对比 17.2%）。Claude 共同署名了 34.9% 的提交，并且四种提交类型（`docs`、`perf`、`style` 和 `refactor`）在插件代码库中的含义与传统软件有本质的不同。大多数组件类型是独立演化的，但在技能目录内，自然语言指令文件和实现脚本以高于随机概率的频率共演化，其中 78% 的共同变更是功能耦合的，这代表了一种在传统软件工程中未曾观察到的新型维护依赖关系。

> AI coding agents, software tools that automate development tasks through reasoning and tool use, are increasingly extended through plugin marketplaces, yet the structure, maintenance, and co-evolution dynamics of these emerging repositories remain empirically unexplored. Unlike traditional software packages that deliver functionality through source code, agent plugins deliver functionality through a combination of natural-language instruction files, scripts, and configuration files, raising the question of whether these plugins are maintained artifacts that co-evolve across components, or one-off artifacts that developers write once and do not need to revisit. 
>
> To study the maintenance and co-evolution of agent plugins, we conduct an empirical study of 1,926 repositories hosting Claude Code plugin marketplaces, analyzing 8,351 plugins and 77,773 commits across 2,018 marketplaces. We find that the marketplace is expanding rapidly, plugin-touching commit activity growing 8.8x over six months after the October 2025 launch, and plugins targeting Software Engineering tasks accounting for 61.3% of all plugins. Plugin development is predominantly feature-driven, with feature commits occurring at more than twice the rate of conventional open-source software (OSS) (39.6% vs. 17.2%). Claude co-authors 34.9% of all commits, and four commit types (docs, perf, style, and refactor) carry substantially different meanings in plugin repositories than in traditional software. Most component types evolve independently, but within skills directories, natural-language instruction files and implementation scripts co-evolve at above-chance rates, with 78% of co-changes being functionally coupled, representing a new class of maintenance dependency not observed in traditional software engineering.