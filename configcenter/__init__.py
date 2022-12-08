import yaml
import os

filepath = os.path.join(os.path.dirname(__file__), 'configdata.yaml')
with open(filepath) as file:
    configdata = yaml.safe_load(file)
    print(configdata)
