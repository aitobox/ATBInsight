---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-03
hide:
- navigation
tags:
- 模拟集成电路
- 智能体
- 开源数据库
- EDA
- 领域特定语言
title: Analog-DB：面向Agent的模拟集成电路数据库，从模块到系统
---
### 文章背景与核心概要
模拟集成电路设计的共享长期以来一直受到晶圆厂保密协议（NDA，限制了底层工艺细节）以及完整的测试平台（Testbench）极少公开的阻碍。为突破这些障碍，**Analog-DB** 引入了一个开源的版本化数据库，采用了可共享的、工艺无关的表示形式。通过在统一的领域特定语言模式（Schema）下整合工艺无关的拓扑结构、可复用的测试平台以及机器可读的数据手册，该数据库使得人工智能设计Agent能够直接在开源工艺设计库（PDK）中发现、仿真和组合模拟电路。

该研究在涵盖16个类别的68个电路中进行了验证，证明了其在自动化模拟电路设计、智能体协同设计以及跨工艺重定向方面的巨大潜力，为AI赋能的硬件设计提供了关键的基础设施。

---

## 📌 Summary
Sharing analog integrated circuit (IC) designs has historically been hindered by foundry non-disclosure agreements (NDAs)—which restrict underlying process details—and the rare publication of complete testbenches. To overcome these hurdles, **Analog-DB** introduces an open-source, versioned database utilizing a shareable, process-neutral representation. By unifying process-neutral topologies, reusable testbenches, and machine-readable datasheets under a single domain-specific language schema, the database enables AI design agents to directly discover, simulate, and compose analog circuits across open process design kits (PDKs).

> 长期以来，共享模拟集成电路（IC）设计一直受到晶圆厂保密协议（NDA，限制了设计所依赖的底层工艺细节）以及已发表成果背后的测试平台极少公开的阻碍。为了克服这些障碍，**Analog-DB** 推出了一个开源的、版本化的数据库，该数据库利用了可共享的、工艺无关的表示形式。通过在单个领域特定语言模式下统一工艺无关的拓扑结构、可复用的测试平台以及机器可读的数据手册，该数据库使AI设计Agent能够直接跨开源工艺设计库（PDK）发现、仿真和组合模拟电路。

---

## 📋 Metadata

* **arXiv ID:** [arXiv:2609.01286](https://arxiv.org/abs/2609.01286)
* **Subjects:** Artificial Intelligence (`cs.AI`); Hardware Architecture (`cs.AR`); Signal Processing (`eess.SP`)
* **Authors:** Danial Noori Zadeh, Mohamed B. Elamien
* **Submitted On:** September 1, 2026
* **Paper Length:** 23 pages, 5 figures, 13 tables
* **Repository & Code:** [GitHub Release](https://github.com/MacAnalog/spicexplorer-release)

> * **arXiv ID:** [arXiv:2609.01286](https://arxiv.org/abs/2609.01286)
> * **研究学科:** 人工智能 (`cs.AI`); 硬件架构 (`cs.AR`); 信号处理 (`eess.SP`)
> * **作者:** Danial Noori Zadeh, Mohamed B. Elamien
> * **提交时间:** 2026年9月1日
> * **论文页数:** 23 页, 5 幅图, 13 个表
> * **代码仓库:** [GitHub Release](https://github.com/MacAnalog/spicexplorer-release)

---

## 📖 Abstract

Sharing analog integrated circuit designs remains difficult: foundry non-disclosure agreements restrict the process details a design depends on, and the testbenches behind published results are rarely released. We present **analog-db**, an open-source, versioned database built on a shareable design representation. 

A domain-specific language captures each design as a process-neutral topology, reusable testbenches, and a machine-readable datasheet under one schema, so a design is shared in full and re-simulates on the process kits it is bound to. A parameterization scheme exposes functional sub-blocks and device sizes as named parameters that carry their matching constraints, making circuits composable and retargetable; a schema-governed contract and queryable catalog let AI design agents discover and reuse them directly. 

Across the regulator corpus, all 23 circuit-kit bindings on three open kits meet their own recorded specification bands (typical corner, matched devices, no layout) and 10 of 23 meet a common class band. Seventeen of the 23 imported sizings failed their testbenches and closed under a $gm/ID$ sizing loop driven by the annotated sub-block roles, typically within one to three iterations. In a supervised case study, a coding agent working from the released artifacts sized the op-amp cores of a chopper instrumentation amplifier on an open 130nm kit, locating four hand-entry defects and a missing common-mode feedback loop that the sizing-only baseline did not repair. The database holds 68 circuits across sixteen classes, verifiable at schematic level under a tiered harness and tracked on a power/performance scoreboard.

> 共享模拟集成电路设计仍然十分困难：晶圆厂保密协议限制了设计所依赖的工艺细节，而已发表成果背后的测试平台也极少被发布。我们提出了 **analog-db**，这是一个建立在可共享设计表示基础上的开源、版本化数据库。
> 
> 一种领域特定语言在统一的模式下将每个设计捕获为工艺无关的拓扑结构、可复用的测试平台以及机器可读的数据手册，因此设计可以被完整共享，并在其绑定的工艺套件上重新仿真。参数化方案将功能性子模块和器件尺寸暴露为带有匹配约束的命名参数，使得电路具备可组合性和可重定向性；受模式管辖的契约（schema-governed contract）和可查询的目录让AI设计Agent能够直接发现并复用它们。
> 
> 在稳压器语料库中，三个开源套件上的全部 23 个电路-套件绑定都满足了其自身记录的规范频段（典型角、匹配器件、无版图），其中 23 个中有 10 个满足通用的类别频段。导入的 23 种尺寸中有 17 种在测试平台上失败，并在由注释的子模块角色驱动的 $gm/ID$ 尺寸调整循环下收敛，通常在 1 到 3 次迭代内完成。在一个受监督的案例研究中，一个编码Agent利用发布的构件，在开源 130nm 工艺套件上对斩波仪表放大器的运算放大器核心进行了尺寸调整，定位了四个手动输入的缺陷以及一个仅靠尺寸调整基线无法修复的缺失的共模反馈回路。该数据库包含横跨 16 个类别的 68 个电路，可在分层测试平台下进行原理图级别的验证，并在功耗/性能记分板上进行追踪。