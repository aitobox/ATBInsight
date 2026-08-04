# Advancing the Price-Performance Frontier with GPT-5.6

## Summary
OpenAI has announced substantial price cuts for its GPT-5.6 model lineup—featuring a 20% reduction for **GPT-5.6 Terra** and a massive 80% drop for **GPT-5.6 Luna**. These efficiency gains were largely driven by **GPT-5.6 Sol**, which autonomously optimized inference kernels and load balancing. With Luna now priced below competing budget models from Google and Anthropic, the competitive landscape for low-cost LLMs has shifted dramatically.

---

## Key Price Drops
* **GPT-5.6 Terra:** 20% price reduction.
* **GPT-5.6 Luna:** 80% price reduction, bringing costs down to **$0.20 per million input tokens** and **$1.20 per million output tokens**.

---

## How GPT-5.6 Sol Enabled the Breakthrough
According to OpenAI's technical overview on [fusing frontier intelligence with frontier efficiency](https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/), GPT-5.6 Sol was used to streamline load balancing and optimize the model’s forward pass. 

> "We also used GPT‑5.6 Sol to optimize the model’s forward pass: the computation that transforms inputs into next-token predictions. Even when individual operations are fast, excess memory movement, synchronization, and inefficient data layouts can leave GPUs idle. To avoid this, GPT‑5.6 Sol found work that could be precomputed, avoided, or parallelized. With Codex, GPT‑5.6 Sol autonomously rewrote and optimized our production kernels, the core code that executes the mathematical operations that make up the model. This worked in part because we’ve trained GPT‑5.6 to be effective at writing and improving kernels in [Triton⁠](https://triton-lang.org/main/index.html) and [Gluon⁠](https://triton-lang.org/main/gluon/index.html), two open-source GPU programming languages maintained by OpenAI. These efforts, combined with broader kernel advancements from GPT‑5.6 Sol, reduced end-to-end serving costs by 20%."

---

## Market Impact on Budget LLMs
The dramatic price cut for GPT-5.6 Luna completely reshapes the tier of lower-priced models:
* **Google Gemini 3.1 Flash-Lite:** $0.25 (input) / $1.50 (output)
* **GPT-5.6 Luna:** $0.20 (input) / $1.20 (output) — *Now cheaper than Google's offering.*
* **Anthropic Claude Haiku 4.5:** $1.00 (input) / $5.00 (output) — *Luna is now five times cheaper for input.*

As a practical result of these changes, development projects like [agent.datasette.io](https://agent.datasette.io/) have already begun migrating their infrastructure from Gemini 3.1 Flash-Lite over to GPT-5.6 Luna.

---

*Via [Hacker News](https://news.ycombinator.com/item?id=49112867)*

**Tags:** [ai](https://simonwillison.net/tags/ai), [openai](https://simonwillison.net/tags/openai), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [anthropic](https://simonwillison.net/tags/anthropic), [gemini](https://simonwillison.net/tags/gemini), [llm-pricing](https://simonwillison.net/tags/llm-pricing)