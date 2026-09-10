import pytest
from unittest.mock import patch, MagicMock
from src.robots.llm_robot import score_article, load_screener_prompt
from scripts.article_ingestor import process_single_entry

def test_load_screener_prompt():
    prompt = load_screener_prompt()
    assert "Chief Editor Persona" in prompt
    assert "Strict Rejection Criteria" in prompt
    assert "Technical Depth & Rigor" in prompt
    assert "Core Domain Relevance" in prompt
    assert "Engineering Value & Practical Insights" in prompt
    assert "Originality & Thinking Quality" in prompt
    assert "70" in prompt
    assert not prompt.startswith("---")  # Frontmatter should be stripped

@patch("src.robots.llm_robot._chat_completion_with_fallback")
def test_score_article_agent_success(mock_chat):
    mock_chat.return_value = '''{
      "score": 85.5,
      "verdict": "ACCEPT",
      "reason": "Outstanding technical deep dive into compiler architecture with flamegraphs.",
      "breakdown": {
        "technical_depth": 26,
        "domain_relevance": 28,
        "engineering_value": 21.5,
        "originality": 10
      }
    }'''
    
    entry = {"title": "Test Compiler Post", "content": "A" * 2500, "url": "https://example.com/compiler"}
    score = score_article(entry)
    
    assert score == 85.5
    assert mock_chat.called

@patch("src.robots.llm_robot._chat_completion_with_fallback")
def test_score_article_smart_sampling_and_arxiv(mock_chat):
    mock_chat.return_value = '{"score": 75.0, "verdict": "ACCEPT", "reason": "Good paper"}'
    
    long_content = "HEAD" * 2000 + "TAIL" * 1000  # > 8000 chars
    entry = {
        "title": "Novel Attention Architecture",
        "content": long_content,
        "url": "https://arxiv.org/abs/2609.12345"
    }
    score = score_article(entry)
    
    assert score == 75.0
    called_messages = mock_chat.call_args[1]["messages"]
    user_message = called_messages[1]["content"]
    assert "[Academic / arXiv Entry]" in user_message
    assert "Middle content truncated" in user_message

@patch("src.robots.llm_robot._chat_completion_with_fallback")
def test_score_article_agent_failure(mock_chat):
    mock_chat.return_value = 'invalid json'
    
    entry = {"title": "Test", "content": "A" * 2500}
    score = score_article(entry)
    
    assert score == 0.0

@patch("scripts.article_ingestor.score_article")
@patch("scripts.article_ingestor.init_db")
@patch("scripts.article_ingestor.is_entry_processed")
@patch("scripts.article_ingestor.mark_entry")
def test_process_single_entry_threshold_70(mock_mark, mock_cached, mock_init, mock_score):
    mock_conn = MagicMock()
    mock_init.return_value = mock_conn
    mock_cached.return_value = False
    
    # 65.0 is below the new 70.0 threshold
    mock_score.return_value = 65.0
    entry = {"id": "101", "title": "Borderline Post", "content": "B" * 2500, "url": "https://example.com/101"}
    
    status, score, reason = process_single_entry(entry, target_dir="/tmp/test", db_path="/tmp/test.db", threshold=70.0)
    assert status == "skipped"
    assert score == 65.0
    mock_mark.assert_called_with(mock_conn, "101", "Borderline Post", "https://example.com/101", 65.0, "skipped")

