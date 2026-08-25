---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- KV Cache
- Sigmoid Attention
- Transformer
- 模型推理优化
- 大语言模型
title: Sigmoid Attention：构建学习型 KV 缓存淘汰的更优底层架构
---
### 文章背景与核心概要
在大语言模型（Transformer）的推理过程中，键值（KV）缓存的内存开销往往随着上下文长度的增加而急剧膨胀，因此 KV 缓存淘汰技术备受关注。然而，现有的“学习型 KV 缓存淘汰”方法常常面临“软-硬不匹配（soft-to-hard mismatch）”的痛点：在训练阶段，模型通常依赖可微门控机制来衰减某些 Token 的贡献；但在实际推理时，只有物理移除对应的 KV 条目才能真正节省内存。这种训练时软门控与推理时硬删除的脱节，导致模型性能在实际淘汰时显著下降。

为了解决这一问题，本文作者 Isaac (Rucheng) Li 深入探究了注意力机制的底层选择是否会影响这一过渡过程。通过在 GPT-2 规模的模型上进行受控的 $2\times2\times2$ 实验，作者发现：尽管 Sigmoid Attention 作为标准的稠密语言模型时表现逊于 Softmax，但它却是实现学习型硬淘汰的更优底层架构。使用学习型 Sigmoid 门控的模型在删除 KV 条目时，其困惑度（PPL）变化微乎其微，显著优于 $H_2O$ 和 KeyDiff 等事后（post-hoc）淘汰方法。该研究表明，注意力归一化方式会极大影响训练时的软门控能否顺利转化为推理时的硬 KV 删除。

---

# Sigmoid Attention as a Better Substrate for Learned KV Cache Eviction

> ## Summary
> Learned KV-cache eviction in Transformers often encounters a "soft-to-hard mismatch": training relies on differentiable gates that attenuate token contributions, whereas inference only achieves memory savings when Key-Value (KV) entries are physically removed. This paper investigates whether the choice of attention substrate impacts this transition. Through controlled $2\times2\times2$ experiments on GPT-2-scale models, the author demonstrates that while sigmoid attention performs worse as a standard dense language model, it serves as a superior substrate for learned hard eviction. Models using learned sigmoid gates can delete KV entries with negligible perplexity (PPL) changes relative to their baseline models, outperforming post-hoc methods like $H_2O$ and KeyDiff.

---

## Paper Metadata

| Field | Details |
| :--- | :--- |
| **Title** | Sigmoid Attention as a Better Substrate for Learned KV Cache Eviction |
| **Author** | Isaac (Rucheng) Li |
| **Submitted On** | August 24, 2026 |
| **Primary Subject** | Machine Learning (`cs.LG`) |
| **Secondary Subjects** | Artificial Intelligence (`cs.AI`) |
| **Conference Venue** | Accepted at the ICML 2026 Workshop on Resource-Adaptive Foundation Model Inference (AdaptFM) |
| **arXiv ID** | [arXiv:2608.23296](https://arxiv.org/abs/2608.23296) |
| **DOI** | [10.48550/arXiv.2608.23296](https://doi.org/10.48550/arXiv.2608.23296) |

---

## Abstract
学习型 KV 缓存淘汰常常面临软-硬不匹配问题：在训练过程中，可微门控通常会衰减 Token 的贡献，而在推理时，只有物理移除 KV 条目才能节省内存。我们探讨了注意力底层架构是否会影响这种软到硬的过渡。通过使用在 OpenWebText 上训练的 GPT-2 规模 Transformer，我们针对注意力类型、学习型门控和位置编码进行了受控的 $2\times2\times2$ 对比实验。

> Learned KV-cache eviction often faces a soft-to-hard mismatch: during training, differentiable gates typically attenuate token contributions, whereas inference saves memory only when KV entries are physically removed. We ask whether the attention substrate affects this soft-to-hard transition. Using GPT-2-scale Transformers trained on OpenWebText, we run a controlled $2\times2\times2$ comparison over attention type, learned gating, and positional encoding.

尽管 Sigmoid Attention 作为稠密语言模型时表现较差，但学习型硬淘汰改变了其有用的工作点：使用 Sigmoid 门控的模型在删除 KV 条目时，其困惑度（PPL）相对于无淘汰的基线模型而言变化微乎其微。在相同的稠密主干网络及匹配的动态缓存协议下，学习型 Sigmoid 门控取得了比我们实现的 $H_2O$ 和 KeyDiff 更低的 PPL，而 Softmax 门控则无法在所有情况下都超越这些事后淘汰方法。结果表明，注意力归一化会显著影响训练时的软门控能否干净利落地转化为硬 KV 删除。

> Although sigmoid attention is worse as a dense language model, learned hard eviction changes the useful operating points: sigmoid-gated models delete KV entries with negligible PPL change relative to their own no-eviction references. Under a matched live-cache protocol on the same dense backbones, learned sigmoid gates obtain lower PPL than our $H_2O$ and KeyDiff implementations, whereas softmax gates do not uniformly beat these post-hoc methods. The results suggest that attention normalization can substantially affect whether a training-time soft gate transfers cleanly to hard KV deletion.

---

## Access Links & Resources
* **PDF Version:** [View PDF](https://arxiv.org/pdf/2608.23296)
* **TeX Source:** [Download Source](https://arxiv.org/src/2608.23296)
* **Citations & Tools:** 
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.23296)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.23296)
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.23296)