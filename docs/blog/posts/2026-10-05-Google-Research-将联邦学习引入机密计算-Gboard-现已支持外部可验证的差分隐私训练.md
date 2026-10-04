---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-10-05
hide:
- navigation
tags:
- Google Research
- 联邦学习
- TEE
- 机密计算
- 差分隐私
- Gboard
- Project Oak
title: Google Research 将联邦学习引入机密计算：Gboard 现已支持外部可验证的差分隐私训练
---
### 文章背景与核心概要
传统联邦学习 (Federated Learning, FL) 虽能在不收集用户原始数据的前提下协同训练模型，但用户和外界始终无法从密码学层面证实中央服务器是否私下记录了数据，也无法确证差分隐私 (Differential Privacy, DP) 噪声是否被严谨添加，存在着难以弥合的“信任鸿沟”。为了攻克这一关键技术挑战，Google Research 正式推出了基于可信执行环境 (Trusted Execution Environment, TEE) 构建的新一代机密联邦学习系统，将梯度计算从端侧转移至经过硬件远程证明的服务端机密飞地中执行。该系统结合了公共透明日志 (Public Transparency Logs) 与可重构构建技术，使得任何外部机构都能独立审计其服务端的完整执行逻辑，在业内首次实现了具有外部可验证性的中心差分隐私保障。目前该技术已全面投入生产环境，稳定支撑 Gboard 输入法的英语与日语下一词预测模型，不仅大幅提升了用户隐私防线，更将原本耗时数月的跨设备训练周期缩短了数倍。

---

# Google Research 将联邦学习引入机密计算：Gboard 现已支持外部可验证的差分隐私训练

> # Google Research Moves Federated Learning Into TEEs: Gboard Now Trains With Externally Verifiable Differential Privacy

## 内容总结

> ## Summary

Google Research 正式公布了基于可信执行环境 (Trusted Execution Environment, TEE) 构建的下一代联邦学习 (Federated Learning, FL) 系统，在业界首次实现了外部可验证的中心差分隐私 (Differential Privacy, DP) 保障。通过将原本由手机端侧承担的梯度计算转移到经过硬件远程证明的服务端 TEE 中运行，并依托公共透明日志进行公开公示，该系统从根本上消除了传统联邦学习中长期存在的“信任鸿沟”。目前，这套全新架构已全面投入生产环境，成功支撑了 Gboard 输入法的英语与日语下一词预测模型，不仅大幅缩短了训练耗时，更为用户隐私筑起了一道坚实的密码学防线。

> Google Research has announced a next-generation Federated Learning (FL) system built on Trusted Execution Environments (TEEs), achieving externally verifiable central differential privacy (DP) guarantees for the first time. By shifting client gradient computation to attested server-side TEEs and utilizing public transparency logs, the system eliminates the traditional "trust gap" in federated learning. This architecture is already live in production, powering English and Japanese next-word prediction models on Gboard with significantly faster training times and enhanced privacy protections.

---

## 基于 TEE 的联邦学习解决了什么痛点？

> ## What Problem Does TEE-Based Federated Learning Solve?

早在 2017 年，Google 便率先推出了联邦学习 (FL) 技术，广泛应用于 Gboard 的 [下一词预测](https://arxiv.org/abs/1811.03604) 与智能撰写 (Smart Compose) 、Google Messages 的智能回复建议，以及 Android 系统的智能文本选择等日常功能中。

> Google introduced Federated Learning (FL) in 2017 to power features like [next-word prediction](https://arxiv.org/abs/1811.03604) and Smart Compose on Gboard, reply suggestions in Google Messages, and Smart Text Selection in Android. 

然而，早期的联邦学习系统始终面临着难以逾越的信任鸿沟：

> However, earlier systems suffered from a trust gap:

* **缺乏可验证性 (Lack of Verification) ：** 用户设备在本地处理后上传数据用于实时聚合，但外部审计人员无法在密码学层面证实这些数据是否从未被服务器私下记录或窥探。
* **兼容性瓶颈 (Compatibility Issues) ：** 尽管 [Secure Aggregation](https://arxiv.org/abs/1611.04482) 安全聚合协议引入了密码学防护，但它无法兼容当前业界最前沿的中心差分隐私算法，例如 [矩阵分解 DP-FTRL](https://arxiv.org/abs/2202.08312) 。此外，用户仍必须无条件盲目相信 Google 会规范且正确地添加 DP 差分隐私噪声。

> * **Lack of Verification:** Devices uploaded data for immediate aggregation, but outsiders could not cryptographically verify that data was never logged or inspected.
> * **Compatibility Issues:** While [Secure Aggregation](https://arxiv.org/abs/1611.04482) added cryptographic protection, it was incompatible with state-of-the-art central DP algorithms like [matrix factorization DP-FTRL](https://arxiv.org/abs/2202.08312). Furthermore, users had to blindly trust Google to apply DP noise correctly.

这项全新设计正是为了打破这一僵局：它将客户端的梯度计算迁移到了云端服务器上，并通过软硬件远程证明技术确保服务端运行逻辑绝对透明可查，从而使用户和外部机构彻底摆脱对云服务运营商的被动盲信。

> The new design addresses this by moving client gradient computation to the server and making the server logic attestable, removing the need to implicitly trust the operator.

---

## 这套系统是如何协同运转的？

> ## How Does the System Work?

在 Google 先前开展的 [机密联邦分析 (Confidential Federated Analytics) ](https://research.google/blog/confidential-federated-analytics/) 研究基础之上，新系统精密编排了四大核心组件：

> Building upon Google’s earlier work in [confidential federated analytics](https://research.google/blog/confidential-federated-analytics/), the new system coordinates four core components:

* **数据上传 (Data Upload) ：** 用户设备在本地对训练样本进行高强度加密，并预先授权访问策略。该策略精确界定了哪些 TEE 计算任务有权处理这些数据，且该策略必须公开发布到不可篡改的公开透明日志中。
* **KMS 与策略验证 (KMS and Policy Verification) ：** 基于运行 [RAFT 共识协议 (RAFT consensus protocol) ](https://raft.github.io/raft.pdf) 的 TEE 集群构建密钥管理系统 (Key Management System, KMS) ，仅当工作负载完全符合经预先授权的安全策略时，KMS 才会分发解密密钥。
* **工作负载执行 (Workload Execution) ：** 根节点 TEE (Root TEE) 负责执行 Python 训练循环，并利用基于 [TensorFlow Federated](https://www.tensorflow.org/federated) 衍生的 [Federated Language](https://github.com/google-parfait/federated-language) 将子任务安全分发给各个工作节点 TEE (Worker TEE) 。在整个计算过程中，系统最终仅对外输出符合 DP 差分隐私标准的模型权重。
* **容错与状态恢复 (Fault-Tolerant Recovery) ：** 每个训练轮次都会自动保存一份经 KMS 加密的系统恢复状态，确保无论根节点还是工作节点发生意外宕机故障，系统都能实现无缝恢复与断点续训。

> * **Data Upload:** Devices encrypt training examples locally and pre-authorize an access policy. This policy specifies which TEE computations may process the data and must be published in a public transparency log.
> * **KMS and Policy Verification:** A Key Management System (KMS) built from TEEs running the [RAFT consensus protocol](https://raft.github.io/raft.pdf) releases decryption keys exclusively to workloads matching the authorized policy.
> * **Workload Execution:** A root TEE runs a Python training loop and delegates subtasks to worker TEEs using [Federated Language](https://github.com/google-parfait/federated-language) (derived from [TensorFlow Federated](https://www.tensorflow.org/federated)). Only DP model weights are released.
> * **Fault-Tolerant Recovery:** Each training round saves a KMS-encrypted recovery state to seamlessly handle root or worker node failures.

---

## 为什么说这里的隐私保障是真正“可验证”的？

> ## Why Is the Privacy Guarantee Verifiable?

* **公开透明日志 (Public Transparency Logs) ：** 所有数据访问策略都会同步发布到 Sigstore 旗下的公开透明日志系统 [Rekor](https://docs.sigstore.dev/logging/overview/) 中。这使得任何外部独立审计员都可以全流程追踪用户设备可能喂给服务端的所有计算负载。
* **可重构构建 (Reproducible Builds) ：** KMS 密钥管理系统与核心数据处理的二进制程序均由开源代码编译而成，完全支持可重构构建 (Reproducible Builds) ，任何人都可以自行编译并核对二进制哈希值。
* **运行时安全机制 (Runtime Security) ：** 访问策略直接对 Python 训练程序的具体内容进行了严格约束。为了兼顾商业私有模型架构的机密性，TEE 允许在运行时以侧载形式加载序列化逻辑，前提是所有涉及数据隐私的关键代码必须在通过远程证明的程序中硬编码固化。此外，集群运维人员全局只能查看训练指标和经 DP 保护的模型权重，且上传的原始数据只在极其严苛的时间窗口内允许解密。

> * **Public Transparency Logs:** Access policies are published to [Rekor](https://docs.sigstore.dev/logging/overview/), Sigstore’s public transparency log, allowing external auditors to track every server workload a device could potentially feed.
> * **Reproducible Builds:** The KMS and data processing binaries are reproducibly buildable from open-source code.
> * **Runtime Security:** Policies directly describe the Python training program. To protect proprietary model architectures, TEEs support sideloading serialized logic at runtime, provided all privacy-relevant code remains hardcoded in the attested program. Workload operators only see metrics and DP model weights, and uploaded data can only be decrypted for a strictly limited window of time.

---

## Gboard 获得了哪些实打实的收益？

> ## What Did Gboard Gain?

Gboard 输入法正是利用这套全新架构，顺利上线了英语和日语的下一词预测模型，并在实际工程中释放出两大核心架构优势：

> Gboard utilized the system to roll out English and Japanese next-word prediction models, yielding two primary architectural advantages:

1. **异步解耦的灵活性 (Asynchronous Flexibility) ：** 系统会在服务端正式启动模型训练前先行收集并缓存所有加密上传的数据。如此一来，全球手机设备因昼夜作息规律带来的可用性剧烈波动不再成为训练进度的瓶颈，训练程序能够从容计算出全局最优的设备参与计划，并动态精准微调 DP 差分隐私参数。
2. **服务端高度并行化 (Server-Side Parallelization) ：** 随着计算瓶颈从低算力的移动设备转移到了高性能服务器，训练时间迎来了断崖式缩短。过去在跨设备联邦学习环境下往往需要耗费 1 至 2 个月才能完成训练的模型，如今可以在多台机器间高效并行展开，训练效率仅仅取决于可调配的 TEE 硬件算力规模。

> 1. **Asynchronous Flexibility:** All uploads are collected before server-side training begins. Diurnal swings in device availability no longer bottleneck training, allowing the program to compute an optimal participation schedule and dynamically tune DP parameters.
> 2. **Server-Side Parallelization:** By moving the computational bottleneck to the server, training times dropped dramatically. Where previous FL models took 1 to 2 months to train, jobs now parallelize across machines, constrained only by available TEE hardware resources.

---

## 与其他主流联邦学习框架对比表现如何？

> ## How Does It Compare With Other FL Frameworks?

| 特性 (Feature) | [Google TEE-based FL](https://research.google/blog/toward-provably-private-learning-from-federated-data/) | [NVIDIA FLARE](https://nvflare.readthedocs.io/en/main/welcome.html) | [Flower](https://github.com/flwrlabs/flower) | [Apple pfl-research](https://github.com/apple/pfl-research) |
| :--- | :--- | :--- | :--- | :--- |
| **主要用途 (Primary use) ** | 生产级跨设备训练 (已在 Gboard 实装上线) | 面向生产的 FL SDK，配备 Docker、Kubernetes 及云原生工具 | 构建联邦 AI 系统的通用框架 | 仅用于学术仿真模拟；不支持第三方部署 |
| **客户端更新计算位置 (Where client updates are computed) ** | 服务端 TEE | 各参与计算节点本地 | 客户端本地 | 仅软件模拟 |
| **硬件 TEE 支持 (Hardware TEE support) ** | 支持，基于 Project Oak 构建 | 支持：AMD SEV-SNP、Intel TDX、NVIDIA GPU 机密计算 | 并非核心框架自带组件 | 不支持 |
| **差分隐私 (Differential privacy) ** | 中心 DP，支持外部独立验证 | DP 过滤器，通过 Opacus 实现 DP-SGD | 支持中心 DP 与本地 DP | 支持本地与中心 DP 机制 |
| **其他隐私技术 (Other privacy tech) ** | KMS 门控解密机制；Willow 安全聚合容器 | 同态加密、隐私集合求交 (Private Set Intersection) | SecAgg 与 SecAgg+ | 不适用 (仿真环境) |
| **服务端代码公开透明日志 (Public transparency log for server code) ** | 支持，采用 Sigstore Rekor | 未明确记录 | 未明确记录 | 不适用 |
| **可重构 TEE 构建 (Reproducible TEE builds) ** | 支持 (包含 KMS 与数据处理二进制程序) | 未明确记录 | 不适用 | 不适用 |
| **开源许可证 (License) ** | Apache 2.0 | Apache 2.0 | Apache 2.0 | Apache 2.0 |

*数据来源：[Google Research 博客](https://research.google/blog/toward-provably-private-learning-from-federated-data/)、[Confidential Federated Compute 代码仓库](https://github.com/google-parfait/confidential-federated-compute)、[NVIDIA FLARE 官方文档](https://nvflare.readthedocs.io/en/main/welcome.html)、[FLARE 远程证明指南](https://nvflare.readthedocs.io/en/2.7.0/_sources/user_guide/confidential_computing/attestation.rst.txt)、[Flower 1.8 发布说明](https://flower.ai/blog/2024-04-03-announcing-flower-1.8-release)、[pfl-research 代码仓库](https://github.com/apple/pfl-research)。*

> *Sources: [Google Research blog](https://research.google/blog/toward-provably-private-learning-from-federated-data/), [Confidential Federated Compute repo](https://github.com/google-parfait/confidential-federated-compute), [NVIDIA FLARE docs](https://nvflare.readthedocs.io/en/main/welcome.html), [FLARE attestation guide](https://nvflare.readthedocs.io/en/2.7.0/_sources/user_guide/confidential_computing/attestation.rst.txt), [Flower 1.8 release notes](https://flower.ai/blog/2024-04-03-announcing-flower-1.8-release), [pfl-research repo](https://github.com/apple/pfl-research).*

---

## 核心要点总结

> ## Key Takeaways

* Google 成功将联邦学习的梯度计算从移动端设备迁移到了经过硬件证明的服务端 TEE 机密计算环境中。
* 依托 Rekor 公开透明日志与开源可重构构建机制，中心差分隐私保障在业界首次实现了外部独立可验证。
* Gboard 输入法已在生产环境中正式实装该升级架构，稳定支撑英语和日语的下一词预测模型。
* 模型训练周期大幅缩减，跨设备训练的瓶颈从漫长的单模型训练耗时彻底转变为取决于可用的 TEE 硬件算力规模。
* 核心 TEE 二进制代码与 Federated Language 组件均已在 Apache 2.0 协议下完全开源。

> * Google successfully transitioned FL gradient computation from mobile devices into attested server-side TEEs.
> * Central DP guarantees are now externally verifiable via Rekor logs and reproducible builds.
> * Gboard is actively shipping English and Japanese next-word models using this upgraded architecture.
> * Training durations have been slashed, shifting the primary limitation from time-per-model to available TEE compute capacity.
> * Core TEE binaries and Federated Language components have been open-sourced under the Apache 2.0 license.

---

***

*欢迎查阅 [**学术论文**](https://arxiv.org/abs/2609.31494) 、 [**技术博客详情**](https://research.google/blog/toward-provably-private-learning-from-federated-data/) 以及 [**GitHub 开源仓库**](https://github.com/google-parfait/confidential-federated-compute) 。*

> *Check out the [**Paper**](https://arxiv.org/abs/2609.31494), [**Technical details**](https://research.google/blog/toward-provably-private-learning-from-federated-data/), and [**GitHub Repo**](https://github.com/google-parfait/confidential-federated-compute).*
