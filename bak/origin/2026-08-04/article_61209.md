# Inkling: Our Open-Weights Model

## Summary
Thinking Machines Lab (founded by Mira Murati) has released **Inkling**, its first open-weights multimodal model. Licensed under Apache-2.0, Inkling is a Mixture-of-Experts (MoE) transformer featuring 975 billion total parameters (41 billion active) and trained on 45 trillion tokens of text, images, audio, and video. While not positioned as a frontier model, it serves as a strong, customizable base model optimized for fine-tuning via Thinking Machines' Tinker platform.

---

## Model Overview & Architecture

Inkling is an Apache-2.0 licensed multimodal model featuring:
* **Architecture:** Mixture-of-Experts (MoE) transformer
* **Parameters:** 975B total / 41B active
* **Training Data:** 45 trillion tokens spanning text, images, audio, and video

Thinking Machines has also announced **Inkling-Small**, a 276B parameter model (12B active), which is currently undergoing testing and will have its weights released upon completion.

---

## Documentation & Training Data

The official [model card](https://thinkingmachines.ai/model-card/inkling/) is notably concise compared to standard releases from major US AI labs. Similarly, the [Training Data Documentation](https://thinkingmachines.ai/training-data-documentation/) offers minimal specifics, summarizing its data sources as follows:

> The datasets Thinking Machines Lab uses to develop its AI services includes content that is in the public domain as well as content that may be subject to intellectual property protection.
> 
> Thinking Machines Lab’s services were developed using publicly available content obtained from the open internet and publicly accessible data repositories. Certain datasets were also obtained from third parties.

---

## Positioning & Fine-Tuning

By the lab's own admission, Inkling is not intended to be a top-tier frontier model. Instead, its value lies in its versatility:

> Inkling is not the strongest overall model available today, open or closed. Instead, a combination of qualities makes it a good open-weights base for customization: multimodal capabilities, efficient thinking, and availability on Tinker for fine-tuning.

This release strengthens the US open-weights ecosystem, providing a competitive alternative to models coming out of China, as well as established US offerings like NVIDIA Nemotron and Gemma 4.

---

## Hands-On Example: Generating an SVG

Inkling's capabilities can be tested via the Thinking Machines API. Below is an example using `curl` to prompt the model to generate an SVG of a pelican riding a bicycle:

```bash
curl "https://tinker.thinkingmachines.dev/services/tinker-prod/oai/api/v1/chat/completions" \
  -H "Authorization: Bearer $TINKER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "thinkingmachines/Inkling",
    "messages": [
      {"role": "user", "content": "Generate an SVG of a pelican riding a bicycle"}
    ],
    "stream": false
  }'
```

*(You can view the full API response [here](https://gist.github.com/simonw/8117ac4376371dd3fc2b5dbce27e0855).)*

### Multimodal Self-Analysis

To test its multimodal capabilities, the rendered image was converted to a JPEG and sent back to Inkling with a request to describe its own output:

```json
{
  "model": "thinkingmachines/Inkling",
  "messages": [{
    "role": "user",
    "content": [
      {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,$BASE_64_JPEG"}},
      {"type": "text", "text": "Describe this image in detail"}
    ]
  }],
  "stream": false
}
```

In [its full response](https://gist.github.com/simonw/dccebd0581f5c4056c5b0ca5bdc38cd9#reasoning_content)—mistaking its subject slightly for a stork or seagull—Inkling provided the following description:

> This is a cheerful, flat-vector cartoon illustration featuring a white bird riding a bicycle across a green landscape.
> 
> **The Bird:** The central figure is a stylized white bird—resembling a stork or seagull—with a plump, rounded body. It has a long, prominent orange beak that is slightly open, revealing a black line for the mouth. Its eye is small and black with a tiny white highlight. The bird has black wing and tail feathers with white edges, and thin orange legs ending in black feet that rest on the bicycle's orange pedals.
> 
> **The Bicycle:** The bike has a simple black frame with two large wheels featuring black tires, gray inner rims, and black spokes arranged in a cross pattern. The handlebars are black, and there are bright orange pedals attached to a black crank. A white seat is visible behind the bird's body.
> 
> **The Setting:** The scene is set against a clear, light blue sky. There are two fluffy white clouds—one on the left side and a smaller one near the bird's head on the right. A bright, solid yellow sun shines in the upper right corner. At the bottom, there are rolling green hills with a smooth, curved top edge where the bicycle rests.
> 
> The overall style is playful, simple, and colorful, with clean lines and a bright, sunny atmosphere.

---

*Via [Hacker News](https://news.ycombinator.com/item?id=48924912)*

**Tags:** [ai](https://simonwillison.net/tags/ai), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [training-data](https://simonwillison.net/tags/training-data), [pelican-riding-a-bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle), [llm-release](https://simonwillison.net/tags/llm-release)