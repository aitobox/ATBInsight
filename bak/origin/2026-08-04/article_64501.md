# I'm (Mostly) Picking Models on Speed Now, Not Intelligence

## Summary
For the first time, model selection is shifting from raw intelligence to raw speed. With modern mid-tier models (such as those around the Opus 4.6 level) proving "smart enough" for everyday coding, research, and design, the sluggishness of ultra-heavy frontier models has become a noticeable bottleneck. While ultra-fast token generation (100–200+ tok/s) drastically improves user experience, agent workflows will eventually hit a wall defined by local tool calls and human review times. Meanwhile, an aggressive price war and upcoming hardware leaps—like HBM4 memory—promise even faster, cheaper models by 2027.

---

## Have We Reached an Intelligence Tipping Point?

This is probably going to age like spoilt milk, but right now, models around the ~Opus 4.6 level seem to be "smart enough" for most of my daily tasks—code, pulling together research, designing slide decks, and doing analytical tasks against a plethora of databases.

While like most I was hyped to play around with Fable, ironically the US Gov shutdown gave everyone time to get used to Opus again. When Fable came back post-hype with additional guardrails, the first thing I noticed was just how *slow* it is [^1]. So slow, actually, that I switched back to Opus pretty quickly.

I've spent a *lot* of my career making software fast. It's remarkable how much better software feels to interact with when it's *fast*. In my experience (and many studies), you can take the most beautiful product, but if it's slow, you won't enjoy using it. Equally, you can take a very basic product that's super fast and it will feel brilliantly utilitarian [^2].

It's clear to me that when only a few, big, slow models cleared the aforementioned (and hypothetical) intelligence bar, it wasn't really worth the trade-off to use a slower model. Whatever speed you gain, you quickly lose in having to redo it because it was broken.

---

## Is 100tok/s the New 100ms?

I've [written before](https://martinalderson.com/posts/what-happens-when-coding-agents-stop-feeling-like-dialup/) about agents feeling like dial-up, back when frontier models were crawling along at 30–60 tok/s. That has changed faster than I expected.

The key fact I remember is that to humans, ~100ms feels "instant"—the gold standard. I reckon a 100 tok/s output on a model is about as fast as I can keep up with. After that, it comes in faster than I can (skim) read. This isn't an exact bar, because increasingly most of the model time is spent in reasoning, not actually showing you output tokens. It also massively varies based on the output; prose gets output with far fewer tokens per character than code, so your mileage may (and will) vary.

Roughly, 100–200 tok/s *to me* seems pretty damn fast. Below 50 tok/s, output feels increasingly sluggish. Ironically, going past 200 tok/s seems almost unnerving—you can try a [model out here](https://chatjimmy.ai/) running at 10,000 tok/s+ (!). I'm sure this feeling will edge upwards as we get used to it and push our agents to do more complicated work.

Given the plethora of new models that I think are clearing the aforementioned bar—such as GLM5.2 and DeepSeek V4 Flash GA, which are open weights *and* smaller—we now have a wide range of models and speeds. If you look at the speed rankings of various providers for GLM5.2 on [OpenRouter](https://openrouter.ai/z-ai/glm-5.2?tableSort=throughput&tableSortDir=desc#providers), you can see the enormous range of serving speeds: from less than 30 tok/s at the bottom to 129 tok/s at the top.

This is another huge plus to the open weights ecosystem. While the obvious cost benefits are great, the fact that providers are also incentivized to compete on speed like this is really interesting [^3].

---

## But There Are Limitations

If you're familiar with [Pareto's Principle](https://en.wikipedia.org/wiki/Pareto_principle) and [Amdahl's Law](https://en.wikipedia.org/wiki/Amdahl%27s_law), you'll know what's coming up.

Assuming "good enough" models continue to get faster and faster, increasingly the speed benefit is lost to tool calls and human oversight.

Take an agent using a model processing at 50 tok/s. Most of the time is spent waiting for inference to come back. Now run the same turn at 250 tok/s, and you'll see that you are increasingly bottlenecked by tool calls on your "local" machine and your own decision-making.

![Stacked bar chart comparing one agent turn at 50 tok/s and 250 tok/s. At 50 tok/s the turn takes 65 seconds - 40s inference, 15s tool calls, 10s human review. At 250 tok/s it takes 33 seconds - 8s inference, with the same 15s of tool calls and 10s of review. A 5x faster model gives only a 2x faster agent.](http://localhost/proxy/H2FYqU0OU1pVl9qDhdK5fsxx2Wb2tdOBWQ9v_K4x4M4=/aHR0cHM6Ly9tYXJ0aW5hbGRlcnNvbi5jb20vaW1nL2FnZW50LXR1cm4tdGltZS1icmVha2Rvd24ucG5n)

> *Rough numbers, but the shape holds. The 5x speedup on the model only buys you a 2x speedup on the turn, because the other 25 seconds didn't move.*

And *even worse*, making your local machine faster on these tool calls is sort of stalling out, because hardware costs have gone parabolic *because* of AI. Yet another weird derivative effect of the AI market.

So I suspect (for now at least) there is a limit to how much demand there will be for speed past a certain point. No doubt there will be some examples where huge amounts of reasoning are useful (like mathematics research), where speeding that up is helpful. But I'd expect many agents to start getting bottlenecked by local/internal hardware, database calls, and other sources of latency.

---

## The Price War Is Coming

Interestingly, OpenAI reduced the cost of their Luna variant by 80% just before the DeepSeek V4 Flash GA release, making it remarkably affordable for a frontier model. While I haven't had as much luck getting great output out of it compared to GLM5.2, I think it points toward an absolute bloodbath of pricing at this end of the market.

You can see this happening on OpenRouter with GLM5.2—endless discounts being offered to try and attract customers. We're already down to $0.42/$1.32/MTok on GLM5.2—*5%* of the price of Opus.

![OpenRouter provider table for GLM 5.2 showing discounted per-million-token prices and throughput for StreamLake, NovitaAI, Decart, DeepInfra, Baidu Qianfan, CoreWeave, AkashML, GMICloud and Inceptron](http://localhost/proxy/xNkkUj2hRXk84ZC1n6H7SR1QGhxB5WYQsbk3EXn9QtQ=/aHR0cHM6Ly9tYXJ0aW5hbGRlcnNvbi5jb20vaW1nL2dsbS01Mi1vcGVucm91dGVyLXByb3ZpZGVycy5wbmc)

> *While the very cheapest is slow, for not much more you can get 109 tok/s from DeepInfra.*

As the next generation of GPUs starts being deployed over the next few months—Nvidia's Vera Rubin series and AMD's MI400s, amongst others—the new HBM4 memory in those chips will deliver a 2x+ speedup on output tokens from memory bandwidth alone, plus more on top from additional compute and interlinks.

In 2027, it's very possible we'll have very good quality models at reasonable prices running at 500 tok/s+. Staring at "still thinking on xhigh effort" for most of your day may finally become a thing of the past.

What will be interesting to watch for—and I'm not sure where to bet—is whether the vast 2–3T+ parameter models actually do perform *dramatically* better for everyday tasks. On one hand, it feels like we've hit a sweet spot right now; on the other, having an order of magnitude more intelligence in the model may make today's sweet spot look very, very primitive.

---

## Footnotes

[^1]: Second, of course, is the endless guardrails firing, which tend to happen at the worst possible time—just when I'm getting deep into a difficult task and I feel I could do with the extra "firepower" that Fable offers, but that's a story for another day. [↩](#fnref1)

[^2]: A classic example is something like Craigslist or Hacker News. While they look dated, they are so damn responsive you don't notice. Equally, your "standard" SPA app serving 30MB of React to render a homepage feels like treacle and a chore to use most of the time, despite what was surely an enormous spend on design and product. [↩](#fnref2)

[^3]: I'm aware that both OpenAI and Anthropic have offered fast variants of models for a long time, but the API pricing is eye-watering. Unless you are token-maxxing your benchmarks with a blank check, I haven't come across anyone who uses them for day-to-day operations. Having great models that are super fast at a reasonable price is a very recent addition to the market. [↩](#fnref3)