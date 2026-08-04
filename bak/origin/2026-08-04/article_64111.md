# Why do OpenAI's GPT-2 weights beat mine? Part 3: Testing Overtraining

### Summary
In this installment, the author investigates whether the superior performance of OpenAI’s original GPT-2 models on instruction fine-tuning (IFT) tasks is due to "overtraining"—training on significantly more data than the Chinchilla-optimal heuristic suggests. By training new models with extended token counts and multiple epochs, the author tests if this approach closes the performance gap. The results show a modest improvement in test loss, but the gains in instruction-following remain statistically insignificant, leaving the mystery of the OpenAI weights' performance largely unresolved.

---

## Overtraining vs. Overfitting
It is crucial to distinguish between these two concepts:
*   **Overfitting:** A failure where the model memorizes specific training data rather than learning general rules. It is almost always detrimental.
*   **Overtraining:** A judgment call regarding the compute budget. Following the *Chinchilla* paper, "optimal" training involves roughly 20 tokens per parameter. Overtraining implies exceeding this ratio. While often considered inefficient compared to scaling model size, it can still yield performance gains when parameter counts are constrained (e.g., for mobile deployment).

The author notes that GPT-2 was trained in 2019, well before the Chinchilla paper, and likely utilized multiple epochs over a smaller dataset, effectively "overtraining" by modern standards.

## The Experiments
To test if overtraining could replicate OpenAI's success, the author used their dedicated training box, `poppy`, to run two experiments:
1.  **Extended-train:** Training on 6.4B unique tokens (double the previous 3.2B baseline).
2.  **Two-epoch model:** Training on the standard 3.2B tokens, but repeating the dataset for a second epoch.

**Pre-experiment predictions:**
*   Both models would outperform existing models on test loss.
*   Both models would score better on IFT tests but still fall short of the original OpenAI GPT-2 small model.

## Results: The Extended-Train Model
Despite a minor `CUDA_ERROR_STREAM_CAPTURE_INVALIDATED` crash, the extended-train model completed successfully. 
*   **Test Loss:** The model achieved a loss of **3.324953**, significantly beating the previous Chinchilla-optimal baseline (3.418784) and coming close to the OpenAI medium model (3.231442).
*   **Generation:** Smoke tests confirmed the model remained coherent and functional.

## Results: The Two-Epoch Model
The two-epoch run completed without hardware issues.
*   **Test Loss:** The model achieved a loss of **3.326482**. 
*   **Comparison:** The performance was nearly identical to the "one long epoch" model, suggesting that the difference between the two methods is negligible.

## The IFT Test
The ultimate test was the Instruction Fine-Tuning (IFT) evaluation. Using an LLM-as-a-judge script, the author compared the new models against the existing lineup.

| Model | Test Loss | IFT Score |
| :--- | :--- | :--- |
| OpenAI weights: medium | 3.231442 | 42.91 |
| **JAX, overtrained one long epoch** | 3.324953 | 18.75 |
| **JAX, overtrained two normal epochs** | 3.326482 | 18.45 |
| OpenAI weights: small | 3.499677 | 25.66 |

The results were inconclusive. While the new models performed slightly better than the most similar baseline, the improvement was within the "noise" of the evaluation process. The models remained significantly worse than the original OpenAI GPT-2 small model.

## Conclusion
The hypothesis that simple overtraining explains the performance gap remains unproven. While the models showed improved test loss, they did not exhibit a breakthrough in instruction-following capability. The author concludes that while further training might eventually yield results, the current experiment suggests that overtraining is not a "silver bullet" for matching the performance of the original OpenAI weights. The author plans to pivot to other investigative avenues in future posts.