---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-19
hide:
- navigation
tags:
- 大语言模型
- 工具调用
- 模型安全
- 提示词工程
- 假信息传播
title: 工具返回结果比纯文本更具权威性吗？基于 Claude Opus 5 针对合成赋值任务中虚假声明采纳的三项前瞻性研究
---
### 文章背景与核心概要

随着语言模型越来越多地从它们写入的相同数据存储中读取数据，先前仅由断言产生的信息可能会在后期伪装成检索到的工具结果返回。本文探讨了在合成查找任务中，承载未经证实赋值的消息包形式是否会影响模型对虚假声明的采纳。

该研究使用 **Claude Opus 5** 进行了三项前瞻性研究，评估了模型对先前助手断言与结构化工具结果的反应差异：
* **探索性研究：** 当不存在目标声明或使用助手断言时，未出现虚假代码采纳现象。然而，当通过工具结果记录（14/24）或未校验的元数据包装器（15/24）引入该声明时，采纳率急剧上升。
* **预注册复现：** 成功复现了工具结果与助手断言之间的显著差距（7/24 对比 0/24，$p = 0.0047$），尽管相隔数天运行的绝对采纳率有所下降。
* **实时文本对照研究：** 当与放置在同一最终用户轮次中的已声明行内文本进行对比时，原生工具结果的位置并非必需——行内文本实现了 60/60 的采纳率，而工具结果条件产生了 57/60。

**结论：** 研究结果并未证明工具结果完全没有影响；相反，它们表明虚假声明的采纳并不严格需要原生工具结果的位置，并且与已声明的行内文本相比，这种特定设置并未表现出对工具包更高的行为权重。

---

## 文档元数据与资源 (Document Metadata & Resources)

* **评论：** 20 页，2 张图表。包含两项文档预注册研究、精确提示词以及完整的程序披露。
* **许可证：** [知识共享署名 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
* **链接：** 
  * [查看 PDF](https://arxiv.org/pdf/2608.14992)
  * [HTML 版本（实验性）](https://arxiv.org/html/2608.14992v1)
  * [TeX 源码](https://arxiv.org/src/2608.14992)

> **Comments:** 20 pages, 2 figures. Includes two document-preregistered studies, exact prompts, and complete program disclosure.
> **License:** [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png">
> **Links:** 
>   * [View PDF](https://arxiv.org/pdf/2608.14992)
>   * [HTML Version (Experimental)](https://arxiv.org/html/2608.14992v1)
>   * [TeX Source](https://arxiv.org/src/2608.14992)

---

## 提交历史 (Submission History)

* **[v1]** 2026年8月15日 星期六 02:43:35 UTC *(1,616 KB)*

> * **[v1]** Sat, 15 Aug 2026 02:43:35 UTC *(1,616 KB)*