Here is the polished content, formatted in elegant Markdown with a summary and proper headings.

***

# Regarding Ad Blockers and Daring Fireball

## Summary
In this post, John Gruber discusses an unexpected issue where RSS readers and content blockers (such as NetNewsWire and the Safari extension Banish) inadvertently break sentences by entirely deleting text linked to domains flagged as ad networks (like `ads.apple.com` or the App Store). Rather than resorting to workaround URLs like Bitly, Gruber advocates against overzealous pattern-matching in software. He concludes with a personal appeal regarding Daring Fireball’s unobtrusive, privacy-friendly ads, asking readers and ad-blocker developers to consider allowlisting the site.

***

## The Hidden Danger of Overzealous Ad Blockers

Following up on a previous discussion regarding [content blockers and ad-blocking](https://daringfireball.net/linked/2026/07/24/coiner-of-enshittification-endorses-dickover), I ran into a weird situation a few weeks ago with my column, “[John Ternus Should Reverse Apple’s Slide Down the Advertising Slippery Slope](https://daringfireball.net/2026/07/ternus_apple_slippery_slope).” 

That article contained this sentence in Markdown:

```markdown
And -- at this writing, still "coming soon" -- Apple is
launching [ads on Apple Maps][🗺️].

[🗺️]: https://ads.apple.com/maps
```

The problem? Anyone reading that article in NetNewsWire saw it rendered with the words “ads on Apple Maps” entirely omitted:<sup>[1](#fn1)</sup>

[![Screenshot of article text from NetNewsWire](./images/0b52c9c8c938.png)](./images/0b52c9c8c938.png)

It looked like I simply forgot to finish writing the sentence. 

After a few readers reported this, I suspected the domain `ads.apple.com` was to blame. I’d never linked to it before, and many ad blockers automatically target domains starting with `ads.*`. 

That turned out to be precisely the case. While I didn't know NetNewsWire filtered content natively (and arguably, it shouldn't), DF reader Antonio Germano dug into the open-source code and found the culprit in [the `core.css` file](https://github.com/Ranchero-Software/NetNewsWire/blob/main/Shared/Article%20Rendering/core.css), line 49:

```css
38  /*Block ads and junk*/
39  
40  iframe[src*="feedads" ],
41  iframe[src*="doubleclick"],
42  iframe[src*="plusone.google"] {
43      display: none !important;
44  }
45  
46  a[href*=".ads."],
47  a[href*="feedads" ],
48  a[href*="doubleclick"],
49  a[href*="//ads."],
```

## The Dilemma of Workarounds

Once the culprit was identified, I pinged my friend [Brent Simmons](https://inessential.com/) to report the problem. But that left me with a decision to make. 

NetNewsWire is arguably the most popular feed reader—it’s the one I use personally. Since I can't alter NetNewsWire’s `core.css`, I couldn't stop it from stripping out words linking to `ads.apple.com`. I *could* have changed my link to a short-and-redirect URL like a [Bitly link](https://bit.ly/4wmXFSE) pointing back to Apple, but I chose not to. 

I dislike playing whack-a-mole to work around bugs in other software. I also dislike forcing readers to click mystery URLs instead of direct links—it destroys transparency and ruins links meant to last for decades.

What bothers me most is *how* NetNewsWire handles this blocking: it **omits the hyperlinked words entirely** rather than keeping the text and merely disabling the link. 

I’ve run into this elsewhere. For instance, the Safari extension Banish—[which I recommended back in 2022](https://daringfireball.net/linked/2022/08/02/banish)—started blocking links to Apple’s App Store domain a year or two ago by deleting the linked words. If you have Banish installed and read my post recommending it, you literally miss the headline and cannot follow the link.<sup>[2](#fn2)</sup>

So, what’s the solution? Stop linking to the App Store? Create custom redirects for every Apple link? That’s unreasonable work that introduces unnecessary friction. Instead, I just ignore it. But it means an untold number of readers miss words in my articles simply because of an overzealous pattern-matching rule. 

Ultimately, when you install a content blocker, you take responsibility for its overzealousness.

---

## A Personal Request Regarding Daring Fireball's Ads

Let me use this opportunity to make a small personal request. 

The display ads on Daring Fireball are unobtrusive, limited to one per page, and entirely private. There are no cookies or JavaScript attempting to track you, and the ads are served directly from the `daringfireball.net` domain. I turn down advertisers who request to serve images or "tracking pixels" from *their* domains. I don’t display mid-article banner ads between paragraphs—a practice I find disrespectful to both writer and reader. My goal is for DF's ads to match the quality of high-end print magazines like *The New Yorker*.

I hope they are ads readers don’t *want* to block. Most content blockers I've tested do not block ads on Daring Fireball by default, or make it easy to adjust per-domain settings. In my [previous post](https://daringfireball.net/linked/2026/07/24/coiner-of-enshittification-endorses-dickover), I recommended [uBlock Origin Lite](https://apps.apple.com/us/app/ublock-origin-lite/id6745342698) (free, slightly complex) and [Magic Lasso](https://www.magiclasso.co/) (paid, much simpler). Magic Lasso leaves DF ads unblocked by default; uBlock Origin is trivial to adjust.

If your ad blocker currently blocks DF, I humbly ask you to take a moment to allowlist the site. *(If you use a blocker that strips ads entirely by default, please [shoot me a quick email](https://daringfireball.net/contact/) telling me which one—I'm curious.)* And if you are an ad-blocker developer, please consider allowlisting Daring Fireball **by default**.

Of course, if you genuinely want to block DF's ads, go right ahead. It’s your browser and your call—no hard feelings, and I don't run aggressive scripts to nag you about it.

---

## Footnotes

<ol>
<li id="fn1">
I omitted the Markdown creating a link on the words “still ‘coming soon’” for clarity, to emphasize only the problematic link in my original prose. (Also, it’s fun to use emoji as named link definitions, like in this example.) <a href="#fnr1-2026-07-24" title="Jump back to footnote 1 in the text.">↩︎</a>
</li>

<li id="fn2">
I reported this to the developer of Banish twice, but never received a response. Consequently, I’ve banished Banish from my own devices, and I am officially un-recommending it. <a href="#fnr2-2026-07-24" title="Jump back to footnote 2 in the text.">↩︎</a>
</li>
</ol>