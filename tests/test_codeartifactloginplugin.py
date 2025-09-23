from poetry_codeartifact_auth_plugin.plugin import CodeartifactLoginPlugin
from tomlkit import loads
import pytest


def test_correct_source():
    no_source = """
    [[tool.poetry.source]]
    name = "source1"
    url = "random_url.url"
    priority = "primary"
    
    [[tool.poetry.source]]
    name = "pypi"
    priority = "primary"
    """
    toml_content = loads(no_source)
    plugin = CodeartifactLoginPlugin()
    plugin.find_sources(toml_content)

def test_incorrect_correct_source():
    no_source = """
    [[tool.poetry.source]]
    name = "source1"
    priority = "primary"

    [[tool.poetry.source]]
    name = "pypi"
    priority = "primary"
    """
    toml_content = loads(no_source)
    plugin = CodeartifactLoginPlugin()
    with pytest.raises(Exception):
        plugin.find_sources(toml_content)

def test_incorrect_source():
    no_source = """
    [[tool.poetry.source]]
    name = "source1"
    url = "random_url.url"
    priority = "primary"

    [[tool.poetry.source]]
    priority = "primary"
    """
    toml_content = loads(no_source)
    plugin = CodeartifactLoginPlugin()
    with pytest.raises(Exception):
        plugin.find_sources(toml_content)
