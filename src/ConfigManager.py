import json
import os

class ConfigManager:
    def __init__(self, env, config_path):
        self.env = env
        self.config_path = config_path

    def load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        with open(self.config_path) as f:
            data = json.load(f)
            print("------------------")
            print(data)
        if self.env not in data:
            raise ValueError(f"Environment '{self.env}' not found in config.")
        return data[self.env]

# confObj = ConfigManager('dev','C:\\D Drive\\Vinod\\GitHub -Projects\\pytest_allure_api_automation\\conf\\configuration_qa.json')
# print(confObj.load_config())