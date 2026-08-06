import os
import glob
import yaml

def test_migrated_articles_frontmatter():
    posts = glob.glob("docs/blog/posts/*.md")
    if not posts:
        return
    for p in posts[:5]:
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        assert content.startswith("---")
        parts = content.split("---", 2)
        assert len(parts) >= 3
        fm = yaml.safe_load(parts[1])
        assert "title" in fm
        assert "date" in fm
        assert "authors" in fm
        assert "categories" in fm
        assert "tags" in fm
