from gendiff.file_operations.file_parser import get_file


def generate_diff(path_1: str, path_2: str) -> str:
    file_1, file_2 = get_file(path_1), get_file(path_2)
    keys = set(file_1.keys()) | set(file_2.keys())
    diff = {key: (file_1.get(key), file_2.get(key)) for key in sorted(keys)}
    result = []

    for key, (value_1, value_2) in diff.items():
        if value_1 is None:
            result.append(f'+ {key}: {str(value_2).lower()}')
        elif value_2 is None:
            result.append(f'- {key}: {str(value_1).lower()}')
        elif value_1 != value_2:
            result.append(f'- {key}: {str(value_1).lower()}')
            result.append(f'+ {key}: {str(value_2).lower()}')
        else:
            result.append(f'  {key}: {str(value_1).lower()}')

    return '{\n  ' + '\n  '.join(result) + '\n}'
