---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-09
hide:
- navigation
tags:
- NVIDIA
- NeMo Retriever
- LanceDB
- RAG
- 多模态
title: 使用 NVIDIA NeMo Retriever、托管 NIM、LanceDB、重排及基础生成构建多模态 RAG 管道
---
### 文章背景与核心概要
本教程深入探讨了如何利用 NVIDIA NeMo Retriever 构建一个先进的多模态检索增强生成（RAG）管道。文章首先指导用户配置 Python 3.12 环境并执行基于 PDFium 的离线文本提取，随后无缝接入托管的 NVIDIA NIM 微服务，以解析复杂文档中的页面元素、表格、图表和信息图。

处理后的数据经过分块、去密和向量化处理后存储于高性能的 LanceDB 向量数据库中。在此基础上，系统结合了稠密检索、视觉语言重排（Vision-Language Reranking）以及元数据过滤功能，最后利用 Nemotron 大语言模型生成带内联引用和页面元数据的扎实回答，并通过 Recall-at-k 指标评估检索效果。

---

## 1. Environment Setup and Offline Text Extraction
## 1. 环境设置与离线文本提取

We begin by configuring the Python 3.12 environment, installing NVIDIA NeMo Retriever, and importing the required ingestion and retrieval components. We download the sample multimodal PDF, define it as the input document, and perform CPU-based offline text extraction with PDFium.
> 我们首先配置 Python 3.12 环境，安装 NVIDIA NeMo Retriever，并导入所需的摄取和检索组件。接着下载样本多模态 PDF，将其定义为输入文档，并使用 PDFium 执行基于 CPU 的离线文本提取。

```python
import sys, os, subprocess, textwrap, json, time, warnings
warnings.filterwarnings("ignore")
assert sys.version_info[:2] == (3, 12), (
   f"nemo-retriever requires Python 3.12.x (found {sys.version.split()[0]}). "
   "Colab's default runtime is 3.12; if you changed it, switch back."
)
def sh(cmd):
   print(f"$ {cmd}")
   subprocess.run(cmd, shell=True, check=False)
try:
   import nemo_retriever
   print("nemo-retriever already installed")
except ImportError:
   sh("pip install -q --ignore-installed PyJWT nemo-retriever openai")
import nemo_retriever
print("nemo-retriever version:", nemo_retriever.__version__)
from nemo_retriever import create_ingestor
try:
   from nemo_retriever.io import to_markdown, to_markdown_by_page
except ImportError:
   from nemo_retriever.common.io import to_markdown, to_markdown_by_page
try:
   from nemo_retriever.retriever import Retriever
except ImportError:
   from nemo_retriever.graph.retriever import Retriever
import pandas as pd
pd.set_option("display.max_colwidth", 160)
DOC = "multimodal_test.pdf"
if not os.path.exists(DOC):
   sh(f"curl -sL -o {DOC} "
      "https://raw.githubusercontent.com/NVIDIA/NeMo-Retriever/main/data/multimodal_test.pdf")
print("document:", DOC, os.path.getsize(DOC), "bytes")
DOCS = [DOC]
print("\n=== STAGE 1: offline text extraction (no API key) ===")
offline = (
   create_ingestor(run_mode="inprocess", allow_no_gpu=True)
   .files(DOCS)
   .extract(
       extract_text=True,
       extract_tables=False, extract_charts=False,
       extract_images=False, extract_infographics=False,
       use_page_elements=False,
       extract_page_as_image=False,
       method="pdfium",
   )
)
df_offline = offline.ingest()
print("rows:", df_offline.shape, "\ncolumns:", list(df_offline.columns))
print("\npage 1 text preview:\n", df_offline.iloc[0]["text"][:400])
```

---

## 2. Multimodal Ingestion via Hosted NIMs
## 2. 通过托管 NIM 进行多模态摄取

Next, we securely load the NVIDIA API key and define the hosted NIM endpoints for layout detection, OCR, table extraction, graphic analysis, embedding, reranking, and generation. We create a multimodal ingestion pipeline that extracts text, tables, charts, and infographics, applies token-aware chunking, deduplicates content, generates embeddings, and uploads vectors to a LanceDB table.
> 接下来，我们安全加载 NVIDIA API 密钥，并定义用于版面检测、OCR、表格提取、图形分析、嵌入、重排和生成的托管 NIM 端点。我们构建了一个多模态摄取管道，用于提取文本、表格、图表和信息图，应用基于 Token 感知的分块，对内容去重，生成向量嵌入，并将向量上传到 LanceDB 表中。

```python
from getpass import getpass
if not os.environ.get("NVIDIA_API_KEY"):
   try:
       from google.colab import userdata
       os.environ["NVIDIA_API_KEY"] = userdata.get("NVIDIA_API_KEY")
   except Exception:
       os.environ["NVIDIA_API_KEY"] = getpass("NVIDIA_API_KEY (nvapi-...): ").strip()
API_KEY = os.environ.get("NVIDIA_API_KEY", "").strip()
HAVE_KEY = API_KEY.startswith("nvapi-")
print("API key present:", HAVE_KEY)
PAGE_ELEMENTS_URL   = "https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-page-elements-v3"
OCR_URL             = "https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-ocr-v1"
TABLE_STRUCT_URL    = "https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-table-structure-v1"
GRAPHIC_ELEM_URL    = "https://ai.api.nvidia.com/v1/cv/nvidia/nemotron-graphic-elements-v1"
EMBED_URL           = "https://integrate.api.nvidia.com/v1/embeddings"
RERANK_URL          = "https://ai.api.nvidia.com/v1/retrieval/nvidia/llama-nemotron-rerank-vl-1b-v2/reranking"
CHAT_URL            = "https://integrate.api.nvidia.com/v1"
EMBED_MODEL  = "nvidia/llama-nemotron-embed-1b-v2"
RERANK_MODEL = "nvidia/llama-nemotron-rerank-vl-1b-v2"
LLM_MODEL    = "nvidia/llama-3.3-nemotron-super-49b-v1.5"
LANCEDB_URI, TABLE = "./lancedb", "colab_demo"
df = df_offline
if HAVE_KEY:
   print("\n=== STAGE 2: multimodal ingest via hosted NIMs ===")
   ing = (
       create_ingestor(
           run_mode="inprocess",
           allow_no_gpu=True,
           error_policy="collect",
       )
       .files(DOCS)
       .extract(
           extract_text=True,
           extract_tables=True,
           extract_charts=True,
           extract_infographics=True,
           extract_images=False,
           method="pdfium",
           dpi=200,
           table_output_format="markdown",
           page_elements_invoke_url=PAGE_ELEMENTS_URL,
           ocr_invoke_url=OCR_URL,
           table_structure_invoke_url=TABLE_STRUCT_URL,
           graphic_elements_invoke_url=GRAPHIC_ELEM_URL,
           api_key=API_KEY,
           request_timeout_s=120.0,
           split_config={"text": {"max_tokens": 512, "overlap_tokens": 64}},
       )
       .dedup(content_hash=True, bbox_iou=True, iou_threshold=0.45)
       .embed(
           embedding_endpoint=EMBED_URL,
           model_name=EMBED_MODEL,
           embed_model_name=EMBED_MODEL,
           api_key=API_KEY,
           input_type="passage",
           inference_batch_size=16,
           nim_http_max_concurrent=8,
       )
       .vdb_upload(
           vdb_op="lancedb",
           vdb_kwargs={
               "uri": LANCEDB_URI,
               "table_name": TABLE,
               "overwrite": True,
               "create_index": True,
               "index_type": "IVF_HNSW_SQ",
               "metric": "l2",
           },
       )
   )
   t0 = time.time()
   df = ing.ingest(show_progress=True)
   print(f"ingested in {time.time()-t0:.1f}s -> {df.shape}")
```

---

## 3. Dense Retrieval & Extraction Inspection
## 3. 稠密检索与提取检查

We inspect the extracted elements, convert the document to page-level and full Markdown, and set up a dense retriever to search the LanceDB vector index.
> 我们检查提取出的元素，将文档转换为按页及全文的 Markdown 格式，并设置稠密检索器来搜索 LanceDB 向量索引。

```python
print("\n=== Extraction inspection ===")
for col in ["tables", "charts", "infographics", "images"]:
   if col in df.columns:
       n = int(df[col].apply(lambda v: len(v) if isinstance(v, (list, tuple)) else 0).sum())
       print(f"  {col:<14} {n}")
pages = to_markdown_by_page(df)
print("\npages rendered to markdown:", list(pages.keys()))
print("\n--- page 1 markdown (first 900 chars) ---\n", pages[min(pages)][:900])
full_md = to_markdown(df)
if full_md:
   with open("extracted.md", "w") as f:
       f.write(full_md)
   print("\nfull document markdown -> extracted.md")
if HAVE_KEY:
   print("\n=== STAGE 3: dense retrieval ===")
   retriever = Retriever(
       run_mode="service",
       top_k=5,
       rerank=False,
       vdb_kwargs={"uri": LANCEDB_URI, "table_name": TABLE},
       embed_kwargs={
           "embedding_endpoint": EMBED_URL,
           "model_name": EMBED_MODEL,
           "embed_model_name": EMBED_MODEL,
           "api_key": API_KEY,
           "input_type": "query",
       },
   )
   QUERIES = [
       "Given their activities, which animal is responsible for the typos in my documents?",
       "What is the most expensive gadget and how much does it cost?",
       "Which animal is at the beach?",
   ]
   def show(hits, label=""):
       print(f"\n--- {label} ---")
       for i, h in enumerate(hits, 1):
           meta = h.get("metadata")
           if isinstance(meta, str):
               try: meta = json.loads(meta)
               except Exception: meta = {}
           page = (meta or {}).get("page_number", "?")
           score = h.get("_distance", h.get("rerank_score", ""))
           body = " ".join(str(h.get("text", "")).split())[:180]
           print(f" {i}. p{page} score={score}  {body}")
   show(retriever.query(QUERIES[0]), "single query")
   for q, hits in zip(QUERIES, retriever.queries(QUERIES, top_k=3)):
       show(hits, q[:60])
```

---

## 4. Vision-Language Reranking and Filtered Retrieval
## 4. 视觉语言重排与过滤检索

We introduce a vision-language reranking pipeline to reorder retrieval results by semantic relevance and apply text-based filters to pinpoint specific document chunks.
> 我们引入了视觉语言重排管道，根据语义相关性对检索结果进行重新排序，并应用基于文本的过滤器来精确定位特定的文档块。

```python
if HAVE_KEY:
   print("\n=== STAGE 4: retrieve + VL rerank ===")
   reranking = Retriever(
       run_mode="service",
       top_k=5,
       rerank=True,
       vdb_kwargs={"uri": LANCEDB_URI, "table_name": TABLE},
       embed_kwargs={
           "embedding_endpoint": EMBED_URL, "model_name": EMBED_MODEL,
           "embed_model_name": EMBED_MODEL, "api_key": API_KEY, "input_type": "query",
       },
       rerank_kwargs={
           "model_name": RERANK_MODEL,
           "invoke_url": RERANK_URL,
           "api_key": API_KEY,
           "refine_factor": 4,
           "batch_size": 16,
       },
   )
   try:
       show(reranking.query(QUERIES[0]), "reranked")
   except Exception as e:
       print("rerank unavailable, dense results stand:", type(e).__name__, str(e)[:160])
if HAVE_KEY:
   print("\n=== STAGE 5: filtered retrieval ===")
   try:
       hits = retriever.query(
           "gadget costs",
           top_k=5,
           vdb_kwargs={"where": "text LIKE '%Cost%'"},
       )
       show(hits, "where: text LIKE '%Cost%'")
   except Exception as e:
       print("filter push-down failed:", type(e).__name__, str(e)[:160])
   import lancedb
   tbl = lancedb.connect(LANCEDB_URI).open_table(TABLE)
   print("\nrows in LanceDB:", tbl.count_rows())
   print(tbl.to_pandas()[["text"]].head(3).to_string())
```

---

## 5. Grounded RAG Generation and Evaluation
## 5. 基于溯源的 RAG 生成与评估

We use a hosted Nemotron language model to generate answers grounded strictly in the supplied context, accompanied by citations and page metadata. Finally, we measure retrieval effectiveness using a recall-at-k evaluation.
> 我们使用托管的 Nemotron 语言模型来生成严格基于所提供上下文的答案，并附带引用和页面元数据。最后，我们使用 recall-at-k 评估指标来衡量检索的有效性。

```python
if HAVE_KEY:
   print("\n=== STAGE 6: RAG answer ===")
   from openai import OpenAI
   client = OpenAI(base_url=CHAT_URL, api_key=API_KEY)
   def rag(question, k=5):
       hits = retriever.query(question, top_k=k)
       ctx = []
       for i, h in enumerate(hits, 1):
           meta = h.get("metadata")
           if isinstance(meta, str):
               try: meta = json.loads(meta)
               except Exception: meta = {}
           ctx.append(f"[{i}] (page {(meta or {}).get('page_number','?')})\n{h.get('text','')}")
       prompt = textwrap.dedent(f"""\
           Answer the question using ONLY the numbered context below.
           Cite the sources you used as [1], [2], etc. If the context is
           insufficient, say so plainly.
           Context:
           {chr(10).join(ctx)}
           Question: {question}
           """)
       r = client.chat.completions.create(
           model=LLM_MODEL,
           messages=[{"role": "user", "content": prompt}],
           temperature=0.0, max_tokens=512,
       )
       return r.choices[0].message.content, hits
   for q in QUERIES[:2]:
       try:
           ans, _ = rag(q)
           print(f"\nQ: {q}\nA: {ans}\n" + "-" * 70)
       except Exception as e:
           print("generation failed:", type(e).__name__, str(e)[:200])
if HAVE_KEY:
   print("\n=== Recall@k check ===")
   GOLD = [
       ("which animal is jumping onto a laptop", "Cat"),
       ("what does the chart show", "Gadgets"),
       ("which animal is at the beach", "Giraffe"),
   ]
   K = 5
   hit_lists = retriever.queries([q for q, _ in GOLD], top_k=K)
   got = sum(
       any(exp.lower() in str(h.get("text", "")).lower() for h in hits)
       for (_, exp), hits in zip(GOLD, hit_lists)
   )
   print(f"recall@{K} = {got}/{len(GOLD)} = {got/len(GOLD):.2f}")
print("\nDone. Artifacts: ./lancedb (vector table), ./extracted.md (markdown).")
```

---

## Conclusion
## 结论

By completing this workflow, we established a reusable foundation for building document intelligence applications that process text, tables, charts, and visual elements through a unified retrieval pipeline. NeMo Retriever coordinates extraction, deduplication, chunking, embedding, vector database indexing, retrieval, and reranking, while hosted NVIDIA NIM services keep resource requirements lightweight.
> 通过完成此工作流，我们为构建文档智能应用程序奠定了可复用的基础，能够通过统一的检索管道处理文本、表格、图表和视觉元素。NeMo Retriever 协调了提取、去重、分块、嵌入、向量数据库索引、检索和重排，而托管的 NVIDIA NIM 服务则使资源需求保持在轻量级水平。

---

**Check out the [FULL CODES here](https://github.com/MARKTECHPOST-AI-MEDIA-INC/AI-Agents-Projects-Tutorials/blob/main/LLM%2520Projects/nvidia_nemo_retriever_advanced_multimodal_rag_Marktechpost.ipynb).** 
> **点击此处查看[完整代码](https://github.com/MARKTECHPOST-AI-MEDIA-INC/AI-Agents-Projects-Tutorials/blob/main/LLM%2520Projects/nvidia_nemo_retriever_advanced_multimodal_rag_Marktechpost.ipynb)。**

Also, feel free to follow us on **[Twitter](https://x.com/intent/follow?screen_name=marktechpost)** and don’t forget to join our **[150k+ ML SubReddit](https://www.reddit.com/r/machinelearningnews/)**, Subscribe to **[our Newsletter](https://www.aidevsignals.com/)**, and join us on **[Telegram](https://t.me/machinelearningresearchnews)**.
> 此外，欢迎在 **[Twitter](https://x.com/intent/follow?screen_name=marktechpost)** 上关注我们，加入我们拥有超 15万名成员的 **[ML SubReddit](https://www.reddit.com/r/machinelearningnews/)**，订阅 **[我们的新闻通讯](https://www.aidevsignals.com/)**，并加入我们的 **[Telegram 频道](https://t.me/machinelearningresearchnews)**。

Need to partner with us for promoting your GitHub Repo, Hugging Face Page, Product Release, or Webinar? **[Connect with us](https://forms.gle/wbash1wF6efRj8G58)**.
> 如果您需要与我们合作推广您的 GitHub 仓库、Hugging Face 页面、产品发布或网络研讨会，请**[与我们联系](https://forms.gle/wbash1wF6efRj8G58)**。

*The post [Building a Multimodal RAG Pipeline with NVIDIA NeMo Retriever, Hosted NIMs, LanceDB, Reranking, and Grounded Generation](https://www.marktechpost.com/2026/08/07/building-a-multimodal-rag-pipeline-with-nvidia-nemo-retriever-hosted-nims-lancedb-reranking-and-grounded-generation/) appeared first on [MarkTechPost](https://www.marktechpost.com).*
> *本文首发于 [MarkTechPost](https://www.marktechpost.com)，原标题为[使用 NVIDIA NeMo Retriever、托管 NIM、LanceDB、重排及基础生成构建多模态 RAG 管道](https://www.marktechpost.com/2026/08/07/building-a-multimodal-rag-pipeline-with-nvidia-nemo-retriever-hosted-nims-lancedb-reranking-and-grounded-generation/)*