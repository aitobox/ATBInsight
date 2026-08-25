---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-26
hide:
- navigation
tags:
- 机器人感知
- 点云处理
- 隐私保护
- 信息论
- 深度学习
title: RoboShape：面向隐私感知机器人感知的基于信息论的点云表征
---
### 文章背景与核心概要

随着机器人越来越多地在人类环境中作业，它们通过扫描并共享3D点云（用于车队学习、协作建图及云端规划）来执行任务。然而，这些数据在捕捉场景对象的同时，往往无意中泄露了敏感的空间背景及未经用户授权的隐私信息。传统的点云编码器通常只能在“全量保留”与“完全丢弃”之间做二选一，缺乏对隐私信息的精细化控制。

为了解决这一问题，研究人员提出了 **RoboShape**。这是一个基于信息论引导的压缩头，构建在冻结的 `Sonata` 编码器之上。RoboShape 利用互信息（MI）的 Donsker-Varadhan 公式对体素级嵌入进行投影：在最大化嵌入与对象级理解之间互信息的同时，最小化其与敏感属性之间的互信息。该方法在显著降低数据传输成本的同时，有效平衡了感知效用与隐私保护，为机器人感知流水线提供了一种紧凑且具备隐私意识的实用方案。

---

## RoboShape：面向隐私感知机器人感知的基于信息论的点云表征

### 摘要
> With the increased adoption of robotic agents operating in human environments by scanning and sharing 3D representations (e.g., for fleet learning, cloud-based planning, or collaborative mapping), collected point clouds reveal not just the objects in a scene but also sensitive spatial context, such as room function or information that occupants never consented to disclose. Traditional point cloud encoders offer no principled control over this: either all is preserved, or none. Hence, we introduce RoboShape, an information theory guided compression head following the frozen `Sonata` encoder. We project voxel-level embeddings using the Donsker-Varadhan formulation of mutual information (MI). Specifically, we maximize the MI between embeddings and object-level understanding while minimizing it for private attributes. RoboShape leads to 87.5% smaller embeddings that retain 98.7% of object classification utility while collapsing sensitive attribute predictions by 39.3% across the three real-world indoor LiDAR datasets. Its privacy-preserving embeddings are cheaper to transmit over the network or to train a model for any downstream tasks. We release the RoboShape codebase to give the robotics community a practical, encoder-agnostic tool for building perception pipelines that are compact, privacy-aware, and deployment-ready.

随着机器人代理在人类环境中的应用日益广泛，它们通过扫描和共享3D表征（例如用于车队学习、云端规划或协作建图）来执行任务。然而，收集到的点云不仅揭示了场景中的物体，还暴露了敏感的空间背景，例如房间功能或居住者从未同意披露的信息。传统的点云编码器对此无法提供原则性的控制：要么全部保留，要么全部丢弃。因此，我们引入了 RoboShape，这是一个在冻结的 `Sonata` 编码器之后的信息论引导压缩头。我们利用互信息（MI）的 Donsker-Varadhan 公式对体素级嵌入进行投影。具体而言，我们最大化嵌入与对象级理解之间的互信息，同时最小化其与私有属性之间的互信息。RoboShape 生成的嵌入体积缩小了 87.5%，在保留 98.7% 对象分类效用的同时，在三个真实室内 LiDAR 数据集上将敏感属性预测能力降低了 39.3%。其隐私保护嵌入在网络传输或下游任务模型训练中更具成本效益。我们发布了 RoboShape 代码库，旨在为机器人社区提供一种实用的、与编码器无关的工具，用于构建紧凑、隐私感知且可部署的感知流水线。

---

## 论文元数据

| 字段 | 详情 |
| :--- | :--- |
| **标题** | RoboShape: Information-Theoretic Point Cloud Representations for Privacy-Aware Robot Perception |
| **作者** | Oguzhan Baser, Mirac Sozen, Kaan Kale, Sandeep Chinchali, Sriram Vishwanath |
| **提交日期** | 2026年7月16日 |
| **主要学科** | 机器人学 (`cs.RO`) |
| **次要学科** | 人工智能 (`cs.AI`), 计算机视觉与模式识别 (`cs.CV`), 信息论 (`cs.IT`) |
| **arXiv ID** | [arXiv:2608.21380](https://arxiv.org/abs/2608.21380) |
| **DOI** | [10.48550/arXiv.2608.21380](https://doi.org/10.48550/arXiv.2608.21380) |
| **状态** | 审稿中 |

---

## 访问链接与资源

* **全文格式：** [查看 PDF](https://arxiv.org/pdf/2608.21380) | [HTML (实验性)](https://arxiv.org/html/2608.21380v1) | [TeX 源码](https://arxiv.org/src/2608.21380)
* **许可协议：** [知识共享署名 4.0 国际许可协议](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
* **外部引用：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.21380) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.21380) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.21380)