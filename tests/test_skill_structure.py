import os


def test_tech_article_translator_skill_exists():
    path = "skills/tech-article-translator/SKILL.md"
    assert os.path.exists(path), f"{path} does not exist"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "name: tech-article-translator" in content
    assert "description: Use when" in content
    assert "bak/origin/" in content
    assert "HARD-GATE" in content
    assert "categories" in content
    assert "docs/blog/posts/" in content
    assert "科普" in content
    assert "直译" in content
    assert "问题诊断" in content
    assert "意译" in content
    assert "Transformer -> Transformer" in content
    assert "Token -> Token" in content
    assert "LLM / Large Language Model" in content
    assert "大语言模型" in content
    assert "Zero-shot" in content
    assert "零样本" in content
    assert "Few-shot" in content
    assert "少样本" in content
    assert "AI Agent" in content
    assert "AI 智能体" in content
    assert "AGI" in content
    assert "通用人工智能" in content





