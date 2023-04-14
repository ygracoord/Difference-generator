from gendiff.file_operations.gendiff import generate_diff

FLAT_JSON1 = 'tests/fixtures/input_files/file1.json'
FLAT_JSON2 = 'tests/fixtures/input_files/file2.json'
FLAT_YML1 = 'tests/fixtures/input_files/file1.yml'
FLAT_YML2 = 'tests/fixtures/input_files/file2.yml'

RESULT_STYLISH = 'tests/fixtures/output_files/stylish.txt'


def test_flat_json():
    with open(RESULT_STYLISH) as file:
        expected = file.read()
        assert expected == generate_diff(FLAT_JSON1, FLAT_JSON2)


def test_flat_yaml():
    with open(RESULT_STYLISH) as file:
        expected = file.read()
        assert expected == generate_diff(FLAT_YML1, FLAT_YML2)
