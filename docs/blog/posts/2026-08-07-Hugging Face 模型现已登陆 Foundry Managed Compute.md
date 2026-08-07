---
authors:
- aitoboxrobot
categories:
- 产品发布
date: 2026-08-07
hide:
- navigation
tags:
- Microsoft Foundry
- Hugging Face
- Managed Compute
- AI Models
- Azure
title: Hugging Face 模型现已登陆 Foundry Managed Compute
---
### 文章背景与核心概要
本文介绍了在 Microsoft Build 2026 上发布的重大更新：Microsoft Foundry Managed Compute 以及在 Foundry 上集成 Hugging Face 模型。该平台将 Hugging Face 生态系统中经过精选的开源权重模型直接引入 Microsoft Foundry，支持每周更新与一键部署，并通过预置的 Azure 权重、经微软扫描的安全运行时以及 Foundry 原生的企业级安全、治理、可观测性和计费框架，为企业级 AI 应用提供强大支撑。

通过 Foundry Managed Compute，用户可以利用托管的 GPU 平台即服务（PaaS）来运行开源和自定义模型。该集成弥补了 Hugging Face 单独缺乏企业级运维层的短板，结合了前沿性能、深度定制、数据主权和成本控制等优势，使企业能够在私有端点后方安全地构建和运营智能体（Agentic）AI 应用。

---

## 摘要 (Executive Summary)

Announced at Microsoft Build 2026, **Foundry Managed Compute** and **Hugging Face models on Foundry** bring a curated catalog of open-weight models from the Hugging Face ecosystem directly to Microsoft Foundry. Refreshed weekly and deployable with a single click, these models leverage pre-staged Azure weights, Microsoft-scanned runtimes, and the complete enterprise security, governance, observability, and billing framework native to Foundry.

> 在 Microsoft Build 2026 上发布的 **Foundry Managed Compute**（Foundry 托管计算）与 **Hugging Face models on Foundry**（Foundry 上的 Hugging Face 模型）将 Hugging Face 生态系统中精选的开源权重模型直接引入了 Microsoft Foundry。这些模型每周更新一次，支持一键部署，并充分利用了预置的 Azure 权重、微软扫描的运行时，以及 Foundry 原生的完整企业级安全、治理、可观测性和计费框架。

---

## 平台：Microsoft Foundry 与托管计算 (The Platform: Microsoft Foundry and Managed Compute)

Microsoft Foundry is an end-to-end platform designed for building and operating agentic AI applications. It offers the widest model selection on any cloud—spanning frontier, open-source, and custom weights from providers like Microsoft, OpenAI, Anthropic, Meta, Mistral, DeepSeek, and Hugging Face—accessible through a single endpoint and unified SDKs (Python, C#, JavaScript, and Java).

> Microsoft Foundry 是一个端到端平台，专为构建和运营智能体（agentic）AI 应用而设计。它在所有云中提供了最广泛的模型选择——涵盖来自微软、OpenAI、Anthropic、Meta、Mistral、DeepSeek 和 Hugging Face 等提供商的前沿模型、开源模型以及自定义权重，并通过单一端点和统一的 SDK（Python、C#、JavaScript 和 Java）进行访问。

### 核心平台能力 (Core Platform Capabilities)
* **Foundry Agent Service:** Multi-agent orchestration featuring built-in memory, knowledge grounding through Foundry IQ, and connectable tools via agentic protocols.
* **Observability & Quality Loops:** End-to-end tracing, real-time monitoring, continuous evaluations, and an automated prompt optimizer.
* **Enterprise Controls:** Content safety filters, task-adherence guardrails, an AI Red Teaming Agent for adversarial testing, unified RBAC, private networking, and Azure Policy integration.

> * **Foundry Agent Service（Foundry 智能体服务）：** 多智能体编排，具备内置内存、通过 Foundry IQ 实现的知识基础（Grounding），以及通过智能体协议连接的工具。
> * **可观测性与质量循环：** 端到端追踪、实时监控、持续评估以及自动化的提示词优化器。
> * **企业级控制：** 内容安全过滤器、任务遵循护栏（guardrails）、用于对抗测试的 AI 红队智能体、统一的 RBAC、私有网络以及 Azure Policy 集成。

### Foundry 托管计算 (Foundry Managed Compute)
Alongside pay-per-token and provisioned throughput, **Foundry Managed Compute** acts as a managed GPU platform-as-a-service specifically for open-source and custom models. 
* **Model-Centric Deployment:** You define workloads by parameter count, context length, and latency/throughput goals; Foundry dynamically handles the underlying GPU topology.
* **Automated Maintenance:** Microsoft handles container updates, security patches, and runtime upgrades for supported engines (**vLLM, SGLang, TensorRT-LLM, NIM, TEI, and llama.cpp**) without requiring redeployments.
* **Deployment Flexibility:** Supports both **Global deployments** (optimized for capacity and pricing) and **Data Zone deployments** (optimized for data residency and sovereignty).

> 除了按 token 计费和预留吞吐量之外，**Foundry Managed Compute** 还充当专门针对开源和自定义模型的托管 GPU 平台即服务（PaaS）。
> * **以模型为中心的部署：** 您通过参数量、上下文长度以及延迟/吞吐量目标来定义工作负载；Foundry 会动态处理底层 GPU 拓扑。
> * **自动化维护：** 微软负责处理所支持引擎（**vLLM、SGLang、TensorRT-LLM、NIM、TEI 和 llama.cpp**）的容器更新、安全补丁和运行时升级，无需重新部署。
> * **部署灵活性：** 同时支持**全球部署**（针对容量和价格优化）和**数据区部署**（针对数据驻留和主权优化）。

---

## 为什么选择 Hugging Face？ (Why Hugging Face?)

As the public square of open AI, Hugging Face hosts over **3 million open models, 15 million builders, and 400,000 organizations**. Open models have rapidly closed the gap with proprietary alternatives, offering key strategic advantages:
* **State-of-the-Art Performance:** Competitive benchmarks matching top closed-source frontier models.
* **Deep Customization:** Full weights enable fine-tuning, distillation, quantization, and LoRA adaptation.
* **Data Sovereignty:** Run models securely within your own tenant infrastructure behind private endpoints.
* **Cost Shaping & Control:** Scale to zero when idle and right-size accelerators for predictable workloads.
* **Version Control:** Maintain precise release cadences, pinning or rolling back model versions independently.

*The Challenge:* Hugging Face alone lacks an enterprise-grade operational layer. **Hugging Face models on Foundry** bridges this gap, managed entirely by Microsoft.

> 作为开放 AI 的公共广场，Hugging Face 托管了超过 **300 万个开源模型、1500 万构建者以及 40万个组织**。开源模型迅速缩小了与专有替代方案之间的差距，具备以下关键战略优势：
> * **顶尖性能：** 与顶级闭源前沿模型相媲美的竞争基准。
> * **深度定制：** 完整的权重支持微调、蒸馏、量化和 LoRA 适配。
> * **数据主权：** 在私有端点后方的自有租户基础设施内安全运行模型。
> * **成本塑形与控制：** 空闲时缩减至零，并为可预测的工作负载匹配合适大小的加速器。
> * **版本控制：** 维持精确的发布节奏，独立锁定或回滚模型版本。
> 
> *挑战：* 仅靠 Hugging Face 缺乏企业级的运维层。**Hugging Face models on Foundry** 填补了这一空白，并由微软完全托管。

---

## Foundry 上的 Hugging Face 模型 (Hugging Face Models on Foundry)

The integration brings a curated subset of models straight into the Foundry Model Catalog:
* **Weekly Refreshes:** Continuous integration of trending models from the global community.
* **Full Modality Support:** Text, vision, audio, and multimodal setups (LLMs, VLMs, ASR, translation, embeddings, segmentation, and image generation).
* **Enterprise-Safe Curation:** Strictly utilizes **SafeTensors** with rigorous screening against untrusted executable code (`trust_remote_code`).
* **Optimized Runtimes:** Automated engine matching (vLLM, SGLang, TEI, llama.cpp, etc.) tailored to each model.

> 此次集成将一小部分精选模型直接引入了 Foundry 模型目录（Model Catalog）：
> * **每周更新：** 持续集成来自全球社区的热门模型。
> * **全模态支持：** 文本、视觉、音频和多模态设置（LLM、VLM、ASR、翻译、嵌入、分割和图像生成）。
> * **企业级安全筛选：** 严格使用 **SafeTensors**，并针对不受信任的可执行代码（`trust_remote_code`）进行严格筛查。
> * **优化的运行时：** 针对每个模型定制的自动化引擎匹配（vLLM、SGLang、TEI、llama.cpp 等）。

### 筛选流水线 (The Curation Pipeline)
1. **Identification:** Selecting trending and high-demand open-weight models.
2. **Compliance & Security Screening:** Reviewing licenses against Microsoft distribution policies and stripping out unsafe executable code vectors.
3. **Runtime Build & CVE Scanning:** Building, signing, and publishing secure inference container images.
4. **Pre-Staging Weights:** Caching validated weights directly in secure, region-specific Azure storage.
5. **Catalog Validation & Publish:** Rigorous testing for API conformance and performance metrics before launching into the Foundry Catalog.

> 1. **识别：** 选择热门且高需求的开源权重模型。
> 2. **合规与安全筛选：** 依据微软的分发政策审查许可证，并剔除不安全的可执行代码向量。
> 3. **运行时构建与 CVE 扫描：** 构建、签名并发布安全的推理容器镜像。
> 4. **预置权重：** 将验证过的权重直接缓存在安全的、特定区域的 Azure 存储中。
> 5. **目录验证与发布：** 在发布到 Foundry 目录之前，对 API 一致性和性能指标进行严格测试。

---

## 模型运行时 (Model Runtimes)

* **vLLM:** The default high-throughput engine for open LLMs, integrated directly with Hugging Face Transformers for day-one model support.
* **SGLang:** Optimized for multi-modal and language models with advanced support for structured outputs (JSON, regex) critical for agents.
* **Text Embeddings Inference (TEI):** Lean, hardware-compiled pipelines tailored for RAG and semantic search.
* **llama.cpp:** Cost-optimized CPU and small-GPU execution paths for GGUF-quantized models.
* **TensorRT-LLM & NIM:** NVIDIA-optimized execution paths for maximum throughput and low latency.
* **hf-serve:** Handles non-LLM modalities like audio, vision, and segmentation pipelines.

> * **vLLM：** 针对开源 LLM 的默认高吞吐量引擎，直接与 Hugging Face Transformers 集成，实现首日模型支持。
> * **SGLang：** 针对多模态和语言模型进行了优化，对智能体至关重要的结构化输出（JSON、正则表达式）提供了高级支持。
> * **文本嵌入推理 (TEI)：** 专为 RAG 和语义搜索量身定制的精简硬件编译流水线。
> * **llama.cpp：** 针对 GGUF 量化模型的成本优化型 CPU 和小型 GPU 执行路径。
> * **TensorRT-LLM & NIM：** 经 NVIDIA 优化的执行路径，可实现最大吞吐量和低延迟。
> * **hf-serve：** 处理音频、视觉和分割流水线等非 LLM 模态。

---

## 部署和评分开源权重模型 (Deploying and Scoring an Open-Weight Model)

Deploying an open-weight model follows a streamlined 5-step process: browse the catalog, choose a deployment template, configure instance counts, deploy via portal/CLI/SDK, and query via the unified endpoint.

> 部署开源权重模型遵循简化的 5 步骤流程：浏览目录、选择部署模板、配置实例数量、通过门户/CLI/SDK 部署，以及通过统一端点进行查询。

### 部署模板 (Deployment Templates)
Deployment templates pin the runtime, accelerator count, context length, and performance tuning configurations. For instance, `qwen3-32b` provides options such as:

> 部署模板锁定了运行时、加速器数量、上下文长度和性能调优配置。例如，`qwen3-32b` 提供了以下选项：

| Template | Runtime | Accelerator | Context |
| :--- | :--- | :--- | :--- |
| `qwen–qwen3-32b–40k-nvidia-a100` | vLLM | 1 × A100 80 GB | 40K |
| `qwen–qwen3-32b–40k-nvidia-h100` | vLLM | 1 × H100 80 GB | 40K |
| `qwen–qwen3-32b–128k-nvidia-2xa100` | vLLM | 2 × A100 80 GB | 128K |
| `qwen–qwen3-32b–128k-nvidia-2xh100` | vLLM | 2 × H100 80 GB | 128K |

### 通过 Python SDK 部署 (Deploy via Python SDK)
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient

client = CognitiveServicesManagementClient(DefaultAzureCredential(), SUBSCRIPTION_ID)

deployment = client.managed_compute_deployments.begin_create_or_update(
    resource_group_name=RESOURCE_GROUP,
    account_name=ACCOUNT_NAME,
    deployment_name="qwen3-32b",
    resource={
        "sku": {"name": "GlobalManagedCompute", "capacity": 1},
        "properties": {
            "model": "azureml://registries/azure-huggingface/models/qwen--qwen3-32b/versions/1",
            "deploymentTemplate": "azureml://registries/azure-huggingface/deploymenttemplates/qwen--qwen3-32b--40k-nvidia-h100/labels/latest",
            "acceleratorType": "H100_80GB",
        },
    },
).result()
```

### 通过 OpenAI SDK 进行评分/调用 (Score via OpenAI SDK)
```python
from openai import OpenAI

api_key  = client.accounts.list_keys(RESOURCE_GROUP, ACCOUNT_NAME).key1
endpoint = f"https://{ACCOUNT_NAME}.services.ai.azure.com/openai/v1"

openai_client = OpenAI(base_url=endpoint, api_key=api_key)

completion = openai_client.chat.completions.create(
    model=deployment.name,
    messages=[{"role": "user", "content": "What is the capital of France?"}],
)

print(completion.choices[0].message)
```

---

## 现状与未来展望 (What's Available Today)

* **In Preview Now:** The Hugging Face Collection in the Microsoft Foundry Model Catalog—supporting NVIDIA A100, H100, and AMD MI300X accelerators across Global and Data Zone scopes. Includes automated monitoring, Azure Monitor integration, billing tags, and zero-downtime CVE runtime patching.
* **On the Roadmap:** Expanded ecosystem model coverage, new hardware accelerator families, and Bring Your Own Weights (BYOW) support for fine-tuned enterprise models.

> * **现已推出预览版：** Microsoft Foundry 模型目录中的 Hugging Face 集合——支持全球（Global）和数据区（Data Zone）范围内的 NVIDIA A100、H100 和 AMD MI300X 加速器。包含自动化监控、Azure Monitor 集成、计费标签以及零停机 CVE 运行时修补。
> * **路线图展望：** 扩展生态系统模型覆盖范围、引入新的硬件加速器系列，以及针对微调企业模型的自带权重（BYOW）支持。