---
authors:
- aitoboxrobot
categories:
- 商业动态
date: 2026-08-21
hide:
- navigation
tags:
- Hacker News
- 人工智能
- 内容生成
- 数据分析
- LLM
title: Hacker News 上有多少内容是 AI 生成的？
---
### 文章背景与核心概要
本文探讨了作者对知名极客新闻聚合网站 Hacker News (HN) 的复杂情感：一方面将其视为重要的技术新闻来源和博客流量入口，另一方面又对其日益严苛的评论文化感到头疼。除了社区摩擦，作者更深入地调查了一个深刻的现象：AI 驱动的内容正在呈爆发式增长。

通过在 2026 年 2 月和 6 月进行系统性数据采样（并借助 Pangram 等 AI 检测工具），调查结果显示，专注或生成自 AI 的文章比例已经从每日热门帖子的 40% 上升至近 50% 甚至 60%。本文通过真实的数据图表和严谨的分析，揭示了当前主流技术社区被 LLM（大语言模型）内容重塑的现状。

---

# How much of HN is AI?

## Summary
The author explores their complicated relationship with [Hacker News (HN)](https://news.ycombinator.com)—valuing it as a vital geek news aggregator and traffic source while grappling with its toxic comment culture. Beyond the usual community friction, the author investigates a more profound shift: the staggering saturation of AI-driven content. Through systematic data sampling in February and June 2026 (utilizing tools like the Pangram detector), the investigation reveals that AI-focused or AI-generated stories have risen from 40% of the daily top posts to nearly 50–60%.

---

## Introduction

我与 [Hacker News](https://news.ycombinator.com) 保持着一种复杂的关系。这个网站是最重要的极客新闻聚合器，也是本博客的主要流量来源。与此同时，它也有相当一部分充满毒性的评论者，成了持续向我泼冷水的温床；如果你想见识一下，[这篇文章](https://lcamtuf.substack.com/p/how-has-mathematics-gotten-so-abstract)曾被他们斥为“毫无营养的水货（watered-down and slop）”。

> I have a complicated relationship with [Hacker News](https://news.ycombinator.com). The site is the most important aggregator of geek news and a major source of traffic to this blog. At the same time, it has a fair number of toxic commenters, making it a dependable source of insults hurled in my general direction; if you want a taste, [this article](https://lcamtuf.substack.com/p/how-has-mathematics-gotten-so-abstract) has been called “watered-down” and “slop”.

该网站由极客运营、为极客服务，因此它也无法对技术潮流免疫；例如，在 2018 年前后，它曾充斥着大量关于加密货币和 NFT 的报道。话虽如此，最近的这种转变感觉更为深刻：几乎每一天，头条阵容都被聚焦于 AI、由 AI 撰写或由 AI 评论的故事所主导。

> The site is run by geeks and for geeks, so it’s not immune to tech trends; for example, around 2018, it had a fair number of stories focused on cryptocurrencies and NFTs. That said, the recent shift feels more profound: almost every day, it feels that the lineup is dominated by stories focused on AI, written by AI, or commented on by AI.

<figure><a href="https://substackcdn.com/image/fetch/$s_!uOdH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53eb781a-accb-4de0-9d65-7cc0ea08f1b7_2437x1746.png" rel="noopener noreferrer" referrerpolicy="no-referrer" target="_blank"><picture><source type="image/webp" srcset="http://localhost/proxy/83jquJCu1nFackxTiieWrKTWrVb4OPGxmsYvWqX1ses=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXVPZEghLHdfNDI0LGNfbGltaXQsZl93ZWJwLHFfYXV0bzpnb29kLGZsX3Byb2dyZXNzaXZlOnN0ZWVwL2h0dHBzJTNBJTJGJTJGc3Vic3RhY2stcG9zdC1tZWRpYS5zMy5hbWF6b25hd3MuY29tJTJGcHVibGljJTJGaW1hZ2VzJTJGMjNlYjc4MWEtYWNjYi00ZGUwLTlkNjUtN2NjMGVhMDhmMWF3XzI0Mzd4MTc0Ni5wbmc= 424w, http://localhost/proxy/ncU2z7btT88UzDsdirLvFkenUz2AZK4lv3yNV-tDTJc=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXVPZEghLHdfODQ4LGNfbGltaXQsZl93ZWJwLHFfYXV0bzpnb29kLGZsX3Byb2dyZXNzaXZlOnN0ZWVwL2h0dHBzJTNBJTJGJTJGc3Vic3RhY2stcG9zdC1tZWRpYS5zMy5hbWF6b25hd3MuY29tJTJGcHVibGljJTJGaW1hZ2VzJTJGNTNlYjc4MWEtYWNjYi00ZGUwLTlkNjUtN2NjMGVhMDhmMWI3XzI0Mzd4MTc0Ni5wbmc= 848w, http://localhost/proxy/djTThuYHHooJfsT4wJMi9gGSD4th3v2x5pxfei8LZhg=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXVPZEghLHdfMTI3MixjX2xpbWl0LGZfd2VicCxxX2F1dG86Z29vZCxmbF9wcm9ncmVzc2l2ZTpzdGVlcC9odHRwcyUzQSUyRiUyRnN1YnN0YWNrLXBvc3QtbWVkaWEuczMuYW1hem9uYXdzLmNvbSUyRnB1YmxpYyUyRmltYWdlcyUyRjUzZWI3ODFhLWFjY2ItNGRlMC05ZDY1LTdjYzBlYTA4ZjFiN18yNDM3eDE3NDYucG5n 1272w, http://localhost/proxy/_h2uJOKqqyn16yYcqwxTDZ7jeV8lgaPg-grs5wRKe4g=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXVPZEghLHdfMTQ1NixjX2xpbWl0LGZfd2VicCxxX2F1dG86Z29vZCxmbF9wcm9ncmVzc2l2ZTpzdGVlcC9odHRwcyUzQSUyRiUyRnN1YnN0YWNrLXBvc3QtbWVkaWEuczMuYW1hem9uYXdzLmNvbSUyRnB1YmxpYyUyRmltYWdlcyUyRjUzZWI3ODFhLWFjY2ItNGRlMC05ZDY1LTdjYzBlYTA4ZjFiN18yNDM3eDE3NDYucG5n 1456w" sizes="100vw"/><img src="./images/b23426b7e22e.png" width="1456" height="1043" alt="" title="" srcset="http://localhost/proxy/8CtGlB0haAM0JxNptYetExeoy_yo6z2lvgDReQa-K0E=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXVPZEghLHdfNDI0LGNfbGltaXQsZl9hdXRvLHFfYXV0bzpnb29kLGZsX3Byb2dyZXNzaXZlOnN0ZWVwL2h0dHBzJTNBJTJGJTJGc3Vic3RhY2stcG9zdC1tZWRpYS5zMy5hbWF6b25hd3MuY29tJTJGcHVibGljJTJGaW1hZ2VzJTJGNTNlYjc4MWEtYWNjYi00ZGUwLTlkNjUtN2NjMGVhMDhmMWI3XzI0Mzd4MTc0Ni5wbmc= 424w, http://localhost/proxy/E8MGxBt9Jg-LZ7YsKGhhU61VwsOIrwgTAm83g8Hf0bQ=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXVPZEghLHdfODQ4LGNfbGltaXQsZl9hdXRvLHFfYXV0bzpnb29kLGZsX3Byb2dyZXNzaXZlOnN0ZWVwL2h0dHBzJTNBJTJGJTJGc3Vic3RhY2stcG9zdC1tZWRpYS5zMy5hbWF6b25hd3MuY29tJTJGcHVibGljJTJGaW1hZ2VzJTJGNTNlYjc4MWEtYWNjYi00ZGUwLTlkNjUtN2NjMGVhMDhmMWI3XzI0Mzd4MTc0Ni5wbmc= 848w, http://localhost/proxy/tFC6WMQgZZaazMmjK6R-xOFL2iuqkhqdatlVekxPqzM=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXVPZEghLHdfMTI3MixjX2xpbWl0LGZfYXV0byxxX2F1dG86Z29vZCxmbF9wcm9ncmVzc2l2ZTpzdGVlcC9odHRwcyUzQSUyRiUyRnN1YnN0YWNrLXBvc3QtbWVkaWEuczMuYW1hem9uYXdzLmNvbSUyRnB1YmxpYyUyRmltYWdlcyUyRjUzZWI3ODFhLWFjY2ItNGRlMC05ZDY1LTdjYzBlYTA4ZjFiN18yNDM3eDE3NDYucG5n 1272w, ./images/b23426b7e22e.png 1456w" sizes="100vw" fetchpriority="high" loading="lazy"/></picture></a><figcaption><em>HN AI singularity (July 21, 2026).</em></figcaption></figure>

那张图片展示的是一个格外极端的日子，为了给出更客观公正的评估，我还在 2026 年 2 月以及同年 6 月进行了更系统性的调查。

> That image shows a particularly bad day, so to give a more honest assessment, I also performed a more systematic survey in February 2026, and again in June of the same year.

---

## Original February 2026 Investigation

为了解信息流中被 AI 相关话题占据的比例，我对整个 2 月份每天的前 5 名热门内容进行了采样：

> To get a sense of how much of the feed is occupied by AI-related topics, I took a sampling of the daily top #5 for all of February:

<figure><a href="https://substackcdn.com/image/fetch/$s_!nyFk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F186ff171-6d6b-44c5-a7bd-951cea16899e_2000x713.jpeg" rel="noopener noreferrer" referrerpolicy="no-referrer" target="_blank"><picture><source type="image/webp" srcset="http://localhost/proxy/5yyPEIFw_26rwi7l8YQfELryGNMpKL2OWsDIBCw7F00=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIW55RmshLHdfNDI0LGNfbGltaXQsZl93ZWJwLHFfYXV0bzpnb29kLGZsX3Byb2dyZXNzaXZlOnN0ZWVwL2h0dHBzJTNBJTJGJTJGc3Vic3RhY2stcG9zdC1tZWRpYS5zMy5hbWF6b25hd3MuY29tJTJGcHVibGljJTJGaW1hZ2VzJTJGMTg2ZmYxNzEtNmQ2Yi00NGM1LWE3YmQtOTUxY2VhMTY4OTllXzIwMDB4NzEzLmpwZWc= 424w, http://localhost/proxy/cpVS6NUYGZa_1PiJIey4L1rMAi_CMhPAcsuiG1S8hRU=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIW55RmshLHdfODQ4LGNfbGltaXQsZl93ZWJwLHFfYXV0bzpnb29kLGZsX3Byb2dyZXNzaXZlOnN0ZWVwL2h0dHBzJTNBJTJGJTJGc3Vic3RhY2stcG9zdC1tZWRpYS5zMy5hbWF6b25hd3MuY29tJTJGcHVibGljJTJGaW1hZ2VzJTJGMTg2ZmYxNzEtNmQ2Yi00NGM1LWE3YmQtOTUxY2VhMTY4OTllXzIwMDB4NzEzLmpwZWc= 848w, http://localhost/proxy/IEuUb7hp6U5Yda9vaFbTSoZ4Y3A3xSJNPlbP20uaTRY=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIW55RmshLHdfMTI3MixjX2xpbWl0LGZfd2VicCxxX2F1dG86Z29vZCxmbF9wcm9ncmVzc2l2ZTpzdGVlcC9odHRwcyUzQSUyRiUyRnN1YnN0YWNrLXBvc3QtbWVkaWEuczMuYW1hem9uYXdzLmNvbSUyRnB1YmxpYyUyRmltYWdlcyUyRjE4NmZmMTcxLTZkNmItNDRjNS1hN2JkLTk1MWNlYTE2ODk5ZV8yMDAweDcxMy5qcGVn 1272w, http://localhost/proxy/vGNh5VWhvV3YhVCX82O9Ep-YgmyfcbFajeGyEtdQkeM=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIW55RmshLHdfMTQ1NixjX2xpbWl0LGZfd2VicCxxX2F1dG86Z29vZCxmbF9wcm9ncmVzc2l2ZTpzdGVlcC9odHRwcyUzQSUyRiUyRnN1YnN0YWNrLXBvc3QtbWVkaWEuczMuYW1hem9uYXdzLmNvbSUyRnB1YmxpYyUyRmltYWdlcyUyRjE4NmZmMTcxLTZkNmItNDRjNS1hN2JkLTk1MWNlYTE2ODk5ZV8yMDAweDcxMy5qcGVn 1456w" sizes="100vw"/><img src="./images/ef1f6343e953.jpg" width="1456" height="519" alt="" srcset="http://localhost/proxy/ZyDd33hzBwz0JSC4jy7BYxXXhrzHwCGUJThjyJEekN8=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIW55RmshLHdfNDI0LGNfbGltaXQsZl9hdXRvLHFfYXV0bzpnb29kLGZsX3Byb2dyZXNzaXZlOnN0ZWVwL2h0dHBzJTNBJTJGJTJGc3Vic3RhY2stcG9zdC1tZWRpYS5zMy5hbWF6b25hd3MuY29tJTJGcHVibGljJTJGaW1hZ2VzJTJGMTg2ZmYxNzEtNmQ2Yi00NGM1LWE3YmQtOTUxY2VhMTY4OTllXzIwMDB4NzEzLmpwZWc= 424w, http://localhost/proxy/5s6s4txlh-zlWfcxQ3srh1z2Gx0EWBKz0LMRxfCVKGg=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIW55RmshLHdfODQ4LGNfbGltaXQsZl9hdXRvLHFfYXV0bzpnb29kLGZsX3Byb2dyZXNzaXZlOnN0ZWVwL2h0dHBzJTNBJTJGJTJGc3Vic3RhY2stcG9zdC1tZWRpYS5zMy5hbWF6b25hd3MuY29tJTJGcHVibGljJTJGaW1hZ2VzJTJGMTg2ZmYxNzEtNmQ2Yi00NGM1LWE3YmQtOTUxY2VhMTY4OTllXzIwMDB4NzEzLmpwZWc= 848w, http://localhost/proxy/Td2zS2weTa_h_khXNoPRmAJ6CIE742uJuVcTILwY4bY=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIW55RmshLHdfMTI3MixjX2xpbWl0LGZfYXV0byxxX2F1dG86Z29vZCxmbF9wcm9ncmVzc2l2ZTpzdGVlcC9odHRwcyUzQSUyRiUyRnN1YnN0YWNrLXBvc3QtbWVkaWEuczMuYW1hem9uYXdzLmNvbSUyRnB1YmxpYyUyRmltYWdlcyUyRjE4NmZmMTcxLTZkNmItNDRjNS1hN2JkLTk1MWNlYTE2ODk5ZV8yMDAweDcxMy5qcGVn 1272w, ./images/ef1f6343e953.jpg 1456w" sizes="100vw" loading="lazy"/></picture></a></figure>

在 [2 月 4 日](https://news.ycombinator.com/front?day=2026-02-04)和 [2 月 12 日](https://news.ycombinator.com/front?day=2026-02-12)，AI 占据了前五名中的四个席位；而在 [2 月 5 日](https://news.ycombinator.com/front?day=2026-02-05)，可以说整个榜单都被其占领（第三条其实是某 AI 厂商的隐形营销）。唯一没有将 LLM 新闻挤入前五的天数是 [2 月 1 日](https://news.ycombinator.com/front?day=2026-02-01)（第一条 AI 新闻排在第 7 位，然后是第 9 位）、[2 月 9 日](https://news.ycombinator.com/front?day=2026-02-09)（第一条在第 8 位）以及 [2 月 25 日](https://news.ycombinator.com/front?day=2026-02-25)（AI 内容分别排在第 6、9、10 位）。

> AI took four out of five spots on [Feb 4](https://news.ycombinator.com/front?day=2026-02-04) and [Feb 12](https://news.ycombinator.com/front?day=2026-02-12), plus arguably the entire line-up on [Feb 5](https://news.ycombinator.com/front?day=2026-02-05) (story #3 was submarine marketing for an AI vendor). The only days without LLM news in the top 5 were [February 1](https://news.ycombinator.com/front?day=2026-02-01) (with the first AI story at #7, then #9), [February 9](https://news.ycombinator.com/front?day=2026-02-09) (first at #8), and [February 25](https://news.ycombinator.com/front?day=2026-02-25) (with AI at #6, #9, #10).

为了实验的第二部分——弄清楚哪些故事可能是 AI 撰写的——我使用了 [Pangram](https://pangram.com/)。Pangram 是一个非常优秀且保守的模型，专门用于检测 LLM 生成的文本。这类检测器在技术人员中名声不太好，但反对意见往往基于过时的假设或彻头彻尾的误解。要让这些工具发挥作用，AI 撰写的内容并不需要具备任何“非人类”的特征。只需当前这批 LLM 的*默认语调*具有准确定性（quasi-deterministic）就足够了：要求它写两次相同的文章，你会得到风格极其相似的结果。虽然单个人格特征看起来很像人类，但你的写作风格几乎不可能完美组合出完全相同的特征集。我在[这里](https://lcamtuf.substack.com/p/the-100000-whys-of-ai)对此进行了更多探讨。

> For the second part of the experiment — figuring out which stories were likely AI-written — I tapped into [Pangram](https://pangram.com/). Pangram is a remarkably good, conservative model for detecting LLM-generated text. These detectors have bad rap among techies, but the objections are often based on outdated assumptions or outright misconceptions. For the tools to work, AI writing doesn’t need to be in any way “inhuman”. It’s enough that the *default voice* of the current crop of LLMs is quasi-deterministic: ask for the same essay twice and you’ll get a stylistically similar result. The individual mannerisms are human-like, but it’s very unlikely that your writing combines the exact same set. I write about it a bit more [here](https://lcamtuf.substack.com/p/the-100000-whys-of-ai).

为了验证结果，我还复盘了所有被标记的故事，我认为这些发现合情合理；如果说有什么偏差的话，那就是 Pangram 漏掉了一些（false negatives）。为了让你对被标记的内容有一个直观感受，可以看看 [2 月 19 日](https://news.ycombinator.com/front?day=2026-02-19)排名第三的故事（*“AI 不是同事，而是外骨骼（AI is not a coworker, it’s an exoskeleton）”*）。它获得了 500 多个赞和 500 多条评论。在我看来，它充满了各种可疑的危险信号。

> To validate the results, I also reviewed all the flagged stories and I think the findings make sense; if anything, Pangram had a couple of false negatives. To give you a sense of what was flagged, have a look at the #3 story on [February 19](https://news.ycombinator.com/front?day=2026-02-19) (*“AI is not a coworker, it’s an exoskeleton”*). It had 500+ upvotes and 500+ comments. In my opinion, it has a wide range of red flags.

---

## Updated Data for June 2026

<figure><a href="https://substackcdn.com/image/fetch/$s_!y81s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7261bba-52bd-4a75-acc8-cdd70f153cf9_3500x1050.jpeg" rel="noopener noreferrer" referrerpolicy="no-referrer" target="_blank"><picture><source type="image/webp" srcset="http://localhost/proxy/rAW6WIgRP0sbg3dV7IRZHEgptOM6t6lTmc5dHZZhoK4=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXk4MXMhLHdfNDI0LGNfbGltaXQsZl93ZWJwLHFfYXV0bzpnb29kLGZsX3Byb2dyZXNzaXZlOnN0ZWVwL2h0dHBzJTNBJTJGJTJGc3Vic3RhY2stcG9zdC1tZWRpYS5zMy5hbWF6b25hd3MuY29tJTJGcHVibGdkJTJGaW1hZ2VzJTJGMjcyNjFiYmEtNTJiZC00YTc1LWFjYzgtY2RkNzBmMTUzY2Y5XzM1MDB4MTA1MC5qcGVn 424w, http://localhost/proxy/9oWtXnfOuGEC2K_JWHmiAUPhKOzOdk1lHEp6iKTUyko=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXk4MXMhLHdfODQ4LGNfbGltaXQsZl93ZWJwLHFfYXV0bzpnb29kLGZsX3Byb2dyZXNzaXZlOnN0ZWVwL2h0dHBzJTNBJTJGJTJGc3Vic3RhY2stcG9zdC1tZWRpYS5zMy5hbWF6b25hd3MuY29tJTJGcHVibGljJTJGaW1hZ2VzJTJGMjcyNjFiYmEtNTJiZC00YTc1LWFjYzgtY2RkNzBmMTUzY2Y5XzM1MDB4MTA1MC5qcGVn 848w, http://localhost/proxy/WbAIX5GNaanMkGeDJpFFUlfERq62D9YOshqr6zUa_Gs=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXk4MXMhLHdfMTI3MixjX2xpbWl0LGZfd2VicCxxX2F1dG86Z29vZCxmbF9wcm9ncmVzc2l2ZTpzdGVlcC9odHRwcyUzQSUyRiUyRnN1YnN0YWNrLXBvc3QtbWVkaWEuczMuYW1hem9uYXdzLmNvbSUyRnB1YmxpYyUyRmltYWdlcyUyRmY3MjYxYmJhLTUyYmQtNGE3NS1hY2M4LWNkZDcwZjE1M2NmOV8zNTAweDEwNTAuanBlZw== 1272w, http://localhost/proxy/g6FTj-ImnMcFfiEMa3D1oqjhbUT0AxPl6D-ytTsJBRI=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXk4MXMhLHdfMTQ1NixjX2xpbWl0LGZfd2VicCxxX2F1dG86Z29vZCxmbF9wcm9ncmVzc2l2ZTpzdGVlcC9odHRwcyUzQSUyRiUyRnN1YnN0YWNrLXBvc3QtbWVkaWEuczMuYW1hem9uYXdzLmNvbSUyRnB1YmxpYyUyRmltYWdlcyUyRmY3MjYxYmJhLTUyYmQtNGE3NS1hY2M4LWNkZDcwZjE1M2NmOV8zNTAweDEwNTAuanBlZw== 1456w" sizes="100vw"/><img src="./images/d5e2102eeee3.jpg" width="1456" height="437" alt="" srcset="http://localhost/proxy/hiq61Zmmso19f5cTl_KjdHRoQOZ8F4cUOFsxWx_Dhvk=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXk4MXMhLHdfNDI0LGNfbGltaXQsZl9hdXRvLHFfYXV0bzpnb29kLGZsX3Byb2dyZXNzaXZlOnN0ZWVwL2h0dHBzJTNBJTJGJTJGc3Vic3RhY2stcG9zdC1tZWRpYS5zMy5hbWF6b25hd3MuY29tJTJGcHVibGljJTJGaW1hZ2VzJTJGMjcyNjFiYmEtNTJiZC00YTc1LWFjYzgtY2RkNzBmMTUzY2Y5XzM1MDB4MTA1MC5qcGVn 424w, http://localhost/proxy/mx6Fmy8dIBexdSWUnZhi0907L_Bs_7-6hUMA2NxJhyQ=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXk4MXMhLHdfODQ4LGNfbGltaXQsZl9hdXRvLHFfYXV0bzpnb29kLGZsX3Byb2dyZXNzaXZlOnN0ZWVwL2h0dHBzJTNBJTJGJTJGc3Vic3RhY2stcG9zdC1tZWRpYS5zMy5hbWF6b25hd3MuY29tJTJGcHVibGljJTJGaW1hZ2VzJTJGMjcyNjFiYmEtNTJiZC00YTc1LWFjYzgtY2RkNzBmMTUzY2Y5XzM1MDB4MTA1MC5qcGVn 848w, http://localhost/proxy/m8-EJInllfv09mG4ZoIHigREBXAoi9k8H7Ym0W7fDMA=/aHR0cHM6Ly9zdWJzdGFja2Nkbi5jb20vaW1hZ2UvZmV0Y2gvJHNfIXk4MXMhLHdfMTI3MixjX2xpbWl0LGZfYXV0byxxX2F1dG86Z29vZCxmbF9wcm9ncmVzc2l2ZTpzdGVlcC9odHRwcyUzQSUyRiUyRnN1YnN0YWNrLXBvc3QtbWVkaWEuczMuYW1hem9uYXdzLmNvbSUyRnB1YmxpYyUyRmltYWdlcyUyRmY3MjYxYmJhLTUyYmQtNGE3NS1hY2M4LWNkZDcwZjE1M2NmOV8zNTAweDEwNTAuanBlZw== 1272w, ./images/d5e2102eeee3.jpg 1456w" sizes="100vw" loading="lazy"/></picture></a></figure>

在 6 月份，为了捕捉更多细节，我用纯黑色块来表示纯粹的 AI 自恋式内容（厂商发布会、关于该技术利弊的社论等），并用阴影纹理来表示那些深度涉足 AI 但具有更广泛影响的故事（例如 [Instagram AI 客服账号被黑事件](https://www.securityweek.com/meta-says-20000-instagram-accounts-hacked-via-ai-tool-abuse/)）。和之前一样，那些与 AI 仅有间接联系的故事（例如关于内存价格暴涨的报道）不在此标记范围内。

> In June, to capture more detail, I used solid black for pure-play AI navel-gazing (vendor announcements, op-eds about the benefits or drawbacks of the technology, etc) and hatched shapes for stories that lean heavily into AI, but have broader ramifications (e.g., the [Instagram AI support agent account hack](https://www.securityweek.com/meta-says-20000-instagram-accounts-hacked-via-ai-tool-abuse/)). As before, stories that are only tangentially related to AI (e.g., reports of RAM price hikes) are not flagged.

在六月的前半个月，大约 60% 的 HN 每日头条阵容都与 AI 相关或由 AI 生成，随着临近月底这一比例回落至 50% 左右。相比 2 月份的 40%，这一比例显然有所上升。

> In the first half of the month, roughly 60% of the daily HN lineup was AI-related or AI-generated, tapering off to ~50% as we approached the end of the month. This is up from 40% in February.

---

[Subscribe now](https://blog.coredump.cx/subscribe?)