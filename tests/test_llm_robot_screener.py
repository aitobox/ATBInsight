import pytest
from unittest.mock import patch
from src.robots.llm_robot import score_article

@patch("src.robots.llm_robot._chat_completion_with_fallback")
def test_score_article_agent_success(mock_chat):
    mock_chat.return_value = 'Here is my evaluation:\n```json\n{"score": 85.5, "reason": "Good depth"}\n```\n'
    
    entry = {"title": "Test", "content": "A" * 2500}
    score = score_article(entry)
    
    assert score == 85.5
    assert mock_chat.called

@patch("src.robots.llm_robot._chat_completion_with_fallback")
def test_score_article_agent_failure(mock_chat):
    mock_chat.return_value = 'invalid json'
    
    entry = {"title": "Test", "content": "A" * 2500}
    score = score_article(entry)
    
    assert score == 0.0
