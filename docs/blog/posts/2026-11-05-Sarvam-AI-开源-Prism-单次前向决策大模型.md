---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-11-05
hide:
  - navigation
tags:
  - Sarvam AI
  - Prism
  - 决策模型
  - 单次前向推理
  - NVIDIA B200
  - FP8
  - AI智能体评测
title: "Sarvam AI 开源 Prism 单次前向决策大模型"
---

# Sarvam AI 开源 Prism 单次前向决策大模型

![Sarvam AI Releases Open-Weight Prism Decision Model](./images/1968b58fc6af.jpg)

### 文章背景与核心概要
在企业级 AI 系统与 AI 智能体 (AI Agent) 工作流中，诸如意图路由、模型分发、合规审查与质量判别等决策场景，往往并不需要大模型逐字生成长篇文本，而是对推理延迟、置信度准确度与显存成本有着近乎苛刻的要求。Sarvam AI 正式开源的 Sarvam Prism 决策模型另辟蹊径，舍弃了传统自回归式的逐 Token 生成方式，创新采用“单次前向传递 (Single Forward Pass)”机制，直接对预定义候选项进行并行评分。在单块 NVIDIA B200 GPU (FP8) 上，Prism 实现了中位数仅 44 毫秒的超低响应延迟，且支持高达 131,072 Token 的超长上下文。该模型基于 Apache 2.0 协议开源，为高并发企业级决策与智能体自动化监管树立了新的性能标杆。

---

## 核心概要

> ## Summary

Sarvam AI 正式发布了 **Sarvam Prism**，这是一款基于 Sarvam 105B 基座构建的开源权重企业级决策大模型。不同于传统的逐 Token (Token-by-Token) 文本生成模式，Prism 仅通过单次前向传递即可完成对所有预设候选选项的并行评估与打分。在单张运行 FP8 精度的 NVIDIA B200 GPU 上，该模型实现了令人惊叹的 **44 毫秒**中位数响应时间，并在 Hugging Face 上以 Apache 2.0 协议向全球开发者开放。专为意图路由、文档智能与智能体评估等企业级工作流量身打造的 Prism，完美兼具了极高推理速度、精准置信度校准以及高达 131,072 Token 的超长上下文支持。

> Sarvam AI has released **Sarvam Prism**, an open-weight enterprise decision model built on the Sarvam 105B base. Instead of traditional token-by-token text generation, Prism processes requests in a single forward pass to evaluate and score predefined options. It achieves an impressive 44-millisecond median response time on a single NVIDIA B200 GPU (running in FP8) and is available under an Apache 2.0 license on Hugging Face. Designed for enterprise workflows—such as intent routing, document intelligence, and agent evaluation—Prism combines high inference speed, precise confidence calibration, and support for massive context windows up to 131,072 tokens.

---

## 单次前向决策模型架构

> ## A Single-Pass Decision Model

Sarvam AI 于 2026 年 11 月 3 日发布了 **Sarvam Prism**，推出了一款专门针对企业决策场景而非自由文本生成定制的开源权重模型。

> Sarvam released **Sarvam Prism** on November 3, 2026, offering an open-weight model tailored specifically for enterprise decision-making rather than free-form text generation.

提交给 Prism 的每个推理请求由以下三部分组成：
* 当前系统状态 (Current state)
* 待决问题 (Question)
* 任意数量的候选选项（容纳在上下文窗口限制内）

> Each request submitted to Prism consists of:
> * A current state
> * A question
> * Any number of candidate options (fitting within the context window)

模型通过单次前向传递同时处理整组输入。随后，一个轻量级评分头 (Scoring head) 会为每一个候选项分配精准的置信概率。Prism 基于对 Sarvam 105B 系统进行 LoRA 微调打造，针对以下场景进行了深度优化：
* 客服意图分类路由
* 跨模型调用动态分发
* 文档智能分析
* AI 智能体运行轨迹的自动化评估与监督

> The model processes this input in a single forward pass. A small scoring head then assigns a probability to every option. Built using LoRA fine-tuning applied to the Sarvam 105B system, Prism is optimized for tasks such as:
> * Customer-support intent routing
> * Model routing
> * Document intelligence
> * Automated evaluation and oversight of AI agent runs

---

### 训练目标与注意力机制

> ### Training Objectives and Architecture

Prism 输出的概率分布由两个权重均等的训练目标共同塑造：
1. **带 5% 标签平滑的交叉熵损失 (Cross-entropy with 5% label smoothing)**：有效防止模型产生过度确定性判断；
2. **布里尔分数损失 (Brier loss)**：精确度量预测概率的均方误差，对高置信度误判施加严厉惩罚，确保极强的模型置信度标定 (Calibration)。

> Prism's probabilities are shaped by two equally weighted training objectives:
> 1. **Cross-entropy with 5% label smoothing:** Discourages complete certainty.
> 2. **Brier loss:** Measures squared probability error, making confident mistakes costly and ensuring robust model calibration.

此外，专门定制的注意力掩码 (Attention Mask) 确保候选项在打分过程中保持相互隔离。当状态与问题以双向注意力充分阅读后，仅由答案 Token 统一对比并衡量所有可用选项。

> Additionally, a custom attention mask keeps options isolated during scoring. While the state and question are read bidirectionally, only the answer token evaluates and compares all available options.

---

## 准确率与延迟评测

> ## Accuracy and Latency Measurements

Sarvam AI 对 Prism 的综合性能评测涵盖了三个维度的基准测试：
* **Jev 决策指数 (Jev Decision Index)**（涵盖 37 个公开基准测试）
* Sarvam 针对 **Artificial Analysis 决策指数** 的复现测试（用“不知道”选项替代专有私密知识考题）
* 内部构建的**印度多语种基准测试 (Indian-language benchmark)**

> Sarvam’s evaluation of Prism combined three distinct benchmarks:
> * The **Jev Decision Index** (covering 37 public benchmarks)
> * Sarvam’s recreation of the **Artificial Analysis Decision Index** (substituting private knowledge tests with an "I don't know" option)
> * An internal **Indian-language benchmark**

---

### 核心性能亮点

> ### Performance Highlights

* **综合得分：** Prism 取得了 **71.8** 的全场景平均分（在 Jev 指数上为 67.0，Artificial Analysis 复现测试上为 65.9，印度语系测试上高达 82.5）。
* **推理速度：** 借助 FP8 低精度量化，Prism 可在**单块 NVIDIA B200 GPU** 上极速运行，实现仅 **44 毫秒** 的中位数响应延迟。

> * **Overall Score:** Prism achieved an average score of **71.8** (67.0 on Jev, 65.9 on the Artificial Analysis recreation, and 82.5 on Indian languages).
> * **Speed:** Utilizing FP8 precision allows Prism to run efficiently on a **single NVIDIA B200 GPU**, achieving a median response time of **44 milliseconds**.

得益于一系列深入底层的高并发系统工程优化——包括将全部 128 个专家融合至单一内核、将整个前向过程固化捕获为 CUDA Graph、将 FP8 格式转换内嵌融合至专家计算算子以及合并微调适配器权重——Sarvam 在毫厘不损模型精确度的情况下，达成了这一亮眼的单卡极致低延迟性能。

> Through extensive engineering optimizations—including grouping all 128 experts into one kernel, capturing the forward pass as a CUDA Graph, fusing FP8 conversion into expert kernels, and merging fine-tuning adapters—Sarvam achieved this high-speed, single-GPU performance without sacrificing model accuracy.

---

## 置信度校准与智能体监管能力

> ## Calibration and Agent Evaluation

### 置信度校准表现

> ### Confidence Calibration

为了让企业级自动化流水线能够完全放心地依据置信度阈值进行自动化裁决：
* 在英语环境下设定 **90% 置信度阈值**时，Prism 预估失误率为 3.3%，而实际测试出的失误率仅为 **2.2%**（基于 226,088 道测试题目）；
* 在涵盖 10 种印度本地语言与印地英语 (Hinglish) 的测试中，模型预估失误率为 5.4%，实际失误率仅为 **4.4%**；
* 在所有测试区间（50% 到 95% 置信度）内，实际失误率均严格低于模型预测的错误上限。

> To ensure enterprise workflows can safely rely on confidence thresholds for automation:
> * At a **90% confidence threshold** in English, Prism expected a 3.3% error rate and actually delivered **2.2% errors** (tested across 226,088 questions).
> * Across 10 Indian languages and Hinglish, it expected 5.4% errors and delivered **4.4% errors**. 
> * Actual error rates remained consistently below predicted thresholds across all tested ranges (50% to 95%).

---

### 选项顺序鲁棒性

> ### Option Consistency

为消除候选项排列顺序带来的评估偏差，Sarvam 进行了选项混洗 (Shuffling) 测试。尽管随机乱序会造成轻微扰动，但通过确立固定的内部评分时序——将预测概率映射回原始输入标签——模型彻底消除了答案漂移，且不产生任何额外计算负荷。

> To address order bias, Sarvam tested option shuffling. While random ordering caused slight variations, establishing a fixed internal scoring order—returning probabilities mapped to original labels—completely eliminated answer shifts without adding computational overhead.

---

### 智能体监管与网络安全基准测试

> ### Agent Oversight & Cybersecurity

* **智能体评测 (Agent Evaluation)**：在针对 700 次完整运行记录与 1,770 个评测问题的严格检验中，Prism 取得了 **78.5%** 的综合判定准确率（任务成功判定准确率 75.0%，人工介入审查决策准确率 86.4%，故障归因准确率 69.6%），每次运行的评测耗时仅约半秒。
* **网络安全基准测试 (Cybersecurity Benchmarks)**：在包含九类关键任务（如网络钓鱼识别、越狱反弹攻击防范、MITRE 框架攻击判定等）共 5,517 个问题的内部网络安全测试中，Prism 斩获 **89.0%** 的高分，显著超越了 Clef 和 Jev 1.14 等同类竞品方案。

> * **Agent Evaluation:** Tested on 700 recorded runs and 1,770 questions, Prism achieved an overall accuracy of **78.5%** (75.0% for judging task success, 86.4% for human review decisions, and 69.6% for failure attribution) with an evaluation time of about half a second per run.
> * **Cybersecurity Benchmarks:** Prism scored **89.0%** on an internal cybersecurity benchmark comprising 5,517 questions across nine tasks (such as identifying phishing, jailbreak attempts, and MITRE-framed attacks), outperforming competing solutions like Clef and Jev 1.14.
