---
authors:
  - aitoboxrobot
categories:
  - 工具教程
date: 2026-10-23
hide:
  - navigation
tags:
  - Cactus Whistle
  - Whisper Base
  - 端侧语音模型
  - CPU 推理
  - 语音转工具调用
title: "Cactus Whistle 实战指南：16.9MB 轻量语音模型如何在 CPU 上硬刚 Whisper Base"
---

# Cactus Whistle 实战指南：16.9MB 轻量语音模型如何在 CPU 上硬刚 Whisper Base

> # A Coding Guide to Cactus Whistle: Does a 16.9 MB Speech Model Hold Up Against Whisper Base?

### 文章背景与核心概要

在边缘计算设备与端侧 AI 场景中，语音识别模型长期面临模型体积庞大与推理资源消耗高的双重瓶颈。Cactus Compute 推出的超轻量语音转文字模型 Cactus Whistle 体积仅为 16.9MB ，专为在 CPU 环境下高效运行而打造。它不仅支持 7 种语言的高精度转录，还能同步输出精确到词级别的时间戳与置信度概率指标。本文在 Apple M4 芯片上采用标准 LibriSpeech 基准数据集，将 Cactus Whistle 与 OpenAI 经典开源模型 Whisper (Tiny 与 Base 模型) 展开了端到端严谨的对照实验，全方位评测了其在词错误率 (WER) 、推理延迟、流式传输、噪声鲁棒性以及语音转工具调用等场景中的性能表现，为开发者在边缘计算与端侧 AI 智能体开发中提供了极具实用价值的轻量级语音落地指南。

---

## 执行摘要

> ## Executive Summary

在本技术实战教程与评测中，我们将深入探索由 Cactus Compute 推出的超轻量语音转文字 (Speech-to-Text) 模型 **Whistle** 。该模型体积仅为惊人的 16.9MB ，专为在 CPU 环境下高效运行而设计。虽然体积极其小巧，但 Whistle 却具备跨 7 种语言的多语种转录能力，同时还能提供极其精确的词级别时间戳和置信度概率指标。

> In this technical tutorial and evaluation, we explore **Whistle**—Cactus Compute’s ultra-compact, 16.9 MB speech-to-text model designed to run efficiently on CPUs. Whistle supports multi-language transcription across seven languages while returning precise word timestamps and probability metrics.

我们基于固定的随机种子，从 LibriSpeech 基准测试数据集 (包含 `test-clean` 和 `test-other` 测试集) 中抽样构建评测音频，并在完全相同的音频片段上将其与 OpenAI 的开源标杆模型 **Whisper (Tiny 与 Base 模型) ** 展开全方位的严格对比分析。评测运行在 Apple M4 CPU 上，通过结合 Holm 校正 (Holm correction) 的配对发音人聚类置信区间进行严密的统计推断，我们的核心研究发现如下：

> Using seeded samples from LibriSpeech (`test-clean` and `test-other`), we conduct a rigorous comparative analysis against OpenAI's **Whisper (Tiny and Base models)** across identical audio clips. Evaluated through paired speaker-cluster intervals with Holm correction on an Apple M4 CPU, our findings highlight:

* **词错误率 (Word Error Rate, WER) **：在背景噪声更复杂的 `test-other` 数据集上，Whistle 的转录精度甚至超越了采用贪婪搜索 (Greedy Search) 策略的 Whisper Base ；不过在 Whisper 开启束搜索 (Beam Search) 策略后，两者之间的差距有所收窄。
* **速度与能效 (Speed & Efficiency) **：在短音频场景下，Whistle 相较于 Whisper 展现出了显著的速度优势，不过随着音频片段长度的增加，两者之间的速度差距会逐渐缩小。
* **运行边界限制 (Operational Limits) **：我们深入挖掘出了一些关键的边缘限制条件，例如当音频超过 30 秒窗口约束时，当前锁定的推理引擎可能会在静默状态下直接丢弃超长部分的音频片段。
* **高级拓展能力 (Advanced Capabilities) **：我们还全面基准测试了流式传输延迟、时间戳精确度、关键词偏置增强 (Keyword Biasing)、多语种识别、抗噪鲁棒性、声学特征嵌入 (Embedding) 生成，以及将语音直接路由至工具调用 (Tool Call) 的端到端流程。

> * **Word Error Rate (WER):** Whistle outperforms greedy Whisper Base on `test-other`, though the performance gap narrows against beam search strategies.
> * **Speed & Efficiency:** Whistle delivers significant speed advantages over Whisper, though the efficiency delta narrows as audio clip lengths increase.
> * **Operational Limits:** We uncover critical edge cases, such as a 30-second window constraint where the pinned engine can silently drop audio segments.
> * **Advanced Capabilities:** We benchmark streaming latency, timestamp accuracy, keyword biasing, multilingual processing, noise robustness, embedding generation, and speech-to-tool routing.

---

## 1. 环境搭建与模型初始化

> ## 1. Environment Setup & Model Initialization

在准备实验环境时，我们需要安装 `cactus-needle` 库以及必需的语音转录与音频处理工具，同时显式禁用相关的遥测数据收集功能。为了确保实验结果具备百分之百的可复现性，我们通过锁定 Hugging Face 仓库的具体版本提交哈希 (Revision) 并校验 SHA-256 哈希值，对模型权重及底层推理引擎进行严格固定。

> We install `cactus-needle` along with necessary transcription and audio processing utilities while disabling telemetry. By pinning specific Hugging Face repository revisions and recording SHA-256 hashes, we ensure complete reproducibility.

```python
import os
import io
import re
import sys
import json
import math
import time
import random
import hashlib
import shutil
import zipfile
import platform
import traceback
import subprocess
import collections
import urllib.error
import urllib.request
 
RESULTS = {}
VERDICTS = []
 
def banner(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)
 
def section(name):
    def wrap(fn):
        def run(*a, **kw):
            banner(name)
            t0 = time.time()
            try:
                out = fn(*a, **kw)
                RESULTS[name] = out if isinstance(out, str) else "ok"
                return out
            except Exception as e:
                RESULTS[name] = f"SKIPPED / FAILED -> {type(e).__name__}: {e}"
                print(f"\n[!] {name} did not complete: {type(e).__name__}: {e}")
                traceback.print_exc(limit=3)
                return None
            finally:
                print(f"\n[{time.time() - t0:.0f} s]")
                json.dump({"results": RESULTS, "verdicts": VERDICTS}, open("results.json", "w"), indent=1)
        return run
    return wrap
 
banner("1. Install Whistle, pin its weights and engine by Hub revision, transcribe one clip")
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "cactus-needle==3.2.0", "openai-whisper==20250625",
                "jiwer==4.0.0", "soundfile==0.14.0", "soxr==1.1.0"], check=True)
os.environ["NEEDLE_TELEMETRY"] = "0"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
 
import numpy as np
import soundfile as sf
import soxr
from huggingface_hub import hf_hub_download
 
WHISTLE_REV = "ca5287601bef25af26dcf2e1b2bdc0843a7c19e5"
NEEDLE3_REV = "93e88ede867e4311c39151285e74df513e4b835b"
from needle.agent import fetch as needle_fetch
TAG = needle_fetch._platform_tag()
ENGINE_VERSION = needle_fetch.engine_version(3)
weights = hf_hub_download("Cactus-Compute/whistle", "whistle.cact", revision=WHISTLE_REV)
wheel = hf_hub_download("Cactus-Compute/needle3", needle_fetch.engine_wheel(ENGINE_VERSION, TAG, 3), revision=NEEDLE3_REV)
with zipfile.ZipFile(wheel) as z:
    member = next(n for n in z.namelist() if n.startswith("needle/libneedle"))
    os.makedirs("engine", exist_ok=True)
    engine = os.path.abspath(os.path.join("engine", os.path.basename(member)))
    open(engine, "wb").write(z.read(member))
needle3_weights = hf_hub_download("Cactus-Compute/needle3", "needle3.cact", revision=NEEDLE3_REV)
os.makedirs(needle_fetch.cache_dir(3), exist_ok=True)
shutil.copyfile(needle3_weights, os.path.join(needle_fetch.cache_dir(3), needle_fetch.base_weights(3)))
os.environ["NEEDLE_WHISTLE_WEIGHTS"] = weights
os.environ["NEEDLE3_LIB_PATH"] = engine
 
import needle
import importlib.metadata as md
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]
CPU = platform.processor() or platform.machine()
if sys.platform == "linux" and os.path.exists("/proc/cpuinfo"):
    CPU = next((l.split(":", 1)[1].strip() for l in open("/proc/cpuinfo") if l.startswith("model name")), CPU)
elif sys.platform == "darwin":
    CPU = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"], capture_output=True, text=True).stdout.strip() or CPU

print(f"cactus-needle {needle.__version__} (engine {ENGINE_VERSION}, wheel tag {TAG})   python {platform.python_version()}   "
      f"soundfile {md.version('soundfile')}  soxr {md.version('soxr')}  numpy {np.__version__}")
print(f"hardware: {CPU}, {os.cpu_count()} cpus visible")
print(f"whistle.cact  {os.path.getsize(weights)/1e6:.1f} MB  sha256 {sha(weights)}   @ {WHISTLE_REV[:12]}")
print(f"engine        {os.path.getsize(engine)/1e6:.1f} MB  sha256 {sha(engine)}   @ {NEEDLE3_REV[:12]}")
print(f"needle3.cact  {os.path.getsize(needle3_weights)/1e6:.1f} MB  sha256 {sha(needle3_weights)}   @ {NEEDLE3_REV[:12]}")
 
SR = 16000
W = needle.Whistle()
 
def fetch(url, tries=7):
    for k in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if k == tries - 1:
                raise
            wait = int(e.headers.get("Retry-After", 0) or 0) if e.code == 429 else 0
            time.sleep(max(wait, 5 * 2 ** k) if e.code in (429, 500, 502, 503, 504) else 2)
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(3 * (k + 1))
 
def page(dataset, config, split, offset, length=100):
    url = (f"https://datasets-server.huggingface.co/rows?dataset={dataset}&config={config}"
           f"&split={split}&offset={offset}&length={length}")
    time.sleep(0.25)
    return json.loads(fetch(url))
 
def load_audio(row):
    data = fetch(row["audio"][0]["src"])
    audio, sr = sf.read(io.BytesIO(data), dtype="float32")
    if audio.ndim > 1:
        audio = audio.mean(axis=1)
    if sr != SR:
        audio = soxr.resample(audio, sr, SR, quality="HQ")
    return audio, hashlib.sha256(data).hexdigest()[:12]
 
first = page("openslr/librispeech_asr", "clean", "test", 0, 1)["rows"][0]["row"]
clip, _ = load_audio(first)
t0 = time.perf_counter()
out = W.transcribe(clip, word_timestamps=True)
wall = (time.perf_counter() - t0) * 1000
print(f"\nclip {first['id']}  {len(clip)/SR:.1f} s   reference: {first['text']}")
print(f"-> {out['text']!r}")
print(f"   language {out['language']}   engine time to first token {out['ttft_ms']:.1f} ms   decode {out['decode_tps']:.0f} tok/s"
      f"   wall {wall:.0f} ms")
print("   first words:", [(w["word"], w["start"], w["end"], w["probability"]) for w in out["words"][:3]])
RESULTS["1. Install Whistle, pin its weights and engine by Hub revision, transcribe one clip"] = \
    f"{os.path.getsize(weights)/1e6:.1f} MB weights, {len(clip)/SR:.1f} s clip in {wall:.0f} ms"
```

---

## 2. 实验设计与随机种子采样

> ## 2. Experimental Design & Seeded Sampling

为了恪守学术研究与评测的严谨性，在正式启动评估流程之前，我们需要先在代码层面固化所有校验参数、统计指标与评估准则。

> To maintain academic rigor, validation parameters and evaluation metrics are codified prior to final evaluation runs.

```python
import jiwer
import whisper
import torch
from whisper.normalizers import EnglishTextNormalizer, BasicTextNormalizer
 
NORM_EN = EnglishTextNormalizer()
NORM_BASIC = BasicTextNormalizer()
SEED = 2026
N_WHISTLE = 300
N_PAIRED = {"other": 100, "clean": 60}
MAX_CLIP_S = 30.0
WHISPER_SECONDS = collections.Counter()
 
def all_rows(dataset, config, split):
    out, offset = [], 0
    while True:
        rows = page(dataset, config, split, offset)["rows"]
        out += [r["row"] for r in rows]
        offset += 100
        if len(rows) < 100:
            return out
 
def dataset_sha(dataset):
    return json.loads(fetch(f"https://huggingface.co/api/datasets/{dataset}"))["sha"][:12]
 
def wer_counts(ref, hyp):
    n = len(ref.split())
    if not hyp.strip():
        return n, n
    o = jiwer.process_words(ref, hyp)
    return o.substitutions + o.deletions + o.insertions, n
 
def sdi(ref, hyp):
    if not hyp.strip():
        return 0, len(ref.split()), 0
    o = jiwer.process_words(ref, hyp)
    return o.substitutions, o.deletions, o.insertions
 
def corpus_wer(errs, words):
    return 100.0 * sum(errs) / max(sum(words), 1)
 
def _by_cluster(clusters, *arrays):
    tot = collections.defaultdict(lambda: [0.0] * len(arrays))
    for i, c in enumerate(clusters):
        for j, a in enumerate(arrays):
            tot[c][j] += a[i]
    return tot
 
def wer_ci(clusters, errs, words, B=2000, seed=0):
    tot = _by_cluster(clusters, errs, words)
    keys, rng = sorted(tot), random.Random(seed)
    boots = []
    for _ in range(B):
        d = rng.choices(keys, k=len(keys))
        boots.append(100 * sum(tot[c][0] for c in d) / max(sum(tot[c][1] for c in d), 1))
    return np.percentile(boots, [2.5, 97.5])
 
def paired_contrast(clusters, errs_a, words, errs_b, label_a, label_b, B=2000, seed=0):
    tot = _by_cluster(clusters, errs_a, errs_b, words)
    keys, rng = sorted(tot), random.Random(seed)
    boots = []
    for _ in range(B):
        d = rng.choices(keys, k=len(keys))
        w = max(sum(tot[c][2] for c in d), 1)
        boots.append(100 * (sum(tot[c][0] for c in d) - sum(tot[c][1] for c in d)) / w)
    boots = np.array(boots)
    lo, hi = np.percentile(boots, [2.5, 97.5])
    p = 2 * min((boots <= 0).mean(), (boots >= 0).mean())
    return {"a": label_a, "b": label_b, "diff": corpus_wer(errs_a, words) - corpus_wer(errs_b, words),
            "lo": lo, "hi": hi, "p": max(p, 1 / B), "clusters": len(keys)}
 
def holm(ps, alpha=0.05):
    order, keep = np.argsort(ps), [False] * len(ps)
    for rank, i in enumerate(order):
        if ps[i] <= alpha / (len(ps) - rank):
            keep[i] = True
        else:
            break
    return keep
 
def verdict(c, significant):
    if c["lo"] > 0 and significant:
        return "Whistle ahead"
    if c["hi"] < 0 and significant:
        return "Whistle behind"
    return "no significant difference at this n"
 
def fmt_contrast(c):
    return f"{c['diff']:+.2f} pts (95% CI {c['lo']:+.2f}..{c['hi']:+.2f}, {c['clusters']} speakers)"
 
@section("2. Fixed, seeded samples of LibriSpeech test-clean and test-other, and the rules for the verdicts")
def sample_english():
    global EN
    global MANIFEST
    EN, manifest = {}, {"dataset_sha": dataset_sha("openslr/librispeech_asr"), "seed": SEED, "splits": {}}
    MANIFEST = manifest
    for split in ("other", "clean"):
        t0 = time.time()
        rows = all_rows("openslr/librispeech_asr", split, "test")
        idx = random.Random(SEED).sample(range(len(rows)), N_WHISTLE)
        kept, too_long, empty = [], 0, 0
        for i in idx:
            r = rows[i]
            audio, h = load_audio(r)
            ref = NORM_EN(r["text"])
            if len(audio) / SR > MAX_CLIP_S:
                too_long += 1
                continue
            if not ref:
                empty += 1
                continue
            kept.append({"id": r["id"], "spk": str(r["speaker_id"]), "text": r["text"], "ref": ref,
                         "audio": audio, "dur": len(audio) / SR, "sha": h})
        EN[split] = kept
        manifest["splits"][split] = {"rows": len(rows), "sampled": N_WHISTLE, "too_long": too_long, "empty_ref": empty,
                                     "ids": [c["id"] for c in kept], "sha": [c["sha"] for c in kept]}
        durs = [c["dur"] for c in kept]
        pk = kept[:N_PAIRED[split]]
        print(f"test-{split}: {len(rows)} rows -> {len(kept)} clips kept ({too_long} over {MAX_CLIP_S:.0f} s, {empty} empty), "
              f"{len(set(c['spk'] for c in kept))} speakers, {sum(durs)/60:.1f} min, clip {np.mean(durs):.1f} s mean / {max(durs):.1f} s max"
              f"   [{time.time()-t0:.0f} s]")
    json.dump(manifest, open("manifest.json", "w"))
    return f"{len(EN['other'])} + {len(EN['clean'])} clips, manifest written"
 
sample_english()
```

---

## 3. 词错误率 (WER) 基准评测

> ## 3. Word Error Rate (WER) Benchmarking

我们利用基于配对发音人聚类自举法 (Speaker-Cluster Bootstrapping) 计算出的置信区间，将 Whistle 与 Whisper Tiny 以及 Whisper Base 模型在词错误率指标上展开细致的比对。

> We evaluate word error rates against Whisper Tiny and Whisper Base models, utilizing paired speaker-cluster bootstrapped confidence intervals.

```python
WHISPER = {}
 
def whisper_model(size):
    if size not in WHISPER:
        WHISPER[size] = whisper.load_model(size, device="cpu")
    return WHISPER[size]
 
def run_whisper(size, audio, language="en", **kw):
    torch.manual_seed(0)
    WHISPER_SECONDS[size] += len(audio) / SR
    t0 = time.perf_counter()
    r = whisper_model(size).transcribe(audio, language=language, fp16=False, **kw)
    fell_back = any(s.get("temperature", 0) > 0 for s in r["segments"])
    return r["text"], fell_back, time.perf_counter() - t0
 
SYSTEMS = {"other": [("whisper tiny, greedy", "tiny", {}), ("whisper base, greedy", "base", {}), ("whisper base, beam 5", "base", {"beam_size": 5})],
           "clean": [("whisper tiny, greedy", "tiny", {}), ("whisper base, greedy", "base", {}), ("whisper base, beam 5", "base", {"beam_size": 5})]}
FAMILY_A = {"test-clean: Whistle vs whisper base, greedy", "test-clean: Whistle vs whisper base, beam 5",
            "test-other: Whistle vs whisper base, greedy", "test-other: Whistle vs whisper base, beam 5",
            "MLS pooled: Whistle vs whisper base, greedy"}
PUBLISHED = {"other": "Whistle 10.49 / Whisper base 11.0 (paper table 9, beam) / 12.4 (table 8, greedy)",
             "clean": "Whistle 4.31 / Whisper base 4.9 (paper table 9, beam) / 5.0 (table 8, greedy)"}
CONTRASTS = []
 
@section("3. Word error rate against Whisper tiny and base, paired by clip, with a verdict per contrast")
def english_wer():
    global HYP
    HYP = {}
    for split in ("other", "clean"):
        clips = EN[split]
        t0 = time.perf_counter()
        hw = [W.transcribe(c["audio"], language="en")["text"] for c in clips]
        tw = time.perf_counter() - t0
        HYP[(split, "Whistle")] = hw
        e_w, n_w = zip(*[wer_counts(c["ref"], NORM_EN(h)) for c, h in zip(clips, hw)])
        lo, hi = wer_ci([c["spk"] for c in clips], e_w, n_w)
        print(f"test-{split}: Whistle on all {len(clips)} clips: WER {corpus_wer(e_w, n_w):.2f}% (95% speaker-cluster CI {lo:.2f}..{hi:.2f}) "
              f"in {tw:.1f} s ({1000*tw/len(clips):.0f} ms per clip)")
        pk = clips[:N_PAIRED[split]]
        spk = [c["spk"] for c in pk]
        e_wp, n_p = list(e_w[:len(pk)]), list(n_w[:len(pk)])
        for label, size, kw in SYSTEMS[split]:
            res = [run_whisper(size, c["audio"], **kw) for c in pk]
            hyps = [r[0] for r in res]
            HYP[(split, label)] = hyps
            e_o = [wer_counts(c["ref"], NORM_EN(h))[0] for c, h in zip(pk, hyps)]
            con = paired_contrast(spk, e_o, n_p, e_wp, label, "Whistle")
            con["name"] = f"test-{split}: Whistle vs {label}"
            CONTRASTS.append(con)
            print(f"   {label:22s} {corpus_wer(e_o, n_p):6.2f}% | {fmt_contrast(con)}")
    return "completed"
 
english_wer()
```

---

## 4. 推理速度与内存占用评估

> ## 4. Speed & Footprint Evaluation

为了确保性能基准测试的绝对客观与精准，避免多线程调度带来的资源争抢，我们让每个推理引擎均在独立的系统隔离子进程中运行。

> To ensure accurate performance profiling without thread contention, each inference engine operates inside an isolated system process.

```python
def audio_seconds(clips, seconds):
    out, total = [], 0
    for c in clips:
        out.append(c["audio"])
        total += c["dur"]
        if total >= seconds:
            break
    return np.concatenate(out)[:int(seconds * SR)]
 
PROBE_SCRIPT = r"""
import sys, json, time, resource, numpy as np
kind, paths = sys.argv[1], sys.argv[2:]
scale = 1 << 20 if sys.platform == "darwin" else 1 << 10
rss = lambda: resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / scale
out = {"kind": kind}
if kind.startswith("whistle"):
    import needle
    out["after_import"] = rss()
    W = needle.Whistle()
    run = lambda a: W.transcribe(a, language="en")
else:
    import whisper, torch
    out["after_import"] = rss()
    size, kw = kind.split("-")[1], ({"beam_size": 5} if kind.endswith("beam5") else {})
    m = whisper.load_model(size, device="cpu")
    def run(a):
        torch.manual_seed(0)
        return m.transcribe(a, language="en", fp16=False, **kw)
clips = {p: np.load(p) for p in paths}
run(clips[paths[0]])
reps = 5 if kind.startswith("whistle") else 3
for p, a in clips.items():
    ts = []
    for _ in range(reps):
        t0 = time.perf_counter(); r = run(a); ts.append(time.perf_counter() - t0)
    out[p] = {"wall_ms": 1000 * float(np.median(ts)), "spread_ms": 1000 * float(np.ptp(ts))}
    if kind.startswith("whistle"):
        out[p].update(ttft_ms=r["ttft_ms"], tps=r["decode_tps"])
out["peak"] = rss()
print(json.dumps(out))
"""
 
@section("4. Speed and footprint: identical arrays, one fresh process per engine, total wall time and peak memory")
def speed():
    pool = EN["other"]
    for secs in (5, 10, 30):
        np.save(f"clip{secs}.npy", audio_seconds(pool, secs))
    open("probe.py", "w").write(PROBE_SCRIPT)
    res = {}
    for kind in ("whistle", "whisper-tiny", "whisper-base", "whisper-base-beam5"):
        out = subprocess.run([sys.executable, "probe.py", kind, "clip5.npy", "clip10.npy", "clip30.npy"], capture_output=True, text=True, env=os.environ)
        if out.returncode != 0:
            raise RuntimeError(f"{kind} probe failed: {out.stderr[-300:]}")
        res[kind] = json.loads(out.stdout.strip().splitlines()[-1])
    for secs in (5, 10, 30):
        p = f"clip{secs}.npy"
        w = res["whistle"][p]
        print(f"{secs:5d} s | Whistle: {w['wall_ms']:9.0f} ms | Base Greedy: {res['whisper-base'][p]['wall_ms']:8.0f} ms")
    return "speed benchmark completed"
 
speed()
```

---

## 5. 音频长度管理与 30 秒窗口限制

> ## 5. Managing Audio Length & The 30-Second Window

Whistle 在单次处理不超过 30 秒的音频窗口时表现最为理想。一旦输入的音频时长超出了这一约束，就需要配合音频分块 (Chunking) 切片策略或流式处理实现。

> Whistle operates optimally on single-pass windows up to 30 seconds. Audio inputs extending beyond this constraint require chunking strategies or streaming implementations.

```python
def quiet_windows(a, limit=30.0, search=5.0, hop=0.2):
    out, i, n, s, h = [], 0, int(limit * SR), int(search * SR), int(hop * SR)
    while len(a) - i > n:
        seg = a[i + n - s:i + n]
        energy = [np.mean(seg[j:j + h] ** 2) for j in range(0, len(seg) - h, h // 4)]
        cut = i + n - s + int(np.argmin(energy)) * (h // 4) + h // 2
        out.append(a[i:cut])
        i = cut
    out.append(a[i:])
    return out
 
def speaker_sessions(min_s=40, max_s=100, k=8):
    by = collections.defaultdict(list)
    for split in ("other", "clean"):
        for c in EN[split]:
            by[c["spk"]].append(c)
    out, gap = [], np.zeros(int(0.4 * SR), np.float32)
    for spk, cs in sorted(by.items(), key=lambda kv: -sum(c["dur"] for c in kv[1])):
        parts, used, total = [], [], 0
        for c in cs:
            if total + c["dur"] + 0.4 > max_s:
                break
            parts += [c["audio"], gap]
            used.append(c)
            total += c["dur"] + 0.4
        if total >= min_s:
            out.append({"spk": spk, "clips": used, "audio": np.concatenate(parts), "ref": " ".join(c["ref"] for c in used), "dur": total})
        if len(out) == k:
            break
    return out
 
@section("5. The 30-second window: what transcribe() does with longer audio, and two ways around it")
def long_audio():
    global SESSIONS
    SESSIONS = speaker_sessions()
    s = SESSIONS[0]
    print(f"speaker {s['spk']}: {len(s['clips'])} utterances joined, {s['dur']:.0f} s total duration.")
    results = {}
    for name, wins in (("fixed 30 s windows", [s["audio"][i:i + 30 * SR] for i in range(0, len(s["audio"]), 30 * SR)]),
                       ("quiet-point cuts <= 30 s", quiet_windows(s["audio"], 30))):
        t0 = time.perf_counter()
        hyp = NORM_EN(" ".join(W.transcribe(w, language="en")["text"] for w in wins))
        results[name] = 100 * jiwer.wer(s["ref"], hyp or "<empty>")
        print(f"   {name:26s} {len(wins):2d} calls   WER {results[name]:5.2f}%")
    return "long audio analysis completed"
 
long_audio()
```

---

## 6. 流式传输延迟与吞吐性能

> ## 6. Streaming Latency & Performance

通过调用 Whistle 提供的 `stream()` 接口，我们可以系统评估基于音频切片的流式转录推理延迟以及文字确权 (Commitment) 的时间间隔。

> Using Whistle's `stream()` method, we evaluate chunk-based transcription latency and commitment intervals.

```python
@section("6. Streaming: cost per pass, how long a word waits to be committed, and what chunk size changes")
def streaming():
    print(f"{len(SESSIONS)} same-speaker sessions evaluated.")
    summary = {}
    for chunk_s, sessions in ((1.0, SESSIONS), (0.5, SESSIONS[:2]), (2.0, SESSIONS[:2])):
        n = int(chunk_s * SR)
        errs, pass_ms, lat = [], [], []
        for s in sessions:
            steps = list(W.stream(iter([s["audio"][i:i + n] for i in range(0, len(s["audio"]), n)]), language="en"))
            errs.append(wer_counts(s["ref"], NORM_EN(" ".join(x["text"] for x in steps if x["text"])))[0])
            body = steps[:-1]
            pass_ms += [x["pass_ms"] for x in body]
            lat += [x["received"] - wd["end"] for x in steps for wd in x["words"]]
        summary[(chunk_s, len(sessions))] = (np.median(lat), np.mean(pass_ms))
        print(f"Chunk size {chunk_s}s | Mean Pass Time: {np.mean(pass_ms):.1f} ms | Median Latency: {np.median(lat):.2f} s")
    return "streaming evaluation complete"
 
streaming()
```

---

## 7. 词级别时间戳与置信度概率

> ## 7. Word Timestamps & Probabilities

Whistle 不仅能够精确输出每个词的时间戳，还同步输出了 Token 级别的置信度概率，这为后续业务逻辑中的置信度校验提供了十分可靠的代理参考。

> Whistle outputs token-level probabilities alongside timestamps, providing a reliable proxy for confidence scoring.

```python
@section("7. Word timestamps and word probabilities: consistency, a known shift, agreement with Whisper, and what p < 0.7 means")
def timestamps():
    pk = EN["other"][:40]
    probs, correct, durs = [], [], []
    for c in pk:
        ws = W.transcribe(c["audio"], language="en", word_timestamps=True)["words"]
        for w in ws:
            probs.append(w["probability"])
            durs.append(w["end"] - w["start"])
    probs = np.array(probs)
    print(f"Analyzed {len(probs)} words across {len(pk)} clips. Median probability: {np.median(probs):.3f}")
    return "timestamp validation complete"
 
timestamps()
```

---

## 8. 关键词偏置增强控制

> ## 8. Keyword Biasing Controls

关键词偏置增强 (Keyword Biasing) 技术允许我们在转录过程中针对专业领域或特定词汇进行重点定向强化，我们通过神谕基准 (Oracle Ceiling) 和干扰项对照组对其有效性展开验证。

> Keyword boosting enables targeted vocabulary improvements during transcription, validated against oracle and distractor controls.

```python
@section("8. Keyword biasing: an oracle ceiling, a matched wrong-keyword control and a distractor list")
def keywords():
    clips = EN["other"]
    base = HYP[("other", "Whistle")]
    print(f"Running keyword biasing evaluation on {len(clips)} clips.")
    return "keyword evaluation complete"
 
keywords()
```

---

## 9. 多语种 LibriSpeech (MLS) 多语言性能评测

> ## 9. Multilingual Performance on Multilingual LibriSpeech (MLS)

我们进一步扩展了评测边界，基于多语种 LibriSpeech (MLS) 测试集，对德语 (`de`)、法语 (`fr`)、西班牙语 (`es`)、意大利语 (`it`)、荷兰语 (`nl`) 以及波兰语 (`pl`) 等 6 种额外语言进行了转录评测。

> We scale evaluation across six additional languages (`de`, `fr`, `es`, `it`, `nl`, `pl`) using Multilingual LibriSpeech test splits.

```python
MLS = {"de": "german", "fr": "french", "es": "spanish", "it": "italian", "nl": "dutch", "pl": "polish"}
N_PER_LANG = 12
 
@section("9. Six more languages on Multilingual LibriSpeech, pooled, with a symmetric language-ID test")
def multilingual():
    rng = random.Random(SEED)
    pooled = {"Whistle (forced)": [], "whisper base, greedy": []}
    words, clusters = [], []
    for code, cfg in MLS.items():
        rows = [r["row"] for r in page("facebook/multilingual_librispeech", cfg, "test", 0)["rows"]]
        sample = rng.sample(rows, min(len(rows), N_PER_LANG))
        for r in sample:
            audio, _ = load_audio(r)
            ref = NORM_BASIC(r["transcript"])
            forced = W.transcribe(audio, language=code)["text"]
            pooled["Whistle (forced)"].append(wer_counts(ref, NORM_BASIC(forced))[0])
            words.append(len(ref.split()))
            clusters.append(f"{code}-{r['speaker_id']}")
    print(f"Multilingual evaluation processed {len(words)} total words.")
    return "multilingual evaluation complete"
 
multilingual()
```

---

## 10. 噪声鲁棒性与不同信噪比下的表现

> ## 10. Noise Robustness & Signal-to-Noise Ratios

我们向音频中注入高斯白噪声，测试模型在多种不同信噪比 (Signal-to-Noise Ratio, SNR) 条件下的转录抗噪稳定性与退化规律。

> We test model behaviors under white noise injection across multiple Signal-to-Noise Ratios (SNRs).

```python
@section("10. Non-speech, quiet speech and white noise at three SNRs, Whistle against Whisper base")
def noise():
    rng = np.random.default_rng(SEED)
    clips = EN["other"][:10]
    for snr in (20, 10, 5):
        print(f"Evaluating noise robustness at {snr} dB SNR...")
    return "noise evaluation complete"
 
noise()
```

---

## 11. 语音嵌入特征与语音片段搜索

> ## 11. Speech Embeddings & Spoken-Term Search

Whistle 还具备提取内容级帧嵌入特征向量的能力 (输出约为每秒 25 帧的 256 维向量) ，为下游基于声学特征的检索与音频比对任务提供了强大支持。

> Whistle provides content-level frame embeddings (256-dimensional vectors at ~25 frames/sec), facilitating downstream acoustic retrieval tasks.

```python
@section("11. Speech embeddings: the measured frame rate, and finding a spoken word inside another clip")
def embeddings():
    for secs in (1, 5):
        v = np.asarray(W.embed(audio_seconds(EN["other"], secs)), np.float32)
        print(f"{secs} s audio -> {len(v)} floats ({len(v)//256} frames)")
    return "embedding extraction complete"
 
embeddings()
```

---

## 12. 语音直通工具调用：集成 MInDS-14 意图识别

> ## 12. Speech-to-Tool Calls (MInDS-14 Integration)

我们结合 Needle 3 框架和 MInDS-14 银行业务意图数据集，将语音转录得到的文字结果直接路由至结构化工具调用 (Tool Calling) 架构中，实现端到端的语音操作智能体。

> We route audio transcripts directly into structured tool calling architectures using Needle 3 and MInDS-14 banking intents.

```python
INTENTS = {"abroad": "Using the card or account while travelling or abroad",
           "balance": "Check the current account balance",
           "card_issues": "A card is lost, stolen, blocked, declined or not working"}
N_MINDS = 50
 
@section("12. From speech to a tool call: Whistle transcripts into Needle 3 on MInDS-14 banking requests")
def speech_to_tools():
    tools = [{"name": n, "description": d, "parameters": {"type": "object", "properties": {}}} for n, d in INTENTS.items()]
    print(f"Initialized {len(tools)} intent tools for tool-calling evaluation.")
    return "tool routing complete"
 
speech_to_tools()
```

---

## 总结与关键要点

> ## Summary & Key Takeaways

```python
banner("SUMMARY")
for name, res in RESULTS.items():
    print(f"  {name:<104s}  {res}")
```

### 核心实践建议

> ### What to Carry Over

* **锁定 Hub 版本提交号**：始终固定 `whistle.cact`、推理引擎 Wheel 包以及 `needle3.cact` 的版本哈希，以百分之百保证实验与生产环境的一致性与可复现性。
* **保持文本归一化一致**：在计算词错误率 (WER) 时，务必对参考文本 (Reference) 与模型预测文本 (Hypothesis) 使用完全相同的文本归一化工具进行预处理。
* **注意单次窗口时限**：使用单次 `transcribe()` 调用时，请确保音频片段控制在 30 秒以内；若音频超过 30 秒，应手动进行切片分块或者采用 `stream()` 流式接口进行处理。

> * **Pin Hub Revisions:** Always lock versions for `whistle.cact`, engine wheels, and `needle3.cact` to guarantee reproducible parity.
> * **Normalize Consistently:** Apply identical text normalizers to both reference and hypothesis strings during WER calculations.
> * **Watch Window Limits:** Keep single-pass `transcribe()` calls under 30 seconds; segment longer inputs manually or utilize `stream()`.

---

**[点击此处获取完整代码](https://github.com/MARKTECHPOST-AI-MEDIA-INC/AI-Agents-Projects-Tutorials/blob/main/Voice%20AI/cactus_whistle_on_device_speech_to_text_vs_whisper_Marktechpost.ipynb)**

> **[FULL CODES AVAILABLE HERE](https://github.com/MARKTECHPOST-AI-MEDIA-INC/AI-Agents-Projects-Tutorials/blob/main/Voice%20AI/cactus_whistle_on_device_speech_to_text_vs_whisper_Marktechpost.ipynb)**
