---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-01
hide:
- navigation
tags:
- AI加速器
- 硬件设计
- 自动化验证
- 芯片设计
- 递归自我改进
title: Redwood：由AI从零开始设计、验证并在2周内部署的前沿AI加速器
---
### 文章背景与核心概要
现代硬件设计周期通常长达数年，往往远远落后于每月都在快速演进的AI工作负载。为了克服这一根本瓶颈，Architect Labs推出了 **Redwood**——这是全球首款由AI系统在两周内完全从零开始设计、验证并部署的达到生产级要求的尖端AI加速器。

在仅由两位人类架构师提供高级规范说明的前提下，该AI自主生成了性能模型、RTL设计、UVM验证环境、形式化证明、固件以及内核，在规范层级以下实现了零人工干预。其实验变体Redwood Nano成功运行了Llama和Qwen等数十亿参数的开源大模型，并在同等工艺下实现了对行业基准的大幅性能超越，同时还展示了AI在硬件架构设计中的递归自我改进能力。

---

# Redwood: A Frontier AI Accelerator Designed, Verified, and Deployed from Scratch in 2 Weeks by AI

**Authors:** Architect Labs  
**Subject:** Computer Science > Hardware Architecture (`cs.AR`)  
**arXiv ID:** [`arXiv:2608.26418`](https://arxiv.org/abs/2608.26418) [cs.AR]  
**Submitted:** 26 Aug 2026 (Last revised: 28 Aug 2026)

---

## Summary

现代硬件设计周期通常需要数年时间——这往往落后于AI工作负载按月计算的快速演进节奏。为了克服这一根本性瓶颈，Architect Labs 推出了 **Redwood**，这是第一款由AI系统在不到两周时间内完全从零开始设计、验证并部署的达到生产级别的尖端AI加速器。

> Modern hardware design cycles typically take years—often lagging far behind the rapid, monthly evolution of AI workloads. To overcome this fundamental bottleneck, Architect Labs presents **Redwood**, the first production-worthy frontier AI accelerator designed, verified, and deployed entirely from scratch by an AI system in under two weeks. 

从仅由两名人类架构师提供的高级规范出发，该AI在没有规范层级以下任何人工干预的情况下，自主生成了性能模型、RTL设计、UVM环境、形式化证明、固件和内核。

> Starting from only a high-level specification provided by two human architects, the AI autonomously generated the performance model, RTL design, UVM environments, formal proofs, firmware, and kernels without any human intervention below the specification level. 

---

## Key Highlights & Performance

* **快速开发周期：** 在不到两周的时间内完成完整的设计、验证与部署。规范更新的重新验证和重新部署在48小时内完成。
* **严格的验证：** 借助商业EDA工具、专有形式化引擎以及硬件在环验证，每个硬件模块均达到了95%的覆盖率。
* **真实世界能力：** **Redwood Nano**（一种超低功耗的FPGA变体）成功执行了诸如 *Llama* 和 *Qwen* 这样拥有数十亿参数的模型。
* **竞争优势：** 投影至三星 8nm 工艺（与 Jetson Orin Nano 处于同一工艺级别）时，Redwood 展现出：
  * **1.75×** 更高的吞吐量。
  * **1.9×** 更低的功耗。
  * 在运行相同模型时，相比测得的 Jetson 基准硬件，其单位功耗性能（Performance-per-watt）提升了 **3.4×**。
* **递归自我改进：** 在 Redwood 本地运行的 Qwen 模型积极协助设计了*下一代* Redwood 架构。

> * **Rapid Development Cycle:** Fully designed, verified, and deployed in under two weeks. Specification updates were reverified and redeployed in under 48 hours.
> * **Rigorous Verification:** Every hardware block achieved 95% coverage leveraging commercial EDA tools, proprietary formal engines, and hardware-in-the-loop validation.
> * **Real-World Capability:** **Redwood Nano** (an ultra-low-power FPGA variant) successfully executes multi-billion-parameter models like *Llama* and *Qwen*.
> * **Competitive Edge:** Projected onto the Samsung 8nm process (matching the Jetson Orin Nano's class), Redwood delivers:
>   * **1.75×** higher throughput.
>   * **1.9×** lower power consumption.
>   * **3.4×** higher performance-per-watt gain compared to measured baseline Jetson hardware on the same models.
> * **Recursive Self-Improvement:** The Qwen model running locally on Redwood actively assisted in designing the *next-generation* Redwood architecture.

---

## Abstract

> 现代AI工作负载与其运行的硬件在不同的时间尺度上进化：架构定义领先于量产硅片数年，而目标工作负载却在几个月内发生变化。因此，设计决策是在高度不确定的情况下做出的，并且需要付出双重代价：一次是为了对冲风险而增加的通用性成本，另一次则是当新工作负载无法很好地映射到固定的硅片上时的性能损失。随着摩尔定律的停滞，专用化成为保持单位功耗性能的主要剩余源泉，这也要求设计周期必须与工作负载的节奏同步。
> 
> 我们提出了一种端到端的AI系统，它将软件到硅片的整个技术栈折叠成一个单一的优化循环，在此循环中，硬件和软件在同一个目标下进行协同设计与验证。它的首次演示是 Redwood，这是一个专为物理AI的单批次、低功耗、超低延迟推理而构建的前沿AI加速器。根据两名人类架构师提供的高级规范，该系统在规范以下无人工干预的情况下，于两周内自主生成了性能模型、RTL设计、UVM环境、形式化证明、固件和内核。通过商业EDA工具、我们的专有形式化引擎以及硬件在环验证，每个模块都达到了95%的覆盖率。规范变更在48小时内完成了重新验证并部署到硬件中。其超低功耗的FPGA变体 Redwood Nano 运行了 Llama 和 Qwen 等数十亿参数模型。投影到与 Jetson Orin Nano 相同工艺级别的三星 8nm 工艺上时，Redwood 在相同模型上实现了 1.75 倍的吞吐量、1.9 倍的低功耗，以及相对于测得的 Jetson 基准 3.4 倍的单位功耗性能提升。在 Redwood 上运行的 Qwen 还协助设计了下一代 Redwood，这是迈向递归自我改进的早期一步。据我们所知，这是第一个由AI系统端到端设计并运行现代AI模型的达到生产级要求的AI加速器。

> Modern AI workloads and the hardware that runs them evolve on different timescales: architectural definition precedes volume silicon by years, while target workloads shift in months. Design decisions are therefore committed under deep uncertainty and paid for twice, once in the generality added as a hedge, and again when new workloads map poorly onto frozen silicon. As Moore's Law stagnates, specialization is the main remaining source of performance-per-watt and demands a design cycle that runs at the cadence of the workloads. 
>
> We present an end-to-end AI system that collapses the software-to-silicon stack into a single optimization loop, where hardware and software are co-designed and verified under one objective. Its first demonstration is Redwood, a frontier AI accelerator built for single-batch, low-power, ultra-low-latency inference for physical AI. From a high-level specification by two human architects, the system autonomously generated the performance model, RTL design, UVM environments, formal proofs, firmware, and kernels in under two weeks with no human intervention below the specification. Every block reached 95% coverage via commercial EDA tools, our proprietary formal engine, and hardware-in-the-loop validation. Specification changes were reverified and redeployed to hardware in under 48 hours. Redwood Nano, its ultra-low-power FPGA variant, runs multi-billion-parameter models like Llama and Qwen. Projected onto Samsung 8 nm, the Jetson Orin Nano's process class, Redwood delivers 1.75x the throughput at 1.9x lower power, a 3.4x performance-per-watt gain against a measured Jetson baseline on the same models. Qwen running on Redwood also helped design next-generation Redwood, an early step toward recursive self-improvement. To our knowledge, this is the first production-worthy AI accelerator designed end-to-end by an AI system and running a modern AI model.

---

## Full-Text & Resources

* **[在 arXiv 上查看 PDF](https://arxiv.org/pdf/2608.26418)**
* **数字对象唯一标识符 (DOI):** [10.48550/arXiv.2608.26418](https://doi.org/10.48550/arXiv.2608.26418)
* **许可证：** [知识共享 署名-非商业性使用-禁止演绎 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-nd/4.0/)  
  <img alt="license icon" role="presentation" src="./images/fb423b2203a9.png" width="32" />

> * **[View PDF on arXiv](https://arxiv.org/pdf/2608.26418)**
> * **Digital Object Identifier (DOI):** [10.48550/arXiv.2608.26418](https://doi.org/10.48550/arXiv.2608.26418)
> * **License:** [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](http://creativecommons.org/licenses/by-nc-nd/4.0/)  
>   <img alt="license icon" role="presentation" src="./images/fb423b2203a9.png" width="32" />

---
*文献计量工具、代码仓库以及引文参考可直接通过 [arXiv 摘要页面](https://arxiv.org/abs/2608.26418) 获取。*

> *Bibliographic tools, code repositories, and citation references are available directly via the [arXiv abstract page](https://arxiv.org/abs/2608.26418).*