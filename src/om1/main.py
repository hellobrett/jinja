from jinja2 import Environment, FileSystemLoader
from src.om1.templater import Templater
import yaml


# Read in config from yml file
with open("easi.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)["variable"]
    except yaml.YAMLError as exc:
        print(exc)


env = Environment(loader=FileSystemLoader("templates/note_extraction/"))
print(env.list_templates())
templater = Templater(env)
templater.write_models(config)
