---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-21
hide:
- navigation
tags:
- Medical Imaging
- LoRA
- MedSAM3
- Few-Shot Learning
- Image Segmentation
title: 只需少数几个样本：MedSAM3高标注效率LoRA微调的实证研究
---
### 文章背景与核心概要
医学图像分割对于治疗规划和疾病评估等临床工作流程至关重要。虽然专业的分割工具能够取得出色的性能，但它们的训练需要大量标注好的数据集。尽管医学基础模型通过大规模预训练减轻了这种标注负担，但它们的零样本（zero-shot）性能仍然有限。

本文研究了**低秩自适应（Low-Rank Adaptation, LoRA）**技术，旨在利用极少量的专家标注数据，高效地对**MedSAM3**进行特定任务的微调。通过在包含CT和MRI模态的AMOS22数据集上进行评估，作者证明了仅使用**10个标注病例**进行训练，就能取得与依赖海量数据训练的专业系统极具竞争力的性能。此外，该方法还能有效地扩展到新的临床领域（如心脏MRI分割），并且与nnU-Net等标准流程相比，显著缩短了训练时间。

---

# A Few Cases Are All You Need: An Empirical Study of Annotation-Efficient LoRA Fine-Tuning of MedSAM3

* **arXiv ID:** [arXiv:2608.18731](https://arxiv.org/abs/2608.18731) [cs.CV]
* **Submitted:** August 19, 2026
* **Authors:** Sachin Dudda Nagaraju, Bendik Skarre Abrahamsen, Ashkan Moradi, Mattijs Elschot
* **Subjects:** Computer Vision and Pattern Recognition (`cs.CV`); Artificial Intelligence (`cs.AI`)

---

## 📌 Summary

Medical image segmentation is essential for clinical workflows such as treatment planning and disease assessment. While specialist segmentation tools achieve strong performance, they require large annotated datasets for training. Although medical foundation models reduce this annotation burden via large-scale pretraining, their zero-shot performance remains limited. 

This paper investigates **Low-Rank Adaptation (LoRA)** for efficiently specializing **MedSAM3** with minimal expert-annotated data. Evaluating on the AMOS22 dataset across CT and MRI modalities, the authors demonstrate that training on **just 10 annotated cases** yields performance highly competitive with specialist systems trained on orders of magnitude more data. Furthermore, the approach extends effectively to new clinical domains (such as cardiac MRI segmentation) and reduces training times significantly compared to standard pipelines like nnU-Net.

---

## 🔬 Key Findings & Results

* **Annotation Efficiency:** Using only **10 annotated cases**, the fine-tuned models achieve performance competitive with traditional specialist systems trained on over $100\times$ more data.
* **Challenging Anatomies:** For gallbladder segmentation—a task where existing tools fail almost completely (Dice $0.0004$)—LoRA fine-tuning achieves reliable performance (Dice $0.68$ for CT and $0.59$ for MRI).
* **Core Organs:** For standard abdominal organs (liver, kidneys, and spleen), performance remains within **5–10%** of benchmark tools (like MRSegmentator) while consuming a fraction of the annotation effort.
* **Cross-Domain Generalization:** External validation on the Whole Heart Segmentation dataset confirms that the approach successfully adapts to cardiac segmentation (beyond the baseline scope of TotalSegmentator and MRSegmentator) with only 10 cases.
* **Computational Efficiency:** Training requires only **3–5 hours per organ on a single GPU**, running approximately **$2–3\times$ faster than nnU-Net**.

> ## 📌 摘要
> 
> Medical image segmentation is essential for clinical workflows such as treatment planning and disease assessment. While specialist segmentation tools achieve strong performance, they require large annotated datasets for training. Although medical foundation models reduce this annotation burden via large-scale pretraining, their zero-shot performance remains limited. 
> 
> This paper investigates **Low-Rank Adaptation (LoRA)** for efficiently specializing **MedSAM3** with minimal expert-annotated data. Evaluating on the AMOS22 dataset across CT and MRI modalities, the authors demonstrate that training on **just 10 annotated cases** yields performance highly competitive with specialist systems trained on orders of magnitude more data. Furthermore, the approach extends effectively to new clinical domains (such as cardiac MRI segmentation) and reduces training times significantly compared to standard pipelines like nnU-Net.

> ## 🔬 关键发现与结果
> 
> * **标注效率：** 仅使用**10个标注病例**，微调后的模型就能取得与使用多达$100\times$以上数据训练的传统专业系统相媲美的性能。
> * **具有挑战性的解剖结构：** 对于胆囊分割这一现有工具几乎完全失效的任务（Dice仅为$0.0004$），LoRA微调实现了可靠的性能（CT的Dice为$0.68$，MRI的Dice为$0.59$）。
> * **核心器官：** 对于标准的腹部器官（肝脏、肾脏和脾脏），其性能保持在基准工具（如MRSegmentator）的**5–10%**以内，而标注成本仅为后者的一小部分。
> * **跨领域泛化：** 在全心分割（Whole Heart Segmentation）数据集上的外部验证证实，该方法仅需10个病例即可成功适应心脏分割任务（超出了TotalSegmentator和MRSegmentator的基线范围）。
> * **计算效率：** 每个器官在单块GPU上仅需**3–5小时**的训练时间，运行速度比nnU-Net快大约**$2–3\times$**。