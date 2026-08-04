# Why Compute Might Get 10x+ More Expensive in Coming Years

*A quick, time-boxed exploration into the economics of AI labs, scaling limits, and the soaring future value of compute.*

---

## 📌 Executive Summary

As frontier AI labs experience explosive revenue growth (e.g., Anthropic growing ~10x year-over-year) while total available compute scales at a more modest ~3x annually, a massive economic tension emerges. To bridge this gap without shifting all compute entirely to inference, either lab margins must reach unrealistic mid-90% levels, or **the price of compute must rise dramatically**. 

Driven by the increasing economic utility of AI models (such as automating human-level software engineering), standard labor economics and severe supply-chain bottlenecks suggest that high-end compute could soon become **15x more expensive** than today's spot prices. While compute will eventually become cheap again once robotics and automation fully decouple hardware production from human labor, the coming years will likely introduce severe compute scarcity, massive consolidation, and the pricing-out of casual AI applications.

---

## 1. The Scaling Paradox: Revenue vs. Compute

Frontier AI labs are growing at staggering rates. Anthropic’s revenue has scaled 10x year-over-year, potentially ending the year around $100B–$150B. For this trend to hold, revenue would need to hit $1T by the end of next year. 

However, lab compute is only scaling at roughly **3x year-over-year**. For a lab to grow revenue 10x while its compute base only triples, three things must happen in tandem:
1. **Lab margins must increase.**
2. **The price of compute must increase.**
3. **Labs must dedicate a greater fraction of compute to inference rather than training.**

Option #3 is undesirable for labs; spending most compute on inference signals that training has stalled, reducing their business to a basic cloud provider. This leaves margin expansion and surging compute prices as the primary safety valves. 

While margins are already climbing (OpenAI and Anthropic boast high blended inference margins), pushing margins to the mid-90s by next year is implausible. That leaves **surging compute prices** as the primary mechanism to absorb surging demand.

---

## 2. The Rising Cost of Secure, Scalable Compute

The compute market is already reflecting this pressure. Frontier labs cannot rely on volatile spot instances; they require secure environments for proprietary weights, customer data, and massive scale. 

The insanity of this tier of the market is highlighted by infrastructure deals like Google and Anthropic renting from SpaceX:
* Google is reportedly paying **$900 million a month for 110K GPUs** (a blend of GB200s and GB300s).
* This rate is roughly **2x the standard spot price** per hour, which is itself already up 40% since February.

---

## 3. The Economic Value of an AI "Software Engineer"

To understand where compute pricing is heading, consider the economic utility of advanced models. 

If a frontier model achieves human-level software engineering capabilities and runs on an H100 equivalent, pricing it against market rates for human software engineers suggests that a single H100 should rent for **over $250k a year**—roughly **15x today’s spot prices**.

Critics might argue that flooding the market with millions of AI "workers" would collapse their marginal value (similar to the *lump of labor fallacy*). However, standard economic theory on high-skilled labor suggests that specialization and innovation actually *increase* the long-term value of labor rather than depressing wages. If this applies to AI agents, the marginal value—and price—of compute will remain astonishingly high.

---

## 4. Consequences of a High-Compute-Cost Regime

If compute prices surge by an order of magnitude or more, several major market shifts will follow:

* **Extremized Market Concentration:** As top models become drastically better at monetizing compute, it will become exponentially harder for upstarts with zero revenue to compete against frontier labs for scarce hardware.
* **The Alchian–Allen Effect:** When a heavy fixed cost (expensive compute) is added to models of varying quality, demand shifts heavily toward the premium, highly efficient good. At $20/hour for an H100, using an inefficient model wastes too much money on tokens; labs and enterprises will gladly pay a massive premium for the absolute best-performing models.
* **Pricing-Out Casual AI:** Many lightweight or frivolous applications (e.g., short-form video "slop") will simply get priced out of viability as raw compute costs soar.
* **Severe Supply-Chain Inelasticity:** Unlike the famous *Simon–Ehrlich wager* on commodities—where human ingenuity and market signals easily bypassed resource scarcity—compute supply is heavily constrained. The 3x annual scaling relies on three strict multipliers:
  1. ~1.4x from Moore’s Law.
  2. ~1.2x from new fab construction (bottlenecked through 2030 by EUV tool supply).
  3. ~1.8x from AI capturing leading-edge wafer allocation from other devices (projected to hit a 86% saturation wall by late 2027).

---

## 5. The Long-Term Outlook: When Compute Becomes Cheap Again

This high-price regime is ultimately temporary. 

At some point in the future, advanced robotics and automation will allow autonomous systems to turn silica sand and copper mines directly into computers. When that happens, the price of compute will plummet toward the baseline cost of raw inputs and tools. 

Until then, we are stuck in a transitional regime where AI compute grows at "only" 3x a year—a rate fast enough to cause severe scarcity, but far too slow to offset how drastically more useful AI is becoming year-over-year.

---

### Footnotes
1. Blended inference margins for major players are estimated to be >70%, suggesting API-specific margins for leading products sit comfortably above 80%.