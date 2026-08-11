---
authors:
- aitoboxrobot
categories:
- 研究解读
date: 2026-08-12
hide:
- navigation
tags:
- SignLlama
- 大语言模型
- 手语翻译
- 计算机视觉
- 多模态学习
title: SignLlama：通过优先处理视觉特征增强无词汇表手语翻译
---
### 文章背景与核心概要

SignLlama 是一项旨在将大语言模型（LLM）应用于“无词汇表手语翻译”（GFSLT）的创新研究。尽管 LLM 在多种任务中表现出色，但将其直接应用于手语翻译时，往往面临视觉与文本特征分布不匹配，以及模型因过度依赖文本预训练而忽视视觉信息的问题。

为了解决这些挑战，作者提出了两种核心策略：一是“过滤伪词汇表 CTC 预训练”，通过利用从文本生成的伪词汇表序列来监督视觉主干网络；二是“视觉优先蒸馏”，通过掩盖文本输入并强制模型仅依赖视觉特征进行预测，从而引导模型提升对视觉信息的关注度。实验证明，SignLlama 在无需额外模态或外部手语预训练数据集的情况下，在多个基准测试中均取得了极具竞争力的性能。

---

## 📄 摘要

大型语言模型（LLM）在广泛的任务中取得了显著成功。然而，针对无词汇表手语翻译（GFSLT）任务对 LLM 进行微调仍然是一个挑战。在本文中，我们研究了如何有效地使 LLM 适应 GFSLT 任务。我们指出有两个关键问题需要解决：（1）视觉特征输入与文本特征输入之间固有的分布差异，使得 LLM 难以解释视觉输入；（2）现有方法通常在自回归框架中拼接视觉和文本特征，这导致模型过度强调文本输入而降低了视觉线索的优先级，因为 LLM 主要是在以文本为中心的数据上进行预训练的。为了解决第一个挑战，我们提出了一种简单而有效的方法，即“过滤伪词汇表 CTC 预训练”（Filtered Pseudo-Gloss CTC Pretraining），它利用从文本序列生成的过滤伪词汇表序列来监督视觉主干网络的训练。为了解决第二个问题，我们引入了一种“视觉优先蒸馏”（Visual-Prioritized Distillation）训练策略。具体而言，我们定义了一条仅包含视觉的预测路径，其中文本输入被掩盖，模型被要求仅依赖视觉输入来生成目标序列。为了引导该路径，来自标准视觉-文本预测的输出被蒸馏到仅视觉的预测路径中，从而鼓励模型优先处理视觉特征。综合实验和定性分析证明了所提模型的有效性。所提出的 SignLlama 在多个 GFSLT 任务数据集上实现了极具竞争力的性能，且无需使用任何额外的模态或外部手语数据集进行预训练。

> Large Language Models (LLMs) have achieved remarkable success across a wide range of tasks. However, fine-tuning LLMs for Gloss-Free Sign Language Translation (GFSLT) remains a challenge. In this paper, we investigate how to effectively adapt LLMs to the GFSLT task. We show that there are two key issues that need to be solved: (1) the inherent distributional gap between visual feature inputs and text feature inputs makes it difficult for LLMs to interpret visual inputs; and (2) existing approaches typically concatenate visual and textual features in an autoregressive framework, which leads to the model overemphasizing textual inputs and deprioritizing visual cues, as LLMs are pretrained predominantly on text-centric data. To address the first challenge, we propose a simple yet effective method named Filtered Pseudo-Gloss CTC Pretraining, which leverages filtered pseudo-gloss sequences generated from text sequences to supervise the training of the visual backbone. To tackle the second issue, we introduce a Visual-Prioritized Distillation training strategy. Specifically, we define a visual-only prediction path in which text inputs are masked, and the model is required to generate the target sequence relying solely on visual inputs. To guide this path, the outputs from the standard visual-textual prediction are then distilled into the visual-only prediction path, encouraging the model to prioritize visual features. Comprehensive experiments and qualitative analyses demonstrate the effectiveness of the proposed model. The proposed SignLlama achieves very competitive performance on multiple datasets for GFSLT tasks, without using any extra modalities or external sign language datasets for pretraining.

---

## 🔗 链接与资源

* **全文选项：**
  * [查看 PDF](https://arxiv.org/pdf/2608.09006)
  * [HTML (实验性)](https://arxiv.org/html/2608.09006v1)
  * [TeX 源码](https://arxiv.org/src/2608.09006)
* **外部索引：**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.09006)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.09006)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.09006)
* **许可协议：** [知识共享 署名-非商业性使用-禁止演绎 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-nd/4.0/)

> * **Full-Text Options:** 
>   * [View PDF](https://arxiv.org/pdf/2608.09006)
>   * [HTML (Experimental)](https://arxiv.org/html/2608.09006v1)
>   * [TeX Source](https://arxiv.org/src/2608.09006)
> * **External Indices:**
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.09006)
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.09006)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.09006)
> * **License:** [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/)