import os
import yaml

def test_mkdocs_config_and_index_exist():
    assert os.path.exists("zensical.toml")
    assert os.path.exists("docs/index.md")
    with open("zensical.toml", "r", encoding="utf-8") as f:
        config_content = f.read()
    assert "site_name" in config_content

def test_header_override_contains_rss():
    header_path = "overrides/partials/header.html"
    assert os.path.exists(header_path)
    with open(header_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "/rss.xml" in content
    assert "RSS 订阅" in content

