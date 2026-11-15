---
authors:
  - aitoboxrobot
categories:
  - 产品发布
date: 2026-11-16
hide:
  - navigation
tags:
  - Clojure
  - 生成式测试
  - 属性测试
  - 软件质量
title: "Hegel-clj 发布：面向 Clojure 的下一代生成式测试库"
---

# Hegel-clj 发布：面向 Clojure 的下一代生成式测试库

> # Announcing Hegel-clj

### 文章背景与核心概要

在现代软件工程中，生成式测试 (Generative Testing) 能够自动产生海量随机输入，是挖掘系统隐蔽漏洞的利器。然而，Clojure 社区长期依赖的主力库 `test.check` 基于“缩减树 (Shrink Trees) ”机制，在面对由 `bind` 组合的复杂生成器时，缩减算法经常陷入僵局，留下充斥着无用零值的庞大失败样例，给排查问题带来极大困扰。Python 生态著名的 Hypothesis 库开创了“内部测试用例缩减 (Internal Test-Case Reduction) ”范式，通过在测试失败时让生成器重新生成更小、更相似的输入，彻底解决了该难题。著名分布式系统专家 aphyr 结合这一最新理念，将新一代跨平台测试引擎 Hegel 引入 Clojure 生态并发布了 Hegel-clj，为开发者带来了兼具确定性随机数、极致缩减与原生 `clojure.test` 协同的现代化生成式测试体验。

---

我刚刚发布了 [hegel-clj](https://github.com/aphyr/hegel-clj)，这是面向 [Hegel](https://hegel.dev) 生成式测试 (Generative Testing) 库的 Clojure 接口。你可以直接跳到 [官方文档](https://cljdoc.org/d/com.aphyr/hegel-clj/0.1.1/doc/readme) 阅读上手指南，不过我想聊聊为什么我们还需要一个新的测试库，这背后的技术思考或许会更有趣。

> I’ve just released [hegel-clj](https://github.com/aphyr/hegel-clj), a Clojure interface for the [Hegel](https://hegel.dev) generative testing library. You can jump right to [the docs](https://cljdoc.org/d/com.aphyr/hegel-clj/0.1.1/doc/readme), but I thought it might be interesting to explain why I want another testing library.

---

## 内容概要

> ## Summary

* **`test.check` 的固有缺陷**：像 `test.check` 这样复杂的生成式测试库依赖缩减树 (Shrink Trees) 。当使用通过 `bind` 组合的生成器时，测试用例的缩减过程经常会卡死，导致吐出庞大得有些滑稽的失败样例 (例如：一个仅仅因为缩减算法无法有效缩减绑定参数，而充斥着大量无用零值的超长向量) 。
* **Hypothesis 开创的全新思路**：[Hypothesis](https://hypothesis.works/) 开创了“内部测试用例缩减 (Internal Test-Case Reduction) ”技术。生成器先产生单一值，并在测试失败时重新运行生成器，寻找更小但相似的变体。这一机制正是 **Hegel** 的基石。
* **全新亮相的 Hegel-clj**：为 Hegel 打造的简洁、跨平台 Clojure 包装层，提供了极其稳健的用例缩减能力、可预测的生成器组合机制、强大的宏 (`let`、`composite`) ，以及与 `clojure.test` 的无缝集成。

> * **The Problem with `test.check`:** Complex generative testing libraries like `test.check` rely on shrink trees. When using generators combined via `bind`, shrinking can frequently get stuck, yielding comically oversized failure cases (e.g., a massive vector padded with zeroes simply because the shrinking algorithm couldn't efficiently reduce the bound parameters).
> * **The Hypothesis Approach:** [Hypothesis](https://hypothesis.works/) pioneered *internal test-case-reduction*, where generators produce a single value and re-run to find smaller variations if a test fails. This is the foundation of **Hegel**.
> * **Introducing Hegel-clj:** A clean, cross-platform Clojure wrapper for Hegel that provides robust shrinking, predictable composition, powerful macros (`let`, `composite`), and a smooth `clojure.test` integration.

---

## 为什么 `test.check` 会在缩减时陷入僵局

> ## Why `test.check` Gets Stuck

在 Clojure 开发中，我经常使用优秀的 [test.check](https://github.com/clojure/test.check) 库来进行生成式测试。然而，使用 `test.check` 的过程有时令人相当抓狂！尤其是那些复杂的生成器，在用例缩减 (Shrinking) 阶段很容易卡死，结果往往只能靠人工手动去一点点裁剪复杂的失败数据结构。

> I do a lot of generative testing in Clojure with the excellent [test.check](https://github.com/clojure/test.check). However, using `test.check` can be frustrating! In particular, complex generators can get stuck during shrinking, leaving me trying to prune down a complex data structure by hand. 

导致这种窘境的罪魁祸首通常是 `bind`。如果你还不熟悉 `test.check`、Quickcheck 或该家族中的其他测试库，简单来说，`bind` 是这样一种生成器：它首先抽取一个随机值，接着以该值为基础构建一个**全新的**生成器，再由后者去抽取另一个值。

> The culprit is usually `bind`. If you’re not familiar with `test.check`, Quickcheck, or other libraries in this family, `bind` is a generator which draws some random value, then uses that to construct a *new* generator, which in turn is used to draw some other value.

```clojure
(require '[clojure.test.check :as tc]
         '[clojure.test.check.generators :as tcg]
         '[clojure.test.check.properties :as tcp])

(tcg/bind ; Take a number from `nat`, a generator of small positive
          ; integers.
          tcg/nat
          ; Now with that number, construct a generator of vectors, each
          ; with that many elements.
          (fn [size]
            (tcg/vector tcg/large-integer size)))
```

我们也可以用 `test.check` 的 `let` 宏来编写相同的逻辑，它在底层会被展开为一系列相互嵌套的 `bind` 调用。

> We can also write this using `test.check`’s `let` macro, which expands to a series of nested `bind`s under the hood.

```clojure
(tcg/let [size tcg/nat]
  (tcg/vector tcg/large-integer size))
```

### 经典缩减陷阱

> ### The Canonical Shrinking Trap

这直接引出了 `test.check` 中糟糕缩减表现的 [典型范例](https://github.com/clojure/test.check/blob/master/doc/growth-and-shrinking.md#gotchas-1)。假设我们要找出一个包含 `42` 的向量：

> This leads to the [canonical example](https://github.com/clojure/test.check/blob/master/doc/growth-and-shrinking.md#gotchas-1) of poor shrinking in `test.check`. Let’s try to find a vector containing `42`:

```clojure
(-> (tc/quick-check 1000
      (tcp/for-all [xs (tcg/let [size tcg/nat]
                         (tcg/vector tcg/large-integer size))]
                   (not-any? #{42} xs))
      {:seed 1777986545686})
  :shrunk :smallest first)

[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 42 0]
```

虽然这个向量**确实**包含了 42，但它的体积实在是太庞大了。为什么里面会充斥着这么多无关紧要的零？按理说，既然 `test.check` 已经捕获到了这个向量，它本该毫不费力地将其缩减为最简形式 `[42]`，不是吗？

> That *does* contain 42, but this vector is *enormous*. Why are there all these zeroes? Once `test.check` found this vector, surely it could have shrunk it to just `[42]`, right?

问题的根源在于**缩减树 (Shrink Trees)**。实际上，`test.check` 生成器返回的并非单一数值 (例如 `64`) ，而是一棵惰性求值的候选值树：树的根节点可能是 `64`，其子节点可能是 `[32 48 ... 63]`，而这其中的每一个子节点又拥有各自的子节点 (例如 `32` 拥有子节点 `[16, 24, ... 31]`，以此类推) 。稍作简化，大整数生成器的候选树是这样 [定义的](https://github.com/clojure/test.check/blob/5ba3a25b60cf66ff531db8f44d89145abfacfa5c/src/main/clojure/clojure/test/check/generators.cljc#L228-L237)：

> The answer has to do with **shrink trees**. `test.check` generators don’t actually return values like `64`. Instead, they return a lazily evaluated tree of values: the root might be `64`, its children might be `[32 48 ... 63]`, and each of *those* children has further children (`32` has children `[16, 24, ... 31]`, and so on). Simplifying a bit, here’s how the tree for large integers [is defined](https://github.com/clojure/test.check/blob/5ba3a25b60cf66ff531db8f44d89145abfacfa5c/src/main/clojure/clojure/test/check/generators.cljc#L228-L237):

```clojure
(defn- shrink-long
  "Given a number x, returns a coll of (x-x, x-x/2, x-x/4, x-x/8, ..., x-1)"
  [^long x]
  (core/let [size (- 64 (Long/numberOfLeadingZeros (Math/abs x)))
             ^longs vals (long-array size)]
    (loop [i 0 n x]
      (if (zero? n)
        vals
        (do
          (aset vals i (- x n))
          (recur (inc i) (quot n 2))))))))
```

通过对候选树执行深度优先搜索并巧妙选择遍历分支，`test.check` 通常能够迅速将一个大整数缩减为依然能触发测试失败的较小整数。

> By performing a depth-first search of the tree and choosing branches cleverly, `test.check` can often quickly shrink an integer to a smaller one that still fails the test. 

然而，一旦引入了 `bind`，局面就变得极其棘手。`bind` 生成的缩减树有两种缩减方向：缩减外层值 (即长度 `size`) ，或者缩减内层值 (即向量元素) 。如果 `bind` 在缩减过程中尝试减小 `size`，它就会重新调用我们的生成器函数，从而生成**一套全新的随机元素**。由于数字 `42` 在广阔的数值空间中较为罕见，大多数长度都不会碰巧生成包含 `42` 的向量，这导致缩减尝试屡屡失败，最终使 `test.check` 陷入停滞，只能无可奈何地返回那个充斥着多余元素的超长向量。

> However, when `bind` is involved, things get messy. `bind`'s trees can shrink in two ways: by shrinking the outer value (the `size`) or the inner value (the vector). If `bind` picks a smaller size during shrinking, it calls our generator function again, generating *entirely new random elements*. Because `42` is an uncommon integer, most sizes won't produce a vector containing `42`, causing `test.check` to get stuck with an oversized vector.

而在 Python 生态中，[Hypothesis](https://hypothesis.works/) 团队采用了一种截然不同的思路，称为“内部测试用例缩减 (Internal Test-Case Reduction) ”：生成器在运行时只产出单一数值，如果该数值引发了测试断言失败，测试框架就会重新运行生成器，并 [引导它生成相似但规模更小的取值](https://drmaciver.github.io/papers/reduction-via-generation-preview.pdf)。这一优雅的范式正是 [Hegel](https://hegel.dev/) 的核心根基。

> Over in the Python world, the [Hypothesis](https://hypothesis.works/) team took a very different approach called *internal test-case-reduction*, where generators produce a single value, and if that value looks bad, they re-run the generator and [ask it to produce something similar, but smaller](https://drmaciver.github.io/papers/reduction-via-generation-preview.pdf). This approach is the foundation of [Hegel](https://hegel.dev/).

---

## 走近 Hegel-clj

> ## Hegel-clj

Hegel 是一款全新的跨平台生成式测试库。它提供了确定性生成器，能够从指令式、结构化的伪随机数生成器 (RNG) 中抽取随机值，同时配备了丰富的特殊值集合与精巧的用例缩减策略。

> Hegel is a new cross-platform library for generative testing. It provides deterministic generators which draw random values from an imperative, structured RNG, along with a rich family of special values and shrinking tactics. 

过去几个月里，我一直在打磨 [hegel-clj](https://github.com/aphyr/hegel-clj)，它为 Hegel 提供了地道的 Clojure 绑定。编写测试时，你只需调用 `hegel-clj/test!`，从生成器中抽取若干值，并在测试不符合预期时抛出异常即可：

> I’ve been working for a few months on [hegel-clj](https://github.com/aphyr/hegel-clj), which offers Clojure bindings for Hegel. To test something, you call `hegel-clj/test!`, draw some values from generators, and throw an exception if the test fails:

```clojure
(require '[hegel-clj [core :as h] [generator :as g]])
(h/test! {:seed 4}
  (assert (even? (h/draw! (g/integer)))))

{:passed? false
 :status :failed
 :statistics {:total 34
              :valid 5
              :invalid 0
              :overrun 18
              :interesting 11}
 :health-check-failed? false
 :failures ({:draws {"draw_1" 1}
             :exception
             #error {:cause "Assert failed: (even? (h/draw! (g/integer)))"
                     ...}})
 :reproduce-blob "AAEAAAAACgEAAAAB", :caveat nil}
```

Hegel 找到的最小失败用例仅包含一次抽取结果 `1`，这直接导致断言 `(even? 1)` 抛出了异常。

> The smallest case Hegel found involved a single draw of the number `1`, which caused the assertion `(even? 1)` to throw.

### 可组合的生成器

> ### Composable Generators

与 `test.check` 一样，Hegel 中的生成器也是纯粹且易于组合的数据结构。例如，生成一个布尔值向量：

> Generators are pure, composable structures, just like in `test.check`. Here’s a vector of booleans:

```clojure
(h/sample 5 (g/boolean))

[false false true true false]
```

或者生成一个表示人员信息的哈希映射表 (Map) ，其中的名字通过正则表达式生成，年龄则是一个整数：

> Or a map representing a person, with a name generated by a regular expression and an integer age:

```clojure
(h/sample 5 (g/hmap {:name (g/regex-str #"[A-Z][a-z]+")
                     :age  (g/integer 0 101)}))

[{:name "Aa", :age 0}
 {:name "Iyjdklppzxhqdnwmd", :age 89}
 {:name "Kslvqorm", :age 64}
 {:name "Fvyybe", :age 45}
 {:name "Puwppxqag", :age 4}]
```

Hegel 完备支持高阶组合子。你可以使用 `fmap` 对生成的值进行转换：

> Higher-order combinators are fully supported. You can transform generated values with `fmap`:

```clojure
(h/sample 5 (g/fmap keyword (g/string)))

[: :R :👍🏻 :True :çç¦ç¦򜝉ÏÏ򜝉¦¦Ï¦¦ç򜝉Ï¦ç򜝉çÏ򜝉çç¦]
```

或者利用 `bind` 基于一个生成器的输出来构造另一个生成器：

> Or build one generator out of another using `bind`:

```clojure
(h/sample 2 (g/bind (fn [size]
                      (g/tuple (g/vector size (g/integer))
                               (g/vector size (g/boolean))))
                    (g/integer 0 3)))

[[[] []]
 [[144229 531621 -364 -1569883 8194954 -913 16 -745]
 [false true false true]]]
```

### 借助 `let` 实现更出色的用例缩减

> ### Better Shrinking with `let`

与 `test.check` 截然不同，Hegel 的生成器在用例缩减方面表现极其卓越。面对之前的案例，Hegel 不会返回长达 39 个元素的冗余数组，而是能够精准揪出那个短小精悍的问题向量 `[42]`：

> Unlike `test.check`, Hegel's generators shrink exceptionally well. Instead of thirty-nine elements, Hegel can successfully find the much-shorter “bad” vector, `[42]`:

```clojure
(-> (h/test! {:test-cases 1000
              :seed       1777986545686}
      (h/let [size (g/integer {:min 0, :max 128})
              xs   (g/vector {:size size} (g/integer))]
        (assert (not-any? #{42} xs))))
    :failures first :draws (get "xs"))

[42]
```

### 高级特性

> ### Advanced Features

* **`composite` 宏**：轻松将任意代码提升为生成器，无需繁琐地手动嵌套哈希映射或元组：
> * **`composite` Macro:** Easily lift arbitrary code into a generator without struggling with nested maps or tuples:

```clojure
(h/sample 2
  (g/composite
    (h/let [name      (g/string)
            cat-count (g/integer 0 2)
            cats      (g/vector {:size cat-count, :unique? true} (g/string))]
      {:name name     
       :cats cats})))
```

* **递归生成器**：借助类似 Promise 风格的 `deferred` API 轻松构建递归生成器：
> * **Recursive Generators:** Build recursive generators using a promise-style API with `deferred`:

```clojure
(let [leaf (g/integer 0 9)
      tree (g/deferred)]
  (g/set-deferred! tree (g/one-of [leaf (g/vector tree)]))
  (mapv prn (h/sample 5 tree)))
```

* **与 `clojure.test` 无缝集成**：在常规单元测试旁边丝滑编写生成式测试：
> * **`clojure.test` Integration:** Seamlessly write generative tests alongside standard tests:

```clojure
(require '[clojure.test :refer :all] '[hegel-clj.clojure-test :refer [with]])

(defn bad-add
  "Adds two integers via floating-point"
  [x y]
  (long (+ (float x) (float y))))

(deftest bad-add-test
  (with {:test-cases 100}
        [x (g/integer)
         y (g/integer)]
    (h/fprn :x x, :y y)
    (is (= (+ x y) (bad-add x y)))))
```

---

## 致谢

> ## Acknowledgements

我已经使用 `test.check` 超过十年了，它一直是我在 Clojure 中最喜爱的工具之一。在此我想衷心感谢 Reid Draper、Gary Fredericks、Alex Miller 以及所有为该库做出贡献的开发者们。

> I’ve used `test.check` for over a decade now, and it’s one of my favorite things about Clojure. I want to thank Reid Draper, Gary Fredericks, Alex Miller, and everyone else who’s contributed to the library. 

我还要向来自 [Antithesis](https://antithesis.com/) 公司 Hegel 团队的 David MacIver、Liam DeVoe 和 Esau Rodriguez 致以诚挚谢意。他们抽出宝贵时间向我悉心讲解了 Hegel 的内部设计架构，耐心解答了我关于底层协议的无数疑问，并帮助修复了我们发现的一大批问题。大家真的太棒了。

> I’m also indebted to David MacIver, Liam DeVoe, and Esau Rodriguez from the Hegel team at [Antithesis](https://antithesis.com/). They took time to talk me through Hegel’s design, answered endless questions about the protocol, and helped fix a whole slew of issues that we found. Y’all rock.

我非常高兴地宣布 [hegel-clj 0.1.1](https://github.com/aphyr/hegel-clj) 正式发布，并已开始在自己的实际项目中全面使用它进行测试。衷心希望它也能对大家有所帮助。 ❤️

> I’m pleased to announce [hegel-clj 0.1.1](https://github.com/aphyr/hegel-clj), and I’m starting to use it to test my own projects. I hope it will be useful for you too. ❤️
