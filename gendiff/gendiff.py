import json
import os


def check_extension(file):
    _, extension = os.path.splitext(file)
    if extension != '.json':
        raise ValueError('Incorrect file format')
    with open(file) as f:
        file = json.load(f)

    return file


def generate_diff(path_1, path_2):
    file_1, file_2 = check_extension(path_1), check_extension(path_2)
    keys = set(file_1.keys()) | set(file_2.keys())
    diff = {key: (file_1.get(key), file_2.get(key)) for key in sorted(keys)}
    result = []

    for key, (value_1, value_2) in diff.items():
        if value_1 is None:
            result.append(f'+ {key}: {value_2}')
        elif value_2 is None:
            result.append(f'- {key}: {value_1}')
        elif value_1 != value_2:
            result.append(f'- {key}: {value_1}')
            result.append(f'+ {key}: {value_2}')
        else:
            result.append(f'  {key}: {value_1}')

    return '{\n  ' + '\n  '.join(result) + '\n}'
