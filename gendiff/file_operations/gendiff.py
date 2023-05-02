from gendiff.file_operations.diff import make_diff
from gendiff.file_operations.file_parser import get_data
from gendiff.formatters.rendering import render_tree, DEFAULT


def generate_diff(file_path1: str, file_path2: str, format: str = DEFAULT) -> str:  # noqa: E501

    diff_tree = make_diff(
        data_1=get_data(file_path1),
        data_2=get_data(file_path2)
    )

    return render_tree(diff_tree, format)
