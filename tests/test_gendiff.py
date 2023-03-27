from gendiff.gendiff import generate_diff


def test_json():
    first_json = 'tests/fixtures/file1.json'
    second_json = 'tests/fixtures/file2.json'
    result = 'tests/fixtures/result_json.txt'

    with open(result) as result_json:
        assert generate_diff(first_json, second_json) == result_json.read()
