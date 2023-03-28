from unittest.mock import MagicMock

from jinja2 import Environment

from src.om1.templater import Templater


def test_init() -> None:
    expected_env = MagicMock(Environment)
    templater = Templater(expected_env)
    assert templater.environment == expected_env


def test_write_models() -> None:
    print("TODO")
