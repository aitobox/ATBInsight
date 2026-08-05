import os

def test_daily_publisher_skill_exists():
    path = "skills/daily-publisher/SKILL.md"
    assert os.path.exists(path), "Skill file must exist"
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    assert "article_ingestor.py" in content, "Must call ingestor script"
    assert "tech-article-translator" in content, "Must invoke translator skill"
    assert "zensical build" in content, "Must build site"
    assert "ghp-import" in content, "Must deploy to gh-pages"
