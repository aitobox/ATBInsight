import os
import re
import time
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


def score_article(entry: dict, min_score: float = 30.0) -> float:
    content_text = entry.get("content") or ""
    author = entry.get("author") or ""
    feed_title = ""
    if isinstance(entry.get("feed"), dict):
        feed_title = entry.get("feed", {}).get("title") or ""
    
    char_count = len(content_text)
    
    prompt = (
        "You are an expert AI technical curator. Evaluate the quality of the following AI article and assign a final score from 0 to 100.\n"
        "Strictly adhere to the following scoring dimensions and weights:\n\n"
        "1. Content Depth & Length (30%):\n"
        "   - Longer, in-depth technical documents/analysis deserve HIGHER scores.\n"
        "   - Extremely short posts (< 300 words) or superficial summaries should receive lower scores.\n\n"
        "2. Conciseness & Structure (30%):\n"
        "   - Clear, concise, well-structured articles without fluff, clickbait, or excessive marketing rhetoric deserve HIGHER scores.\n"
        "   - Direct, informative technical prose is highly favored.\n\n"
        "3. Author & Publication Reputation (20%):\n"
        "   - Submissions from well-known AI researchers, engineers, official company tech blogs (e.g. OpenAI, Anthropic, Google DeepMind, Meta AI) or reputable tech portals deserve HIGHER scores.\n\n"
        "4. AI Relevance & Technical Insight (20%):\n"
        "   - High relevance to AI architecture, LLM engineering, research papers, or practical system design.\n\n"
        f"Article Metadata:\n"
        f"- Title: {entry.get('title')}\n"
        f"- Author: {author}\n"
        f"- Publication Source: {feed_title}\n"
        f"- URL: {entry.get('url')}\n"
        f"- Character Count: {char_count}\n\n"
        f"Article Content Preview:\n"
        f"{content_text[:3000]}\n\n"
        "Output format required: output exactly 'SCORE: <number>' on a new line."
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


