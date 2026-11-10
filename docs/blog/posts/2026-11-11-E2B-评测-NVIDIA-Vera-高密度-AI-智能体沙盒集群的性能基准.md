---
authors:
  - aitoboxrobot
categories:
  - 研究解读
date: 2026-11-11
hide:
  - navigation
tags:
  - NVIDIA Vera
  - E2B
  - AI智能体沙盒
  - 基准测试
  - Firecracker
title: "E2B 评测 NVIDIA Vera：高密度 AI 智能体沙盒集群的性能基准"
---

# E2B 评测 NVIDIA Vera：高密度 AI 智能体沙盒集群的性能基准

![Featured Image](./images/4a224b6c03bc.jpg)

### 文章背景与核心概要
随着大语言模型和 AI 智能体 (AI Agent) 快速走向自主代码执行与复杂任务协作，如何在单台物理服务器上安全、高效、高密度地运行成千上万个轻量化隔离沙盒，成为当下 AI 基础设施面临的核心工程瓶颈。知名沙盒运行时平台 E2B 率先对 NVIDIA 即将推出的新一代 Vera 服务器展开了预生产环境下的深度基准测试 (Benchmark)。实测表明，在基于 Firecracker 微虚拟机 (MicroVM) 的高密度隔离架构下，双路 Vera 服务器能够稳定支撑多达 1,400 至 1,550 个并发活跃沙盒，并在单线程算力与快照恢复至关重要的内存吞吐量上显著超越传统 x86 参考架构。尽管实现极限密度依赖深入的宿主机内核与网络微调，且能耗经济性尚待多节点测试检验，该评测依然为下一代超大规模智能体集群的算力架构演进提供了极具价值的实证参考。

---

## 内容概要

> ## Summary

2026 年 11 月，E2B 公布了针对 [NVIDIA Vera 服务器](https://www.unite.ai/nvidia-pits-vera-cpu-against-x86-on-agent-speed-and-power-capacity/) 承载高密度 AI 智能体 (AI Agent) 沙盒集群能力的早期工程测试结果。借助一台双路 Vera 预生产服务器，测试团队成功维持了 1,400 至 1,550 个高负载沙盒的稳定运行；在特定的处理器单线程与内存微基准测试 (Microbenchmark) 中，其性能更是显著超越了作为参照的 AMD EPYC 处理器。尽管这批早期实测数据展现出了微虚拟机 (MicroVM) 隔离扩展的巨大潜力，但该评估仍属于工程样机阶段测试，不仅依赖特定的宿主机参数深度调优，且在综合运营成本、整机能耗以及多节点扩展方面仍有待进一步验证。

> In November 2026, E2B published pre-production test results evaluating the performance of the [NVIDIA Vera server](https://www.unite.ai/nvidia-pits-vera-cpu-against-x86-on-agent-speed-and-power-capacity/) for high-density agent sandbox fleets. Utilizing a pre-production dual-socket Vera server, tests demonstrated the ability to sustain between 1,400 and 1,550 loaded sandboxes while outperforming an AMD EPYC reference in specific processor and memory microbenchmarks. While these early findings highlight significant potential for isolated microVM scaling, the evaluation remains a pre-production test with specific host tuning requirements and unresolved cost, power, and multi-node considerations.

---

## 处理器与内存微基准测试

> ## Processor and Memory Microbenchmarks

本次针对 Vera 的评测于 2026 年 10 月 9 日至 13 日展开，测试平台为一台配备 176 个物理核心和 1,479 GiB 内存的双路工程样机服务器，并将其性能与 2026 年 8 月测得的 AMD 平台基准数据进行了横向对比。

> The Vera tests were conducted between October 9 and 13, 2026, on a pre-production dual-socket server featuring 176 physical cores and 1,479 GiB of RAM, compared against AMD reference measurements taken in August 2026.

* **计算性能**：在基于宿主机裸机、采用 Vera 专属 64K 内存页内核的单线程计算测试中，E2B 测得 Vera 的吞吐量达到 **每秒 7,759 次事件**，而作为对照的 AMD EPYC 9B45 则为 **每秒 5,131 次**（基于至少 3 次测试的中位数计算，Vera 达到了参照系统吞吐量的 1.51 倍）。
* **内存吞吐量**：在针对 2 GiB 内存区域、采用 4K 内核并启用 2 MiB 大页内存 (Huge Pages) 的测试中（这也是 E2B 沙盒实际采用的大页内存支持机制），Vera 飙升至 **62.8 GB/s**，相比 AMD 的 **17.4 GB/s** 实现了高达 3.61 倍的吞吐量跃升。对于需要高频从快照恢复环境的沙盒运行时而言，这项指标至关重要。

> * **Compute Performance:** In a bare-host, single-thread compute test using Vera’s 64K-page kernel, E2B reported **7,759 events per second** for Vera compared to **5,131** for the AMD EPYC 9B45 (achieving 1.51 times the reference throughput based on the median of at least three runs).
> * **Memory Throughput:** Testing a 2 GiB memory region using 4K kernels and 2 MiB huge pages (the same huge-page backing used by E2B's sandboxes), Vera reached **62.8 GB/s** compared to AMD's **17.4 GB/s**, marking 3.61 times the throughput. This metric is vital for a runtime that repeatedly restores snapshot-backed environments.

*注：上述对比严格受限于特定微基准测试下的指定硬件型号，并不代表端到端智能体执行速度获得了同等比例的提升，亦不构成相对于 AMD 的绝对集群容量优势。*

> *Note: These comparisons are limited to named systems in specific microbenchmarks and do not establish direct end-to-end agent speedups or absolute fleet-capacity advantages over AMD.*

## 全栈容量评估与宿主机调优

> ## Full-Stack Capacity and Host Tuning

在全栈容量评估中，E2B 采用了 **E2B Embed**——这是开源 E2B Runtime 及其监控面板的单机封装版本——直接运行在宿主机上，并通过 Firecracker 微虚拟机实现轻量化硬件级安全隔离。

> For full-stack evaluations, E2B utilized **E2B Embed**—its single-machine packaging of the open-source E2B Runtime and dashboard—running directly on the host with Firecracker microVM isolation.

* **系统响应能力**：在低负载的独立裸机测试中，评估记录到了 **50 毫秒的热启动顺序沙盒启动耗时** 以及 **3.8 毫秒的命令往返延迟**。在极高换流 (Churn) 压力测试下，系统连续完成了 **22,145 次沙盒创建与销毁循环，且保持零错误**。
* **混合负载表现**：在混合容量测试中，沙盒会交替执行 CPU 突发计算、10 MiB 磁盘写入与短暂休眠暂停（其中十分之一的沙盒保持持续运转），在此场景下第 95 百分位 (P95) 命令往返延迟最高仅为 **255 毫秒**。而当所有沙盒都处于持续不间断高压运行时，系统仍能稳定支撑 **550 个沙盒**。
* **配置约束与调优**：默认的宿主机操作系统配置仅能支持 320 个沙盒；在针对网络邻居表 (Network-neighbor) 进行内核调优后，容量提升至 1,000 个；而只有在完成全系统的底层调优后，才最终释放出巅峰并发容量。E2B 特别强调，这体现的是系统底层配置的阶梯式优化成果，而非单纯由 Vera 硬件架构直接带来的通用性加速。

> * **Responsiveness:** Evaluations recorded **50 ms warm, sequential sandbox starts** and **3.8 ms command round trips** at low load during separate bare-metal tests. A churn test completed **22,145 create-and-destroy cycles with zero errors**.
> * **Mixed Workloads:** In mixed capacity tests where sandboxes continuously performed CPU bursts, 10 MiB disk writes, and pauses (with 1 in 10 running continuously), the 95th-percentile command round-trip latency peaked at **255 ms**. When all sandboxes ran continuously, the system sustained **550 sandboxes**.
> * **Configuration Constraints:** Default host settings only supported 320 sandboxes. Network-neighbor tuning elevated this to 1,000, while full system tuning was required to reach peak capacity. E2B emphasizes this represents a configuration progression rather than a blanket Vera-versus-x86 speedup.

## 评估局限性与后续测试规划

> ## Evaluation Limits and Planned Tests

由于本次评估完全基于工程样机硬件展开，目前仍有一些关键技术问题尚待明确：

> Because the evaluation was conducted on pre-production hardware, several questions remain open:

* 作为对照的 x86 参考系统在某些特定的快照恢复操作上速度依然更快；
* 嵌套虚拟化 (Nested Virtualization) 仍需要额外的底层工程开发与适配；
* 本次测试未采集功耗与成本数据，因此尚未涵盖实际的单机运营经济效益评估。

> * x86 reference systems still completed certain restore operations faster.
> * Nested virtualization requires additional engineering work.
> * Operating economics were excluded, as no power or cost measurements were taken.

**后续计划**：E2B 计划进一步扩大测试范围，包括搭建多节点 [Vera](https://www.unite.ai/modal-plans-nvidia-vera-rollout-for-sandboxes-in-first-arm-move/) 集群测试、评估基于对象存储的冷快照恢复性能，并采用完全一致的软件封装与宿主机调优配置与 x86 平台进行标准化横向评测。

> **Next Steps:** E2B plans to expand its testing to include multi-node [Vera](https://www.unite.ai/modal-plans-nvidia-vera-rollout-for-sandboxes-in-first-arm-move/) clusters, cold resumes backed by object storage, and standardized x86 comparisons using identical packaging and host tuning.
