import os

def test_daily_publisher_skill_exists():
    path = "skills/daily-publisher/SKILL.md"
    assert os.path.exists(path), "Skill file must exist"
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    assert "article_ingestor.py" in content, "Must call ingestor script"
    assert "bak/origin" in content, "Must instruct agent to use bak/origin path"
    assert "tech-article-translator" in content, "Must invoke translator skill"
    assert "zensical build" in content, "Must build site"
    assert "generate_indexes.py" in content, "Must call generate_indexes script"
    assert "git push origin main" in content, "Must push main branch to git"
