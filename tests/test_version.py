import importlib.metadata


def test_version():
    assert isinstance(importlib.metadata.version("test_pyckage_github"), str)
