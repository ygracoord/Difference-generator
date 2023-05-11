import json


def render_json(diff_tree: list) -> str:
    finished_data = json.dumps(diff_tree, indent=4)
    return finished_data
