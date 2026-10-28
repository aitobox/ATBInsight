---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-10-29
hide:
- navigation
tags:
- 投机解码
- FlashMap
- 大语言模型
- 连续流模型
- vLLM
- SGLang
title: FlashMap：普林斯顿与 Polymathic AI 联合发布连续流草稿模型，实现 6.14 倍无损解码加速
---
# FlashMap：普林斯顿与 Polymathic AI 联合发布连续流草稿模型，实现 6.14 倍无损解码加速

> # Polymathic AI and Princeton Researchers Release FlashMap, a Flow Map Drafter for 6.14x Faster LLM Decoding

> **Paper:** [arXiv:2610.24365](https://arxiv.org/abs/2610.24365)  
> **Project:** [jshen.net/flashmap](https://jshen.net/flashmap/)  
> **Code:** [GitHub - al-jshen/flashmap](https://github.com/al-jshen/flashmap)  
> **Model:** [Hugging Face Collection](https://huggingface.co/collections/j-shen/flashmap-6ad0feb955bdc30db59769fa)

### 文章背景与核心概要

在大语言模型 (Large Language Model, LLM) 的推理生成中，传统的逐个 Token 串行自回归解码极易受限于 GPU 显存带宽瓶颈，而投机解码 (Speculative Decoding) 虽能通过小型草稿模型 (Drafter) 批量预估候选 Token，但此前基于离散扩散模型的草稿方案往往因对每个位置独立预测（因子化近似假设）而频频遭遇“语义模态崩溃”——例如在面对“New York”与“San Diego”两种高频合理搭配时，容易错误拼凑出“New Diego”从而被目标模型全盘推翻。为了彻底破除这一顽疾，来自 Polymathic AI、Princeton University、USC ISI、NYU 与 Flatiron Institute 的研究团队联合推出了全新草稿模型 **FlashMap**。FlashMap 突破性地摒弃了离散扩散机制，创新引入连续流映射 (Continuous Flow Map) 技术，仅需单次前向传播就能将高斯噪声整体映射为一个连贯的 16-Token 文本块，从底层数学上严密保留了词间语义关联。在 Qwen3-8B 等模型与 GSM8K 等数学基准上，仅凭一个 0.5B 的超轻量草稿头便实现了最高达 **6.14 倍的完全无损加速 (Lossless Speedup)**，并已原生适配 vLLM 与 SGLang 高性能推理引擎，为大模型实时高速推理开辟了全新可能。

---

## 核心摘要

> ## Summary

来自 Polymathic AI、Princeton University、USC ISI、NYU 以及 Flatiron Institute 的研究人员联合推出了 **FlashMap**——这是一种全新的投机解码草稿模型 (Speculative Decoding Drafter)，创新性地使用连续流映射 (Continuous Flow Map) 机制取代了传统的离散扩散模型。FlashMap 通过在单次前向传播中直接将高斯噪声映射为包含 16 个 Token 的文本块，完美保留了各 Token 之间的上下文语义一致性，并在 Qwen3-8B（GSM8K 基准）上取得了最高 **6.14 倍的无损加速 (Lossless Speedup)**。本次开源发布包含了基于 Apache-2.0 协议的 Qwen3-8B 与 Qwen3-4B 模型权重（托管于 Hugging Face），并同步提供了面向 vLLM 与 SGLang 推理引擎的开箱即用插件。

> Researchers from Polymathic AI, Princeton University, USC ISI, NYU, and the Flatiron Institute have introduced **FlashMap**, a novel speculative decoding drafter that replaces discrete diffusion with a continuous flow map. By mapping Gaussian noise to a 16-token block in a single forward pass, FlashMap preserves inter-token consistency and achieves up to a **6.14x lossless speedup** on Qwen3-8B (GSM8K). The release includes Apache-2.0 model weights for Qwen3-8B and Qwen3-4B on Hugging Face, alongside out-of-the-box plugins for vLLM and SGLang.

---

## 核心要点速览

> ## TL;DR

* **模型规模 (Model Size)**：采用 0.5B 参数量的轻量草稿模型（针对 Qwen3-8B 为 500M 参数，针对 Qwen3-4B 为 475M 参数）；单次草拟包含 $K = 16$ 个 Token 的文本块。
* **硬件需求 (Hardware Requirements)**：草稿模型与目标模型共享部署在同一张 GPU 上。在基准评测中，使用单张 NVIDIA H200 NVL 显卡，在并发为 1、精度为 `bf16` 的环境下完成性能测试。
* **综合性能 (Performance)**：在 Qwen3-8B 上测试的所有草稿模型中速度位列第一，接受率相比重新训练的基线 DFlash 平均高出约 7%。
* **最佳表现 (Best Case)**：在温度为 0 的 GSM8K 数学基准评测中实现了 6.14 倍的加速比（平均单步接受长度达到 7.69 个 Token）。
* **最低表现 (Worst Case)**：在温度为 1 的 Alpaca 任务中加速比为 2.28 倍。在 Qwen3-4B（温度为 0）的测试中，在 9 项评测任务中有 4 项略微落后于 DFlash。

> * **Model Size:** 0.5B-parameter drafter (500M for Qwen3-8B, 475M for Qwen3-4B); drafts blocks of $K = 16$ tokens.
> * **Hardware Requirements:** Runs on the same GPU as the target model. Benchmark speedups utilize 1 NVIDIA H200 NVL at concurrency 1 in `bf16`.
> * **Performance:** The fastest drafter tested on Qwen3-8B, averaging ~7% higher acceptance than a retrained DFlash.
> * **Best Case:** 6.14x speedup on GSM8K at temperature 0 (acceptance length of 7.69 tokens).
> * **Worst Case:** 2.28x speedup on Alpaca at temperature 1. On Qwen3-4B (temperature 0), it trails DFlash on 4 of 9 tasks.

---

## 什么是 FlashMap？

> ## What is FlashMap?

FlashMap 是一种用于投机解码 (Speculative Decoding) 的新型草稿模型，它能够在单步计算内直接将高斯噪声整体映射为包含多个 Token 的完整文本块。其工作流程为：先由轻量级的草稿模型先行“草拟”预估出 $K$ 个 Token，随后由主目标大模型在单次并行前向传播中对这 $K$ 个 Token 进行校验评估，并保留最长匹配的前缀序列。这一严格的验证机制确保了最终生成的输出内容与目标大模型原生逐字解码的数学分布完全一致，实现真正的完全无损输出。

> FlashMap is a speculative decoding drafter that maps Gaussian noise directly to an entire token block in a single step. A small drafter proposes $K$ tokens, after which the target model evaluates all $K$ tokens in one parallel pass and retains the longest matching prefix. This ensures the final output remains completely lossless compared to what the target model would produce natively.

在投机解码框架下，端到端的整体加速性能主要取决于两大关键因素：
1. **接受率 (Acceptance Rate)**：由草稿模型拟定的候选 Token 中，有多少能够被目标主模型成功采纳。
2. **草拟开销 (Drafting Overhead)**：生成这些候选 Token 所消耗的额外计算资源与时间成本有多低。

> In speculative decoding, overall speed depends on two key factors:
> 1. **Acceptance Rate:** How many drafted tokens are accepted.
> 2. **Drafting Overhead:** How cheaply the tokens were generated.

举例来说，[EAGLE-3](https://arxiv.org/abs/2503.01840) 采用自回归的方式逐步草拟 Token，导致其计算开销随着候选文本块的长度线性递增；而 [DFlash](https://arxiv.org/abs/2602.06036) 则通过块级扩散模型 (Block Diffusion) 一次性并行草拟出完整的文本块。

> For instance, [EAGLE-3](https://arxiv.org/abs/2503.01840) drafts autoregressively, causing computational cost to scale with block length, whereas [DFlash](https://arxiv.org/abs/2602.06036) drafts the full block simultaneously using block diffusion.

---

## 为什么基于扩散的草稿模型会导致接受率下降？

> ## Why Do Diffusion Drafters Lose Acceptance?

像 DFlash 这样的标准扩散草稿模型，其核心局限在于独立预测文本块中的每一个位置槽位 (Slot)——这种现象在理论上被称为“因子化近似 (Factorized Approximation)”。

> Standard diffusion drafters like DFlash predict each slot in a token block independently—a limitation known as the *factorized approximation*. 

不妨设想这样一个场景：后续最合理的文本补全有可能是“New York”（纽约），也有可能是“San Diego”（圣地亚哥），两者的出现概率旗鼓相当。对于一个对各槽位进行独立预测的草稿模型而言，由于第一个词和第二个词完全解耦，它有一半的概率会错误拼凑出“New Diego”或“San York”。一旦发生这种情况，目标大模型在校验到第二个词时就会立刻拒绝整条候选序列，导致投机加速失败。

> Imagine a continuation that can be either “New York” or “San Diego” with equal probability. An independent slot drafter might incorrectly propose “New Diego” or “San York” half the time, leading the target model to immediately reject the sequence at the second slot.

FlashMap 巧妙地借鉴了流映射语言模型 ([Flow Map Language Models](https://arxiv.org/abs/2602.16813)) 的设计思想，彻底化解了这一矛盾。它不再对每个槽位孤立预测，而是将每一个噪声样本直接映射到一整个完整的文本块。这意味着，输入的噪声向量能够统筹兼顾全局上下文，同时为所有 Token 槽位联合选定正确的语义模态，从机制上彻底杜绝了跨位置语义割裂的问题。

> FlashMap resolves this by building upon [Flow Map Language Models](https://arxiv.org/abs/2602.16813). Instead of independent slot prediction, each noise sample maps directly to one complete block, allowing the noise vector to jointly select the correct semantic mode for every token slot simultaneously.

---

## FlashMap 的工作原理是什么？

> ## How Does FlashMap Work?

FlashMap 草稿模型采用了 6 层的扩散 Transformer (Diffusion Transformer, DiT) 架构，嵌入维度为 2048，并包含 16 个注意力头。在推理过程中，它直接提取并复用目标大模型第 1、9、17、25 和 33 层的隐层状态 (Hidden States)，同时目标大模型的词嵌入矩阵与语言建模输出头 (LM Head) 保持完全冻结。

> The FlashMap drafter utilizes a 6-block diffusion transformer (DiT) architecture with an embedding dimension of 2048 and 16 attention heads. It consumes hidden states extracted from target model layers 1, 9, 17, 25, and 33, while the target's embedding matrix and language modeling head remain frozen.

### 两阶段训练策略

> ### Training Strategy (Two Stages)

1. **连续流教师模型 (Flow Teacher)**：在 One-hot 编码的 Token 文本块上构建连续流模型，通过交叉熵损失进行训练；同时引入时间重参数化 (Time Reparameterization) 机制，从而优雅且高效地适配 Qwen3 高达 151,936 个 Token 的超大词表。
2. **流映射学生模型 (Flow Map Student)**：采用半群蒸馏 (Semigroup Distillation) 技术，将原本需要多步迭代的流过程压缩为一个直接的“两时间步”去噪器，使其能够在单次前向传播中一步直接跨越从噪声到最终生成数据的全过程。

> 1. **Flow Teacher:** A continuous flow model over one-hot token blocks trained via cross-entropy loss, using a time reparameterization to properly handle Qwen3's massive 151,936-token vocabulary.
> 2. **Flow Map Student:** Employs semigroup distillation to compress the multi-step flow into a direct 2-time denoiser, allowing it to jump from noise to final data in a single forward step.

两款草稿模型均在源自 [Open-PerfectBlend](https://huggingface.co/datasets/mlabonne/open-perfectblend) 的 50 万条样本数据集上完成训练。整体验证、消融实验与训练累计消耗了在 NVIDIA H200 加速卡上约 4,600 个 GPU 时的算力。

> Both drafters were trained on 500K samples sourced from [Open-PerfectBlend](https://huggingface.co/datasets/mlabonne/open-perfectblend). Total training and ablation compute totaled approximately 4,600 GPU hours on NVIDIA H200 accelerators.

---

## 基准测试性能评估

> ## Benchmark Performance

研究团队在统一的训练数据与超参数配置下，重新对 EAGLE-3 与 DFlash 进行了复现测试。评估覆盖了涵盖数学运算、代码编程以及通用日常对话等 9 项具有代表性的基准测试，并在温度设为 0 与 1 两种采样条件下展开了严格比对。

> The research team re-evaluated EAGLE-3 and DFlash under identical training data and hyperparameter settings across 9 distinct benchmarks spanning mathematics, programming, and general conversation at temperatures 0 and 1.

* **解码速度 (Speed)**：在 Qwen3-8B 的*每一项*基准测试任务中，无论是在贪婪采样 (Temperature = 0) 还是随机采样 (Temperature = 1) 设定下，单步 FlashMap 均取得了全场最快的草稿生成速度。
* **准确率与接受长度 (Accuracy)**：尽管 FlashMap 的模型参数量仅为 DFlash 的一半左右，但在全部 18 项测试配置中，单步 FlashMap 有 15 项的 Token 平均接受长度超越了 DFlash。
* **对话任务收益 (Chat Gains)**：在温度为 0 的贪婪模式下，FlashMap 相比 DFlash 在数学推理任务上的加速提升达 5.5%，而在对话类工作负载上的提升更是高达 11.1%。
* **双步增强模式 (2-Step Mode)**：当切换为 2 步去噪配置时，FlashMap 在全部 18 项测试环境中均在接受长度上全面领先 DFlash，平均接受长度提升幅度达到 10%。
* **对比 EAGLE-3**：在温度为 1 的设置下，EAGLE-3 的 Token 接受长度虽然高出 9%，但其整体运行耗时却比 FlashMap 慢了大约 35%。

> * **Speed:** 1-step FlashMap emerged as the fastest drafter across *every* Qwen3-8B benchmark task at both temperature settings.
> * **Accuracy:** 1-step FlashMap surpassed DFlash in token acceptance length across 15 of 18 test configurations, despite having roughly half the parameter count.
> * **Chat Gains:** At temperature 0, performance gains over DFlash reached 5.5% on math and 11.1% on chat workloads.
> * **2-Step Mode:** Operating in a 2-step configuration outperformed DFlash in acceptance length across 18 of 18 test settings, showing an average improvement of 10%.
> * **Comparison to EAGLE-3:** At temperature 1, EAGLE-3 achieved a 9% higher acceptance length but ran roughly 35% slower overall.

---

## 方案对比：FlashMap 与其他主流投机解码草稿模型

> ## Comparison: FlashMap vs. Other Speculative Decoding Drafters

| 特性 (Feature) | [FlashMap](https://arxiv.org/abs/2610.24365) | [DFlash](https://huggingface.co/z-lab/Qwen3-8B-DFlash-b16) | [EAGLE-3](https://arxiv.org/abs/2503.01840) | [DSpark](https://arxiv.org/abs/2607.05147) |
| :--- | :--- | :--- | :--- | :--- |
| **草拟风格 (Drafting Style)** | 连续流映射，1 或 2 步前向传播 | 块级扩散，1 步前向传播 | 自回归树状结构 | 半自回归结构 |
| **Token 间依赖建模 (Inter-token Dependencies)** | 支持，在文本块上进行联合建模 | 不支持，各槽位独立预测 | 支持，严格串行自回归 | 支持，轻量级串行模块 |
| **草稿模型大小 (Drafter Size, Qwen3-8B)** | [500M](https://github.com/al-jshen/flashmap) | [1B](https://huggingface.co/z-lab/Qwen3-8B-DFlash-b16) | 302M（依据论文重训） | 未披露 |
| **官方宣称最高加速 (Headline Claim)** | [最高 6.1x](https://arxiv.org/abs/2610.24365) | [Qwen3-8B 上最高 6.17x](https://huggingface.co/z-lab/Qwen3-8B-DFlash-b16) | [最高 6.5x](https://arxiv.org/abs/2503.01840) | 相比 MTP-1 每用户提速 60–85% |
| **平均加速比 (Qwen3-8B, T=0)** | 4.36x | 4.07x | 2.55x | 未测试 |
| **GSM8K 加速比 (T=0)** | 6.14x | 5.77x | 3.20x | 未测试 |
| **权重开源协议 (Weights License)** | [Apache-2.0](https://huggingface.co/j-shen/FlashMap-Qwen3-8B) | [MIT](https://huggingface.co/z-lab/Qwen3-8B-DFlash-b16) | [Apache-2.0](https://github.com/SafeAILab/EAGLE)（仅代码） | 未披露 |
| **推理框架集成 (Serving Integrations)** | [Transformers, vLLM, SGLang](https://github.com/al-jshen/flashmap) | [Transformers, vLLM, SGLang](https://huggingface.co/z-lab/Qwen3-8B-DFlash-b16) | [SGLang 等主流引擎](https://arxiv.org/abs/2503.01840) | [DeepSeek-V4 推理服务](https://arxiv.org/abs/2607.05147) |

> | Feature | [FlashMap](https://arxiv.org/abs/2610.24365) | [DFlash](https://huggingface.co/z-lab/Qwen3-8B-DFlash-b16) | [EAGLE-3](https://arxiv.org/abs/2503.01840) | [DSpark](https://arxiv.org/abs/2607.05147) |
> | :--- | :--- | :--- | :--- | :--- |
> | **Drafting Style** | Continuous flow map, 1 or 2 passes | Block diffusion, 1 pass | Autoregressive tree | Semi-autoregressive |
> | **Inter-token Dependencies** | Yes, joint over block | No, per-slot independent | Yes, sequential | Yes, lightweight sequential module |
> | **Drafter Size (Qwen3-8B)** | [500M](https://github.com/al-jshen/flashmap) | [1B](https://huggingface.co/z-lab/Qwen3-8B-DFlash-b16) | 302M (retrained per paper) | Not disclosed |
> | **Headline Claim** | [Up to 6.1x](https://arxiv.org/abs/2610.24365) | [Up to 6.17x on Qwen3-8B](https://huggingface.co/z-lab/Qwen3-8B-DFlash-b16) | [Up to 6.5x](https://arxiv.org/abs/2503.01840) | 60–85% faster per user vs MTP-1 |
> | **Avg Speedup (Qwen3-8B, T=0)** | 4.36x | 4.07x | 2.55x | Not tested |
> | **GSM8K Speedup (T=0)** | 6.14x | 5.77x | 3.20x | Not tested |
> | **Weights License** | [Apache-2.0](https://huggingface.co/j-shen/FlashMap-Qwen3-8B) | [MIT](https://huggingface.co/z-lab/Qwen3-8B-DFlash-b16) | [Apache-2.0](https://github.com/SafeAILab/EAGLE) (code) | Not disclosed |
> | **Serving Integrations** | [Transformers, vLLM, SGLang](https://github.com/al-jshen/flashmap) | [Transformers, vLLM, SGLang](https://huggingface.co/z-lab/Qwen3-8B-DFlash-b16) | [SGLang and others](https://arxiv.org/abs/2503.01840) | [DeepSeek-V4 serving](https://arxiv.org/abs/2607.05147) |

*注：平均加速比数据提取自 FlashMap 论文图 1(c)，所比对的 baseline 数据均为作者在相同环境下重新训练测得。*

> *Note: Average speedups calculated from Figure 1(c) of the FlashMap paper using the authors' retrained baselines.*

---

## 如何部署与运行 FlashMap

> ## How to Deploy FlashMap

官方提供的 `flashmap` Python 软件包极为轻巧，仅依赖 `torch` 和 `transformers>=4.56`。用户可以直接通过 pip 或 uv 快速安装：

> The `flashmap` Python package requires only `torch` and `transformers>=4.56`. You can install it directly via:

```bash
uv pip install flashmap
```

在代码层面，只需标准调用 `spec_generate` 函数，即可在单张 GPU 上协同并发执行草稿模型与目标主模型。

> A standard `spec_generate` function call executes both the drafter and target model concurrently on a single GPU.

### 主流推理引擎集成方案

> ### Serving Integration Paths

* **vLLM (v0.31+)**：在启动参数中通过 `--speculative-config` 传递草稿模型配置，并将 `num_speculative_tokens` 设定为 `16`。
* **SGLang (v0.5.20+)**：在启动参数中添加 `--speculative-algorithm DSPARK`，并指向 FlashMap 的本地权重路径即可。

> * **vLLM (v0.31+):** Pass the drafter configuration via `--speculative-config` with `num_speculative_tokens` set to `16`.
> * **SGLang (v0.5.20+):** Use `--speculative-algorithm DSPARK` combined with the path to your FlashMap weights.

*使用贴士：在实际配置中，将 `num_steps` 设置为 `2` 能够以极其轻微的生成速度损耗换取更稳定的 Token 接受率。若要在大于 0 的温度下进行概率采样，在 vLLM 中需要额外将 `"draft_sample_method"` 配置指定为 `"probabilistic"`。*

> *Tip: Set `num_steps=2` to trade a minor amount of generation speed for higher token acceptance. For probabilistic sampling at temperatures above 0, vLLM requires setting `"draft_sample_method": "probabilistic"`.*

---

## 核心总结

> ## Key Takeaways

* FlashMap 采用创新的连续流映射架构，仅需单次前向传播即可联合建模并生成完整的 16-Token 文本块。
* 仅凭 0.5B 参数量的超轻量草稿头，在 Qwen3-8B 上即可实现高达 **6.14 倍的完全无损加速**。
* 在 Qwen3-8B 参与测试的全部 9 项基准评测任务中，性能均全面超越了重训后的 DFlash 基线。
* 原生支持 2 步草拟模式，能够进一步均衡并显著提升文本块中各个 Token 槽位的接受率。
* 全面开源透明，采用 Apache-2.0 权重许可与 MIT 代码协议，并为 vLLM 与 SGLang 提供了开箱即用的推理插件。

> * FlashMap generates 16-token blocks jointly in a single forward pass using a continuous flow map architecture.
> * Achieves up to a **6.14x lossless speedup** on Qwen3-8B while utilizing a lightweight 0.5B drafter.
> * Outperforms a retrained DFlash baseline across all 9 tested Qwen3-8B benchmark tasks.
> * Supports a 2-step drafting mode to stabilize token acceptance uniformly across blocks.
> * Fully open-source with Apache-2.0 model weights, MIT code, and seamless integration plugins for vLLM and SGLang.

---

## 资源与项目链接

> ## Resources & Links

* **研究论文**：[arXiv:2610.24365](https://arxiv.org/abs/2610.24365)
* **项目主页**：[jshen.net/flashmap](https://jshen.net/flashmap/)
* **开源代码库**：[GitHub - al-jshen/flashmap](https://github.com/al-jshen/flashmap)
* **模型权重**：[Hugging Face Collection](https://huggingface.co/collections/j-shen/flashmap-6ad0feb955bdc30db59769fa)

> * **Research Paper:** [arXiv:2610.24365](https://arxiv.org/abs/2610.24365)
> * **Project Page:** [jshen.net/flashmap](https://jshen.net/flashmap/)
> * **Code Repository:** [GitHub - al-jshen/flashmap](https://github.com/al-jshen/flashmap)
> * **Model Weights:** [Hugging Face Collection](https://huggingface.co/collections/j-shen/flashmap-6ad0feb955bdc30db59769fa)

---

*本文最初发布于 MarkTechPost，原英文报道请参阅 [此处](https://www.marktechpost.com/2026/10/28/flashmap-flow-map-speculative-decoding/)。*

> *Originally published by MarkTechPost. Read the original post [here](https://www.marktechpost.com/2026/10/28/flashmap-flow-map-speculative-decoding/).*
