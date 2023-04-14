#!/usr/bin/env python3
from typing import NoReturn
from gendiff.cli import cli_parse
from gendiff.file_operations.gendiff import generate_diff


def main() -> NoReturn:
    args = cli_parse()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
