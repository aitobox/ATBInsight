# Control the Ideas, Not the Code

> **Summary:** In an era where AI is rapidly transforming software development, seasoned developer (and Redis/DwarfStar creator) argues that focusing on line-by-line code review is becoming obsolete and suboptimal. Instead, developers must shift their focus toward **controlling the ideas, system design, and rigorous testing**. While traditionalists view AI reliance as a betrayal of the craft, this resistance is often ideological. The future of programming belongs to those who manage high-level architecture and intent, leaving the implementation details to intelligent agents.

---

## 1. The Motivation Behind the Message
Looking back at the history of this blog, I’ve been writing about programming with AI since early 2024. As a relatively well-regarded programmer—having published a prescient book in 2022 before ChatGPT even existed—I don't need to chase relevance. 

So why do I keep saying things people don't want to hear? Why do I continually announce the default future of programming? 

* **Easing the Transition:** I feel an urge to soften the blow for developers who are less prepared for this change, especially younger ones who didn't see this coming. 
* **Overcoming Imposter Syndrome:** Programmers feel increasingly disrupted by AI. They don't know if they are "betraying their field" by not writing every line by hand. 
* **The Core Trick:** By stepping forward and saying, *"Look, I can still write code, I’m not hiding behind AI,"* I want to normalize the reality that our field is evolving in an incredible, painful, yet joyful direction. It is not your weakness; it's simply a paradigm shift.

---

## 2. Why Looking at Code is Suboptimal
Yesterday on X, I stated that many programmers limit their impact because they spend too much time looking at the code. I truly believe this. This isn’t about lazy "vibe coding" or blindly asking an LLM for a final product. 

If you control the ideas of your software, pouring over the syntax itself is pointless for three major reasons:

1. **The Volume Problem:** Even accounting for LLM verbosity (often a symptom of poor prompting), you can now generate massive amounts of code. How are you realistically supposed to review 5,000 lines of code every day?
2. **Local vs. Global Optimization:** LLMs excel at writing locally optimal code, though they are still catching up with grand architectures. What is the point of scanning line-by-line? Instead, prompt your design, ask the LLM *"how does the design of this part actually work?"*, and evaluate if it serves the model. It is infinitely faster.
3. **Misallocated Time:** A workday is 8 hours. Spending it on manual code reading is a poor trade-off. You are neglecting the most important parts of your job: questioning the direction of the software, dreaming up new features, devising optimization tricks, and rigorous QA.

---

## 3. Beyond "Slop": The Reality of Modern Engineering
Remember the phrase *"Controlling the ideas"* from *The Mythical Man-Month*? A book from the 1970s teaches us more about our current era than anything said between 2000 and 2020. 

Why weren't people protesting AI this horrified by the sheer level of software "slop" we tolerated over the last decade? 

When building DwarfStar, I implemented inference for two LLMs completely through automation. You quickly discover you can’t just say *"implement XYZ"* and expect magic. You must understand how things work, engineer the best design, and chase performance. Comparing my implementations to other systems revealed that human-written codebases are full of subtle, accumulated errors—like broken attention implementations that degrade performance past certain context limits. 

The domain of fast-changing models and inference graphs is an unfair game for developers. Rigorous engineering on the *design side* and thorough testing far outperform hand-writing GPU kernels. Much of the resistance we see today is purely ideological.

---

## 4. The Redis Paradox: Why Manual Review is Dying
People often ask: *“Didn’t you say you check all the AI-generated code for Redis?”* 

Yes, I do. But at this point, I do it mostly out of habit and respect for users. With advanced models like Fable and GPT 5.6 Sol, human line-by-line review is increasingly pointless. 

When I make changes—such as implementing Redis Arrays or optimizing sorted sets for a 50% memory saving—I clean up the code because of my personal taste. However, if I had my hands entirely free, I wouldn't waste time on this. I would use that time for:
* Rigorous QA.
* Brainstorming and applying the next optimization.
* Using LLMs to write comprehensive `DESIGN.md` files describing every data structure, implementation trick, and architectural idea in human language.

In the future, a developer wanting to modify sorted sets won't dig through messy syntax; they will read the design, grasp the ideas, and instruct their agent with the correct mental model. **That is infinitely more useful than human code reviews.**

---

## 5. What About Young Programmers?
My only lingering doubt concerns young programmers who lack experience and struggle to build robust mental models. We don't yet know if deep manual coding is strictly required for them to learn, though they certainly need to learn how to write programs. 

However, checking raw LLM output is likely not the right training ground. It is far more valuable for them to learn a programming language by implementing a small interpreter, a simple database, or a hash table from scratch. 

Reviewing generic JavaScript boilerplate for a corporate website? Hell no—don't waste your time on that shit.

---

*[View original post and comments on antirez.com](http://antirez.com/news/169)*