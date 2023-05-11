from gendiff.formats.stylish import render_stylish
from gendiff.formats.plain import render_plain
from gendiff.formats.json_ import render_json

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'
DEFAULT = STYLISH
ERROR = 'Wrong format, use (stylish, plain, json) only!'


def render_tree(diff_tree: list[dict], format: str) -> str:
    if format == STYLISH:
        return render_stylish(diff_tree)
    elif format == PLAIN:
        return render_plain(diff_tree)
    elif format == JSON:
        return render_json(diff_tree)
    else:
        raise ValueError(ERROR)
