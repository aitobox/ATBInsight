# Benchmarking Qwen 3.6 35B MoE (3B active) on an RTX 3090

## Summary
This post details a deep dive into running the **Qwen 3.6 35B Mixture-of-Experts (MoE)** model on an NVIDIA RTX 3090 (24GB VRAM). By leveraging `llama.cpp` and experimenting with CPU offloading (`-ncmoe`), I explored the trade-offs between context window size and inference speed. Key findings include:
* **CUDA vs. Vulkan:** Compiling `llama.cpp` with CUDA support significantly outperformed the default Vulkan build, providing higher throughput and larger context windows.
* **The "Sweet Spot":** Offloading 10–12 layers to the CPU allows the model to utilize its full 262k context window while maintaining usable speeds.
* **Performance:** On CUDA, I achieved ~140 tokens/s for generation and ~3,300 tokens/s for prompt processing with full GPU offload, dropping to ~85 tokens/s when offloading layers to reach full context.

---

## The Model: Qwen 3.6 35B-A3B
The Qwen 3.6 35B-A3B is a Mixture of Experts model with 35B total parameters but only 3B active parameters per token. Notably, over 1B of those active parameters are tied up in the embedding layer and output head, leaving only 2B for actual reasoning. Because the model requires keeping the full weight set in memory (approx. 22GB for 4-bit quantization), it pushes the 24GB VRAM limit of the RTX 3090, necessitating careful management of the context window.

## Getting Started: Llama.cpp
I initially encountered issues with the Arch Linux default Vulkan-based `llama.cpp` package, specifically "device does not support split buffers" errors. By adjusting parameters—specifically setting `-sm none` (since I am using a single GPU) and using `-ngl all`—I was able to stabilize the model.

## Benchmarking Methodology
To get accurate data, I automated the benchmarking process using `llama-server`. I tested varying levels of CPU offloading (`-ncmoe`) to see how many layers could be moved to system RAM before performance degraded unacceptably. I used a prompt based on the "Lem Test"—a challenging creative writing task—to ensure the model had to perform significant computation.

## The Results

### Context Window Scaling
Offloading layers to the CPU is the primary mechanism to reclaim VRAM for the context window.
* **Vulkan:** Required 12 layers offloaded to reach the full 262,144 context length.
* **CUDA:** Required only 10 layers offloaded to reach the same capacity.

### Throughput Comparison
CUDA consistently outperformed Vulkan across all metrics:

| Metric | Vulkan (All GPU) | CUDA (All GPU) |
| :--- | :--- | :--- |
| **Prompt Processing** | ~2,787 tok/s | ~3,360 tok/s |
| **Generation Speed** | ~122 tok/s | ~140 tok/s |

*Note: When offloading 12 layers to reach full context, CUDA maintained ~85 tok/s, while Vulkan dropped to ~66 tok/s.*

## Conclusion
Running a 35B MoE model on a 24GB card is a balancing act. While the RTX 3090 is constrained by its VRAM, the ability to offload FFN layers to the CPU via `llama.cpp` makes it entirely viable to run high-parameter models with massive context windows. For users on NVIDIA hardware, **compiling from source with CUDA support** is highly recommended over using generic Vulkan builds to maximize both speed and context capacity.

---

### Appendix: The Lem Test
The "Lem Test," popularized by Ethan Mollick, challenges an LLM to write a six-line poem about a haircut where every word begins with the letter "S," while maintaining a tragic, lofty tone. 

While the 35B Qwen model struggled to maintain perfect rhyme and the "S" constraint simultaneously, it produced surprisingly coherent narratives for a model with only 2B active "reasoning" parameters. It serves as an excellent stress test for both the model's reasoning capabilities and the hardware's throughput during high-token-count generation.