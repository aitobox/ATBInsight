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


@patch("time.sleep")
@patch("requests.post")
def test_backoff_retry_and_fallback(mock_post, mock_sleep):
    fail_resp = MagicMock()
    fail_resp.raise_for_status.side_effect = requests.exceptions.HTTPError("500 Internal Server Error")
    
    success_resp = MagicMock()
    success_resp.status_code = 200
    success_resp.json.return_value = {
        "choices": [{"message": {"content": "SCORE: 90"}}]
    }
    # Fail 5 times on model 1 (1 immediate + 4 backoffs: 8, 16, 32, 64), then succeed on model 2
    mock_post.side_effect = [fail_resp, fail_resp, fail_resp, fail_resp, fail_resp, success_resp]

    with patch.dict("os.environ", {"NEWAPI_MODEL": "model-1,model-2"}):
        score = score_article({"title": "Test Title", "content": "Raw content"})
        assert score == 90.0

    assert mock_sleep.call_count == 4
    mock_sleep.assert_has_calls([
        ((8,),),
        ((16,),),
        ((32,),),
        ((64,),),
    ])

