import pytest
from pathlib import Path


@pytest.fixture
def file_preparation(request):
    file_1, file_2, format, result_file = request.param
    fixtures_directory = Path(__file__).resolve().parent / "fixtures"

    file_path1 = fixtures_directory / file_1
    file_path2 = fixtures_directory / file_2
    result_path = fixtures_directory / result_file

    try:
        return file_path1, file_path2, format, result_path
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Could not find the specified file: {e.filename}")
