from enum import Enum

from gendiff.formats.stylish import render_stylish
from gendiff.formats.plain import render_plain
from gendiff.formats.json_ import render_json


class FormatType(str, Enum):
    STYLISH = 'stylish'
    PLAIN = 'plain'
    JSON = 'json'


def render_tree(diff_tree: dict, format: str) -> str:
    if format == FormatType.STYLISH:
        return render_stylish(diff_tree)
    elif format == FormatType.PLAIN:
        return render_plain(diff_tree)
    elif format == FormatType.JSON:
        return render_json(diff_tree)
    else:
        raise ValueError('Wrong format, use (stylish, plain, json) only!')
