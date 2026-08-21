---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-22
hide:
- navigation
tags:
- iOS开发
- Bluesky
- 隐私保护
- 逆向技术
- 增长黑客
title: Bluesky 和 Threads 是如何在 iOS 截图里偷偷塞入自家 Logo 的
---
### 文章背景与核心概要

你是否曾在截屏 Bluesky 或其他社交软件的帖子时，发现原本显示“关注”按钮的角落里，莫名其妙地多出了一个应用的 Logo？本文探讨了这种奇特行为背后的巧妙技术。通过利用原本为密码输入框设计的 iOS 系统级安全特性，开发者可以在用户截图时动态替换界面元素。这是一种兼具巧思、同时又带有一点争议的“增长黑客”技巧，此前 Telegram 和 Signal 等应用也曾使用过类似的方法。

---

## 神秘的 Logo

> # How Bluesky and Threads Sneak Their Logos Into iOS Screenshots
> 
> *Published by [mt](https://timmarinin.net) on Sunday, 16 August 2026*
> 
> ## Summary
> Have you ever taken a screenshot of a Bluesky post and noticed a subtle app logo magically appearing in the corner where the "Follow" button normally sits? This article explores the clever technical trick behind this behavior. By leveraging iOS security features meant for password fields, developers can swap interface elements specifically for screenshots—a clever, if somewhat controversial, growth-hacking technique also utilized by apps like Telegram and Signal.

有时候，我会在截取自己喜欢的帖子时顺手拍个照，要么是发给朋友或表情包频道，要么是留下一份“持久”的备份。就像下面这样（我把界面其余部分裁掉了）：

> ## The Mysterious Logo
> 
> Sometimes I take a screenshot of a post I like, either to send it to friends/meme channel or to save a “durable” copy. Like this one (I’ve cropped out the rest of the interface):

<figure>
<img alt="A screenshot of Bluesky post by @eroston.bsky.social, the important part is that Bluesky logo is visible in the top right corner" src="./skeet.jpg" width="50%"/>
<figcaption><a href="https://bsky.app/profile/eroston.bsky.social/post/3mt5gs2fdyk2l">Original</a>, if you want to reskeet it</figcaption>
</figure>

> <figure>
> <img alt="A screenshot of Bluesky post by @eroston.bsky.social, the important part is that Bluesky logo is visible in the top right corner" src="./skeet.jpg" width="50%"/>
> <figcaption><a href="https://bsky.app/profile/eroston.bsky.social/post/3mt5gs2fdyk2l">Original</a>, if you want to reskeet it</figcaption>
> </figure>

我注意到右下角有一个 Bluesky 的 Logo，心里觉得挺纳闷：为什么我平时用 App 时完全没注意到这个 Logo 呢？于是我再次打开 App 查看那篇帖子——Logo 根本不在那儿，取而代之的是“关注（Follow）”按钮。

> I noticed the Bluesky logo in the right corner and thought that it was weird that the logo doesn’t bother me when I use the app. Then I looked at the post in the app again—logo wasn’t there, replaced by the “Follow” button.

我记得有些 App 会把它们的 Logo 藏在 iPhone 的“灵动岛”或刘海屏附近，这样平时不会突兀，除非你截图。但这里的 Logo 可是大喇喇地摆在显眼位置，他们究竟是怎么做到的？

> I remembered that a few apps hide their logo where the iPhone notch is, so that it doesn’t stick out, unless you take a screenshot. But here the logo is placed in the open, so how do they do it?

我试着再截一次屏，这次我选在切换到另一个 App 的半途中：

> I tried to take another screenshot, this time mid-switching to the other app:

<figure>
<img alt="Screenshot of zoomed out version of Bluesky app mid-switching, Follow button is visible" src="./mid-switch.png" width="50%"/>
<figcaption><a href="https://bsky.app/profile/eroston.bsky.social/post/3mt5gs2fdyk2l">The “Follow” button is visible when I take the screenshot mid-switch.</a></figcaption>
</figure>

> <figure>
> <img alt="Screenshot of zoomed out version of Bluesky app mid-switching, Follow button is visible" src="./mid-switch.png" width="50%"/>
> <figcaption>The “Follow” button is visible when I take the screenshot mid-switch.</figcaption>
> </figure>

难道他们监听了我按下截图组合键的动作，然后在最后一刻来了个“狸猫换太子”？我不是 iOS 开发者，所以不太清楚那边到底支持哪些骚操作。

> Did they somehow set up a listener for two buttons I’m pressing to take a screenshot and do a switcheroo at the last moment? I’m not an iOS developer, so I’m not sure what’s possible and what is not over there.

此时此刻，我的好奇心被彻底勾起来了。好在我记起来 Bluesky 是个开源应用（至少代码是公开可查的）。

> At this point I was mildly intrigued. Thankfully, I remembered that Bluesky app is open source (or at least the code is available to look at).

## 秘密机制

> ## The Secret Mechanism

答案就藏在一个非常直白的文件中：[GrowthHack.tsx](https://github.com/bluesky-social/social-app/blob/main/src/screens/PostThread/components/GrowthHack.tsx)，它是由 [mozzius](https://github.com/mozzius) 在 2026 年 1 月引入的。不过，该文件仅仅是调用了一个依赖库，为了弄清原理，我又去查看了同样由其开发的 [expo-privacy-sensitive](https://github.com/mozzius/expo-privacy-sensitive) 软件包。

> The answer was in the file literally called [GrowthHack.tsx](https://github.com/bluesky-social/social-app/blob/main/src/screens/PostThread/components/GrowthHack.tsx), introduced in January 2026 by [mozzius](https://github.com/mozzius). But it merely used a dependency, so to understand I looked into package [expo-privacy-sensitive](https://github.com/mozzius/expo-privacy-sensitive), also by them.

该软件包会创建一个 `UITextField`，并将 `isSecureTextEntry`（安全文本输入）属性设为 true，然后将实际内容（即那个按钮）渲染到该字段的 `.layer` 中。当我进行截屏时，iOS 会通过将该图层置空来隐去这个 `UITextField`，从而让藏在底下的 Bluesky Logo 显露出来（其实它一直都在那儿）。对于其他平台，它只是按原样渲染内容，而不会进行这种图层遮罩处理。

> The package creates `UITextField` with `isSecureTextEntry` property set to true and renders the actual content (the button) into that field’s `.layer`. When I take the screenshot, iOS hides this UITextField by blanking the layer, allowing the Bluesky logo to flutter its wings through (it was here the whooole time). For other platforms it simply renders content as-is, without masking.

为什么在切换应用的过程中截图不生效呢？我猜是因为 iOS 在手势刚开始时就自己截好了快照（此时并没有触发图层清空），而当我真正完成截图时，并没有一个活生生的 `UITextField` 实例去响应它，只有那个静态的快照。当然了，我还是得强调——我不是 iOS 开发者。

> Why doesn’t it work when I switch between the apps? I suppose that iOS takes a snapshot itself at the start of the gesture (without triggering blanking), and when I do a screenshot, there is no live UITextField instance to react to that, only the inert snapshot. But once again, I’m not an iOS developer.

## 行业先例与结论

> ## Industry Precedent and Conclusion

这是一个绝妙的技巧，还是对原本用于隐私保护的 API 的一种滥用？在[添加该行为的讨论串](https://github.com/bluesky-social/social-app/pull/9637)被锁定之前，大家基本上对它持反感态度。不过我觉得挺有意思的。

> Nifty trick or an abuse of API meant for privacy? The people in [the thread adding the behavior](https://github.com/bluesky-social/social-app/pull/9637) mostly didn’t like it, before the thread got locked. I think it’s cute.

我在谷歌上搜了一下，发现这个小把戏其实已经广为人知。Telegram 在其“私密聊天”功能中就实现了[类似机制](https://github.com/TelegramMessenger/Telegram-iOS/blob/master/submodules/UIKitRuntimeUtils/Source/UIKitRuntimeUtils/UIKitUtils.m#L299-L328)，[Signal](https://github.com/signalapp/Signal-iOS/blob/a9f55ea599561e6d3bcee87d4f1540a7191b28dc/Signal/util/ScreenshotBlocking.swift) 也是如此。因此，我估计苹果短期内并不会把这个“漏洞”给补上。

> I googled a bit, and the trick is well-known. Telegram implemented [similar thing for its "secret" chats](https://github.com/TelegramMessenger/Telegram-iOS/blob/master/submodules/UIKitRuntimeUtils/Source/UIKitRuntimeUtils/UIKitUtils.m#L299-L328), as did [Signal](https://github.com/signalapp/Signal-iOS/blob/a9f55ea599561e6d3bcee87d4f1540a7191b28dc/Signal/util/ScreenshotBlocking.swift), so I don’t expect it to be patched by Apple any time soon.