import os
import json
import yaml


EXTENSIONS = ('.json', '.yaml', '.yml')


def get_file(file_path: str) -> dict:
    _, extension = os.path.splitext(file_path)
    if extension not in EXTENSIONS:
        raise ValueError(f"Incorrect file format: {extension}")
    try:
        with open(file_path) as f:
            if extension == '.json':
                file = json.load(f)
            elif extension == '.yml' or extension == '.yaml':
                file = yaml.safe_load(f)
            return file
    except (FileNotFoundError, json.JSONDecodeError, yaml.YAMLError) as error:
        raise error
