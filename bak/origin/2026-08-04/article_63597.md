# The Inliner is Yielding Benefits for ZJIT

*Originally published on [Rails At Scale](https://railsatscale.com/2026-07-28-the-inliner-is-yielding-benefits/).*

---

## 📌 Executive Summary

ZJIT has recently introduced a powerful new feature: **the inliner**. By copying the body of a callee method directly into its caller's High-Level Intermediate Representation (HIR), ZJIT can leverage **code locality** and specialize code across method calls. 

Focusing on how Ruby handles blocks (specifically core utility methods like `Array#each`), the inliner bridges the gap between general-purpose library code and optimized JIT execution. Early microbenchmarks show staggering performance gains—reaching up to **35x** on loop-heavy tasks and **139x** on specific method-dispatch tests—marking a major milestone in ZJIT's maturity.

---

## 1. Ruby & Blocks: A Historical Refresher

To understand how ZJIT optimizes loops, we have to look at how iteration evolved:
* **Traditional Loops:** Manual index tracking (`while i < arr.length`).
* **Smalltalk Iteration:** Everything is an object; iteration is achieved by sending a message with a block object (e.g., `do:`).
* **Ruby (Matz's hybrid):** Combines standard loops with Smalltalk-style block passing (`arr.each do |a| ... end`).

In CRuby, passing a block involves YARV bytecode (`send` with a block argument). Meanwhile, standard data structures like `Array#each` were historically written in opaque C code, making them invisible to JIT compilers. 

To solve this, modern Rubies have rewritten core methods in Ruby itself (utilizing primitives like `Primitive.attr! :inline_block`), exposing clean structures that JITs can inspect, introspect, and optimize.

---

## 2. How JITs Work: Observe, Assume, Specialize

Following foundational lessons from Smalltalk-80, JIT compilers rely on the fact that programs are heavily localized and types rarely change unexpectedly. 

1. **Observation:** The JIT profiles what types of objects flow through a method (e.g., observing that variable `x` is consistently an `Array`).
2. **Assumption:** The JIT assumes this behavior will continue, inserting a lightweight run-time type check (`GuardType`).
3. **Specialization:** The JIT bypasses generic dispatch, replacing dynamic method lookups with specialized fast paths (like direct array length reads) and leaving behind `PatchPoint` markers to invalidate the code if assumptions fail.

While this works wonderfully for custom code, it fails for megamorphic core utility functions like `Array#each`, which see thousands of different blocks across an entire application.

---

## 3. The Solution: Inlining and Call Context

Because `Array#each` is called from countless places, it lacks internal code locality. However, the individual callers *do* pass constant, predictable blocks. 

To capture this context without relying on manual annotations or complex block-splitting heuristics, ZJIT uses **method inlining**. 

* **What is inlining?** Copying the callee's HIR (`Array#each`) directly into the caller's HIR (`method_a`).
* **The Result:** Dynamic block invocations (`invokeblock`) transform into direct instruction sequences (`InvokeBlockIseqDirect`), turning generic calls into tight, optimizable loops.

---

## 4. Performance Impact

With the inliner enabled, ZJIT's performance on block-heavy microbenchmarks skyrocketed:
* **`cfunc_itself` Benchmark:** Reached a **35x** speedup over the interpreter by folding built-in method calls directly into optimized inline loops.
* **`bmethod` Benchmark:** Hit a staggering **139x** speedup before requiring a rewrite to accurately measure modern dynamic method dispatch.

While larger real-world applications (like Rails) see more diffuse improvements, these foundational upgrades pave the way for even more aggressive optimizations, such as direct block-call inlining.

---

## 5. Wrapping Up

ZJIT is growing up fast. While developers are still actively tuning heuristics (such as `--zjit-inline-threshold`), the introduction of the inliner proves that code locality rules the day.

* **Try it out:** Explore the HIR explorer at [tryzjit.fly.dev](https://tryzjit.fly.dev/), or test ZJIT in your own applications by passing the `--zjit` flag in Ruby 4.0+.

---

### Footnotes
1. *Mostly glossing over `nil`, procs, ifuncs, etc., but iseq blocks are the common path.* ↩
2. *When methods aren't called with a constant block iseq (e.g., `&:symbol`), inline caches can be used, though this is currently rare.* ↩
3. *The iteration variable is `v91`, which maps to `v96` for array indexing (`ArrayAref`), increments via `FixnumAdd` with a constant `1`, and gets validated against array length via `v69` in basic block `bb10`.* ↩