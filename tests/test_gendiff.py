import pytest

from gendiff.file_operations.gendiff import generate_diff
from gendiff.formats.rendering import STYLISH, PLAIN, JSON

FLAT_JSON1 = 'tests/fixtures/input_files/file1.json'
FLAT_JSON2 = 'tests/fixtures/input_files/file2.json'
FLAT_YML1 = 'tests/fixtures/input_files/file1.yml'
FLAT_YML2 = 'tests/fixtures/input_files/file2.yml'
ATTACHED_JSON1 = 'tests/fixtures/input_files/file3.json'
ATTACHED_JSON2 = 'tests/fixtures/input_files/file4.json'
ATTACHED_YML1 = 'tests/fixtures/input_files/file3.yml'
ATTACHED_YML2 = 'tests/fixtures/input_files/file4.yml'

RESULT_STYLISH = 'tests/fixtures/output_files/stylish.txt'
RESULT_STYLISH_ATTACHED = 'tests/fixtures/output_files/stylish_attached.txt'
RESULT_PLAIN = 'tests/fixtures/output_files/plain.txt'
RESULT_PLAIN_ATTACHED = 'tests/fixtures/output_files/plain_attached.txt'
RESULT_JSON = 'tests/fixtures/output_files/json_.txt'
RESULT_JSON_ATTACHED = 'tests/fixtures/output_files/json_attached.txt'


@pytest.mark.parametrize('file_1, file_2, format, result_file', [
    (FLAT_JSON1, FLAT_JSON2, STYLISH, RESULT_STYLISH),
    (FLAT_YML1, FLAT_YML2, STYLISH, RESULT_STYLISH),
    (FLAT_YML1, FLAT_JSON2, STYLISH, RESULT_STYLISH),
    (ATTACHED_JSON1, ATTACHED_JSON2, STYLISH, RESULT_STYLISH_ATTACHED),
    (ATTACHED_YML1, ATTACHED_YML2, STYLISH, RESULT_STYLISH_ATTACHED),
    (FLAT_JSON1, FLAT_JSON2, PLAIN, RESULT_PLAIN),
    (FLAT_YML1, FLAT_YML2, PLAIN, RESULT_PLAIN),
    (ATTACHED_JSON1, ATTACHED_JSON2, PLAIN, RESULT_PLAIN_ATTACHED),
    (ATTACHED_YML1, ATTACHED_YML2, PLAIN, RESULT_PLAIN_ATTACHED),
    (FLAT_JSON1, FLAT_JSON2, JSON, RESULT_JSON),
    (FLAT_YML1, FLAT_YML2, JSON, RESULT_JSON),
    (ATTACHED_JSON1, ATTACHED_JSON2, JSON, RESULT_JSON_ATTACHED),
    (ATTACHED_YML1, ATTACHED_YML2, JSON, RESULT_JSON_ATTACHED),
])
def test_generate_diff(file_1, file_2, format, result_file):
    with open(result_file) as file:
        expected = file.read()
    assert expected == generate_diff(file_1, file_2, format)
