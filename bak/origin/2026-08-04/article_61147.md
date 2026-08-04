# How Predictable Are Laws?

## Executive Summary
Laws are often treated as precise instruments, but how often do they actually achieve what their authors intended? To answer this question, an AI-driven analysis was conducted on hundreds of federal laws passed over the last 50 years. 

The study found that **the vast majority of federal laws (around 89%) perform broadly as expected**. However, roughly **11% experience substantial divergences**, resulting in impacts that are either vastly larger, drastically smaller, or entirely different than originally anticipated. Much like emerging technologies, laws create new legal and institutional capabilities that often get co-opted, expanded, or ignored in ways their creators never imagined.

---

## The Unintended Consequences of Legislation
History is full of laws whose real-world impacts completely blindsided their creators:

* **The National Environmental Policy Act (NEPA):** Conceived in 1969 as an aspirational policy statement to protect the environment, its last-minute environmental impact statement (EIS) requirement received virtually zero congressional debate. Yet, it became the primary weapon for environmental groups to halt or delay major infrastructure projects.
* **The 401(k) Retirement Account:** Originally introduced as an obscure, "negligible" provision within the 1978 Revenue Act by a 28-year-old junior lawyer, it transformed into the primary vehicle for retirement savings for tens of millions of Americans.
* **California’s Housing Laws:** Conversely, several state laws designed to "end single-family zoning" and supercharge housing construction by converting strip malls and church parking lots have had a severely limited impact on housing supply.

---

## Methodology & Scoring Rubric
To measure legislative predictability, an AI model (Claude Opus 4.8 Max Thinking) analyzed **239 federal laws** passed between 1976 and 2023 (filtered to exclude bills under 10 pages, such as post office renamings). 

Based exclusively on contemporaneous sources (bill texts, CBO scores, presidential signing statements, and media coverage), the AI estimated expected versus actual effects, assigning each law a **Divergence Score from -10 to +10**:
* **Positive numbers (+):** Larger-than-anticipated impacts or unforeseen positive/expanded applications.
* **Negative numbers (-):** Smaller-than-anticipated impacts, complete failures, or non-implementation.

### The Scoring Scale
* **0:** Actual impact matched expectations almost exactly.
* **±1–2 (Minor):** Broadly as expected; small secondary deviations.
* **±3–4 (Moderate):** Noticeable gaps, but the core purpose was largely realized.
* **±5–6 (Substantial):** Primary outcomes materially exceeded or unmet, or major unanticipated effects emerged.
* **±7–8 (Major):** Central goal greatly overshot or failed/went unimplemented.
* **±9–10 (Extreme):** Actual impact bore little resemblance to expectations (near-total failure or completely opposite effects).

*(Full prompt data and results can be found in the [GitHub Repository](https://github.com/briancpotter/laweffects).)*

---

## Results: The Shape of Legislative Predictability
The divergence scores formed a bell curve with a slight positive skew:
* **40% (95 laws):** Scored between -1 and 1 (acted precisely as expected).
* **20% (49 laws):** Scored between -2 and -4 (moderate under-delivery).
* **28% (68 laws):** Scored between 2 and 4 (moderate over-delivery/unanticipated reach).
* **~11%:** Suffered a "substantial divergence" (scores $\ge \pm5$).

### Examples of Laws with Much Larger Effects than Predicted (+ Scores)
* **Airline Deregulation / Air Cargo Act (Score: +5):** Intended merely to adjust airline insurance, a cargo deregulation provision allowed companies like FedEx to use large jets on any route, accidentally birthing the modern "air express cargo" industry.
* **Sarbanes-Oxley Act of 2002 (Score: +5):** Aimed at increasing auditing oversight after Enron, compliance costs were 30–50 times higher than expected. Furthermore, an obscure clause regarding "obstruction of an official proceeding" was later used to criminally charge hundreds of January 6 defendants (before being partially limited by the Supreme Court).
* **Trade Facilitation and Trade Enforcement Act of 2015 (Score: +7):** Billed as a routine customs modernization bill, it quietly raised the "de minimis exemption" (goods exempt from tariffs) from $200 to $800, directly fueling the multi-billion-dollar influx of direct-to-consumer Chinese imports from Shein and Temu.

### Examples of Laws with Much Smaller Effects than Predicted (- Scores)
* **The Alaska Natural Gas Transportation Act of 1976 (Score: -7):** Envisioned as the largest privately financed energy project in history to pipe gas to the lower 48 states, it was completely derailed by rising costs and a subsequent natural gas supply glut.
* **The Alabama-Coosa-Tallapoosa River Basin Compact of 1997 (Score: -5):** Created to foster a shared water-allocation plan between Alabama and Georgia, the states failed to reach an agreement, resulting in decades of continuous litigation instead.
* **Enhanced Partnership with Pakistan Act of 2009 (Score: -5):** Aimed at buying goodwill and close relations through billions in infrastructure funding, it utterly failed to shift public opinion as political tensions and military raids strained relations further.

### Additional Patterns
* **Time Invariance:** Recent laws are roughly as predictable as laws passed decades ago.
* **Page Count:** Longer, more complex laws show a slight positive correlation with higher-than-expected impacts, likely due to a "bundling effect" where complex omnibus bills increase the odds of at least one component having an outsized effect.
* **Bill Type:** Routine appropriations bills show much lower variance compared to bills creating brand-new structural programs, which carry a much higher risk of extreme divergence.

---

## Why Do Laws Diverge?
Legislative misalignments generally stem from two primary friction points: **legal operators** (courts, agencies, and future legislatures) and **the broader world** (markets and human behavior).

1. **Judicial Interpretation:** Courts often interpret laws in ways original authors never imagined. For instance, the 1989 Ethics Reform Act banned federal workers from being paid for speeches or articles until the Supreme Court struck down parts of it as a First Amendment violation.
2. **Agency & Prosecutorial Discretion:** Government bodies frequently repurpose laws. The DNA Fingerprinting Act of 2005 (housed within a domestic violence bill) was later leveraged by ICE to collect DNA from immigration detainees. Conversely, the 2012 STOCK Act made congressional insider trading illegal, yet has resulted in zero prosecutions.
3. **Future Legislative Actions:** Subsequent Congresses can either kill a law's intent (e.g., the 1984 Sentencing Reform Act entirely abolished federal parole, rendering the 1976 Parole Reorganization Act moot) or massively expand it (e.g., the 2021 REPLANT Act transformed a tiny $30M tree-planting trust fund into a 1.2-billion-tree national initiative).
4. **Market and Public Response:** Regulated entities adapt in unpredictable ways. The Credit Rating Agency Reform Act of 2006 failed to break up the oligopoly of S&P, Moody’s, and Fitch, while trade laws failed to predict the clever adaptations of fast-fashion global supply chains.

---

## Conclusion: Laws as Technology
Comparing legislation to technology offers a useful framework. When you invent a technology—like Marconi inventing wireless telegraphy—you create a new capability. However, once that capability is deployed into the wild, humanity finds entirely unanticipated ways to exploit it (such as broadcast radio). 

Similarly, laws introduce organizational, institutional, or regulatory capabilities. Sometimes they spark massive, unintended cultural or economic revolutions (like NEPA or the 401(k)); other times, they turn out to be the legal equivalent of "Smell-O-Vision"—utterly useless or ignored by the market. While predicting the long-term impact of laws is generally easier than predicting technology, the persistent 11% divergence rate proves that writing legislation always carries a heavy element of the unknown.