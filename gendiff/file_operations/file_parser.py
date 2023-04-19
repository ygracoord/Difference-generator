import os
import json
import yaml

JSON = '.json'
YAML_OR_YML = ('.yaml', '.yml')
EXTENSIONS = (JSON, YAML_OR_YML)


def get_file(file_path: str) -> dict:
    _, extension = os.path.splitext(file_path)
    if extension not in EXTENSIONS:
        raise ValueError(f"Incorrect file format: {extension}")
    try:
        with open(file_path) as f:
            if extension == JSON:
                file = json.load(f)
            elif extension in YAML_OR_YML:
                file = yaml.safe_load(f)
            return file
    except (FileNotFoundError, json.JSONDecodeError, yaml.YAMLError) as error:
        raise error
