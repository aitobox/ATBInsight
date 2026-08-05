# Article Screener Skill Design

## Overview
This design outlines the creation of a new Antigravity native skill (`article-screener`) to replace the existing direct LLM API scoring mechanism in `scripts/article_ingestor.py`. The new approach leverages the native agent's capability to understand nuances through a persona-driven heuristic evaluation.

## 1. Skill Definition (`skills/article-screener/SKILL.md`)

### Persona
The agent will act as the "ATBInsight Chief Editor".
- **Dislikes**: Absolutely hates political content. Any hint of politics results in an immediate veto (0 score).
- **Loves**: Deep tech, long-form, and highly substantive technical articles.
- **Appreciates**: Humorous, geeky, and interesting tech news or culture pieces.

### Evaluation Mechanism
Instead of rigid formulas, the agent will rely on its persona to write a short "Editor's Monologue" (internal thought process) evaluating the article against its preferences. Based on this monologue, it assigns a holistic score from 0 to 100.

### Output Constraints
To ensure the Python pipeline can parse the result reliably, the agent MUST output ONLY a valid JSON object without markdown code block backticks.
Format:
```json
{
  "score": <0-100>,
  "reason": "<editor's monologue>"
}
```

## 2. Integration Pipeline (`scripts/article_ingestor.py`)

### Modification to `score_article`
The existing `score_article` function in `src/robots/llm_robot.py` (or moved to a new robot module) will be updated:
1. **Remove HTTP API Calls**: Strip out `requests.post` to OpenAI-compatible endpoints.
2. **Subprocess Call**: Use `subprocess.run` to execute:
   `agy run --skill skills/article-screener/SKILL.md "Evaluate this article: [Metadata + Content]"`
3. **JSON Extraction**: Use regex to extract the first valid JSON block from `stdout`.
4. **Error Handling**: If `agy run` fails, times out, or returns invalid JSON, log the error and default the score to 0.0.

### Logging
The ingestor will log both the numerical `score` and the extracted `reason` to provide clear visibility into the agent's decision-making process for each article.

## Out of Scope
- Modifying the RSS fetcher (`miniflux_robot.py`).
- Changing the subsequent markdown refinement or image localization steps.
