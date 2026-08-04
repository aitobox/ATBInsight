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
