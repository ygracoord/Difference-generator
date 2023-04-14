from gendiff.file_operations.gendiff import generate_diff

FLAT_JSON1 = 'tests/fixtures/input_files/file1.json'
FLAT_JSON2 = 'tests/fixtures/input_files/file2.json'
FLAT_JSON_RESULT = 'tests/fixtures/output_files/result_json.txt'

FLAT_YML1 = 'tests/fixtures/input_files/file1.yml'
FLAT_YML2 = 'tests/fixtures/input_files/file2.yml'
FLAT_YAML_RESULT = 'tests/fixtures/output_files/result_yaml.txt'


def test_flat_json():
    with open(FLAT_JSON_RESULT) as file:
        expected = file.read()
        assert expected == generate_diff(FLAT_JSON1, FLAT_JSON2)


def test_flat_yaml():
    with open(FLAT_YAML_RESULT) as file:
        expected = file.read()
        assert expected == generate_diff(FLAT_YML1, FLAT_YML2)
