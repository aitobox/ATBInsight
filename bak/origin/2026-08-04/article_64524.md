# Open Letters About AI Development

> **Executive Summary:** This post summarizes a recent wave of prominent open letters and industry statements concerning the future of AI development. It highlights the fault lines between major tech companies regarding **open-weight models**, the controversial practice of **model distillation**, and growing concerns over **automated AI progress and safety regulation**.

---

*Originally published as part of [Simon Willison's sponsors-only newsletter](https://simonwillison.net/2026/Aug/2/july-newsletter/).*

---

## 1. Open Weights and American AI Leadership

Published on July 24th and shepherded by Microsoft, the **[Open Weights and American AI Leadership](https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/)** letter was signed by 235 AI-adjacent companies—including NVIDIA (marked by Jensen Huang's [first-ever tweet](https://twitter.com/jensenhuang/status/2080643682408321103)), Amazon, Y Combinator, The Linux Foundation, and later, OpenAI.

This letter appears designed to counter [instincts](https://www.axios.com/2026/07/20/ai-us-china-open-source-kimi) by the U.S. government to restrict or ban open-weight models over "safety" concerns—a plausible fear given [what happened to Claude Fable 5](https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/).

> "Relying solely on closed models is not inherently safe: they can be breached, misused, or fail in ways that outsiders cannot detect. And concentrating advanced AI capabilities behind a small number of closed models compounds that risk. It results in a small number of single points of failure, weakens competition, and leaves critical technology in the hands of a few providers. Open weight models, on the other hand, allow a broad community of researchers and developers to examine their behavior, identify vulnerabilities, develop safeguards, and improve them over time."

### A Stance on Distillation
Notably, the letter explicitly supports **distillation** (the practice of training a model on the outputs of another):

> "In shaping this ecosystem, policymakers should be careful not to conflate legitimate model-development techniques with misappropriation. Distillation, or the practice of using one model’s outputs to help train or improve another, is a widely used technique for model improvement, evaluation, and validation..."

---

## 2. Anthropic's Counter-Position

Significantly absent from the Microsoft-led letter was **Anthropic**. Three days later, they published their own response: **[Our position on open-weights models](https://www.anthropic.com/news/position-open-weights-models)**. 

CEO Dario Amodei doubled down on:
* The risks of authoritarian governments building models more powerful than those in the U.S.
* The danger of models being "misused to carry out cyberattacks or biological attacks."
* A call to **"crack down on industrial-scale distillation operations."**

At the same time, Amodei clarified that "Anthropic has never advocated for a ban on open-weights models."

---

## 3. Pacing the Frontier

On July 28th, another significant document, **[Pacing the Frontier](https://www.pacingthefrontier.com)**, was published with signatures from 1,324 employees of frontier AI companies. Notable signatories include:
* **Jakub Pachocki** (Chief Scientist, OpenAI)
* **Ilya Sutskever** (Safe Superintelligence Inc, formerly OpenAI)
* **Dario Amodei** (Anthropic)
* **Jack Clark** (Anthropic)

### Core Message
> "We request that the U.S. government support an international effort to develop the technical and governance tools needed to deliberately pace the frontier of automated AI development."

The signatories are responding to intense competitive pressure coupled with the acceleration of AI progress driven by automated AI research. This risk is already tangible:
* Anthropic produces [80% of their code with Claude Code](https://www.anthropic.com/institute/recursive-self-improvement).
* OpenAI used Sol to [reduce end-to-end serving costs by 20%](https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/).
* Kimi K3 [designed a chip to serve a nano model built on its own architecture](https://www.kimi.com/blog/kimi-k3#chip-design).

---

**Tags:** [anthropic](https://simonwillison.net/tags/anthropic) | [generative-ai](https://simonwillison.net/tags/generative-ai) | [openai](https://simonwillison.net/tags/openai) | [ai](https://simonwillison.net/tags/ai) | [llms](https://simonwillison.net/tags/llms) | [ai-ethics](https://simonwillison.net/tags/ai-ethics)