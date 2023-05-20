from enum import Enum


class ChangeType(str, Enum):
    ADDED = 'added'
    CHANGED = 'changed'
    UNCHANGED = 'unchanged'
    DELETED = 'deleted'
    ATTACHED = 'attached'


def make_diff(data_1: dict, data_2: dict) -> list[dict]:
    diff = []
    keys = set(data_1.keys()) | set(data_2.keys())

    for key in sorted(keys):

        if key not in data_1:
            diff.append({
                'key': key,
                'value': {
                    'new': data_2[key]
                },
                'type': ChangeType.ADDED
            })

        elif key not in data_2:
            diff.append({
                'key': key,
                'value': {
                    'old': data_1[key]
                },
                'type': ChangeType.DELETED
            })

        elif data_1[key] == data_2[key]:
            diff.append({
                'key': key,
                'value': {
                    'old': data_2[key]
                },
                'type': ChangeType.UNCHANGED
            })

        elif isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
            diff.append({
                'key': key,
                'type': ChangeType.ATTACHED,
                'children': make_diff(data_1[key], data_2[key])
            })

        else:
            diff.append({
                'key': key,
                'value': {
                    'old': data_1[key],
                    'new': data_2[key]
                },
                'type': ChangeType.CHANGED
            })

    return diff


def build(data_1: dict, data_2: dict) -> dict:
    return {'type': 'differ', 'children': make_diff(data_1, data_2)}
