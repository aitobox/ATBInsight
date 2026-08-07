import os
import sqlite3
import yaml
from unittest.mock import patch
from scripts.article_ingestor import run_pipeline
from src.db import is_entry_processed


@patch("scripts.article_ingestor.fetch_miniflux_entries")
@patch("scripts.article_ingestor.score_article")
@patch("scripts.article_ingestor.refine_markdown")
@patch("scripts.article_ingestor.localize_images")
def test_run_pipeline(mock_loc, mock_ref, mock_score, mock_fetch, tmp_path):
    mock_fetch.return_value = [
        {"id": "1", "title": "Test AI", "content": "Content", "url": "http://test.com"}
    ]
    mock_score.return_value = 85.0
    mock_ref.return_value = "# Refined Markdown"
    mock_loc.return_value = "# Refined Localized"

    db_path = str(tmp_path / "cache.db")
    out_dir = str(tmp_path / "docs" / "blog" / "posts")
    run_pipeline(db_path=db_path, output_dir=out_dir)
    assert mock_fetch.called


@patch("scripts.article_ingestor.fetch_miniflux_entries")
@patch("scripts.article_ingestor.score_article")
@patch("scripts.article_ingestor.refine_markdown")
@patch("scripts.article_ingestor.localize_images")
def test_run_pipeline_skips_low_score_and_already_processed(
    mock_loc, mock_ref, mock_score, mock_fetch, tmp_path
):
    entries = [
        {"id": "101", "title": "High Score AI", "content": "Content 101", "url": "http://test101.com"},
        {"id": "102", "title": "Low Score AI", "content": "Content 102", "url": "http://test102.com"},
    ]
    mock_fetch.return_value = entries

    def score_side_effect(entry):
        if entry["id"] == "101":
            return 80.0
        return 20.0

    mock_score.side_effect = score_side_effect
    mock_ref.return_value = "# Refined Markdown 101"
    mock_loc.return_value = "# Localized Markdown 101"

    db_path = str(tmp_path / "cache.db")
    out_dir = str(tmp_path / "docs" / "blog" / "posts")

    # Run pipeline first time
    run_pipeline(db_path=db_path, output_dir=out_dir, target_date="2026-08-05")

    conn = sqlite3.connect(db_path)
    assert is_entry_processed(conn, "101")
    assert is_entry_processed(conn, "102")

    cur = conn.cursor()
    cur.execute("SELECT status, output_path FROM processed_entries WHERE entry_id = '101'")
    row101 = cur.fetchone()
    assert row101[0] == "processed"
    assert row101[1].endswith("article_101.md")
    assert os.path.exists(row101[1])
    with open(row101[1], "r", encoding="utf-8") as f:
        content = f.read()
        assert "# Refined Markdown 101" in content

    cur.execute("SELECT status, output_path FROM processed_entries WHERE entry_id = '102'")
    row102 = cur.fetchone()
    assert row102[0] == "skipped"
    assert row102[1] == ""

    # Second run should skip already processed entries without invoking score/refine again
    mock_score.reset_mock()
    mock_ref.reset_mock()
    run_pipeline(db_path=db_path, output_dir=out_dir, target_date="2026-08-05")
    mock_score.assert_not_called()
    mock_ref.assert_not_called()


@patch("requests.get")
def test_fetch_full_article_content(mock_get):
    from scripts.article_ingestor import fetch_full_article_content
    mock_resp = mock_get.return_value
    mock_resp.content = b"<html><body><article><p>Full original content paragraph.</p></article></body></html>"
    mock_resp.raise_for_status.return_value = None

    result = fetch_full_article_content("https://example.com/post")
    assert "Full original content paragraph" in result

