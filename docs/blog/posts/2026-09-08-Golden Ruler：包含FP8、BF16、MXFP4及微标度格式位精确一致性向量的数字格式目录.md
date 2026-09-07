---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-09-08
hide:
- navigation
tags:
- 数字格式
- 硬件架构
- FP8
- 混精度计算
- 验证套件
title: Golden Ruler：包含FP8、BF16、MXFP4及微标度格式位精确一致性向量的数字格式目录
---
### 文章背景与核心概要
机器学习硬件的快速发展引入了大量的数字格式，包括 FP8（E4M3 和 E5M2）、BF16、MXFP4、微标度块格式以及众多研究变体。这种碎片化超出了供应商中立、位精确参考资料的发展速度，导致工程师在不同硬件加速器之间移植模型时经常遇到静默分歧（silent divergences）。

为了应对这一挑战，“Golden Ruler”作为数字格式的综合注册表和验证套件应运而生。它提供了 109 种格式的目录、六个位精确一致性包、IEEE P3109 v3.2.0 交叉映射，以及用于跨包完整性检查的严格验证与锚定机制。本文严格定位为注册表填充工作——不提出新格式，不作模型准确性声明，也不断言优于任何供应商的实现。

---

## 📌 Summary

> The rapid evolution of machine learning hardware has introduced a proliferation of numeric formats—including **FP8** (E4M3 and E5M2), **BF16**, **MXFP4**, microscaling block formats, and numerous research variants. This fragmentation has outpaced the availability of vendor-neutral, bit-exact reference material, often leading engineers to encounter silent divergences when porting models across different hardware accelerators.
> 
> To address this challenge, *Golden Ruler* serves as a comprehensive registry and validation suite for numerical formats. It provides:
* **A Catalog of 109 Formats:** Spanning 12 distinct clusters, including the TNF, BNF, and GF-T ladders, with decimal representations folded into IEEE.
* **Six Bit-Exact Conformance Packs:** Covering GF16, MXFP4 elements, BF16, FP8 E4M3, FP8 E5M2, and E8M0 block scales.
* **IEEE P3109 v3.2.0 Cross-Walk:** Mapping each conformance pack directly to its corresponding standards-track configured format.
* **Rigorous Verification & Anchors:** Each pack is a self-contained JSON document featuring a SHA-256 fingerprint, a shared row schema, and an anchor vector encoding the mathematical identity $\phi^2 + 1/\phi^2 = 3$ as a cross-pack sanity check. Cross-validation is performed against `ml_dtypes 0.5.4` (Google/JAX).
> 
> *Note: This work is framed strictly as registry filling—it does not propose new formats, make model-accuracy claims, or assert superiority over any vendor's implementation.*

---

## 📂 Access and Resources

> * **Paper & PDF:** [arXiv:2606.09686](https://arxiv.org/abs/2606.09686) | [Direct PDF Link](https://arxiv.org/pdf/2606.09686)
* **Source Code & Artifacts:** [GitHub Repository (`gHashTag/t27`)](https://github.com/gHashTag/t27)
* **Experimental HTML Version:** [arXiv HTML Viewer](https://arxiv.org/html/2606.09686v3)

---

## 📋 Additional Metadata

> * **Submission History:**
  * `[v1]` Mon, 8 Jun 2026
  * `[v2]` Mon, 22 Jun 2026
  * `[v3]` Fri, 4 Sep 2026 *(Retitled to remove format count from the title; updated catalog size to 109 formats across 12 clusters; corrected Section 6 regarding `tt-trinity-corona` post-silicon status).*
* **Subjects:** Hardware Architecture (`cs.AR`), Artificial Intelligence (`cs.AI`), Mathematical Software (`cs.MS`), Performance (`cs.PF`), Numerical Analysis (`math.NA`)
* **Classifications:** 
  * *MSC:* 65Y04, 68N20
  * *ACM:* G.1.0; D.3.4; B.2.4