# DeepSeek-V4-Flash-0731

## 📌 Summary
**DeepSeek-V4-Flash-0731** is the latest 304-billion-parameter model in DeepSeek’s V4 family, offering significantly enhanced agentic capabilities at industry-leading pricing ($0.14/M input, $0.27/M output). Benchmarks by *Artificial Analysis* place it in the "most attractive quadrant" for value-per-intelligence, outperforming several larger models while drastically undercutting them in cost. Performance on complex spatial tasks can be dramatically improved by scaling up the model's reasoning effort.

---

## 🚀 Overview & Performance

The new **[deepseek-ai/DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)** clocks in at 304 billion parameters (167 GB on Hugging Face), yet punches *well* above its weight class. 

According to **[Artificial Analysis](https://artificialanalysis.ai/models/deepseek-v4-flash)**, the model ranks ahead of the 428B MiniMax M3. Combined with its aggressive pricing ($0.14/million input and $0.27/million output), it currently stands as one of the best value-per-intelligence models available.

![Intelligence Index vs. Cost per Task Chart](http://localhost/proxy/RVAkzNpYyQ08OG3V0dXYEUmUGWORemfB_Yn5osF2V_E=/aHR0cHM6Ly9zdGF0aWMuc2ltb253aWxsaXNvbi5uZXQvc3RhdGljLzIwMjYvZGVlcHNlZWstZmxhc2gtY2hhcnQud2VicA==)

*As seen on the Artificial Analysis Intelligence Index, DeepSeek V4 Flash sits prominently at the far-left edge of the "most attractive quadrant," offering high intelligence at a fraction of the cost of competing models.*

---

## 🎨 Reasoning Level Impact: The Pelican Test

Agentic and spatial generation capabilities heavily depend on configuration settings. Testing the model with a prompt to generate a vector illustration via OpenRouter demonstrates the impact of adjusting the reasoning level.

### Default Reasoning Level
At the default reasoning setting, the output results in a somewhat mangled, anatomically incorrect attempt:

> **[View prompt details](https://gist.github.com/simonw/83bfb1171792f1e7a4d8935b5e82317e#prompt)**

![Disappointing Pelican (Default Reasoning)](http://localhost/proxy/DpoQNoeeSRhSN4GaCJYpXP60YjBWjOy5r_8j1EFiPkY=/aHR0cHM6Ly9zdGF0aWMuc2ltb253aWxsaXNvbi5uZXQvc3RhdGljLzIwMjYvZGVlcHNlZWstZmxhc2gtdjQtZGVmYXVsdC5wbmc=)

### High Reasoning Level
Increasing the reasoning effort via the command line dramatically improves spatial coherence and accuracy:

```bash
llm -m openrouter/deepseek/deepseek-v4-flash-0731 -t pelican -o reasoning_effort high
```

> **[View options details](https://gist.github.com/simonw/83bfb1171792f1e7a4d8935b5e82317e#options)**

![Improved Pelican (High Reasoning)](http://localhost/proxy/E2KVWZ8ca4OygZHTFtJFoUv8QVJCUeyRSuW7jPk3rsQ=/aHR0cHM6Ly9zdGF0aWMuc2ltb253aWxsaXNvbi5uZXQvc3RhdGljLzIwMjYvZGVlcHNlZWstZmxhc2gtdjQtaGlnaC5wbmc=)

---

*Via [Hacker News](https://news.ycombinator.com/item?id=49120299)*

**Tags:** [ai](https://simonwillison.net/tags/ai) • [generative-ai](https://simonwillison.net/tags/generative-ai) • [llms](https://simonwillison.net/tags/llms) • [pelican-riding-a-bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle) • [deepseek](https://simonwillison.net/tags/deepseek) • [llm-release](https://simonwillison.net/tags/llm-release) • [openrouter](https://simonwillison.net/tags/openrouter) • [ai-in-china](https://simonwillison.net/tags/ai-in-china) • [artificial-analysis](https://simonwillison.net/tags/artificial-analysis)