---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-07
hide:
- navigation
tags:
- Sentence Transformers
- 多模态
- 嵌入模型
- 重排模型
- RAG
title: 使用 Sentence Transformers 构建多模态嵌入与重排模型
---
### 文章背景与核心概要
随着 **Sentence Transformers** v5.4 版本的更新，该框架正式引入了对多模态 AI 管道的原生支持。开发者现在可以通过熟悉的统一 API，在文本、图像、音频和视频等多种模态之间进行编码与比对。本文档详细介绍了如何利用这些全新的多模态功能来进行嵌入生成和跨模态重排（Cross-Modal Reranking），从而为视觉文档检索、跨模态搜索以及多模态 RAG（检索增强生成）等应用提供强大的底层技术支持。

---

## 目录

- [什么是多模态模型？](#什么是多模态模型)
- [安装](#安装)
- [多模态嵌入模型](#多模态嵌入模型)
  - [加载模型](#加载模型)
  - [编码图像](#编码图像)
  - [跨模态相似度计算](#跨模态相似度计算)
  - [编码查询与文档](#编码查询与文档)
- [多模态重排模型](#多模态重排模型)
  - [对混合模态文档进行排序](#对混合模态文档进行排序)
  - [预测成对分数](#预测成对分数)
- [检索与重排结合](#检索与重排结合)
- [输入格式与配置](#输入格式与配置)
  - [支持的输入类型](#支持的输入类型)
  - [检查模态支持情况](#检查模态支持情况)
  - [处理器与模型参数配置](#处理器与模型参数配置)
- [支持的模型列表](#支持的模型列表)
- [更多资源](#更多资源)

---

## 什么是多模态模型？

传统的嵌入模型仅能将文本转换为固定大小的向量。而多模态嵌入模型能够将来自不同模态（文本、图像、音频或视频）的输入映射到一个共享的嵌入空间中。这使得我们可以利用标准的相似度指标，直接在文本查询和图像文档之间进行比对（反之亦然）。

同理，传统的重排器（Cross-Encoder）用于对文本之间的相关性对进行评分。而多模态重排器则可以对其中一个或两个元素为图像、音频、视频或图文混合文档的输入对进行评分。

> 💡 **提示：** 如果你想训练自己的多模态模型，请参考官方配套博客：[使用 Sentence Transformers 训练和微调多模态嵌入与重排模型](https://huggingface.co/blog/train-multimodal-sentence-transformers)。

---

## 安装

根据你所需的模态安装对应的依赖项：

```bash
# For image support
pip install -U "sentence-transformers[image]"

# For audio support
pip install -U "sentence-transformers[audio]"

# For video support
pip install -U "sentence-transformers[video]"

# Mix and match as needed
pip install -U "sentence-transformers[image,video,train]"
```

> `> # For image support`
> `> pip install -U "sentence-transformers[image]"`
> `> `
> `> # For audio support`
> `> pip install -U "sentence-transformers[audio]"`
> `> `
> `> # For video support`
> `> pip install -U "sentence-transformers[video]"`
> `> `
> `> # Mix and match as needed`
> `> pip install -U "sentence-transformers[image,video,train]"`

> ⚠️ **注意：** 视觉语言模型（VLM）如 `Qwen3-VL-2B` 需要配备至少约 8 GB 显存的 GPU（8B 版本则需要约 20 GB）。在 CPU 环境下进行推理将会极其缓慢；因此，CPU 环境更适合纯文本模型或传统的 CLIP 模型。

---

## 多模态嵌入模型

### 加载模型
加载多模态嵌入模型的方式与纯文本模型完全相同：

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")
```

> `> from sentence_transformers import SentenceTransformer`
> `> `
> `> model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")`

### 编码图像
`model.encode()` 接受网络链接（URL）、本地文件路径或 PIL 图像对象作为输入：

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")

img_embeddings = model.encode([
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
])
print(img_embeddings.shape)
# (2, 2048)
```

> `> from sentence_transformers import SentenceTransformer`
> `> `
> `> model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")`
> `> `
> `> img_embeddings = model.encode([`
> `>     "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",`
> `>     "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",`
> `])`
> `> print(img_embeddings.shape)`
> `> # (2, 2048)`

### 跨模态相似度计算
由于各种输入都被映射到了共享空间中，因此你可以评估不同模态之间的相似度：

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")

img_embeddings = model.encode([
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
])

text_embeddings = model.encode([
    "A green car parked in front of a yellow building",
    "A red car driving on a highway",
    "A bee on a pink flower",
    "A wasp on a wooden table",
])

similarities = model.similarity(text_embeddings, img_embeddings)
print(similarities)
```

> `> from sentence_transformers import SentenceTransformer`
> `> `
> `> model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")`
> `> `
> `> img_embeddings = model.encode([`
> `>     "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",`
> `>     "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",`
> `])`
> `> `
> `> text_embeddings = model.encode([`
> `>     "A green car parked in front of a yellow building",`
> `>     "A red car driving on a highway",`
> `>     "A bee on a pink flower",`
> `>     "A wasp on a wooden table",`
> `])`
> `> `
> `> similarities = model.similarity(text_embeddings, img_embeddings)`
> `> print(similarities)`

### 编码查询与文档
对于检索任务，请使用 `encode_query()` 和 `encode_document()`，它们会自动应用由模型作者配置的正确提示词（Prompt）指令：

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")

query_embeddings = model.encode_query([
    "Find me a photo of a vehicle parked near a building",
    "Show me an image of a pollinating insect",
])

doc_embeddings = model.encode_document([
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
])

similarities = model.similarity(query_embeddings, doc_embeddings)
print(similarities)
```

> `> from sentence_transformers import SentenceTransformer`
> `> `
> `> model = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")`
> `> `
> `> query_embeddings = model.encode_query([`
> `>     "Find me a photo of a vehicle parked near a building",`
> `>     "Show me an image of a pollinating insect",`
> `])`
> `> `
> `> doc_embeddings = model.encode_document([`
> `>     "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",`
> `>     "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",`
> `])`
> `> `
> `> similarities = model.similarity(query_embeddings, doc_embeddings)`
> `> print(similarities)`

---

## 多模态重排模型

多模态重排器（Cross-Encoder）能够对任意支持模态的输入对之间的相关性进行评分。

### 对混合模态文档进行排序
`rank()` 方法可以针对某个查询对一组候选文档进行评分和排序：

```python
from sentence_transformers import CrossEncoder

model = CrossEncoder("Qwen/Qwen3-VL-Reranker-2B")

query = "A green car parked in front of a yellow building"
documents = [
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",
    "A vintage Volkswagen Beetle painted in bright green sits in a driveway.",
    {
        "text": "A car in a European city",
        "image": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",
    },
]

rankings = model.rank(query, documents)
for rank in rankings:
    print(f"{rank['score']:.4f}\t(document {rank['corpus_id']})")
```

> `> from sentence_transformers import CrossEncoder`
> `> `
> `> model = CrossEncoder("Qwen/Qwen3-VL-Reranker-2B")`
> `> `
> `> query = "A green car parked in front of a yellow building"`
> `> documents = [`
> `>     "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",`
> `>     "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg",`
> `>     "A vintage Volkswagen Beetle painted in bright green sits in a driveway.",`
> `>     {`
> `>         "text": "A car in a European city",`
> `>         "image": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg",`
> `>     },`
> `]`
> `> `
> `> rankings = model.rank(query, documents)`
> `> for rank in rankings:`
> `>     print(f"{rank['score']:.4f}\t(document {rank['corpus_id']})")`

### 预测成对分数
使用 `predict()` 来提取显式输入对的原始相关性得分：

```python
from sentence_transformers import CrossEncoder

model = CrossEncoder("jinaai/jina-reranker-m0", trust_remote_code=True)

scores = model.predict([
    ("A green car", "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"),
    ("A bee on a flower", "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg"),
    ("A green car", "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg"),
])
print(scores)
```

> `> from sentence_transformers import CrossEncoder`
> `> `
> `> model = CrossEncoder("jinaai/jina-reranker-m0", trust_remote_code=True)`
> `> `
> `> scores = model.predict([`
> `>     ("A green car", "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/car.jpg"),`
> `>     ("A bee on a flower", "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg"),`
> `>     ("A green car", "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/bee.jpg"),`
> `])`
> `> print(scores)`

---

## 检索与重排结合

将快速的初筛嵌入检索与高精度的重排模型相结合，以在大规模场景下实现最佳性能：

```python
from sentence_transformers import SentenceTransformer, CrossEncoder

# Step 1: Initial Retrieval via Embeddings
embedder = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")

query = "revenue growth chart"
query_embedding = embedder.encode_query(query)

document_screenshots = [
    "path/to/doc1.png",
    "path/to/doc2.png",
]
corpus_embeddings = embedder.encode_document(document_screenshots, show_progress_bar=True)

similarities = embedder.similarity(query_embedding, corpus_embeddings)
top_k_indices = similarities.argsort(descending=True)[0][:10]

# Step 2: Precision Reranking
reranker = CrossEncoder("nvidia/llama-nemotron-rerank-vl-1b-v2", trust_remote_code=True)

top_k_documents = [document_screenshots[i] for i in top_k_indices]
rankings = reranker.rank(query, top_k_documents)
for rank in rankings:
    print(f"{rank['score']:.4f}\t{top_k_documents[rank['corpus_id']]}")
```

> `> from sentence_transformers import SentenceTransformer, CrossEncoder`
> `> `
> `> # Step 1: Initial Retrieval via Embeddings`
> `> embedder = SentenceTransformer("Qwen/Qwen3-VL-Embedding-2B")`
> `> `
> `> query = "revenue growth chart"`
> `> query_embedding = embedder.encode_query(query)`
> `> `
> `> document_screenshots = [`
> `>     "path/to/doc1.png",`
> `>     "path/to/doc2.png",`
> `]`
> `> corpus_embeddings = embedder.encode_document(document_screenshots, show_progress_bar=True)`
> `> `
> `> similarities = embedder.similarity(query_embedding, corpus_embeddings)`
> `> top_k_indices = similarities.argsort(descending=True)[0][:10]`
> `> `
> `> # Step 2: Precision Reranking`
> `> reranker = CrossEncoder("nvidia/llama-nemotron-rerank-vl-1b-v2", trust_remote_code=True)`
> `> `
> `> top_k_documents = [document_screenshots[i] for i in top_k_indices]`
> `> rankings = reranker.rank(query, top_k_documents)`
> `> for rank in rankings:`
> `>     print(f"{rank['score']:.4f}\t{top_k_documents[rank['corpus_id']]}")`

---

## 输入格式与配置

### 支持的输入类型

| 模态 | 接受的格式 |
| :--- | :--- |
| **文本 (Text)** | • 字符串 (Strings) |
| **图像 (Image)** | • `PIL.Image.Image` 对象<br>• 文件路径 (`"./photo.jpg"`), URL<br>• Numpy 数组、torch 张量 |
| **音频 (Audio)** | • 文件路径, URL<br>• Numpy/torch 数组<br>• 包含 `"array"` 和 `"sampling_rate"` 键的字典 |
| **视频 (Video)** | • 文件路径, URL<br>• Numpy/torch 数组<br>• 包含 `"array"` 和 `"video_metadata"` 键的字典 |
| **多模态 (Multimodal)** | • 映射模态名称到具体值的字典: `{"text": "...", "image": "..."}` |

### 处理器与模型参数配置
使用 `processor_kwargs` 和 `model_kwargs` 来控制图像分辨率边界和模型精度：

```python
model = SentenceTransformer(
    "Qwen/Qwen3-VL-Embedding-2B",
    model_kwargs={"attn_implementation": "flash_attention_2", "torch_dtype": "bfloat16"},
    processor_kwargs={"min_pixels": 28 * 28, "max_pixels": 600 * 600},
)
```

> `> model = SentenceTransformer(`
> `>     "Qwen/Qwen3-VL-Embedding-2B",`
> `>     model_kwargs={"attn_implementation": "flash_attention_2", "torch_dtype": "bfloat16"},`
> `>     processor_kwargs={"min_pixels": 28 * 28, "max_pixels": 600 * 600},`
> `)`

---

## 支持的模型列表

### 多模态嵌入模型
* `Qwen/Qwen3-VL-Embedding-2B` (2B)
* `Qwen/Qwen3-VL-Embedding-8B` (8B)
* `nvidia/llama-nemotron-embed-vl-1b-v2` (1.7B)
* `nvidia/omni-embed-nemotron-3b` (4.7B)
* `LCO-Embedding/LCO-Embedding-Omni-3B` (5B)
* `BAAI/BGE-VL-base` / `BAAI/BGE-VL-large`
* `nomic-ai/nomic-embed-multimodal-3b` (5B)

### 多模态重排模型
* `Qwen/Qwen3-VL-Reranker-2B` (2B)
* `Qwen/Qwen3-VL-Reranker-8B` (8B)
* `nvidia/llama-nemotron-rerank-vl-1b-v2` (2B)
* `jinaai/jina-reranker-m0` (2B)

---

## 更多资源

- [Sentence Transformers 文档](https://sbert.net/)
- [多模态模型训练与微调博客](https://huggingface.co/blog/train-multimodal-sentence-transformers)
- [Hugging Face v5.4 集成集合](https://huggingface.co/collections/sentence-transformers/sentence-transformers-v54-integrations)