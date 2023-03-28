import os
from abc import abstractmethod


class Templater:

    def write_model(self, template, config):
        """
        Creates a model from a template and config
        :param template: template file for the model
        :param config: config file
        :return: name of the new model (its filename)
        """

        # Prefix actual filename with variable_name
        variable_name = config.get("variable_name").lower()
        substr = "/_"
        idx = template.filename.index(substr)
        filename = "out/" + template.filename[:idx+1] + variable_name + template.filename[idx+1:]

        content = template.render(
            config=config
        )
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, mode="w", encoding="utf-8") as message:
            message.write(content)
            print(f"... wrote {filename}")

        return filename

    @abstractmethod
    def write_models(self, config):
        """
        Writes all the models needed based on given config
        :param config: config file
        :return: TODO
        """
        pass
