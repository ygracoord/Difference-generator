from typing import Any

from gendiff.file_operations.diff import ChangeType

NESTED_OFFSET = 4
LEFT_SHIFTING = 2

TEMPLATES = {
    'base': '{{\n{}\n}}',
    'begin': '{}{} {}: {{',
    'diff': '{}{} {}: {}',
    'end': '{}  }}'
}


def make_offset(depth: int) -> str:
    return ' ' * (depth * NESTED_OFFSET - LEFT_SHIFTING)


def transform(value: Any) -> str:
    if isinstance(value, bool):
        correct_value = str(value).lower()
    elif value is None:
        correct_value = 'null'
    else:
        correct_value = str(value)

    return correct_value


def convert_attached(dict_value: dict, depth: int) -> str:
    result = []

    for key, value in dict_value.items():
        result.append(collect_row(key, value, ' ', depth))

    return '\n'.join(result)


def collect_row(key: Any, value: Any, sign: str, depth: int) -> str:
    result = []
    offset = make_offset(depth)
    depth += 1

    if isinstance(value, dict):
        result.extend([
            TEMPLATES['begin'].format(offset, sign, key),
            convert_attached(value, depth),
            TEMPLATES['end'].format(offset)
        ])

    else:
        result.append(TEMPLATES['diff'].format(
            offset, sign, key, transform(value)
        ))

    return '\n'.join(result)


def render_nodes(diff: dict, depth: int = 1) -> str:  # noqa: C901
    result = []
    offset = make_offset(depth)

    for node in diff['children']:

        if node['type'] == ChangeType.DELETED:
            result.append(collect_row(
                node['key'], node['value']['old'], '-', depth
            ))

        elif node['type'] == ChangeType.ADDED:
            result.append(collect_row(
                node['key'], node['value']['new'], '+', depth
            ))

        elif node['type'] == ChangeType.UNCHANGED:
            result.append(collect_row(
                node['key'], node['value']['old'], ' ', depth
            ))

        elif node['type'] == ChangeType.CHANGED:
            result.append(collect_row(
                node['key'], node['value']['old'], '-', depth
            ))
            result.append(collect_row(
                node['key'], node['value']['new'], '+', depth
            ))

        elif node['type'] == ChangeType.ATTACHED:
            result.extend([
                TEMPLATES['begin'].format(offset, ' ', node['key']),
                render_nodes(node, depth + 1),
                TEMPLATES['end'].format(offset)
            ])

    return '\n'.join(result)


def render_stylish(diff_tree: dict) -> str:
    finished_data = TEMPLATES['base'].format(render_nodes(diff_tree))
    return finished_data
