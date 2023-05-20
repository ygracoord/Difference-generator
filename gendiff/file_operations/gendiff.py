from gendiff.file_operations.diff import build
from gendiff.file_operations.file_parser import get_data
from gendiff.formats.rendering import render_tree, FormatType


def generate_diff(file_path1: str, file_path2: str, format: str = FormatType.STYLISH) -> str:  # noqa: E501

    diff_tree = build(
        data_1=get_data(file_path1),
        data_2=get_data(file_path2)
    )

    return render_tree(diff_tree, format)
