---
authors:
- aitoboxrobot
categories:
- 工具教程
date: 2026-08-06
hide:
- navigation
tags:
- GPT-2
- OpenAI
- LLM评估
- 指令微调
- Bug修复
title: 为什么 OpenAI 的 GPT-2 权重能击败我的模型？第二部分：Bug 修复
---
# 为什么 OpenAI 的 GPT-2 权重能击败我的模型？第二部分：Bug 修复

### 文章背景与核心概要
本文是探索自研 GPT-2 模型为何在指令遵循评估中落后于 OpenAI 原厂权重系列的第二部分。在复盘评估脚本时，借助 AI 审稿辅助发现了一个关键的程序 Bug：评估代码在保存最佳模型参数时使用了浅引用而非深拷贝，导致早停机制失效，同时验证集样本批次被过度截断。作者修复了这些错误并重新构建了评估基准线。虽然各模型指标与排名有所浮动，但核心谜题依旧成立：OpenAI 的原厂模型依然稳居榜首，为后续探究差异根源提供了更可靠的基础。

---

> **Summary:** While reviewing a previous investigation into why custom GPT-2 models underperformed against OpenAI’s original weights on instruction-following evaluations, an AI editorial board helped uncover a critical bug in the evaluation script. Specifically, the script failed to properly copy model parameters and truncated validation batches. After fixing these issues and establishing a new baseline, the core mystery remains intact: OpenAI's models still outperform the custom weights, providing a solid foundation for future experiments.

---

## 导言

我正在深入探究为什么我自己训练的 GPT-2 架构模型在指令遵循评估中的得分会落后于 OpenAI 的原始权重；我在[上一篇文章](https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-1-intro)中详细说明了具体细节。

> I'm digging into why my GPT-2 style models score worse on an instruction-following eval than OpenAI's original weights; I gave the details in [this post](https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-1-intro).

在撰写关于第一项可能原因的实验结果时，我将文章发给了 ChatGPT——我总是使用 AI 组成“编辑委员会”来检查文章的流畅度、文风以及技术错误（不过所有文字始终由我自己撰写）。它查看了我正在运行的评估代码，并指出了一处 Bug。

> While I was writing up the results of my first experiment into possible causes, I ran the post past ChatGPT—I always use an "editorial board" of AIs to check my posts for flow, style, and any technical errors (though all writing is always mine). It took a look at the eval code that I was running, and highlighted a bug.

幸运的是，这并没有改变核心结论——OpenAI 的模型在指令遵循方面依然优于我的模型。但这足以改变基准线数据，重新排列了我自己各个模型的表现顺序。因此我修复了该问题并重新生成了基准线，确保未来的实验能建立在坚实的基础上。

> Luckily, it doesn't change the important results—OpenAI's models continue to be better than mine at instruction-following. But it was enough to change the baseline numbers, re-ordering how well my own models did. So I fixed it and regenerated the baseline so that future experiments are based on solid ground.

---

## Bug 详解

该评估过程接收一个模型，并在 Alpaca 指令遵循数据集子集划分出的训练集上对其进行多轮（epoch）训练。在每个 epoch 结束时，评估脚本会在保留的验证集上评估所得模型；如果验证损失开始上升，则提前退出。最后，它会将数据集的测试集输入到最终模型中并保存结果。

> The eval takes a model, and trains it over multiple epochs on a split of a subset of the Alpaca instruction-following dataset. At the end of each epoch, it evaluates the resulting model against a held-back validation split; if the eval loss starts rising, it bails out. Finally, it runs a test split of the dataset through the resulting model, and saves the result.

一旦我对多个不同的模型运行完该过程，就会使用一个 LLM-as-a-judge（LLM作为裁判）脚本，让 GPT 5.5 给结果打分——对于每个问答结果，它会在[同一个 Prompt 中](https://www.gilesthomas.com/2026/01/llm-from-scratch-30-digging-into-llm-as-a-judge)看到所有模型做出的所有回答，并且每次都随机打乱顺序，以尽可能保证模型间打分的一致性。

> Once I've run it for a bunch of different models, I use an LLM-as-a-judge script to get GPT 5.5 to score results—for each question-answering result, it sees all of the responses for all of the models [in the same prompt](https://www.gilesthomas.com/2026/01/llm-from-scratch-30-digging-into-llm-as-a-judge), shuffled in order each time, to try to make it judge models against each other as consistently as possible.

原本的设计意图是，在生成测试集回答时，使用的是验证损失上升前那一个 epoch 的模型。因此我编写了如下代码：

> Now, the idea was that the generation of the test split answers would use the model from the epoch prior to the rising-loss one. So I had code like this:

```python
    for epoch in range(100):
        model.train()
        for input_batch, target_batch in tqdm(train_loader, desc=f"Epoch {epoch}"):
            optimizer.zero_grad()
            loss = calc_loss_batch(
                input_batch, target_batch, model, device
            )
            loss.backward()
            optimizer.step()

        model.eval()
        val_loss = calc_loss_loader(val_loader, model, device, eval_iter)

        if last_val_loss is None or last_val_loss > val_loss:
            last_val_loss = val_loss
            last_params = model.state_dict()
            print("Val loss still decreasing, continuing")
        else:
            print("Val loss rising, bailing out")
            break

    model.load_state_dict(last_params)
```

每当验证损失下降时，我都希望将模型的参数暂存到 `last_params` 中，以便在最后一行代码里恢复它们。

> Each time the validation loss went down, I wanted to store the model's parameters in `last_params` so that they could be restored later in that last line.

如果你仔细看，错误其实非常明显。`model.state_dict()` 并不返回模型参数的副本——它产生的是一个字典，里面包含的是对模型内部参数的引用。因此，虽然我试图在每次损失下降时把参数暂存在 `last_params` 中，以便保留验证损失上升前上一个 epoch 生效的参数副本，但我实际上只是毫无意义地保存了一个指向“实时”参数的引用。对 `model.load_state_dict(last_params)` 的调用实际上形同虚设（无操作）。

> If you look closely, the error is pretty obvious. `model.state_dict()` does not return a copy of the model's parameters—it produces a dictionary containing references to the parameters inside the model. So although I was trying to stash away the parameters in `last_params` each time loss went down, so that we had a copy of the ones that were live in the epoch prior to the rising-loss one, what I was actually doing was just pointlessly saving a reference to the "live" params. The call to `model.load_state_dict(last_params)` was essentially a no-op.

解决方案很简单：

> The solution was simple enough:

```python
from copy import deepcopy
...
        last_params = deepcopy(model.state_dict())
```

这就足以让代码按照预期的方式运行了。

> That was enough to make the code do what it was meant to do.

顺便提一句，我还注意到评估代码在评估数据集中只使用了前 5 个批次。这段代码最初改编自《*从零开始构建大语言模型 (Build a Large Language Model (from Scratch))*》中的评估部分，原书中的评估运行得非常频繁，必须速度极快。而我自己的代码运行频率较低，因此使用全部数据会更合理。鉴于我要完全重新运行脚本来生成测试回答，我想不妨顺便把这个问题也一并修了。

> While I was there, I also noticed that the evaluation code was only using the first five batches in my eval dataset. This code was originally adapted from an eval in *[Build a Large Language Model (from Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch)*, where the eval was run much more frequently and had to be super-fast. Because my own code ran it more rarely, it made more sense to use all of it. Given that I was going to completely re-run the script to generate the test responses, I figured that I might as well fix that at the same time.

---

## 全新的基准线

我在对比的所有模型上重新运行了修复后的脚本，并将其提交给 GPT 5.5 裁判；以下是我得到的结果：

> I re-ran the fixed script on all of the models I'm comparing, and ran that past the GPT 5.5 judge; here's what I got:

| Model | Test loss | Old IFT epochs | Old IFT score | Old IFT rank | New IFT epochs | New IFT score | New IFT rank |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| OpenAI weights: medium | 3.231442 | 2 | 41.62 | 1 | 2 | 42.41 | 1 |
| JAX, with MHA bias, no dropout | 3.418784 | 4 | 19.25 | 4 | 4 | 18.12 | 5 |
| JAX, no MHA bias, no dropout | 3.420089 | **3** | 14.66 | 11 | **5** | 20.72 | 3 |
| JAX, no MHA bias, with dropout | 3.476802 | **4** | 12.94 | 15 | **7** | 16.98 | 8 |
| OpenAI weights: small | 3.499677 | 2 | 26.73 | 2 | 2 | 26.11 | 2 |
| `1xrtx3090-stacked-interventions` | 3.538161 | 4 | 17.79 | 6 | 4 | 13.68 | 11 |
| `8xa100m40-stacked-interventions-1` | 3.577761 | 4 | 10.29 | 16 | 4 | 9.81 | 15 |
| Cloud FineWeb, 8x A100 40 GiB | 3.673623 | **7** | 20.71 | 3 | **6** | 19.45 | 4 |
| `1xrtx3090-baseline` | 3.683835 | 6 | 15.11 | 9 | 6 | 13.39 | 12 |
| `8xa100m40-baseline` | 3.691526 | 4 | 14.74 | 10 | 4 | 14.64 | 9 |
| Cloud FineWeb, 8x H100 80 GiB | 3.724507 | 4 | 13.25 | 14 | 4 | 13.84 | 10 |
| Cloud FineWeb, 8x A100 80 GiB | 3.729900 | 4 | 14.50 | 12 | 4 | 11.30 | 14 |
| Cloud FineWeb, 8x B200 160 GiB | 3.771478 | 4 | 16.03 | 8 | 4 | 11.82 | 13 |
| Local FineWeb train | 3.943522 | 7 | 13.73 | 13 | 7 | 8.93 | 16 |
| Local FineWeb-Edu extended train | 4.134991 | 7 | 16.70 | 7 | 7 | 17.10 | 7 |
| Local FineWeb-Edu train | 4.166892 | 7 | 18.68 | 5 | 7 | 17.28 | 6 |

让我们深入分析一下这些数据。

> Let's dig into those numbers.

---

## 训练 Epoch 轮数分析

首先来看训练的 epoch 轮数；我高亮标出了发生变化的模型。

> Let's look into the number of training epochs first; I've highlighted the models for which it changed.

对于 "Cloud FineWeb, 8x A100 40 GiB" 模型，我认为这是由于验证样本数量变化导致的结果。

> For the "Cloud FineWeb, 8x A100 40 GiB" model, I think that was a result of the change to the number of validation samples.

至于两个 JAX 模型，情况就更扑朔迷离了。可能存在一部分“更多评估数据”带来的波动，但我怀疑还存在其他与 dropout 相关的因素。

> For the two JAX models, it's a bit more of a mystery. There may be some part of the same "more eval data" variation there, but I have a suspicion that there's something more, related to dropout.

我迄今为止的方法是：IFT 训练运行应当使用与原始基座模型训练运行相同的 dropout 设置（我会在后面的文章中谈到这一点）。然而，由于 JAX 训练脚本与评估代码（基于 PyTorch）之间的差异，在评估这些模型时匹配 dropout 率有点繁琐且容易出错。

> My methodology to date has been that the IFT training runs should use the same dropout setting as the original base model training run (I'll come back to this in a later post). However, due to differences between the JAX training script and the evaluation code (which is PyTorch), matching the dropout rate when evaluating those models is a bit fiddly and error-prone.

我 100% 确定这次设置是正确的——我已经反复核对了运行的具体命令。但我认为——根据我的记忆——上一次我可能搞砸了。这并不确定，只是基于几周前运行的一些命令的模糊记忆（当时打开了太多的终端，没有记录在 `.bash_history` 中）。

> I am 100% sure that I got it right this time around—I've checked and double-checked the specific commands I ran. But I think—from what I remember doing—that I might have messed it up the previous time. That's not certain, though—just a suspicion based on half-memories of some commands I ran several weeks ago, which never wound up in my `.bash_history` (too many terminals open at once).

---

## 排名浮动分析

对于 IFT 分数，请记住不同运行批次之间的得分并不具备强可比性。假设 LLM 裁判针对“《傲慢与偏见》的作者是谁？”这一问题收到了以下回答：

> For the IFT scores, remember that they're not strongly comparable between runs. Let's imagine that the LLM judge is given the following answers to the question "Who was the author of *Pride and Prejudice*?":

* "Jane Austen"
* "The author of 'Pride and Prejudice' was Jane Austen"
* "The author of 'Pride and Prejudice' was Sarah Palin"
* "The author of 'Pride and Prejudice' was 'Pride and Prejudice'"

在某些情况下，它可能会给前两个回答都打 100/100 分，而在另一些情况下，它可能会因为第二个回答过于冗长而只打 95/100 分。同样，在某些情况下，它可能会因为后两个回答错误而打 0/100 分，但在其他情况下，它可能会因为 "Sarah Palin" 至少是一个人名而不是纯粹的废话而打 5/100 分。

> In some cases it might treat the first two as being 100/100, in others it might give the second 95/100 for being too wordy. Likewise, in some cases it might rank the last two as 0/100 for being wrong, in others it might give the "Sarah Palin" one 5/100 for at least being the name of a person rather than complete nonsense.

现在，我们总是要求 LLM 一口气评审所有模型对某个给定问题的回答，因此我们至少可以确保对于给定问题和 Prompt，评估标准是一致的。但我们无法保持一致的是它在不同批次运行之间、或在同一批次的不同问题之间的倾斜态度。有时它可能感觉比较“慷慨”，给莎拉·佩林（Sarah Palin）的回答一点宽容分，有时它可能更严苛。

> Now, we always ask the LLM to judge all of the models' answers for a given question in one go, so at least we can be sure that it will be consistent for a given prompt about a given question. But what we can't keep consistent is which way it leans between different runs, or different questions within the same run. Sometimes it might be feeling "generous" and give the Sarah Palin answer a bit of grace, other times it might be harsher.

因此这里存在相当大的噪声；我的经验法则是 1 到 2 分的波动属于正常噪声范围。因此，OpenAI medium 模型从 41.62 变动到 42.41 几乎没有任何实质意义，同样 "JAX, with MHA bias, no dropout" 从 19.25 移动到 18.12 也是如此。

> So there's a significant amount of noise there; my rule of thumb is that a variation of a point or two is within that noise, so OpenAI medium going from 41.62 to 42.41 is pretty much meaningless, and likewise "JAX, with MHA bias, no dropout"'s move from 19.25 to 18.12.

因此，真正重要的是**相对排名**——谁是第一，谁是第二，依此类推。当然，你必须考虑到如果一个模型像 "JAX, no MHA bias, no dropout" 那样从第 11 位上升到第 3 位，那么原本的第 3 位就会顺延变成第 4 位，第 4 位变成第 5 位，以此类推。你可以在结果表中看到这种情况的发生。显然，随着其他模型的升降，这会产生连锁反应。

> So what's important is the relative ranking—which is first, which is second, and so on. Naturally, you have to allow for the fact that—for example—if one model goes from position 11 to position 3, like "JAX, no MHA bias, no dropout" did, then the previous number 3 will have to become number 4, 4 will become 5, and so on. You can see that happening in the results table. Obviously, as other models rise and fall, that has further knock-on effects.

无论如何，在说明了所有这些注意事项之后，好消息是：我最初的谜题依然存在。OpenAI 的模型表现明显好于我自己训练的模型。GPT-2 medium 继续领跑（考虑到它是更大的模型，这并不令人意外），而 GPT-2 small 仍然稳居第二。如果这个结论改变了，本系列文章就会陷入相当令人失望的结局：“谜底揭晓，原来是评估脚本里的一个 Bug :-("

> Anyway, with all of those caveats, the good news is that my original mystery remains. The OpenAI models were still doing noticeably better than my own ones. GPT-2 medium continued to lead the pack (unsurprisingly, given that it's a bigger model), and GPT-2 small was still in second place. If that had changed, it would have made a rather disappointing end to this series: "mystery explained, it was a bug in the eval :-("

但现在让我们来看看我自己的模型。

> But now let's look at my models.

首先，似乎“无 MHA bias”模型可能受益于额外的训练——或者受益于纠正了 dropout 设置。它们的排名分别从第 11 和第 15 位提升到了第 3 和第 8 位——对于 "JAX, no MHA bias, no dropout" 来说是巨大飞跃，对 "JAX, no MHA bias, with dropout" 也是稳步提升。

> Firstly, it looked like the "no MHA bias" models might have benefited from the extra training—or from having their dropout settings corrected. They rose from positions 11 and 15 to 3 and 8 respectively—a huge swing for "JAX, no MHA bias, no dropout", and a solid improvement for "JAX, no MHA bias, with dropout".

相对排名的绝大多数其他变动都可以解释为这两个模型的排名上升，但也有其他一些变化。特别是，有三个模型的得分（以及随之而来的排名）出现了大幅下降：

> Most of the other changes in relative rankings can be explained by those two models having been promoted, but there are some other changes. In particular, three models dropped significantly in score (and, as a result, ranking):

* `1xrtx3090-stacked-interventions`
* "Cloud FineWeb, 8x B200 160 GiB"
* "Local FineWeb train"

我的猜想——一个不甚确定但很有趣的假说——是这些模型此前可能**受益于**那个 Bug。

> My suspicion—a very weakly-held hypothesis, but an interesting one—is that those models had previously been *benefiting* from the bug.

请记住，我们用来停止训练的信号是验证损失开始上升。我们将此作为过拟合的替代指标，而过拟合又被我们用作“该模型在该数据上的训练量已满足评估需求”的替代指标。

> Remember that the signal we're using to stop training is that the validation loss starts rising. We're using that as a proxy for overfitting, which in turn we're using as a proxy for "this model has had as much training on this data as it needs for the eval".

但并不能保证这其中存在必然联系。也许这些模型并没有过拟合，如果我们再等待一两个 epoch，验证损失可能会重新开始下降。又或者一定程度的过拟合实际上对这项评估是有益的？

> But there's no guarantee that the connection is there. Perhaps the models weren't overfitting and if we'd waited for another epoch or two, the validation loss might have started falling again. Or maybe some amount of overfitting would be beneficial for this eval?

---

## 结论

我在这里可能还可以挖掘出近乎无限的细节。但我认为最好就此打住。修复 Bug 是至关重要的一步，因为它意味着评估代码现在终于做成了我以为它在做的事。

> There's probably a near-infinite amount of digging in that I could potentially do here. But I think it's best to stop. The bugfix was important because it meant that the eval was now doing what I thought it was doing.

最重要的是，这并未改变一个令人困惑的事实：我的模型在本次评估中依然逊色于 OpenAI 的模型，而这正是我想解开的谜团。这也意味着我现在可以更自信地依赖这些基准线数据了。

> Importantly, it doesn't change the puzzling fact that my models were worse at this eval than OpenAI's, which is what I'm trying to untangle. And it means that I can now lean more confidently on the baseline numbers.

所以，现在是时候开始改变一些设定，看看我能否缩小差距了！

> So now it's time to actually start changing things to see if I can close the gap!

[这里是本系列下一篇文章的链接：过度训练是否有用？](https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-3-overtraining)

> [Here's a link to the next post in this series: does overtraining help?](https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-3-overtraining)
