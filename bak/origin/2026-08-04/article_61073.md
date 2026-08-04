# Mermaid to Unicode Box Art (grok-mermaid)

### Summary
This project showcases a browser-based tool that converts Mermaid diagrams into Unicode box art. By porting a Rust-based terminal renderer from the open-sourced Grok CLI codebase to WebAssembly, this tool enables high-quality, text-based diagram rendering directly in the browser.

---

### Overview
While exploring the codebase for the newly open-sourced [Grok CLI coding agent](https://simonwillison.net/2026/Jul/15/grok-build/), I discovered a fascinating component: `xai-grok-markdown/src/mermaid.rs`. This file contains a self-contained terminal renderer for Mermaid diagrams written in Rust.

I decided to bring this functionality to the browser using WebAssembly. You can try the resulting tool here: **[Mermaid to Unicode box art (grok-mermaid)](https://tools.simonwillison.net/grok-mermaid)**.

### Development Process
The implementation was achieved by leveraging AI-assisted coding. You can view the specific prompt I used in Claude Code (Fable 5) [in this pull request](https://github.com/simonw/tools/pull/293#issue-4897479396).

### Preview
![Screenshot of a Mermaid diagram editor showing source code and rendered flowchart. The code reads: graph TD Start[Request received] --> Auth{Authenticated?} Auth -->|yes| Rate{Rate limit OK?} Auth -->|no| R401[401 Unauthorized] Rate -->|yes| H(Handle request) Rate -->|no| R429[429 Too Many Requests] H -.-&gt; Log[Audit log] H ==&gt; Resp[200 OK]. Below the code are controls labeled Max width: Fit output panel, Copy as text, and Copy link to this diagram. The rendered flowchart on a dark background flows top-down: Request received leads to Authenticated?, which branches yes to Rate limit OK? and no to 401 Unauthorized. Rate limit OK? branches yes to Handle request and no to 429 Too Many Requests. Handle request connects with a dotted arrow to Audit log and a thick arrow to 200 OK.](./images/9b0ca2599168.png)

---

**Tags:** #tools #rust #webassembly #mermaid #grok #xai