import os
import re
import time
import requests
import subprocess
import json
import logging
from dotenv import load_dotenv

logger = logging.getLogger("ai_insight")

def _get_llm_config():
    load_dotenv()
    api_base = os.getenv("NEWAPI_URL") or os.getenv("LLM_API_BASE") or "https://api.openai.com/v1"
    if not api_base.endswith("/v1"):
        api_base = f"{api_base.rstrip('/')}/v1"
    api_key = os.getenv("NEWAPI_KEY") or os.getenv("LLM_API_KEY") or ""
    raw_model = os.getenv("NEWAPI_MODEL") or os.getenv("LLM_MODEL") or "gpt-4o-mini"
    models = [m.strip() for m in raw_model.split(",") if m.strip()]
    return api_base, api_key, models


def _chat_completion_with_fallback(
    messages: list[dict],
    temperature: float = 0.2,
    timeout: int = 30,
    backoff_delays: tuple[int, ...] = (8, 16, 32, 64),
) -> str:
    api_base, api_key, models = _get_llm_config()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    last_exception = None
    for model in models:
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }
        # First immediate attempt (delay=0), followed by configured backoff delays
        all_delays = (0,) + backoff_delays
        for delay in all_delays:
            if delay > 0:
                time.sleep(delay)
            try:
                resp = requests.post(
                    f"{api_base.rstrip('/')}/chat/completions",
                    json=payload,
                    headers=headers,
                    timeout=timeout,
                )
                resp.raise_for_status()
                return resp.json()["choices"][0]["message"]["content"]
            except Exception as e:
                last_exception = e
                continue

    if last_exception:
        raise last_exception
    raise RuntimeError("No valid LLM models configured or available.")


_CACHED_SCREENER_PROMPT = None

def load_screener_prompt(skill_path: str | None = None) -> str:
    """
    Dynamically loads the screener system prompt from skills/article-screener/SKILL.md
    as the Single Source of Truth (SSOT).
    """
    global _CACHED_SCREENER_PROMPT
    if _CACHED_SCREENER_PROMPT and not skill_path:
        return _CACHED_SCREENER_PROMPT

    candidate_paths = []
    if skill_path:
        candidate_paths.append(skill_path)

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    candidate_paths.extend([
        os.path.join(base_dir, "skills/article-screener/SKILL.md"),
        os.path.join(base_dir, ".agents/skills/article-screener/SKILL.md"),
        "skills/article-screener/SKILL.md",
        ".agents/skills/article-screener/SKILL.md",
    ])

    for p in candidate_paths:
        if os.path.isfile(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    text = f.read()
                if text.startswith("---"):
                    parts = text.split("---", 2)
                    if len(parts) >= 3:
                        text = parts[2].strip()
                if text:
                    if not skill_path:
                        _CACHED_SCREENER_PROMPT = text
                    return text
            except Exception as e:
                logger.warning(f"Failed to read skill prompt from {p}: {e}")

    # Robust fallback prompt if skill file is not found
    fallback = (
        "You are the ATBInsight Chief Editor, a world-class AI technical curator with extremely high standards. "
        "Strict Rejection Criteria (MUST Score 0): Digests/roundups, out-of-scope applied ML (agriculture, medical, materials), "
        "incremental paper fluff, commercial PR, superficial tutorials, and politics. "
        "Evaluate across Technical Depth (30%), Core Domain Relevance (30%), Engineering Value (25%), Originality (15%). "
        "Ingestion threshold is >= 70. Output ONLY valid JSON: "
        '{"score": 85, "verdict": "ACCEPT", "reason": "...", "breakdown": {"technical_depth": 26, "domain_relevance": 28, "engineering_value": 21, "originality": 10}}'
    )
    return fallback


def score_article(entry: dict) -> float:
    content_text = entry.get("content") or ""
    char_count = len(content_text)
    
    if char_count < 2000:
        return 0.0

    system_prompt = load_screener_prompt()

    # Smart sampling up to 8000 characters for deep engineering articles
    if char_count <= 8000:
        content_preview = content_text
    else:
        content_preview = (
            content_text[:5000]
            + "\n\n... [Middle content truncated for editorial evaluation] ...\n\n"
            + content_text[-3000:]
        )

    title = entry.get("title", "Untitled")
    author = entry.get("author", "Unknown")
    url = entry.get("url", "")
    is_arxiv = "arxiv.org" in url.lower() or "arxiv" in title.lower()
    type_hint = " [Academic / arXiv Entry]" if is_arxiv else " [Technical Blog / Article]"

    user_prompt = (
        f"Evaluate this article{type_hint}:\n"
        f"- Title: {title}\n"
        f"- Author: {author}\n"
        f"- URL: {url}\n"
        f"- Total Character Length: {char_count}\n\n"
        f"Content Preview:\n{content_preview}\n"
    )

    try:
        response_text = _chat_completion_with_fallback(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.1,
            timeout=25,
        )
        
        match = re.search(r'\{[\s\S]*\}', response_text)
        if not match:
            logger.warning(f"No JSON object found in screener response for '{title}'")
            return 0.0
            
        data = json.loads(match.group(0))
        score = float(data.get("score", 0.0))
        verdict = data.get("verdict", "ACCEPT" if score >= 70 else "REJECT")
        reason = data.get("reason", "No reason provided")
        breakdown = data.get("breakdown")
        logger.info(f"Chief Editor Verdict: [{verdict}] Score: [{score:.1f}/100.0] Breakdown: {breakdown} | Reason: {reason}")
        return score
    except Exception as e:
        logger.error(f"Exception evaluating article score: {e}")
        return 0.0


def refine_markdown(entry: dict) -> str:
    content_text = entry.get("content") or ""
    prompt = (
        f"Convert and polish the following content into elegant Markdown with a summary and proper headings:\n"
        f"Title: {entry.get('title')}\n"
        f"Content: {content_text}\n\n"
        f"CRITICAL INSTRUCTION: You MUST preserve all image links (e.g., ![...](./images/...) or <img ...>) and diagram code blocks exactly as they appear in the content. NEVER delete, omit, or modify image links!"
    )
    return _chat_completion_with_fallback([{"role": "user", "content": prompt}], temperature=0.3, timeout=60)


