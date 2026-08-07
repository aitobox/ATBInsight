---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-07
hide:
- navigation
tags:
- PyTorch
- 性能优化
- Profiler
- 深度学习
- 机器学习
title: PyTorch 性能剖析（第一篇）：`torch.profiler` 新手入门指南
---
### 文章背景与核心概要
性能剖析（Profiling）是优化深度学习流水线的核心技能，无论是为了最大化大语言模型（LLM）的每秒生成 Token 数，还是为了排查训练循环缓慢的原因。然而，初学者在面对密集的视觉痕迹和复杂的事件名称时，往往会感到无从下手。

本文是**《PyTorch 性能剖析》**系列的第一篇，旨在揭开 `torch.profiler` 的神秘面纱。文章手把手演示了如何配置剖析器、阅读统计表格、解读 Perfetto 追踪时间线（CPU 与 GPU 通道）、追踪操作分派（Dispatch），并分析 `torch.compile` 带来的影响。通过一个简单的矩阵乘加示例，读者将建立起分析并定位计算瓶颈的直观心智模型。

---

> *"无法剖析，就无法优化。"*

这是**《PyTorch 性能剖析》**系列文章的开篇，在该系列中我们将逐步培养阅读剖析追踪图（Profiler Traces）的技能，从而驱动性能优化：
1. **PyTorch 性能剖析（第一篇）：`torch.profiler` 新手入门指南** *(当前文章)*
2. [PyTorch 性能剖析（第二篇）：从 nn.Linear 到融合 MLP (Fused MLP)](https://huggingface.co/blog/torch-mlp-fusion)
3. [PyTorch 性能剖析（第三篇）：注意力机制（Attention）全景剖析](https://huggingface.co/blog/torch-attention-profile)

---

## 引言 (Introduction)

我们从初学者的角度出发，以极低的门槛切入性能剖析。读完本指南后，你将理解：
* 如何配置 `torch.profiler` 并解释其输出结果。
* 如何阅读统计表格和追踪时间线（CPU 通道、GPU 通道以及空闲间隙）。
* 从 Python 调用一直到 CUDA Kernel 的事件链。
* 在应用 `torch.compile` 时发生了什么改变（以及什么保持不变）。

### 核心术语 (Key Terminology)
1. **GPU Kernel：** 在 GPU 的多个线程上并行执行的程序。
2. **调度器 (Scheduler)：** 负责调度和启动这些 Kernel 的 CPU 组件。

> **完整脚本：** 你可以参考本文使用的完整脚本：[`01_matmul_add.py`](https://huggingface.co/datasets/ariG23498/profiling-pytorch/blob/main/01_matmul_add.py)。我们推荐通过 Hugging Face 基础设施（例如 [Dev Mode with Spaces](https://huggingface.co/docs/hub/spaces-dev-mode) 或 [Hugging Face Jobs 管道](https://huggingface.co/docs/huggingface_hub/en/guides/jobs)）在 `NVIDIA A100-SXM4-80GB` GPU 上对其进行实验。

![博客文章缩略图](./images/4c7679cefcfa.png)

---

## 矩阵乘法与加法运算 (The Matrix Multiplication and Addition Operation)

深度神经网络主要由矩阵乘法构成。我们的剖析之旅从一个模拟神经网络神经元的简单示例开始，它结合了矩阵乘法和加法：

```python
def fn(x, w, b):
  return torch.add(torch.matmul(x, w), b)
```

### 剖析代码的步骤 (Steps to Profile Your Code)

1. **准备目标函数**（如上方的 `fn`）。
2. **使用 <code>record_function</code> 注解算法**，以便在追踪可视化工具中更轻松地定位：
   ```python
   def step():
     with torch.profiler.record_function("matmul_add"):
       return fn(x, w, b)
   ```
3. **将执行过程包裹**在 <code>torch.profiler.profile</code> 上下文管理器中：
   ```python
     with torch.profiler.profile(
       activities=[
           torch.profiler.ProfilerActivity.CPU,  # CPU 活动
           torch.profiler.ProfilerActivity.CUDA, # GPU 活动
       ],
     ) as prof:
       # 运行多次以预热 GPU
       for _ in range(5):
         step()
         prof.step()
   ```
4. **导出结果：**
   ```python
   # 剖析器表格摘要
   prof.key_averages().table(sort_by="cuda_time_total", row_limit=15)

   # 用于可视化工具的剖析器追踪文件
   prof.export_chrome_trace(trace_path)
   ```

剖析器会生成两个截然不同的产物：
* **剖析器表格 (Profiler Table)：** 一个统计摘要，回答“什么占用了最多时间？”以发现瓶颈。
* **剖析器追踪 (Profiler Trace)：** 一个时间维度的执行视图，回答“操作是在什么时候、为什么发生的？”，捕捉 CPU-GPU 重叠、启动延迟以及启动的 Kernel。

---

### 分析小矩阵 (64x64) (Analyzing Small Matrices (64x64))

在 GPU 机器上运行脚本：
```bash
uv run 01_matmul_add.py --size 64
```

| ![针对 64 尺寸矩阵的 matmul add 剖析表格](./images/2851d781f42b.png) |
| :---: |
| 图 1：针对 64 尺寸矩阵的 matmul add 剖析表格 |

统计摘要显示：
```bash
Self CPU time total: 2.314ms
Self CUDA time total: 23.104us
```

GPU 执行 Kernel（`ampere_bf16_s16816gemm...`）的时间不到 CPU 执行时间的 1%。GPU 大多处于空闲状态——这是**开销受限型 (overhead-bound)** 工作负载的典型特征，因为启动 Kernel 的开销远超实际计算。

---

### 放大矩阵规模 (4096x4096) (Scaling Up Matrices (4096x4096))

为了脱离开销受限的区间，我们增大矩阵尺寸：
```bash
uv run 01_matmul_add.py --size 4096 
```

| ![针对 4096 尺寸矩阵的 matmul add 算法剖析表格](./images/cdbfa221c37d.png) |
| :---: |
| 图 2：针对 4096 尺寸矩阵的 matmul add 剖析表格 |

执行摘要更新为：
```bash
Self CPU time total: 4.908ms
Self CUDA time total: 4.495ms
```

两个指标现在都在毫秒级别，这证实了工作负载已从开销受限转变为**计算受限型 (compute-bound)**。

---

## 检查追踪数据 (Examining the Traces)

可以将追踪文件上传到 [Perfetto UI](https://ui.perfetto.dev) 进行交互式查看。

### 64x64 默认追踪 (64x64 Default Trace)

| ![针对 64 尺寸矩阵的 matmul 和 add 剖析追踪](./images/6845053179bd.png) |
| :---: |
| 图 3：针对 64 尺寸矩阵的 matmul 和 add 剖析追踪 |

该追踪显示了清晰的 CPU 和 GPU 通道。条形宽度代表事件持续时间，垂直嵌套代表调用层级，空白区域代表空闲时间。

| ![PyTorch 剖析器追踪的 CPU 和 GPU 通道](./images/b284e23d6a7f.png) |
| :---: |
| 图 4：PyTorch 剖析器追踪的 CPU 和 GPU 通道 |

#### 为什么 `ProfilerStep#2` 耗时更长？

| ![ProfileStep#2 明显比后续的步骤更宽](./images/2e6b14bf2474.png) |
| :---: |
| 图 5：`ProfileStep#2` 明显比随后的步骤更宽 |

在进入 `record_function("matmul_add")` 和执行 `aten::matmul` 之间，第 2 步经历了一个约 228 µs 的“死窗口 (dead window)”。这是由工作区分配、cuBLAS 启发式算法和惰性模块加载（lazy module loading）引起的。

| ![record_function("matmul_add") 与 aten::matmul 之间的约 228 µs 死窗口](./images/575e16be829b.png) |
| :---: |
| 图 6：`record_function("matmul_add")` 与 `aten::matmul` 之间的约 228 µs 死窗口 |

为了避免这些冷启动工件的干扰，我们使用预热阶段：
```bash
uv run 01_matmul_add.py --warmup
```
*(Perfetto 追踪链接：[带预热的 64x64 Perfetto 追踪](https://ui.perfetto.dev/#!/?url=https://huggingface.co/buckets/ariG23498/traces/resolve/01_matmul_add/64_bf16_warm_eager.json))*

| ![预热后，每个剖析步骤耗时相近](./images/541421f5d580.png) |
| :---: |
| 图 7：预热后，每个剖析步骤耗时相近 |

#### 为什么 CPU 通道和 GPU 通道之间存在偏移？

| ![CPU 和 GPU 通道之间约 2.5 ms 的偏移](./images/a4350641cf25.png) |
| :---: |
| 图 8：CPU 和 GPU 通道之间约 2.5 ms 的偏移 |

在 CPU 上提交 Kernel 与其在 GPU 上执行之间，出现了大约 2.5 ms 的偏移。调整调度器配置：
```diff
- schedule = torch.profiler.schedule(wait=1, warmup=1, active=3, repeat=1)
+ schedule = torch.profiler.schedule(wait=0, warmup=0, active=3, repeat=1)
```
这会在 GPU 通道上揭示一个 `Activity Buffer Request`，表明在执行期间有 GPU VRAM 的内存分配请求。

| ![当 wait=0 且 warmup=0 时，追踪揭示了一个 Activity Buffer Request](./images/60ff5638591e.png) |
| :---: |
| 图 9：当 `wait=0` 且 `warmup=0` 时，追踪揭示了一个 `Activity Buffer Request` |

| ![在剖析步骤 1 中，matmul 和 add Kernel 之间出现了间隙](./images/7d772501efda.png) |
| :---: |
| 图 10：在剖析步骤 1 中，matmul 和 add Kernel 之间出现了间隙 |

---

### 分派链 (The Dispatch Chain)

| ![分派链](./images/4d353ca4638d.png) |
| :---: |
| 图 11：分派链 |

PyTorch 操作通过结构化层级执行：
1. `ProfileStep#<id>`
2. 自定义注解 (`matmul_add`)
3. ATen 级分派 (`aten::matmul`, `aten::mm`, `aten::add`)

当修改输入以包含批次维度（batch dimension）时：
```diff
- x = torch.randn(args.size, args.size, device=device, dtype=dtype)
+ x = torch.randn(8, args.size, args.size, device=device, dtype=dtype)
```
分派器将 `aten::matmul` 映射到 `aten::bmm`（批次矩阵乘法），并伴随 CUDA 运行时调用。

| ![批次矩阵乘法 (Batched Matrix Multiplication)](./images/2d04ee5c0dec.png) |
| :---: |
| 图 12：批次矩阵乘法 |

---

### 为什么 `matmul` 具有 CUDA 占用率查询 (CUDA Occupancy Query)？

| ![在 matmul Kernel 启动之前触发了一个 CUDA 占用率查询](./images/772827452b0a.png) |
| :---: |
| 图 13：在 matmul Kernel 启动之前触发了一个 CUDA 占用率查询 |

`aten::mm` 在启动 Kernel 之前会触发规划调用（`cudaOccupancyMaxActiveBlocksPerMultiprocessor`），而 `aten::add` 则不会。

| ![Matmul 内存占用](./images/1e03bdc762a1.png) | ![Add 内存占用](./images/601540d67c5b.png) |
| :---: | :---: |
| 图 14：Matmul 内存占用 | 图 15：Add 内存占用 |

矩阵乘法根据矩阵维度和硬件容量使用动态寄存器和共享内存，因此需要占用率启发式算法。相比之下，诸如加法之类的逐元素（elementwise）操作具有固定且轻量的占用。

---

### 4096x4096 追踪与 Kernel 运行时方差 (4096x4096 Traces and Kernel Runtime Variance)

使用更大的矩阵尺寸运行脚本：
```bash
uv run 01_matmul_add.py --size 4096 --warmup
```

| ![4096x4096 bf16 matmul Kernel 计时在同一 GPU 的不同剖析步骤中有所不同](./images/d444dd3bd71c.png) |
| :---: |
| 图 16：尽管输入完全相同，但其中一个 matmul Kernel 的运行时间比其他步骤更长 |

由于 GPU 时钟加速（clock boosting）、热限制、电源管理策略以及驱动程序任务，Kernel 的运行时间并非绝对恒定。仅看平均值可能会掩盖这些波动。

---

## 让我们看看 `torch.compile` 的实际效果 (Let's See `torch.compile` at Work)

使用 `TorchInductor` 测试编译：
```bash
uv run 01_matmul_add.py --size 4096 --warmup --compile
```

```python
def fn(x, w, b):
  return torch.add(torch.matmul(x, w), b)

fn = torch.compile(fn) if args.compile else fn
```

| ![PyTorch 剖析器追踪中高亮的 torch.compile 区域，显示了 TorchDynamo 和 Inductor 帧](./images/1bed8baa04ed.png) |
| :---: |
| 图 17：编译后的区域在追踪中显示为 TorchDynamo 和 Inductor 帧 |

### 算子融合与分派重写 (Operator Fusion vs. Dispatch Rewriting)

| ![编译运行分派了单个 aten::addmm](./images/3cafb2a12da1.png) |
| :---: |
| 图 18：编译运行分派了单个 `aten::addmm` |

`TorchInductor` 将 `torch.add(torch.matmul(x, w), b)` 重写为单次 `aten::addmm(b, x, w)` 调用。然而，这是**分派器级别的融合 (dispatcher-level fusion)**，而非底层 Kernel 级别的融合。底层 GPU Kernel 的执行仍然是标准的 cuBLAS GEMM。

### `torch.compile` 的运行时架构 (Runtime Architecture of `torch.compile`)
* **TorchDynamo 缓存查找：** 每次调用时验证形状、数据类型、设备和元数据的兼容性。
* **Torch 编译区域：** 执行编译后的块。
* **AOTDispatcher 运行时包装器：** 管理元数据和张量视图。
* **`## Call CompiledFxGraph`：** 运行通过内容哈希映射生成的代码。

### 编译模式下的 Kernel 启动 (Kernel Launches in Compiled Mode)

| ![编译后的 matmul 追踪显示每步启动了 Memcpy DtoD 和 GEMM Kernel](./images/d8de3c2c3eb0.png) |
| :---: |
| 图 19：每个编译步骤仍然启动了两个 GPU Kernel：设备到设备内存拷贝（Device-to-Device memcpy）和 GEMM |

Inductor 生成的代码执行：
1. `out = copy(C)`（设备到设备内存拷贝）
2. `out = α·(A·B) + β·out`（将偏置加法融合进回写的 GEMM）

---

## 追踪阅读小抄 (Trace Reading Cheatsheet)

### 剖析器表格 (Profiler Table)

| 你看到了什么 | 它通常意味着什么 |
| :--- | :--- |
| `Self CPU time total` ≫ `Self CUDA time total` | 开销受限。分派耗时比计算更长。增大尺寸或融合操作。 |
| `Self CPU time total` ≈ `Self CUDA time total` | 计算受限。GPU 是瓶颈（对重负载而言是理想状态）。 |
| 一个事件主导了 `CUDA total` | 主要性能热点。首先在这里进行优化。 |
| 高 `# of Calls` | 潜在的优化目标。检查是否存在融合或批处理的机会。 |
| `CPU total` ≫ `Self CPU` | 子事件开销高。应深入嵌套事件而非父事件。 |

### CPU 通道 (CPU Lane)

| 你看到了什么 | It usually means |
| :--- | :--- |
| 第一个 `ProfileStep` 比后续步骤更宽 | 冷启动开销（工作区分配、cuBLAS 启发式算法）。请使用预热配置。 |
| 第一个 `aten::*` 之前存在大的间隙 | 冷启动分派延迟。 |
| 启动前出现 `cudaOccupancyMaxActiveBlocksPerMultiprocessor` | 重负载 Kernel（GEMM、卷积）正在查询 SM 配置。 |
| `cudaLaunchKernel` 没有伴随占用率查询 | 轻量级逐元素或归约 Kernel。 |
| 活动窗口末尾出现较长的 `cudaDeviceSynchronize` | 剖析器正在清空（flushing）事件。如果关联的是微小的工作，则表明 GPU 利用率低。 |
| 意外的 `cudaMemcpyAsync` | 隐藏的设备间拷贝，例如在 `addmm` 后记（epilogues）期间的偏置拷贝。 |

### GPU 通道 (GPU Lane)

| 你看到了什么 | 它通常意味着什么 |
| :--- | :--- |
| `Activity Buffer Request` | 剖析器正在分配/填充事件缓冲区。 |
| 跨步骤的 Kernel 运行时方差 | GPU 时钟降频（throttling）、热限制或电源管理状态。 |
| GEMM 之前的 `Memcpy DtoD` | `addmm` 后记的偏置拷贝设置。 |

### 分派链 (Dispatch Chain)

| 你看到了什么 | 它通常意味着什么 |
| :--- | :--- |
| `aten::matmul` 解析为 `aten::mm` | 标准二维 × 二维矩阵乘法。 |
| `aten::matmul` 解析为 `aten::bmm` | 三维及以上张量上的批次矩阵乘法。 |
| `aten::addmm(b, x, w)` | 分派器级别的算子融合。 |

### `torch.compile`

| 你看到了什么 | 它通常意味着什么 |
| :--- | :--- |
| 每次调用都有 `TorchDynamo Cache Lookup` | 每次调用都要支付的缓存验证成本。 |
| 编译下每步 CPU 时间更高 | 对于小操作，Dynamo/AOTAutograd/Inductor 栈带来的预期开销。 |

---

## 结论 (Conclusion)

我们通过一个简单的矩阵乘加脚本探索了 PyTorch 性能剖析，并建立了适用于更大模型的关键心智模型。至此结束了《PyTorch 性能剖析》系列的第一篇。请继续阅读[第二篇：从 nn.Linear 到融合 MLP (Fused MLP)](https://huggingface.co/blog/torch-mlp-fusion) 以在这些概念的基础上继续进阶。

*特别感谢 Noe Flandre、Suvaditya Mukherjee 和 Vidit Ostwal 的审阅。*