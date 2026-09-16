---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-09-17
hide:
  - navigation
tags:
  - NVIDIA
  - cuDNN
  - 算子融合
  - 自动调优
  - GPU 优化
title: "深入探秘 NVIDIA cuDNN Graph API：基于 Frontend 的算子融合、自动调优与计划复用"
---

# 深入探秘 NVIDIA cuDNN Graph API：基于 Frontend 的算子融合、自动调优与计划复用

> # Inside NVIDIA’s cuDNN Graph API: Fusion, Autotuning, and Plan Reuse with cuDNN Frontend

### 文章背景与核心概要

随着深度学习模型规模的爆发式增长，现代 GPU 硬件面临着严峻的显存带宽瓶颈，传统框架层逐个算子调用的模式会产生海量中间张量的读写开销。NVIDIA 推出的 cuDNN Graph API 及其高层封装 cuDNN Frontend 彻底打破了以往僵硬的库函数黑盒限制，允许开发者以有向计算图的形式自由编排算子。借助该接口，工程师能够将卷积或矩阵乘法与其后续的偏置加法、激活函数、AMAX 规约等操作深度融合成单个高效内核，并精细挑选最优的底层执行引擎。本文通过详实的单卡实测代码，全面拆解了算子融合、引擎自动调优、执行计划序列化持久化、动态维度内核缓存以及 CUDA Graph 捕获等核心技术，为构建极致吞吐与低延迟的生产级推理服务提供了深度实践参考。

---

## 执行摘要

> ## Executive Summary

本教程带你深入传统深度学习框架底层，全面探索 NVIDIA **cuDNN Frontend** 计算图 API (Graph API) 的强大功能。它摒弃了过往僵化固定的库函数逐层调用逻辑，转而将所有前向或反向计算建模为由各个算子构成的有向计算图。这种贴近硬件底层的构建方式，赋予了开发者极高的控制权：不仅能够手动挑选最契合当前硬件的底层执行引擎 (Execution Engine)，还能构建高度优化的融合内核 (Fused Kernel) ——彻底消除偏置相加 (Bias Addition)、激活函数 (Activation) 以及 AMAX 极值规约等尾部运算产生的显存往返开销；此外，它还原生支持全引擎自动调优 (Autotuning)、执行计划序列化与反序列化 (Plan Serialization)、动态张量形状 (Dynamic Shapes) 处理，并能无缝接入 CUDA Graph 进行图捕获，从而消除内核启动开销。

> This tutorial explores NVIDIA’s **cuDNN Frontend** graph API from beneath traditional deep learning frameworks. Rather than relying on rigid library calls, computations are modeled as directed graphs of operations. This low-level approach allows developers to manually select execution engines, construct highly optimized fused kernels (eliminating unnecessary memory traffic for operations like bias additions, activations, and AMAX reductions), leverage autotuning, utilize plan serialization, handle dynamic shapes, and integrate with CUDA graph capture. 

文中给出的所有实操代码均在单张 GPU 上完成了严格测试，并与原生 PyTorch 的参考基准进行了逐一比对，在确保数值计算绝对正确的前提下量化测量了算子融合与图优化带来的实际性能飞跃。

> All code examples are tested against PyTorch references on a single GPU to validate correctness and measure performance gains.

---

## 1. 环境配置与系统初始化

> ## 1. Environment Setup & Initialization

我们首先安装 `nvidia-cudnn-frontend` 依赖包，并配置动态链接器以确保系统能够精准定位并加载 `libcudnn.so` 动态库。接着，根据当前 GPU 的硬件计算能力 (Compute Capability) 自动匹配并初始化计算精度（在较新的架构上优先选择 `bfloat16`，否则采用 `float16`），同时定义了一套可复用的通用辅助函数，用于张量描述、计算图编译构建、显存工作区 (Workspace) 分配以及基准性能测试。

> We begin by installing the `nvidia-cudnn-frontend` package and configuring the dynamic loader to ensure `libcudnn.so` is correctly detected. We initialize the working precision (`bfloat16` or `float16` depending on compute capability) and define reusable helper functions for tensor descriptions, graph compilation, workspace allocation, and benchmarking.

```python
import os
import sys
import glob
import math
import time
import ctypes
import traceback
import subprocess

RESULTS = {}

def banner(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)

def section(name):
    def wrap(fn):
        def run(*a, **kw):
            banner(name)
            try:
                out = fn(*a, **kw)
                RESULTS[name] = out if isinstance(out, str) else "ok"
                return out
            except Exception as e:
                RESULTS[name] = f"SKIPPED / FAILED -> {type(e).__name__}: {e}"
                print(f"\n[!] {name} did not complete: {type(e).__name__}: {e}")
                traceback.print_exc(limit=3)
                return None
        return run
    return wrap

banner("0. Install nvidia-cudnn-frontend and locate libcudnn")
subprocess.run(
    [sys.executable, "-m", "pip", "install", "-q", "nvidia-cudnn-frontend"],
    check=True,
)

import torch
assert torch.cuda.is_available(), "No GPU. Runtime -> Change runtime type -> GPU."
torch.backends.cudnn.enabled = True
_ = torch.nn.functional.conv2d(
    torch.randn(1, 1, 8, 8, device="cuda"), torch.randn(1, 1, 3, 3, device="cuda")
)
torch.cuda.synchronize()

try:
    import nvidia.cudnn
    _libdir = os.path.join(os.path.dirname(nvidia.cudnn.__file__), "lib")
    os.environ["CUDNN_PATH"] = os.path.dirname(nvidia.cudnn.__file__)
    os.environ["LD_LIBRARY_PATH"] = _libdir + ":" + os.environ.get("LD_LIBRARY_PATH", "")
    for _so in sorted(glob.glob(os.path.join(_libdir, "libcudnn*.so*"))):
        try:
            ctypes.CDLL(_so, mode=ctypes.RTLD_GLOBAL)
        except OSError:
            pass
except Exception as _e:
    print(f"  (no pip cuDNN package found, relying on system cuDNN: {_e})")

import cudnn
print("  cuDNN frontend imported successfully.")

banner("1. Environment")
DEV = torch.device("cuda")
MAJOR, MINOR = torch.cuda.get_device_capability()
SM = MAJOR * 10 + MINOR
CUDNN_VER = cudnn.backend_version()

print(f"  GPU                 : {torch.cuda.get_device_name(0)}")
print(f"  Compute capability  : sm_{SM}")
print(f"  Torch / CUDA        : {torch.__version__} / {torch.version.cuda}")
print(f"  cuDNN backend       : {CUDNN_VER}")

try:
    print(f"  cuDNN version str   : {cudnn.backend_version_string()}")
except Exception:
    pass

DTYPE = torch.bfloat16 if SM >= 80 else torch.float16
HAS_SDPA = SM >= 80
print(f"  Working dtype       : {DTYPE}")
print(f"  Fused SDPA usable   : {HAS_SDPA}")

HANDLE = cudnn.create_handle()
TORCH2CUDNN = {
    torch.float16: cudnn.data_type.HALF,
    torch.bfloat16: cudnn.data_type.BFLOAT16,
    torch.float32: cudnn.data_type.FLOAT,
    torch.int32: cudnn.data_type.INT32,
    torch.int64: cudnn.data_type.INT64,
    torch.int8: cudnn.data_type.INT8,
    torch.uint8: cudnn.data_type.UINT8,
}

def tensor_of(graph, t, name):
    return graph.tensor(
        name=name,
        dim=list(t.size()),
        stride=list(t.stride()),
        data_type=TORCH2CUDNN[t.dtype],
    )

def scalar_of(graph, name):
    return graph.tensor(
        name=name,
        dim=[1, 1, 1],
        stride=[1, 1, 1],
        data_type=cudnn.data_type.FLOAT,
        is_pass_by_value=True,
    )

def build(graph, heur=None, policy=None):
    heur = heur or [cudnn.heur_mode.A, cudnn.heur_mode.FALLBACK]
    graph.validate()
    graph.build_operation_graph()
    graph.create_execution_plans(heur)
    graph.check_support()
    if policy is None:
        graph.build_plans()
    else:
        graph.build_plans(policy)
    return graph

def workspace_for(graph):
    n = graph.get_workspace_size()
    return torch.empty(max(n, 1), device=DEV, dtype=torch.uint8)

def bench(fn, warmup=10, iters=50):
    for _ in range(warmup):
        fn()
    torch.cuda.synchronize()
    s, e = torch.cuda.Event(True), torch.cuda.Event(True)
    s.record()
    for _ in range(iters):
        fn()
    e.record()
    torch.cuda.synchronize()
    return s.elapsed_time(e) / iters

def tflops(flops, ms):
    return flops / (ms * 1e-3) / 1e12

def report(tag, ms, flops=None):
    extra = f"   ({tflops(flops, ms):7.2f} TFLOP/s)" if flops else ""
    print(f"    {tag:<34s} {ms:8.3f} ms{extra}")
```

---

## 2. 算子融合实战：卷积 $\rightarrow$ 偏置加法 $\rightarrow$ ReLU

> ## 2. Fused Convolution $\rightarrow$ Bias $\rightarrow$ ReLU

接下来我们着手构建第一个完整的计算图：将二维卷积 (2D Convolution)、偏置加法 (Bias Addition) 以及非线性激活函数 ReLU 紧密串联，全流程融合成单个 GPU 内核 (Single Kernel)。在张量内存布局上，所有输入输出均严格维持通道后置的 `channels_last` (NHWC) 内存格式，以便充分发挥 NVIDIA Tensor Core 硬件核心的向量化加速吞吐。

> We construct our first computation graph: a 2D convolution followed by a bias addition and a ReLU activation, fused entirely into a single kernel. Tensors are kept in `channels_last` (NHWC) format to match Tensor Core hardware requirements.

```python
N, C, H, W = 32, 128, 56, 56
K, R, S = 256, 3, 3
PAD, STR, DIL = 1, 1, 1
P = (H + 2 * PAD - DIL * (R - 1) - 1) // STR + 1
Q = (W + 2 * PAD - DIL * (S - 1) - 1) // STR + 1
CONV_FLOPS = 2 * N * K * P * Q * C * R * S
CONV_STATE = {}

@section("2. Fused Conv -> Bias -> ReLU")
def conv_fusion():
    x = torch.randn(N, C, H, W, device=DEV, dtype=DTYPE).to(memory_format=torch.channels_last)
    w = torch.randn(K, C, R, S, device=DEV, dtype=DTYPE).to(memory_format=torch.channels_last)
    b = torch.randn(1, K, 1, 1, device=DEV, dtype=DTYPE)
    y = torch.empty(N, K, P, Q, device=DEV, dtype=DTYPE).to(memory_format=torch.channels_last)

    g = cudnn.pygraph(
        handle=HANDLE,
        name="conv_bias_relu",
        io_data_type=TORCH2CUDNN[DTYPE],
        intermediate_data_type=cudnn.data_type.FLOAT,
        compute_data_type=cudnn.data_type.FLOAT,
    )
    X = tensor_of(g, x, "X")
    Wt = tensor_of(g, w, "W")
    Bt = tensor_of(g, b, "bias")

    conv = g.conv_fprop(
        image=X, weight=Wt,
        padding=[PAD, PAD], stride=[STR, STR], dilation=[DIL, DIL],
        compute_data_type=cudnn.data_type.FLOAT,
    )
    biased = g.bias(input=conv, bias=Bt)
    Y = g.relu(input=biased)
    
    Y.set_output(True).set_data_type(TORCH2CUDNN[DTYPE])
    Y.set_dim(list(y.size())).set_stride(list(y.stride()))

    t0 = time.perf_counter()
    build(g)
    build_ms = (time.perf_counter() - t0) * 1e3
    ws = workspace_for(g)
    
    pack = {X: x, Wt: w, Bt: b, Y: y}
    g.execute(pack, ws)
    torch.cuda.synchronize()

    ref = torch.relu(torch.nn.functional.conv2d(x, w, bias=b.flatten(), padding=PAD))
    err = (y.float() - ref.float()).abs().max().item()
    scale = ref.float().abs().max().item()

    print(f"    problem  : N{N} C{C} {H}x{W} -> K{K} {R}x{S}  ({DTYPE})")
    print(f"    build    : {build_ms:.1f} ms   workspace: {ws.numel()/1024:.1f} KiB")
    print(f"    max |err|: {err:.4f}  (ref max {scale:.2f}, rel {err/max(scale,1e-9):.2e})")
    assert err / max(scale, 1e-9) < 5e-2, "numerical mismatch vs PyTorch"

    ms_cudnn = bench(lambda: g.execute(pack, ws))
    ms_torch = bench(lambda: torch.relu(
        torch.nn.functional.conv2d(x, w, bias=b.flatten(), padding=PAD)))
    print()
    report("cuDNN FE (single fused kernel)", ms_cudnn, CONV_FLOPS)
    report("PyTorch (conv+bias, then relu)", ms_torch, CONV_FLOPS)
    print(f"    speedup: {ms_torch/ms_cudnn:.2f}x")

    CONV_STATE.update(graph=g, pack=pack, ws=ws, x=x, w=w, b=b, y=y)
    return f"{ms_cudnn:.3f} ms, {tflops(CONV_FLOPS, ms_cudnn):.1f} TFLOP/s"

conv_fusion()
```

---

## 3. 自动调优：全引擎候选配置基准评测

> ## 3. Autotuning: Benchmarking All Engine Configurations

与其完全盲目依赖库提供的默认启发式搜索，我们主动向系统查询了多种启发式决策模式（包含模式 `A`、模式 `B` 以及保底降级模式 `FALLBACK`），并通过 `cudnn.build_plan_policy.ALL` 策略构建出所有通过支持检查的候选执行计划 (Execution Plans)，从而横向测评各个可用引擎在当前硬件工况下的实际性能差异与算力发挥。

> Instead of relying purely on default heuristics, we query multiple heuristic modes (`A`, `B`, and `FALLBACK`) and build all candidate plans using `cudnn.build_plan_policy.ALL` to evaluate performance variations across available engines.

```python
@section("3. Autotuning: build ALL plans, time each engine config")
def autotune():
    x, w, b, y = CONV_STATE["x"], CONV_STATE["w"], CONV_STATE["b"], CONV_STATE["y"]
    g = cudnn.pygraph(
        handle=HANDLE, name="conv_autotune",
        io_data_type=TORCH2CUDNN[DTYPE],
        intermediate_data_type=cudnn.data_type.FLOAT,
        compute_data_type=cudnn.data_type.FLOAT,
    )
    X = tensor_of(g, x, "X")
    Wt = tensor_of(g, w, "W")
    Bt = tensor_of(g, b, "bias")
    Y = g.relu(input=g.bias(
        input=g.conv_fprop(image=X, weight=Wt, padding=[PAD, PAD],
                           stride=[STR, STR], dilation=[DIL, DIL],
                           compute_data_type=cudnn.data_type.FLOAT),
        bias=Bt))
    Y.set_output(True).set_data_type(TORCH2CUDNN[DTYPE])
    Y.set_dim(list(y.size())).set_stride(list(y.stride()))

    g.validate()
    g.build_operation_graph()
    g.create_execution_plans([cudnn.heur_mode.A, cudnn.heur_mode.B, cudnn.heur_mode.FALLBACK])
    g.check_support()
    g.build_plans(cudnn.build_plan_policy.ALL)
    
    n_plans = g.get_execution_plan_count()
    print(f"    {n_plans} candidate engine configs survived support checks\n")

    pack = {X: x, Wt: w, Bt: b, Y: y}
    timings = []
    for i in range(n_plans):
        try:
            g.build_plan_at_index(i)
            ws_sz = max(g.get_workspace_size_plan_at_index(i), 1)
            ws = torch.empty(ws_sz, device=DEV, dtype=torch.uint8)
            ms = bench(lambda: g.execute_plan_at_index(pack, ws, i), warmup=3, iters=15)
            timings.append((ms, i, ws_sz))
            print(f"      plan {i:>3d}: {ms:8.3f} ms  "
                  f"{tflops(CONV_FLOPS, ms):7.2f} TFLOP/s  ws={ws_sz/1024:8.1f} KiB")
        except Exception as e:
            print(f"      plan {i:>3d}: unusable ({type(e).__name__})")

    assert timings, "no plan executed"
    timings.sort()
    best_ms, best_i, best_ws = timings[0]
    worst_ms = timings[-1][0]

    print(f"\n    fastest = plan {best_i} @ {best_ms:.3f} ms")
    print(f"    slowest = {worst_ms:.3f} ms  -> {worst_ms/best_ms:.1f}x spread across engines")
    print("    Takeaway: heuristics are good, but for a hot shape you ship the")
    print("    autotuned index (or the serialized plan from section 6).")
    return f"best plan {best_i} @ {best_ms:.3f} ms ({worst_ms/best_ms:.1f}x spread)"

autotune()
```

---

## 4. 矩阵乘法尾声流水线：缩放、偏置、激活与 AMAX 规约

> ## 4. Matrix Multiplication Epilogues (Scaling, Bias, Activation, and AMAX)

现在我们将算子融合的范围扩展至批处理矩阵乘法 (Batched Matmul)，并在其尾声 (Epilogue) 阶段嫁接一条复杂的流水线：包含一个主机端标量 alpha 缩放因子相乘、偏置加法、非线性激活，以及提取绝对值最大值的 `AMAX` 极值规约（这一运算在最新的 FP8 低精度训练与量化工作流中至关重要）。

> We expand to batched matrix multiplication with a complex epilogue chain: a host scalar alpha scaling factor, bias addition, activation, and an `AMAX` reduction (useful for FP8 training quantization workflows).

```python
@section("4. Matmul -> scale -> bias -> activation -> AMAX")
def matmul_epilogue():
    Bsz, M, Kd, Nd = 16, 512, 1024, 512
    MM_FLOPS = 2 * Bsz * M * Nd * Kd
    a = torch.randn(Bsz, M, Kd, device=DEV, dtype=DTYPE)
    bm = torch.randn(Bsz, Kd, Nd, device=DEV, dtype=DTYPE)
    bias = torch.randn(1, 1, Nd, device=DEV, dtype=DTYPE)
    out = torch.empty(Bsz, M, Nd, device=DEV, dtype=DTYPE)
    amax = torch.empty(1, 1, 1, device=DEV, dtype=torch.float32)

    alpha_val = 0.125
    alpha = torch.full((1, 1, 1), alpha_val, dtype=torch.float32)

    g = cudnn.pygraph(
        handle=HANDLE, name="matmul_epilogue",
        io_data_type=TORCH2CUDNN[DTYPE],
        intermediate_data_type=cudnn.data_type.FLOAT,
        compute_data_type=cudnn.data_type.FLOAT,
    )
    A = tensor_of(g, a, "A")
    Bt = tensor_of(g, bm, "B")
    BIAS = tensor_of(g, bias, "bias")
    ALPHA = scalar_of(g, "alpha")

    acc = g.matmul(A=A, B=Bt, compute_data_type=cudnn.data_type.FLOAT)
    scaled = g.mul(a=acc, b=ALPHA)
    biased = g.bias(input=scaled, bias=BIAS)

    act_name = "relu"
    if hasattr(g, "gelu"):
        try:
            act = g.gelu(input=biased)
            act_name = "gelu"
        except Exception:
            act = g.relu(input=biased)
    else:
        act = g.relu(input=biased)

    print(f"    activation used: {act_name}")
    OUT = act
    OUT.set_output(True).set_data_type(TORCH2CUDNN[DTYPE])

    have_amax = True
    try:
        AMAX = g.reduction(input=act, mode=cudnn.reduction_mode.AMAX,
                           compute_data_type=cudnn.data_type.FLOAT)
        AMAX.set_output(True).set_data_type(cudnn.data_type.FLOAT)
        AMAX.set_dim([1, 1, 1]).set_stride([1, 1, 1])
    except Exception as e:
        have_amax = False
        print(f"    (AMAX reduction unavailable here: {e})")

    build(g)
    ws = workspace_for(g)
    pack = {A: a, Bt: bm, BIAS: bias, ALPHA: alpha, OUT: out}
    if have_amax:
        pack[AMAX] = amax

    g.execute(pack, ws)
    torch.cuda.synchronize()

    ref = torch.matmul(a.float(), bm.float()) * alpha_val + bias.float()
    ref = torch.nn.functional.gelu(ref) if act_name == "gelu" else torch.relu(ref)
    rel = ((out.float() - ref).abs().max() / ref.abs().max()).item()

    print(f"    shape    : ({Bsz},{M},{Kd}) x ({Bsz},{Kd},{Nd})")
    print(f"    rel err  : {rel:.2e}")
    if have_amax:
        print(f"    fused AMAX {amax.item():.4f} vs torch {ref.abs().max().item():.4f}")

    ms = bench(lambda: g.execute(pack, ws))
    def torch_ref():
        r = torch.baddbmm(bias.expand(Bsz, M, Nd), a, bm, beta=1.0, alpha=alpha_val)
        r = torch.nn.functional.gelu(r) if act_name == "gelu" else torch.relu(r)
        return r.abs().amax()
    ms_t = bench(torch_ref)
    print()
    report("cuDNN FE (one fused kernel)", ms, MM_FLOPS)
    report("PyTorch (bmm + act + amax)", ms_t, MM_FLOPS)
    print(f"    speedup: {ms_t/ms:.2f}x  -- the win is the epilogue traffic, not the GEMM")
    return f"{ms:.3f} ms, {tflops(MM_FLOPS, ms):.1f} TFLOP/s, {ms_t/ms:.2f}x vs torch"

matmul_epilogue()
```

---

## 5. 缩放点积注意力机制 (FlashAttention) 与执行计划序列化

> ## 5. SDPA (FlashAttention) & Plan Serialization

我们基于 cuDNN Graph API 实现了带有因果掩码 (Causal Masking) 的缩放点积注意力机制 (Scaled Dot-Product Attention, SDPA，即工业级 FlashAttention 实现，该特性需要 NVIDIA Ampere 架构及以上的 `SM80+` 硬件支持)；同时，我们展示了执行计划的序列化技术 (Plan Serialization) ——将编译完成的计算图序列化为二进制数据保存至磁盘，后续在生产部署时直接反序列化重载，并通过整数形式的唯一标识符 (UID) 绑定张量即可直接运行，从而彻底消除服务初次冷启动时的实时 JIT 编译等待。

> We implement Scaled Dot-Product Attention (SDPA) with causal masking (requiring Ampere `SM80+` architectures) and demonstrate plan serialization, allowing compiled graphs to be saved to disk, reloaded, and executed via integer UIDs to eliminate startup compilation delays.

```python
@section("5. SDPA (Flash Attention) with causal masking")
def sdpa_demo():
    if not HAS_SDPA:
        raise RuntimeError(f"fused SDPA needs SM80+ (Ampere), this GPU is sm_{SM}")
    b, h, s, d = 4, 16, 1024, 64
    scale = 1.0 / math.sqrt(d)
    SDPA_FLOPS = 4 * b * h * s * s * d * 0.5

    q = torch.randn(b, h, s, d, device=DEV, dtype=DTYPE)
    k = torch.randn(b, h, s, d, device=DEV, dtype=DTYPE)
    v = torch.randn(b, h, s, d, device=DEV, dtype=DTYPE)
    o = torch.empty(b, h, s, d, device=DEV, dtype=DTYPE)

    g = cudnn.pygraph(
        handle=HANDLE, name="sdpa",
        io_data_type=TORCH2CUDNN[DTYPE],
        intermediate_data_type=cudnn.data_type.FLOAT,
        compute_data_type=cudnn.data_type.FLOAT,
    )
    Q, Kt, V = tensor_of(g, q, "Q"), tensor_of(g, k, "K"), tensor_of(g, v, "V")
    causal = True
    try:
        O, _stats = g.sdpa(name="sdpa", q=Q, k=Kt, v=V,
                           is_inference=True, attn_scale=scale, use_causal_mask=True)
    except TypeError:
        try:
            O, _stats = g.sdpa(name="sdpa", q=Q, k=Kt, v=V,
                               is_inference=True, attn_scale=scale,
                               diagonal_alignment=cudnn.diagonal_alignment.TOP_LEFT,
                               right_bound=0)
        except Exception:
            causal = False
            O, _stats = g.sdpa(name="sdpa", q=Q, k=Kt, v=V,
                               is_inference=True, attn_scale=scale)
    print(f"    causal masking: {causal}")
    O.set_output(True).set_data_type(TORCH2CUDNN[DTYPE])
    O.set_dim(list(o.size())).set_stride(list(o.stride()))

    build(g)
    ws = workspace_for(g)
    pack = {Q: q, Kt: k, V: v, O: o}
    g.execute(pack, ws)
    torch.cuda.synchronize()

    ref = torch.nn.functional.scaled_dot_product_attention(q, k, v, is_causal=causal, scale=scale)
    rel = ((o.float() - ref.float()).abs().max() / ref.float().abs().max()).item()
    print(f"    shape   : b{b} h{h} s{s} d{d}   workspace {ws.numel()/1024:.1f} KiB")
    print(f"    rel err : {rel:.2e}")

    ms = bench(lambda: g.execute(pack, ws))
    ms_t = bench(lambda: torch.nn.functional.scaled_dot_product_attention(
        q, k, v, is_causal=causal, scale=scale))
    print()
    report("cuDNN FE SDPA", ms, SDPA_FLOPS)
    report("torch SDPA (backend's choice)", ms_t, SDPA_FLOPS)
    print("    Note: torch may already be dispatching to cuDNN or FlashAttention,")
    print("    so parity here is the expected, healthy outcome.")
    return f"{ms:.3f} ms, {tflops(SDPA_FLOPS, ms):.1f} TFLOP/s"

sdpa_demo()

@section("6. Serialize a built graph, reload it, execute by UID")
def serialization():
    Bsz, M, Kd, Nd = 8, 256, 512, 256
    a = torch.randn(Bsz, M, Kd, device=DEV, dtype=DTYPE)
    bm = torch.randn(Bsz, Kd, Nd, device=DEV, dtype=DTYPE)
    out = torch.empty(Bsz, M, Nd, device=DEV, dtype=DTYPE)
    UID_A, UID_B, UID_C = 1, 2, 3

    g = cudnn.pygraph(
        handle=HANDLE, name="serializable_mm",
        io_data_type=TORCH2CUDNN[DTYPE],
        intermediate_data_type=cudnn.data_type.FLOAT,
        compute_data_type=cudnn.data_type.FLOAT,
    )
    A = tensor_of(g, a, "A").set_uid(UID_A)
    Bt = tensor_of(g, bm, "B").set_uid(UID_B)
    C = g.matmul(A=A, B=Bt, compute_data_type=cudnn.data_type.FLOAT)
    C.set_output(True).set_data_type(TORCH2CUDNN[DTYPE]).set_uid(UID_C)

    t0 = time.perf_counter()
    build(g)
    cold_ms = (time.perf_counter() - t0) * 1e3
    blob = g.serialize()

    print(f"    cold build      : {cold_ms:.1f} ms")
    print(f"    serialized plan : {len(blob)} bytes (cache this to disk / ship it)")

    t0 = time.perf_counter()
    g2 = cudnn.pygraph()
    try:
        g2.deserialize(HANDLE, blob)
    except TypeError:
        g2.deserialize(blob)
    warm_ms = (time.perf_counter() - t0) * 1e3
    print(f"    deserialize     : {warm_ms:.1f} ms  -> {cold_ms/max(warm_ms,1e-6):.1f}x faster startup")

    ws = torch.empty(max(g2.get_workspace_size(), 1), device=DEV, dtype=torch.uint8)
    g2.execute({UID_A: a, UID_B: bm, UID_C: out}, ws, handle=HANDLE)
    torch.cuda.synchronize()

    ref = torch.bmm(a.float(), bm.float())
    rel = ((out.float() - ref).abs().max() / ref.abs().max()).item()
    print(f"    rel err after reload: {rel:.2e}")
    return f"{len(blob)} B blob, reload {cold_ms/max(warm_ms,1e-6):.1f}x faster than rebuild"

serialization()
```

---

## 6. 动态维度处理与 CUDA Graph 捕获加速

> ## 6. Dynamic Shapes and CUDA Graph Capture

在实际推理场景中，为了高效应对多变的批处理大小 (Batch Size) 或变长序列长度 (Sequence Length)，同时避免每次维度微调都触发昂贵的实时 JIT 重新编译，我们跨计算图共享了底层内核缓存 (Kernel Cache)。更进一步，我们还将编译好的执行计划封装进 CUDA Graph 的图捕获机制中，彻底抹平了每次迭代在 CPU 与 GPU 之间的内核启动延迟 (Kernel Launch Latency)。

> To manage dynamic batch sizes or sequence lengths efficiently without incurring continuous JIT compilation overhead, we share a kernel cache across graph iterations. Furthermore, we wrap execution plans inside CUDA graphs to remove per-iteration kernel launch latencies.

```python
@section("7. Dynamic shapes with a shared kernel cache")
def dynamic_shapes():
    kc = cudnn.create_kernel_cache()
    def make(n):
        x = torch.randn(n, 64, 32, 32, device=DEV, dtype=DTYPE).to(memory_format=torch.channels_last)
        w = torch.randn(64, 64, 3, 3, device=DEV, dtype=DTYPE).to(memory_format=torch.channels_last)
        y = torch.empty(n, 64, 32, 32, device=DEV, dtype=DTYPE).to(memory_format=torch.channels_last)
        g = cudnn.pygraph(
            handle=HANDLE, name=f"dyn_{n}",
            io_data_type=TORCH2CUDNN[DTYPE],
            intermediate_data_type=cudnn.data_type.FLOAT,
            compute_data_type=cudnn.data_type.FLOAT,
            kernel_cache=kc,
            is_dynamic_shape_enabled=True,
        )
        X, Wt = tensor_of(g, x, "X"), tensor_of(g, w, "W")
        Y = g.conv_fprop(image=X, weight=Wt, padding=[1, 1], stride=[1, 1],
                         dilation=[1, 1], compute_data_type=cudnn.data_type.FLOAT)
        Y.set_output(True).set_data_type(TORCH2CUDNN[DTYPE])
        Y.set_dim(list(y.size())).set_stride(list(y.stride()))

        t0 = time.perf_counter()
        build(g)
        ms = (time.perf_counter() - t0) * 1e3
        ws = workspace_for(g)
        g.execute({X: x, Wt: w, Y: y}, ws)
        torch.cuda.synchronize()
        return ms

    times = [(n, make(n)) for n in (8, 16, 24, 32)]
    for n, ms in times:
        print(f"      batch {n:>3d}: build {ms:7.1f} ms")
    first, rest = times[0][1], [m for _, m in times[1:]]
    print(f"\n    first shape {first:.1f} ms, later shapes avg {sum(rest)/len(rest):.1f} ms")
    print("    The cache lets shape-variant graphs reuse an already-JIT'd kernel,")
    print("    which is what keeps variable batch/seqlen serving out of rebuild hell.")
    return f"first {first:.0f} ms vs subsequent {sum(rest)/len(rest):.0f} ms"

dynamic_shapes()

@section("8. CUDA Graph capture around a cuDNN execution plan")
def cuda_graph_capture():
    if not CONV_STATE:
        raise RuntimeError("section 2 did not run, nothing to capture")
    g, pack, ws = CONV_STATE["graph"], CONV_STATE["pack"], CONV_STATE["ws"]
    eager_ms = bench(lambda: g.execute(pack, ws))

    side = torch.cuda.Stream()
    side.wait_stream(torch.cuda.current_stream())
    with torch.cuda.stream(side):
        cudnn.set_stream(handle=HANDLE, stream=side.cuda_stream)
        for _ in range(3):
            g.execute(pack, ws, handle=HANDLE)
    torch.cuda.current_stream().wait_stream(side)
    torch.cuda.synchronize()

    cg = torch.cuda.CUDAGraph()
    with torch.cuda.graph(cg):
        cudnn.set_stream(handle=HANDLE, stream=torch.cuda.current_stream().cuda_stream)
        g.execute(pack, ws, handle=HANDLE)
    cudnn.set_stream(handle=HANDLE, stream=torch.cuda.current_stream().cuda_stream)

    replay_ms = bench(lambda: cg.replay())
    report("plain execute()", eager_ms)
    report("cuda graph replay()", replay_ms)
    print(f"    launch overhead removed: {(eager_ms-replay_ms)*1e3:.1f} us/iter")
    print("    Pointers are frozen at capture time -- reuse the same buffers and")
    print("    copy new data into them, or re-capture.")
    return f"{eager_ms:.3f} -> {replay_ms:.3f} ms via replay"

cuda_graph_capture()

banner("SUMMARY")
for name, res in RESULTS.items():
    print(f"  {name:<58s} {res}")

print("""
Where to go next
 - samples/python in the repo: FP8/MXFP8 attention, paged KV cache, MoE grouped GEMM
 - python/cudnn/: the open-sourced CuTe DSL kernels (SDPA, grouped GEMM + SwiGLU,
   block-sparse and native sparse attention) you can read and modify
 - debugging: CUDNN_FRONTEND_LOG_INFO=1 and CUDNN_FRONTEND_LOG_FILE=stdout
   (use level 10 during CUDA graph capture -- level 1 dumps tensors and is not
   capture-safe)
""")
```

---

## 总结

> ## Conclusion

将深度学习网络层重构为显式的有向计算图，使开发者得以对内核融合、执行引擎筛选、编译生命周期以及内核启动开销拥有极致而精准的控制力。cuDNN Frontend API 在许多高频严苛场景中表现尤为卓越，例如：定制化的算子融合（彻底免除激活与规约尾声中间变量的显存写回）、对频繁调用的热点形状 (Hot Shapes) 进行严密的自动调优，以及结合 CUDA Graph 与执行计划序列化技术打造高性能、极低延迟的生产级在线推理服务闭环。

> By structuring deep learning layers as explicit computation graphs, developers unlock precise control over kernel fusion, engine selection, compilation lifecycles, and launch overheads. The cuDNN Frontend API excels particularly in scenarios involving custom fusions (such as avoiding intermediate writes for activation and reduction epilogues), hot shapes requiring rigorous autotuning, and performance-critical low-latency serving loops enhanced via CUDA graphs and plan serialization.

---

欢迎查阅 **[完整源码链接](https://github.com/MARKTECHPOST-AI-MEDIA-INC/AI-Agents-Projects-Tutorials/blob/main/Deep%20Learning/cudnn_frontend_nvidia_tutorial_Marktechpost.ipynb)**。本项目所有成果归原作者研究团队所有。欢迎在 **[Twitter](https://x.com/intent/follow?screen_name=marktechpost)** 上关注我们，加入拥有 **[15 万+ 成员的机器学习 SubReddit 社区](https://www.reddit.com/r/machinelearningnews/)**，订阅 **[官方技术周刊](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526?email={{email}})**，以及关注我们的 **[Telegram 频道](https://t.me/machinelearningresearchnews)**。

> Check out the **[FULL CODES here](https://github.com/MARKTECHPOST-AI-MEDIA-INC/AI-Agents-Projects-Tutorials/blob/main/Deep%20Learning/cudnn_frontend_nvidia_tutorial_Marktechpost.ipynb)**. All credit goes to the researcher of this project. Feel free to follow us on **[Twitter](https://x.com/intent/follow?screen_name=marktechpost)** and join our **[150k+ ML SubReddit](https://www.reddit.com/r/machinelearningnews/)**, subscribe to **[our Newsletter](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526?email={{email}})**, and join our **[Telegram channel](https://t.me/machinelearningresearchnews)**.

如需洽谈 GitHub 开源项目推广、Hugging Face 专题页面合作、新品发布或线上技术研讨会等商务合作，欢迎 **[点击此处与我们联系](https://forms.gle/wbash1wF6efRj8G58)**。

> For partnership inquiries regarding GitHub repo promotions, Hugging Face pages, product releases, or webinars, **[connect with us here](https://forms.gle/wbash1wF6efRj8G58)**.

本文首发于 [MarkTechPost](https://www.marktechpost.com)，原文标题为 [Inside NVIDIA’s cuDNN Graph API: Fusion, Autotuning, and Plan Reuse with cuDNN Frontend](https://www.marktechpost.com/2026/09/15/inside-nvidias-cudnn-graph-api-fusion-autotuning-and-plan-reuse-with-cudnn-frontend/)。

> The post [Inside NVIDIA’s cuDNN Graph API: Fusion, Autotuning, and Plan Reuse with cuDNN Frontend](https://www.marktechpost.com/2026/09/15/inside-nvidias-cudnn-graph-api-fusion-autotuning-and-plan-reuse-with-cudnn-frontend/) appeared first on [MarkTechPost](https://www.marktechpost.com).
