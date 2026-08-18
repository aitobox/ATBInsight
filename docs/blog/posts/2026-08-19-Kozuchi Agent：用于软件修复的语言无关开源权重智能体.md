---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 软件工程
- 大语言模型
- 自动化修复
- 开源权重
- SWE-bench
title: Kozuchi Agent：用于软件修复的语言无关开源权重智能体
---
### 文章背景与核心概要

工业软件工程团队日益迫切地需要能够将错误报告转化为正确补丁的LLM智能体。然而，在基准测试规模下进行操作时，面临着长周期任务、工具使用规范、上下文持久性、异构集群管理以及评估复用等诸多挑战。

Kozuchi Agent 是一款语言无关的开源权重软件修复智能体，并配套了由CI驱动的评估流水线。该系统通过明确的执行阶段、持久化状态、确定性工具链、模型无关的动作接口以及跨智能体的测试时选择（TTS）机制，实现了修复过程的可审计性和可重复性。

在不进行微调的情况下，Kozuchi 利用本地部署的 Qwen3.5-27B 模型，在 SWE-bench Verified 基准测试中成功解决了 500 个实例中的 374 个。在 Multi-SWE-bench Java 任务中，它以 32.03%（41/128）的解决率在所有严格开源权重提交中排名第一，在 42 个参赛系统中总排名第四，并在 Python 基准测试中表现出同等竞争力。该系统通过可复用的 CI 阶段，将异构集群中的操作触点从五个减少到一个，显著提升了运维效率。

---

## 摘要

> Industrial software-engineering teams increasingly need LLM agents that turn bug reports into correct patches, yet benchmark-scale operation adds long horizons, tool-use discipline, context persistence, heterogeneous clusters, and evaluation reuse. 

工业软件工程团队日益迫切地需要能够将错误报告转化为正确补丁的LLM智能体，然而在基准测试规模下进行操作时，面临着长周期任务、工具使用规范、上下文持久性、异构集群管理以及评估复用等诸多挑战。

> We present **Kozuchi Agent**, a language-agnostic open-weight repair agent and CI-operated evaluation pipeline. Explicit phases, persistent state, deterministic tools, a model-independent action interface, and cross-agent test-time selection make runs auditable and repeatable. 

我们提出了 **Kozuchi Agent**，这是一个语言无关的开源权重修复智能体及 CI 驱动的评估流水线。通过明确的执行阶段、持久化状态、确定性工具链、模型无关的动作接口以及跨智能体的测试时选择机制，使得运行过程具备可审计性和可重复性。

> With locally hosted Qwen3.5-27B, no fine-tuning, and TTS@8, Kozuchi resolves **374/500** SWE-bench Verified instances on the official evaluator. Unchanged on Multi-SWE-bench Java, the same 27-billion-parameter agent resolves **41/128 instances (32.03%)**, ranking first among strict open-weight submissions and fourth of 42 overall; on Python it ranks 12th of 135 and first among open-weight systems. Per-phase behavior remains within $\pm 5$ percentage points across languages. Remaining failures mainly reflect semantic correctness, Java-specific harness issues, and selection errors. 

在不进行微调的情况下，Kozuchi 利用本地部署的 Qwen3.5-27B 模型和 TTS@8 技术，在官方评估器上成功解决了 500 个 SWE-bench Verified 实例中的 374 个。在 Multi-SWE-bench Java 任务中，该 270 亿参数的智能体同样解决了 128 个实例中的 41 个（32.03%），在所有严格开源权重提交中排名第一，在 42 个参赛系统中总排名第四；在 Python 任务中，它在 135 个系统中排名第 12 位，在开源权重系统中排名第一。各阶段的行为在不同语言间保持在 $\pm 5$ 个百分点以内。剩余的失败主要源于语义正确性、Java 特有的测试框架问题以及选择错误。

> Across both tracks, results compare favorably with open/local peers by parameter count. Analysis of candidate diversity, selector regret, and patch reliability shows that the remaining gap is primarily semantic correctness and selection rather than edit formatting or proprietary-model access. Operationally, reusable CI stages reduce operator touch-points from five to one across heterogeneous internal clusters.

在两个赛道中，其结果与同参数规模的开源/本地模型相比表现优异。对候选多样性、选择器遗憾值（selector regret）和补丁可靠性的分析表明，目前的差距主要在于语义正确性和选择机制，而非编辑格式或对闭源模型的访问权限。在运维层面，可复用的 CI 阶段将异构内部集群的操作触点从五个减少到了一个。

---

## 文档元数据

| 字段 | 详情 |
| :--- | :--- |
| **arXiv 标识符** | `arXiv:2608.15579` [cs.SE] |
| **主要学科** | 软件工程 (`cs.SE`) |
| **次要学科** | 人工智能 (`cs.AI`), 新兴技术 (`cs.ET`), 编程语言 (`cs.PL`) |
| **提交日期** | 2026年8月16日 |
| **会议地点** | 已被第 41 届 IEEE/ACM 自动化软件工程国际会议 (ASE '26) 录用，工业展示赛道，德国慕尼黑（2026年10月12–16日） |
| **数字对象标识符 (DOI)** | `10.48550/arXiv.2608.15579` (相关 DOI: `10.1145/3832783.3834531`) |

---

## 作者

Mehdi Bahrami, Kosaku Kimura, Satoshi Munakata, Satoshi Nakashima, Yu Ishikawa, Kosuke Maeda, Nao Soma, Kenichi Kobayashi, Keisuke Miyazaki, Keizo Kato, Shigeki Fukuta, Tatsuo Kumano, Nobutaka Imamura, Kevin Musgrave, Shahbaz Abdul Khader, Kwun Ho Ngan, Joe Townsend, Fayas Asharindavida, Matthieu Parizy, Akira Sakai, Yuma Ichikawa, Yang Zhao, Michiaki Takizawa, Taku Fukui, Hiroki Ohtsuji, Wei-Peng Chen, and Hiromichi Kobashi.

---

## 更多资源与链接

* **全文访问：** [查看 PDF](/pdf/2608.15579) | [HTML (实验性)](https://arxiv.org/html/2608.15579v1) | [TeX 源码](/src/2608.15579)
* **许可协议：** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/)
* **外部引用：** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.15579) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.15579) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.15579)