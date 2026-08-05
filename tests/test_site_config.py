import os
import yaml

def test_mkdocs_config_and_index_exist():
    assert os.path.exists("zensical.toml")
    assert os.path.exists("docs/index.md")
    with open("zensical.toml", "r", encoding="utf-8") as f:
        config_content = f.read()
    assert "site_name" in config_content
