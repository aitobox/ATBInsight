# Who’s Afraid of Chinese Models?

> **Summary:** A discussion on Ben Thompson’s proposal for U.S. copyright reform regarding AI model training and distillation, Alibaba’s open-weights release of the massive Qwen 3.8 Max model following geopolitical shifts, and a delightful look at the model's reasoning process while generating vector art. 
> 
> *Via [John Gruber](https://daringfireball.net/linked/2026/07/20/thompson-chinese-models-distillation)*

---

## 🏛️ Policy, Distillation, and Fair Use

In a recent [Stratechery article](https://stratechery.com/2026/whos-afraid-of-chinese-models/), Ben Thompson highlights the hypocrisy of top AI labs that outlaw model distillation via terms of service despite having trained their own models on unlicensed data. To level the playing field and help U.S. open models compete with global counterparts, Thompson proposes a clear legislative solution:

> "The U.S. should pass a law that (1) makes explicit that collecting data for training models is fair use, and (2) bars terms of service that forbid distillation, for U.S. companies at a minimum. Stopping distillation — which is nearly officially just querying the API — is nearly impossible; the U.S. should go the other way and lean into a new copyright policy that both indemnifies the labs and also guarantees that what they learned fuels further innovation for everyone else."

---

## 🇨🇳 The Shift in Chinese Open Source Strategy

Thompson also theorizes about Alibaba’s strategic reversal. After choosing *not* to release [Qwen 3.7 Max](https://qwen.ai/blog?id=qwen3.7) in May, Alibaba surprised the industry by releasing **[Qwen 3.8 Max](https://twitter.com/Alibaba_Qwen/status/2078759124914098291)** as an open-weights model. 

This pivot may have been heavily influenced by a [recent speech by Xi Jinping](http://english.scio.gov.cn/topnews/2026-07/18/content_118605932.html), in which he stated:

> *"We should seize this rare, historic opportunity to encourage open source, openness, collaboration and sharing."*

---

## 🎨 Inside the Mind of Qwen 3.8 Max

Qwen 3.8 Max is a massive 2.4-trillion-parameter model (nearly rivaling the 2.8T Kimi K3). To showcase its capabilities, Simon Willison shared a [pelican illustration](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F735f2cf19b795517cb2ff6cae1c71c64) generated entirely by the model:

> **Generated Description:**  
> *Flat vector cartoon illustration of a white pelican with a large orange beak and pouch riding a red bicycle, its orange legs on the pedals, against a light blue sky with a yellow sun top right and a white cloud top left, with horizontal motion lines behind the bike and a pale green ground strip at the bottom.*

```
[ Illustration Placeholder: White pelican riding a red bicycle ]
```

Perhaps most charmingly, a peek inside the model's extensive reasoning trace revealed the meticulous creative decisions being made behind the scenes:
* *"Could add helmet? No."*
* *"Maybe add small bell? no."*
* *"Need maybe add small fish in basket? Not necessary."*

---

### 🏷️ Tags
`ai` | `generative-ai` | `llms` | `training-data` | `qwen` | `pelican-riding-a-bicycle` | `ai-ethics` | `llm-release` | `ai-in-china`