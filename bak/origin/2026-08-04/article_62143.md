# A Fireside Chat with Cat and Thariq from the Claude Code Team

**Host:** Simon Willison  
**Guests:** Cat Wu and Thariq Shihipar (Anthropic)  
**Event:** AI Engineer World's Fair  
**Original Media:** [Watch on YouTube](https://www.youtube.com/watch?v=uU5Gv2h8-9g)

---

## 📌 Executive Summary

Earlier this year, Simon Willison sat down with Cat Wu and Thariq Shihipar from Anthropic’s Claude Code team at the AI Engineer World's Fair. The conversation explored the cutting edge of AI-assisted software engineering, multi-agent collaboration, system prompt optimization, and internal workflows at Anthropic. 

### Key Takeaways:
* **Claude Tag's Impact:** Anthropic's collaborative Slack integration, Claude Tag, now successfully lands **65% of product engineering PRs** for the team.
* **The Death of "Don't Do X":** For frontier models like Fable and Opus 4.8, restrictive negative prompts ("don't do X") and extensive few-shot examples are no longer best practices. Claude Code's system prompt has recently **shrunk by 80%** to rely more on model judgment.
* **Rewrites are Back:** With robust test suites, codebases act as living specs, making full rewrites (like rewriting Bun in Rust internally) not only viable but advantageous.
* **Internal "Ant Fooding":** Anthropic holds a strict internal bar—features must demonstrate strong user retention among employees before shipping externally.
* **Auto Mode & Security:** Backed by thousands of evals and adversarial red-teaming, Auto Mode handles dynamic permissions and sandbox breakouts securely, laying the groundwork for safe asynchronous workflows.
* **Shift in Ambition:** To combat the "Deep Blue" feeling of loss in traditional coding, engineers must scale up their ambition—solving larger, more complex problems faster than ever.

---

## 📅 Chronological Transcript & Highlights

### How Has Your Day-to-Day Changed in the Past Year?
* **Simon:** How has your day-to-day work shifted since Claude Code launched less than a year and a half ago?
* **Cat:** Initially, we monitored every single permission prompt closely. Now, with model generations improving, we've stepped back to delegate menial implementation, freeing us up to focus on UX and product experience. With Fable, we can frequently one-shot complex features.
* **Thariq:** We amnesiacally forget how much we used to babysit prompts. Now, my goal is simply to do higher-quality work faster. I've even used it to successfully meet brand standards for video editing in a matter of hours.

### What Conventional Software Engineering No Longer Holds?
* **Cat:** The traditional 6-to-12-month product requirement document (PRD) cycle is dead. Because building is so fast, product managers and engineers need stronger **business sense and product taste** to determine what is worth building in a matter of days.
* **Thariq:** **Rewrites are good now.** The old "never rewrite" rule from *The Mythical Man-Month* no longer holds if you have a great test suite. A codebase is a living spec, and rewriting it can be liberating. (Note: Anthropic internally shipped Claude Code running on Bun-in-Rust).

### What Are Non-Engineers Doing with Claude Tag?
* **Cat:** Claude Tag is multiplayer by default, living natively in Slack channels. It's proactive rather than reactive—monitoring bug reports, opening PRs, and tagging relevant engineers. It also features **team memory**, remembering natural language team preferences. It currently lands 65% of product engineering PRs.
* **Thariq:** Non-engineers use it as an organizational search engine, hooking it into event stores to answer metric questions, clone codebases, and demonstrate live feature recordings.

### Claude Tag as a Team Collaborative Layer
* **Cat:** Sessions are fluid and multiplayer. One person kicks off a task, design jumps in to nudge the UI, and engineering takes it across the finish line. 
* **Thariq:** Working in public channels levels up team dynamics, naturally teaching everyone better prompting habits—reminiscent of how Midjourney taught users via public Discord channels.

### Prioritization When Building is Cheap
* **Cat:** We rely heavily on **internal dogfooding ("ant fooding")** and a strict retention bar. If a feature isn't polished enough to retain internal users, we don't ship it.

### Surprising Feature Engagement: Remote Control
* **Cat:** Many team members plug in their laptops, lock their screens, and use **Remote Control** from their mobile devices on the couch to command local CLI Claude Code sessions—a workflow Cat initially didn't anticipate.

### Does a Human Review Every Line of Production Code?
* **Thariq:** Critical code domains have strict human code owners. However, for outer layers, **Claude Code fully reviews the PRs**.
* **Cat:** Moving humans out of the loop took six months of building trust. We turn incident root causes into automated evals so code reviews never regress.

### Building Intuition for New Models via Evals
* **Cat:** Our comprehensive eval suite allows new models (like Fable) to act as drop-in replacements. For Auto Mode, we use thousands of evals and external red teams to test against prompt injections and malicious inputs.

### System Prompt Reductions: Cutting Down by 80%
* **Thariq:** We removed extensive few-shot examples and restrictive negative instructions ("don't do X"). Newer frontier models perform better with cleaner context and fewer hard constraints.
* **Cat:** Instead of absolute rules like "always verify," we prompt models to use nuanced judgment based on the scale of the change. We maintain model-specific system prompts so smaller models still get more explicit guardrails.

### The Bar for Introducing New Tools
* **Thariq:** Tool design is more of an "art or biology" than a hard science. We trend toward fewer, more general-purpose tools with distinct functions.
* **Cat:** The file editing tool remains valuable because it allows us to render a nice deterministic UI for user approval, though Auto Mode users rarely need to look at it.

### Safety, Security, and Auto Mode
* **Cat:** Almost everyone at Anthropic uses Auto Mode for long-running workflows. Extensive adversarial testing shows its risk profile for prompt injection and data exfiltration is far lower than an average human reviewer.
* **Thariq:** Auto Mode uses a built-in **Sonnet classifier** to evaluate tool calls against user intent dynamically (e.g., distinguishing between explicit instructions to push to GitHub versus general safety blocks). Combined with sandboxing and credential injection (where proxies audit and inject keys dynamically), it enables secure autonomous operations.

### Dealing with the Human Element: "Being More Ambitious"
* **Thariq:** If you try to do the exact same work you did before LLMs, it can feel hollow. **The antidote to the "Deep Blue" feeling is to scale up your ambition.** Success is fun, and tackling massive rewrites or sweeping projects brings back the joy of creation.
* **Cat:** The PM role has evolved into a hybrid of engineer, designer, and PM—automating every bottleneck between an idea and customer delivery.

### What Surprised You? (Advanced Video Editing)
* **Thariq:** Fable successfully edited a conference talk video entirely via a one-shot prompt: it transcribed audio, recognized deck slide changes, converted an HTML deck into visual assets, tracked Thariq's physical movement across the stage via dynamic cropping, and compiled it using `ffmpeg` and Remotion.

### What Can't It Do Yet?
* **Cat:** It still lacks genuine design and UX taste for entirely novel frontier interactions.
* **Thariq:** Interacting with the physical world—solving real-world science and orchestrating physical experiments.

### Cultural Hacks to Steal from Anthropic
* **Cat:** Keep communication channels public so AI tools like Claude Tag have maximum contextual awareness.
* **Thariq:** **Never negotiate against yourself.** Avoid talking yourself out of ambitious projects based on assumed trade-offs; let reality prove the trade-offs to you.

---

## 🏷️ Tags
`ai` | `prompt-engineering` | `generative-ai` | `llms` | `anthropic` | `annotated-talks` | `coding-agents` | `claude-code` | `thariq-shihipar` | `cat-wu`