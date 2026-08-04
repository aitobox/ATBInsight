# LLM 聊天补全服务器 0.1a0

**背景与摘要：**
`llm-chat-completions-server 0.1a0` 是一个全新的插件，它通过一个兼容 OpenAI 格式的 Chat Completions API 端点，对外暴露你本地的大语言模型（LLM）。该服务器基于 LLM 0.32rc1 引入的内容可寻址日志构建，通过使用哈希值对消息各个部分进行去重，从而高效地处理具有状态且不断增长的对话历史记录。有趣的是，这个插件的整个实现代码都是由人工智能（GPT-5.6 Sol）编写的。

> ## Summary
> `llm-chat-completions-server 0.1a0` is a new plugin that exposes your local LLM models via an OpenAI-compatible Chat Completions endpoint. Built to leverage the content-addressable logs introduced in LLM 0.32rc1, the server efficiently handles stateful, growing conversation histories by deduplicating message parts using hashes. Interestingly, the entire plugin implementation was written by an AI (GPT-5.6 Sol).

---

## 概览

此次发布的版本旨在支持类似 OpenAI Chat Completion 风格的请求，即每一条传入的新消息都在延续之前的对话。

> ## Overview
> 
> This release is designed to support OpenAI Chat Completion style requests, where each incoming message extends the previous conversation. 

例如：

> For example:

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

在这种工作流中，对话状态完全由客户端进行跟踪，导致每一轮的请求内容都变得越来越长。[LLM 0.32rc1](https://simonwillison.net/2026/Jul/30/llm-rc1/) 中新的架构设计，通过对单个消息片段进行哈希处理，有效地对这些消息进行了去重。

> In this workflow, the conversation state is tracked entirely by the client, causing requests to grow longer with each turn. The new schema design in [LLM 0.32rc1](https://simonwillison.net/2026/Jul/30/llm-rc1/) efficiently de-duplicates these messages using hashes of the individual message parts.

---

## 安装与使用

若要试用这个新服务器，你可以使用 `uv` 来安装该插件：

> ## Installation and Usage
> 
> To test out the new server, you can install the plugin using `uv`:

```bash
uv tool install llm --pre
llm install llm-chat-completions-server
llm chat-completions-server -p 9001
```

运行这个命令会在 9001 端口启动一个本地服务器，通过一个兼容 ChatGPT Completions 的端点，将你全部的 LLM 模型集合（包括来自任何已安装插件的模型）暴露出来。

> Running this command starts a local server on port 9001, exposing your full collection of LLM models (including those from any installed plugins) through a ChatGPT Completions-compatible endpoint.

---

## 趣闻轶事

有趣的是，[GPT-5.6 Sol 编写了整个程序的代码](https://gist.github.com/simonw/53be513c1bd4a29a7aa480d9bde9b4a5)——证明了它对 OpenAI Chat Completions API 的形态了如指掌。

> ## Fun Fact
> 
> Interestingly, [GPT-5.6 Sol wrote the whole thing](https://gist.github.com/simonw/53be513c1bd4a29a7aa480d9bde9b4a5)—proving to be exceptionally knowledgeable about the OpenAI Chat Completions API shape.

---

**标签:** [项目 (projects)](https://simonwillison.net/tags/projects) | [openai](https://simonwillison.net/tags/openai) | [大语言模型 (llm)](https://simonwillison.net/tags/llm)  
**发布链接:** [llm-chat-completions-server 0.1a0](https://github.com/simonw/llm-chat-completions-server/releases/tag/0.1a0)

> **Tags:** [projects](https://simonwillison.net/tags/projects) | [openai](https://simonwillison.net/tags/openai) | [llm](https://simonwillison.net/tags/llm)  
> **Release Link:** [llm-chat-completions-server 0.1a0](https://github.com/simonw/llm-chat-completions-server/releases/tag/0.1a0)
