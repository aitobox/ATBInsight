import os
import re
import requests
from dotenv import load_dotenv


def _get_llm_config():
    load_dotenv()
    api_base = os.getenv("NEWAPI_URL") or os.getenv("LLM_API_BASE") or "https://api.openai.com/v1"
    if not api_base.endswith("/v1"):
        api_base = f"{api_base.rstrip('/')}/v1"
    api_key = os.getenv("NEWAPI_KEY") or os.getenv("LLM_API_KEY") or ""
    raw_model = os.getenv("NEWAPI_MODEL") or os.getenv("LLM_MODEL") or "gpt-4o-mini"
    model = raw_model.split(",")[0].strip()
    return api_base, api_key, model


def score_article(entry: dict, min_score: float = 30.0) -> float:
    api_base, api_key, model = _get_llm_config()

    content_text = entry.get("content") or ""
    prompt = (
        f"Evaluate article quality and AI relevance (0-100). "
        f"Output format SCORE: <number>.\n"
        f"Title: {entry.get('title')}\n"
        f"Content: {content_text[:1000]}"
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
    }
    resp = requests.post(
        f"{api_base.rstrip('/')}/chat/completions",
        json=payload,
        headers=headers,
        timeout=30,
    )
    resp.raise_for_status()
    content = resp.json()["choices"][0]["message"]["content"]
    match = re.search(r"SCORE:\s*(\d+(\.\d+)?)", content)
    return float(match.group(1)) if match else 0.0


def refine_markdown(entry: dict) -> str:
    api_base, api_key, model = _get_llm_config()

    content_text = entry.get("content") or ""
    prompt = (
        f"Convert and polish the following content into elegant Markdown with a summary and proper headings:\n"
        f"Title: {entry.get('title')}\n"
        f"Content: {content_text}"
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
    }
    resp = requests.post(
        f"{api_base.rstrip('/')}/chat/completions",
        json=payload,
        headers=headers,
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]

