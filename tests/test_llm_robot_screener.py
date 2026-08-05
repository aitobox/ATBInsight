import pytest
from unittest.mock import patch
from src.robots.llm_robot import score_article

@patch("subprocess.run")
def test_score_article_agent_success(mock_run):
    class MockProcess:
        stdout = '{"score": 85.5, "reason": "Good depth"}'
        returncode = 0
        stderr = ""
    mock_run.return_value = MockProcess()
    
    entry = {"title": "Test", "content": "A" * 2500}
    score = score_article(entry)
    
    assert score == 85.5
    assert mock_run.called

@patch("subprocess.run")
def test_score_article_agent_failure(mock_run):
    class MockProcess:
        stdout = 'invalid json'
        returncode = 0
        stderr = ""
    mock_run.return_value = MockProcess()
    
    entry = {"title": "Test", "content": "A" * 2500}
    score = score_article(entry)
    
    assert score == 0.0
