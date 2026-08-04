# How I Use AI on This Blog

Inspired by [this LessWrong post](https://www.lesswrong.com/posts/tgigHkZoYrJEGe4tP/ai-use-policy-for-my-essay-writing), I wanted to document my current AI workflow. This isn't just for disclosure; it’s a snapshot of my process so I can track how it evolves.

My working philosophy is simple: **AIs identify problems, and I fix them myself.** With rare, clearly flagged exceptions, the text and code on this blog are human-generated. This is not a moral stance, but a constraint to ensure this remains a place for me to [learn in public](https://www.gilesthomas.com/2025/02/20250223-til-deep-dive-posts).

---

## Ideation and Running Experiments
Every post originates from my own ideas and work. For large-scale coding projects, I often keep chat sessions open with ChatGPT or Claude. Because the value of these projects lies in the learning process, I avoid letting the AI do the "thinking" for me. 

If an AI starts explaining concepts I should be learning through experimentation, I pivot it into "rubber duck" mode. For complex projects, I use AI for code review—I paste my code, explain the goal, and ask the model to identify bugs without rewriting the solution.

## Writing and the Editorial Board
Once I finish a project, I write the draft entirely on my own. Then, it enters my "editorial board" process:

1.  **Claude:** I ask for feedback on technical errors, missing steps, or over-explanations. Crucially, I instruct it **not to rewrite anything**.
2.  **ChatGPT:** I use it to catch issues with metaphors or technical terminology clashes. It is particularly diligent at checking external links and supporting materials.
3.  **The "Cast":** I run the draft past a rotating group of models (currently DeepSeek, Grok, GLM-5.2, and Kimi K3) to catch any remaining blind spots.
4.  **Final Polish:** I perform a final read-through on a staging site, ideally after dinner, to smooth out the prose and ensure it remains conversational.

This process takes anywhere from 30 minutes to two hours, depending on the post's complexity—a small price for the resulting polish.

## AI Coding
My rule for code is: **If I would learn something by writing it, I write it by hand.** 

I only delegate to AI for "utility" code—such as `matplotlib` charts or visualization scripts—that doesn't contribute to my core learning goals. Even then, I avoid agentic systems (like Claude Code or Codex) for blog work, preferring the friction of a standard chat interface to keep the scope minimal and focused.

## The Future of Agents
While I use agentic tools like OpenClaw, Codex, and Claude Code for my professional life and personal projects, they aren't currently part of my blogging workflow. My current focus is on low-level, hands-on learning. As my foundation grows, I may eventually use agents to handle the "details" while I focus on the broader strokes. 

Until then, every word and almost every line of code remains hand-crafted—even if I rely on AI to keep me on track and coherent.

***

### Footnotes
[^1]: If you're wondering "why not use Claude Code or Codex," I avoid them for blog-related work to maintain manual control over the learning process.
[^2]: **Current thoughts on the "Cast":**
    *   **DeepSeek:** Awaiting updates to regain its previous standing.
    *   **Grok:** Improving; less prone to turning posts into "clickbait" than in earlier versions.
    *   **GLM-5.2:** Surprisingly context-aware regarding the "near-future" nature of my writing.
    *   **Kimi K3:** Very impressive; I particularly appreciate the depth of its chain-of-thought output.
[^3]: ChatGPT, being true to form, requested I clarify that this "human-generated" rule excludes direct quotes from models used as examples within my posts.