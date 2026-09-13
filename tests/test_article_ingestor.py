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


def test_is_arxiv_entry():
    from scripts.article_ingestor import is_arxiv_entry
    assert is_arxiv_entry({"url": "https://arxiv.org/abs/2609.12345", "title": "Paper", "content": "..."})
    assert is_arxiv_entry({"url": "https://example.com/p", "title": "Analysis of arXiv:2609.12345", "content": "..."})
    assert is_arxiv_entry({"url": "https://example.com/p", "title": "Paper", "content": "Published on arxiv:2609..."})
    assert not is_arxiv_entry({"url": "https://blog.cloudflare.com/post", "title": "Postmortem", "content": "Kernel trace"})


@patch("scripts.article_ingestor.fetch_miniflux_entries")
@patch("scripts.article_ingestor.score_article")
@patch("scripts.article_ingestor.refine_markdown")
@patch("scripts.article_ingestor.localize_images")
def test_run_pipeline_arxiv_quota_top_3(mock_loc, mock_ref, mock_score, mock_fetch, tmp_path):
    # 5 arXiv papers and 1 normal engineering blog post, all qualifying with score >= 70
    entries = [
        {"id": "arxiv_1", "title": "arXiv Paper 1", "content": "Content 1", "url": "https://arxiv.org/abs/1"},
        {"id": "arxiv_2", "title": "arXiv Paper 2", "content": "Content 2", "url": "https://arxiv.org/abs/2"},
        {"id": "arxiv_3", "title": "arXiv Paper 3", "content": "Content 3", "url": "https://arxiv.org/abs/3"},
        {"id": "arxiv_4", "title": "arXiv Paper 4", "content": "Content 4", "url": "https://arxiv.org/abs/4"},
        {"id": "arxiv_5", "title": "arXiv Paper 5", "content": "Content 5", "url": "https://arxiv.org/abs/5"},
        {"id": "blog_1", "title": "Engineering Deep Dive", "content": "Blog content", "url": "https://blog.eng.com/deep"},
    ]
    mock_fetch.return_value = entries

    scores = {
        "arxiv_1": 75.0,
        "arxiv_2": 95.0,  # Top 1
        "arxiv_3": 85.0,  # Top 3
        "arxiv_4": 90.0,  # Top 2
        "arxiv_5": 72.0,
        "blog_1": 82.0,   # Non-arXiv, must be accepted
    }
    mock_score.side_effect = lambda e: scores[e["id"]]
    mock_ref.side_effect = lambda e: f"# Refined {e['id']}"
    mock_loc.side_effect = lambda c, d, conn: c

    db_path = str(tmp_path / "cache.db")
    out_dir = str(tmp_path / "docs" / "blog" / "posts")

    run_pipeline(db_path=db_path, output_dir=out_dir, target_date="2026-09-13", max_arxiv=3)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # The top 3 arXiv papers (arxiv_2=95, arxiv_4=90, arxiv_3=85) should be processed
    for approved_id in ["arxiv_2", "arxiv_4", "arxiv_3"]:
        cur.execute("SELECT status, score, output_path FROM processed_entries WHERE entry_id = ?", (approved_id,))
        row = cur.fetchone()
        assert row is not None, f"{approved_id} should be recorded"
        assert row[0] == "processed", f"{approved_id} should be processed"
        assert os.path.exists(row[2]), f"File for {approved_id} must exist"

    # Non-arXiv blog post must be processed regardless of arXiv quota
    cur.execute("SELECT status, score, output_path FROM processed_entries WHERE entry_id = 'blog_1'")
    row_blog = cur.fetchone()
    assert row_blog[0] == "processed"
    assert os.path.exists(row_blog[2])

    # The remaining 2 arXiv papers (arxiv_1=75, arxiv_5=72) should be skipped due to quota
    for exceeded_id in ["arxiv_1", "arxiv_5"]:
        cur.execute("SELECT status, score, output_path FROM processed_entries WHERE entry_id = ?", (exceeded_id,))
        row = cur.fetchone()
        assert row is not None, f"{exceeded_id} should be recorded in DB"
        assert row[0] == "skipped", f"{exceeded_id} should be skipped due to exceeding quota"
        assert row[2] == ""


