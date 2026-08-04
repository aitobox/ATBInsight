# Why do OpenAI's GPT-2 weights beat mine? Part two: The bugfix

### Summary
In my ongoing investigation into why my custom GPT-2 models underperform compared to OpenAI’s original weights on instruction-following tasks, I discovered a critical bug in my evaluation pipeline. While the fix didn't close the performance gap, it corrected my baseline metrics and provided a more reliable foundation for future experiments. This post details the technical oversight, the necessary code correction, and an analysis of the updated performance rankings.

---

## The Bug
My evaluation pipeline uses a "stop-early" mechanism based on validation loss. The intention was to save the model parameters from the last epoch where the validation loss was still decreasing.

The flaw was in how I handled the model state:
```python
# The buggy code
last_params = model.state_dict()
```
`model.state_dict()` returns a dictionary of **references** to the model's parameters, not a copy. Consequently, `last_params` was always pointing to the "live" parameters of the model, making the subsequent `model.load_state_dict(last_params)` a no-op.

**The Fix:**
I implemented `deepcopy` to ensure the parameters were correctly snapshotted:
```python
from copy import deepcopy
...
last_params = deepcopy(model.state_dict())
```
Additionally, I updated the evaluation script to use the full validation dataset rather than just the first five batches, ensuring a more robust assessment of model performance.

---

## A New Baseline
After re-running the evaluation with the corrected code, I generated a new set of rankings. While the OpenAI models remain at the top, the relative rankings of my own models shifted significantly.

| Model | New IFT Score | New IFT Rank |
| :--- | :--- | :--- |
| OpenAI weights: medium | 42.41 | 1 |
| OpenAI weights: small | 26.11 | 2 |
| JAX, no MHA bias, no dropout | 20.72 | 3 |
| Cloud FineWeb, 8x A100 40 GiB | 19.45 | 4 |
| JAX, with MHA bias, no dropout | 18.12 | 5 |

---

## Analysis of Results

### Training Epochs and Dropout
The "no MHA bias" models saw a significant performance boost, likely due to the combination of more comprehensive evaluation data and corrected dropout settings. Previously, I suspected my dropout configuration was inconsistent between the JAX training environment and the PyTorch evaluation script; I have now verified these settings are correctly aligned.

### The "Noise" of LLM-as-a-Judge
It is important to note that LLM-based evaluation is inherently noisy. A variation of 1–2 points is often within the margin of error. However, the *relative* ranking remains a useful indicator. The fact that some models dropped in rank suggests they may have been "benefiting" from the previous bug, perhaps by stopping at a point that happened to be favorable for the incomplete evaluation data.

### Conclusion
The mystery remains: OpenAI’s weights still outperform my models. While the bugfix didn't solve the core issue, it has provided a stable baseline. I can now move forward with confidence to test whether variables like overtraining can help close the performance gap.

*Read the next post in this series:* [Does overtraining help?](https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-3-overtraining)