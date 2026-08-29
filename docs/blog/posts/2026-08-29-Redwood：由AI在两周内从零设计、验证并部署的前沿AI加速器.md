---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-29
hide:
- navigation
tags:
- AI加速器
- 硬件设计自动化
- 芯片设计
- RTL生成
- 具身智能
title: Redwood：由AI在两周内从零设计、验证并部署的前沿AI加速器
---
### 文章背景与核心概要
现代AI工作负载与底层硬件的发展速度存在严重的时间错位：芯片架构的定义往往需要数年时间，而目标工作负载的演进周期却只有几个月。为了打破摩尔定律的停滞并克服固化芯片带来的性能损耗，Architect Labs推出了Redwood——一个将“软件到硅片”全栈压缩至单一优化循环中的端到端AI系统。

仅凭两名人类架构师提供的高层规范，该系统在不到两周的时间内，在没有规范以下人工干预的情况下，自主生成了完整的性能模型、RTL设计、UVM验证环境、形式化证明、固件以及内核。Redwood不仅实现了极高的开发效率，其性能在相同工艺下也大幅超越了现有同类硬件，展示了AI在芯片自主设计与递归自我改进方面的巨大潜力。

---

## 摘要与核心亮点

> Modern AI workloads and hardware evolve on mismatched timescales: architectural definitions precede volume silicon by years, while target workloads shift in months. To overcome the stagnation of Moore's Law and the performance penalties of frozen silicon, **Architect Labs** presents **Redwood**—an end-to-end AI system that collapses the software-to-silicon stack into a single optimization loop.

现代AI工作负载与其运行的硬件在不同的时间尺度上演进：架构定义比量产硅片早几年，而目标工作负载则在几个月内发生变化。为了克服摩尔定律的停滞和固化硅片的性能惩罚，**Architect Labs** 推出了 **Redwood**——一个将软件到硅片技术栈压缩为单一优化循环的端到端AI系统。

> Starting from a high-level specification written by just two human architects, the system autonomously generated a complete performance model, RTL design, UVM environments, formal proofs, firmware, and kernels in **under two weeks with no human intervention** below the spec.

从仅由两名人类架构师编写的高级规范出发，该系统在**不到两周的时间内且在规范以下没有人工干预**的情况下，自主生成了完整的性能模型、RTL设计、UVM验证环境、形式化证明、固件和内核。

---

## 关键亮点与性能表现

* **快速开发周期：** 从头开始设计、验证并在两周内完成部署。规范更改在48小时内成功完成重新验证并重新部署到硬件。
* **严格的验证：** 利用商业EDA工具、专有形式化引擎和硬件在环验证，每个模块都达到了 **95% 的覆盖率**。
* **Redwood Nano（FPGA变体）：** 能够运行像 *Llama* 和 *Qwen* 这样具有数十亿参数的模型。
* **竞争优势：** 映射到三星8纳米工艺（与Jetson Orin Nano同工艺级别）时，Redwood 实现了 **1.75倍的吞吐量** 和 **1.9倍的更低功耗**，在运行相同模型时，相比实测的 Jetson 基准测试，实现了 **3.4倍的每瓦性能提升**。
* **递归自我改进：** 运行在 Redwood 上的 *Qwen* 实例积极参与了下一代 Redwood 架构的设计。

*(注：原仓库中包含的相关图像资源或许可证指示符如下： <img alt="license icon" role="presentation" src="./images/fb423b2203a9.png">)*

---

## 摘要

> Modern AI workloads and the hardware that runs them evolve on different timescales: architectural definition precedes volume silicon by years, while target workloads shift in months. Design decisions are therefore committed under deep uncertainty and paid for twice, once in the generality added as a hedge, and again when new workloads map poorly onto frozen silicon. As Moore's Law stagnates, specialization is the main remaining source of performance-per-watt and demands a design cycle that runs at the cadence of the workloads. We present an end-to-end AI system that collapses the software-to-silicon stack into a single optimization loop, where hardware and software are co-designed and verified under one objective. Its first demonstration is Redwood, a frontier AI accelerator built for single-batch, low-power, ultra-low-latency inference for physical AI. From a high-level specification by two human architects, the system autonomously generated the performance model, RTL design, UVM environments, formal proofs, firmware, and kernels in under two weeks with no human intervention below the specification. Every block reached 95% coverage via commercial EDA tools, our proprietary formal engine, and hardware-in-the-loop validation. Specification changes were reverified and redeployed to hardware in under 48 hours. Redwood Nano, its ultra-low-power FPGA variant, runs multi-billion-parameter models like Llama and Qwen. Projected onto Samsung 8 nm, the Jetson Orin Nano's process class, Redwood delivers 1.75x the throughput at 1.9x lower power, a 3.4x performance-per-watt gain against a measured Jetson baseline on the same models. Qwen running on Redwood also helped design next-generation Redwood, an early step toward recursive self-improvement. To our knowledge, this is the first production-worthy AI accelerator designed end-to-end by an AI system and running a modern AI model.

现代AI工作负载与运行它们的硬件在不同的时间尺度上演进：架构定义领先于量产硅片数年，而目标工作负载则在数月内发生变化。因此，设计决策是在极大的不确定性下做出的，并且需要付出双重代价：一次是为了对冲风险而增加通用性所付出的代价，另一次则是当新工作负载无法很好地映射到固化硅片上时所付出的代价。随着摩尔定律的停滞，专用化成为提升每瓦性能的主要剩余来源，这就需要一个与工作负载节奏相匹配的设计周期。我们提出了一个端到端的AI系统，它将软件到硅片的堆栈折叠到一个单一的优化循环中，在此循环中，硬件和软件在单一目标下进行协同设计和验证。它的首个演示是 Redwood，这是一个专为具身智能的单批次、低功耗、超低延迟推理而构建的前沿AI加速器。根据两名人类架构师提供的高级规范，该系统在不到两周的时间内自主生成了性能模型、RTL设计、UVM环境、形式化证明、固件和内核，在规范之下没有任何人工干预。通过商业EDA工具、我们专有的形式化引擎和硬件在环验证，每个模块都达到了95%的覆盖率。规范更改在48小时内完成了重新验证并重新部署到硬件。Redwood Nano 是其超低功耗的FPGA变体，能够运行 Llama 和 Qwen 等数十亿参数的模型。映射到三星 8nm（Jetson Orin Nano 的工艺级别）时，Redwood 实现了 1.75 倍的吞吐量和 1.9 倍的低功耗，在运行相同模型时，相比实测的 Jetson 基准测试，实现了 3.4 倍的每瓦性能提升。运行在 Redwood 上的 Qwen 还帮助设计了下一代 Redwood，这是迈向递归自我改进的早期一步。据我们所知，这是第一个由AI系统端到端设计并运行现代AI模型的具备生产价值的AI加速器。