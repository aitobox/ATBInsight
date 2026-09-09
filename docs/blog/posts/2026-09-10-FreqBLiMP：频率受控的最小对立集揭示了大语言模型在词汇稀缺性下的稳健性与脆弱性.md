---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-10
hide:
- navigation
tags:
- 大语言模型
- 语言学基准
- 词汇频率
- BLiMP
- EMNLP 2026
title: FreqBLiMP：频率受控的最小对立集揭示了大语言模型在词汇稀缺性下的稳健性与脆弱性
---
### 文章背景与核心概要
大语言模型（LLMs）的语言学能力评估通常依赖于像 BLiMP 这样的最小对立集（minimal-pair）基准，但传统评估往往忽视了词汇频率这一自然语言中的关键变量。为此，研究者 Tyrone White 和 Yuki Arase 推出了 FreqBLiMP——一个在显式齐普夫频率（Zipf-frequency）机制下重建所有 67 个范式的基准扩展。

通过对多种开源大模型系列进行跨规模评估，研究发现：虽然降低词汇频率会导致句子似然度（likelihood）的单调下降，但总体对比可接受性准确率仅出现小幅下降。然而，这种宏观上的稳定性掩盖了深层的模型脆弱性：模型在处理外显的形态句法泛化时表现出强劲的稳健性，但在依赖特定引理（lemma-specific）信息的语言学现象上则显著退化。这项工作已被 EMNLP 2026 主会接受。

---

# FreqBLiMP: Frequency-Controlled Minimal Pairs Reveal Robustness and Fragility of LLMs Under Lexical Rarity

> FreqBLiMP: Frequency-Controlled Minimal Pairs Reveal Robustness and Fragility of LLMs Under Lexical Rarity

[![license icon](./images/345c7ad61f1b.png)](http://creativecommons.org/licenses/by/4.0/)

> [![license icon](./images/345c7ad61f1b.png)](http://creativecommons.org/licenses/by/4.0/)

## Summary

> ## Summary

**FreqBLiMP** is a frequency-controlled extension of the BLiMP benchmark designed to evaluate how lexical rarity affects the linguistic knowledge of Large Language Models (LLMs). While traditional minimal-pair benchmarks test whether models prefer grammatically acceptable sentences over unacceptable ones, they typically ignore lexical frequency variation. 

> **FreqBLiMP** is a frequency-controlled extension of the BLiMP benchmark designed to evaluate how lexical rarity affects the linguistic knowledge of Large Language Models (LLMs). While traditional minimal-pair benchmarks test whether models prefer grammatically acceptable sentences over unacceptable ones, they typically ignore lexical frequency variation. 

By regenerating all 67 paradigms under explicit Zipf-frequency regimes, researchers Tyrone White and Yuki Arase evaluated open-weight LLM families across various scales. Their findings reveal that while decreasing lexical frequency consistently reduces sentence likelihood, the overall contrastive acceptability accuracy experiences only a modest decline. However, this aggregate stability masks deeper vulnerabilities: LLMs remain robust when handling overt morphosyntactic generalizations, but degrade significantly on phenomena requiring lemma-specific information.

> By regenerating all 67 paradigms under explicit Zipf-frequency regimes, researchers Tyrone White and Yuki Arase evaluated open-weight LLM families across various scales. Their findings reveal that while decreasing lexical frequency consistently reduces sentence likelihood, the overall contrastive acceptability accuracy experiences only a modest decline. However, this aggregate stability masks deeper vulnerabilities: LLMs remain robust when handling overt morphosyntactic generalizations, but degrade significantly on phenomena requiring lemma-specific information.

---

> ---

## Paper Metadata

> ## Paper Metadata

* **arXiv ID:** [arXiv:2609.07153 [cs.CL]](https://arxiv.org/abs/2609.07153)
* **Authors:** Tyrone White, Yuki Arase
* **Primary Subject:** Computation and Language (`cs.CL`)
* **Other Subjects:** Artificial Intelligence (`cs.AI`)
* **Submission Date:** September 7, 2026
* **Conference Status:** Accepted to EMNLP 2026 Main Conference
* **Repository:** [GitHub - freqblimp-generation](https://github.com/TimeTravelerTy/freqblimp-generation)

> * **arXiv ID:** [arXiv:2609.07153 [cs.CL]](https://arxiv.org/abs/2609.07153)
> * **Authors:** Tyrone White, Yuki Arase
> * **Primary Subject:** Computation and Language (`cs.CL`)
> * **Other Subjects:** Artificial Intelligence (`cs.AI`)
> * **Submission Date:** September 7, 2026
> * **Conference Status:** Accepted to EMNLP 2026 Main Conference
> * **Repository:** [GitHub - freqblimp-generation](https://github.com/TimeTravelerTy/freqblimp-generation)

---

> ---

## Abstract

> ## Abstract

Minimal-pair benchmarks such as BLiMP evaluate linguistic knowledge by testing whether language models (LMs) prefer acceptable sentences over minimally different unacceptable ones. However, these benchmarks largely ignore lexical frequency variation, despite lexical frequency being a pervasive and highly skewed property of natural language use. Consequently, existing evaluations do not test whether grammatical preferences remain stable when contrasts involve rare lexical items. 

> Minimal-pair benchmarks such as BLiMP evaluate linguistic knowledge by testing whether language models (LMs) prefer acceptable sentences over minimally different unacceptable ones. However, these benchmarks largely ignore lexical frequency variation, despite lexical frequency being a pervasive and highly skewed property of natural language use. Consequently, existing evaluations do not test whether grammatical preferences remain stable when contrasts involve rare lexical items. 

We introduce `FreqBLiMP`, a frequency-controlled extension of BLiMP that regenerates all 67 paradigms under explicit Zipf-frequency regimes while preserving each minimal-pair's grammatical contrast. Evaluating multiple open-weight LLM families across scales, we find that decreasing lexical frequency produces a consistent, monotonic decrease in sentence likelihood, but only a modest reduction in overall contrastive acceptability accuracy. However, this aggregate stability masks substantial variation across linguistic phenomena, with LLMs remaining robust on overt morphosyntactic generalization while degrading on phenomena that require lemma-specific information.

> We introduce `FreqBLiMP`, a frequency-controlled extension of BLiMP that regenerates all 67 paradigms under explicit Zipf-frequency regimes while preserving each minimal-pair's grammatical contrast. Evaluating multiple open-weight LLM families across scales, we find that decreasing lexical frequency produces a consistent, monotonic decrease in sentence likelihood, but only a modest reduction in overall contrastive acceptability accuracy. However, this aggregate stability masks substantial variation across linguistic phenomena, with LLMs remaining robust on overt morphosyntactic generalization while degrading on phenomena that require lemma-specific information.

---

> ---

## Access Links

> ## Access Links

* **PDF:** [View PDF](https://arxiv.org/pdf/2609.07153)
* **HTML:** [arXiv HTML (Experimental)](https://arxiv.org/html/2609.07153v1)
* **Source:** [TeX Source](https://arxiv.org/src/2609.07153)
* **DOI:** [10.48550/arXiv.2609.07153](https://doi.org/10.48550/arXiv.2609.07153)

> * **PDF:** [View PDF](https://arxiv.org/pdf/2609.07153)
> * **HTML:** [arXiv HTML (Experimental)](https://arxiv.org/html/2609.07153v1)
> * **Source:** [TeX Source](https://arxiv.org/src/2609.07153)
> * **DOI:** [10.48550/arXiv.2609.07153](https://doi.org/10.48550/arXiv.2609.07153)