---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-05
hide:
- navigation
tags:
- 图神经网络
- 强化学习
- 任务调度
- 云边端计算
- DAG
title: PPO-STGNN：结合时空图神经网络与近端策略优化的云边端计算DAG任务调度方法
---
### 文章背景与核心概要
随着物联网（IoT）的迅猛发展，计算密集型有向无环图（DAG）任务在现代云边端协同环境中变得日益普遍。然而，由于云、边、端节点在计算能力、网络带宽和能耗方面存在极端的异构性，如何高效调度这些具有复杂依赖关系的任务是一个典型的NP-hard问题。传统的启发式算法和常规强化学习方法往往难以捕捉系统资源复杂多变的时空动态特征。

为了解决这一挑战，本文作者提出了 **PPO-STGNN** 这一全新的调度框架。该框架结合了时空图神经网络（STGNNs）来提取任务拓扑与物理资源的特征，并利用近端策略优化（PPO）算法最小化完工时间（Makespan）和调度长度比（SLR），同时优化CPU与内存的负载均衡。此外，该研究还引入了多教师行为克隆机制用于预训练，从而加速策略收敛。实验结果表明，PPO-STGNN在保持较低任务完成时间的同时显著提升了负载均衡能力，展现出其在动态异构云边端调度场景中的巨大应用价值。

---

## 📌 Summary

> With the rapid expansion of the Internet of Things (IoT), computation-intensive Directed Acyclic Graph (DAG) tasks have become increasingly prevalent in modern cloud-edge-end collaborative environments. However, efficiently scheduling these dependent tasks is an **NP-hard problem** due to the extreme heterogeneity of cloud, edge, and end nodes in terms of computing capacity, network bandwidth, and energy consumption. 
> 
> Traditional heuristic algorithms and conventional reinforcement learning methods often struggle to capture the complex spatio-temporal dynamics of system resources. To address this, the authors introduce **PPO-STGNN**, a novel scheduling framework that combines:
> 1. **Spatio-Temporal Graph Neural Networks (STGNNs):** Designed to extract rich feature representations from both the DAG task topology and the physical cloud-edge-end resource graph.
> 2. **Proximal Policy Optimization (PPO):** Optimizes the task scheduling policy to minimize the *makespan* and *Schedule Length Ratio (SLR)* while actively improving CPU and memory load balancing.
> 3. **Multi-Teacher Behavior-Cloning:** A pretraining mechanism incorporated to accelerate policy convergence.
> 
> Experimental evaluations demonstrate that PPO-STGNN significantly enhances load balancing while preserving low task completion times, proving its viability for dynamic and heterogeneous cloud-edge-end scheduling scenarios.

---

## 📝 Abstract

随着物联网的迅猛发展，计算密集型有向无环图（DAG）任务在云边端协同环境中变得越来越普遍。然而，云、边、端节点在计算能力、网络带宽和能耗方面具有高度的异构性，这使得对具有复杂依赖关系的任务进行高效调度成为一个NP-hard问题。传统的启发式算法和常规强化学习方法往往无法捕捉系统资源的时空动态特征。本文提出了 PPO-STGNN，这是一种将近端策略优化（PPO）与时空图神经网络（STGNNs）相集成的新型DAG任务调度算法。该方法利用STGNN从DAG任务拓扑和物理云边端资源图中提取特征，然后通过PPO优化调度策略，以最小化完工时间和调度长度比（SLR），同时改善CPU和内存的负载均衡。为了加速收敛，引入了多教师行为克隆机制进行预训练。实验结果表明，PPO-STGNN在保持较低完成时间的同时显著改善了负载均衡，使其非常适合动态和异构的云边端DAG调度场景。

> With the rapid development of the Internet of Things, computation intensive directed acyclic graph (DAG) tasks have become increasingly common in cloud-edge-end collaborative environments. However, cloud, edge, and end nodes are highly heterogeneous in computing capacity, network bandwidth, and energy consumption, which makes the efficient scheduling of tasks with complex dependencies an NP-hard problem. Traditional heuristic algorithms and conventional reinforcement-learning methods often fail to capture the spatio-temporal dynamics of system resources. This paper proposes PPO-STGNN, a DAG task-scheduling algorithm that integrates proximal policy optimization (PPO) with spatio-temporal graph neural networks (STGNNs). The method uses an STGNN to extract features from both the DAG task topology and the physical cloud-edge-end resource graph, and then optimizes the scheduling policy through PPO to minimize makespan and schedule length ratio (SLR) while improving CPU and memory load balancing. To accelerate convergence, a multi-teacher behavior-cloning mechanism is introduced for pretraining. Experimental results show that PPO-STGNN significantly improves load balancing while maintaining a low completion time, making it suitable for dynamic and heterogeneous cloud-edge- end DAG scheduling scenarios.

---

## 🔗 Quick Links & Resources

* **全文访问：** [查看 PDF](https://arxiv.org/pdf/2609.03503)
* **开源许可：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) ![license icon](./images/345c7ad61f1b.png)
* **引用与参考：**
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2609.03503)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2609.03503)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2609.03503)