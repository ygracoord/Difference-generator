from typing import Any

from gendiff.file_operations.diff import ChangeType

PATH = '{}.{}'
COMPLEX_VALUE = "[complex value]"
TEMPLATES = {
    'added': "Property '{}' was added with value: {}",
    'deleted': "Property '{}' was removed",
    'changed': "Property '{}' was updated. From {} to {}",
}


def render_nodes(diff: dict, root='') -> str:
    result = []

    for node in diff['children']:
        path = PATH.format(root, node['key']) if root else node['key']

        if node['type'] == ChangeType.ADDED:
            result.append(TEMPLATES['added'].format(
                path, transform(node['value']['new'])
            ))

        elif node['type'] == ChangeType.DELETED:
            result.append(TEMPLATES['deleted'].format(path))

        elif node['type'] == ChangeType.CHANGED:
            result.append(TEMPLATES['changed'].format(
                path,
                transform(node['value']['old']),
                transform(node['value']['new'])
            ))

        elif node['type'] == ChangeType.ATTACHED:
            result.append(render_nodes(node, path))

    return '\n'.join(result)


def render_plain(diff_tree: dict) -> str:
    finished_data = render_nodes(diff_tree)
    return finished_data


def transform(value: Any) -> str:
    if isinstance(value, bool):
        correct_value = str(value).lower()
    elif value is None:
        correct_value = 'null'
    elif isinstance(value, int):
        correct_value = str(value)
    elif isinstance(value, dict):
        correct_value = COMPLEX_VALUE
    else:
        correct_value = f"'{value}'"

    return correct_value
