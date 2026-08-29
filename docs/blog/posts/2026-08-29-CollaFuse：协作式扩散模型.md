---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- 扩散模型
- 协作学习
- 拆分学习
- 边缘计算
- 隐私保护
title: CollaFuse：协作式扩散模型
---
### 文章背景与核心概要
生成式人工智能（特别是扩散模型）在合成高质量图像方面展现出了巨大潜力，但在实际应用中常常面临数据可用性受限、严格的隐私约束以及极高的计算需求等痛点。传统的联邦学习等方法虽然能在一定程度上保护隐私，但往往会给资源受限的边缘客户端带来沉重的计算负担。

为了解决这些挑战，本文提出了一种名为 **CollaFuse** 的新型分布式协作扩散模型方法，该方法受到“拆分学习”（split learning）的启发。CollaFuse 通过将原始数据和轻量级计算保留在本地，同时将高负载的计算外包给共享的高效服务器资源，从而在显著减轻客户端计算负担和减少信息泄露的同时，降低了对共享原始数据的需求。

在 CelebA、CIFAR-10 和 Animals-with-Attributes2 等主流数据集上的实验表明，CollaFuse 不仅能实现优异的性能，还在边缘计算解决方案的设计等多个应用领域展现出广阔的应用前景，有力推动了分布式机器学习与协作扩散模型的发展。

---

## 📋 Summary
**CollaFuse** is a novel distributed collaborative approach for training and running diffusion models, inspired by split learning. It addresses the key challenges of generative AI—such as data availability, strict privacy constraints, and high computational demands—especially for resource-constrained edge clients. By keeping raw data and lightweight processes local while offloading heavy computations to shared, efficient server resources, CollaFuse reduces information disclosure and client computational overhead while achieving enhanced performance across datasets like CelebA, CIFAR-10, and Animals-with-Attributes2.

> **CollaFuse** 是受拆分学习启发而提出的一种新型分布式协作方法，用于训练和运行扩散模型。它解决了生成式 AI 的核心挑战（如数据可用性、严格的隐私约束以及高计算需求），特别适合资源受限的边缘客户端。通过将原始数据和轻量级处理保留在本地，同时将繁重的计算卸载到共享的高效服务器资源上，CollaFuse 在降低信息泄露和客户端计算开销的同时，在 CelebA、CIFAR-10 和 Animals-with-Attributes2 等数据集上实现了更强的性能。

---

## 📌 Metadata & Publication Details

| 字段 | 详情 |
| :--- | :--- |
| **arXiv ID** | [2406.14429](https://arxiv.org/abs/2406.14429) [cs.LG] |
| **作者** | Simeon Allmendinger, Domenique Zipperling, Lukas Struppek, Niklas Kühl |
| **学科分类** | 机器学习 (`cs.LG`); 人工智能 (`cs.AI`); 计算机视觉与模式识别 (`cs.CV`) |
| **期刊引用** | Journal of Artificial Intelligence Research (JAIR), Vol. 86 (2026) |
| **相关 DOI** | [10.1613/jair.1.20934](https://doi.org/10.1613/jair.1.20934) |
| **许可协议** | ![license icon](./images/fb423b2203a9.png) [知识共享 署名-非商业性使用-禁止演绎 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/) |

> | Field | Details |
> | :--- | :--- |
> | **arXiv ID** | [2406.14429](https://arxiv.org/abs/2406.14429) [cs.LG] |
> | **Authors** | Simeon Allmendinger, Domenique Zipperling, Lukas Struppek, Niklas Kühl |
> | **Subjects** | Machine Learning (`cs.LG`); Artificial Intelligence (`cs.AI`); Computer Vision and Pattern Recognition (`cs.CV`) |
> | **Journal Reference** | Journal of Artificial Intelligence Research (JAIR), Vol. 86 (2026) |
> | **Related DOI** | [10.1613/jair.1.20934](https://doi.org/10.1613/jair.1.20934) |
> | **License** | ![license icon](./images/fb423b2203a9.png) [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/) |

---

## 📝 Abstract
In the landscape of generative artificial intelligence, diffusion-based models have emerged as a promising method for generating synthetic images. However, the application of diffusion models poses numerous challenges, particularly concerning data availability, computational requirements, and privacy. 

> 在生成式人工智能领域，基于扩散的模型已成为合成图像的一种极具前景的方法。然而，扩散模型的应用带来了诸多挑战，特别是在数据可用性、计算需求和隐私方面。

Traditional approaches to address these shortcomings, like federated learning, often impose significant computational burdens on individual clients, especially those with constrained resources. In response to these challenges, we introduce the novel approach **CollaFuse** for distributed collaborative diffusion models inspired by split learning. 

> 解决这些缺点传统方法（如联邦学习）往往会对单个客户端（尤其是资源受限的客户端）带来沉重的计算负担。为了应对这些挑战，我们引入了一种受拆分学习启发的新方法 **CollaFuse**，用于分布式协作扩散模型。

Our approach facilitates collaborative training of diffusion models while alleviating client computational burdens during image synthesis. This reduced computational burden is achieved by retaining data and computationally inexpensive processes locally at each client while outsourcing the computationally expensive processes to shared, more efficient server resources. Through experiments on the common datasets CelebA, CIFAR-10, and Animals-with-Attributes2, our approach demonstrates enhanced performance while decreasing information disclosure as it reduces the necessity for sharing raw data. These capabilities hold significant potential across various application areas, including the design of edge computing solutions. Thus, our work advances distributed machine learning by contributing to the evolution of collaborative diffusion models.

> 我们的方法既促进了扩散模型的协同训练，又减轻了图像合成过程中客户端的计算负担。这种计算负担的降低是通过将数据和计算成本低廉的过程保留在每个客户端的本地，同时将计算成本高昂的过程外包给共享、更高效的服务器资源来实现的。通过在 CelebA、CIFAR-10 和 Animals-with-Attributes2 等常见数据集上的实验，我们的方法表现出增强的性能，同时通过减少共享原始数据的必要性降低了信息泄露。这些功能在包括边缘计算解决方案设计在内的各种应用领域中具有巨大潜力。因此，我们的工作通过促进协作扩散模型的演进，推动了分布式机器学习的发展。

---

## 🕒 Submission History
* **[v1]** Thu, 20 Jun 2024 15:54:21 UTC *(1,423 KB)*
* **[v2]** Sun, 27 Oct 2024 12:42:53 UTC *(1,977 KB)*
* **[v3]** Fri, 1 May 2026 10:03:23 UTC *(1,507 KB)*
* **[v4]** Tue, 4 Aug 2026 14:03:44 UTC *(1,517 KB)*
* **[v5]** Thu, 27 Aug 2026 13:35:30 UTC *(1,520 KB)* *(This version)*

> * **[v1]** Thu, 20 Jun 2024 15:54:21 UTC *(1,423 KB)*
> * **[v2]** Sun, 27 Oct 2024 12:42:53 UTC *(1,977 KB)*
> * **[v3]** Fri, 1 May 2026 10:03:23 UTC *(1,507 KB)*
> * **[v4]** Tue, 4 Aug 2026 14:03:44 UTC *(1,517 KB)*
> * **[v5]** Thu, 27 Aug 2026 13:35:30 UTC *(1,520 KB)* *(This version)*

---

## 🔗 Quick Links & Resources
* **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2406.14429) | [HTML (Experimental)](https://arxiv.org/html/2406.14429v5) | [TeX Source](https://arxiv.org/src/2406.14429)
* **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2406.14429) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2406.14429) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2406.14429)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2406.14429) | [HTML (Experimental)](https://arxiv.org/html/2406.14429v5) | [TeX Source](https://arxiv.org/src/2406.14429)
> * **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2406.14429) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2406.14429) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2406.14429)