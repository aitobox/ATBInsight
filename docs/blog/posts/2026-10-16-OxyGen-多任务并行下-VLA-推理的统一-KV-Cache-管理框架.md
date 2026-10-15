---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-16
hide:
  - navigation
tags:
  - OxyGen
  - KV Cache
  - VLA
  - 具身智能
  - 推理加速
title: "OxyGen：多任务并行下 VLA 推理的统一 KV Cache 管理框架"
---

# OxyGen：多任务并行下 VLA 推理的统一 KV Cache 管理框架

> # OxyGen: Unified KV Cache Management for VLA Inference under Multi-Task Parallelism

> **arXiv ID:** [2603.14371](https://arxiv.org/abs/2603.14371) [cs.RO]  
> **Authors:** Xiangyu Li, Huaizhi Tang, Xin Ding, Weijun Wang, Ting Cao, Yunxin Liu  
> **Subjects:** Robotics (`cs.RO`), Artificial Intelligence (`cs.AI`)  
> **Conference:** NeurIPS 2026  
> **License:** [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/) [![license icon](./images/345c7ad61f1b.png)](http://creativecommons.org/licenses/by/4.0/)  

### 文章背景与核心概要

在具身智能领域，实体机器人为了在复杂物理世界中生存与协作，往往需要一边手眼协同执行精细操作，一边与人类自然对话并实时构建情境记忆，且各项任务对执行频率与延迟 (Latency) 的容忍度截然不同。尽管基于 Transformer 架构的现代视觉-语言-动作模型 (Vision-Language-Action Model, VLA) 赋予了机器人多模态输出的能力，但现有的端侧推理系统在处理多任务并发时，频频陷入算力资源严重争抢与重复计算视觉特征预填充 (Prefill) 的泥潭。为此，研究团队推出了创新的 **OxyGen** 统一管理框架，突破性地将键值缓存 (Key-Value Cache, KV Cache) 视作贯穿多任务与控制周期的“一等公民共享资源”，通过跨任务 KV 共享彻底斩断了多任务重复编码同一视觉画面的开销，并依托跨帧连续批处理 (Continuous Batching) 在严苛的毫秒级控制预算内高效推进文本解码。基准测试与真实人形机器人实测表明，OxyGen 相比传统隔离运行框架带来了高达 3.7 倍的推理加速，不仅能在 NVIDIA RTX 4090 上同时实现 70 Hz 的高频动作控制与超过 200 Token/s 的流畅语言吞吐量 (Throughput) ，更在车载 Jetson AGX Thor 平台上实现了稳健的端侧具身部署，为多任务实时智能机器人的规模化落地带来了关键基石。

---

## 内容概要

> ## Summary

在现实场景中，具身 AI 智能体 (Embodied AI Agent) 日益需要在共享传感器感知输入的前提下，并行处理多项异构任务——例如精准的机械臂操控、流畅的语音交互以及情境记忆的实时构建，同时还要满足各任务严格且截然不同的时间约束。尽管当下先进的混合架构 (Mixture-of-Transformers, MoT) 视觉-语言-动作模型能够胜任这些多模态输出，但现存的设备端推理系统在调度并发任务时，却深陷大量冗余计算与剧烈硬件资源冲突的困境。

> Embodied AI agents are increasingly required to execute multiple tasks in parallel—such as manipulation, conversation, and memory construction—from shared sensory observations while meeting strict, distinct time constraints. Modern Mixture-of-Transformers (MoT) Vision-Language-Action Models (VLAs) support these heterogeneous outputs, but current on-device inference systems struggle with redundant computations and severe resource contention when managing concurrent tasks. 

为此，**OxyGen** 提出了一套统一的键值缓存 (KV Cache) 管理框架，它将 KV Cache 提升为贯穿所有并发任务与控制周期的“一等公民共享资源”。这一创新架构释放出两大核心优化能力：

> **OxyGen** introduces a unified Key-Value (KV) cache management framework that treats the KV cache as a first-class shared resource across tasks and control cycles. This design unlocks two core optimizations:

1. **跨任务 KV 共享 (Cross-task KV sharing)**：对于多任务共同观察到的同一视觉画面，彻底免除了重复昂贵的预填充计算阶段；
2. **跨帧连续批处理 (Cross-frame continuous batching)**：将源自不同视频帧且尚未完成的语言生成请求统一打包批处理，并在每帧严格限定的解码时间预算内紧凑推进。

> 1. **Cross-task KV sharing**, which completely eliminates the redundant prefill phase for shared visual observations.
> 2. **Cross-frame continuous batching**, which batches unfinished language requests originating from different frames and advances them within strict per-frame decoding budgets.

在包括桌面端 NVIDIA GeForce RTX 4090 与边缘计算平台 Jetson AGX Thor 等多种硬件设备上的综合评测中 (涵盖 $\pi_{0.5}$、Xiaomi-Robotics-0 以及 StarVLA 等主流模型) ，**OxyGen** 相比传统任务各自为战的隔离执行方案，实现了最高达 **3.7 倍的推理加速**。在 RTX 4090 上，它能够以惊人的并发效率同时达成超过 **200 Token/s** 的语言吞吐量与 **70 Hz** 的动作控制频率；更重要的是，研究团队在搭载车载 Jetson AGX Thor 计算单元的真实人形机器人上完成了真机实测，充分验证了其在复杂物理交互场景中强大的实时推理增益。

> Evaluated on platforms like the NVIDIA GeForce RTX 4090 and Jetson AGX Thor (using models such as $\pi_{0.5}$, Xiaomi-Robotics-0, and StarVLA), **OxyGen** delivers up to a **3.7× speedup** over isolated execution frameworks. On an RTX 4090, it achieves over **200 tokens/s** language throughput and a **70 Hz** action frequency simultaneously, and demonstrates robust real-world inference gains on a humanoid robot powered by an on-board Jetson AGX Thor.

---

## 相关链接与资源

> ## Links & Resources

* **全文链接：** [查看 PDF](https://arxiv.org/pdf/2603.14371) | [HTML 网页版本 (实验性) ](https://arxiv.org/html/2603.14371v4) | [TeX 源码](https://arxiv.org/src/2603.14371)
* **关联代码与工具：** [Hugging Face](https://huggingface.co/huggingface) | [CatalyzeX 代码检索](https://www.catalyzex.com) | [alphaXiv](https://alphaxiv.org/)
* **学术引用与索引：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2603.14371) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2603.14371) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2603.14371)

> * **Full-Text Access:** [View PDF](https://arxiv.org/pdf/2603.14371) | [HTML (Experimental)](https://arxiv.org/html/2603.14371v4) | [TeX Source](https://arxiv.org/src/2603.14371)
> * **Associated Code & Tools:** [Hugging Face](https://huggingface.co/huggingface) | [CatalyzeX Code Finder](https://www.catalyzex.com) | [alphaXiv](https://alphaxiv.org/)
> * **Citations & References:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2603.14371) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2603.14371) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2603.14371)
