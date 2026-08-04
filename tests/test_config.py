import os
import tempfile
import pytest
from src.config import load_config


def test_load_default_config():
    cfg = load_config("etc/ai_insight_pipeline.yaml")
    assert cfg["name"] == "AI Weekly News Pipeline"
    assert "steps" in cfg
    assert isinstance(cfg["steps"], list)
    assert len(cfg["steps"]) > 0


def test_env_var_expansion(monkeypatch):
    monkeypatch.setenv("TEST_ENV_VAR", "custom_value")
    
    yaml_content = """
    name: Test Config
    val1: "${TEST_ENV_VAR:default1}"
    val2: "${UNSET_ENV_VAR:default2}"
    val3: "${UNSET_ENV_VAR_NO_DEFAULT}"
    """
    
    with tempfile.NamedTemporaryFile("w+", suffix=".yaml", delete=False) as f:
        f.write(yaml_content)
        f.flush()
        temp_path = f.name

    try:
        cfg = load_config(temp_path)
        assert cfg["name"] == "Test Config"
        assert cfg["val1"] == "custom_value"
        assert cfg["val2"] == "default2"
        assert cfg["val3"] == ""
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_config("non_existent_config.yaml")
