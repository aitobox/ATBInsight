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

def test_update_and_replace_entry(tmp_path):
    db_file = str(tmp_path / "test_replace.db")
    conn = init_db(db_file)

    mark_entry(conn, "entry-1", "Old Title", "http://example.com/1", 50.0, "pending")
    assert is_entry_processed(conn, "entry-1")

    # Update entry
    mark_entry(conn, "entry-1", "New Title", "http://example.com/1", 90.0, "processed", "path/to/doc.md")
    cur = conn.cursor()
    cur.execute("SELECT title, score, status, output_path FROM processed_entries WHERE entry_id = ?", ("entry-1",))
    row = cur.fetchone()
    assert row == ("New Title", 90.0, "processed", "path/to/doc.md")

def test_update_and_replace_image(tmp_path):
    db_file = str(tmp_path / "test_image_replace.db")
    conn = init_db(db_file)

    save_image_record(conn, "http://example.com/a.png", "local1.png", "hash1")
    assert is_image_downloaded(conn, "http://example.com/a.png") == "local1.png"

    # Update image record
    save_image_record(conn, "http://example.com/a.png", "local2.png", "hash2")
    assert is_image_downloaded(conn, "http://example.com/a.png") == "local2.png"

def test_init_db_default_path(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    default_db = tmp_path / "var" / "db" / "pipeline_cache.db"
    conn = init_db()
    assert default_db.exists()
    conn.close()
