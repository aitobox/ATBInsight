# Why do OpenAI's GPT-2 weights beat mine?

### Summary
After training an LLM from scratch, the author encountered a persistent mystery: despite achieving competitive cross-entropy loss on technical benchmarks, their models consistently underperformed compared to OpenAI’s original GPT-2 weights in instruction-following tasks. This post explores the potential causes—ranging from loss landscape geometry and data quality to the effects of "overtraining"—and outlines the experimental path taken to solve this performance gap.

---

## More on the Mystery
The author’s "IFT eval" (Instruction Fine-Tuning evaluation) uses the Alpaca dataset to test model performance. When comparing custom models against OpenAI’s GPT-2 weights, a clear discrepancy emerges:

| Model | Test Loss | IFT Epochs | IFT Score | IFT Rank |
| :--- | :--- | :--- | :--- | :--- |
| **OpenAI: Medium** | **3.23** | **2** | **41.62** | **1** |
| JAX (MHA bias, no dropout) | 3.42 | 4 | 19.25 | 4 |
| **OpenAI: Small** | **3.50** | **2** | **26.73** | **2** |
| Cloud FineWeb (8x A100 40GB) | 3.67 | 7 | 20.71 | 3 |

The OpenAI weights consistently outperform the author's models, even when the author's models achieve lower test loss. Notably, the OpenAI models reach their optimal fine-tuning point in only two epochs, suggesting they start from a more advantageous position in the parameter space.

## The Loss Landscape
The author hypothesizes that the "pre-training" phase determines the starting point in the model's loss landscape. 
*   **The Intuition:** If we view the loss landscape as a high-dimensional surface, a "good" pre-trained model lands in a valley that is also close to a low-loss region for instruction-following.
*   **The Gap:** While modern LLMs rely on this pre-train-then-fine-tune paradigm, the author’s models—trained on FineWeb—seem to land in valleys that are less "transferable" to instruction-following tasks than those discovered by OpenAI’s original training process.

## OpenAI Weights: Better Than We Thought
The author notes that OpenAI’s weights are not only high-performing but also structurally different due to **weight tying**, which makes their "small" model effectively smaller than the author's 163M parameter models. 

The author uses a trail-runner analogy: if a newcomer (the OpenAI model) runs a race on an unfamiliar forest route (the FineWeb test set) and still beats the locals (the custom models), it suggests the newcomer possesses superior inherent capability.

## Investigating Potential Causes
The author systematically evaluates potential reasons for the performance gap:

*   **Dropout:** Initially suspected as a way to improve generalization, dropout was tested in a JAX training run but resulted in poor IFT performance, leading the author to deprioritize it.
*   **Data Quality:** OpenAI’s WebText was curated using Reddit karma as a heuristic for quality. While the author’s FineWeb-Edu models showed promise, data quality alone does not fully explain the performance delta.
*   **Overtraining:** The author’s current models follow the "Chinchilla-optimal" heuristic (20 tokens per parameter). However, GPT-2 was likely trained on significantly more data. The author posits that "overtraining" (training beyond Chinchilla limits) might be the key to closing the gap.

## Next Steps
The author has inaugurated a dedicated training box, `poppy`, to test the hypothesis that overtraining will improve instruction-following performance. 

*Stay tuned for the next post in this series, where the author explores the results of these overtraining experiments.*

---
*Footnotes:*
1. *Modern production LLMs often incorporate Reinforcement Learning (RLHF), which differs from the standard cross-entropy fine-tuning used here.*
2. *The loss landscape is technically a high-dimensional hypersurface.*
3. *The author draws parallels to the "overlaid worlds" found in fantasy literature like Philip Pullman’s "His Dark Materials."*
4. *The OpenAI Medium model is excluded from the primary 15-model comparison as an "Olympic-level" outlier.*
5. *While the GPT-2 paper cites 117M parameters, the released weights align closer to 124M.*