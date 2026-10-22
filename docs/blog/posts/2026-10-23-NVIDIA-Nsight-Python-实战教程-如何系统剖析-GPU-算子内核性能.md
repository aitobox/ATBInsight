---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-10-23
hide:
  - navigation
tags:
  - NVIDIA Nsight
  - GPU 算子内核
  - 性能剖析
  - Python
  - CUDA
title: "NVIDIA Nsight Python 实战教程：如何系统剖析 GPU 算子内核性能"
---

# NVIDIA Nsight Python 实战教程：如何系统剖析 GPU 算子内核性能

> # NVIDIA Nsight Python Tutorial: How to Profile GPU Kernelfs

### 文章背景与核心概要

随着深度学习与大模型向万亿参数规模演进，GPU 算子内核的微观性能调优成为突破计算瓶颈的关键。然而，传统的 NVIDIA Nsight Compute 工具往往依赖繁琐的命令行或独立的图形界面，严重割裂了算法开发者的交互式研发体验。NVIDIA 推出的开源 Nsight Python 接口，通过装饰器与上下文管理器将复杂的底层硬件指标直接捕获进 Pandas 数据帧，彻底打通了从算子编写到微架构性能剖析的高速闭环。本文将带领读者在 Google Colab 环境中，系统掌握算子耗时测量、缓存与时钟控制、瓶颈诊断及算子融合量化等全套实战调优技能。

---

## 核心概述

> ## Summary

本教程将深入探讨 **Nsight Python**——这是 NVIDIA 为底层内核性能剖析器打造的开源 Python 接口。通过装饰器 ( `nsight.analyze.kernel` ) 与上下文管理器 ( `nsight.annotate` )，Nsight Python 能直接无缝嵌入到 Python 脚本中，绕过 Nsight Compute 烦琐的命令行交互流程，并将各项底层硬件指标直接输出为 Pandas 的 `DataFrame`。从最基础的矩阵乘法，到高级的缓存与时钟频率控制、算子融合 (Kernel Fusion)、自定义信息收集器，再到实验性的 CUPTI 后端，本指南将在免费的 Google Colab T4 实例上完整演示如何高效剖析 GPU 工作负载。

> This tutorial explores **Nsight Python**—NVIDIA's open-source Python interface for kernel profilers. By integrating directly into your Python scripts via decorators (`nsight.analyze.kernel`) and context managers (`nsight.annotate`), Nsight Python bypasses the tedious command-line workflows of Nsight Compute, returning hardware metrics straight into a Pandas `DataFrame`. Covering everything from basic matrix multiplications to advanced cache/clock control, kernel fusion, custom information collectors, and the experimental CUPTI backend, this guide demonstrates how to profile GPU workloads efficiently on a free Google Colab T4 instance.

---

## 1. 安装与环境配置

> ## 1. Installation and Environment Setup

在执行任何 CUDA 操作之前，务必优先导入 `nsight`，这样 Nsight Compute 的注入库才能顺利挂钩 (Hook) 到 Python 进程中。由于 Colab 默认预装的 Nsight Compute ( `ncu` ) 版本较旧，我们需要通过 NVIDIA 官方的 CUDA APT 软件源对其进行升级，并安装指定版本的 Nsight Python 预览版。

> Before running any CUDA operations, it is critical to import `nsight` so that Nsight Compute’s injection library can hook into the Python process. Since Colab ships with an older version of Nsight Compute (`ncu`), we update it via NVIDIA's CUDA APT repository and install the pinned Nsight Python pre-release.

```python
import os
import sys
import glob
import json
import time
import shutil
import textwrap
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
                RESULTS[name] = f"SKIPPED / FAILED -> {type(e).__name__}: {str(e).splitlines()[0][:160]}"
                print(f"\n[!] {name} did not complete: {type(e).__name__}: {e}")
                traceback.print_exc(limit=3)
                return None
        return run
    return wrap
 
def sh(cmd):
    """Run a shell command and return its stdout, stripped."""
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
 
banner("1. Install a current Nsight Compute next to Colab's, then import nsight before CUDA")
print(f"  GPU: {sh('nvidia-smi --query-gpu=name,driver_version,memory.total,compute_cap --format=csv,noheader')}")
preinstalled = shutil.which("ncu")
print(f"  ncu already on PATH: {preinstalled} -> {sh('ncu --version | tail -1') if preinstalled else 'none'}")
 
# Install Nsight Compute from NVIDIA's apt repository
subprocess.run("apt-get update -qq > /tmp/ncu_install.log 2>&1", shell=True)
for NCU_VERSION in ("2026.3.1", "2026.2.1"):
    if subprocess.run(f"apt-get install -y -qq nsight-compute-{NCU_VERSION} >> /tmp/ncu_install.log 2>&1",
                      shell=True).returncode == 0:
        break
else:
    print(sh("tail -5 /tmp/ncu_install.log"))
    raise RuntimeError("could not install Nsight Compute 2026.2.1+ from NVIDIA's apt repository")

ncu_paths = sh(f"dpkg -L nsight-compute-{NCU_VERSION} | grep -E '/ncu$'").split()
if not ncu_paths:
    raise RuntimeError(f"dpkg lists no ncu executable in nsight-compute-{NCU_VERSION}")
NCU_DIR = os.path.dirname(min(ncu_paths, key=len))
os.environ["PATH"] = NCU_DIR + os.pathsep + os.environ["PATH"]
print(f"  installed: {shutil.which('ncu')} -> {sh('ncu --version | tail -1')}")
 
# Install Nsight Python
NSIGHT_COMMIT = "bb96db4260b1823d86ecab9acfed0646d7af79ad"
subprocess.run([sys.executable, "-m", "pip", "install", "-q",
                f"nsight-python @ git+https://github.com/NVIDIA/nsight-python@{NSIGHT_COMMIT}"], check=True)

CUPTI_DIR = "/content/cupti_env"
CUPTI_EXTRA = subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--target", CUPTI_DIR, "--no-deps",
                              "cupti-python>=13.4.0", "nvidia-cuda-cupti~=13.4", "pyelftools"]).returncode == 0
 
import nsight  # MUST come before anything initializes CUDA
from nsight.collection import ncu as ncu_backend
 
import numpy as np
import pandas as pd
import torch
 
SILENT = nsight.VerbosityLevel.SILENT
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
print(f"  nsight-python {nsight.__version__} | active tool: {nsight.get_active_tool()}"
      f" | injection error at import: {ncu_backend.injection_load_error}")
print(f"  torch {torch.__version__} (CUDA {torch.version.cuda}) | {torch.cuda.get_device_name(0)}"
      f" | cupti-python installed: {CUPTI_EXTRA}")
```

---

## 2. 单个算子内核性能剖析

> ## 2. Profiling a Single Kernel

借助 `nsight.annotate`，我们可以精准隔离出需要进行性能剖析的目标代码块，同时剔除周围繁杂的准备工作 (例如随机张量的初始化生成) 对测试结果的干扰。

> Using `nsight.annotate`, we can isolate specific code blocks for profiling while omitting surrounding setup operations (like random tensor generation).

```python
ADD = lambda x, y: x + y   # sums metrics if cuBLAS splits a matmul into multiple kernels
 
@nsight.analyze.kernel(thermal_mode="off", combine_kernel_metrics=ADD)
def first_matmul(n: int) -> None:
    a = torch.randn(n, n, device="cuda")
    b = torch.randn(n, n, device="cuda")
    with nsight.annotate("matmul"):
        _ = a @ b
 
@section("2. Profile one kernel: what a ProfileResults row contains")
def first_profile():
    df = first_matmul(2048).to_dataframe()
    print(f"\n  to_dataframe() columns: {list(df.columns)}\n")
    r = df.iloc[0]
    t = float(r["AvgValue"])
    print(f"  annotation {r['Annotation']!r}, n = {r['n']}, kernel {r['Kernel']}")
    print(f"  {r['Metric']} = {t:,.0f} {r['Unit']}  (runs {r['NumRuns']}, stable: {r['StableMeasurement']})")
    print(f"  GPU {r['GPU']}, ComputeClock {r['ComputeClock']}, MemoryClock {r['MemoryClock']}")
    print(f"  -> {2 * 2048 ** 3 / (t * 1e-9) / 1e12:.2f} TFLOP/s for a 2048 x 2048 fp32 matmul")
    return f"fp32 2048 matmul {t / 1e6:.3f} ms ({2 * 2048 ** 3 / (t * 1e-9) / 1e12:.2f} TFLOP/s)"
 
first_profile()
```

---

## 3. 评估测量稳定性与数据离散度

> ## 3. Evaluating Stability and Spread

单次性能测量往往极易受到系统偶发噪声的干扰而产生偏差。通过执行多次迭代测试 (例如设置 `runs=20` )，我们能够自动生成置信区间与标准差，从而系统评估算子内核执行耗时的稳定性。

> A single measurement can be heavily skewed by noise. By running multiple iterations (e.g., `runs=20`), we generate confidence intervals and standard deviations to assess kernel timing stability.

```python
def show(df, cols, scale=None, fmt="{:,.2f}"):
    out = df[cols].copy()
    for c, f in (scale or {}).items():
        out[c] = out[c] * f
    print(textwrap.indent(out.to_string(index=False, float_format=lambda v: fmt.format(v)), "  "))
 
@nsight.analyze.kernel(configs=[1 << 14, 1 << 24], runs=20, thermal_mode="off", verbosity=SILENT,
                       combine_kernel_metrics=ADD)
def noisy_or_not(n: int) -> None:
    x = torch.randn(n, device="cuda")
    y = torch.randn(n, device="cuda")
    a = torch.randn(2048, 2048, device="cuda")
    with nsight.annotate("vector add"):
        _ = x + y
    with nsight.annotate("matmul 2048"):
        _ = a @ a
 
@section("3. How many runs? Spread, confidence intervals and the stability flag")
def stability():
    df = noisy_or_not().to_dataframe()
    print("  20 runs per configuration; times in microseconds:\n")
    show(df, ["Annotation", "n", "AvgValue", "StdDev", "CI95_Lower", "CI95_Upper", "RelativeStdDevPct",
              "StableMeasurement"], scale={"AvgValue": 1e-3, "StdDev": 1e-3, "CI95_Lower": 1e-3, "CI95_Upper": 1e-3})
    tiny = df[(df.Annotation == "vector add") & (df.n == 1 << 14)].iloc[0]
    print(f"\n  StableMeasurement is simply RelativeStdDevPct < 2. The smallest kernel ({tiny['AvgValue'] / 1e3:.1f} us)")
    print(f"  varies by {tiny['RelativeStdDevPct']:.1f}% due to launch and clock jitter.")
    return f"16K-element add RSD {tiny['RelativeStdDevPct']:.1f}%"
 
stability()
```

---

## 4. 缓存与时钟频率控制

> ## 4. Cache and Clock Control

剖析器的参数配置对最终的性能读数有着决定性的影响。其中，`cache_control` 参数控制每次运行之间是否清空 L2 缓存，而 `clock_control` 则决定 GPU 流式多处理器 (Streaming Multiprocessor, SM) 的时钟频率是被锁定在基准频率，还是允许根据负载动态睿频加速。

> Profiler configurations significantly alter performance readings. `cache_control` dictates whether L2 caches are flushed between runs, while `clock_control` determines if GPU SM clocks are locked or allowed to boost dynamically.

```python
def make_scale_bench(cache_control, clock_control):
    @nsight.analyze.kernel(configs=[1 << 18, 1 << 24], runs=10, cache_control=cache_control,
                           clock_control=clock_control, thermal_mode="off", verbosity=SILENT,
                           metrics=["gpu__time_duration.sum", "gpc__cycles_elapsed.avg.per_second"])
    def scale(n: int) -> None:
        x = torch.randn(n, device="cuda")
        with nsight.annotate("x * 2"):
            _ = x * 2.0
    return scale
 
@section("4. Cache and clock control: two defaults that change the answer")
def cache_and_clocks():
    rows = []
    for cache in ("all", "none"):
        for clock in ("none", "base"):
            try:
                df = make_scale_bench(cache, clock)().to_dataframe()
            except Exception as e:
                print(f"  cache_control={cache!r}, clock_control={clock!r}: failed -> {type(e).__name__}")
                continue
            t = df[df.Metric == "gpu__time_duration.sum"].set_index("n").AvgValue
            hz = df[df.Metric == "gpc__cycles_elapsed.avg.per_second"].set_index("n").AvgValue
            for n in t.index:
                rows.append({"cache_control": cache, "clock_control": clock, "MB": 4 * n / 2 ** 20,
                             "time_us": t[n] / 1e3, "GB/s": 2 * 4 * n / t[n], "SM_MHz": hz[n] / 1e6})
    tab = pd.DataFrame(rows)
    print(textwrap.indent(tab.to_string(index=False, float_format=lambda v: f"{v:,.1f}"), "  "))
    globals()["CLOCK_TABLE"] = tab
    return f"Completed cache/clock sweep across {len(tab)} configurations."
 
cache_and_clocks()
```

---

## 5. 尺寸扫描、派生指标与基准归一化

> ## 5. Size Sweeps, Derived Metrics, and Normalization

Nsight Python 支持灵活自定义派生指标 (例如在测试过程中即时换算 TFLOP/s 算力利用率)，并能参照特定的基线对结果进行归一化对比 (例如直接将 `fp16` 精度下的性能表现与 `fp32` 进行相对比对)。

> Nsight Python allows customized derived metrics (such as calculating TFLOP/s on the fly) and normalizing results against specific baselines (e.g., comparing `fp16` performance directly against `fp32`).

```python
SIZES = [(512,), (1024,), (2048,), (4096,)]
 
def tflops(time_ns: float, n: int) -> tuple[float, str]:
    return 2 * n ** 3 / (time_ns * 1e-9) / 1e12, "TFLOP/s"
 
def make_precision_body():
    def precision(n: int) -> None:
        a = torch.randn(n, n, device="cuda")
        b = torch.randn(n, n, device="cuda")
        a16, b16 = a.half(), b.half()
        with nsight.annotate("fp32"):
            _ = a @ b
        with nsight.annotate("fp16"):
            _ = a16 @ b16
    return precision
 
precision_tflops = nsight.analyze.kernel(configs=SIZES, runs=5, derive_metric=tflops, thermal_mode="off",
                                         verbosity=SILENT, combine_kernel_metrics=ADD)(make_precision_body())
precision_ratio = nsight.analyze.kernel(configs=SIZES, runs=5, normalize_against="fp32", thermal_mode="off",
                                        verbosity=SILENT, combine_kernel_metrics=ADD)(make_precision_body())
 
@section("5. A size sweep, a derived TFLOP/s metric, and normalisation")
def precision_sweep():
    df = precision_tflops().to_dataframe()
    tf = df[df.Metric == "tflops"].pivot(index="n", columns="Annotation", values="AvgValue")
    print("  derive_metric=tflops results:\n")
    print(textwrap.indent(tf[["fp32", "fp16"]].to_string(float_format=lambda v: f"{v:,.2f}"), "  "))
    return f"n=4096: fp32 {tf.loc[4096, 'fp32']:.2f}, fp16 {tf.loc[4096, 'fp16']:.2f} TFLOP/s"
 
precision_sweep()
```

---

## 6. 识别性能瓶颈：算力受限还是显存受限

> ## 6. Identifying Performance Bottlenecks: Compute-Bound vs. Memory-Bound

通过在单次重放中同时查询多项底层硬件吞吐指标 (包括 `sm__throughput` 与 `dram__throughput` )，我们能够明确判断算子内核究竟是受限于 GPU 的计算能力，还是受限于显存的带宽吞吐瓶颈。

> By querying multiple hardware metrics simultaneously (`sm__throughput` and `dram__throughput`), we can determine whether a kernel is bound by compute capability or memory bandwidth.

```python
BOUND_METRICS = ["gpu__time_duration.sum",
                 "sm__throughput.avg.pct_of_peak_sustained_elapsed",
                 "dram__throughput.avg.pct_of_peak_sustained_elapsed"]
 
@nsight.analyze.kernel(metrics=BOUND_METRICS, runs=3, thermal_mode="off", verbosity=SILENT)
def what_limits(n: int) -> None:
    a = torch.randn(n, n, device="cuda").half()
    x = torch.randn(64 * 2 ** 20, device="cuda")
    s = torch.randn(8192, 1024, device="cuda")
    with nsight.annotate("fp16 matmul 4096"):
        _ = a @ a
    with nsight.annotate("x * 2 (256 MB)"):
        _ = x * 2.0
    with nsight.annotate("softmax 8192x1024"):
        _ = torch.softmax(s, dim=-1)
 
@section("6. Compute-bound or memory-bound? Three metrics from one replayed kernel")
def bound():
    df = what_limits(4096).to_dataframe()
    tab = df.pivot(index="Annotation", columns="Metric", values="AvgValue")
    tab = tab.rename(columns={"gpu__time_duration.sum": "ms",
                              "sm__throughput.avg.pct_of_peak_sustained_elapsed": "SM % of peak",
                              "dram__throughput.avg.pct_of_peak_sustained_elapsed": "DRAM % of peak"})
    tab["ms"] = tab["ms"] / 1e6
    tab["limited by"] = np.where(tab["SM % of peak"] > tab["DRAM % of peak"], "compute", "memory")
    print(textwrap.indent(tab.to_string(float_format=lambda v: f"{v:,.2f}"), "  "))
    return "Analyzed compute vs memory bottlenecks successfully."
 
bound()
```

---

## 7. 通过显存访问量量化算子融合效果

> ## 7. Measuring Kernel Fusion via Memory Traffic

算子融合的核心优势在于消除了中间临时数据在全局显存中的往返读写开销。借助 `dram__bytes_read.sum` 和 `dram__bytes_write.sum` 这两项指标，我们可以精确量化如 `torch.addcmul` 等融合算子相较于未融合表达式所带来的显存访问效率提升。

> Kernel fusion eliminates intermediate global memory roundtrips. Using `dram__bytes_read.sum` and `dram__bytes_write.sum`, we can quantify the memory efficiency gains of operations like `torch.addcmul` compared to unfused expressions.

```python
BYTES = ["gpu__time_duration.sum", "dram__bytes_read.sum", "dram__bytes_write.sum"]
 
@nsight.analyze.kernel(metrics=BYTES, runs=5, thermal_mode="off", verbosity=SILENT,
                       combine_kernel_metrics=lambda x, y: x + y)
def fusion(n: int) -> None:
    a, b, c = (torch.randn(n, device="cuda") for _ in range(3))
    with nsight.annotate("a + b * c (unfused)"):
        _ = a + b * c
    with nsight.annotate("torch.addcmul (fused)"):
        _ = torch.addcmul(a, b, c)
 
@section("7. Kernel fusion, measured in bytes: combine_kernel_metrics")
def fused():
    n = 32 * 2 ** 20
    df = fusion(n).to_dataframe()
    tab = df.pivot(index="Annotation", columns="Metric", values="AvgValue")
    tab = pd.DataFrame({"ms": tab["gpu__time_duration.sum"] / 1e6,
                        "MB read": tab["dram__bytes_read.sum"] / 2 ** 20,
                        "MB written": tab["dram__bytes_write.sum"] / 2 ** 20})
    print(textwrap.indent(tab.to_string(float_format=lambda v: f"{v:,.1f}"), "  "))
    u, f = tab.loc["a + b * c (unfused)"], tab.loc["torch.addcmul (fused)"]
    return f"fusion: {u['ms'] / f['ms']:.2f}x faster"
 
fused()
```

---

## 8. 自定义信息收集器与温度控制

> ## 8. Custom Information Collectors & Thermal Control

在 1.1 版本中，Nsight Python 引入了实验性的元数据收集器机制，允许用户在每次性能运行期间按需轮询自定义硬件指标 (例如通过 NVML 获取实时的 SM 时钟频率或 GPU 核心温度)。

> Version 1.1 introduces experimental metadata collectors to poll custom hardware parameters (such as SM clock frequencies or temperatures via NVML) per run.

```python
import pynvml
 
pynvml.nvmlInit()
NVML = pynvml.nvmlDeviceGetHandleByIndex(0)
 
@nsight.experimental.collect(scope=nsight.CollectionScope.ONCE)
def driver_version(*args):
    return pynvml.nvmlSystemGetDriverVersion()
 
@nsight.experimental.collect(scope=nsight.CollectionScope.RUN)
def sm_clock_mhz(*args):
    return pynvml.nvmlDeviceGetClockInfo(NVML, pynvml.NVML_CLOCK_SM)
 
@nsight.experimental.collect(scope=nsight.CollectionScope.RUN)
def gpu_temp_c(*args):
    return pynvml.nvmlDeviceGetTemperature(NVML, pynvml.NVML_TEMPERATURE_GPU)
 
def make_heat_body():
    def heat(n: int) -> None:
        a = torch.randn(n, n, device="cuda").half()
        with nsight.annotate("fp16 matmul"):
            _ = a @ a
    return heat
 
@section("8. Custom info collectors and thermal control (experimental API)")
def collectors():
    out = {}
    for mode in ("off", "auto"):
        bench = nsight.analyze.kernel(configs=[4096], runs=10, thermal_mode=mode, thermal_timeout=60,
                                      info_collectors=[driver_version, sm_clock_mhz, gpu_temp_c],
                                      verbosity=SILENT, output_prefix=f"/content/nspy_thermal_{mode}/",
                                      output_csv=True)(make_heat_body())
        try:
            df = bench().to_dataframe()
            out[mode] = df.iloc[0]
            print(f"  thermal_mode={mode!r}: {out[mode]['AvgValue'] / 1e6:.3f} ms")
        except Exception as e:
            print(f"  thermal_mode={mode!r}: failed -> {e}")
    return "Collectors executed successfully."
 
collectors()
```

---

## 9. 实验性 CUPTI 后端对比 Nsight Compute

> ## 9. The Experimental CUPTI Backend vs. Nsight Compute

全新的 CUPTI 后端基于底层 CUPTI 活动接口 (Activity API) 实现，能够在不需要 Nsight Compute 繁重内核重放周期的前提下，以极低的额外开销直接剖析算子内核的执行耗时。

> The new CUPTI backend provides lower-overhead kernel duration profiling via the CUPTI activity API without requiring heavy Nsight Compute kernel replay cycles.

```python
CUPTI_SCRIPT = r'''
import os, json, time
os.environ["NSPY_NCU_INIT_AT_IMPORT"] = "0"
import nsight
nsight.activate(nsight.Tool.CUPTI)
import torch
@nsight.analyze.kernel(configs=[512, 1024, 2048, 4096], runs=10, thermal_mode="off",
                       verbosity=nsight.VerbosityLevel.SILENT, combine_kernel_metrics=lambda x, y: x + y)
def matmul(n):
    a = torch.randn(n, n, device="cuda")
    b = torch.randn(n, n, device="cuda")
    with nsight.annotate("matmul"):
        _ = a @ b
t0 = time.time()
df = matmul().to_dataframe()
wall = time.time() - t0
nsight.deactivate()
print(json.dumps({"wall": wall, "rows": df[["n", "AvgValue", "RelativeStdDevPct"]].to_dict("records")}))
'''
 
@section("9. The experimental CUPTI backend, in its own process, against Nsight Compute")
def cupti_vs_ncu():
    if not CUPTI_EXTRA:
        return "cupti-python could not be installed."
    with open("/content/cupti_matmul.py", "w") as f:
        f.write(CUPTI_SCRIPT)
    env = {k: v for k, v in os.environ.items() if k not in ("NVTX_INJECTION64_PATH", "NV_COMPUTE_PROFILER_PERFWORKS_DIR", "NV_COMPUTE_PROFILER_IN_PROCESS")}
    env["PYTHONPATH"] = CUPTI_DIR + os.pathsep + env.get("PYTHONPATH", "")
    p = subprocess.run([sys.executable, "/content/cupti_matmul.py"], capture_output=True, text=True, env=env, timeout=900)
    print(f"  CUPTI execution return code: {p.returncode}")
    return f"CUPTI subprocess completed with exit code {p.returncode}"
 
cupti_vs_ncu()
```

---

## 10. 保存性能分析证据：报告与原始 CSV 日志

> ## 10. Archiving Evidence: Reports and Raw CSV Logs

性能剖析会话会生成非常全面的输出结果，包括汇总整理后的 CSV 表格、每次运行的原始细节日志，以及完全兼容 Nsight Compute 桌面图形界面 (GUI) 的 `.ncu-rep` 报告文件。

> Profiling sessions produce comprehensive outputs, including aggregated processed CSVs, raw per-run logs, and `.ncu-rep` files compatible with the full Nsight Compute desktop GUI.

```python
@section("10. Keep the evidence: CSVs and the full Nsight Compute report")
def evidence():
    files = sorted(glob.glob("/content/nspy_thermal_off/*"))
    for f in files:
        print(f"  {os.path.basename(f):60s} {os.path.getsize(f) / 1024:9.1f} KB")
    import ncu_report
    rep_path = next((f for f in files if f.endswith(".ncu-rep")), None)
    if rep_path is None:
        return "No .ncu-rep report file found."
    rep = ncu_report.load_report(rep_path)
    print(f"\n  Successfully loaded .ncu-rep report containing {rep.num_ranges()} range(s).")
    return f"Report loaded successfully with {rep.num_ranges()} ranges."
 
evidence()
```

---

## 总结

> ## Conclusion

Nsight Python 将底层性能剖析结果直接封装为直观的 Python 原生数据结构，大幅降低了 GPU 算子内核优化的门槛。只要遵循最佳工程实践——例如在初始化 CUDA 之前优先导入 `nsight` 模块、根据评测目标合理配置缓存与时钟策略、利用置信区间过滤测试波动——开发者便无需离开熟悉的 Python 研发环境，即可快速诊断显存带宽瓶颈、量化评估算子融合增益，并精准采集各项微架构硬件指标。

> Nsight Python simplifies GPU kernel optimization by moving profiling insights directly into Python data structures. By following best practices—such as importing `nsight` prior to initializing CUDA, configuring cache/clock policies intentionally, and leveraging confidence intervals—developers can rapidly diagnose memory bottlenecks, evaluate kernel fusion, and collect precise hardware metrics without stepping outside their Python workflows.

欢迎点击 **[完整代码链接](https://github.com/MARKTECHPOST-AI-MEDIA-INC/AI-Agents-Projects-Tutorials/blob/main/Deep%2>)** 查阅实战脚本。本项目的所有技术荣誉均归属于该项目的研发团队。欢迎关注我们的 **[Twitter](https://x.com/intent/follow?screen_name=marktechpost)** 并加入拥有 15 万+开发者的 **[机器学习 Reddit 社区](https://www.reddit.com/r/machinelearningnews/)**。

> Check out the **[FULL CODES here](https://github.com/MARKTECHPOST-AI-MEDIA-INC/AI-Agents-Projects-Tutorials/blob/main/Deep%2>)**. All credit goes to the researchers of this project. Feel free to follow us on **[Twitter](https://x.com/intent/follow?screen_name=marktechpost)** and join our **[150k+ ML SubReddit](https://www.reddit.com/r/machinelearningnews/)**.
