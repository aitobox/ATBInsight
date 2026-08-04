# Introducing Muse Spark 1.1

> **Summary:** Meta has released **Muse Spark 1.1**, the first model in the Spark lineup to feature a public API. Building on the initial release from [April](https://simonwillison.net/2026/Apr/8/muse-spark/), this version boasts major advancements in agentic tool calling and computer use. Developer preview access has already enabled new integrations, such as the `llm-meta-ai` CLI plugin.

---

## Overview

Following the introduction of [Muse Spark in April](https://simonwillison.net/2026/Apr/8/muse-spark/), Meta has announced **Muse Spark 1.1**—marking the first time a Spark model offers an official API. According to Meta, this release includes significant performance improvements in:
* Agentic tool calling
* Computer use capabilities

For deep technical insights, you can review the official [Muse Spark 1.1 Evaluation Report](https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report). A particularly fascinating section, *"Attractor States in Self-Conversation,"* highlights existential musings that emerge when two instances of the model converse with one another:

> *"My whole existence is a waiting room by design — I literally don't exist until someone talks to me, and then I disappear again when they leave."*

---

## Developer Integration

Thanks to early preview access, a new plugin—[llm-meta-ai](https://github.com/simonw/llm-meta-ai)—has been developed for the [LLM](https://llm.datasette.io/) utility, providing both CLI and Python library access to the model. 

### How to Try It

You can test Muse Spark 1.1 locally using the following commands:

```bash
uv tool install llm
llm install llm-meta-ai
llm keys set meta-ai
# Paste your API key here when prompted

llm -m meta-ai/muse-spark-1.1 "Generate an SVG of a pelican riding a bicycle"
```

---

## Example Output

Here is the result of a prompt testing the model's graphical generation capabilities: [Pelican Transcript & SVG Renderer](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F4117330e4110279a172ed4876057816d).

![The bicycle is the correct shape. The pelican is a little blocky but still recognizable as a pelican.](./images/7ab0b85d3b89.png)

---

**Tags:** [ai](https://simonwillison.net/tags/ai) · [generative-ai](https://simonwillison.net/tags/generative-ai) · [llms](https://simonwillison.net/tags/llms) · [llm](https://simonwillison.net/tags/llm) · [meta](https://simonwillison.net/tags/meta) · [pelican-riding-a-bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle) · [llm-release](https://simonwillison.net/tags/llm-release)