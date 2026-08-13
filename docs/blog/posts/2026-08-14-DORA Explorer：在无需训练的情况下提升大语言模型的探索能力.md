---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- 大语言模型
- 智能体探索
- 强化学习
- 推理时优化
- 多臂老虎机
title: DORA Explorer：在无需训练的情况下提升大语言模型的探索能力
---
### 文章背景与核心概要
在大语言模型（LLM）被应用于序列决策任务时，智能体常常面临输出多样性不足的问题，这会导致探索不充分、动作重复以及生成次优解。虽然传统的温度缩放（temperature scaling）等采样方法能够在单个词元（token）级别增加多样性，但它们无法在真正生成动作的序列级别上引入足够的多样性。

为了解决这一痛点，本文作者推出了 **DORA Explorer**（面向多样性的动作排序算法，**D**iversity-**O**riented **R**anking of **A**ctions）。这是一种无需训练的推理时算法，旨在增强智能体的探索能力。DORA 的工作原理是：生成多个候选动作，利用序列级别的对数概率统计数据对其进行评分，并使用一个可调节的探索参数来有效地采样动作。

---

# DORA Explorer: Improving the Exploration Ability of LLMs Without Training

> ## 📋 Summary
> Large Language Model (LLM) agents used for sequential decision-making often suffer from a lack of output diversity, leading to insufficient exploration, repetitive actions, and suboptimal solutions. While traditional sampling methods like temperature scaling add diversity at the individual token level, they fail to introduce diversity at the sequence level where actions are actually generated. 
> 
> To solve this, the authors introduce **DORA Explorer** (**D**iversity-**O**riented **R**anking of **A**ctions), a training-free inference-time algorithm designed to enhance agent exploration. DORA works by generating multiple candidate actions, scoring them using sequence-level log-probability statistics, and using a tunable exploration parameter to sample actions effectively. 

### 核心亮点：
* **经典多臂老虎机性能：** 在标准的多臂老虎机（bandit）设置中，DORA 的性能显著优于传统的基于温度的采样方法。
* **文本冒险学习（TALES）：** 尽管标准的提示词策略在探索上面临困难，但 DORA 在各个模型系列中都带来了持续的性能提升（例如，在 TextWorld 中结合 ReAct 与 DORA，将 Qwen-2.5 7B 的性能从 **31.43% 提升至 45.5%**）。
* **鲁棒性：** 除了增强探索能力，DORA 还成功防止了智能体常见的失败模式，例如陷入重复执行的死循环。

> ### Key Highlights:
> * **Classic Multi-Armed Bandit Performance:** DORA significantly outperforms traditional temperature-based sampling in standard bandit settings.
> * **Text Adventure Learning (TALES):** While standard prompting strategies struggle with exploration, DORA delivers consistent performance gains across various model families (e.g., boosting Qwen-2.5 7B from **31.43% to 45.5%** using ReAct vs. DORA in TextWorld).
> * **Robustness:** Beyond boosting exploration, DORA successfully prevents common agent failure modes, such as getting trapped in repetitive execution loops.

---

## 📄 元数据与出版详情

> ## 📄 Metadata & Publication Details

* **arXiv 标识符：** [arXiv:2604.17244](https://arxiv.org/abs/2604.17244) [cs.CL]
* **主要学科：** 计算与语言 (`cs.CL`)
* **次要学科：** 人工智能 (`cs.AI`)
* **作者：** 
  * Priya Gurjar
  * Md Farhan Ishmam
  * Kenneth Marino
* **提交历史：** 
  * 2026年4月19日提交 (v1)
  * 2026年8月11日最后修订 (v2 — 17页，6张图表，13个表格)
* **项目主页 / 代码：** [DORA Explorer 网站](https://dora-explore.github.io/)

> * **arXiv Identifier:** [arXiv:2604.17244](https://arxiv.org/abs/2604.17244) [cs.CL]
> * **Primary Subject:** Computation and Language (`cs.CL`)
> * **Secondary Subjects:** Artificial Intelligence (`cs.AI`)
> * **Authors:** 
>   * Priya Gurjar
>   * Md Farhan Ishmam
>   * Kenneth Marino
> * **Submission History:** 
>   * Submitted on 19 Apr 2026 (v1)
>   * Last revised on 11 Aug 2026 (v2 — 17 pages, 6 figures, 13 tables)
> * **Project Page / Code:** [DORA Explorer Website](https://dora-explore.github.io/)

---

## 🔗 快速链接与资源

> ## 🔗 Quick Links & Resources

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2604.17244) | [实验性 HTML](https://arxiv.org/html/2604.17244v2) | [TeX 源码](https://arxiv.org/src/2604.17244)
* **许可协议：** [知识共享署名 4.0 国际版](http://creativecommons.org/licenses/by/4.0/)
* **外部工具与引用：** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2604.17244)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2604.17244)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2604.17244)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2604.17244) | [Experimental HTML](https://arxiv.org/html/2604.17244v2) | [TeX Source](https://arxiv.org/src/2604.17244)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/)
> * **External Tools & Citations:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2604.17244)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2604.17244)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2604.17244)