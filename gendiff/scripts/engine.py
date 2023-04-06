#!/usr/bin/env python3
from gendiff.cli import cli_parse
from gendiff.gendiff import generate_diff


def main():
    args = cli_parse()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
