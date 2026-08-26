---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-27
hide:
- navigation
tags:
- 音频转乐谱
- 音乐信息检索
- 深度学习
- 数据集
- 多媒体
title: 基于预训练特征、数据增强与全新 SheetSage-A2S 数据集的音频转乐谱系统
---
### 文章背景与核心概要
传统的音频转乐谱（Audio-to-Score, A2S）系统长期以来主要集中于古典音乐领域，而对流行音乐的探索相对不足。为了填补这一空白，本文作者团队推出了 SheetSage-A2S 数据集——这是首个专门用于流行音乐 A2S 研究的大规模数据集，涵盖来自 6,066 首独特歌曲的 9,468 个音频片段，总时长达 61 小时。

在技术实现上，该研究引入了数据增强策略以及面向音乐音频的预训练特征提取模型 **MuQ**，显著提升了模型的泛化能力与特征表征水平。实验结果表明，该框架在古典音乐四重奏数据集上的符号错误率（SER）大幅降至 4.98%（远超此前 15.3% 的 SOTA 水平），同时在全新的流行音乐数据集上也创下了 20.92% SER 的优秀基准。

> Existing audio-to-score (A2S) systems have historically concentrated on classical music, leaving popular music largely underexplored. This paper introduces the **SheetSage-A2S Dataset**—the first of its kind for popular music A2S research, containing 61 hours of audio across 9,468 clips from 6,066 unique songs. By incorporating data augmentation and **MuQ** (a pre-trained feature-extraction model for music audio), the authors significantly improve model generalization and feature extraction. The proposed framework achieves a remarkable 4.98% symbol error rate (SER) on classical music quartets (outperforming the previous state-of-the-art 15.3% SER) and sets a strong baseline of 20.92% SER on the new popular music dataset.

---

## 📌 摘要 (Summary)

> Existing audio-to-score (A2S) systems have historically concentrated on classical music, leaving popular music largely underexplored. This paper introduces the **SheetSage-A2S Dataset**—the first of its kind for popular music A2S research, containing 61 hours of audio across 9,468 clips from 6,066 unique songs. By incorporating data augmentation and **MuQ** (a pre-trained feature-extraction model for music audio), the authors significantly improve model generalization and feature extraction. The proposed framework achieves a remarkable 4.98% symbol error rate (SER) on classical music quartets (outperforming the previous state-of-the-art 15.3% SER) and sets a strong baseline of 20.92% SER on the new popular music dataset.

---

## 📋 论文详情 (Paper Details)

| 元数据 | 详情 |
| :--- | :--- |
| **主要学科** | 声音 (`cs.SD`) |
| **交叉学科** | 人工智能 (`cs.AI`)、多媒体 (`cs.MM`) |
| **提交日期** | 2026年8月6日（最近修订：2026年8月25日） |
| **收录会议** | 第34届ACM国际多媒体会议 (MM '26) |
| **DOI** | [10.48550/arXiv.2608.06165](https://doi.org/10.48550/arXiv.2608.06165) |

---

## 🔍 摘要原文 (Abstract)

> Existing audio-to-score (A2S) systems primarily focus on classical music, and the application to popular music remains underexplored. This paper first presents the new SheetSage-A2S Dataset, which includes 61 hours of audio with \*\*kern score encodings for 9,468 clips originating from 6,066 unique songs, the first of its kind to facilitate A2S research for popular music. Additionally, we improve on existing A2S approaches by using data augmentation and MuQ, a pretrained feature-extraction model for music audio, to enhance generalisation abilities and extract meaningful audio features. Results show that the proposed A2S model achieves 4.98% symbol error rate (SER) on the Quartets collection for classical music, which significantly outperforms the 15.3% SER from the existing state-of-the-art (Alfaro-Contreras et al. 2024). Additionally, our model achieves 20.92% SER on the SheetSage-A2S dataset for popular music, serving as a strong benchmark for future research. The dataset, model, and code are made publicly available at [this link](https://github.com/Multimodal-Music-Research-Lab/SheetSage2Kern_model).

---

## 🛠️ 核心贡献 (Key Contributions)

1. **全新数据集 (SheetSage-A2S)：** 提供了 61 小时的对齐音频与 \*\*kern 乐谱编码格式，有效填补了流行音乐转谱研究领域的空白。
2. **先进的特征提取与增强技术：** 结合了用于鲁棒音乐音频特征表示的 MuQ 模型与全面的数据增强策略。
3. **最先进的性能表现：** 将古典音乐四重奏的符号错误率（SER）大幅降至 **4.98%**（此前基准为 15.3%），并为流行音乐转谱建立了一个稳固的 **20.92% SER** 性能基准。

> 1. **New Dataset (SheetSage-A2S):** Bridges the gap in popular music transcription by providing 61 hours of aligned audio and \*\*kern score formats.
> 2. **Advanced Feature Extraction & Augmentation:** Utilizes MuQ for robust music audio feature representation alongside comprehensive data augmentation strategies.
> 3. **State-of-the-Art Performance:** Slashes the symbol error rate (SER) on classical music quartets down to **4.98%** (compared to the previous 15.3% benchmark) and establishes a solid baseline of **20.92% SER** for popular music transcription.

---

<img alt="license icon" role="presentation" src="./images/fb423b2203a9.png" style="display:none;" />