# Release: llm 0.32rc2

## Summary
Following closely on the heels of RC1, the **llm 0.32rc2** release fixes a dependency issue and introduces two major updates: a new default model (**GPT-5.6 Luna**) for unconfigured users, and a powerful new `llm openai endpoint` command designed for querying arbitrary OpenAI-compatible APIs without prior configuration.

---

## What's New in 0.32rc2

* **New Default Model:** The default model for users who have not specified their own is now [GPT-5.6 Luna](https://developers.openai.com/api/docs/models/gpt-5.6-luna) (replacing `gpt-4o-mini`). Luna offers vastly improved performance at $0.20/M input tokens and $1.20/M output tokens. 
  * *Tip:* You can revert to `gpt-4o-mini` using `llm models default gpt-4o-mini`, or switch to the even more budget-friendly [GPT-5 nano](https://developers.openai.com/api/docs/models/gpt-5-nano) ($0.05/$0.40) using `llm models default gpt-5-nano` ([#1576](https://github.com/simonw/llm/issues/1576)).
* **OpenAI Endpoint Command:** Added the new [`llm openai endpoint`](https://llm.datasette.io/en/latest/other-models.html#openai-endpoint) command. This allows you to run prompts, chats, and model listings against any arbitrary OpenAI-compatible endpoint instantly without configuring a model first (and crucially, these calls are unlogged) ([#1565](https://github.com/simonw/llm/issues/1565)).

---

## Spotlight: The `llm openai endpoint` Command

Created out of a need for a seamless CLI tool to test prompts against arbitrary OpenAI Chat Completions imitation endpoints, this command brings immense flexibility to local and custom LLM workflows.

You don't even need a permanent installation of LLM to use it. Here is a handy `uvx` one-liner demonstrating how to run a prompt—complete with tools—against a local [LM Studio](https://lmstudio.ai) model:

```bash
uvx --pre llm openai endpoint http://127.0.0.1:1234/v1 \
  T llm_version -T llm_time --td \
  -m google/gemma-4-31b 'what is the current LLM version? And the time?'
```

👉 [View sample output here](https://github.com/simonw/llm/pull/1568#issuecomment-5136163707).

---

**Tags:** [llm](https://simonwillison.net/tags/llm) • [uv](https://simonwillison.net/tags/uv) • [lm-studio](https://simonwillison.net/tags/lm-studio)