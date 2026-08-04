# Agentic Coding Techniques

![Agentic coding techniques](http://localhost/proxy/8VhGpiHvawcGQDo8-k48X7bJM4ROlyY6OsT91PeBiEs=/aHR0cHM6Ly9zdG9yYWdlLmdob3N0LmlvL2MvYWIvYjkvYWJiOTVhZjAtM2NiNy00ZTQ5LWE2YzItYzg3YjM2ZjVkSmMyL2NvbnRlbnQvaW1hZ2VzLzIwMjYvMDgvU2NyZWVuc2hvdC0yMDI2LTA4LTAzLWF0LTguNDYuNTAtLS1BTS5wbmc=)

## Summary
While the broader AI industry faces heavy criticism for hype, environmental impacts, and over-saturation, agentic coding remains a genuinely useful and powerful time-saver. When used correctly—and overseen by a developer who reviews code before merging—agents can write high-quality, maintainable code much faster than humans. This guide covers practical techniques for utilizing open-weight and frontier models, leveraging structured LLM skills, and safely sandboxing agents using Docker and isolated credentials to prevent security risks.

---

## 1. The Current State of AI
The AI industry is burdened by hyper-inflated valuations, resource-heavy data centers, and a rush toward enterprise automation. Many companies sell monthly subscriptions below the actual cost of token usage, creating a bubble that will eventually burst. 

However, because frontier models are currently cheaper and more accessible than they will likely be in the future, developers can strategically leverage them now to accelerate coding workflows before economic corrections reshape the industry.

## 2. Open-Weight Models
When possible, relying on local open-weight models provides privacy and control. Running a powerful hardware setup (such as a 128GB RAM server with Ollama) enables local workflows using models like:
* **`qwen3-coder-next:q8_0`** (84 GB) for coding.
* **`qwen3-vl:32b-thinking-q8_0`** (35 GB) for vision tasks.

### Use Cases for Local Models:
* **Secret Projects:** Generating code without exposing proprietary source code to third parties.
* **Sensitive Data Analysis:** Analyzing private datasets locally while letting frontier models write the helper code.
* **Private Chatbots:** Managing simple, low-context tasks via local interfaces like [Open WebUI](https://openwebui.com).
* **Repetitive Scaling Tasks:** Executing high-volume, low-complexity tasks (like extracting browser URLs from millions of screenshots) without incurring API costs.

## 3. Agentic Coding Tools
Moving away from expensive IDE-integrated tools like GitHub Copilot, CLI-based agents offer greater flexibility and easier sandboxing:
* **[Claude Code CLI](https://code.claude.com/docs/en/overview)** for Anthropic models.
* **[Codex CLI](https://learn.chatgpt.com/docs/codex/cli)** for OpenAI models.
* **[OpenCode](https://opencode.ai)** for locally hosted Ollama models.

## 4. Structured LLM Skills
Integrating workflows like Matt Pocock’s [LLM Skills](https://github.com/mattpocock/skills) transforms how agents operate:
* **"Grilling Sessions":** Forcing the LLM to aggressively question the developer about feature specifications *before* writing any code to catch edge cases early.
* **Issue Tracker Integration:** Using commands like `/to-tickets` to convert specs into GitHub issues, and `/implement` to autonomously build, review, and create pull requests for well-defined tasks.
* **Specialized Ecosystem Skills:** Utilizing tools like [Expo Skills](https://docs.expo.dev/skills/) for tedious upgrades or security-focused repositories (e.g., [Trail of Bits Skills](https://github.com/trailofbits/skills)).

## 5. Sandboxing the Agents
To let agents execute end-to-end tasks autonomously (e.g., implementing an issue, pushing code, and opening a PR), they must run in "YOLO mode" (`--dangerously-skip-permissions` or `--dangerously-bypass-approvals-and-sandbox`). **Never run agents with these flags directly on your host machine.**

### Recommended Workflow: [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/)
Using the `sbx` command isolates agents within dedicated Docker VMs, providing:
* **Kernel Isolation:** Runs containers inside an independent VM.
* **Nested Container Support:** Allows test suites reliant on Docker Compose to function normally.
* **Network Restrictions:** Proxies all network traffic through a firewall restricted to trusted development domains (GitHub, NPM, PyPI, etc.).
* **Credential Isolation:** Configures authentication tokens safely per sandbox.

## 6. Isolating GitHub Access
Giving an agent full access via the GitHub CLI (`gh`) creates massive security risks if the agent is prompt-injected. To limit exposure:
* **Scoped Personal Access Tokens (PATs):** Create fine-grained GitHub PATs restricted strictly to the specific repository the sandbox is modifying, then store them in the sandbox's secrets manager.
* **Dedicated SSH Keys:** Use a signing-only SSH key exclusively for agent commits, ensuring no other keys are forwarded into the container.

These security layers ensure that even if an agent goes rogue, it remains strictly contained within a single repository and sandbox environment.