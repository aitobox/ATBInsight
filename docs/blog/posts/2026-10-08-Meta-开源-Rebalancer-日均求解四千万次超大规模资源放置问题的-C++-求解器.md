---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-10-08
hide:
  - navigation
tags:
  - Meta
  - Rebalancer
  - C++
  - 资源调度
  - MIP 求解器
  - 局部搜索
  - 开源项目
  - 产品发布
title: "Meta 开源 Rebalancer：日均求解四千万次超大规模资源放置问题的 C++ 求解器"
---

# Meta 开源 Rebalancer：日均求解四千万次超大规模资源放置问题的 C++ 求解器

> # Meta AI Open-Sources Rebalancer: A C++ Assignment Solver That Runs About 40 Million Placement Problems a Day

### 文章背景与核心概要

在超大规模数据中心中，如何将数以百万计的计算任务、存储分片高效且均衡地安置在数以万计的服务器机架上，是支撑全球海量互联网服务的底层核心难题。这类“分箱与资源放置”问题大多属于计算复杂度极高的 NP-Hard 难题，传统商业优化求解器在面对数百万量级的实体规模时往往力不从心或耗时过长。为此，Meta 正式开源了其在内部生产环境中稳定运行超过 9 年的高性能 C++ 求解器——Rebalancer。该项目创新性地将“问题建模规范”与“底层求解计算”彻底解耦，通过统一的表达式图结构，无缝支持面向小规模任务的精确混合整数规划 (Mixed Integer Programming, MIP) 求解，以及面向超大规模集群的高并发并行局部搜索 (Local Search)，目前在 Meta 内部日均高效处理约 4,000 万次放置决策。Rebalancer 以 Apache 2.0 协议全量开源并提供原生 Python 绑定，为工业界解决海量资源调度、全局流量治理与运筹优化提供了强大而开箱即用的基础设施。

---

## 内容概要

> ## Summary

Meta 正式开源了高性能 C++ 算法库 **Rebalancer**，该项目配备了便捷的 Python 接口，专为解决复杂的分配与放置问题而生 (即在严苛的约束条件与优化目标下，将海量对象合理分配到不同容器中)。Rebalancer 已在 Meta 内部平稳运行超过 9 年，日均处理约 **4,000 万次资源放置问题**，覆盖 30 多种截然不同的业务建模形态。该项目基于 Apache 2.0 协议发布，通过创新的“双求解器架构”巧妙打通了从业务问题抽象到高效求解执行之间的鸿沟：一方面为中小规模任务提供能求得全局最优解的混合整数规划 (Mixed Integer Programming, MIP) 求解器，另一方面为处理对象超过 100 万个的超大规模负载提供极速的大规模并行局部搜索求解器。

> Meta has open-sourced **Rebalancer**, a high-performance C++ library with a Python interface designed to solve complex assignment problems (allocating objects to bins under strict constraints and objectives). Used internally at Meta for over 9 years, the library handles around **40 million placement problems daily** across 30+ unique formulations. Released under the Apache 2.0 license, Rebalancer bridges the gap between problem specification and execution by offering a dual-solver architecture: an optimal Mixed Integer Programming (MIP) solver for smaller tasks and a massively parallel local-search solver for hyperscale workloads (exceeding 1 million objects).

---

## Rebalancer 解决了什么痛点？

> ## What Problem Does Rebalancer Solve?

在 Meta 的超大规模基础设施中，各类资源分配挑战无处不在——从在数据中心摆放服务器机架、向具体服务分配物理服务器，到调度分布式计算任务以及调度全球用户的网络流量。在以往应对这些挑战时，工程师们通常会遭遇两大核心瓶颈：

> Assignment challenges appear everywhere in Meta’s hyperscale infrastructure—from placing racks in datacenters and servers into services, to scheduling tasks and routing global user traffic. Two primary bottlenecks traditionally plagued engineers tackling these issues:

1. **易用性瓶颈**：如何将高度抽象、复杂多变的底层基础设施策略，准确翻译为严谨的数学规划公式；
2. **可扩展性瓶颈**：大多数资源放置问题在计算理论上都属于 NP-hard 难题，面对海量数据时其计算复杂度呈爆炸式增长，传统商业求解器根本无法承受如此庞大的求解规模。

> 1. **Usability:** Translating abstract infrastructure policies into precise mathematical formulas.
> 2. **Scalability:** Many resource allocation problems are NP-hard and far too massive for traditional commercial solvers.

Rebalancer 巧妙地化解了这一困局，其核心思想在于将**“如何定义/描述问题”**与**“如何求解计算问题”**彻底解耦。关于这一系统架构的完整理论与工程细节，已发表在其入选顶会系统的 [OSDI 2024 论文](https://www.usenix.org/conference/osdi24/presentation/kumar) 中。

> Rebalancer solves this by decoupling **how a problem is specified** from **how it is solved**, an architecture detailed in its [OSDI 2024 paper](https://www.usenix.org/conference/osdi24/presentation/kumar).

---

## 规范描述层的工作机制

> ## How the Specification Layer Works

Rebalancer 的问题描述语言被精心划分为三个清晰的抽象层级：

> The specification language is structured into three distinct layers:

* **建模基础构件 (Modeling Constructs)**：定义资源的具体维度 (例如 CPU、存储属性等)、分区 (对象的分组集合)、作用域 (容器的分组集合) 以及资源利用率指标；
* **表达式 API (Expression API)**：提供灵活的聚合计算操作 (例如 `SUM` 求和或 `MAX` 求极大值)，并支持各类数学变换 (例如 `SQUARE` 平方运算)；
* **规范 API (Spec API)**：内置开箱即用的数十种预设优化目标与约束条件 (例如用于容量限制的 `CapacitySpec`、控制分组数量的 `GroupCountSpec`，以及实现负载均衡的 `BalanceSpec` 等)。

> * **Modeling Constructs:** Dimensions (e.g., CPU, storage attributes), partitions (groups of objects), scopes (groups of bins), and utilization metrics.
> * **Expression API:** Aggregate utilization using operations like `SUM` or `MAX`, or apply mathematical transformations like `SQUARE`.
> * **Spec API:** Access to dozens of predefined objectives and constraints (such as `CapacitySpec`, `GroupCountSpec`, and `BalanceSpec`).

---

## 统一表达式图与双求解器架构

> ## One Expression Graph, Two Solvers

Rebalancer 会将用户定义的业务规范编译为一个有向无环表达式图，进而驱动两种截然不同且优势互补的求解引擎：

> Rebalancer compiles specifications into a directed acyclic expression graph, enabling two distinct solving strategies:

* **最优解求解器 (MIP)**：自动将表达式图转换为标准的混合整数规划问题，底层支持无缝对接 **FICO Xpress**、**Gurobi** 或 **HiGHS** 等成熟后端，非常适合追求理论全局最优的中小规模调度场景；
* **局部搜索求解器 (Local Search Solver)**：直接作用于编译生成的表达式图，能够以大规模并行的方式高效评估对象之间的迁移与交换操作，每秒运算评估次数高达数百万次。面对极其庞大的超大规模基础设施挑战时，Meta 正是依托该引擎实现秒级高效收敛。

> * **Optimal Solver (MIP):** Translates the graph into a Mixed Integer Program using backends like **FICO Xpress**, **Gurobi**, or **HiGHS**. Ideal for small-to-mid-scale problems.
> * **Local Search Solver:** Operates directly on the expression graph by evaluating object moves and swaps in parallel, achieving millions of evaluations per second. Meta relies on this method for its largest infrastructure challenges.

---

## Meta 内部生产环境实测数据

> ## Production Numbers at Meta

* **日均求解 4,000 万次**：覆盖全公司 30 多种完全不同的业务场景与建模公式；
* **P99 求解时间仅需 12 秒**：在包含 26.5 万个对象与 3,200 个容器的典型生产负载下达成；
* **超大规模平均求解时间仅 171 秒**：在对象规模突破 100 万且容器超过 5,000 个的超大型极值负载下，历经 3,400 多次实际运行测得。

> * **40 million** assignment problems solved daily across 30+ unique formulations.
> * **P99 solve time of 12 seconds** on workloads featuring 265k objects and 3.2k bins.
> * **Average solve time of 171 seconds** for hyperscale workloads exceeding 1 million objects and 5k bins (across 3.4k+ runs).

---

## 典型应用场景

> ## Best Use Cases

1. **集群资源分配**：在严格满足 CPU、内存等资源容量上限的同时，将数据分片、容器或计算任务分配至服务器，并保证副本跨物理机架均匀分布 (例如 Meta 内部著名的 *Shard Manager* 与 *RAS* 系统)；
2. **全局流量管理**：在满足网络延迟与带宽约束的前提下，将在线工作负载与边缘接入流量精准导流至最适宜的数据中心 (例如 Meta 的 *Taiji* 流量管理系统)；
3. **运维与运营调度**：依据复杂的容量与规则限制，自动分发客服工单至对应的工程师、分配会议室资源或调度办公工位等。

> 1. **Cluster Resource Allocation:** Assigning shards, containers, or tasks to servers while respecting resource caps and distributing replicas across racks (e.g., Meta’s *Shard Manager* and *RAS*).
> 2. **Global Traffic Management:** Routing workloads and edge traffic to datacenters while balancing latency constraints (e.g., *Taiji*).
> 3. **Operational Logistics:** Mapping support tickets to engineers, allocating conference rooms, or assigning office desks based on capacity rules.

---

## Rebalancer 与主流开源方案特性对比

> ## Rebalancer vs. Closest Open-Source Alternatives

| 特性维度 | Meta Rebalancer | Google OR-Tools | Timefold Solver (Community 社区版) |
| :--- | :--- | :--- | :--- |
| **开源许可证** | [Apache 2.0](https://github.com/facebook/rebalancer/blob/main/LICENSE) | [Apache 2.0](https://github.com/google/or-tools/blob/stable/LICENSE) | [Apache 2.0](https://github.com/TimefoldAI/timefold-solver) *(企业版闭源商业化)* |
| **核心实现语言** | C++ | C++ | Java |
| **支持 API 语言** | C++, Python | C++, Python, Java, C# | Java, Kotlin |
| **核心聚焦点** | 通用分配/放置问题 (将对象分配至容器) | 综合性套件：涵盖 CP-SAT、LP、MIP 包装器、路径规划、装箱问题等 | 业务规划：路径规划、排班考勤、作业调度、任务分派 |
| **局部搜索能力** | 支持，基于表达式图的高并发并行评估 | [支持，内置于路径规划求解器中](https://developers.google.com/optimization/routing/routing_options) | [支持，作为核心求解引擎](https://docs.timefold.ai/timefold-solver/latest/optimization-algorithms/local-search) |
| **MIP 求解后端** | FICO Xpress, Gurobi, HiGHS | 封装对接多种商业/开源求解器 | 不支持 / 未使用 |
| **调试可视化 UI** | Rebalancer Explorer (基于 Docker) | 官方 README 中未列出 | 基准测试套件；商业版中提供评分诊断分析 |
| **安装方式** | `pip install rebalancer` | `pip install ortools` | Maven, JDK 21+ |

> | Feature | Meta Rebalancer | Google OR-Tools | Timefold Solver (Community) |
> | :--- | :--- | :--- | :--- |
> | **License** | [Apache 2.0](https://github.com/facebook/rebalancer/blob/main/LICENSE) | [Apache 2.0](https://github.com/google/or-tools/blob/stable/LICENSE) | [Apache 2.0](https://github.com/TimefoldAI/timefold-solver) *(Enterprise is commercial)* |
> | **Core Language** | C++ | C++ | Java |
> | **APIs** | C++, Python | C++, Python, Java, C# | Java, Kotlin |
> | **Focus** | Generic assignment (objects to bins) | Broad suite: CP-SAT, LP, MIP wrappers, routing, packing | Planning: routing, rostering, scheduling, task assignment |
> | **Local Search** | Yes, parallel, on expression graph | [Yes, in routing solver](https://developers.google.com/optimization/routing/routing_options) | [Yes, core engine](https://docs.timefold.ai/timefold-solver/latest/optimization-algorithms/local-search) |
> | **MIP Backends** | FICO Xpress, Gurobi, HiGHS | Wrappers for commercial/open-source solvers | Not used |
> | **Debugging UI** | Rebalancer Explorer (Docker) | Not listed in README | Benchmarker; score analysis in commercial editions |
> | **Installation** | `pip install rebalancer` | `pip install ortools` | Maven, JDK 21+ |

---

## 核心要点梳理

> ## Key Takeaways

* **高度通用的抽象模型**：Rebalancer 将现实世界中任意复杂的资源放置问题，统一抽象为对象、容器、约束条件以及优化目标；
* **双求解器灵活驱动**：上层业务规范统一编译为表达式图，既可驱动并行局部搜索求解，亦可直接对接 MIP 商业/开源后端 (**FICO Xpress**、**Gurobi**、**HiGHS**)；
* **超大规模生产验证**：历经 Meta 内部 9 年以上的真实超大规模集群检验，日均稳定承载数千万次高并发放置计算；
* **全面开源易于集成**：采用极为宽松的 **Apache 2.0 许可证**，提供原生 **C++ 与 Python API**，通过 `pip install rebalancer` 即可一键安装使用。

> * Rebalancer abstracts any assignment problem into objects, bins, constraints, and objectives.
> * Specifications compile into expression graphs solved via local search or MIP backends (**FICO Xpress**, **Gurobi**, **HiGHS**).
> * Proven at hyperscale inside Meta, handling millions of complex placement routines daily.
> * Open-sourced under the **Apache 2.0 license** with native **C++ and Python APIs** (`pip install rebalancer`).

---

## 项目资源与参考链接

> ## Resources & Links

* **代码仓库与官方文档**：[GitHub 代码仓库](https://github.com/facebook/rebalancer) | [官方技术文档](https://facebook.github.io/rebalancer/)
* **学术研究与工程深度解析**：[OSDI 2024 会议论文](https://www.usenix.org/system/files/osdi24-kumar.pdf) | [Meta 工程官方发布博文](https://engineering.fb.com/2026/09/21/open-source/rebalancer-generic-high-performance-library-assignment-problems/)
* **PyPI 安装包**：[PyPI 官方主页 (rebalancer)](https://pypi.org/project/rebalancer/)

> * **Documentation & Code:** [GitHub Repository](https://github.com/facebook/rebalancer) | [Official Documentation](https://facebook.github.io/rebalancer/)
> * **Research & Technical Details:** [OSDI 2024 Paper](https://www.usenix.org/system/files/osdi24-kumar.pdf) | [Engineering at Meta Announcement](https://engineering.fb.com/2026/09/21/open-source/rebalancer-generic-high-performance-library-assignment-problems/)
> * **PyPI Package:** [rebalancer on PyPI](https://pypi.org/project/rebalancer/)
