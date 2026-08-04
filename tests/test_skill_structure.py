import os


def test_tech_article_translator_skill_exists():
    path = "skills/tech-article-translator/SKILL.md"
    assert os.path.exists(path), f"{path} does not exist"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "name: tech-article-translator" in content
    assert "description: Use when" in content
    assert "bak/origin/" in content
