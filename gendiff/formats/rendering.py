from gendiff.formats.stylish import render_stylish

STYLISH = 'stylish'
DEFAULT = STYLISH


def render_tree(diff: list[dict], format: str) -> str:
    if format == STYLISH:
        return render_stylish(diff)
