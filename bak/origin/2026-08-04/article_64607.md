# Boris Cherny on Trying to Get Claude Code to Rewrite the Claude App

## 📌 Summary
In a recent interview at Y Combinator’s Startup School 2026, Anthropic's Boris Cherny discussed how he tasked Claude Code with rewriting the Claude desktop app from Electron into native Swift. However, commentators argue that this pixel-by-pixel port misses the bigger picture: the core issue isn't the technology stack (Electron vs. native), but rather the flawed, non-native design of the app itself. Furthermore, claims of the app's current performance and reliability are heavily disputed.

---

## 🎙️ The Interview: Pushing Claude to Its Limits

At Y Combinator’s Startup School 2026, Diana Hu interviewed Boris Cherny, head of Claude Code at Anthropic. [Around the 20:30 mark in the video](https://youtu.be/qyPCVqFUyDo?t=1230), Cherny discussed the evolving nature of AI interaction:

> **Cherny:** I think the skill nowadays is less about prompt engineering and more about figuring out how do you give Claude a hard task that seems a little bit too hard. Then how do you make it possible for Claude to verify its work along the way? The verification is probably the single most important thing that people do not get right, largely.
> 
> One example of this is people were — we have this desktop app for Claude and it’s built using Electron. We’ve made it quite fast. Now it’s a pretty awesome experience. Six months ago it was sluggish and it wasn’t very reliable. Now it’s pretty awesome. It’s the thing that most of the team uses. As an experiment, I wanted to see what it would feel like if it was native. So what I did is I started a Claude Tag session. Claude Tag is a new product we have. It’s just Claude running in Slack. 
> 
> My first question was, “Hey Tag, do you have access to a Mac OS runner on GitHub?” It said no. Then I hooked up a runner. So it was able to start a Mac virtual machine using GitHub. My second question was, I created this empty code base that was a Claude desktop app rewritten in Swift.
> 
> I asked, “Can you access this code base?” It said no. Then I gave it access and it was like, “Okay, great. Now I have access.” Then I said, “Okay, now what I want you to do is I want you to rewrite the Electron app in Swift. I want you to run the Electron app in the Mac virtual machine, screenshot it, and then look pixel by pixel. Compare it to the Swift version. Don’t stop until you’re done.”
> 
> **Hu:** And that was your prompt basically?
> 
> **Cherny:** That was my prompt.
> 
> **Hu:** And how long did this take to run?
> 
> **Cherny:** It’s still running.
> 
> **Hu:** When did you start it?
> 
> **Cherny:** It’s been a little over two weeks. So it’s like 14 days, 15 days.

---

## 🔍 Critique: Better Ingredients, Same Recipe

While this experiment makes for a fascinating headline, it largely misses the mark regarding what makes a great user experience. 

The primary issue with the Claude Mac client isn't merely the technical overhead of using a bloated, non-native framework like Electron. The actual problem is **poor design**. The app’s interface is fundamentally non-native. It ignores standard Mac UI idioms and suffers from [subpar abstract design](https://daringfireball.net/linked/2026/07/17/openais-product-shake-up)—feeling clunky on the web, on Windows, and consequently on the Mac.

Directing Claude Code to recreate the current Electron app in Swift, *pixel-by-pixel*, only addresses technical debt, not design flaws. A well-designed Electron app is infinitely preferable to a poorly designed native AppKit or SwiftUI app. To use an analogy: the current Claude app is a terrible recipe made with subpar ingredients. Asking Claude to follow that exact same terrible recipe using premium native ingredients still results in something unappealing.

Moreover, it is hardly surprising that an automated, multi-week migration struggle ensued. Forcing native frameworks like AppKit and SwiftUI—which are meticulously crafted to build native Mac applications—to replicate an entirely un-Mac-like UI is like swimming upstream. 

---

## ⚠️ A Question of Performance

Finally, Cherny’s assertion that the current Claude Mac app has evolved from sluggish and unreliable into something "pretty awesome" is difficult to accept at face value. 

Launching the app often involves a frustrating wait—complete with a spinning beach ball cursor—before it finally becomes usable, sometimes greeting the user with [unexpected UI quirks](https://daringfireball.net/misc/2026/08/claude-dickover.png). It may well be an improvement over its state six months ago, but calling it "pretty awesome" is a stretch.

***

*[Permanent link to original commentary via Daring Fireball](https://daringfireball.net/linked/2026/08/02/cherny-claude-swift)*