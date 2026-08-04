# Winners and Losers in the Coming AI Margin Collapse (Part 2)

> *This is the second article in a two-part series focusing on what I believe is perhaps the least understood upcoming shift in AI economics. If you haven't read it yet, I'd recommend starting with [Part One](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/). If you enjoy my writing, I'd love it if you subscribe to my [newsletter](https://martinalderson.com/newsletter/) or [RSS feed](https://martinalderson.com/feed.xml).*

---

## 📌 Executive Summary

As the AI market races forward, the proliferation of aggressively priced, "good enough" models (such as GLM5.2 and Grok 4.5) is driving down inference margins. This article explores the shifting dynamics of the AI economy, identifying who stands to profit and who faces unprecedented pressure:

* **The Winners:** Hardware providers (semiconductors, data centers, power/cooling infrastructure), hyperscalers, application layers like coding agents (e.g., Cursors), and everyday end-users.
* **The Losers / The Uncertain:** Pure-play frontier labs relying heavily on API revenue, who face fierce competition from open weights and cheaper alternatives. Their survival depends on widening their intelligence lead or walling off top-tier models behind managed agent platforms.
* **The Wildcards:** The untapped potential of the B2C market and the possibility of cracking LLM-adjacent advertising.

---

## Your Margin Is My Opportunity

This is one of Jeff Bezos’s most famous quotes, illustrating how in highly competitive markets, any margin becomes a weakness for others to exploit. 

Grok 4.5’s aggressive pricing—offered at $6/MTok output, comparable to hosted GLM5.2—exemplifies this. While xAI is unlikely to beat OpenAI or Anthropic at the absolute frontier of intelligence, they have identified a clear path to traction: price.

The market is bifurcating into two distinct tiers:
1. **Expensive, very high-end models** (such as Fable or GPT5.6 Sol).
2. **A broad swath of good (~Opus-level), cheap models.**

While a lag between the frontier and everyone else has always existed, the dynamic has fundamentally shifted now that these cheaper models are becoming "good enough" for many complex agentic tasks.

---

## The Winners

### 1. The Hardware Supply Chain
The definitive winners in this shift are semiconductor companies and the entire downstream inference supply chain. Memory, GPUs, data centers, and the necessary power and cooling remain [severely supply constrained](https://martinalderson.com/posts/what-next-for-the-compute-crunch/). Basic microeconomics dictates that as models get cheaper, demand increases. Consequently, value is increasingly accruing to the [hardware layer](https://martinalderson.com/posts/xais-new-rental-business/), breaking historical tech paradigms where software historically captured all the margins. 

*(Note: While not capturing 100% of the value, this hardware-dominant wave is reminiscent only of Apple's cash-generation ability with the iPhone.)*

### 2. Hyperscalers and Neoclouds
Hyperscalers and hosted inference providers can capture value by serving lower-cost models at scale. Proprietary efficiency improvements and privileged relationships with hardware providers grant them a distinct competitive advantage until supply catches up with demand.

### 3. Application Layers (e.g., Coding Agents)
Coding agents (like Cursor) previously faced a brutal economic reality: reselling frontier inference at near-retail API prices left them with wafer-thin or negative margins on heavy users. "Good enough" cheap models flip this overnight. They can now offer near-Opus capabilities at a fraction of the cost, securing healthy profit margins. 

More importantly, these platforms sit on a goldmine of real-world agentic usage data—prompt preferences, accepted edits, and operational bottlenecks. This behavioral telemetry is precisely what model providers need to train future iterations. (This explains why xAI acquired Cursor: not just for the IDE, but for the cheap-model economics and data flywheel).

### 4. Consumers and End-Users
Ultimately, everyday users benefit most from accessing unprecedented levels of intelligence for pennies. What once looked like a potential OpenAI monopoly on quality inference has evolved into a diverse marketplace offering intelligence substantially better than GPT-4 for 5–10% of its original cost.

---

## The Losers (and the Frontier Lab Dilemma)

Predicting the fate of frontier AI labs is complex. On one hand, a massive chunk of AI use cases is migrating to open or cheaper models with little to no loss in quality. This poses an existential threat to labs like Anthropic, which reportedly earns [roughly 80% of its revenue](https://valueaddvc.com/blog/how-anthropic-makes-money-claude-api-enterprise-and-the-business-model-breakdown) from API usage.

However, two major wildcards complicate this picture:

1. **Restricted Access & Managed Platforms:** Frontier labs will likely stop releasing their most powerful models to the open market. Instead of raw APIs or direct coding agent integrations, access may be restricted to [managed agent platforms](https://martinalderson.com/posts/managed-agents-are-the-new-lambda/). This limits model substitution, strips users of harness control, and mitigates the risks of [model distillation](https://martinalderson.com/posts/open-weights-are-quietly-closing-up/) by international competitors.
2. **Accelerating Capabilities:** This analysis assumes "good enough" will remain stagnant. In reality, upcoming frontier models could represent [another massive leap forward](https://martinalderson.com/posts/are-we-in-a-gpt4-style-leap-that-evals-cant-see/), rendering current models obsolete overnight in terms of intelligence, speed, or context length. 

Whether frontier labs survive depends entirely on their ability to out-innovate and widen their lead over open-weights alternatives—a lead that currently appears to be shrinking.

---

## The B2C Wildcard

Over the past 12 months, the AI market has pivoted overwhelmingly toward B2B and enterprise use cases, leaving the consumer (B2C) market largely overlooked. 

A critical question remains: Will anyone successfully crack **LLM-adjacent advertising**? While OpenAI has experimented with rollout strategies, Anthropic has explicitly ruled out ads, and Google's Gemini chat sessions remain largely unmonetized in this regard. 

With ChatGPT boasting over 1 billion Monthly Active Users (MAUs), consumer engagement represents a massive, largely untapped revenue stream beyond standard subscriptions. Should a company successfully monetize this traffic, the hype cycle could swiftly swing back toward B2C.

---

## Conclusion

Pure model inference margins are rapidly heading toward zero, driven by "good enough" open models and a hyper-competitive hosting market. Bezos's maxim holds true: value is being captured on either side of the model layer—at the hardware foundation below, and by the end-users above.

Frontier labs have two paths out of the commodity trap: maintain a technological lead so wide that users happily pay a premium, or wall off top-tier models behind closed, managed platforms. Right now, betting against their ability to innovate is risky, but their historical lead is undeniably under pressure.

---

### Footnotes
1. *Though I'd argue that Apple itself, rather than the downstream supply chain, absorbed much of the margin in that historic ecosystem.* [↩](#fnref1)