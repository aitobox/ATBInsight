# Rewriting Bun in Rust

> **Summary:** Jarred Sumner shares the story of rewriting Bun from Zig to Rust using sophisticated agentic engineering. Challenging traditional software wisdom that says "never rewrite from scratch," this massive undertaking was made possible by AI coding agents, a robust TypeScript test suite used as a conformance suite, and a need to eliminate complex memory-management bugs.

---

## Introduction

Jarred Sumner has been promising a blog post about his Zig-to-Rust rewrite of [Bun](https://bun.com/blog/bun-in-rust) since May 9th—for significantly longer than it actually took him to finish the rewrite. 

The wait was well worth it. The post details an extremely sophisticated piece of agentic engineering featuring dynamic workflows, trial runs, adversarial review, and a variety of other clever techniques.

While Jarred spends the first half of the post praising Zig for getting Bun to its current state, he arrives at a significant realization:

> Our bugfix list felt bad and I was tired of going to sleep worrying about crashes in Bun. I don't blame Zig for that - other users of Zig don't have the bugs we had, and mixing GC with manually-managed memory is an uncommon enough thing for software to need that no language really designs for it. We wouldn't have gotten this far if not for Zig, and I'll always be grateful. **Until very recently, programming language choice was a one-way decision for a project like Bun.**

---

## Why Rewrite? Entering the Age of AI Agents

Conventional software wisdom—famously highlighted by Joel Spolsky in [Things You Should Never Do, Part I](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/) back in April 2000—dictates that you should never stop the world and rewrite a large piece of software from the ground up. 

However, coding agents powered by today's frontier models completely change that equation.

### The Memory Management Challenge

The primary motivation for choosing Rust came down to safety and memory management:

> A large percentage of bugs from that list are use-after-free, double-free, and "forgot to free" in an error path. In safe Rust, these are compiler errors and RAII-like automatic cleanup with `Drop`.

---

## The Role of Conformance Suites and AI

A crucial enabling factor for the rewrite was Bun's comprehensive test suite written in TypeScript, which served as a robust [conformance suite](https://simonwillison.net/tags/conformance-suites/). This allowed an agent harness to automate much of the initial porting process as an experiment with an early version of the model now available as Mythos/Fable.

> At first, I didn't expect it to work. A few days in, a high % of the test suite started passing and I saw how much the new Rust code matched up with the original Zig codebase. My opinion went from "this is worth trying" to "I'm going to merge this". [...]
>
> For most of those 11 days (and after), I monitored workflows - manually reading the outputs to check for issues and bugs, and prompting Claude to edit the loop to fix things.

### Reviewing a Million-Line Pull Request

How do you build confidence in merging massive quantities of LLM-authored code? Jarred's approach relied on:
* A language-independent test suite containing over a million assertions.
* Adversarial code review.
* Fixing the *process* that generates the code when something goes wrong, rather than manually patching the code itself.

---

## Deployment and Costs

The new Rust-based implementation of Bun has been live in Claude Code for nearly a month:

> Claude Code v2.1.181 (released June 17th) and later use the Rust port of Bun. Startup got 10% faster on Linux but otherwise, barely anyone noticed. Boring is good.

Of course, working at Anthropic comes with one distinct perk: not having to pay out-of-pocket for tokens—especially handy when the estimated API cost hits **$165,000**:

> Pre-merge, this took 5.9 billion uncached input tokens, 690 million output tokens, and 72 billion cached input token reads — around $165,000 at API pricing.

Ultimately, the rewrite stands as a fascinating case study in taking on wildly ambitious engineering projects through the power of coordinated, parallel AI agents.

---

*Via [Hacker News](https://news.ycombinator.com/item?id=48837877)*

**Tags:** [ai](https://simonwillison.net/tags/ai), [rust](https://simonwillison.net/tags/rust), [zig](https://simonwillison.net/tags/zig), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [ai-assisted-programming](https://simonwillison.net/tags/ai-assisted-programming), [anthropic](https://simonwillison.net/tags/anthropic), [bun](https://simonwillison.net/tags/bun), [conformance-suites](https://simonwillison.net/tags/conformance-suites), [agentic-engineering](https://simonwillison.net/tags/agentic-engineering), [claude-mythos-fable](https://simonwillison.net/tags/claude-mythos-fable)