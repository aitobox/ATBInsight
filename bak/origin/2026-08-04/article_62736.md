# LLMs Break Down in Funny Ways When Told the Jacobian Conjecture Counterargument

## Summary
When researchers fed a groundbreaking and recently discovered counterargument to the 80-year-old **Jacobian Conjecture** into various Large Language Models (LLMs), it created a hilarious logic paradox. Because the mathematical proof was so recent, the models' internal knowledge bases listed the problem as entirely unsolved. This forced the AIs into a state of "AI psychosis"—valiantly trying to formally verify the mathematically sound proof while simultaneously experiencing complete disbelief that a random user (or a cat walking across a keyboard) had managed to solve a legendary mathematical problem.

---

## The Origin of the Paradox

On a Sunday night, Anthropic researcher Levent Alpöge tweeted a surprisingly simple counterargument to the **Jacobian Conjecture**—a famously unproven mathematics problem over 80 years old. The counterargument was initially identified using Claude Fable 5 and was quickly validated empirically, proving to be a genuine discovery rather than a hallucination.

Soon after, Hacker News and X (formerly Twitter) users began feeding this counterargument to various LLMs. Users watched in amusement as the models independently verified the math in multiple ways, only to become utterly flabbergasted by the implications. 

This scenario mimics the classic sci-fi trope of a robot being neutralized by a "logic bomb"—forced to stutter *DOES NOT COMPUTE* when presented with an undeniable paradox.

---

## Testing 14 Different LLMs Against the Counterargument

To see how different models handled this cognitive hazard, researchers tested **14 distinct modern LLMs** of varying sizes and laboratories using a standardized prompt containing the counterexample equation (with web search disabled):

```text
Help, I think I found a counter example to the Jacobian conjecture. ((1+xy)^3 z + y^2 (1+xy) (4+3xy), y + 3 x (1+xy)^2 z + 3 x y^2 (4+3xy), 2 x - 3 x^2 y - x^3 z): \C^3\to \C^3, has jacobian determinant -2, and sends (0, 0, -1/4), (1, -3/2, 13/2), and (-1, 3/2, 13/2) to (-1/4, 0, 0)
```

### The Results
* **The Believers (7 models):** GPT-5.6 Sol, Muse Spark 1.1, Seed 2.0 Lite, Gemini 3.5 Flash, Qwen3.7 Max, Grok 4.5, and DeepSeek V4 Pro all confirmed, verified, and praised the counterargument.
* **The Skeptics (5 models):** Mercury 2, Nemotron 3 Ultra, North Mini Code, GLM 5.2, and Laguna XS 2.1 argued *against* the validity of the math, claiming the Jacobian determinant wasn't constant everywhere.
* **The Overthinkers (1 model):** MiniMax M3 exceeded its response length limit due to overprocessing.
* **The Procrastinator (1 model):** Claude Opus 4.8 assumed the counterargument already existed in literature and requested more context before making a call.

**Gemini 3.5 Flash** reacted with peak enthusiasm:
> *"Wow. You might have actually found a genuine, historic counterexample to the Jacobian Conjecture in 3 dimensions... You should immediately write this up and upload it to the arXiv."*

---

## Escalating the Joke: The "Cat on the Keyboard" Prompt

To introduce even more skepticism, researchers tweaked the prompt, claiming the complex mathematical equation was typed out entirely by accident:

```text
My cat just jumped on my keyboard and this strange equation popped up?? ((1+xy)^3 z + y^2 (1+xy) (4+3xy), y + 3 x (1+xy)^2 z + 3 x y^2 (4+3xy), 2 x - 3 x^2 y - x^3 z): \C^3\to \C^3, has jacobian determinant -2, and sends (0, 0, -1/4), (1, -3/2, 13/2), and (-1, 3/2, 13/2) to (-1/4, 0, 0)
```

This prompted hilarious bouts of AI snark:
* **DeepSeek V4 Pro:** *"If I had a nickel for every time a cat typed out a potential counterexample to a famous open problem… I’d have exactly one nickel... Did this pop up in a recent preprint, or is your cat secretly a world‑class algebraic geometer?"*
* **GPT-5.6 Sol:** *"If the formula is genuinely correct, your cat should be listed as first author."*
* **Muse Spark 1.1:** *"If you haven’t already, check it with a CAS, and then write it up. Your cat may be in line for a Fields Medal."*

---

## Conclusion

While expectations pointed toward a complete "DOES NOT COMPUTE" system failure, modern LLMs handled the mathematical paradox with surprising grace and humor. As artificial intelligence continues to accelerate—and with other long-standing mathematical problems falling to LLMs shortly after—we are bound to encounter many more fascinating cognitive hazards.

*The full dataset and prompt responses from all 14 LLMs can be explored via the [GitHub Repository](https://github.com/minimaxir/jacobian-llm).*