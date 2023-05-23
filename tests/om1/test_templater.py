from unittest.mock import MagicMock, call

from jinja2 import Environment

from src.om1.templater import write_model, write_models
import yaml

def test_write_models() -> None:
    # setup
    def list_templates():
        return [1,2,3]

    def get_template(t):
        return t

    mock_env = MagicMock(Environment)
    mock_writer = MagicMock(write_model)
    mock_config = MagicMock(dict)
    mock_env.list_templates = list_templates
    mock_env.get_template = get_template

    # test
    write_models(mock_config, mock_env, mock_writer)

    # verify
    calls = [call(1, mock_config), call(2, mock_config), call(3, mock_config)]
    mock_writer.assert_has_calls(calls)

def test_yml_parser() -> None:
    with open("example.yml", "r") as stream:
        try:
            loaded_yml = yaml.safe_load(stream)
            print(loaded_yml)
        except yaml.YAMLError as exc:
            print(exc)
