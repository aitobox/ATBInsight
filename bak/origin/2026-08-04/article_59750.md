# The New GPT-5.6 Family: Luna, Terra, Sol

> **Summary:** OpenAI has released its latest flagship model family—**Luna**, **Terra**, and **Sol** (ranging from smallest to largest). Featuring a February 2026 knowledge cutoff, a 1-million-token context window, and advanced agentic capabilities, these models aim to deliver high efficiency and significantly lower costs compared to competitors like Anthropic's Claude. Alongside the release, OpenAI has introduced powerful new API features including programmatic tool calling, multi-agent support, and explicit prompt caching.

---

## Model Lineup & Pricing

OpenAI's new flagship models hit general availability, categorized by size from smallest to largest:

*   **Luna:** $1.00 / $6.00 per 1M input/output tokens
*   **Terra:** $2.50 / $15.00 per 1M input/output tokens
*   **Sol:** $5.00 / $30.00 per 1M input/output tokens

### Comparison and Context
For context, the Claude Opus series runs at $5/$25 and Claude Fable 5 at $10/$50. However, raw price-per-million tokens is becoming less informative as reasoning token counts vary significantly between models for the same task.

**Core Technical Specs:**
*   **Knowledge Cutoff:** February 16, 2026
*   **Context Window:** 1,000,000 tokens
*   **Max Output Tokens:** 128,000

---

## Benchmarks & Performance

OpenAI’s primary performance claims center on long-running agentic tasks. 

> "We trained GPT-5.6 to get more useful work from every token. On [Agents’ Last Exam](https://agents-last-exam.org/), an evaluation of long-running professional workflows across 55 fields, GPT-5.6 Sol sets a new high of 53.6, eclipsing Claude Fable 5 (adaptive reasoning) by 13.1 points. Even at medium reasoning, it beats Fable 5 by 11.4 points at roughly one-quarter the estimated cost. That efficiency extends to smaller models... GPT-5.6 Terra and GPT-5.6 Luna outperform Fable 5 at around one-sixteenth the cost."

### The SWE-Bench Pro Debate
Interestingly, Claude Fable 5 outperformed the GPT-5.6 family on *SWE-Bench Pro*, scoring 80% compared to GPT-5.6 Sol's 64.6%. This likely prompted OpenAI to publish an audit highlighting issues with the benchmark:

> "In light of these results, we estimate that ~30% of SWE-bench Pro tasks are broken, and advise that model developers carefully examine results."

*Early impressions from early-access testing suggest GPT-5.6 Sol is highly competent, though it hasn't quite surpassed Anthropic's models for complex coding tasks.*

---

## New API Features

The [GPT-5.6 model guidance docs](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.6) outline several notable additions to the API:

*   **[Programmatic Tool Calling](https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling):** Allows models to compose and run JavaScript that orchestrates tool calls, bridging the gap between MCPs and terminal sessions.
*   **[Multi-agent Support](https://developers.openai.com/api/docs/guides/tools-multi-agent):** Bakes the sub-agent pattern directly into the core API, enabling models to spin up subagents for parallel, focused work.
*   **[Prompt Cache Breakpoints](https://developers.openai.com/api/docs/guides/prompt-caching#prompt-cache-breakpoints):** Brings explicit prompt caching to OpenAI (similar to Claude), allowing developers to manually define cache breakpoints for cost optimization alongside automatic detection.
*   **Original Image Detail:** You can now set `detail: original` on image requests to bypass resizing completely.

---

## Visual Tests: The Pelican Matrix

To showcase reasoning efforts (none, low, medium, high, xhigh, and max) across the three models, a comprehensive test page was generated featuring **18 different pelicans**:

*   **Cheapest:** `gpt-5.6-luna` at `effort: none` cost **0.71 cents**.
*   **Most Expensive:** `gpt-5.6-sol` at `effort: max` cost **48.55 cents**.

![A grid of nine pelicans riding bicycles, of varying quality](./images/bbe154f37eaf.webp)

*(View the full showcase at [simonwillison.net](https://static.simonwillison.net/static/2026/gpt-5.6-pelicans.html).)*

### Livestream Highlights
During OpenAI's launch livestream, a demo featured 3D pelicans riding tricycles, bicycles, ponies, and even *other pelicans*.

![Frame from a livestream showing a 3D model of a pelican riding another pelican](./images/54bad6d89a1a.jpg)

---

**Tags:** [ai](https://simonwillison.net/tags/ai) · [openai](https://simonwillison.net/tags/openai) · [generative-ai](https://simonwillison.net/tags/generative-ai) · [llms](https://simonwillison.net/tags/llms) · [llm-tool-use](https://simonwillison.net/tags/llm-tool-use) · [llm-pricing](https://simonwillison.net/tags/llm-pricing) · [pelican-riding-a-bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle) · [llm-release](https://simonwillison.net/tags/llm-release) · [gpt-5](https://simonwillison.net/tags/gpt-5)