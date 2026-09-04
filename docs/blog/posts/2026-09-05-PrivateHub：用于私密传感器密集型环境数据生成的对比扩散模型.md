---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 隐私保护
- 扩散模型
- 对比学习
- 传感器数据
- 数据合成
title: PrivateHub：用于私密传感器密集型环境数据生成的对比扩散模型
---
### 文章背景与核心概要
在现代智能环境中，传感器密集型系统通过收集异构数据流来推断用户的应用行为，从而提供智能服务。然而，这也引发了一个根本性冲突：用户希望享受有用的服务推断，同时又需要保护某些个人活动不被泄露。传统的隐私保护方法（如差分隐私和基于规则的过滤）通常只能保护孤立的数据流，无法有效应对由*跨传感器推断*带来的隐私风险。

为了解决这一挑战，本文作者推出了 **PrivateHub**，这是一个将对比学习与扩散模型相结合的新颖框架。PrivateHub 能够生成合成的多传感器数据流，在保持非私密应用可检测性的同时，成功掩盖私密应用。该框架主要包含两个阶段：应用条件预训练（ACP）利用应用嵌入对多传感器数据进行扩散模型条件化；应用感知微调（AAF）则利用对比学习显式地区分私密数据与非私密数据。

在三个真实世界的多传感器数据集上的评估表明，PrivateHub 在不降低非私密应用性能的前提下，将私密应用的推断准确率降低了 **40% 至 50%**，并且在攻击者利用合成数据重新训练模型时仍能保持稳健性。

---

# PrivateHub: Contrastive Diffusion Model for Private Sensor-Intensive Environment Data Generation

**arXiv ID:** [arXiv:2609.02958](https://arxiv.org/abs/2609.02958)  
**Subjects:** Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI)  
**Submission Date:** September 2, 2026  
**Authors:** Jiechao Gao, Yuandong Pan, Jie Wang, Michael Lepech, Bradford Campbell  

---

## 📌 Summary

> 传感器密集型环境依赖异构数据流，通过推断用户的应用来提供智能服务。然而，这产生了一个根本性的冲突：用户希望从有用的服务推断中受益，同时保持某些个人活动私密。传统的隐私保护方法——如差分隐私和基于规则的过滤——保护了孤立的数据流，但它们无法缓解源自*跨传感器推断*的隐私风险。
> 
> 为了解决这一挑战，作者引入了 **PrivateHub**，这是一个将对比学习集成到扩散模型中的新颖框架。PrivateHub 生成合成的多传感器数据流，旨在保持非私密应用可检测的同时成功隐藏私密应用。
> 
> 该框架分两个主要阶段运行：
> 1. **应用条件预训练 (ACP)：** 使用应用嵌入将多传感器数据条件化到扩散模型中。
> 2. **应用感知微调 (AAF)：** 利用对比学习显式分离私密数据与非私密数据。
> 
> 对三个真实世界多传感器数据集的评估表明，PrivateHub 在不降低非私密性能的情况下，将私密应用推断准确率降低了 **40% 至 50%**，同时在攻击者基于合成数据重新训练模型时依然保持稳健。

> ## 📌 Summary
> 
> Sensor-intensive environments rely on heterogeneous data streams to provide intelligent services by inferring user applications. However, this creates a fundamental conflict: users want to benefit from useful service inferences while keeping certain personal activities private. Traditional privacy preservation methods—such as differential privacy and rule-based filtering—protect isolated data streams, but they fail to mitigate privacy risks stemming from *cross-sensor inference*.
> 
> To address this challenge, the authors introduce **PrivateHub**, a novel framework that integrates contrastive learning within a diffusion model. PrivateHub generates synthetic multi-sensor streams designed to keep non-private applications detectable while successfully concealing private ones. 
> 
> The framework operates in two main stages:
> 1. **App-Conditioned Pre-training (ACP):** Conditions the diffusion model on multi-sensor data using application embeddings.
> 2. **App-Aware Fine-tuning (AAF):** Leverages contrastive learning to explicitly separate private data from non-private data.
> 
> Evaluations across three real-world multi-sensor datasets demonstrate that PrivateHub reduces private-application inference accuracy by **40% to 50%** without degrading non-private performance, while remaining robust even when an attacker retrains models on the synthetic data.

---

## 📖 Abstract

> 传感器密集型环境通过从异构数据流中推断用户的应用，实现了许多智能服务。然而，并非所有应用都应该暴露：用户希望某些活动保持私密。这就造成了推断应用以提供有用服务与防止不需要的推断之间的张力。现有方法（如差分隐私和基于规则的过滤）保护了单个数据流，但无法解决跨传感器推断带来的隐私风险。
> 
> 我们引入了 Privatehub，它在扩散模型中使用对比学习来生成合成的多传感器数据流，使非私密应用保持可检测，同时隐藏私密应用。Privatehub 包含两个阶段：应用条件预训练（ACP），使用应用嵌入将多传感器数据条件化到模型中；应用感知微调（AAF），通过对比学习将私密数据与非私密数据分离。我们还为多传感器共享设置定义了一个威胁模型。在三个真实世界多传感器数据集上的实验表明，Privatehub 将私密应用的准确率降低了 40% 到 50%，且不损害非私密性能，并且在攻击者对合成数据进行重新训练时保持稳健。

> > Sensor-intensive environments enable many intelligent services by inferring user applications from heterogeneous data streams. However, not all applications should be exposed: users want some activities to stay private. This creates a tension between inferring applications for useful services and preventing unwanted inference. Existing approaches such as differential privacy and rule-based filtering protect individual streams but cannot address the privacy risk from cross-sensor inference.
> >
> > We introduce Privatehub, which uses contrastive learning within a diffusion model to generate synthetic multi-sensor streams that keep non-private applications detectable while concealing private ones. Privatehub has two stages: App-Conditioned Pre-training (ACP), which conditions the model on multi-sensor data with application embeddings, and App-Aware Fine-tuning (AAF), which separates private from non-private data via contrastive learning. We also define a threat model for the multi-sensor sharing setting. Experiments on three real-world multi-sensor datasets show Privatehub lowers private-application accuracy by 40 to 50\% without hurting non-private performance, and stays robust when the attacker retrains on the synthetic data.

---

## 🔗 Links & Resources

* **全文访问:** [查看 PDF](https://arxiv.org/pdf/2609.02958) | [HTML (实验性)](https://arxiv.org/html/2609.02958v1)
* **源代码与数据:** [TeX 源码](https://arxiv.org/src/2609.02958)
* **引文与参考:** [谷歌学术](https://scholar.google.com/scholar_lookup?arxiv_id=2609.02958) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.02958) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.02958)
* **许可证:** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2609.02958) | [HTML (Experimental)](https://arxiv.org/html/2609.02958v1)
> * **Source Code & Data:** [TeX Source](https://arxiv.org/src/2609.02958)
> * **Citations & References:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.02958) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.02958) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.02958)
> * **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">