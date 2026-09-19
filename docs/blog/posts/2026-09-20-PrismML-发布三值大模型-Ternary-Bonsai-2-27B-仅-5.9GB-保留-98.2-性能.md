---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-20
hide:
- navigation
tags:
- PrismML
- 三值量化
- Qwen3.8
- 端侧大模型
- 模型压缩
title: PrismML 发布三值大模型 Ternary Bonsai 2 27B：仅 5.9GB 体积保留 98.2% 顶尖性能
---
# PrismML 发布三值大模型 Ternary Bonsai 2 27B：仅 5.9GB 体积保留 98.2% 顶尖性能

> # PrismML Releases Ternary Bonsai 2 27B: A 5.9 GB Apache 2.0 Model Retaining 98.2% of Qwen3.8 27B Performance

### 文章背景与核心概要
近年来，如何在保持前沿大语言模型 (Large Language Model, LLM) 强大能力的同时，将其体积极致压缩以便在消费级设备上流畅运行，始终是 AI 领域的核心技术挑战之一。PrismML 团队近期正式开源了基于 Qwen3.8 27B 深度优化的三值大模型——**Ternary Bonsai 2 27B**。该模型采用宽松友好的 Apache 2.0 协议，创新性地将权重限制为仅包含 -1、0、+1 的三值离散表示，成功把原本高达 53.80 GB 的庞大模型压缩至惊人的 5.93 GB (平均每个权重仅占 1.72 比特) ，并在 20 项涵盖推理、数学与代码的基准测试中平均保留了原模型 98.2% 的顶尖性能。凭借对文本与图像的多模态理解能力以及 262K 的超长上下文窗口支持，该模型不仅可以在普通 16 GB 笔记本或单张 24 GB 消费级显卡上高吞吐流畅运行，更标志着百亿级端侧大模型向极致能效与平民化部署迈出了里程碑式的一步。

---

## 核心概述

> ## Summary

[PrismML](https://prismml.com/) 正式推出了 [Ternary Bonsai 2 27B](https://prismml.com/news/bonsai-2-27b)，这是基于 [Qwen3.8 27B](https://huggingface.co/Qwen/Qwen3.8-27B) 打造的高能效三值权重衍生模型。该模型采用 Apache 2.0 开源协议，将原本高达 53.80 GB 的半精度 (FP16) 原始模型彻底瘦身至仅 5.93 GB，并在 20 项基准测试中令人惊叹地保留了父模型 98.2% 的平均性能。Ternary Bonsai 2 27B 不仅支持文本与图像理解，还具备 262K Token 的超长上下文窗口；借助 PrismML 提供的定制化运行时，它能够在普通的 16 GB 笔记本电脑或单张 24 GB 显存显卡上轻松完成本地部署。

> [PrismML](https://prismml.com/) has introduced [Ternary Bonsai 2 27B](https://prismml.com/news/bonsai-2-27b), a highly efficient ternary-weight derivative of [Qwen3.8 27B](https://huggingface.co/Qwen/Qwen3.8-27B). Compressing the original 53.80 GB (FP16) model down to a mere 5.93 GB, this Apache 2.0-licensed model preserves an impressive 98.2% of its parent model's average performance across 20 benchmarks. Supporting text, images, and a 262K-token context window, Ternary Bonsai 2 27B can be deployed on a standard 16 GB laptop or a single 24 GB GPU using PrismML’s custom runtimes.

---

## 什么是 Ternary Bonsai 2 27B？

> ## What is Ternary Bonsai 2 27B?

该模型完整继承了 Qwen3.8 27B 的基础架构，总参数量达 273.6 亿 (27.36B) ，具体分布如下：

> The model preserves the foundational architecture of the Qwen3.8 27B with its 27.36 billion parameters, distributed as follows:

* **语言主干网络 (Language Backbone) ：** 243.5 亿 (24.35B) 参数 (采用混合注意力机制：约 75% 线性注意力层和 25% 全注意力层) ；
* **嵌入层与语言模型头 (Embeddings & LM Head) ：** 25.4 亿 (2.54B) 参数；
* **视觉塔 (Vision Tower) ：** 4.7 亿 (0.47B) 参数 (以独立的 0.63 GB GGUF 文件分发，仅在处理图像时载入) 。

> * **Language Backbone:** 24.35B parameters (utilizing hybrid attention: ~75% linear-attention and 25% full-attention layers).
> * **Embeddings & LM Head:** 2.54B parameters.
> * **Vision Tower:** 0.47B parameters (shipped as a separate 0.63 GB GGUF file, loaded only when processing images).

三值权重广泛应用于嵌入层、注意力投影矩阵、MLP 投影层以及语言模型头 (LM Head) 。全模型仅有 2620 万 (26.2M) 参数 (占比仅 0.0976%) 依然保留在较高精度，这些高精度参数主要集中在循环状态路径与归一化权重上。

> Ternary weights are applied across embeddings, attention projections, MLP projections, and the LM head. Only 26.2M parameters (0.0976%)—specifically the recurrent state path and normalization weights—remain in higher precision.

## 三值量化格式是如何工作的？

> ## How Does the Ternary Format Work?

该模型的权重被严格限制在三个离散值之间：**-1、0 或 +1**。

> The model utilizes weights restricted to three values: **-1, 0, or +1**.

* **比特分配 (Bit Allocation) ：** 每 128 个权重组成一组，共享一个 FP16 缩放因子 (Scale) 。单个三进制数值携带 $\log_2(3)$ (约 1.585) 比特的信息量。结合缩放因子开销与保留的高精度张量，模型的实际运行开销为**每个权重 1.72 比特 (1.72 bits per weight)**。
* **打包方案 (Packings) ：** 为了在实际算子内核上获得极致性能，[技术白皮书](https://github.com/PrismML-Eng/Bonsai-demo/blob/main/bonsai-2-27b-whitepaper.pdf) 详述了两种 GGUF 打包格式：
  * `PTQ1_0`：以每个权重 1.76 比特的密度紧凑打包三进制位 (Trit) (模型总大小 5.93 GB) ；
  * `PQ2_0`：将每个三进制位存入一个 2 比特的槽位中 (模型总大小 7.25 GB) ，能够实现更迅速的解包速度。
* **基底旋转 (Rotated Basis) ：** 遵循 [SpinQuant](https://arxiv.org/abs/2405.16406) 的技术方案，PrismML 在三值分配前引入了分块阿达马旋转 (Hadamard Rotation，分块大小为 1,024) ，并在运行时对激活值应用相应的数学变换。

> * **Bit Allocation:** Every group of 128 weights shares a single FP16 scale. A ternary value carries $\log_2(3)$ (approx. 1.585) bits. Combined with the scale overhead and high-precision tensors, the model operates at **1.72 bits per weight**.
> * **Packings:** To optimize performance on real kernels, the [whitepaper](https://github.com/PrismML-Eng/Bonsai-demo/blob/main/bonsai-2-27b-whitepaper.pdf) details two GGUF packings:
>   * `PTQ1_0`: Packs trits densely at 1.76 bits per weight (5.93 GB total size).
>   * `PQ2_0`: Stores each trit in a 2-bit slot (7.25 GB total size), offering faster unpacking.
> * **Rotated Basis:** Following [SpinQuant](https://arxiv.org/abs/2405.16406) methodology, PrismML applies a blockwise Hadamard rotation (block size 1,024) before ternary assignment, with corresponding transformations applied to activations during runtime.

## 与 Qwen3.8 27B 的基准测试对比如何？

> ## How Does It Score Against Qwen3.8 27B?

评估测试由 PrismML 在思考模式下开展，测试环境基于 NVIDIA H100 GPU，并结合了 EvalScope 与 vLLM 推理框架：

> Evaluations were conducted by PrismML in thinking mode using EvalScope and vLLM on H100 GPUs:

| 能力维度 | Qwen3.6 27B | Qwen3.8 27B | Ternary Bonsai 2 27B | 性能保持率 |
| :--- | :---: | :---: | :---: | :---: |
| 知识与推理能力 | 84.71 | 86.66 | 83.95 | 96.9% |
| 数学计算能力 | 94.64 | 97.06 | 96.57 | 99.5% |
| 代码编写能力 | 82.57 | 82.17 | 81.58 | 99.3% |
| 智能体与工具调用能力 | 80.05 | 79.74 | 77.57 | 97.3% |
| 指令遵循能力 | 74.53 | 81.25 | 82.66 | 101.7% |
| 视觉多模态能力 | 79.82 | 81.64 | 78.59 | 96.3% |
| **综合评分 (20 项基准测试) ** | **83.6** | **85.4** | **83.9** | **98.2%** |

> | Capability | Qwen3.6 27B | Qwen3.8 27B | Ternary Bonsai 2 27B | Retention |
> | :--- | :---: | :---: | :---: | :---: |
> | Knowledge and reasoning | 84.71 | 86.66 | 83.95 | 96.9% |
> | Math | 94.64 | 97.06 | 96.57 | 99.5% |
> | Coding | 82.57 | 82.17 | 81.58 | 99.3% |
> | Agentic and tool calling | 80.05 | 79.74 | 77.57 | 97.3% |
> | Instruction following | 74.53 | 81.25 | 82.66 | 101.7% |
> | Vision | 79.82 | 81.64 | 78.59 | 96.3% |
> | **Overall (20 benchmarks)** | **83.6** | **85.4** | **83.9** | **98.2%** |

相较于体积为 7.3 GB 的传统量化构建版本 (例如平均得分仅 75.2 的 `IQ2_XXS`) ，Bonsai 2 展现出了飞跃式的提升——在 AIME26 数学竞赛测试中取得 95.83 分 (对比后者的 78.6 分) ，在 LiveCodeBench v6 编程基准测试中取得 90.07 分 (对比后者的 70.05 分) 。

> Compared to conventional quantization builds like `IQ2_XXS` (averaging 75.2 at 7.3 GB), Bonsai 2 demonstrates dramatic improvements—scoring 95.83 on AIME26 (vs. 78.6) and 90.07 on LiveCodeBench v6 (vs. 70.05).

## 哪些能力依然存在质量损耗？

> ## Where Does It Still Lose Quality?

尽管 98.2% 的综合平均保留率非常优异，但在特定的长流程复杂任务中，模型性能的下滑依然相对明显：

> While the 98.2% overall average is robust, quality drops are more pronounced in specific long-horizon workflows:

* **智能体工作负载 (Agentic Workloads) ：** 在 [Terminal-Bench 2.1](https://www.tbench.ai/news/terminal-bench-2-1) 终端基准测试中，Bonsai 2 得分为 52.8 分 (Qwen3.8 原型为 69.7 分) ；在 [SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) 软件工程智能体基准测试中，其得分为 60.8 分 (对比全精度的 80.6 分，性能保持率约为 75%) 。
* **推理算力投入 (Reasoning Effort) ：** 中等思考预算 (Medium-effort) 下的平均得分为 79.3 分 (对比 FP16 基准的 82.6 分) ，且当前版本暂不支持低思考预算 (Low-effort) 执行。*(注：所有评估数据均源自 PrismML 官方公布，尚待第三方独立复现与验证。)*

> * **Agentic Workloads:** On [Terminal-Bench 2.1](https://www.tbench.ai/news/terminal-bench-2-1), Bonsai 2 scores 52.8 compared to Qwen3.8's 69.7. On [SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/), it scores 60.8 against 80.6 (~75% retention).
> * **Reasoning Effort:** Medium-effort execution averages 79.3 (compared to 82.6 for the FP16 baseline), and low-effort execution is unsupported. *(Note: All evaluation data stems from PrismML and awaits independent verification.)*

## 在真实硬件上的运行速度如何？

> ## How Fast Is It on Real Hardware?

基于 PrismML 自研算子内核在批大小为 1 (Batch Size 1) 解码时的实测性能 (2026 年 9 月测试数据) ：

> Benchmarked at batch size 1 decode on custom PrismML kernels (September 2026):

* **硬件实测速度：**
  * **RTX 5090：** 142.5 Token/秒 (每生成一个 Token 仅耗电 0.582 毫瓦时/mWh) ；
  * **RTX 4090：** 96.7 Token/秒 (采用 `PTQ1_0` 格式) ；
  * **NVIDIA L4 (72W) ：** 32.1 Token/秒；
  * **Apple M5 Max：** 46.8 Token/秒；
  * **Apple M5 Pro：** 27.7 Token/秒。
* **打包格式效率对比：** `PTQ1_0` 在 Ada 架构显卡与 L4 上表现最佳；而在 Blackwell、Hopper、Ampere 以及 Apple 芯片架构上，`PQ2_0` 的运行速度更快。PrismML 同时表示，相较于全精度 8B 模型，该模型的整体能效比提升了 40%。

> * **Hardware Speeds:**
>   * **RTX 5090:** 142.5 tokens/sec (0.582 mWh per token).
>   * **RTX 4090:** 96.7 tokens/sec (using `PTQ1_0`).
>   * **NVIDIA L4 (72W):** 32.1 tokens/sec.
>   * **Apple M5 Max:** 46.8 tokens/sec.
>   * **Apple M5 Pro:** 27.7 tokens/sec.
> * **Packing Efficiency:** `PTQ1_0` excels on Ada-generation cards and the L4, whereas `PQ2_0` is faster on Blackwell, Hopper, Ampere, and Apple silicon architectures. PrismML also claims a 40% improvement in energy efficiency over full-precision 8B models.

## 如何在本地运行？

> ## How Do You Run It?

* **GGUF 格式运行：** 需要使用 PrismML 专门优化的 [llama.cpp 分支仓库](https://github.com/PrismML-Eng/llama.cpp) (原生 llama.cpp 目前无法识别 `PTQ1_0` 与 `PQ2_0` 格式) 。参照 [Bonsai-demo 代码仓库](https://github.com/PrismML-Eng/Bonsai-demo/) 的使用说明，运行 `./setup.sh` 脚本，随后执行 `./scripts/start_llama_server.sh`，即可在本地 `localhost:8080` 启动推理服务。
* **Apple Silicon 平台：** 可直接选用针对 Mac 优化的 [MLX 整合包](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-mlx-2bit) 及其附带的模型加载器。
* **浏览器端体验：** 可以访问 [WebGPU 在线演示](https://huggingface.co/spaces/webml-community/ternary-bonsai-2-webgpu-kernels) ，在现代网络浏览器中直接体验端侧免安装运行。

> * **GGUF Format:** Requires PrismML’s [llama.cpp fork](https://github.com/PrismML-Eng/llama.cpp) (stock llama.cpp rejects `PTQ1_0` and `PQ2_0` formats). Follow instructions in the [Bonsai-demo repo](https://github.com/PrismML-Eng/Bonsai-demo/) by running `./setup.sh` followed by `./scripts/start_llama_server.sh` to launch a local server at `localhost:8080`.
> * **Apple Silicon:** Use the [MLX pack](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-mlx-2bit) with its bundled loader.
> * **Browser:** Explore the [WebGPU demo](https://huggingface.co/spaces/webml-community/ternary-bonsai-2-webgpu-kernels) to run the model directly inside a web browser.

## 核心要点速览

> ## Key Takeaways

* **极致压缩：** 模型最终体积仅为 5.93 GB，比 53.80 GB 的 FP16 全精度基准缩小了约 9.1 倍；
* **极高保留率：** 在 20 项基准测试中平均得分达到 83.9 分，保留了原版 Qwen3.8 27B 模型 98.2% 的顶尖性能；
* **极速推理：** 在 RTX 5090 显卡上能够达到每秒 142.5 Token，在 Apple M5 Max 芯片上可达到每秒 46.8 Token；
* **长流程智能体局限：** 在 SWE-bench 等长跨度复杂任务中，性能保持率下降至全精度的约 75%；
* **需专属运行时：** 当前运行必须依赖 PrismML 定制适配的 llama.cpp 分支或 MLX 运行时。

> * **Massive Reduction:** 5.93 GB model size, operating ~9.1x smaller than the 53.80 GB FP16 baseline.
> * **High Retention:** Achieves an 83.9 average across 20 benchmarks, retaining 98.2% of the parent Qwen3.8 27B model's performance.
> * **Blazing Fast:** Delivers 142.5 tokens per second on an RTX 5090 and 46.8 tokens per second on an M5 Max.
> * **Agentic Limitations:** Long-horizon tasks like SWE-bench drop to roughly 75% retention compared to full precision.
> * **Custom Runtimes Required:** Requires PrismML's specialized llama.cpp fork or MLX runtime to execute.

---

### 资源与链接

> ### Resources & Links

* [技术白皮书 (Whitepaper)](https://github.com/PrismML-Eng/Bonsai-demo/blob/main/bonsai-2-27b-whitepaper.pdf)
* [模型权重集合 (GGUF Collections)](https://huggingface.co/collections/prism-ml/bonsai-2)
* [GitHub 代码仓库 (Bonsai-demo)](https://github.com/PrismML-Eng/Bonsai-demo/)
* [PrismML 官方技术文档](https://docs.prismml.com/)
* [WebGPU 网页端在线演示](https://huggingface.co/spaces/webml-community/ternary-bonsai-2-webgpu-kernels)
* [X (原 Twitter) 官方发布公告](https://x.com/PrismML/status/2100692248480596348)

> * [Whitepaper](https://github.com/PrismML-Eng/Bonsai-demo/blob/main/bonsai-2-27b-whitepaper.pdf)
> * [Model Weights (GGUF collections)](https://huggingface.co/collections/prism-ml/bonsai-2)
> * [GitHub Repository](https://github.com/PrismML-Eng/Bonsai-demo/)
> * [Official Documentation](https://docs.prismml.com/)
> * [WebGPU Demo](https://huggingface.co/spaces/webml-community/ternary-bonsai-2-webgpu-kernels)
> * [Announcement on X](https://x.com/PrismML/status/2100692248480596348)
