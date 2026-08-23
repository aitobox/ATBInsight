---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-24
hide:
- navigation
tags:
- deepDoctection
- 文档智能
- OCR
- RAG
- 计算机视觉
title: 使用 deepDoctection 构建端到端文档智能流水线
---
### 文章背景与核心概要

在本教程中，我们将使用 **deepDoctection 1.2.x** 实现一个全面的文档智能流水线（Pipeline）。该流水线将版面检测、表格结构识别、OCR、阅读顺序重建、标注链接以及结构化导出整合到一个连贯的工作流中。我们显式配置了基于 DocLayNet 的版面检测器、Table Transformer 结构识别器以及 DocTR OCR 的分析器（Analyzer）。随后，我们检查生成的 `Page` 对象，以了解 deepDoctection 如何表示文本、图像、表格、关系、来源追溯以及阅读顺序。

此外，我们通过注册自定义对象类型并实现我们自己的 `PipelineComponent` 来扩展该框架，从而提取货币和日期实体，同时根据文档的表格特征对其进行分类。最后，我们使用 `ServiceFactory` 手动组装自定义流水线，探索过滤和服务回滚、序列化处理后的页面，并将文档标注转换为适合下游 RAG 和检索系统的有序 JSONL 文本块。

> In this tutorial, we implement a comprehensive document intelligence pipeline using **deepDoctection 1.2.x**. This pipeline combines layout detection, table structure recognition, OCR, reading-order reconstruction, annotation linking, and structured export into a single cohesive workflow. We configure the analyzer explicitly with DocLayNet-based layout detection, Table Transformer structure recognition, and DocTR OCR. We then inspect the resulting `Page` objects to understand how deepDoctection represents text, figures, tables, relationships, provenance, and reading order. 
> 
> Furthermore, we extend the framework by registering custom object types and implementing our own `PipelineComponent` to extract monetary and date entities while classifying documents based on their tabular characteristics. Finally, we manually assemble a custom pipeline with `ServiceFactory`, explore filtering and service rollback, serialize processed pages, and transform document annotations into ordered JSONL chunks suitable for downstream RAG and retrieval systems.

---

## 🛠️ 环境设置与辅助函数

我们安装所需的 deepDoctection 依赖项，配置其运行时环境，并为 Transformers 和 PEFT 应用兼容性补丁。我们下载用于教程的示例文档 PDF 和图像文件并准备输出目录，同时准备好用于可视化和多格式输入处理的辅助函数。

> We install the required deepDoctection dependencies, configure its runtime environment, and apply a compatibility patch for Transformers and PEFT. We download sample PDF and image files for the tutorial and prepare our output directories, along with helper functions for visualization and multi-format input handling.

```python
!pip install -q "deepdoctection" "transformers>=5.2.0" "timm" "python-doctr" "pdfplumber" "networkx" "lxml"
import os
os.environ["DD_USE_TORCH"]  = "True"
os.environ["DPI"]           = "200"
os.environ["LOG_LEVEL"]     = "INFO"
os.environ["ENABLE_DYNAMIC_OBJECT_TYPES"] = "False"
import json, re, textwrap
from pathlib import Path
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import HTML, display
import deepdoctection as dd
print("deepdoctection:", dd.__version__)
import transformers.integrations.peft as _hf_peft
if _hf_peft.is_peft_available():
   _hf_peft.is_peft_available = lambda: False
   print("patched: PEFT adapter lookup disabled for from_pretrained")
!mkdir -p /content/docs /content/imgs
!wget -q -O /content/docs/paper.pdf \
 https://raw.githubusercontent.com/deepdoctection/notebooks/main/sample/2312.13560.pdf
!wget -q -O /content/imgs/finance.png \
 https://raw.githubusercontent.com/deepdoctection/notebooks/main/sample/finance/1bcac3899c9cb1c0b0f650b1431d3d52_7.png
PDF = Path("/content/docs/paper.pdf")
PNG = Path("/content/imgs/finance.png")
OUT = Path("/content/out"); OUT.mkdir(exist_ok=True)
def show(img, w=16):
   if img is None: return
   plt.figure(figsize=(w, w * 1.3)); plt.axis("off"); plt.imshow(img); plt.show()
def analyze_any(pipe, path, **kw):
   """
   Dispatch correctly for a directory, a PDF, or a single image file.
   DoctectionPipe can stream a directory or a PDF from disk, but a *single*
   image has no reader — path= only supplies the file name / provenance, and
   the pixels must be handed in via bytes=. Without this you get:
     ValueError: When passing a path to a single image, bytes of the image
                 must be passed
   """
   path = Path(path)
   if path.is_dir():
       kw.setdefault("file_type", [".jpg", ".png", ".jpeg", ".tif"])
       return pipe.analyze(path=path, **kw)
   if path.suffix.lower() == ".pdf":
       return pipe.analyze(path=path, **kw)
   if path.suffix.lower() in (".png", ".jpg", ".jpeg", ".tif"):
       return pipe.analyze(path=path, bytes=path.read_bytes(), **kw)
   raise ValueError(f"unsupported input: {path}")
```

---

## ⚙️ 配置分析器（Analyzer）

我们检查 deepDoctection 的模型注册表，以验证版面模型及其支持的文档类别。我们显式配置分析器，以结合版面检测、表格分割、DocTR OCR、单词匹配、阅读顺序重建和版面链接。

> We inspect deepDoctection’s model registry to verify the layout model and its supported document categories. We explicitly configure the analyzer to combine layout detection, table segmentation, DocTR OCR, word matching, reading-order reconstruction, and layout linking.

```python
dd.print_model_infos(add_description=False, add_config=False, add_categories=False)
profile = dd.ModelCatalog.get_profile("Aryn/deformable-detr-DocLayNet/model.safetensors")
print("\nlayout model categories:", profile.categories)
print("is registered:", dd.ModelCatalog.is_registered("Aryn/deformable-detr-DocLayNet/model.safetensors"))
config_overwrite = [
   "USE_ROTATOR=False",
   "USE_LAYOUT=True",
   "USE_LAYOUT_NMS=True",
   "USE_TABLE_SEGMENTATION=True",
   "USE_TABLE_REFINEMENT=False",
   "USE_PDF_MINER=False",
   "USE_OCR=True",
   "USE_LAYOUT_LINK=True",
   "LAYOUT.WEIGHTS=Aryn/deformable-detr-DocLayNet/model.safetensors",
   "ITEM.WEIGHTS=deepdoctection/tatr_tab_struct_v2/model.safetensors",
   "ITEM.FILTER=['table']",
   "OCR.USE_DOCTR=True",
   "OCR.USE_TESSERACT=False",
   "OCR.USE_TEXTRACT=False",
   "OCR.WEIGHTS.DOCTR_WORD=doctr/db_resnet50/db_resnet50-ac60cadc.pt",
   "OCR.WEIGHTS.DOCTR_RECOGNITION=doctr/crnn_vgg16_bn/crnn_vgg16_bn-0417f351.pt",
   "SEGMENTATION.THRESHOLD_ROWS=0.4",
   "SEGMENTATION.THRESHOLD_COLS=0.4",
   "SEGMENTATION.FULL_TABLE_TILING=True",
   "WORD_MATCHING.RULE=ioa",
   "WORD_MATCHING.THRESHOLD=0.3",
   "WORD_MATCHING.MAX_PARENT_ONLY=True",
   "TEXT_ORDERING.INCLUDE_RESIDUAL_TEXT_CONTAINER=True",
   "TEXT_ORDERING.PARAGRAPH_BREAK=0.035",
   "TEXT_ORDERING.BROKEN_LINE_TOLERANCE=0.003",
   "LAYOUT_LINK.PARENTAL_CATEGORIES=['figure','table']",
   "LAYOUT_LINK.CHILD_CATEGORIES=['caption']",
]
analyzer = dd.get_dd_analyzer(config_overwrite=config_overwrite)
print("\n--- pipeline ---")
for sid, name in analyzer.get_pipeline_info().items():
   print(f"{sid}  {name}")
print("\n--- what this pipeline produces ---")
print(analyzer.get_meta_annotation())
```

---

## 🔍 执行分析并检查结果

我们在示例文档 PDF 上运行配置好的分析器，从惰性数据流（lazy data flow）中实例化生成的页面，以检查叙事文本、阅读顺序块、标注类别、图表标题关系以及结构化表格。

> We run the configured analyzer on the sample PDF, materializing the resulting pages from the lazy data flow to inspect narrative texts, reading-order chunks, annotation categories, figure-caption relationships, and structured tables.

```python
df = analyze_any(analyzer, PDF, session_id="tutorial01", max_datapoints=3)
df.reset_state()
pages = list(df)
print(f"\nparsed {len(pages)} pages")
page = pages[0]
show(page.viz(show_figures=True, show_residual_layouts=True, show_table_structure=True))
print("== narrative text ==")
print(textwrap.fill(page.text[:900], 110))
print("\n== layout blocks in reading order ==")
for doc_id, img_id, pno, ann_id, order, cat, txt in page.chunks[:12]:
   print(f"[{order:>3}] {str(cat):<15} {txt[:70]!r}")
print("\n== category histogram ==")
print(Counter(a.category_name for a in page.get_annotation()))
for fig in page.figures:
   linked = fig.get_relationship("layout_link")
   print("figure", fig.annotation_id[:8], "-> caption ids:", [i[:8] for i in linked])
if page.words:
   w = page.words[0]
   print("\nword:", w.characters, "| service:", w.service_id,
         "| model:", w.model_id, "| bbox:", [round(x) for x in w.bbox])
tbl_pages = [p for p in pages if p.tables]
if tbl_pages:
   t = tbl_pages[0].tables[0]
   print(f"table {t.number_of_rows}x{t.number_of_columns}, "
         f"max_row_span={t.max_row_span}, max_col_span={t.max_col_span}")
   display(HTML(t.html))
   for row in t.csv[:5]:
       print([c[:22] for c in row])
   for c in t.cells[:5]:
       print(f"  r{c.row_number} c{c.column_number} "
             f"(span {c.row_span}x{c.column_span}) {c.text[:40]!r}")
else:
   print("no table on these pages — the finance.png sample below has one")
```

---

## 🛠️ 注册自定义对象类型与流水线组件

我们为提取到的货币提及、日期提及和文档风格（flavor）分类注册自定义对象类型，并实现一个自定义流水线组件来动态生成这些摘要。

> We register custom object types for extracted monetary mentions, date mentions, and document flavor classifications, implementing a custom pipeline component to generate these summaries dynamically.

```python
@dd.object_types_registry.register("CustomKey")
class CustomKey(dd.ObjectTypes):
   """Custom summary keys — must be registered to be serialisable."""
   MONEY_MENTIONS = "money_mentions"
   DATE_MENTIONS  = "date_mentions"
   DOC_FLAVOUR    = "doc_flavour"
@dd.object_types_registry.register("FlavourLabel")
class FlavourLabel(dd.ObjectTypes):
   TABULAR   = "tabular"
   NARRATIVE = "narrative"
   MIXED     = "mixed"
MONEY = re.compile(r"(?:[$€£]\s?\d[\d,.]*|\d[\d,.]*\s?(?:USD|EUR|GBP|million|bn))")
DATE  = re.compile(r"\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2}|"
                  r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{1,2},?\s+\d{4})\b")
class EntityAndFlavourService(dd.PipelineComponent):
   def __init__(self, name="entity_flavour", tabular_ratio=0.25):
       self.tabular_ratio = tabular_ratio
       super().__init__(name)
   def serve(self, dp: dd.Image) -> None:
       page = dd.Page.from_image(dp, text_container=dd.LayoutLabel.WORD)
       text = page.text_no_line_break
       money = sorted(set(MONEY.findall(text)))
       dates = sorted(set(DATE.findall(text)))
       tables = page.tables
       table_area = sum((b[2] - b[0]) * (b[3] - b[1]) for b in (t.bbox for t in tables))
       ratio = table_area / float(page.width * page.height or 1)
       flavor = (FlavourLabel.TABULAR if ratio > self.tabular_ratio
                  else FlavourLabel.NARRATIVE if not tables
                  else FlavourLabel.MIXED)
       self.dp_manager.set_summary_annotation(
           summary_key=CustomKey.MONEY_MENTIONS, summary_name=CustomKey.MONEY_MENTIONS,
           summary_value=money)
       self.dp_manager.set_summary_annotation(
           summary_key=CustomKey.DATE_MENTIONS, summary_name=CustomKey.DATE_MENTIONS,
           summary_value=dates)
       self.dp_manager.set_summary_annotation(
           summary_key=CustomKey.DOC_FLAVOUR, summary_name=flavor,
           summary_score=round(ratio, 4))
   def clone(self):
       return self.__class__(self.name, self.tabular_ratio)
   def get_meta_annotation(self) -> dd.MetaAnnotation:
       return dd.MetaAnnotation(
           image_annotations=(),
           sub_categories={},
           relationships={},
           summaries=(CustomKey.MONEY_MENTIONS, CustomKey.DATE_MENTIONS, CustomKey.DOC_FLAVOUR),
       )
for k in (CustomKey.MONEY_MENTIONS, CustomKey.DATE_MENTIONS, CustomKey.DOC_FLAVOUR):
   dd.Page.add_attribute_name(k)
```

---

## 🎛️ 组装自定义流水线与服务回滚

我们使用 `ServiceFactory` 手动组装 deepDoctection 流水线，配置入站过滤器，并在标注上测试撤销（undo）操作。

> We manually assemble a deepDoctection pipeline using `ServiceFactory`, configure inbound filters, and test undo operations on annotations.

```python
from deepdoctection.analyzer import cfg, ServiceFactory
cfg.freeze(False)
cfg.USE_TABLE_SEGMENTATION = True
cfg.freeze(True)
components = []
layout_detector = ServiceFactory.build_layout_detector(cfg, mode="LAYOUT")
components.append(ServiceFactory.build_layout_service(cfg, detector=layout_detector, mode="LAYOUT"))
components.append(ServiceFactory.build_layout_nms_service(cfg))
item_detector = ServiceFactory.build_layout_detector(cfg, mode="ITEM")
components.append(ServiceFactory.build_sub_image_service(cfg, detector=item_detector, mode="ITEM"))
components.append(ServiceFactory.build_table_segmentation_service(cfg, detector=item_detector))
word_detector = ServiceFactory.build_doctr_word_detector(cfg)
components.append(ServiceFactory.build_doctr_word_detector_service(word_detector))
components.append(ServiceFactory.build_text_extraction_service(cfg, ServiceFactory.build_ocr_detector(cfg)))
components.append(ServiceFactory.build_word_matching_service(cfg))
components.append(ServiceFactory.build_text_order_service(cfg))
components.append(EntityAndFlavourService())
custom_pipe = dd.DoctectionPipe(pipeline_component_list=components)
print("\ncustom pipeline:", list(custom_pipe.get_pipeline_info().values()))
df2 = analyze_any(custom_pipe, PNG)
df2.reset_state()
fin_page = next(iter(df2))
print("flavour  :", fin_page.doc_flavour)
print("money    :", fin_page.money_mentions[:10])
print("dates    :", fin_page.date_mentions[:10])
show(fin_page.viz(show_table_structure=True), w=13)
def skip_if_no_table(dp: dd.Image) -> bool:
   return "table" not in {a.category_name for a in dp.get_annotation()}
components[-1].set_inbound_filter(skip_if_no_table)
det_sid = next(sid for sid, n in analyzer.get_pipeline_info().items()
              if n.startswith("image_doctr"))
det_comp = analyzer.get_pipeline_component(service_id=det_sid)
df_undo = det_comp.undo(dd.DataFromList([p.base_image for p in pages]))
df_undo.reset_state()
undone = list(df_undo)
print("annotations before/after undo:",
     len(pages[0].get_annotation()),
     len(dd.Page.from_image(undone[0]).get_annotation()))
```

---

## 💾 针对 RAG 的序列化与导出

我们将每个处理后的页面序列化为 JSON（不嵌入原始图像数据），验证往返持久性（round-trip persistence），并从文本块和表格 HTML 结构生成可用于 RAG 的 JSONL 块。

> We serialize each processed page to JSON without embedding raw image data, verify round-trip persistence, and generate RAG-ready JSONL chunks from text blocks and table HTML structures.

```python
for i, p in enumerate(pages):
   p.save(image_to_json=False, path=OUT / f"page_{i}.json")
restored = dd.Page.from_file(str(OUT / "page_0.json"))
print("round-trip:", len(restored.get_annotation()), "of",
     len(pages[0].get_annotation()), "annotations restored")
records = []
for p in pages:
   for doc_id, img_id, pno, ann_id, order, cat, txt in p.chunks:
       if txt and txt.strip():
           records.append({"document_id": doc_id, "page": pno, "order": order,
                           "category": str(cat), "annotation_id": ann_id, "text": txt})
   for t in p.tables:
       records.append({"document_id": p.document_id, "page": p.page_number,
                       "order": -1, "category": "table_html",
                       "annotation_id": t.annotation_id, "text": t.html})
(OUT / "chunks.jsonl").write_text("\n".join(json.dumps(r) for r in records))
print(f"\n{len(records)} chunks -> {OUT/'chunks.jsonl'}")
print(json.dumps(records[0], indent=2)[:400])
```

---

## 📌 结论

我们对 deepDoctection 如何将多个文档分析模型和基于规则的服务编排成可配置的处理流水线有了实用的理解。通过超越简单的执行——检查模型注册、控制各个服务、访问结构化标注、提取表格以及编写自定义流水线组件——我们获得了对复杂文档工作流的精确控制。最后，生成干净的、可用于 RAG 的 JSONL 块，为构建高级搜索、信息提取和检索增强生成（RAG）应用程序奠定了坚实的基础。

> We have developed a practical understanding of how deepDoctection orchestrates multiple document-analysis models and rule-based services into a configurable processing pipeline. By going beyond simple execution—inspecting model registrations, controlling individual services, accessing structured annotations, extracting tables, and writing custom pipeline components—we gained precise control over complex document workflows. Finally, generating clean RAG-ready JSONL chunks sets a robust foundation for building advanced search, information extraction, and retrieval-augmented generation applications.

---

<hr/>

查看 **[完整代码（点击这里）](https://github.com/MARKTECHPOST-AI-MEDIA-INC/AI-Agents-Projects-Tutorials/blob/main/Computer%2520Vision/deepdoctection_advanced_document_intelligence_pipeline_Marktechpost.ipynb)**。

欢迎在 **[Twitter](https://x.com/intent/follow?screen_name=marktechpost)** 上关注我们，加入我们拥有 **[150k+ 成员的 ML SubReddit](https://www.reddit.com/r/machinelearningnews/)**，并订阅 **[我们的通讯](https://magic.beehiiv.com/v1/f5e63dd4-5653-4f09-83e2-321a8b1ba526?email={{email}})**。您也可以加入我们的 **[Telegram](https://t.me/machinelearningresearchnews)** 频道！

需要与我们合作推广您的 GitHub 仓库、Hugging Face 页面、产品发布或网络研讨会吗？ **[点此与我们联系](https://forms.gle/wbash1wF6efRj8G58)**。

The post [Building an End-to-End Document Intelligence Pipeline with deepDoctection](https://www.marktechpost.com/2026/08/23/building-an-end-to-end-document-intelligence-pipeline-with-deepdoctection/) appeared first on [MarkTechPost](https://www.marktechpost.com).