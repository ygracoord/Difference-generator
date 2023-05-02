from typing import Any, Optional


class ChangeType:
    ADDED = 'added'
    CHANGED = 'changed'
    UNCHANGED = 'unchanged'
    DELETED = 'deleted'
    ATTACHED = 'attached'


def create_node(key: Any, status: str,
                value: Any = None, old_value: Any = None,
                children: Optional[list] = None) -> dict:
    node = {
        'key': key,
        'value': {
            'old': old_value,
            'new': value
        },
        'type': status
    }

    if children is not None:
        node['children'] = children

    return node


def make_diff(data_1: dict, data_2: dict) -> list[dict]:
    diff = []
    keys = sorted(set(data_1.keys()) | set(data_2.keys()))

    for key in keys:

        if key not in data_1:
            diff.append(create_node(key, ChangeType.ADDED, value=data_2[key]))

        elif key not in data_2:
            diff.append(create_node(key, ChangeType.DELETED,
                                    old_value=data_1[key]))

        elif data_1[key] == data_2[key]:
            diff.append(create_node(key, ChangeType.UNCHANGED,
                                    old_value=data_1[key]))

        elif isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
            attached_diff = make_diff(data_1[key], data_2[key])
            diff.append(create_node(key, ChangeType.ATTACHED,
                                    children=attached_diff))

        else:
            diff.append(
                create_node(key, ChangeType.CHANGED, value=data_2[key],
                            old_value=data_1[key])
            )

    return diff
