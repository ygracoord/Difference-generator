from gendiff.formats.stylish import render_stylish
from gendiff.formats.plain import render_plain

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'
DEFAULT = STYLISH


def render_tree(diff_tree: list[dict], format: str) -> str:
    if format == STYLISH:
        return render_stylish(diff_tree)
    elif format == PLAIN:
        return render_plain(diff_tree)
