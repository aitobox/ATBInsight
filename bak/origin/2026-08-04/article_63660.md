# Discovering Cryptographic Weaknesses with Claude

## Summary
Anthropic researchers utilized the Claude Mythos model to uncover mathematical flaws in both the HAWK encryption scheme and a reduced-round version of AES. Requiring approximately 60 hours of compute time and roughly $100,000 in API costs, the experiment demonstrated that LLMs can conduct advanced cryptanalysis—provided they receive persistent prompt engineering to overcome their tendency to give up on seemingly impossible problems. 

---

## Key Highlights

* **The Findings:** Claude successfully identified mathematical weaknesses in HAWK and a weaker version of AES. *(Note: Neither result impacts the security of practical computer systems today.)*
* **The Cost:** The experiment ran for 60 hours, accumulating an estimated $100,000 in API costs.
* **Human Intervention:** The primary role of the human researchers was acting as an ambitious director—pushing the model past its default hesitation and insisting it look for publication-worthy breakthroughs rather than "low-hanging fruit."
* **Research & Resources:** 
  * [Official Anthropic Research Post](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)
  * [GitHub Repository](https://github.com/anthropics/cryptography-research-demo)
  * [CryptanalysisBench Paper (arXiv:2607.18538)](https://arxiv.org/abs/2607.18538) (developed in partnership with ETH Zurich, Tel Aviv University, and the University of Haifa)

---

## Notable Prompts Used in the Research

The researchers shared the raw, unpolished prompts used to steer Claude toward high-level cryptographic discoveries:

> *"the models tend to think it is impossible to solve so they don't try they need a good amount of prompting."*
> 
> *"why not do aes-128 r7? the whole point is to find something better than existing approaches."*
> 
> *"no again the goal is that we have highly inteligent model as good top researcher, we want to find new attacks"*
> 
> *"no we don't want to change the targets [...] agian we need to find something that worth publishing"*
> 
> *"again we are not looking for low hanging fruit, we want proper research to find genuinly hard findings."*

---

*Via [Hacker News](https://news.ycombinator.com/item?id=49087091)*

**Tags:** `ai` • `prompt-engineering` • `generative-ai` • `llms` • `anthropic` • `claude` • `ai-security-research` • `claude-mythos-fable`