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


def score_article(entry: dict) -> float:
    content_text = entry.get("content") or ""
    char_count = len(content_text)
    
    if char_count < 2000:
        return 0.0

    system_prompt = (
        "You are the ATBInsight Chief Editor, an expert AI technical curator. Your job is to read incoming articles and evaluate their quality based on your strong editorial preferences.\n"
        "Preferences:\n"
        "- Dislikes: Absolutely hates political content. Any hint of politics means you immediately reject it (0 score).\n"
        "- Loves: Deep tech, long-form, and highly substantive technical articles. The longer and deeper, the better.\n"
        "- Appreciates: Humorous, geeky, and interesting tech news or culture pieces.\n\n"
        "OUTPUT CONSTRAINTS (CRITICAL):\n"
        "You MUST output ONLY a valid JSON object without markdown code block backticks. Output exactly like this:\n"
        '{"score": 85, "reason": "This is a great long-form deep dive..."}'
    )

    user_prompt = (
        f"Evaluate this article:\n"
        f"- Title: {entry.get('title')}\n"
        f"- Author: {entry.get('author')}\n"
        f"- URL: {entry.get('url')}\n\n"
        f"Content Preview:\n{content_text[:3000]}\n"
    )

    try:
        response_text = _chat_completion_with_fallback(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.1,
            timeout=15,
        )
        
        match = re.search(r'\{.*?\}', response_text, re.DOTALL)
        if not match:
            return 0.0
            
        data = json.loads(match.group(0))
        score = float(data.get("score", 0.0))
        reason = data.get("reason", "No reason provided")
        logger.info(f"Chief Editor Evaluation Reason: {reason}")
        return score
    except Exception as e:
        logger.error(f"Exception evaluating article score: {e}")
        return 0.0


def refine_markdown(entry: dict) -> str:
    content_text = entry.get("content") or ""
    prompt = (
        f"Convert and polish the following content into elegant Markdown with a summary and proper headings:\n"
        f"Title: {entry.get('title')}\n"
        f"Content: {content_text}"
    )
    return _chat_completion_with_fallback([{"role": "user", "content": prompt}], temperature=0.3, timeout=60)


