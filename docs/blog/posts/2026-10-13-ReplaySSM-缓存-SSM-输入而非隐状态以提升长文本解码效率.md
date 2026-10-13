---
authors:
  - aitoboxrobot
categories:
  - arXiv论文
date: 2026-10-13
hide:
  - navigation
tags:
  - ReplaySSM
  - Mamba-2
  - 状态空间模型
  - 推理加速
title: "ReplaySSM：缓存输入而非隐状态，破局 SSM 混合模型解码吞吐瓶颈"
---

# ReplaySSM：缓存输入而非隐状态，破局 SSM 混合模型解码吞吐瓶颈

> # ReplaySSM: Cache SSM Inputs, Not State

> **arXiv:2610.13778** [cs.LG]  
> **Submitted:** October 9, 2026  
> **Authors:** Ze-Wei Liou, Harris Nover, Amey Naik, Andrii Skliar, Igor Shovkun, Ido Shahaf, Tri Dao  
> **Code Repository:** [GitHub - ReplaySSM](https://github.com/Johnny-Liou/ReplaySSM)  

### 文章背景与核心概要

状态空间模型 (State-Space Model, SSM) 凭借恒定的显存占用与线性的长文本推理效率，被视为突破传统 Transformer 架构二次方计算瓶颈的关键方向，以 Mamba-2 为代表的混合架构更是备受学界与工业界瞩目。然而在实际部署中，传统 SSM 每一生成一个 Token 都要频繁读写其庞大的循环隐状态，由此带来的高频显存 I/O 成为制约自回归解码吞吐的核心瓶颈，同时也使投机解码的状态回滚和低比特量化面临严重阻碍。为此，Tri Dao 团队联合推出的 **ReplaySSM** 另辟蹊径，提出“缓存输入而非隐状态”的创新范式：它将连续状态解耦为周期性的检查点与一段极轻量的近期输入缓冲区，在绝大多数解码步中完全免除了高昂的状态写回，将主导显存访存量腰斩。在主流推理系统 vLLM 的实操测试中，ReplaySSM 在 Mamba-2 与 Gated DeltaNet 上带来了 $1.20\times \sim 1.47\times$ 的标准解码提速，并在 120B 级大型混合模型上实现了约 $1.8\times$ 的投机解码吞吐飞跃，为超长文本的高并发落地提供了全新解题思路。

---

## 内容概要

> ## Summary

传统的状态空间模型 (State-Space Model, SSM) 通常会在推理时维护一个固定尺寸的循环隐状态。然而，在结合了注意力的混合架构大模型中，解码每生成一个 Token 都要对该隐状态进行一次完整的读取与写回，这逐渐演变成了拖累吞吐量的严重瓶颈。这种“步步更新”的急切状态管理策略，不仅引发了极其庞大的显存 I/O 访存流量与极低的计算访存比 (Arithmetic Intensity) ，还使得投机解码 (Speculative Decoding) 中的状态回滚变得异常笨重迟缓，更导致状态量化误差在后续的循环更新中不断累积放大。

> State-space models (SSMs) traditionally maintain a fixed-size recurrent state, but frequently reading and writing this state at every decoding step creates a significant bottleneck in hybrid models. This eager state management results in high memory traffic, low arithmetic intensity, inefficient speculative decoding rollbacks, and error accumulation from state quantization. 

**ReplaySSM** 针对这一难题提出了革命性的解决方案：它通过时间维度上的循环展开，创新性地将状态表征解耦为一个周期性检查点 (Periodic Checkpoint) 与一段近期 SSM 输入轻量缓冲区 (Buffer of Recent SSM Inputs) 的组合。这种解耦架构在绝大多数解码步骤中完全免去了高昂的状态写回，将主导性的隐状态显存访存量直接砍掉近一半；同时，它将复杂的投机回滚简化为极度轻量的缓冲区指针回拨操作，并支持双精度检查点设计以彻底隔绝量化舍入误差对后续状态迭代的污染。在主流大模型推理框架 vLLM 中对 Mamba-2 与 Gated DeltaNet 的实际集成评测显示，ReplaySSM 将标准解码速度提升了 $1.20\times \sim 1.47\times$ ，并在 120B 参数级大型混合模型上实现了约 $1.8\times$ 于标准投机解码的极致吞吐量提升。

> **ReplaySSM** solves this by unrolling the recurrence to represent the state as a periodic checkpoint paired with a buffer of recent SSM inputs. This decoupled architecture avoids state writes on most steps, reduces dominant state memory traffic by roughly half, transforms speculative rollback into a simple buffer-pointer operation, and allows dual-precision checkpoints to prevent quantization error from corrupting recurrent updates. Implemented within vLLM for Mamba-2 and Gated DeltaNet, ReplaySSM accelerates standard decoding by $1.20\times$ to $1.47\times$ and delivers roughly $1.8\times$ the throughput of standard speculative decoding on 120B-class models.

---

## 论文元数据

> ## Paper Metadata

| 属性 | 详情 |
| :--- | :--- |
| **主要学科** | 机器学习 (`cs.LG`) |
| **次要学科** | 人工智能 (`cs.AI`) |
| **论文备注** | 正文 11 页 (含参考文献与附录共 35 页) ，6 张图，2 张表 |
| **DOI 链接** | [10.48550/arXiv.2610.13778](https://doi.org/10.48550/arXiv.2610.13778) |
| **版权许可** | [知识共享署名 4.0 (Creative Commons Attribution 4.0)](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"><span>view license</span></a> |

> | Attribute | Detail |
> | :--- | :--- |
> | **Primary Subject** | Machine Learning (`cs.LG`) |
> | **Secondary Subjects** | Artificial Intelligence (`cs.AI`) |
> | **Comments** | 11 pages (35 pages counting references and appendix), 6 figures, 2 tables |
> | **DOI** | [10.48550/arXiv.2610.13778](https://doi.org/10.48550/arXiv.2610.13778) |
> | **License** | [Creative Commons Attribution 4.0](http://creativecommons.org/licenses/by/4.0/) <a class="has_license" href="http://creativecommons.org/licenses/by/4.0/" title="Rights to this article"><img alt="license icon" role="presentation" src="./images/345c7ad61f1b.png"><span>view license</span></a> |

---

## 论文摘要

> ## Abstract

传统状态空间模型 (SSM) 在自回归解码中维护着固定大小的循环隐状态，然而在注意力机制与 SSM 相融合的混合架构模型中，每一生成步都要频繁读写该隐状态，极易形成制约吞吐量的系统瓶颈。这种“步步更新”的急切状态管理策略造成了庞大的状态显存 I/O 访存开销与偏低的计算访存比 (Arithmetic Intensity) ，使得投机解码 (Speculative Decoding) 缺乏低成本的回滚机制，更会导致状态量化误差无休止地代入并污染后续的循环状态迭代。为此，我们提出了 **ReplaySSM**：它通过在时间维度上展开循环递归，将隐状态巧妙地解耦为“周期性保存的检查点”与“近期 SSM 输入数据的轻量缓冲区”，从而彻底将输出计算与检查点更新相分离。通过仅进行周期性检查点写入，ReplaySSM 在绝大多数解码步中完全免去了状态写回，将主导显存开销的状态访存量大致缩减了一半。与此同时，保留近期输入使得投机解码的回滚退化为极简的缓冲区指针调整，并能直接完成“仅针对输出”的高效验证，无需在显存中实体化展开任何中间隐状态。该解耦架构还支持状态双精度存储方案：绝大部分生成步采用低精度检查点供给输出计算，而底层更新则由高精度检查点维系，确保低精度量化的舍入误差永远不会反噬随后的循环更新。我们在主流服务引擎 vLLM 中为 Mamba-2 与 Gated DeltaNet 实现了 ReplaySSM。在并发服务批次大小 (Batch Size) 为 256 时，面对四款主流混合模型，ReplaySSM 相比精细调优后的 vLLM 基线实现了 $1.20$--$1.47\times$ 的标准解码加速；在两款 120B 参数级大型混合模型上，其吞吐量更达到 vLLM 原生投机解码的约 $1.8\times$。此外，相比共享单一低精度检查点，分离式的双精度状态机制显著降低了输出 KL 散度 (KL Divergence) 与下游任务的精度损失。

> State-space models (SSMs) maintain a fixed-size recurrent state, but reading and writing it at every decoding step can bottleneck hybrid models. This eager state management causes large state I/O with low arithmetic intensity, leaves speculative decoding no cheap rollback, and feeds state quantization error into subsequent recurrent updates. We introduce ReplaySSM, which unrolls the recurrence to represent the state as a checkpoint and a buffer of recent SSM inputs. This separates output computation from checkpoint updates. By updating the checkpoint periodically, ReplaySSM avoids state writes on most steps and roughly halves the dominant state memory traffic. Keeping recent inputs also makes speculative rollback a buffer-pointer operation and enables output-only verification without materializing intermediate states. The same separation allows a low-precision checkpoint to serve output computation on most steps while a higher-precision checkpoint serves recurrent updates, so rounding error in the low-precision copy never enters later updates. We implement ReplaySSM in vLLM for Mamba-2 and Gated DeltaNet. At serving batch size 256, it accelerates standard decoding by $1.20$--$1.47\times$ over a tuned vLLM baseline across four hybrid models, and delivers about $1.8\times$ the throughput of vLLM's speculative decoding on the two 120B-class models. Separate state precisions also reduce output KL divergence and downstream accuracy losses compared with a shared low-precision checkpoint.

---

## 全文获取与相关资源

> ## Full-Text and Additional Resources

* **论文 PDF：** [查看 PDF (View PDF)](https://arxiv.org/pdf/2610.13778)
* **LaTeX 源码：** [TeX 源码 (TeX Source)](https://arxiv.org/src/2610.13778)
* **在线 HTML 版本：** [HTML 版本 (HTML Version)](https://arxiv.org/html/2610.13778v1)
* **学术引用检索：** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2610.13778) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2610.13778) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2610.13778)

> * **PDF:** [View PDF](https://arxiv.org/pdf/2610.13778)
> * **LaTeX Source:** [TeX Source](https://arxiv.org/src/2610.13778)
> * **Experimental HTML:** [HTML Version](https://arxiv.org/html/2610.13778v1)
> * **External Citations:** [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2610.13778) | [Semantic Scholar](https://api.semanticscholar.org/arXiv:2610.13778) | [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2610.13778)
