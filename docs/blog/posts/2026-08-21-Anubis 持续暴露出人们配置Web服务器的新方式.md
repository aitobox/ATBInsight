---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-21
hide:
- navigation
tags:
- CSP
- WebWorkers
- Anubis
- 安全配置
- JavaScript
title: Anubis 持续暴露出人们配置Web服务器的新方式
---
### 文章背景与核心概要
构建可靠的 Web 应用程序意味着必须应对浏览器固有不可靠性的挑战，特别是当现代 API（如 WebUSB 和内置 AI）不断扩大攻击面时。本文探讨了如何使用内容安全策略（CSP）来限制浏览器的功能，处理 `blob:` URI Worker 错误的微妙怪癖，以及 **Anubis** 安全系统如何在应对严格的 Web 服务器配置的同时，优化并行工作量证明（Proof-of-Work）检查。

通过将 Worker 源码封装进 `blob:` URI 中，Anubis 成功解决了并行请求引发的服务器负载暴增问题，并为那些在浏览器策略和服务器性能之间寻找平衡的开发者提供了宝贵的实践经验。

---

## 理解内容安全策略 (CSPs)

> One of the most annoying parts of writing web applications is that, in general, you can't trust browsers. However, you have to trust them at *some* level because that is how users interact with your software. As browsers gain more capable APIs (such as [WebUSB](https://developer.mozilla.org/en-US/docs/Web/API/WebUSB_API), [Built-in AI](https://developer.chrome.com/docs/ai/built-in), or other complex features), administrators want the ability to turn off features their web applications do not use. This is the exact reason [Content-Security-Policies (CSPs)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) exist.

编写 Web 应用程序最令人头疼的事情之一，就是通常情况下你无法信任浏览器。然而，你必须在某种程度上信任它们，因为这是用户与你的软件交互的方式。随着浏览器获得越来越强大的 API（例如 [WebUSB](https://developer.mozilla.org/en-US/docs/Web/API/WebUSB_API)、[内置 AI](https://developer.chrome.com/docs/ai/built-in) 或其他复杂功能），管理员希望能够关闭其 Web 应用不需要的功能。这正是[内容安全策略 (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) 存在的根本原因。

> <img alt="Mara is hacker" width="64" height="64" src="./images/5c1784965481.png" loading="lazy"/> [Mara](https://xeiaso.net/characters#mara)

> <img alt="Mara is hacker" width="64" height="64" src="./images/5c1784965481.png" loading="lazy"/> [Mara](https://xeiaso.net/characters#mara)

> Normally we avoid acronyms when writing posts like this, but for the purpose of this article, when you see "CSP", think "Content-Security-Policy".

通常我们在写这样的文章时会避免使用缩写，但在本文中，当你看到“CSP”时，请将其理解为“Content-Security-Policy（内容安全策略）”。

> In general, a CSP disables all browser features by default and then selectively enables the ones the website actually needs. For example (stolen from [the Anubis docs](https://anubis.techaro.lol/docs/admin/configuration/content-security-policy)):

总的来说，CSP 默认会禁用所有浏览器功能，然后有选择地启用网站实际需要的功能。例如（摘自 [Anubis 文档](https://anubis.techaro.lol/docs/admin/configuration/content-security-policy)）：

```http
default-src 'none';
script-src  'self' 'unsafe-inline';
style-src   'self' 'unsafe-inline';
img-src     'self';
font-src    'self' data:;
connect-src 'self';
worker-src  'self' blob:;
base-uri    'none';
form-action 'self';
```

> This policy effectively disables all browser features except for:
* Loading scripts from the same [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin)
* Inline JavaScript in `<script>` tags and inline CSS
* Loading CSS, images, and fonts from the same origin
* Loading fonts inline into CSS files via [`data:` URIs](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data)
* Making `fetch()` requests to the same origin
* Loading [Worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) scripts from the same origin or [`blob:` URIs](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/blob)
* Disallowing the use of the [`<base>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base)
* Restricting HTML `<form>` actions exclusively to the same origin

该策略实际上禁用了所有浏览器功能，除了以下几项：
* 从同一[源（origin）](https://developer.mozilla.org/en-US/docs/Glossary/Origin)加载脚本
* `<script>` 标签中的内联 JavaScript 和内联 CSS
* 从同源加载 CSS、图片和字体
* 通过 [`data:` URI](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data) 将字体内联加载到 CSS 文件中
* 向同源发起 `fetch()` 请求
* 从同源或 [`blob:` URI](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/blob) 加载 [Worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) 脚本
* 禁止使用 [`<base>` 元素](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base)
* 严格限制 HTML `<form>` 操作仅限于同源

---

## Blob URI 和 Worker 的怪癖

## The Quirks of Blob URIs and Workers

> A fascinating quirk arises when you enforce a CSP that forbids loading Worker scripts from `blob:` URIs: you don't receive an error *until* after the Worker is constructed and the browser forks a background thread:

当你实施一项禁止从 `blob:` URI 加载 Worker 脚本的 CSP 时，会出现一个有趣的怪癖：在 Worker 构建完成且浏览器分叉出一个后台线程**之前**，你不会收到任何错误：

```javascript
blobURL = URL.createObjectURL(
  new Blob([`console.log("Hello, world!");`], { type: "text/javascript" }),
);
const w = new Worker(blobURL);
// does not throw an error synchronously
// 不会同步抛出错误
```

> Instead, you have to catch it asynchronously via the `.onerror` callback:

相反，你必须通过 `.onerror` 回调异步捕获它：

```javascript
w.onerror = (event) => {
  console.error(`Got an error: ${event}`);
};
```

> If you (like me) [implemented fallback logic that depends on this behavior](https://github.com/TecharoHQ/anubis/pull/1766), you have to adapt your architecture to account for it.

如果你（像我一样）[实现了依赖于此行为的回退逻辑](https://github.com/TecharoHQ/anubis/pull/1766)，你就必须调整架构来适应它。

---

## 使用 Anubis 减轻服务器负载

## Mitigating Server Load with Anubis

> Let's face it: users do not like seeing an Anubis challenge page. I've tried to make them appear less often, but this doesn't scale as scrapers continuously adapt to changes. One way Anubis mitigates the friction of a challenge page is by making it *go away* as fast as possible, executing its proof-of-work checks in parallel. This leverages modern multi-core CPU architectures rather than relying on single-core performance.

面对现实吧：用户不喜欢看到 Anubis 的挑战页面。我曾试图让它们少出现一些，但随着爬虫不断适应变化，这种方法无法线性扩展。Anubis 减轻挑战页面摩擦的一种方法是让它尽可能快地**消失**，即并行执行其工作量证明检查。这利用了现代多核 CPU 架构，而不是依赖单核性能。

> By default, when you create a Worker pointing to a JavaScript program on your web server, browsers make a request to load that program:

默认情况下，当你创建一个指向 Web 服务器上 JavaScript 程序的 Worker 时，浏览器会发起请求来加载该程序：

```javascript
const w = new Worker("/static/js/worker/test1.mjs");
```

> This results in a `GET /static/js/worker/test1.mjs` request to the server to fetch the JavaScript source code. The browser then executes that code in parallel and initializes the [worker environment](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API).

这会导致向服务器发送一个 `GET /static/js/worker/test1.mjs` 请求以获取 JavaScript 源码。随后，浏览器会并行执行该代码并初始化 [worker 环境](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API)。

### 并行请求问题

### The Parallel Request Problem

> Spawning multiple workers in parallel—as Anubis does—introduces a scaling bottleneck:

像 Anubis 那样并行派生多个 worker 会引入一个扩展瓶颈：

```javascript
const getHardwareConcurrency = () =>
  navigator.hardwareConcurrency !== undefined
    ? navigator.hardwareConcurrency
    : 1;

let workers: Worker[] = [];
const threads = Math.trunc(Math.max(getHardwareConcurrency() / 2, 1));

for (let i = 0; i < threads; i++) {
  let w: Worker;
  try {
    w = new Worker("/whatever/worker.mjs");
  } catch (err) {
    magic!(cleanup);
    magic!(throwError);
    return;
  }

  workers.push(w);

  // Draw the rest of the owl
  // 画出猫头鹰的剩下部分
}
```

> This approach triggers `threads` number of HTTP requests simultaneously. When the server is already overloaded—such as when scrapers [attack in droves from nearly every ISO country code on the planet](https://xeiaso.net/notes/2026/check-your-smart-tv/)—a single legitimate user could inadvertently force up to 16 extra HTTP requests onto the server. Furthermore, applying [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) here isn't straightforward without adding complex wrapper logic around the Worker constructor.

这种方法会同时触发 `threads` 数量的 HTTP 请求。当服务器本已超载时——例如当爬虫[从地球上几乎所有 ISO 国家代码处成群结队地发起攻击](https://xeiaso.net/notes/2026/check-your-smart-tv/)时——单个合法用户可能会无意中向服务器强加多达 16 个额外的 HTTP 请求。此外，如果在 Worker 构造函数周围不添加复杂的包装逻辑，在这里应用[指数退避（exponential backoff）](https://en.wikipedia.org/wiki/Exponential_backoff)并不是一件简单的事。

### Blob URI 解决方案

### The Blob URI Solution

> To work around this, Anubis loads the worker source *once* via a standard `fetch()` request and packs it into a `blob:` URI. This prevents clients from bombarding the server with duplicate parallel requests.

为了解决这个问题，Anubis 通过标准的 `fetch()` 请求**只加载一次** worker 源码，并将其打包到 `blob:` URI 中。这防止了客户端用重复的并行请求轰炸服务器。

> The legacy fallback logic (fanning out direct requests) is retained just in case administrators enforce a CSP that forbids `blob:` URIs. While maintaining this fallback adds testing overhead, ensuring client reliability remains essential, even if it risks placing extra request pressure on an already strained server.

为了防止管理员强制实施禁止 `blob:` URI 的 CSP，传统的后备逻辑（分发直接请求）得以保留。虽然维护这种后备逻辑增加了测试开销，但确保客户端的可靠性仍然至关重要，即使这可能会给本已紧张的服务器带来额外的请求压力。

> <img alt="Cadey is coffee" width="64" height="64" src="./images/2c7b46067805.png" loading="lazy"/> [Cadey](https://xeiaso.net/characters#cadey)

> <img alt="Cadey is coffee" width="64" height="64" src="./images/2c7b46067805.png" loading="lazy"/> [Cadey](https://xeiaso.net/characters#cadey)

> As a side note, this optimization only works because Anubis assumes its worker code is fundamentally correct unless something *completely unrecoverable* happens. Most of the proof-of-work code is "just math"; if the math fails, the user's CPU or RAM is likely failing anyway, and the server would reject the result regardless.

顺便提一句，这种优化之所以可行，是因为 Anubis 假定其 worker 代码在根本上是正确的，除非发生*完全不可恢复*的故障。大部分工作量证明代码都“只是数学”；如果数学计算失败，用户的 CPU 或 RAM 很可能已经出问题了，无论如何服务器都会拒绝该结果。

> Ideally, you would want the entire challenge session to abort if any worker thread encounters an error. In practice, however, it is "fine-ish" to lose a worker or two as long as at least one remains active. 

理想情况下，如果任何 worker 线程遇到错误，你都会希望整个挑战会话中止。然而在实践中，只要至少还有一个处于活动状态，损失一两个 worker 也是“勉强可以接受的”。

> You can think of the proof-of-work solver as dividing the nonce space into separate "lanes" assigned to individual worker threads. Solutions are generally dense enough that losing a thread is acceptable—at the cost of skipping potential solutions within that specific lane. Future improvements may include attempting to relaunch failed workers where they left off, but that remains out of scope for now.

你可以将工作量证明求解器想象成将随机数（nonce）空间划分为分配给各个 worker 线程的独立“车道”。解决方案通常足够密集，因此损失一个线程是可以接受的——代价是跳过了该特定车道内的潜在解决方案。未来的改进可能包括尝试在失败的 worker 离开的地方重新启动它们，但这目前超出了本文的讨论范围。

> Navigating edge cases like these is simply part of working on Anubis—and explains why I often end up [writing essays in PR commit messages](https://github.com/TecharoHQ/anubis/pull/1874). The joys of modern software engineering truly know no bounds.

处理诸如此类的边缘情况只是开发 Anubis 的一部分——这也解释了为什么我经常在 [PR 提交信息中写长篇大论](https://github.com/TecharoHQ/anubis/pull/1874)。现代软件工程的乐趣当真是无边无际。