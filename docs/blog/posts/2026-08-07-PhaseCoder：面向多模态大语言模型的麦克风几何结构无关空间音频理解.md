---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-07
hide:
- navigation
tags:
- 多模态大模型
- 空间音频
- 音频处理
- 麦克风几何无关
- 具身智能
title: PhaseCoder：面向多模态大语言模型的麦克风几何结构无关空间音频理解
---
### 文章背景与核心概要
当前的各类多模态大语言模型（LLM）通常将音频处理为单声道流，从而忽略了对于具身智能至关重要的丰富空间信息。与此同时，现有的空间音频模型往往受限于固定的麦克风几何结构，无法在各类不同的设备上进行部署。

为了解决这一痛点，本文作者推出了 **PhaseCoder**——一个纯 Transformer 架构的、对麦克风几何结构不敏感的空间音频编码器。PhaseCoder 将原始多通道音频以及麦克风坐标作为输入来执行定位，并生成稳健的空间嵌入。该论文证明了可以通过微调 Gemma 3n 大模型，使其能够对 PhaseCoder 生成的“空间音频令牌（Spatial Audio Tokens）”进行推理。该编码器在麦克风不变定位基准测试中取得了最先进（SOTA）的成果，并首次赋能大语言模型，使其能够从任意麦克风阵列中执行复杂的空间推理和定向转录任务。

---

# PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Understanding for Multimodal LLMs

> # PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Understanding for Multimodal LLMs

## Summary
* **arXiv ID:** `arXiv:2601.21124` [cs.SD]
* **Subjects:** Sound (`cs.SD`), Artificial Intelligence (`cs.AI`), Audio and Speech Processing (`eess.AS`)
* **Authors:** Artem Dementyev, Wazeer Zulfikar, Sinan Hersek, Pascal Getreuer, Anurag Kumar, Vivek Kumar
* **Submission Dates:** Submitted on 28 January 2026; last revised 5 August 2026 (v2)

> ## Summary
> * **arXiv ID:** `arXiv:2601.21124` [cs.SD]
> * **Subjects:** Sound (`cs.SD`), Artificial Intelligence (`cs.AI`), Audio and Speech Processing (`eess.AS`)
> * **Authors:** Artem Dementyev, Wazeer Zulfikar, Sinan Hersek, Pascal Getreuer, Anurag Kumar, Vivek Kumar
> * **Submission Dates:** Submitted on 28 January 2026; last revised 5 August 2026 (v2)

---

## Abstract
Current multimodal LLMs process audio as a mono stream, ignoring the rich spatial information essential for embodied AI. Existing spatial audio models, conversely, are constrained to fixed microphone geometries, preventing deployment across diverse devices. 

The authors present **PhaseCoder**, a transformer-only spatial audio encoder that is agnostic to microphone geometry. PhaseCoder takes raw multichannel audio and microphone coordinates as inputs to perform localization and produces robust spatial embeddings. The paper demonstrates that the Gemma 3n LLM can be fine-tuned to reason over "Spatial Audio Tokens" produced by PhaseCoder. The encoder achieves state-of-the-art results on microphone-invariant localization benchmarks and, for the first time, enables an LLM to perform complex spatial reasoning and targeted transcription tasks from an arbitrary microphone array.

> ## Abstract
> Current multimodal LLMs process audio as a mono stream, ignoring the rich spatial information essential for embodied AI. Existing spatial audio models, conversely, are constrained to fixed microphone geometries, preventing deployment across diverse devices. 
> 
> The authors present **PhaseCoder**, a transformer-only spatial audio encoder that is agnostic to microphone geometry. PhaseCoder takes raw multichannel audio and microphone coordinates as inputs to perform localization and produces robust spatial embeddings. The paper demonstrates that the Gemma 3n LLM can be fine-tuned to reason over "Spatial Audio Tokens" produced by PhaseCoder. The encoder achieves state-of-the-art results on microphone-invariant localization benchmarks and, for the first time, enables an LLM to perform complex spatial reasoning and targeted transcription tasks from an arbitrary microphone array.

---

## Access & Resources

* **Full-Text Links:**
  * [View PDF](https://arxiv.org/pdf/2601.21124)
  * [HTML (Experimental)](https://arxiv.org/html/2601.21124v2)
  * [TeX Source](https://arxiv.org/src/2601.21124)
* **DOI:** [10.48550/arXiv.2601.21124](https://doi.org/10.48550/arXiv.2601.21124)
* **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) *(<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> view license)*

> ## Access & Resources
> 
> * **Full-Text Links:**
>   * [View PDF](https://arxiv.org/pdf/2601.21124)
>   * [HTML (Experimental)](https://arxiv.org/html/2601.21124v2)
>   * [TeX Source](https://arxiv.org/src/2601.21124)
> * **DOI:** [10.48550/arXiv.2601.21124](https://doi.org/10.48550/arXiv.2601.21124)
> * **License:** [Creative Commons Attribution 4.0 International](http://creativecommons.org/licenses/by/4.0/) *(<img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"> view license)*

---

## References & External Tools
* **Citations:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2601.21124) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2601.21124) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2601.21124)
* **Bookmarks:** [BibSonomy](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2601.21124&description=PhaseCoder:%20Microphone%20Geometry-Agnostic%20Spatial%20Audio%20Understanding%20for%20Multimodal%20LLMs) | [Reddit](https://reddit.com/submit?url=https://arxiv.org/abs/2601.21124&title=PhaseCoder:%20Microphone%20Geometry-Agnostic%20Spatial%20Audio%20Understanding%20for%20Multimodal%20LLMs)

> ## References & External Tools
> * **Citations:** [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2601.21124) | [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2601.21124) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2601.21124)
> * **Bookmarks:** [BibSonomy](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2601.21124&description=PhaseCoder:%20Microphone%20Geometry-Agnostic%20Spatial%20Audio%20Understanding%20for%20Multimodal%20LLMs) | [Reddit](https://reddit.com/submit?url=https://arxiv.org/abs/2601.21124&title=PhaseCoder:%20Microphone%20Geometry-Agnostic%20Spatial%20Audio%20Understanding%20for%20Multimodal%20LLMs)