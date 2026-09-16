---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-09-17
hide:
  - navigation
tags:
  - 移动端智能体
  - GUI Agent
  - BlueLM
  - 自我演进
title: "BlueLM-GUI 技术报告：面向自进化移动端 GUI 智能体的真机飞轮系统"
---

# BlueLM-GUI 技术报告：面向自进化移动端 GUI 智能体的真机飞轮系统

> # BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents

> **arXiv:** [2609.12394](https://arxiv.org/abs/2609.12394) [cs.AI]  
> **Submitted on:** 11 September 2026 (v1), last revised 15 September 2026 (v3)  
> **Authors:** Tong Ye, Kunyang Han, Guozhi Wang, Longqiang Luo, Zhifeng Ding, Yongxiang Zhang, Xiaolei Shen, Yuxuan Zhang, Zhuping Zhang, Tao Xu, Yue Pan, Yucheng Zhao, Yupei Hu, Yuanjiang Ouyang, Danfeng Shen, Runqi Lin, Hongda Cai, Zhaoxiong Wang, Mengjia Yan, Yingjie Zhong, Chen Zhou, Zeyu Zhang, Xuwen Zhu, Penggang Shi, Mingcheng Luo, Ziyang Wu, Min Jin, Mingfu Shen, Zairong Xu, Fan Zhang, Hao Wang, Liang Liu, Zhulin Xie, Lijun Yao, Xiao Liang, Liangmin Wen, Liqiang Feng, Feilong Wu, Min Hu, Min Chen, Guanjing Xiong, Xiaohu Ruan, Xiaoxin Chen  

### 文章背景与核心概要

当前，能够像人类一样自主操作手机应用的移动端图形用户界面智能体 (GUI Agent) 正成为前沿热点，但现有模型在模拟沙盒中表现出色，一到真实真机环境下往往频频碰壁。本论文推出了 BlueLM-GUI——一个拥有 350 亿参数 (35B-A3B) 的移动端 GUI 智能体，首次确立了以“真实物理设备”为核心的数据与演进飞轮系统。该系统贯彻“珍惜每个样本、交互基于真机、评测动态演进”三大原则，不仅将真机操作中的报错转化为宝贵的高质量训练数据，还在数百台真实物理手机上展开强化学习。在 MobileGUI-VBench 与 AndroidWorld 等权威基准测试中，BlueLM-GUI 均斩获顶尖成绩，大幅超越顶尖闭源与开源模型，为移动端智能体的工业规模化落地开辟了全新路径。

---

## 执行摘要

> ## Executive Summary

在移动端，能够帮我们操作手机应用的图形用户界面 (GUI) 智能体 (AI Agent) 正在经历深刻演化——正从以往拼凑式的模块化框架，迅速转向浑然一体的原生端到端训练模型。然而，要想把这种智能体真正推向实际工业化落地，长期以来一直受制于三大棘手瓶颈：

> Mobile Graphical User Interface (GUI) agents are rapidly transitioning from modular frameworks to native, end-to-end trained models. However, industrial deployment has historically been impeded by three persistent bottlenecks:

1. **分布偏差 (Distribution Mismatch)**：传统的沙盒模拟训练环境很难真实还原真实生产环境中的复杂状况；
2. **失败经验未充分利用 (Underutilized Failures)**：智能体在真机上执行任务遭遇的昂贵报错，往往被随手丢弃，未能转化为反哺训练的养料；
3. **基准测试易饱和 (Benchmark Saturation)**：固定的静态基准测试很快就会被模型“刷爆”，逐渐失去指引模型持续迭代的能力。

> 1. **Distribution Mismatch:** Sandbox training environments fail to accurately simulate real-world production conditions.
> 2. **Underutilized Failures:** Expensive errors occurring on physical devices are typically discarded rather than leveraged for training.
> 3. **Benchmark Saturation:** Static benchmarks quickly saturate, reducing their efficacy in guiding model iteration.

为了攻克这些难题，研究团队推出了 **BlueLM-GUI**——一个基于“以真机为中心”的自我演化飞轮打造的 350 亿参数 (35B-A3B) 移动端 GUI 智能体。BlueLM-GUI 严格秉持三大核心理念——**“珍惜每个样本” (Every Sample Matters)**、**“交互基于真机” (Every Rollout Is Real)** 以及 **“评测动态演进” (Every Query Evolves)**，成功跨越了虚拟模拟与真实应用之间的鸿沟，在多项主流权威评测中均斩获了顶尖水准的性能表现。

> To address these challenges, the authors introduce **BlueLM-GUI**, a 35B-A3B mobile GUI agent built around a real-device-centric self-improvement flywheel. By adhering to three core principles—**Every Sample Matters**, **Every Rollout Is Real**, and **Every Query Evolves**—BlueLM-GUI bridges the gap between simulated training and real-world deployment, achieving state-of-the-art performance across major evaluation suites.

---

## BlueLM-GUI 飞轮的核心设计原则

> ## Core Principles of the BlueLM-GUI Flywheel

### 1. 珍惜每个样本 (Every Sample Matters)

> ### 1. Every Sample Matters

为了避免宝贵的训练数据白白浪费，该系统设计了一套双轨数据处理链路，包含两大关键组件：

> To prevent valuable training data from being lost, the framework incorporates a dual-track pipeline featuring:

* **异构三系统共识评测 (Heterogeneous Triple-System Consensus Evaluation)**：通过多个异构系统的交叉验证，对智能体的行为进行极其严格的把关与评估；
* **纠错与衍生模块 (Error Correction & Derivation Module)**：这是一套专门设计的“抢救”机制，能够把智能体在交互中失败的任务轨迹重新修正、衍生，进而转化为高水准的监督微调训练数据。

> * **Heterogeneous Triple-System Consensus Evaluation:** Multi-system validation to rigorously assess agent behaviors.
> * **Error Correction & Derivation Module:** A dedicated mechanism that rescues failed trajectories and transforms them into high-quality supervised data.

### 2. 交互基于真机 (Every Rollout Is Real)

> ### 2. Every Rollout Is Real

模型的能力并非闭门造车，而是通过一套三阶段训练方案直接与真实生产环境紧密锚定：

> Model capabilities are grounded directly in production environments using a three-stage recipe:

* **持续预训练 (Continual Pre-training)**
* **监督微调 (Supervised Fine-Tuning, SFT)**
* **智能体强化学习 (Agentic Reinforcement Learning)**：直接在数百台真实的物理手机上并发运行强化学习训练，从而确保模型在真实设备上沉淀出的能力，可以毫无损耗地无缝迁移到用户的实际使用场景中。

> * **Continual Pre-training**
> * **Supervised Fine-Tuning (SFT)**
> * **Agentic Reinforcement Learning** executed across hundreds of physical mobile devices to ensure seamless transfer to user deployments.

### 3. 评测动态演进 (Every Query Evolves)

> ### 3. Every Query Evolves

为了防止静态基准测试迅速过时、无法持续指引模型升级，团队提出了一套基于配额驱动的动态基准测试方法，并在三个相互独立的正交维度上展开结构化设计。这种机制不仅能对智能体出现的错误进行极为精准的根因归因，还能让评测基准随着模型自身能力的演进实现动态扩展与难度升级。

> To combat benchmark stagnation, the team established a quota-driven benchmark methodology structured across three orthogonal axes. This allows for precise error attribution and enables benchmarks to scale dynamically alongside model improvements.

---

## 核心性能评估结果

> ## Key Performance Results

在业界多项标准的权威基准测试中，BlueLM-GUI 均展现出了出类拔萃的实战能力：

> BlueLM-GUI demonstrates exceptional capabilities on standard industry benchmarks:

* **MobileGUI-VBench 基准测试**：取得了 **87.4** 的优异成绩，大幅领先最优秀的顶级闭源模型整整 5.1 分；
* **AndroidWorld 基准测试**：斩获 **84.9** 的高分，不仅稳居所有开源模型的榜首第一名，即便与顶尖的闭源模型相比也丝毫不落下风。

> * **MobileGUI-VBench:** Achieves a score of **87.4**, outperforming the leading closed-source model by 5.1 points.
> * **AndroidWorld:** Achieves a score of **84.9**, securing the top performance among all open-source models while remaining highly competitive with closed-source alternatives.

---

## 补充信息与资源

> ## Additional Information

* **主要学科领域**：人工智能 (`cs.AI`)
* **论文篇幅**：49 页
* **全文资源**：
  * [查看 PDF 论文](https://arxiv.org/pdf/2609.12394)
  * [实验性 HTML 网页版](https://arxiv.org/html/2609.12394v3)
  * [TeX 源代码](https://arxiv.org/src/2609.12394)
* **数字对象唯一标识符 (DOI)**：[10.48550/arXiv.2609.12394](https://doi.org/10.48550/arXiv.2609.12394)

> * **Primary Subject:** Artificial Intelligence (`cs.AI`)
> * **Length:** 49 pages
> * **Full-Text Resources:** 
>   * [View PDF](https://arxiv.org/pdf/2609.12394)
>   * [Experimental HTML Version](https://arxiv.org/html/2609.12394v3)
>   * [TeX Source](https://arxiv.org/src/2609.12394)
> * **Digital Object Identifier (DOI):** [10.48550/arXiv.2609.12394](https://doi.org/10.48550/arXiv.2609.12394)
