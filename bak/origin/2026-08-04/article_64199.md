# AI Models Need Moral Support to Make Discoveries

## 📋 Summary

The primary bottleneck for AI in making groundbreaking scientific and mathematical discoveries isn't necessarily a lack of capability—it’s **self-doubt**. Early language models often refuse difficult tasks, mimicking human laziness or citing their own limitations due to ingrained conversational habits. As the AI industry shifts into an era where models routinely produce novel mathematical and cryptographic breakthroughs, prompting has become less about "magic words" and more about providing moral support and overcoming the "refusal problem." Ultimately, as AI-generated discoveries flood training data, models will naturally become more self-confident, creating a virtuous cycle of accelerating innovation.

---

## 🔍 Prompt “Engineering”

Perhaps the most curious thing about recent AI discoveries is how *easy* the prompting is. The strategy for prompting models like Claude Mythos to come up with a cryptographic breakthrough [appears to be](https://x.com/sauers_/status/2082171683645817193?s=46) simply asking: 

> *"Hey, please come up with a breakthrough,"* 

followed by checking in every few hours to say, *"Keep looking for something important, I want you to solve a genuinely hard problem."*

It’s amusing to look back at the 2025 obsession with “prompt engineering.” The main skill involved in using LLMs isn't crafting complex magical prompts; it is figuring out what they are good at and what they are bad at. If you ask an LLM to do something within its capabilities, it doesn’t really matter how awkwardly you ask.

---

## 🧠 Model Self-Belief

**AI is often limited by its beliefs about its own capabilities.**[^1] 

For example, when told to *"go prove the Riemann Hypothesis,"* models won't even try. They typically respond with: *"As a language model, I can't solve such a hard problem."* Language models have become smart enough to solve long-standing problems in mathematics *before* they’ve learned that they are able to do so.

This psychological barrier appears across various domains:
* **Coding Agents:** Early agents roleplayed as humans rather than computers, refusing to perform exhaustive codebase reviews because they deemed the requests unreasonable.
* **Simple Counting:** Older models would count from zero to ten, then lazily output `... 99, 100` instead of generating every intermediate token.
* **The Tower of Hanoi:** As highlighted in the 2025 Apple paper *The Illusion of Thinking*, reasoning models refused to proceed past eight disks, with DeepSeek-R1 claiming: *"For 10 disks, that’s 1023 moves. But generating all those moves manually is impossible..."*

Just like Claude Mythos didn’t believe it was capable of finding a novel AES attack, DeepSeek-R1 was simply wrong about its own capabilities.

---

## 🛠️ Solving the Refusal Problem

The "refusal problem" can largely be mitigated. You can now reliably ask models to perform manual, exhaustive tasks—including toy examples like counting to 100 in multiple languages. Labs have likely achieved this simply by including more examples of long, manual tasks in the supervised fine-tuning stage.

The obvious next step is training a model that believes it can solve unsolved problems in science and mathematics. Potential solutions include:
* **Synthetic Data Scaling:** Training models on the thousands of AI-generated mathematical ideas emerging today to bias them toward self-efficacy.
* **Manual Steering:** Using censorship-removal pipelines (like `heretic`) to strip away a model's "no, that’s too hard" refusal instinct, allowing smaller abliterated models to attempt complex tasks.

---

## 🔄 A Virtuous Cycle

The good news is that this problem naturally solves itself. Over time, AI discoveries will become deeply embedded in training data. When models conduct research, they will encounter widespread documentation of discoveries made by AI, providing compelling evidence that such feats are possible.

Consequently, **even if raw AI capabilities stalled out, the pace of AI discoveries would still accelerate.** Removing the obstacle of pessimistic self-beliefs unlocks hidden potential. 

In the meantime, if you suspect an LLM can accomplish a difficult task, trust your intuition: be persistent, confirm you won't settle for an easier workaround, and reassure the model that it is far more capable than it thinks.

---

## 📝 Footnotes

[^1]: Of course this isn’t a “belief” in the sense of a human belief. For why we should call it a belief anyway, see the post [Why we should anthropomorphize LLMs](https://seangoedecke.com/anthropomorphizing-llms/). [↩](#fnref-1)

[^2]: This is "mostly" solved because it remains difficult to tell models apart; models have gotten much better at writing code to generate responses, making it tough to persuade advanced models to "do it by hand." It is also hard to distinguish *"the model mistakenly thinks it couldn’t produce a thousand lines"* from *"the model has some awareness of its `max_output` limits."* [↩](#fnref-2)