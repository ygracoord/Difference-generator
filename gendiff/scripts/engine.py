#!/usr/bin/env python3
import argparse
from gendiff.gendiff import generate_diff


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    return args.first_file, args.second_file


def main():
    first, second = parse()
    print(generate_diff(first, second))


if __name__ == '__main__':
    main()
