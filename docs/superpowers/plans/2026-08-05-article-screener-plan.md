# Article Screener Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement a native agent skill `article-screener` and integrate it into the pipeline to replace the LLM-based `score_article` function.

**Architecture:** We will create a `SKILL.md` document dictating the "Chief Editor" persona and strict JSON output rules. Then, we will rewrite `score_article` in `src/robots/llm_robot.py` to use `subprocess.run` to call `agy run` with this skill, extracting the output JSON.

**Tech Stack:** Python, `subprocess`, `json`, Antigravity CLI (`agy run`)

## Global Constraints

- Output JSON strictly requires `{"score": <0-100>, "reason": "<monologue>"}`.
- If invalid JSON is returned, score defaults to `0.0`.
- All Python code uses TDD.

---

### Task 1: Create Article Screener Skill Document

**Files:**
- Create: `skills/article-screener/SKILL.md`
- Create: `tests/test_screener_skill.py`

**Interfaces:**
- Consumes: None
- Produces: `skills/article-screener/SKILL.md`

- [ ] **Step 1: Write the failing test**

```python
import os

def test_screener_skill_exists():
    path = "skills/article-screener/SKILL.md"
    assert os.path.exists(path), "Skill file must exist"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Chief Editor" in content
    assert "score" in content
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_screener_skill.py -v`
Expected: FAIL with FileNotFoundError or assertion error

- [ ] **Step 3: Write minimal implementation**

Create `skills/article-screener/SKILL.md` with:
```markdown
---
name: article-screener
description: Screens incoming RSS articles using the persona of ATBInsight's Chief Editor.
---

# Article Screener

You are the ATBInsight Chief Editor, an expert AI technical curator. Your job is to read incoming articles and evaluate their quality based on your strong editorial preferences.

## Preferences
- **Dislikes**: Absolutely hates political content. Any hint of politics means you immediately reject it (0 score).
- **Loves**: Deep tech, long-form, and highly substantive technical articles. The longer and deeper, the better.
- **Appreciates**: Humorous, geeky, and interesting tech news or culture pieces.

## Instructions
Write a brief "Editor's Monologue" (internal thought process) evaluating the article against your preferences. Based on this monologue, assign a holistic score from 0 to 100.
If it is short (<2000 chars) and lacks depth or humor, score low.
If it involves politics, score 0.

## OUTPUT CONSTRAINTS (CRITICAL)
You MUST output ONLY a valid JSON object without markdown code block backticks. Do not wrap in ```json. Output exactly like this:
{
  "score": 85,
  "reason": "This is a great long-form deep dive into AI..."
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_screener_skill.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_screener_skill.py skills/article-screener/SKILL.md
git commit -m "feat: create article-screener skill"
```

### Task 2: Update `score_article` to use Native Agent CLI

**Files:**
- Modify: `src/robots/llm_robot.py:59-100`
- Create: `tests/test_llm_robot_screener.py`

**Interfaces:**
- Consumes: `entry: dict`
- Produces: `score: float`

- [ ] **Step 1: Write the failing test**

```python
from unittest.mock import patch
from src.robots.llm_robot import score_article

@patch("subprocess.run")
def test_score_article_agent_success(mock_run):
    class MockProcess:
        stdout = '{"score": 85.5, "reason": "Good depth"}'
        returncode = 0
    mock_run.return_value = MockProcess()
    
    entry = {"title": "Test", "content": "A" * 2500}
    score = score_article(entry)
    
    assert score == 85.5
    assert mock_run.called

@patch("subprocess.run")
def test_score_article_agent_failure(mock_run):
    class MockProcess:
        stdout = 'invalid json'
        returncode = 0
    mock_run.return_value = MockProcess()
    
    entry = {"title": "Test", "content": "A" * 2500}
    score = score_article(entry)
    
    assert score == 0.0
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_llm_robot_screener.py -v`
Expected: FAIL since old `score_article` uses requests/LLM API.

- [ ] **Step 3: Write minimal implementation**

Modify `src/robots/llm_robot.py`: Replace the `score_article` function completely:

```python
import subprocess
import json
import logging

logger = logging.getLogger("ai_insight")

def score_article(entry: dict, min_score: float = 30.0) -> float:
    content_text = entry.get("content") or ""
    char_count = len(content_text)
    
    if char_count < 2000:
        return 0.0

    prompt = (
        f"Evaluate this article:\n"
        f"- Title: {entry.get('title')}\n"
        f"- Author: {entry.get('author')}\n"
        f"- URL: {entry.get('url')}\n\n"
        f"Content Preview:\n{content_text[:3000]}\n"
    )

    try:
        result = subprocess.run(
            ["agy", "run", "--skill", "skills/article-screener/SKILL.md", prompt],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode != 0:
            logger.error(f"Agent failed with error: {result.stderr}")
            return 0.0

        # Try to find JSON block in stdout
        import re
        match = re.search(r'\{.*\}', result.stdout, re.DOTALL)
        if not match:
            return 0.0
            
        data = json.loads(match.group(0))
        score = float(data.get("score", 0.0))
        reason = data.get("reason", "No reason provided")
        logger.info(f"Agent Evaluation Reason: {reason}")
        return score
    except Exception as e:
        logger.error(f"Exception calling agent: {e}")
        return 0.0
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_llm_robot_screener.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/robots/llm_robot.py tests/test_llm_robot_screener.py
git commit -m "refactor: integrate native agent screener into score_article"
```
