# Are AI labs pelicanmaxxing?

> **Summary:** Dylan Castillo investigates a fun internet theory: are AI labs deliberately training their models to excel at drawing pelicans riding bicycles? Through a rigorous, systematic benchmark of multiple animal and vehicle combinations across top-tier models, the study concludes that "pelicanmaxxing" is a myth—pelicans and bicycles are simply rendered as well as any other common combination.

---

## Overview

Dylan Castillo has published an excellent deep-dive exploring whether AI labs have been deliberately training models to draw pelicans riding bicycles. This follows a [deeply unscientific benchmark](https://simonwillison.net/tags/pelican-riding-a-bicycle/) I previously popularized.

While I have occasionally spot-tested models against other animals riding various vehicles, Dylan approached this with a much higher level of methodological rigor. 

## Methodology

Dylan's evaluation framework consisted of:
* **8 animals** × **6 vehicles** = **48 unique prompts**
* **3 test runs** per prompt 
* **7 different models tested:** GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.5 Flash, Grok 4.5, Qwen3.7-Max, GLM-5.2, and DeepSeek V4 Pro
* **Automated evaluation** using GPT-5.6 Luna and Gemini 3.1 Flash-Lite to score the results

The analysis also featured an interactive filter view to explore the generated grids:

![Screenshot of a grid for sample 1/3 of GLM-5.2, featuring a pelican, flamingo, and heron riding bicycles, unicycles, skateboards, scooters, planes, and boats](http://localhost/proxy/3_D1Vd6SpLtsCCNtQ5LtGIK1S4o9wMIVeNlcJDRAew4=/aHR0cHM6Ly9zdGF0aWMuc2ltb253aWxsaXNvbi5uZXQvc3RhdGljLzIwMjYvcGVsaWNhbi1ncmlkLndlYnA)

## The Findings: Is Pelicanmaxxing Real?

According to [Dylan's findings](https://dylancastillo.co/posts/pelicanmaxxing.html), there is **no evidence** to support the pelicanmaxxing theory. Key takeaways include:

* [The pelicans on bicycles don’t look any better](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-1-the-pelicans-on-bicycles-dont-look-any-better)
* [Labs are not better at drawing pelicans](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-2-labs-are-not-better-at-drawing-pelicans)
* [Labs are not better at drawing bicycles](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-3-labs-are-not-better-at-drawing-bicycles)
* [Labs are not better at drawing pelicans on bicycles, even adjusting for difficulty](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-4-labs-are-not-better-at-drawing-pelicans-on-bicycles-even-adjusting-for-difficulty)
* [The pelican-bicycle scenes don’t look memorized](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-5-the-pelican-bicycle-scenes-dont-look-memorized) [...]

To summarize the conclusion:
> Pelicans aren’t drawn any better than other animals. Bicycles aren’t drawn any better than other vehicles. And no lab draws the combination better than its pelicans and bicycles already predict. 
> 
> GLM-5.2 comes closest: it has the largest boost on the exact pelican-bicycle cell, and its first pelican-on-bicycle sample caught my eye. But the effect is small and not significant, so I wouldn’t put too much weight on it.

***

*Via [Hacker News](https://news.ycombinator.com/item?id=49010129)*

**Tags:** [ai](https://simonwillison.net/tags/ai), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [evals](https://simonwillison.net/tags/evals), [pelican-riding-a-bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle)