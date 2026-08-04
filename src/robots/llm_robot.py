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
    models = [m.strip() for m in raw_model.split(",") if m.strip()]
    return api_base, api_key, models


def _chat_completion_with_fallback(messages: list[dict], temperature: float = 0.2, timeout: int = 30) -> str:
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


def score_article(entry: dict, min_score: float = 30.0) -> float:
    content_text = entry.get("content") or ""
    prompt = (
        f"Evaluate article quality and AI relevance (0-100). "
        f"Output format SCORE: <number>.\n"
        f"Title: {entry.get('title')}\n"
        f"Content: {content_text[:1000]}"
    )
    content = _chat_completion_with_fallback([{"role": "user", "content": prompt}], temperature=0.2, timeout=30)
    match = re.search(r"SCORE:\s*(\d+(\.\d+)?)", content)
    return float(match.group(1)) if match else 0.0


def refine_markdown(entry: dict) -> str:
    content_text = entry.get("content") or ""
    prompt = (
        f"Convert and polish the following content into elegant Markdown with a summary and proper headings:\n"
        f"Title: {entry.get('title')}\n"
        f"Content: {content_text}"
    )
    return _chat_completion_with_fallback([{"role": "user", "content": prompt}], temperature=0.3, timeout=60)


