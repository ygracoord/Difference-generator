import pytest

from gendiff.file_operations.gendiff import generate_diff
from gendiff.formats.rendering import FormatType

ATTACHED_JSON1 = 'file1.json'
ATTACHED_JSON2 = 'file2.json'
ATTACHED_YML1 = 'file1.yml'
ATTACHED_YML2 = 'file2.yml'

RESULT_STYLISH_ATTACHED = 'stylish_attached.txt'
RESULT_PLAIN_ATTACHED = 'plain_attached.txt'
RESULT_JSON_ATTACHED = 'json_attached.txt'


@pytest.mark.parametrize('file_preparation', [
    (ATTACHED_JSON1, ATTACHED_JSON2, FormatType.STYLISH, RESULT_STYLISH_ATTACHED),
    (ATTACHED_YML1, ATTACHED_YML2, FormatType.STYLISH, RESULT_STYLISH_ATTACHED),
    (ATTACHED_JSON1, ATTACHED_JSON2, FormatType.PLAIN, RESULT_PLAIN_ATTACHED),
    (ATTACHED_YML1, ATTACHED_YML2, FormatType.PLAIN, RESULT_PLAIN_ATTACHED),
    (ATTACHED_JSON1, ATTACHED_JSON2, FormatType.JSON, RESULT_JSON_ATTACHED),
    (ATTACHED_YML1, ATTACHED_YML2, FormatType.JSON, RESULT_JSON_ATTACHED),
], indirect=True)
def test_generate_diff(file_preparation):
    file_1, file_2, format, result_file = file_preparation
    with open(result_file) as file:
        expected = file.read()
    assert expected == generate_diff(file_1, file_2, format)
