# AI Insight Pipeline & SQLite Caching Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an automated pipeline fetching RSS entries from Miniflux, filtering & refining them using LLM APIs, downloading images locally with link updates, and caching progress in SQLite (`var/db/pipeline_cache.db`).

**Architecture:** A modular Python pipeline driven by `etc/ai_insight_pipeline.yaml`. Modules include configuration loader, SQLite manager (`var/db/pipeline_cache.db`), Miniflux RSS fetcher, LLM scoring & refinement client, and an image downloader with link localizing parser.

**Tech Stack:** Python 3.10+, SQLite3, Requests, PyYAML, python-dotenv, pytest.

## Global Constraints

- Database file MUST be stored at `var/db/pipeline_cache.db`.
- Miniflux credentials and LLM API parameters MUST be loaded from `.env`.
- Pipeline step definitions MUST strictly follow `etc/ai_insight_pipeline.yaml`.
- Refined articles MUST be saved to `docs/insight/YYYY-MM-DD/<slug>.md`.
- Local images MUST be saved to `docs/insight/YYYY-MM-DD/images/<hash>.<ext>`.

---

### Task 1: SQLite Cache Manager

**Files:**
- Create: `src/db.py`
- Test: `tests/test_db.py`

**Interfaces:**
- Produces:
  - `init_db(db_path: str = "var/db/pipeline_cache.db") -> sqlite3.Connection`
  - `is_entry_processed(conn, entry_id: str) -> bool`
  - `mark_entry(conn, entry_id: str, title: str, url: str, score: float, status: str, output_path: str = "") -> None`
  - `is_image_downloaded(conn, original_url: str) -> str | None`
  - `save_image_record(conn, original_url: str, local_path: str, sha256: str) -> None`

- [ ] **Step 1: Write the failing test**

```python
import os
import pytest
from src.db import init_db, is_entry_processed, mark_entry, is_image_downloaded, save_image_record

def test_cache_db_operations(tmp_path):
    db_file = str(tmp_path / "test_cache.db")
    conn = init_db(db_file)

    assert not is_entry_processed(conn, "entry-123")
    mark_entry(conn, "entry-123", "Title", "http://example.com", 85.0, "processed", "docs/insight/2026-08-04/test.md")
    assert is_entry_processed(conn, "entry-123")

    assert is_image_downloaded(conn, "http://example.com/img.png") is None
    save_image_record(conn, "http://example.com/img.png", "./images/hash.png", "sha256hash")
    assert is_image_downloaded(conn, "http://example.com/img.png") == "./images/hash.png"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_db.py -v`
Expected: FAIL with ModuleNotFoundError or function definition errors.

- [ ] **Step 3: Write minimal implementation**

```python
import os
import sqlite3

def init_db(db_path: str = "var/db/pipeline_cache.db") -> sqlite3.Connection:
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS processed_entries (
                entry_id TEXT PRIMARY KEY,
                title TEXT,
                url TEXT,
                published_at TEXT,
                score REAL,
                status TEXT,
                output_path TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS downloaded_images (
                original_url TEXT PRIMARY KEY,
                local_path TEXT,
                sha256 TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    return conn

def is_entry_processed(conn: sqlite3.Connection, entry_id: str) -> bool:
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM processed_entries WHERE entry_id = ?", (entry_id,))
    return cur.fetchone() is not None

def mark_entry(conn: sqlite3.Connection, entry_id: str, title: str, url: str, score: float, status: str, output_path: str = "") -> None:
    with conn:
        conn.execute(
            "INSERT OR REPLACE INTO processed_entries (entry_id, title, url, score, status, output_path) VALUES (?, ?, ?, ?, ?, ?)",
            (entry_id, title, url, score, status, output_path)
        )

def is_image_downloaded(conn: sqlite3.Connection, original_url: str) -> str | None:
    cur = conn.cursor()
    cur.execute("SELECT local_path FROM downloaded_images WHERE original_url = ?", (original_url,))
    row = cur.fetchone()
    return row[0] if row else None

def save_image_record(conn: sqlite3.Connection, original_url: str, local_path: str, sha256: str) -> None:
    with conn:
        conn.execute(
            "INSERT OR REPLACE INTO downloaded_images (original_url, local_path, sha256) VALUES (?, ?, ?)",
            (original_url, local_path, sha256)
        )
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_db.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/db.py tests/test_db.py
git commit -m "feat: implement SQLite cache manager"
```

---

### Task 2: Config and Env Loader

**Files:**
- Create: `src/config.py`
- Test: `tests/test_config.py`

**Interfaces:**
- Consumes: `.env`, `etc/ai_insight_pipeline.yaml`
- Produces:
  - `load_config(config_path: str = "etc/ai_insight_pipeline.yaml") -> dict`

- [ ] **Step 1: Write the failing test**

```python
import os
from src.config import load_config

def test_load_config():
    cfg = load_config("etc/ai_insight_pipeline.yaml")
    assert cfg["name"] == "AI Weekly News Pipeline"
    assert "steps" in cfg
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_config.py -v`
Expected: FAIL

- [ ] **Step 3: Write minimal implementation**

```python
import os
import yaml
from dotenv import load_dotenv

def load_config(config_path: str = "etc/ai_insight_pipeline.yaml") -> dict:
    load_dotenv()
    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = os.path.expandvars(content)
    return yaml.safe_load(content)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_config.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/config.py tests/test_config.py
git commit -m "feat: add config and env loader"
```

---

### Task 3: Miniflux RSS Fetch Robot

**Files:**
- Create: `src/robots/miniflux_robot.py`
- Test: `tests/test_miniflux_robot.py`

**Interfaces:**
- Consumes: Miniflux API endpoint and credentials from `.env`
- Produces:
  - `fetch_miniflux_entries(url: str, username: str, password: str, days: int) -> list[dict]`

- [ ] **Step 1: Write the failing test**

```python
from unittest.mock import patch, MagicMock
from src.robots.miniflux_robot import fetch_miniflux_entries

@patch("requests.get")
def test_fetch_miniflux_entries(mock_get):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "entries": [{"id": 1, "title": "AI Insight Test", "content": "<p>Content</p>", "url": "http://example.com"}]
    }
    mock_get.return_value = mock_resp

    entries = fetch_miniflux_entries("http://mock-miniflux", "user", "pass", days=7)
    assert len(entries) == 1
    assert entries[0]["title"] == "AI Insight Test"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_miniflux_robot.py -v`
Expected: FAIL

- [ ] **Step 3: Write minimal implementation**

```python
import requests

def fetch_miniflux_entries(url: str, username: str, password: str, days: int = 7) -> list[dict]:
    api_url = f"{url.rstrip('/')}/v1/entries?status=read,unread"
    resp = requests.get(api_url, auth=(username, password), timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return data.get("entries", [])
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_miniflux_robot.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/robots/miniflux_robot.py tests/test_miniflux_robot.py
git commit -m "feat: add Miniflux RSS fetch robot"
```

---

### Task 4: LLM Filter & Refinement Robot

**Files:**
- Create: `src/robots/llm_robot.py`
- Test: `tests/test_llm_robot.py`

**Interfaces:**
- Consumes: OpenAI API key / base from `.env`
- Produces:
  - `score_article(entry: dict, min_score: float = 30.0) -> float`
  - `refine_markdown(entry: dict) -> str`

- [ ] **Step 1: Write the failing test**

```python
from unittest.mock import patch, MagicMock
from src.robots.llm_robot import score_article, refine_markdown

@patch("requests.post")
def test_score_article(mock_post):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "choices": [{"message": {"content": "SCORE: 85"}}]
    }
    mock_post.return_value = mock_resp

    score = score_article({"title": "Test", "content": "Content"})
    assert score == 85.0
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_llm_robot.py -v`
Expected: FAIL

- [ ] **Step 3: Write minimal implementation**

```python
import os
import re
import requests

def score_article(entry: dict, min_score: float = 30.0) -> float:
    api_base = os.getenv("LLM_API_BASE", "https://api.openai.com/v1")
    api_key = os.getenv("LLM_API_KEY", "")
    model = os.getenv("LLM_MODEL", "gpt-4o-mini")

    prompt = f"Evaluate article quality and AI relevance (0-100). Output format SCORE: <number>.\nTitle: {entry.get('title')}\nContent: {entry.get('content')[:1000]}"
    
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }
    resp = requests.post(f"{api_base.rstrip('/')}/chat/completions", json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    content = resp.json()["choices"][0]["message"]["content"]
    match = re.search(r"SCORE:\s*(\d+(\.\d+)?)", content)
    return float(match.group(1)) if match else 0.0

def refine_markdown(entry: dict) -> str:
    api_base = os.getenv("LLM_API_BASE", "https://api.openai.com/v1")
    api_key = os.getenv("LLM_API_KEY", "")
    model = os.getenv("LLM_MODEL", "gpt-4o-mini")

    prompt = f"Convert and polish the following content into elegant Markdown with a summary and proper headings:\nTitle: {entry.get('title')}\nContent: {entry.get('content')}"
    
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }
    resp = requests.post(f"{api_base.rstrip('/')}/chat/completions", json=payload, headers=headers, timeout=60)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_llm_robot.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/robots/llm_robot.py tests/test_llm_robot.py
git commit -m "feat: add LLM scoring and markdown refinement robot"
```

---

### Task 5: Image Downloader & Markdown Localizer

**Files:**
- Create: `src/robots/image_robot.py`
- Test: `tests/test_image_robot.py`

**Interfaces:**
- Consumes: Markdown content, output date path
- Produces:
  - `localize_images(markdown_content: str, output_dir: str, conn) -> str`

- [ ] **Step 1: Write the failing test**

```python
from unittest.mock import patch, MagicMock
from src.db import init_db
from src.robots.image_robot import localize_images

@patch("requests.get")
def test_localize_images(mock_get, tmp_path):
    conn = init_db(str(tmp_path / "test.db"))
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.content = b"fake-image-bytes"
    mock_resp.headers = {"Content-Type": "image/png"}
    mock_get.return_value = mock_resp

    md = "Here is an image: ![test](http://example.com/test.png)"
    out_dir = str(tmp_path / "docs" / "insight" / "2026-08-04")
    
    new_md = localize_images(md, out_dir, conn)
    assert "./images/" in new_md
    assert "!(http://example.com/test.png)" not in new_md
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_image_robot.py -v`
Expected: FAIL

- [ ] **Step 3: Write minimal implementation**

```python
import os
import re
import hashlib
import requests
from src.db import is_image_downloaded, save_image_record

def localize_images(markdown_content: str, output_dir: str, conn) -> str:
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    img_urls = re.findall(r'!\[.*?\]\((https?://[^\)]+)\)', markdown_content)
    img_urls += re.findall(r'<img[^>]+src=["\'](https?://[^"\']+)["\']', markdown_content)

    for url in set(img_urls):
        cached_path = is_image_downloaded(conn, url)
        if cached_path:
            markdown_content = markdown_content.replace(url, cached_path)
            continue

        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                sha256 = hashlib.sha256(resp.content).hexdigest()[:12]
                ext = "png" if "png" in resp.headers.get("Content-Type", "") else "jpg"
                filename = f"{sha256}.{ext}"
                local_file_path = os.path.join(images_dir, filename)
                
                with open(local_file_path, "wb") as f:
                    f.write(resp.content)
                
                rel_path = f"./images/{filename}"
                save_image_record(conn, url, rel_path, sha256)
                markdown_content = markdown_content.replace(url, rel_path)
        except Exception:
            pass

    return markdown_content
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_image_robot.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/robots/image_robot.py tests/test_image_robot.py
git commit -m "feat: add image downloader and link localizer"
```

---

### Task 6: Main Pipeline Runner Integration

**Files:**
- Create: `src/main.py`
- Test: `tests/test_main.py`

**Interfaces:**
- Consumes: Config, DB, Miniflux, LLM, Image localizer
- Produces: CLI execution `python -m src.main`

- [ ] **Step 1: Write the failing test**

```python
from unittest.mock import patch
from src.main import run_pipeline

@patch("src.main.fetch_miniflux_entries")
@patch("src.main.score_article")
@patch("src.main.refine_markdown")
@patch("src.main.localize_images")
def test_run_pipeline(mock_loc, mock_ref, mock_score, mock_fetch, tmp_path):
    mock_fetch.return_value = [{"id": "1", "title": "Test AI", "content": "Content", "url": "http://test.com"}]
    mock_score.return_value = 85.0
    mock_ref.return_value = "# Refined Markdown"
    mock_loc.return_value = "# Refined Localized"

    db_path = str(tmp_path / "cache.db")
    out_dir = str(tmp_path / "docs" / "insight")
    run_pipeline(db_path=db_path, output_dir=out_dir)
    assert mock_fetch.called
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_main.py -v`
Expected: FAIL

- [ ] **Step 3: Write minimal implementation**

```python
import os
import datetime
from src.config import load_config
from src.db import init_db, is_entry_processed, mark_entry
from src.robots.miniflux_robot import fetch_miniflux_entries
from src.robots.llm_robot import score_article, refine_markdown
from src.robots.image_robot import localize_images

def run_pipeline(config_path: str = "etc/ai_insight_pipeline.yaml", db_path: str = "var/db/pipeline_cache.db", output_dir: str = "docs/insight"):
    cfg = load_config(config_path)
    conn = init_db(db_path)

    miniflux_cfg = cfg["steps"][0]["config"]
    entries = fetch_miniflux_entries(
        url=os.getenv("MINIFLUX_URL", miniflux_cfg.get("url")),
        username=os.getenv("MINIFLUX_USERNAME", miniflux_cfg.get("username")),
        password=os.getenv("MINIFLUX_PASSWORD", miniflux_cfg.get("password")),
        days=miniflux_cfg.get("days", 7)
    )

    date_str = datetime.date.today().strftime("%Y-%m-%d")
    target_dir = os.path.join(output_dir, date_str)

    for entry in entries:
        entry_id = str(entry.get("id"))
        if is_entry_processed(conn, entry_id):
            continue

        score = score_article(entry)
        if score < 30.0:
            mark_entry(conn, entry_id, entry.get("title"), entry.get("url"), score, "skipped")
            continue

        refined_md = refine_markdown(entry)
        localized_md = localize_images(refined_md, target_dir, conn)

        os.makedirs(target_dir, exist_ok=True)
        slug = f"article_{entry_id}.md"
        filepath = os.path.join(target_dir, slug)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(localized_md)

        mark_entry(conn, entry_id, entry.get("title"), entry.get("url"), score, "processed", filepath)

if __name__ == "__main__":
    run_pipeline()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_main.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/main.py tests/test_main.py
git commit -m "feat: assemble main pipeline runner"
```
