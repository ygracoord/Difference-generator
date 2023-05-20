import os
import json
import yaml

JSON = '.json'
YAML_OR_YML = ('.yaml', '.yml')


def parse(content, extension):
    if extension == JSON:
        return json.loads(content)
    elif extension in YAML_OR_YML:
        return yaml.safe_load(content)
    else:
        raise ValueError(f"Incorrect file format: {extension}")


def get_data(file_path: str):
    _, extension = os.path.splitext(file_path)

    with open(file_path) as file:
        content = file.read()
    return parse(content, extension)
