---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-21
hide:
- navigation
tags:
- 大模型智能体
- 软件工程
- 自动代码修复
- 知识蒸馏
- SkillForge
title: SkillForge：面向特定项目问题解决的自我蒸馏智能体
---
### 文章背景与核心概要
本文介绍了来自上海交通大学等机构的研究团队提出的全新框架——**SkillForge**。在大语言模型（LLM）用于自动化软件问题解决时，智能体往往因为缺乏特定项目的领域知识而在特定代码库中表现不佳。现有的自进化方法要么过度依赖历史问题解决信号，要么在测试时产生极高的探索成本。

为了突破这一瓶颈，SkillForge 提出了一种创新的自我蒸馏框架，能够通过主动综合和解决从测试覆盖的核心功能中派生的项目特定问题，来积极获取代码库知识。该方法将可重用的知识蒸馏为基于实体（entity-grounded）的技能，并将其与相关的代码库实体关联，从而显著提升了开源和闭源模型在下游问题解决中的性能。

---

# SkillForge: Self-Distilling Agents for Project-Specific Issue Resolution

## Summary
Large language model (LLM) agents often struggle with automated software issue resolution in specific repositories due to a lack of project-specific knowledge. Existing self-evolving approaches either rely heavily on historical issue-resolution signals or incur high exploration costs. **SkillForge** introduces a novel self-distillation framework that proactively acquires repository knowledge by synthesizing and resolving project-specific issues derived from test-covered core functionalities. This approach distills reusable knowledge into entity-grounded skills, significantly enhancing downstream issue-resolution performance across both open-source and closed-source models.

> 大语言模型（LLM）智能体通常在特定代码库中进行自动化软件问题解决时表现不佳，这是由于缺乏特定项目的知识。现有的自进化方法要么严重依赖历史问题解决信号，要么产生高昂的探索成本。**SkillForge** 引入了一种新颖的自我蒸馏框架，通过综合和解决从测试覆盖的核心功能中派生的特定项目问题，主动获取代码库知识。这种方法将可重用的知识蒸馏为基于实体的技能，显著增强了开源和闭源模型在下游问题解决中的性能。

---

## Metadata & Document Information

| Attribute | Details |
| :--- | :--- |
| **arXiv ID** | [arXiv:2608.18933](https://arxiv.org/abs/2608.18933) [cs.SE] |
| **Subject Areas** | Software Engineering (`cs.SE`), Artificial Intelligence (`cs.AI`) |
| **Submission Date** | August 19, 2026 |
| **Authors** | Silin Chen, Han Li, Xiaodong Gu, Yuling Shi, Haibing Guan |
| **Code & Data Repository** | [GitHub - SkillForge](https://github.com/cslsolow/SkillForge) |
| **License** | [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> |

---

## Abstract
Large language model (LLM) based agents have demonstrated remarkable proficiency in automated software issue resolution, yet they often struggle to resolve issues in a specific repository because they lack project-specific knowledge. Existing self-evolving approaches acquire such knowledge from repository history or online repair trajectories, but they either depend on available historical issue-resolution signals or incur substantial per-issue test-time exploration cost. 

In this paper, we propose **SkillForge**, a self-distillation framework that proactively acquires project-specific knowledge from the repository itself. Instead of waiting for real issues to expose project-specific knowledge gaps, SkillForge synthesizes project-specific issues by re-implementing test-covered core functionalities of the repository. By resolving these synthetic issues, SkillForge distills reusable project-specific knowledge into entity-grounded skills and associates them with relevant repository entities for future issue resolution. 

Extensive experiments using both open-source and closed-source models show that SkillForge consistently improves issue resolution performance over strong baselines. These results demonstrate that proactively acquiring project-specific knowledge before solving real issues substantially improves downstream software issue resolution.

> 基于大语言模型（LLM）的智能体在自动化软件问题解决方面表现出卓越的熟练度，然而由于缺乏特定项目的知识，它们在特定代码库中解决问题时往往面临困难。现有的自进化方法从代码库历史或在线修复轨迹中获取此类知识，但它们要么依赖于可用的历史问题解决信号，要么在每个问题上产生大量的测试时探索成本。
> 
> 在本文中，我们提出了 **SkillForge**，这是一个从代码库本身主动获取特定项目知识的自我蒸馏框架。SkillForge 没有等待真实问题暴露出特定项目的知识空白，而是通过重新实现代码库中测试覆盖的核心功能来合成特定项目的问题。通过解决这些合成问题，SkillForge 将可重用的特定项目知识蒸馏为基于实体的技能，并将它们与相关的代码库实体关联起来，以用于未来的问题解决。
> 
> 使用开源和闭源模型的广泛实验表明，与强基线相比，SkillForge 持续提升了问题解决性能。这些结果证明，在解决真实问题之前主动获取特定项目的知识，可以显着改善下游的软件问题解决能力。

---

## Access & Full-Text Links

* **PDF Version:** [View PDF](https://arxiv.org/pdf/2608.18933)
* **HTML Version:** [HTML (Experimental)](https://arxiv.org/html/2608.18933v1)
* **TeX Source:** [arXiv e-Print Source](https://arxiv.org/src/2608.18933)
* **DOI:** [10.48550/arXiv.2608.18933](https://doi.org/10.48550/arXiv.2608.18933)

---

## External References & Tools
* **Academic Databases:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.18933) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.18933) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.18933)
* **Associated Platforms:** [Hugging Face](https://huggingface.co/) | [CatalyzeX Code Finder](https://www.catalyzex.com) | [Connected Papers](https://www.connectedpapers.com/)