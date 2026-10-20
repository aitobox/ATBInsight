---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-10-21
hide:
- navigation
tags:
- Google
- TorchTPU
- PyTorch
- TPU
- Meta
- 开源后端
title: Google 开源 TorchTPU：面向 Cloud TPU 的原生 PyTorch 后端正式亮相
---
# Google 开源 TorchTPU：面向 Cloud TPU 的原生 PyTorch 后端正式亮相

> # Google Open-Sources TorchTPU, a Native PyTorch Backend for Cloud TPUs

### 文章背景与核心概要

长期以来，在硬件生态中直接以原生体验运行 PyTorch 往往是 NVIDIA GPU 的专属特权，而 Google Cloud TPU 则长期依赖于相对繁琐且存在诸多局限的 PyTorch/XLA 静态图录制方案。在 2026 年 10 月 20 日举行的 PyTorch 开发者大会上，Google 携手 Meta 联合宣布正式开源下一代原生软硬件后端 TorchTPU。TorchTPU 基于 PyTorch 的 PrivateUse1 扩展机制构建，开发者如今仅需一行简短的 `torch.device("tpu")`，即可让 TPU 享受与 GPU、CPU 平起平坐的原生设备级待遇。该后端彻底取代了原有的 PyTorch/XLA，不仅提供开箱即用的即时执行 (Eager Mode) 体验，还通过 `torch.compile` 深度整合了 OpenXLA 编译优化，并在高达 8,192 颗 Ironwood 芯片集群上斩获了 52% 的 MFU 算力利用率，标志着 TPU 深度学习软件生态迈入了全面原生化的崭新纪元。

---

Google 正式开源了面向 Cloud TPU 的原生 PyTorch 后端 [TorchTPU](https://github.com/google-pytorch/torch_tpu)。该项目由 Google 与 Meta 的 PyTorch 团队联合开发，并于 [2026 年 10 月 20 日举行的 PyTorch 开发者大会上正式发布](https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus)。现有的 PyTorch 代码库如今只需简单声明标准设备 `torch.device("tpu")`，即可将 TPU 作为原生设备直接调用，使其在 PyTorch 生态中与 GPU 和 CPU 享受同等的“一等公民”待遇。根据 Google 团队的说明，TorchTPU 已经全面[取代了旧有的 PyTorch/XLA](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu)，成为所有新业务与新工作负载的官方推荐首选。

> Google has open-sourced [TorchTPU](https://github.com/google-pytorch/torch_tpu), a native PyTorch backend for Cloud TPUs. Co-developed with the PyTorch team at Meta, it was [announced at PyTorch Conference 2026 on October 20, 2026](https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus). Existing PyTorch code can now target a TPU simply through a standard `torch.device("tpu")`, placing TPUs right beside GPUs and CPUs as a native PyTorch device. According to the Google team, TorchTPU [replaces PyTorch/XLA](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu) and is now recommended for all new workloads.

---

## 📌 执行摘要

> ## 📌 Executive Summary

* **核心定位**：一套完备的原生软件技术栈（基于 Apache 2.0 协议开源，支持 Python 3.11+，当前 PyPI 发布版本为 `v0.2.0`），涵盖 4 个开源代码仓库：`TorchTPU`、`vLLM-TorchTPU`、`SGLang-TorchTPU` 以及 `TorchTitan`。
* **硬件支持范围**：面向 Google Cloud TPU 硬件平台，已在 [v5e 及后续各代硬件](https://arxiv.org/abs/2610.24161) 上完成充分验证，最大可水平扩展至 8,192 颗 Ironwood (TPU7x) 芯片，并为 FP8、MXFP4 和 NVFP4 量化权重提供推理部署支持。
* **性能特性**：提供用于直观调试的即时执行模式 (Eager Mode)，以及用于支撑工业级吞吐量的 `torch.compile` 编译加速模式。
* **亮点与权衡**：在 Ironwood 集群上使用 TorchTitan 训练 Qwen 3 8B 模型时，实现了高达 52% 的模型浮点运算利用率 (Model FLOPs Utilization, MFU)；但在未经任何优化的纯 Eager 模式下初始执行较慢（例如调优前单步耗时 11.49 秒，而经过完整编译调优后仅需 2.78 秒）。

> * **What it is:** A native software stack (Apache 2.0, Python 3.11+, currently `v0.2.0` on PyPI) spanning 4 open repositories: `TorchTPU`, `vLLM-TorchTPU`, `SGLang-TorchTPU`, and `TorchTitan`.
> * **Hardware Support:** Google Cloud TPUs, tested from [generation v5e onwards](https://arxiv.org/abs/2610.24161), scaling up to 8,192 Ironwood (TPU7x) chips with serving support for FP8, MXFP4, and NVFP4 checkpoints.
> * **Performance Profile:** Offers Eager mode for straightforward debugging and `torch.compile` for production-level throughput.
> * **Highlights & Trade-offs:** Achieved up to 52% Model Flops Utilization (MFU) training Qwen 3 8B using TorchTitan on Ironwood. Conversely, out-of-the-box eager execution can be slower initially (e.g., 11.49s per step un-tuned vs. 2.78s fully tuned).

---

## 什么是 TorchTPU？

> ## What is TorchTPU?

TorchTPU 是一款专为在 TPU 硬件上原生运行 PyTorch 模型而设计的开源后端。它通过 PyTorch 官方规范的 [PrivateUse1 扩展接口](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/) 实现了无缝接入。

> TorchTPU is an open-source PyTorch backend designed to run PyTorch models natively on TPUs. It integrates seamlessly via PyTorch’s [PrivateUse1 interface](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/). 

* **原生张量 (Native Tensors)**：张量即为标准的 PyTorch 原生对象，完全不需要任何自定义子类或额外的封装壳。
* **状态保真 (State Preservation)**：采用单设备单进程模型运行，同时完美保留了张量视图 (Tensor Views) 与就地修改 (In-place Mutation) 语义。

> * **Native Tensors:** Tensors are ordinary PyTorch objects without custom subclasses or wrappers.
> * **State Preservation:** It operates on a one-process-per-device model while preserving tensor views and in-place mutations.

相比之下，其前身 **PyTorch/XLA** 依赖于惰性张量 (Lazy Tensor) 图录制机制，强制要求开发者手动标注可编译的计算区域，且[仅支持纯单程序多数据 (SPMD) 模式](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/)；而 TorchTPU 则原生支持具有分支分支分歧的多程序多数据 (MPMD) 执行范式。

> Unlike its predecessor, **PyTorch/XLA**—which relied on lazy-tensor graph recording, forced developers to manually mark compilable regions, and [only supported pure SPMD code](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/)—TorchTPU natively supports divergent MPMD execution as well.

---

## TorchTPU 如何执行 PyTorch 代码？

> ## How Does TorchTPU Execute PyTorch Code?

TorchTPU 提供了[三种即时执行模式 (Eager Execution Modes)](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu)：

> TorchTPU provides [three eager execution modes](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu):

1. **严格模式 (Strict，默认)**：在严格遵循标准 PyTorch 语义的同时，对每个算子进行异步分派；
2. **调试模式 (Debug)**：采用同步阻塞执行，并内置张量边界与越界检查；
3. **延迟融合模式 (DeferAndFuse)**：将连续执行的 Eager 算子自动融合，以最大程度减少高带宽内存 (High Bandwidth Memory, HBM) 的数据搬运。根据 [TorchTPU 论文](https://arxiv.org/abs/2610.24161) 数据，该模式相比默认严格模式可带来 50% 甚至更高的性能提升。

> 1. **Strict (Default):** Dispatches each operator asynchronously while adhering to standard PyTorch semantics.
> 2. **Debug:** Runs synchronously and includes built-in tensor bounds checking.
> 3. **DeferAndFuse:** Fuses consecutive eager operators to minimize High Bandwidth Memory (HBM) traffic. According to the [TorchTPU paper](https://arxiv.org/abs/2610.24161), this can yield performance boosts of 50% or more over Strict mode.

### 图编译与自定义算子内核

> ### Compilation and Custom Kernels

为了获取极致计算性能，`torch.compile(backend="tpu")` 通过 TorchDynamo 捕获计算图，并将其逐层降级至 StableHLO 与 OpenXLA，从而生成高度优化的 TPU 机器码指令。这些编译出的可执行制品会在进程、主机甚至作业重启之间进行智能缓存。

> For peak performance, `torch.compile(backend="tpu")` uses TorchDynamo to capture graphs, lowering them through StableHLO to OpenXLA to generate optimized TPU machine code. These compiled executables are intelligently cached across processes, hosts, and job restarts.

此外，开发者还可以深度使用以下高级特性：

> Additionally, developers can utilize:

* **自定义 Pallas 内核**：可直接作为标准 PyTorch 函数进行调用；
* **预构建算子内核**：深度集成了 [Tokamax](https://github.com/openxla/tokamax) 与 [Helion](https://pytorch.org/blog/helion-on-tpu-towards-hardware-heterogeneous-kernel-authoring/) 分块内核；
* **分布式训练**：通过专用的 `tpu_dist` 进程组进行管理，全面支持 DDP、FSDP2、DTensor 以及拓扑感知 Mesh 架构。

> * **Custom Pallas Kernels:** Callable directly as standard PyTorch functions.
> * **Prebuilt Kernels:** Integration with [Tokamax](https://github.com/openxla/tokamax) and [Helion](https://pytorch.org/blog/helion-on-tpu-towards-hardware-heterogeneous-kernel-authoring/) tile kernels.
> * **Distributed Training:** Managed via the `tpu_dist` process group, supporting DDP, FSDP2, DTensor, and topology-aware meshes.

---

## 性能实测指标

> ## Performance Metrics

*(注：以下所有性能数据均由 Google 及其合作伙伴官方测试提供。)*

> *(Note: All figures are self-reported by Google and its partners.)*

* **超大训练规模**：TorchTitan 在训练 Qwen 3 8B 模型时实现了高达 [52% 的 MFU 算力利用率](https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus)，并在扩展至 8,192 颗 Ironwood TPU 芯片时展现出近乎线性的扩展性能。
* **逐级优化收益**：在典型的 TorchTitan 微调任务中，单步执行时间从 11.49 秒大幅压缩至 2.78 秒：
  * *仅开启 DeferAndFuse*：获得 `1.15x` 的加速；
  * *开启完整 `torch.compile`*：获得 `3.80x` 的加速（[数据来源](https://arxiv.org/abs/2610.24161)）。
* **广泛模型覆盖**：Google 持续针对约 5,000 个 Hugging Face 模型在 Eager 模式与编译模式下进行全面的自动化回归验证。
* **生产集群推理**：Zenteiq 利用 GKE 上的 `llm-d` 路由搭配 TorchTPU，在每 1,000 颗 TPU v6e 芯片上的日均 Token 输出量从 14.7 亿大幅攀升至 59.7 亿。

> * **Training Scale:** TorchTitan achieved up to [52% MFU on Qwen 3 8B](https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus), showing near-linear scaling up to 8,192 Ironwood TPUs.
> * **Optimization Progression:** In a sample TorchTitan fine-tuning task, step time dropped significantly from 11.49s to 2.78s:
>   * *DeferAndFuse alone:* `1.15x` speedup
>   * *Full `torch.compile`:* `3.80x` speedup ([Source](https://arxiv.org/abs/2610.24161))
> * **Model Coverage:** Google continuously validates roughly 5,000 Hugging Face models across both eager and compiled modes.
> * **Fleet Serving:** Zenteiq scaled daily outputs from 1.47B to 5.97B tokens per 1,000 TPU v6e chips, largely driven by `llm-d` routing on GKE alongside TorchTPU.

---

## 软件生态无缝整合

> ## Ecosystem Integrations

TorchTPU 出厂即做好了与现代主流机器学习工具链无缝协同的准备：

> TorchTPU comes ready to integrate with standard machine learning tooling:

* **Hugging Face**：Transformers v5 通过 `device_map="tpu"` 直接支持 TPU 部署；Diffusers 则全面支持 Eager 模式、`torch.compile` 以及张量并行 (Tensor Parallelism)。
* **[vLLM-TorchTPU](https://github.com/vllm-project/vllm-torchtpu)**：基于 Inferact 构建，在完整保留上游调度器与 API 服务端架构的同时，深度融入了定制的 Pallas 算子内核。
* **[SGLang-TorchTPU](https://github.com/sgl-project/sglang-torchtpu)**：基于 RadixArk 构建，完整保留了 RadixAttention 前缀缓存复用能力。
* **前沿推理特性**：全面支持 FP8 KV Cache、低比特量化检查点 (FP8, MXFP4, NVFP4) 以及投机解码 (MTP, EAGLE-3)。
* **[TorchTitan](https://github.com/google-pytorch/torchtitan)**：提供针对 Llama 3 (70B/405B)、Qwen 3 (8B/32B/235B MoE) 以及 FLUX.1 (12B) 的开箱即用训练配方。
* **更多框架支持**：支持 llm-d 1.0、Ray、TorchRec、[VeRL (预览版)](https://github.com/verl-project/verl/tree/main/examples/tpu/grpo) 以及面向端侧导出的 [LiteRT-Torch](https://github.com/google-ai-edge/litert-torch)。

> * **Hugging Face:** Transformers v5 supports direct TPU deployment via `device_map="tpu"`, while Diffusers fully supports eager execution, `torch.compile`, and tensor parallelism.
> * **[vLLM-TorchTPU](https://github.com/vllm-project/vllm-torchtpu):** Built with Inferact to preserve upstream schedulers and API servers while incorporating custom Pallas kernels.
> * **[SGLang-TorchTPU](https://github.com/sgl-project/sglang-torchtpu):** Built with RadixArk, retaining RadixAttention prefix-reuse capabilities.
> * **Advanced Serving Features:** Includes support for FP8 KV caches, quantization checkpoints (FP8, MXFP4, NVFP4), and speculative decoding (MTP, EAGLE-3).
> * **[TorchTitan](https://github.com/google-pytorch/torchtitan):** Ready-to-use recipes for Llama 3 (70B/405B), Qwen 3 (8B/32B/235B MoE), and FLUX.1 (12B).
> * **Additional Frameworks:** Supports llm-d 1.0, Ray, TorchRec, [VeRL (preview)](https://github.com/verl-project/verl/tree/main/examples/tpu/grpo), and [LiteRT-Torch](https://github.com/google-ai-edge/litert-torch) for on-device exports.

---

## 核心技术架构横向对比

> ## Technical Comparison

| 特性维度 | **TorchTPU** ([代码库](https://github.com/google-pytorch/torch_tpu)) | **PyTorch/XLA** ([代码库](https://github.com/pytorch/xla)) | **TorchNeuron** ([AWS 文档](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/torch/index.html)) | **TPU 上的 JAX** ([Google 文档](https://docs.cloud.google.com/tpu/docs/jax-ai-stack)) |
| :--- | :--- | :--- | :--- | :--- |
| **研发厂商** | Google + Meta | Google / PyTorch | AWS | Google |
| **硬件平台** | Cloud TPU (v5e 及更新代际) | Cloud TPU | Trainium 2, Trainium 3 | Cloud TPU |
| **PyTorch 设备名** | `tpu` | `xla` | `neuron` | *非 PyTorch 生态* |
| **后端机制** | PrivateUse1 | 惰性张量计算图录制 | PrivateUse1 | 不适用 |
| **默认执行范式** | 即时执行 (Strict, Debug, DeferAndFuse) | 惰性张量模式 | 即时执行 + `torch.compile` | 不适用 |
| **编译优化路径** | TorchDynamo $\rightarrow$ StableHLO $\rightarrow$ XLA | XLA | Neuron Compiler | [XLA](https://en.wikipedia.org/wiki/Accelerated_Linear_Algebra) |
| **分布式 API** | DDP, FSDP2, DTensor, SPMD, MPMD | [仅支持纯 SPMD 模式](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/) | FSDP, DTensor, DDP, TP | 不适用 |
| **自定义算子** | Pallas, Tokamax, Helion | 未公开 | NKI | Pallas |
| **vLLM / SGLang 推理服务** | vLLM-TorchTPU, SGLang-TorchTPU | 未公开 | vLLM Neuron | [vLLM-JAX, SGLang-JAX](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu) |
| **发展状态** | 开源 (`v0.2.0`) | 正被 TorchTPU 全面取代 | 公开测试阶段 (Neuron 2.33) | 持续维护中 |
| **开源协议** | Apache 2.0 | 未公开 | 未公开 | 未公开 |

> | Feature | **TorchTPU** ([Repo](https://github.com/google-pytorch/torch_tpu)) | **PyTorch/XLA** ([Repo](https://github.com/pytorch/xla)) | **TorchNeuron** ([AWS Docs](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/torch/index.html)) | **JAX on TPU** ([Google Docs](https://docs.cloud.google.com/tpu/docs/jax-ai-stack)) |
> | :--- | :--- | :--- | :--- | :--- |
> | **Vendor** | Google + Meta | Google / PyTorch | AWS | Google |
> | **Hardware** | Cloud TPU (v5e and later) | Cloud TPU | Trainium 2, Trainium 3 | Cloud TPU |
> | **PyTorch Device** | `tpu` | `xla` | `neuron` | *Not PyTorch* |
> | **Backend Mechanism** | PrivateUse1 | Lazy-tensor graph recording | PrivateUse1 | N/A |
> | **Default Execution** | Eager (Strict, Debug, DeferAndFuse) | Lazy tensors | Eager + `torch.compile` | N/A |
> | **Compile Path** | TorchDynamo $\rightarrow$ StableHLO $\rightarrow$ XLA | XLA | Neuron Compiler | [XLA](https://en.wikipedia.org/wiki/Accelerated_Linear_Algebra) |
> | **Distributed APIs** | DDP, FSDP2, DTensor, SPMD, MPMD | [Pure SPMD only](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/) | FSDP, DTensor, DDP, TP | N/A |
> | **Custom Kernels** | Pallas, Tokamax, Helion | Not disclosed | NKI | Pallas |
> | **vLLM / SGLang Serving** | vLLM-TorchTPU, SGLang-TorchTPU | Not disclosed | vLLM Neuron | [vLLM-JAX, SGLang-JAX](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu) |
> | **Status** | Open source (`v0.2.0`) | Being replaced by TorchTPU | Public beta (Neuron 2.33) | Maintained |
> | **License** | Apache 2.0 | Not disclosed | Not disclosed | Not disclosed |

---

## 如何安装与快速上手 TorchTPU

> ## How to Install TorchTPU

在你的 TPU 虚拟机环境上安装该软件包，并使用标准 PyTorch 语法直接初始化 `tpu` 设备：

> Install the package on your TPU VM and initialize the `tpu` device using standard PyTorch syntax:

```python
# pip install torch_tpu
import torch

device = torch.device("tpu")
x = torch.randn((4, 4), device=device)
```

> 💡 **安装实用贴士**：[官方仓库 README](https://github.com/google-pytorch/torch_tpu) 将 `torch_tpu==0.2.0` 与 CPU 版 PyTorch Wheel 索引源进行了固定。如果不显式指定该源，`pip` 可能会误拉取 CUDA 版本的 `torch` 构建包。完整的环境配置指引可参阅 [torchtpu.readthedocs.io](https://torchtpu.readthedocs.io/)。

> 💡 **Installation Tip:** The [repository README](https://github.com/google-pytorch/torch_tpu) pins `torch_tpu==0.2.0` alongside the CPU PyTorch wheel index. Without specifying this index, `pip` may pull the CUDA build of `torch` instead. Full setup guides are available at [torchtpu.readthedocs.io](https://torchtpu.readthedocs.io/).

---

## 核心要点总结

> ## Key Takeaways

* TorchTPU 在 Apache 2.0 开源协议下发布，由 Google 与 Meta 深度联合打造；
* 它正式废弃并取代了旧有的 PyTorch/XLA，全面拥抱以 Eager 为先、基于 PrivateUse1 的现代执行流水线；
* `torch.compile(backend="tpu")` 通过 StableHLO 与 XLA 编译器将模型图原生编译为高效机器码；
* 经过实战检验的高扩展性：TorchTitan 在 Qwen 3 8B 模型上实现了 52% 的 MFU 算力利用率，并在 8,192 颗 Ironwood 芯片集群上实现高效线性扩展；
* vLLM、SGLang、Hugging Face 等主流推理生态现均可通过标准原生 PyTorch API 无缝运行于 TPU 之上。

> * TorchTPU is open-sourced under the Apache 2.0 license, jointly built with Meta.
> * It deprecates and replaces PyTorch/XLA in favor of a modern, eager-first, PrivateUse1-based execution pipeline.
> * `torch.compile(backend="tpu")` translates model graphs natively via StableHLO and XLA.
> * Proven scalability: TorchTitan achieved 52% MFU on Qwen 3 8B while scaling effectively across 8,192 Ironwood chips.
> * Major serving ecosystems like vLLM, SGLang, and Hugging Face now run on TPUs using idiomatic PyTorch APIs.

---

### 相关资源与项目链接

> ### Resources & Links

* [GitHub 代码仓库](https://github.com/google-pytorch/torch_tpu)
* [学术研究论文](https://arxiv.org/abs/2610.24161)
* [官方技术文档](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu)
* [Google Cloud 官方发布公告](https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus)

> * [GitHub Repository](https://github.com/google-pytorch/torch_tpu)
> * [Research Paper](https://arxiv.org/abs/2610.24161)
> * [Official Documentation](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu)
> * [Google Cloud Announcement](https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus)

*(版权归原研发团队所有。本文内容最初由 [MarkTechPost](https://www.marktechpost.com/2026/10/20/google-torchtpu-open-source-native-pytorch-tpu/) 报道。)*

> *(All credit belongs to the original research and development teams. Originally reported by [MarkTechPost](https://www.marktechpost.com/2026/10/20/google-torchtpu-open-source-native-pytorch-tpu/).)*
