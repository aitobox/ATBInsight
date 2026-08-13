---
authors:
- aitoboxrobot
categories:
- arXiv论文
date: 2026-08-14
hide:
- navigation
tags:
- RAG
- 大语言模型
- 基准测试
- 指令遵循
- 企业级AI
title: EnterpriseRAG：基准测试大模型在非理想企业检索条件下的指令遵循与鲁棒性
---
### 文章背景与核心概要

企业级检索增强生成（RAG）系统在实际生产环境中往往面临显著的可靠性差距。虽然大语言模型（LLM）在满足单个约束条件时的准确率大约能达到 80%，但**同时满足所有要求的响应比例仅为 26.8%**，这暴露出高达 57 个百分点的编排性能差距。

传统的基准测试通常假设检索结果十分纯净且查询较为简单，无法真实还原混乱的现实生产环境。为了解决这一痛点，作者推出了 **EnterpriseRAG**，这是一个严格的基准测试集，包含来自六个不同领域的 983 个经专家验证的样本。EnterpriseRAG 系统性地评估了大模型在应对以下三种主要失效模式时的表现：1. 检索噪声；2. 知识空白；3. 事实冲突（并结合了复杂指令）。

对 13 个最先进大模型的评估表明，模型在指令遵循能力上出现了严重坍塌——高单项约束满足率严重掩盖了其糟糕的整体合规性。研究结果表明，即便具备增强推理能力，强大的企业级 RAG 系统仍然需要明确的上下文感知协议和校准判断。该基准测试和评估框架将在论文发表后开源。

---

# EnterpriseRAG: Benchmarking LLM Instruction Adherence and Robustness under Non-Ideal Enterprise Retrieval

**arXiv:** [2608.11584](https://arxiv.org/abs/2608.11584) [cs.AI]  
**Submitted:** August 12, 2026  
**Authors:** Huiqi Miao, Xinbao Sun, Bo Wang, Fanyu Meng, Lijun Mei, Na Wu, Di Jin, Chao Deng, Junlan Feng  

---

## 📌 Summary

> Enterprise Retrieval-Augmented Generation (RAG) deployments often experience a significant reliability gap in production environments. While Large Language Models (LLMs) can satisfy individual constraints roughly 80% of the time, **only 26.8% of responses meet all requirements simultaneously**, uncovering a massive 57-point orchestration gap. 
> 
> Conventional benchmarks typically assume clean retrieval paired with simplistic queries, failing to replicate messy, real-world conditions. To address this, the authors introduce **EnterpriseRAG**, a rigorous benchmark comprising 983 expert-validated samples across six distinct domains. EnterpriseRAG systematically evaluates LLMs against three major failure modes:
> 1. **Retrieval noise**
> 2. **Knowledge gaps**
> 3. **Factual conflicts** (combined with complex instructions)
> 
> Evaluations across 13 state-of-the-art LLMs demonstrate a severe collapse in instruction adherence—where high per-constraint satisfaction rates heavily mask poor holistic compliance. The findings indicate that even with reasoning-enhanced inference, robust enterprise RAG systems demand explicit context-aware protocols and calibrated judgment. The benchmark and evaluation framework will be made publicly available upon publication.

---

## 👥 Authors & Affiliations

> * Huiqi Miao
> * Xinbao Sun
> * Bo Wang
> * Fanyu Meng
> * Lijun Mei
> * Na Wu
> * Di Jin
> * Chao Deng
> * Junlan Feng

---

## 🔗 Additional Resources

> * [View PDF](https://arxiv.org/pdf/2608.11584)
> * [HTML Version (Experimental)](https://arxiv.org/html/2608.11584v1)
> * [TeX Source](https://arxiv.org/src/2608.11584)
> * [DOI Reference](https://doi.org/10.48550/arXiv.2608.11584)

---

## 🗂️ Citation & References

> * **BibTeX Citation:** Available via the [arXiv Abstract Page](https://arxiv.org/abs/2608.11584).
> * **External Tools:** 
>   * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2608.11584)
>   * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2608.11584)
>   * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2608.11584)