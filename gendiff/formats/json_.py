import json


def render_json(diff_tree: dict) -> str:
    finished_data = json.dumps(diff_tree, indent=4)
    return finished_data
