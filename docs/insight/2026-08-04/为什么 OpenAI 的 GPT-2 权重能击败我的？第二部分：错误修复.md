# 为什么 OpenAI 的 GPT-2 权重能击败我的？第二部分：错误修复

**背景与摘要：**
在我持续调查为什么我自定义的 GPT-2 模型在遵循指令任务上的表现不如 OpenAI 原始权重的过程中，我在自己的评估流程里发现了一个严重的 Bug。虽然修复这个 Bug 并没有消除性能差距，但它纠正了我的基准指标，并为未来的实验提供了更可靠的基础。本文详细介绍了这个技术疏忽、必要的代码修正，以及对更新后性能排名的分析。

> ### Summary
> In my ongoing investigation into why my custom GPT-2 models underperform compared to OpenAI’s original weights on instruction-following tasks, I discovered a critical bug in my evaluation pipeline. While the fix didn't close the performance gap, it corrected my baseline metrics and provided a more reliable foundation for future experiments. This post details the technical oversight, the necessary code correction, and an analysis of the updated performance rankings.

---

## 那个 Bug

我的评估流程使用了一个基于验证集损失的“提前停止 (stop-early)”机制。其意图是保存验证集损失仍在下降的最后一个 epoch 的模型参数。

> ## The Bug
> My evaluation pipeline uses a "stop-early" mechanism based on validation loss. The intention was to save the model parameters from the last epoch where the validation loss was still decreasing.

缺陷在于我处理模型状态的方式：

> The flaw was in how I handled the model state:

```python
# 有 Bug 的代码
last_params = model.state_dict()
```

`model.state_dict()` 返回的是一个包含模型参数**引用**的字典，而不是副本。因此，`last_params` 总是指向模型的“实时”参数，这使得后续的 `model.load_state_dict(last_params)` 变成了一个毫无意义的空操作 (no-op)。

> `model.state_dict()` returns a dictionary of **references** to the model's parameters, not a copy. Consequently, `last_params` was always pointing to the "live" parameters of the model, making the subsequent `model.load_state_dict(last_params)` a no-op.

**修复方法：**
我实现了 `deepcopy`（深拷贝）以确保正确地对参数进行了快照：

> **The Fix:**
> I implemented `deepcopy` to ensure the parameters were correctly snapshotted:

```python
from copy import deepcopy
...
last_params = deepcopy(model.state_dict())
```

此外，我更新了评估脚本，使其使用完整的验证数据集，而不仅仅是前五个批次，从而确保对模型性能进行更稳健的评估。

> Additionally, I updated the evaluation script to use the full validation dataset rather than just the first five batches, ensuring a more robust assessment of model performance.

---

## 新的基准

在使用修正后的代码重新运行评估后，我生成了一组新的排名。虽然 OpenAI 的模型依然名列前茅，但我自己各个模型的相对排名发生了显著变化。

> ## A New Baseline
> After re-running the evaluation with the corrected code, I generated a new set of rankings. While the OpenAI models remain at the top, the relative rankings of my own models shifted significantly.

| 模型 | 新的 IFT 分数 | 新的 IFT 排名 |
| :--- | :--- | :--- |
| OpenAI 权重: medium | 42.41 | 1 |
| OpenAI 权重: small | 26.11 | 2 |
| JAX, 无 MHA 偏差, 无 dropout | 20.72 | 3 |
| Cloud FineWeb, 8x A100 40 GiB | 19.45 | 4 |
| JAX, 有 MHA 偏差, 无 dropout | 18.12 | 5 |

> | Model | New IFT Score | New IFT Rank |
> | :--- | :--- | :--- |
> | OpenAI weights: medium | 42.41 | 1 |
> | OpenAI weights: small | 26.11 | 2 |
> | JAX, no MHA bias, no dropout | 20.72 | 3 |
> | Cloud FineWeb, 8x A100 40 GiB | 19.45 | 4 |
> | JAX, with MHA bias, no dropout | 18.12 | 5 |

---

## 结果分析

### 训练轮数与 Dropout

“无 MHA 偏差”的模型性能有了显著提升，这可能是由于更全面的评估数据和修正后的 dropout 设置共同作用的结果。此前，我怀疑我的 dropout 配置在 JAX 训练环境和 PyTorch 评估脚本之间不一致；现在我已经验证这些设置已正确对齐。

> ## Analysis of Results
> 
> ### Training Epochs and Dropout
> The "no MHA bias" models saw a significant performance boost, likely due to the combination of more comprehensive evaluation data and corrected dropout settings. Previously, I suspected my dropout configuration was inconsistent between the JAX training environment and the PyTorch evaluation script; I have now verified these settings are correctly aligned.

### 作为裁判的大语言模型带来的“噪音”

需要注意的是，基于 LLM 的评估本质上就带有噪音。1-2 分的波动通常在误差范围之内。然而，*相对*排名仍然是一个有用的指标。某些模型排名下降这一事实表明，它们可能曾经因为之前的 Bug 而“受益”，也许是恰好停在了一个对当时不完整的评估数据有利的节点上。

> ### The "Noise" of LLM-as-a-Judge
> It is important to note that LLM-based evaluation is inherently noisy. A variation of 1–2 points is often within the margin of error. However, the *relative* ranking remains a useful indicator. The fact that some models dropped in rank suggests they may have been "benefiting" from the previous bug, perhaps by stopping at a point that happened to be favorable for the incomplete evaluation data.

### 结论

谜团依然存在：OpenAI 的权重表现仍然优于我的模型。虽然 Bug 修复并没有解决核心问题，但它提供了一个稳定的基准。现在我可以充满信心地继续前进，测试过度训练（overtraining）等变量是否有助于缩小性能差距。

> ### Conclusion
> The mystery remains: OpenAI’s weights still outperform my models. While the bugfix didn't solve the core issue, it has provided a stable baseline. I can now move forward with confidence to test whether variables like overtraining can help close the performance gap.

*阅读本系列的下一篇文章：* [过度训练有帮助吗？](https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-3-overtraining)

> *Read the next post in this series:* [Does overtraining help?](https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-3-overtraining)
