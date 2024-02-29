import yaml

class Utils:
    def __init__(self) -> None:
        # Load YAML data from a file
        with open("application.yaml", "r") as file:
            self.data = yaml.safe_load(file)

    def get_property(self, property_name:str):
        # Access values using keys
        return self.data[property_name]
