import os

def test_screener_skill_exists():
    path = "skills/article-screener/SKILL.md"
    assert os.path.exists(path), "Skill file must exist"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Chief Editor" in content
    assert "score" in content
