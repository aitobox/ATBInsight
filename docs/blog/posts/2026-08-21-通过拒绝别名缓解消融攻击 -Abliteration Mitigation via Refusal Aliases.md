---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-21
hide:
- navigation
tags:
- 大语言模型
- 模型安全
- 消融攻击
- 模型编辑
- AMRA
title: 通过拒绝别名缓解消融攻击 (Abliteration Mitigation via Refusal Aliases)
---
### 文章背景与核心概要

“消融攻击”（Abliteration）是一种通过将权重矩阵投影到目标拒绝方向的正交空间，从而剥离大语言模型拒绝能力的技术，这构成了重大的安全隐患。现有的防御手段往往忽视了仅需少量对比提示词即可轻易定位并提取该拒绝方向的风险。

本文提出了 AMRA（通过拒绝别名缓解消融攻击），这是一种新型的权重编辑防御机制。AMRA 通过对残差流写入矩阵应用秩-$k$（rank-$k$）更新，用随机别名替换诱导拒绝的激活值，并校正下游读取矩阵，从而在掩盖拒绝信号的同时，确保模型能够保留其原始的行为效用。

---

# 通过拒绝别名缓解消融攻击 (Abliteration Mitigation via Refusal Aliases)

**作者：** Nathan Truong  
**提交日期：** 2026年6月7日  
**arXiv：** [2608.18093 [cs.CL]]  
**DOI：** [10.48550/arXiv.2608.18093](https://doi.org/10.48550/arXiv.2608.18093)  
**许可协议：** [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/) *(查看许可： <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">)*

---

## 📌 摘要
> Abliteration—the practice of stripping refusal capabilities from large language models by projecting weight matrices orthogonally to a targeted refusal direction—poses a significant safety vulnerability. Existing defenses often overlook how easily this refusal direction can be isolated and extracted using only a small set of contrastive prompts. 
> 
> To combat this, the paper introduces **AMRA (Abliteration Mitigation via Refusal Aliases)**, a novel weight-editing defense mechanism. AMRA obscures the refusal signal by applying rank-$k$ updates to residual stream writer matrices, replacing refusal-inducing activations with random aliases, and correcting downstream reader matrices to ensure the model retains its original behavioral utility.

消融攻击（Abliteration）——即通过将权重矩阵投影到目标拒绝方向的正交空间来剥离大语言模型拒绝能力的做法——构成了重大的安全漏洞。现有的防御措施往往忽视了仅使用少量对比提示词即可轻易隔离和提取该拒绝方向的风险。

为了应对这一问题，本文引入了 **AMRA（通过拒绝别名缓解消融攻击）**，这是一种新型的权重编辑防御机制。AMRA 通过对残差流写入矩阵应用秩-$k$ 更新来掩盖拒绝信号，用随机别名替换诱导拒绝的激活值，并校正下游读取矩阵，以确保模型保留其原始的行为效用。

---

## 📊 关键结果与性能
> * **Llama-3-8B:** Improves post-abliteration refusal scores by **2.16 points** over the undefended baseline while incurring less than **0.5 percentage points** of degradation on MMLU benchmarks.
> * **Gemma-2-9B:** Improves post-abliteration refusal scores by **14.70 points** over the baseline, maintaining comparable harmful output rates, though at a higher utility cost.

* **Llama-3-8B：** 在消融攻击后的拒绝得分上，较未防御基线提高了 **2.16 分**，同时在 MMLU 基准测试上的性能下降不到 **0.5 个百分点**。
* **Gemma-2-9B：** 在消融攻击后的拒绝得分上，较基线提高了 **14.70 分**，在保持相当的有害输出率的同时，付出了较高的效用成本。

---

## 🔗 链接与资源
> * **Full-Text Access:** [View PDF](/pdf/2608.18093) | [HTML (Experimental)](https://arxiv.org/html/2608.18093v1) | [TeX Source](/src/2608.18093)
> * **Explore Code & Tools:** [Hugging Face](https://huggingface.co/) | [CatalyzeX Code Finder](https://www.catalyzex.com) | [Connected Papers](https://www.connectedpapers.com/)
> * **Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.18093) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.18093) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.18093)

* **全文访问：** [查看 PDF](/pdf/2608.18093) | [HTML (实验性)](https://arxiv.org/html/2608.18093v1) | [TeX 源码](/src/2608.18093)
* **探索代码与工具：** [Hugging Face](https://huggingface.co/) | [CatalyzeX 代码查找器](https://www.catalyzex.com) | [Connected Papers](https://www.connectedpapers.com/)
* **引用：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.18093) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.18093) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.18093)