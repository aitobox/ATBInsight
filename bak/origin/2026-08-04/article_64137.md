# LLM Chat Completions Server 0.1a0

## Summary
`llm-chat-completions-server 0.1a0` is a new plugin that exposes your local LLM models via an OpenAI-compatible Chat Completions endpoint. Built to leverage the content-addressable logs introduced in LLM 0.32rc1, the server efficiently handles stateful, growing conversation histories by deduplicating message parts using hashes. Interestingly, the entire plugin implementation was written by an AI (GPT-5.6 Sol).

---

## Overview

This release is designed to support OpenAI Chat Completion style requests, where each incoming message extends the previous conversation. 

For example:

```bash
curl http://localhost:8002/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "qwen3.5-4b",
    "messages": [
      {"role": "user", "content": "Capital of France?"},
      {"role": "assistant", "content": "Paris."},
      {"role": "user", "content": "Germany?"}
    ]
  }'
```

In this workflow, the conversation state is tracked entirely by the client, causing requests to grow longer with each turn. The new schema design in [LLM 0.32rc1](https://simonwillison.net/2026/Jul/30/llm-rc1/) efficiently de-duplicates these messages using hashes of the individual message parts.

---

## Installation and Usage

To test out the new server, you can install the plugin using `uv`:

```bash
uv tool install llm --pre
llm install llm-chat-completions-server
llm chat-completions-server -p 9001
```

Running this command starts a local server on port 9001, exposing your full collection of LLM models (including those from any installed plugins) through a ChatGPT Completions-compatible endpoint.

---

## Fun Fact

Interestingly, [GPT-5.6 Sol wrote the whole thing](https://gist.github.com/simonw/53be513c1bd4a29a7aa480d9bde9b4a5)—proving to be exceptionally knowledgeable about the OpenAI Chat Completions API shape.

---

**Tags:** [projects](https://simonwillison.net/tags/projects) | [openai](https://simonwillison.net/tags/openai) | [llm](https://simonwillison.net/tags/llm)  
**Release Link:** [llm-chat-completions-server 0.1a0](https://github.com/simonw/llm-chat-completions-server/releases/tag/0.1a0)