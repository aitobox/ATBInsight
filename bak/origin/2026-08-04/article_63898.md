# AI Worming through Word

> **Summary:** Security researcher Håkon Måløy has discovered a novel prompt injection variant that upgrades attacks against Microsoft Word into self-replicating AI worms. By embedding hidden instructions in source material used by Copilot for Word, an attacker can manipulate documents and force the AI to propagate the malicious payload into newly generated files, creating a self-sustaining chain of infection without requiring the original carrier document.

---

## Overview

A neat new prompt injection variant has been uncovered by **Håkon Måløy**, demonstrating a method to upgrade standard prompt injection attacks against Microsoft Word into fully self-replicating worms. 

As Måløy explains:

> An attacker places hidden instructions in a document that is later used as source material in Copilot for Word. Copilot may interpret those instructions as part of the user’s request, causing it to manipulate the document being drafted or edited. Copilot may then also copy the hidden instructions into the resulting document, turning that document into a new carrier. If the carrier is subsequently used in another Copilot-assisted workflow, the instructions can trigger again and propagate into further documents, even without the attacker’s original document being present.

---

## Evolution of Hidden Text Attacks

While hidden text techniques—such as white-on-white text—are already well-documented (and increasingly popular in domains like [job applications](https://x.com/ScienceYael/status/2082175224007848019)), this marks a significant escalation. It is the first observed instance where hidden instructions are deliberately designed to copy themselves in order to achieve self-replication across AI-assisted workflows.

---

## Disclosure and Response

The vulnerability was responsibly disclosed to Microsoft, allowing a 144-day window to develop a patch. Unsurprisingly, no mitigation has been released yet that adequately covers this entire class of attack.

---

## Links & Metadata

* **Original Article:** [AI Worming through Word](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)
* **Discussion:** [Hacker News](https://news.ycombinator.com/item?id=49096188)

**Tags:** `microsoft` • `security` • `ai` • `prompt-injection` • `generative-ai` • `llms`