import os
import re
import yaml
from dotenv import load_dotenv


def _expand_env_vars(content: str) -> str:
    """
    Expands environment variables in the format ${VAR:default} or ${VAR} or $VAR.
    If VAR is set in os.environ, its value is used.
    If VAR is not set and a default value is specified, the default value is used.
    If VAR is not set and no default value is specified, it expands to an empty string.
    """
    pattern = re.compile(r'\$\{([A-Za-z0-9_]+)(?::([^}]*))?\}')

    def replacer(match):
        var_name = match.group(1)
        default_val = match.group(2)
        if var_name in os.environ:
            return os.environ[var_name]
        elif default_val is not None:
            return default_val
        else:
            return ""

    expanded = pattern.sub(replacer, content)
    return os.path.expandvars(expanded)


def load_config(config_path: str = "etc/ai_insight_pipeline.yaml") -> dict:
    """
    Loads and parses YAML configuration file with environment variable expansion.
    """
    load_dotenv()
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()

    expanded_content = _expand_env_vars(content)
    return yaml.safe_load(expanded_content) or {}
