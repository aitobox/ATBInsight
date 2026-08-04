# Stateless MCP Has Recaptured My Interest (and Inspired `mcp-explorer` and `datasette-mcp`)

## 📌 Summary
The release of the stateless Model Context Protocol (MCP 2.0 / 2026-07-28 specification) has drastically reduced implementation complexity by removing server-side session management. This evolution has reignited interest in MCP as a safer, more auditable alternative to giving LLM agents general shell and internet access. Inspired by the update, the author built three new projects: **`mcp-explorer`** (a CLI tool for probing MCP servers), **`datasette-mcp`** (a plugin adding MCP support to Datasette instances), and **`llm-mcp-client`** (an official MCP integration for the LLM CLI tool).

---

## 🔄 The Evolution of MCP: From Stateful to Stateless

Tuesday marked **Stateless MCP day**—the rollout of the 2026-07-28 Model Context Protocol specification. This represents the most significant change to the MCP spec since Anthropic introduced it in November 2024. 

While MCP saw a massive surge of interest through 2025, it was somewhat eclipsed by "Skills" (another Anthropic innovation) when agent harnesses with terminal and `curl` access proved more flexible. However, giving an agent unrestricted shell environments is fraught with security risks. MCP tools offer a simpler, easier-to-audit alternative that even smaller, laptop-running models can operate effectively.

The new stateless MCP specification significantly decreases implementation complexity for both clients and servers by eliminating the need for session IDs.

### Stateful vs. Stateless Comparison

* **Legacy (Stateful) MCP:** Required two separate HTTP requests—one to initialize a session and obtain an `Mcp-Session-Id`, and a second to call the tool.
  
  ```http
  POST /mcp HTTP/1.1
  Content-Type: application/json

  {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
      "protocolVersion": "2025-11-25",
      "capabilities": {},
      "clientInfo": {
        "name": "my-app",
        "version": "1.0"
      }
    }
  }

  POST /mcp HTTP/1.1
  Mcp-Session-Id: 1868a90c-3a3f-4f5b
  Content-Type: application/json

  {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
      "name": "search",
      "arguments": {
        "q": "otters"
      }
    }
  }
  ```

* **Stateless MCP:** Uses a single HTTP request, making it vastly cleaner and much better suited for scalable web applications without backend session overhead.

  ```http
  POST /mcp HTTP/1.1
  MCP-Protocol-Version: 2026-07-28
  Mcp-Method: tools/call
  Mcp-Name: search
  Content-Type: application/json

  {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "search",
      "arguments": {
        "q": "otters"
      },
      "_meta": {
        "io.modelcontextprotocol/clientInfo": {
          "name": "my-app",
          "version": "1.0"
        }
      }
    }
  }
  ```

---

## 🛠️ New Projects Built This Week

### 1. `mcp-explorer`
Unable to find a great interactive CLI tool for probing MCP servers, [mcp-explorer](https://github.com/simonw/mcp-explorer) was built as a stateless Python CLI tool. Powered by `uvx`, you don't even need to formally install it to run it:

```bash
uvx mcp-explorer list https://agentic-mermaid.dev/mcp
```

To inspect a specific tool and review its JSON schema:
```bash
uvx mcp-explorer inspect render_svg
```

To execute a tool directly via the command line:
```bash
uvx mcp-explorer call \
  https://agentic-mermaid.dev/mcp \
  render_svg \
  -a source 'graph TD; A-->B' \
  -a options '{"padding":24}'
```

---

### 2. `datasette-mcp`
[datasette-mcp](https://github.com/datasette/datasette-mcp) is a Datasette plugin that injects a `/-/mcp` endpoint into any Datasette instance. It provides three straightforward, read-only tools:
* `list_databases()`
* `get_database_schema(database_name)`
* `execute_sql(database_name, sql)`

Wiring this into chat tools like ChatGPT or Claude gives them direct SQL querying capabilities over your hosted data. For example, asking Claude *"what has Simon said recently about MCP?"* successfully triggered 7 separate SQL queries to retrieve the answer.

---

### 3. `llm-mcp-client`
The [llm-mcp-client](https://github.com/simonw/llm-mcp-client) alpha plugin brings official MCP integration to the [LLM command-line utility](https://llm.datasette.io/):

```bash
llm install llm-mcp-client
llm -T 'MCP("https://datasette.simonwillison.net/-/mcp")' 'count the notes'
```

Output with reasoning traces:
> *Considering note count... I see the question "count the notes" is probably asking me to tally up blog notes...*
> 
> There are **151 notes**.

Future plans include folding this directly into LLM's core and experimenting with it inside [Datasette Agent](https://agent.datasette.io/) and [llm-coding-agent](https://github.com/simonw/llm-coding-agent).

---

## 🔒 Why MCP Offers a Safer Agent Architecture
Earlier security discussions highlighted how letting end-users mix and match arbitrary tools creates severe prompt injection vulnerabilities (the "Lethal Trifecta"). General agents possessing open shell and `curl` access present massive security blind spots. 

By contrast, MCP provides structured, limited, and easily auditable capabilities. Reasoning about what an agent can and cannot do becomes vastly simpler, making MCP the preferred framework for building secure, sensitive LLM-powered applications.

---

### 🏷️ Tags
[projects](https://simonwillison.net/tags/projects) | [ai](https://simonwillison.net/tags/ai) | [datasette](https://simonwillison.net/tags/datasette) | [mermaid](https://simonwillison.net/tags/mermaid) | [generative-ai](https://simonwillison.net/tags/generative-ai) | [llms](https://simonwillison.net/tags/llms) | [llm](https://simonwillison.net/tags/llm) | [anthropic](https://simonwillison.net/tags/anthropic) | [model-context-protocol](https://simonwillison.net/tags/model-context-protocol)