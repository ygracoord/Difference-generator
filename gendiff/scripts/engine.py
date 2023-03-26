#!/usr/bin/env python3
import argparse


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()

    return args


def main():
    parse()


if __name__ == '__main__':
    main()
