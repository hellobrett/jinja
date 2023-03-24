from templater import Templater
from jinja2 import Environment, FileSystemLoader


class NoteExtractionTemplater(Templater):
    setup_environment = Environment(loader=FileSystemLoader("templates/note_extraction/setup/"))
    # final_environment = Environment(loader=FileSystemLoader("templates/note_extraction/final/"))

    def write_models(self, config):
        setup_templates = self.setup_environment.list_templates()
        # final_templates = self.final_environment.list_templates()

        # TODO: Somehow collapse these together. Nontrivial because we want to make sure
        # The models are handled properly by directory and written to such directories correctly
        for t in setup_templates:
            template = self.setup_environment.get_template(t)
            self.write_model(template, config)

        # for t in final_templates:
        #     template = self.final_environment.get_template(t)
        #     self.write_model(config, template)
