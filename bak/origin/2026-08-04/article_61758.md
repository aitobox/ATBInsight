# Claude Code Uses Bun Written in Rust Now

> **Summary:** Recent releases of Anthropic's Claude Code (v2.1.181 and later) quietly incorporate the newly Rust-rewritten version of Bun. This article explores how to verify this production rollout using simple command-line inspection techniques.

---

## Background

In the blog post [Rewriting Bun in Rust](https://bun.com/blog/bun-in-rust), Jarred Sumner dropped an interesting production detail:

> *"Claude Code v2.1.181 (released June 17th) and later use the Rust port of Bun. Startup got 10% faster on Linux but otherwise, barely anyone noticed. Boring is good."*

Intrigued by this claim, I decided to inspect my own local Claude Code installation to find concrete evidence of the Rust-based Bun runtime in action.

---

## Verifying the Rust-Based Bun

I found two quick commands particularly convincing:

### 1. Checking the Embedded Bun Version
Running the following command checks the binary strings for the embedded Bun version:

```bash
strings ~/.local/bin/claude | grep -m1 'Bun v1'
```

For me, this outputs `Bun v1.4.0 (macOS arm64)`. Because the most recent public GitHub release of [Bun](https://github.com/oven-sh/bun/releases) at the time was `v1.3.14`, this indicates that Claude Code was shipping with an unreleased, preview version of Bun. 

> **Update:** This Rust version is now available via [Bun canary builds](https://bun.com/docs/installation#canary-builds). Running `bun upgrade --canary` will install [this release](https://github.com/oven-sh/bun/releases/tag/canary).

### 2. Inspecting Embedded Rust Source Paths
Next, searching for Rust source file references within the binary yields a definitive list:

```bash
strings ~/.local/bin/claude | grep -Eo 'src/[[:alnum:]_./-]+\.rs'
```

This outputs a list of [563 filenames](https://gist.github.com/simonw/c92fb0f67b114ac26e3b95a09ddccfdc), beginning with:

```text
src/runtime/bake/dev_server/mod.rs
src/runtime/bake/production.rs
src/bundler/bundle_v2.rs
```

It appears that Bun written in Rust is indeed running smoothly in production across millions of devices. As Jarred said: *"Boring is good."*

---

## Bonus Trick: Verifying via Preload

Here is a neat trick shared [by Ajan Raj](https://twitter.com/ajanraj25/status/2078825794701242697) to check the embedded version dynamically:

```bash
cat > /tmp/bun-version.ts <<'EOF'
console.log("embedded bun:", Bun.version);
process.exit(0);
EOF

BUN_OPTIONS="--preload=/tmp/bun-version.ts" claude --version
```

This outputs `1.4.0` on my machine. 

For the curious, you can inspect [the commit from May 17th](https://github.com/oven-sh/bun/commit/b18bf6d1d0a92238f240bfd125f0e3b3461b9243#diff-7ae45ad102eab3b6d7e7896acd08c427a9b25b346470d7bc6507b6481575d519) which updated the version in `package.json` to `1.4.0`.

---

**Tags:** [bun](https://simonwillison.net/tags/bun) | [rust](https://simonwillison.net/tags/rust) | [anthropic](https://simonwillison.net/tags/anthropic) | [claude-code](https://simonwillison.net/tags/claude-code) | [jarred-sumner](https://simonwillison.net/tags/jarred-sumner)