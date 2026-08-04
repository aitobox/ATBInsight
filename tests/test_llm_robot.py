from unittest.mock import patch, MagicMock
import pytest
import requests
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
    mock_post.assert_called_once()


@patch("requests.post")
def test_score_article_no_match(mock_post):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "choices": [{"message": {"content": "Invalid output format"}}]
    }
    mock_post.return_value = mock_resp

    score = score_article({"title": "Test", "content": "Content"})
    assert score == 0.0


@patch("requests.post")
def test_refine_markdown(mock_post):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "choices": [{"message": {"content": "# Refined Title\n\nRefined content summary."}}]
    }
    mock_post.return_value = mock_resp

    refined = refine_markdown({"title": "Test Title", "content": "Raw content"})
    assert refined == "# Refined Title\n\nRefined content summary."
    mock_post.assert_called_once()
