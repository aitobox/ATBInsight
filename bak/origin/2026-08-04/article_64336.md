# smevals: A Small Eval Suite for Models, Prompts, and Harnesses

## Summary
`smevals` is a lightweight, newly released evaluation framework developed in collaboration with Jesse Vincent’s Prime Radiant applied AI research lab. Designed to answer specific questions about AI capabilities, it allows users to run small, YAML-based evaluation suites across various model configurations, grade the results using flexible checks, and explore the outcomes via a local web server or static HTML reports.

---

## Getting Started

According to the official [blog entry](https://primeradiant.com/blog/2026/smevals.html) and [README](https://github.com/prime-radiant-inc/smevals/blob/main/README.md), getting started with the tool takes just two steps:

1. Instruct your coding agent to run `uvx smevals docs` to learn the tool.
2. Ask the agent to build an eval suite for you.

An eval takes the form of a simple directory containing YAML files.

---

## Core Commands

Once your eval suite is set up, you can execute, grade, and visualize results using `uvx`:

### 1. Run the Evaluation
Execute the eval against multiple model configurations:
```bash
uvx smevals run path-to-eval/ -m gpt-5.5 -m claude-opus-4.6
```

### 2. Grade the Results
Runs are kept separate from grading operations. Grade your outputs against your defined checks using:
```bash
uvx smevals grade path-to-eval/
```

### 3. Explore the Results
Launch a localhost web server to interactively explore the findings:
```bash
uvx smevals serve path-to-eval/
```

Alternatively, build the report as static HTML to host anywhere (see a live [haiku evaluation example](https://static.simonwillison.net/static/2026/smevals-haiku-build/#/haiku)):
```bash
uvx smevals build path-to-eval/
```

> ![Screenshot of an evaluation dashboard](./images/f94fc21b2002.webp)
> *An evaluation dashboard benchmarking how well models write haikus, featuring leaderboards, recent runs, tag pass rates, prompts, and grader details.*

---

## Key Terminology

After years of iteration, the framework relies on a streamlined vocabulary:

* **Eval:** A collection of challenges designed to answer a specific question about a model (e.g., *"How good is this model at generating SVGs?"*).
* **Task:** A specific challenge within an eval (e.g., *"Generate an SVG of a pelican riding a bicycle"*).
* **Config:** Specifies a model to be evaluated, alongside optional parameters like system prompts, model settings, or agent harnesses.
* **Run:** A record of what happened when a specific config executed a specific task.
* **Runner:** The script responsible for executing a run.
* **Grader & Grade:** A grader evaluates completed runs against defined criteria to produce a grade.
* **Checks & Checkers:** Sequences of validation operations ranging from simple string/XML matching to complex custom scripts (including secondary LLM calls).

---

## Background
Representing the third iteration on the concept over several years of experimentation, `smevals` provides a robust, streamlined approach to AI evaluation that bridges the gap between raw model outputs and actionable insights.

***

**Tags:** [projects](https://simonwillison.net/tags/projects) | [ai](https://simonwillison.net/tags/ai) | [generative-ai](https://simonwillison.net/tags/generative-ai) | [llms](https://simonwillison.net/tags/llms) | [llm](https://simonwillison.net/tags/llm) | [evals](https://simonwillison.net/tags/evals) | [jesse-vincent](https://simonwillison.net/tags/jesse-vincent)