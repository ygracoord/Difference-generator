import json
import yaml

JSON = '.json'
YAML_OR_YML = ('.yaml', '.yml')


def load_json(data: str) -> dict:
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        raise ValueError('Failed to load JSON data:' + str(e))


def load_yaml(data: str) -> dict:
    try:
        return yaml.safe_load(data)
    except yaml.YAMLError as e:
        raise ValueError('Failed to load YAML data:' + str(e))


def load_data(data: str, data_format: str) -> dict:
    if data_format == JSON:
        return load_json(data)
    elif data_format in YAML_OR_YML:
        return load_yaml(data)
    else:
        raise ValueError(f'Unsupported data format: {data_format}')
