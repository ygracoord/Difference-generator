import argparse
from gendiff.formats.rendering import DEFAULT


def cli_parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default=DEFAULT
    )
    args = parser.parse_args()

    return args
