---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-07
hide:
- navigation
tags:
- PyTorch
- Profiler
- 性能优化
- MLP
- Triton
title: PyTorch 性能分析（第二部分）：从 nn.Linear 到融合 MLP
---
### 文章背景与核心概要

本文是“PyTorch 性能分析”系列的第二篇。在前作中，我们探讨了如何解读基础的 Profiler 轨迹，本文则进一步深入，将分析对象从简单的矩阵乘法扩展到深度学习的核心构建模块：`nn.Linear` 层以及包含 GeGLU 激活函数的完整多层感知机（MLP）块。

文章重点分析了 PyTorch 如何通过“算子融合（Fusion）”技术减少 GPU 高带宽内存（HBM）的读写开销。我们对比了 Eager 模式、`torch.compile` 编译模式以及使用 Liger Kernels 手动调优内核在性能表现和调度开销上的差异，旨在帮助开发者理解 GPU 内核调度、算子融合机制以及如何通过工具链实现极致性能。

---

## 系列导航

1. [Profiling in PyTorch (Part 1): A Beginner's Guide to torch.profiler](https://huggingface.co/blog/torch-profiler)
2. **Profiling in PyTorch (Part 2): From nn.Linear to a Fused MLP** *(当前文章)*
3. [Profiling in PyTorch (Part 3): Attention is all you profile](https://huggingface.co/blog/torch-attention-profile)

---

## 引言

在[本系列的第一部分](https://huggingface.co/blog/torch-profiler)中，我们通过 `torch.add(torch.matmul(x, w), b)` 学习了如何解读 PyTorch Profiler 轨迹，探索了 CPU 分发链、启动开销、计算受限与开销受限的区别，以及 `torch.compile` 的内部机制。

在第二篇中，我们将更进一步，用 `nn.Linear` 模块（设置 `bias=True`）替换手动编写的运算。随后，我们将堆叠三个线性层，并结合 GeGLU 激活函数，构建一个完整的多层感知机（MLP）块。

> **注意：** 本文的脚本位于：[`02_linear.py`](https://huggingface.co/datasets/ariG23498/profiling-pytorch/blob/main/02_linear.py)、[`03_simple_mlp.py`](https://huggingface.co/datasets/ariG23498/profiling-pytorch/blob/main/03_simple_mlp.py) 和 [`03_kernels_mlp.py`](https://huggingface.co/datasets/ariG23498/profiling-pytorch/blob/main/03_kernels_mlp.py)。建议在单独的标签页中打开它们以便跟随阅读。所有脚本均在 `NVIDIA A100-SXM4-80GB` GPU 上执行。你可以通过 [Dev Mode with Spaces](https://huggingface.co/docs/hub/spaces-dev-mode) 或 [Hugging Face Jobs pipeline](https://huggingface.co/docs/huggingface_hub/en/guides/jobs) 轻松配置 GPU 环境。

在开始之前，请记住两个核心原则：
1. GPU **内核（Kernel）** 是在多个 GPU 线程上并行运行的程序。
2. CPU **调度并启动**这些内核；大部分观察到的 PyTorch CPU 开销都源于这种调度工作。

---

## 从 `matmul-add` 到 `Linear`

`nn.Linear` 封装了我们在第一部分中分析过的矩阵乘法和加法运算，同时将权重和偏置作为参数进行管理：

```python
# bias=True 模拟了第一部分中的乘法和加法运算
linear_layer = nn.Linear(in_dim, out_dim, bias=True)
y = linear_layer(x)
```

数学表达式为：
$$y = x W^T + b$$

让我们运行 [`02_linear.py`](https://huggingface.co/datasets/ariG23498/profiling-pytorch/blob/main/02_linear.py) 并检查分析结果：

```bash
uv run 02_linear.py --batch 1024 --in_dim 32 --out_dim 64
uvx trace-util -f traces -b <hf_uname>/traces
```

> **提示：** [`trace-util`](https://x.com/ariG23498/status/2054811716727517374) 会将你的轨迹同步到 [Hugging Face 存储桶](https://huggingface.co/storage)，并直接在终端中提供 [Perfetto URL](https://perfetto.dev/)。

| ![PyTorch profiler trace of an `nn.Linear` forward pass](./images/b5420596487b.png) |
| :-----------------------------------------------------------------------------: |
|                     *图 1：`nn.Linear` 的 Profiler 轨迹*                     |

图 1 展示了线性层单次前向传播的 Profiler 轨迹（`wait=1`, `warmup=1`, `active=3`）。

### 转置操作在做什么？

| ![Zoomed in CPU dispatch chain showing aten::t](./images/f0c2f0953287.png) |
| :-----------------------------------------------------------------------: |
|                     *图 2：转置 CPU 行*                     |

放大轨迹（图 2），我们可以看到 `aten::addmm` 之前有一个 `aten::t`（转置）操作，这证实了 `nn.Linear` 在乘法之前会对权重参数进行转置。

关键在于，`aten::t` **不会复制数据**。它只是在 CPU 上更新张量的元数据（形状和步长），不会在 GPU 上启动任何内核。

### 为什么没有单独的 `mul` 和 `add` 内核？

| ![Profiler trace of the linear layer dispatch chain](./images/67dc8a065878.png) |
| :--------------------------------------------------------------------------: |
|               *图 3：线性层分析中没有 `aten::add`*               |

如图 3 所示，分发链中不存在 `aten::add`，因为偏置加法通过**尾声（Epilogue）**被**折叠（Folded）**进了矩阵乘法内核中。

**尾声**是 GEMM（通用矩阵乘法）内核在将结果写回高带宽内存（HBM）之前执行的一小段最终计算。通过直接在内核中执行偏置加法、缩放或激活等操作，我们避免了昂贵的额外 HBM 内存往返。`aten::linear` 分发了 `aten::addmm(bias, x, weight)`，直接映射到带有内置偏置加法的 cuBLAS GEMM 变体。

### `--compile` 对单个线性层有帮助吗？

让我们编译前向调用：

```bash
uv run 02_linear.py --batch 1024 --in_dim 32 --out_dim 64 --compile
uvx trace-util -f traces -b <hf_uname>/traces
```

对比单个 `nn.Linear` 的 Eager 模式和编译模式轨迹，发现它们使用了相同的 cuBLAS GEMM 内核和 `aten::addmm` 操作。由于 Eager 模式下的 `nn.Linear` 已经利用了优化的融合内核（`addmm`），`torch.compile` 对单个孤立层几乎没有进一步优化的空间。

### 转置去哪了？内核布局与预操作

| Eager 分发链 (`aten::t` + `aten::addmm`) | 编译分发链 (直接 `aten::addmm`) |
| :---: | :---: |
| ![图 4](./images/36778d689f3b.png) | ![图 5](./images/5a1045a30951.png) |
| *图 4：Eager 分发链* | *图 5：编译分发链* |

在底层，张量将数据存储为内存中的平铺数组，并通过 `shape`（形状）和 `stride`（步长）进行解释。通过 `M.t()` 进行转置只是交换了步长，而没有复制数据：

```python
>>> M = torch.tensor([[0, 1], [2, 3], [4, 5]])
>>> M.shape, M.stride()
(torch.Size([3, 2]), (2, 1))

>>> T = M.t()
>>> T.shape, T.stride()
(torch.Size([2, 3]), (1, 2))  # 步长已交换，数据未动
```

虽然 Eager 模式会产生 CPU 开销来维护这些视图，但 Inductor 会在编译时预计算步长，从而完全消除了 `aten::t` 的 CPU 开销。

> **提示：** Profiler 轨迹中的 GPU 内核名称（例如 `cutlass_80_wmma_tensorop_bf16_s161616gemm_bf16_32x32_32x1_tn_align8`）通过后缀（如 `tn`，表示转置/非转置）编码了其输入布局。分发器会匹配输入步长以选择正确的预编译内核二进制文件。

---

## 堆叠三个线性层：MLP

接下来，我们将分析一个使用 **GeGLU** 激活变体的多层感知机（MLP），这在现代 Transformer 架构中非常流行。

| ![Conclusions section of the GLU Variants Improve Transformer paper](./images/6c725feb4688.png) |
| :--------------------------------------------------------------------------------------------: |
|               *图 6：[GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202) 的结论* |

```python
class SimpleGeGLUMLP(nn.Module):
    def __init__(self, dim, hidden):
        super().__init__()
        self.gate_proj = nn.Linear(dim, hidden, bias=False)
        self.up_proj = nn.Linear(dim, hidden, bias=False)
        self.down_proj = nn.Linear(hidden, dim, bias=False)

    def forward(self, x):
        g = self.gate_proj(x)
        u = self.up_proj(x)
        h = F.gelu(g, approximate="tanh")
        m = h * u
        y = self.down_proj(m)
        return y
```

执行 [`03_simple_mlp.py`](https://huggingface.co/datasets/ariG23498/profiling-pytorch/blob/main/03_simple_mlp.py)：

```bash
uv run 03_simple_mlp.py --batch 64 --seq 128 --dim 768 --hidden 3072
uvx trace-util -f traces -b <hf_uname>/traces
```

| ![Profiler trace of the GeGLU MLP forward pass](./images/1e053df37894.png) |
| :-----------------------------------------------------------------------: |
|             *图 7：GeGLU MLP 的 Profiler 轨迹*              |

| ![Occupancy Queries in linear projection traces](./images/dacc945f36f2.png) |
| :-------------------------------------------------------------------------: |
|           *图 8：线性投影通道中的占用率查询*          |

在每次前向传播中，GPU 执行 **5 个内核**：三个线性投影、一个 GeLU 激活和一个逐元素乘法。线性层还会执行占用率查询（`cudaOccupancyMaxActiveBlocksPerMultiprocessor`）来确定网格大小（图 8）。

| 操作 | CPU 操作 | GPU 内核 | 启动 |
| :---: | :---: | :---: | :---: |
| `gate_proj` | `aten::linear` | `ampere_bf16_s16816gemm_bf16_128x128_...` | 占用率查询 + `cudaLaunchKernel` |
| `up_proj` | `aten::linear` | `ampere_bf16_s16816gemm_bf16_128x128_...` | 占用率查询 + `cudaLaunchKernel` |
| `gelu` | `aten::gelu` | `vectorized_elementwise_kernel<4, GeluCUDAKernelImpl...>` | `cudaLaunchKernel` |
| `h * u` | `aten::mul` | `vectorized_elementwise_kernel<4, ...MulFunctor...>` | `cudaLaunchKernel` |
| `down_proj` | `aten::linear` | `ampere_bf16_s16816gemm_bf16_128x256_...` | 占用率查询 + `cudaLaunchKernel` |

元数据操作（`aten::t`、`aten::reshape` 等）在 Profiler 表中显示为 `0.000us` 的 CUDA 时间，因为它们不启动任何内核。

### 为什么有两种 GEMM 内核？

虽然所有三个 GEMM 的 FLOP 计数大致相同（每个约 $38.7 \text{ GFLOP}$），但 `down_proj` 的运行速度快了约 $10\%$。由于其输出形状不同（$N=768$ 对比 $3072$），cuBLAS 为该特定形状选择了不同的平铺策略（$128\times 256$ 并带有更深的流水线）。

### `torch.compile` 做了什么？

```bash
uv run 03_simple_mlp.py --batch 64 --seq 128 --dim 768 --hidden 3072 --compile
uvx trace-util -f traces -b <hf_uname>/traces
```

| ![Profiler trace of the compiled GeGLU MLP](./images/409d034facfe.png) |
| :--------------------------------------------------------------------: |
|            *图 10：编译后 MLP 的 Profiler 轨迹*            |

`torch.compile` 剥离了高级 ATen 分发器包装，留下了原始的 `aten::mm` 调用，其内核名称与 Eager 模式完全一致。

### 融合的 Triton 内核

| ![Compiled MLP trace with fused triton kernel](./images/59cc20bb59af.png) |
| :-----------------------------------------------------------------------: |
|                     *图 11：融合的 Triton 内核*                    |

在 Eager 模式下，中间的 `h = gelu(g)` 张量（约 50 MB）由 GeLU 内核写入 HBM，并立即被乘法内核读回。

编译将 GeLU、乘法和 reshape 合并为一个**融合的 Triton 内核**（`triton_poi_fused__unsafe_view_gelu_mul_0`，图 11）。这使得中间值保留在快速的片上寄存器中，消除了通过全局 HBM 的完整往返。

---

## 让我们使用手动调优的内核

或者，我们可以使用 `kernels` 库直接从 [Hugging Face Hub](https://huggingface.co/kernels/kernels-community/liger-kernels) 获取专家调优的 `LigerGEGLUMLP` 内核：

```python
from kernels import get_kernel

kernels_layers = get_kernel("kernels-community/liger-kernels", version=1).layers
kernels_geglu_mlp = kernels_layers.LigerGEGLUMLP(Config()).to(device, dtype=torch.bfloat16).eval()
```

运行 [`03_kernels_mlp.py`](https://huggingface.co/datasets/ariG23498/profiling-pytorch/blob/main/03_kernels_mlp.py)：

```bash
uv run 03_kernels_mlp.py --batch 64 --seq 128 --dim 768 --hidden 3072
uvx trace-util -f traces -b <hf_uname>/traces
```

| ![Profiler trace of the LigerGEGLUMLP forward pass](./images/19f092841a1f.png) |
| :--------------------------------------------------------------------------: |
|               *图 12：`LigerGEGLUMLP` 的 Profiler 轨迹*                |

### 为什么要使用 `kernels` 库？

在本地编译 Triton 或 CUDA 内核通常会因为环境不匹配而失败。[`kernels`](https://github.com/huggingface/kernels) 库下载的是**预构建、版本锁定**的内核包，并缓存在本地（`~/.cache/...kernels-community--liger-kernels`）：
* 在 CI 中跨多种架构编译一次。
* `version=1` 锁定确切构建，防止意外的性能回归。
* 提供即插即用的 `nn.Module` 替代方案（例如 `LigerGEGLUMLP`）。

### 为什么调优内核更好？

| 编译运行预操作 (Dynamo, guards, prologue) | Liger 内核 (零编译开销) |
| :---: | :---: |
| ![图 13](./images/f6400a54995b.png) | ![图 14](./images/c71415729221.png) |
| *图 13：编译运行开销* | *图 14：Liger 内核 (无预操作)* |

1. **内置融合：** `LigerGEGLUMLP` 执行单个优化的 Triton 内核（`_geglu_tanh_forward_kernel`），无需 PyTorch 编译，也不会产生 Dynamo 守卫延迟（图 13 和 14）。
2. **硬件调优参数：** 块大小是根据输入维度专门选择的。

虽然 Inductor 的编译内核对于*静态*形状的运行速度略快（`89.4 µs`）于 Liger（`92.8 µs`），但 `torch.compile` 会针对每个输入形状专门化内核——如果维度发生变化，会触发昂贵的重新编译。Liger 用几微秒的形状特定优化换取了稳健、与形状无关的执行，且没有重新编译开销。

---

## 结论

| 设置 | 变化 | 保持不变 |
| :--- | :--- | :--- |
| **Eager `nn.Linear`** | 基准：偏置加法作为单个 cuBLAS 内核折叠进 GEMM 尾声 (`addmm`)。 | — |
| **Compiled `nn.Linear`** | CPU 分发簿记 (`aten::t`) 消失。 | 相同的单个 cuBLAS GEMM 内核。 |
| **Eager MLP** | 5 个 GPU 内核：3 个 GEMM + GeLU + 乘法。中间值进行完整的 HBM 往返。 | 每个 GEMM 保持为标准 cuBLAS 内核。 |
| **Compiled MLP** | GeLU + 乘法 + reshape 合并为**一个**融合的 Triton 内核。产生编译预操作 (Dynamo/guards)。 | 3 个 GEMM 保持不变。 |
| **Liger MLP** | 通过手写 Triton 内核实现内置融合，**零** Dynamo、守卫或编译延迟。 | 3 个 GEMM 保持为标准 cuBLAS 内核。 |

**性能分析的黄金法则：** *先猜测，再观察。* 在打开轨迹之前，务必先陈述你的预期，并将任何不匹配视为学习的机会。

在下一篇文章中，我们将继续攀登性能分析的阶梯，迈向注意力块和完整模型！

*感谢 [Noe Flandre](https://huggingface.co/NoeFlandre) 和 [Pedro Gabriel Gengo Lourenço](https://huggingface.co/pedrogengo) 的宝贵审阅！*

> **注意：** 本文在 LLM 的协助下进行了润色，以优化非母语英语使用者的语法和措辞，同时保持了完整的技术真实性。🤗