import os
import yaml

def test_mkdocs_config_and_index_exist():
    assert os.path.exists("mkdocs.yml")
    assert os.path.exists("docs/index.md")
    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    assert config["site_name"] == "ATBInsight"
    assert "blog" in [p if isinstance(p, str) else list(p.keys())[0] for p in config.get("plugins", [])]
