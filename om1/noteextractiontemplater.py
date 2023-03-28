from templater import Templater
from jinja2 import Environment, FileSystemLoader


class NoteExtractionTemplater(Templater):
    environment = Environment(loader=FileSystemLoader("om1/templates/note_extraction/"))

    def write_models(self, config):
        templates = self.environment.list_templates()

        for t in templates:
            template = self.environment.get_template(t)
            self.write_model(template, config)
