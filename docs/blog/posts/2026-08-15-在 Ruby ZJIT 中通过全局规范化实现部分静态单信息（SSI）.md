---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-15
hide:
- navigation
tags:
- Ruby
- ZJIT
- 编译器优化
- SSA
- SSI
title: 在 Ruby ZJIT 中通过全局规范化实现部分静态单信息（SSI）
---
### 文章背景与核心概要

本文探讨了如何在 Ruby 的 ZJIT 编译器中扩展全局的 `canonicalize`（规范化）优化趟（Pass），从而实现部分静态单信息（Partial Static Single Information, SSI）的好处。继之前关于 SSA 和类型精炼的工作之后，文章展示了如何通过将分支条件常量注入基于支配树（dominator-based）的 `rewrite_map` 中，使基本块能够自动从传入的控制边推断布尔状态，从而成功消除冗余的条件分支。

这种技术允许编译器在更一般的控制流场景中捕获变量的真假状态，而不仅仅依赖于显式的类型精炼指令。通过在基本块入口处根据前驱分支条件“播种”重写映射，ZJIT 能够穿透多个基本块传播常量状态，最终简化复杂的控制流图（CFG），提升生成的机器码质量。

---

## 摘要

This post explores how to extend a global `canonicalize` optimization pass in Ruby's ZJIT compiler to achieve partial Static Single Information (SSI) benefits. Following up on previous work regarding SSA and type refinement, the article demonstrates how seeding a dominator-based `rewrite_map` with branch condition constants allows basic blocks to automatically infer boolean states from incoming control edges, successfully eliminating redundant conditional branches.

> 本文探讨了如何在 Ruby 的 ZJIT 编译器中扩展全局的 `canonicalize`（规范化）优化趟，从而实现部分静态单信息（SSI）的好处。继之前关于 SSA 和类型精炼的工作之后，文章展示了如何通过将分支条件常量注入基于支配树的 `rewrite_map` 中，使基本块能够自动从传入的控制边推断布尔状态，从而成功消除冗余的条件分支。

---

## Context: The Journey to Global Canonicalization

*See [the previous post](https://bernsteinbear.com/blog/partial-ssi/) for context and explanation of SSI.*

After reading [Chris Fallin’s aegraph post](https://cfallin.org/blog/2026/04/09/aegraph/), new ZJIT contributor `dak2` landed a block-local version of the `canonicalize` function in [#16828](https://github.com/ruby/ruby/pull/16828).

The pseudocode of the block-local canonicalize function looks like this:

```python
for block in function.reverse_post_order():
    rewrite_map = {}
    for insn in block.insns:
        insn.operands.map_in_place(lambda o: rewrite_map.get(o, o))
        if insn.opcode == "GuardType":
            rewrite_map[insn.val] = insn
```

As a refresher, this turns IR like this:

```
v0:Object = ...
v1:Int = GuardType v0, Int
... do something with v1

v2:Int = GuardType v0, Int
... do something with v2
```

into this:

```
v0:Object = ...
v1:Int = GuardType v0, Int
... do something with v1

v2:Int = GuardType v1, Int
... do something with v2
```

Note that the second use of `v0` has been turned into `v1`. This is important because a later constant-folding pass can observe that the input `v1` of `GuardType v1, Int` is *already an Int* and can therefore replace all uses of `v2` with `v1` and delete the guard.

Because in this local version we make a new `rewrite_map` for each block, we don’t carry any rewrites across blocks (but ZJIT still gained a lot because until recently its IR was in maximal SSA form, so a block-local pass had more global effects).

> ## 背景：迈向全局规范化之旅
> 
> *有关 SSI 的背景和解释，请参阅[上一篇文章](https://bernsteinbear.com/blog/partial-ssi/)。*
> 
> 在阅读了 [Chris Fallin 的 aegraph 一文](https://cfallin.org/blog/2026/04/09/aegraph/)之后，ZJIT 的新贡献者 `dak2` 在 [#16828](https://github.com/ruby/ruby/pull/16828) 中提交了 `canonicalize` 函数的块级局部版本。
> 
> 块级局部规范化函数的伪代码如下所示：
> 
> ```python
> for block in function.reverse_post_order():
>     rewrite_map = {}
>     for insn in block.insns:
>         insn.operands.map_in_place(lambda o: rewrite_map.get(o, o))
>         if insn.opcode == "GuardType":
>             rewrite_map[insn.val] = insn
> ```
> 
> 作为复习，这会将这样的 IR：
> 
> ```
> v0:Object = ...
> v1:Int = GuardType v0, Int
> ... 对 v1 进行操作
> 
> v2:Int = GuardType v0, Int
> ... 对 v2 进行操作
> ```
> 
> 转化为这样：
> 
> ```
> v0:Object = ...
> v1:Int = GuardType v0, Int
> ... 对 v1 进行操作
> 
> v2:Int = GuardType v1, Int
> ... 对 v2 进行操作
> ```
> 
> 请注意，`v0` 的第二次使用已被替换为 `v1`。这一点很重要，因为随后的常量折叠（constant-folding）趟可以观察到 `GuardType v1, Int` 的输入 `v1` *已经是一个 Int*，因此可以用 `v1` 替换 `v2` 的所有使用并删除该保护指令（guard）。
> 
> 由于在这个局部版本中，我们为每个基本块都创建了一个新的 `rewrite_map`，因此我们不会将任何重写跨基本块传递（但 ZJIT 仍然获益良多，因为直到最近其 IR 仍处于极大 SSA 形式，所以块级局部的趟也能产生更广泛的全局效果）。

---

## Scaling Up to a Global Canonicalize Pass

About five days later, `dak2` came back with a global version in [#17013](https://github.com/ruby/ruby/pull/17013)! This PR came with a bunch of changes in the name of performance—which I appreciate—but I like doing the silly slow thing first, especially because the PR is so much smaller. We can always refactor it later to be faster and, in the meantime, use the slow but maybe-easier-to-verify thing as a correctness oracle. So I did[^1] the silly slow thing in [#17766](https://github.com/ruby/ruby/pull/17766).

This copy-happy version of canonicalize looks like:

```python
rewrite_maps = {block: {} for block in blocks}
dominators = compute_dominators()
for block in function.reverse_post_order():
    rewrite_map = rewrite_maps[dominators.idom(block)].clone()
    for insn in block.insns:
        insn.operands.map_in_place(lambda o: rewrite_map.get(o, o))
        if insn.opcode == "GuardType":
            rewrite_map[insn.val] = insn
    rewrite_maps[block] = rewrite_map
```

*(Which you may or may not notice looks a lot like [Maxine’s GVN implementation](https://github.com/beehive-lab/Maxine-VM/blob/e213a842f78983e2ba112ae46de8c64317bc206e/com.sun.c1x/src/com/sun/c1x/opt/GlobalValueNumberer.java). This is not a coincidence.)*

The core stays the same as the block-local version, but now we can cascade rewrites along the dominator tree. I say that, but we’re not actually computing a (top-down walkable) dominator tree—we’re only building a (bottom-up) map of `idom` using [the engineered algorithm](https://bernsteinbear.com/assets/img/dominators-engineered.pdf) (PDF). The rewrites still cascade down the dominator tree because this RPO-walk + idom-clone approach ends up being equivalent to actually walking a dominator tree.

The block iteration order is different (RPO vs domtree pre-order) but the only property we care about maintaining is that we visit dominators before blocks that get dominated, and that is true in both.

> ## 扩展到全局规范化趟
> 
> 大约五天后，`dak2` 在 [#17013](https://github.com/ruby/ruby/pull/17013) 中带来了全局版本！这个 PR 包含了一系列为了性能而做的改动——对此我很赞赏——但我喜欢先做那个看起来有点蠢但很慢的版本，特别是当这个版本的代码量要小得多的时候。我们以后随时可以将其重构得更快，在此期间，可以将这个虽慢但或许更容易验证的版本作为正确性的预言机（correctness oracle）。因此，我在 [#17766](https://github.com/ruby/ruby/pull/17766) 中实现了那个略显笨拙但直观的慢版本[^1]。
> 
> 这个频繁复制的规范化版本看起来像这样：
> 
> ```python
> rewrite_maps = {block: {} for block in blocks}
> dominators = compute_dominators()
> for block in function.reverse_post_order():
>     rewrite_map = rewrite_maps[dominators.idom(block)].clone()
>     for insn in block.insns:
>         insn.operands.map_in_place(lambda o: rewrite_map.get(o, o))
>         if insn.opcode == "GuardType":
>             rewrite_map[insn.val] = insn
>     rewrite_maps[block] = rewrite_map
> ```
> 
> *（你可能会或可能不会注意到，这看起来非常像 [Maxine 的 GVN 实现](https://github.com/beehive-lab/Maxine-VM/blob/e213a842f78983e2ba112ae46de8c64317bc206e/com.sun.c1x/src/com/sun/c1x/opt/GlobalValueNumberer.java)。这绝非巧合。）*
> 
> 其核心逻辑与块级局部版本保持一致，但现在我们可以沿着支配树（dominator tree）级联重写。话虽如此，我们实际上并没有去计算一个（自顶向下遍历的）支配树——我们只是使用[经过工程优化的算法](https://bernsteinbear.com/assets/img/dominators-engineered.pdf)（PDF）构建了一个（自底向上的）`idom`（直接支配者）映射。重写仍然会沿支配树向下级联，因为这种“逆后序遍历（RPO-walk）+ idom 克隆”的方法最终等同于实际遍历支配树。
> 
> 基本块的遍历顺序有所不同（RPO 与支配树先序遍历），但我们需要维护的唯一属性是：在访问被支配的基本块之前必须先访问支配者，这两种方法都满足该属性。

---

## Applying Canonicalization to Partial SSI

But where was I going with all this?

…

Oh, right. More [partial SSI](https://bernsteinbear.com/blog/partial-ssi/). In the last post, we inserted `RefineType` in SSA construction so that we can infer things about the Ruby type of the conditional. For example:

```
bb0:
  v0: Object = ...
  v1: CBool = Test v0
  v2: Truthy = RefineType v0, Truthy
  v3: Falsy = RefineType v0, Falsy
  CondBranch v1, bb1(v2), bb2(v3)

bb1(v4:Truthy):
  ...

bb2(v5:Falsy):
  ...
```

This is neat when the branch comes from Ruby code, but sometimes we synthesize branches, so we can’t do this in SSA construction. The general case looks like this:

```
bb0:
  v0: CBool = ...
  CondBranch v0, bb1, bb2

bb1:
  ...

bb2:
  ...
```

In this more general case, we still want `bb1` to know that `v0` is `CBool[true]` in that branch and `bb2` to know that `v0` is `CBool[false]` in its branch (and in blocks dominated by `bb1` and `bb2`).

Well, this is another thing we can do in `canonicalize`!

> ## 将规范化应用于部分 SSI
> 
> 但是我讲这一切的最终目的是什么呢？
> 
> ……
> 
> 哦，对。更多关于[部分 SSI](https://bernsteinbear.com/blog/partial-ssi/)的内容。在上一篇文章中，我们在构建 SSA 时插入了 `RefineType`，以便我们可以推断条件表达式的 Ruby 类型。例如：
> 
> ```
> bb0:
>   v0: Object = ...
>   v1: CBool = Test v0
>   v2: Truthy = RefineType v0, Truthy
>   v3: Falsy = RefineType v0, Falsy
>   CondBranch v1, bb1(v2), bb2(v3)
> 
> bb1(v4:Truthy):
>   ...
> 
> bb2(v5:Falsy):
>   ...
> ```
> 
> 当分支来自 Ruby 代码时，这非常巧妙，但有时我们会合成一些分支，因此在 SSA 构建阶段无法做到这一点。一般情况如下：
> 
> ```
> bb0:
>   v0: CBool = ...
>   CondBranch v0, bb1, bb2
> 
> bb1:
>   ...
> 
> bb2:
>   ...
> ```
> 
> 在这种更一般的情况下，我们仍然希望 `bb1` 知道在该分支中 `v0` 是 `CBool[true]`，并且 `bb2` 知道在其分支中 `v0` 是 `CBool[false]`（以及在被 `bb1` 和 `bb2` 支配的基本块中也是如此）。
> 
> 嗯，这是我们可以在 `canonicalize` 中做的另一件事！

---

## Seeding the Rewrite Map

All we need to do is at the beginning of each block `B`:

* Check if `B` has one incoming control edge `E`[^2]
* Check if the terminator `T` for `E.block` is a conditional branch
* If `T.iftrue == B`, seed the `rewrite_map` with `T.cond => Const(CBool[true])`
* If `T.iffalse == B`, seed the `rewrite_map` with `T.cond => Const(CBool[false])`

If you plan on running `canonicalize` multiple times, you may end up generating many constant instructions in your IR. To avoid this, you can intern them and, for example, place them in the entry block. This helps make the pass idempotent instead of always allocating new instructions.

### What Does This Buy Us?

Well, I admit I was looking at the `30k_ifelse` benchmark on ruby-bench and wondering how to further collapse a bunch of IR that came out of my prototype value numbering implementation. The IR after value numbering looked like:

```
bb0:
  v0: CBool = ...
  CondBranch v0, bb1, bb2

bb1:
  ...
  CondBranch v0, ...

bb2:
  ...
  CondBranch v0, ...
```

And it felt a little silly that `bb1` and `bb2` didn’t get more information about `v0` by being branch targets. This couple-line change managed to collapse a bunch of those branches.

So, perhaps a bit contrived, but it feels like a useful tool to have.

See you all next time!

---

## Footnotes

[^1]: This PR landed much later than `dak2`’s because I wanted to wait for the [SSA minimization pass](https://github.com/ruby/ruby/pull/17311) to land—more on that another time—so that global canonicalization could do more. Otherwise, because we had maximal SSA, we didn’t really re-use SSA values across blocks. [↩](#fnref:much-later)
[^2]: It’s possible to have one block `A` do a conditional branch to another block `B` for both the `iftrue` case and the `iffalse` case. This is useful if, for example, it is passing different data along the block arguments of each edge. For this reason, we check the number of incoming edges, not the number of predecessor blocks. [↩](#fnref:block-vs-edge)

> ## 播种重写映射
> 
> 我们需要做的一切就是在每个基本块 `B` 的开头：
> 
> * 检查 `B` 是否只有一条传入的控制边 `E`[^2]
> * 检查 `E.block` 的终结指令（terminator）`T` 是否是一个条件分支
> * 如果 `T.iftrue == B`，则用 `T.cond => Const(CBool[true])` 播种 `rewrite_map`
> * 如果 `T.iffalse == B`，则用 `T.cond => Const(CBool[false])` 播种 `rewrite_map`
> 
> 如果你计划多次运行 `canonicalize`，最终可能会在 IR 中生成许多常量指令。为了避免这种情况，你可以对其进行内化（intern），例如将它们放在入口块中。这有助于使该优化趟具有幂等性，而不是总是分配新的指令。
> 
> ### 这给我们带来了什么？
> 
> 嗯，我承认我当时正在查看 ruby-bench 上的 `30k_ifelse` 基准测试，并琢磨着如何进一步折叠从我的原型值编号（value numbering）实现中产生的一堆 IR。值编号之后的 IR 看起来像这样：
> 
> ```
> bb0:
>   v0: CBool = ...
>   CondBranch v0, bb1, bb2
> 
> bb1:
>   ...
>   CondBranch v0, ...
> 
> bb2:
>   ...
>   CondBranch v0, ...
> ```
> 
> `bb1` 和 `bb2` 作为分支目标，却没有获得关于 `v0` 的更多信息，这让人感觉有点傻。这几行代码的改动成功折叠了其中许多分支。
> 
> 所以，这或许有点刻意，但它确实是一个很有用的工具。
> 
> 我们下次见！
> 
> ---
> 
> ## 脚注
> 
> [^1]: 这个 PR 登陆的时间比 `dak2` 的要晚得多，因为我想等待 [SSA 最小化趟](https://github.com/ruby/ruby/pull/17311)合并——以后再详细讨论——以便全局规范化能够发挥更大作用。否则，由于我们采用的是极大 SSA 形式，我们实际上无法在不同基本块之间复用 SSA 值。[↩](#fnref:much-later)
> [^2]: 允许出现一个基本块 `A` 对另一个基本块 `B` 同时进行 `iftrue` 情况和 `iffalse` 情况的条件分支。例如，如果它沿每条边的基本块参数传递不同的数据，这就很有用。出于这个原因，我们检查的是传入边的数量，而不是前驱基本块的数量。[↩](#fnref:block-vs-edge)