import os


def get_extension(file_path: str) -> str:
    _, extension = os.path.splitext(file_path)

    return extension


def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def get_file_components(file_path: str) -> tuple:
    try:
        return read_file(file_path), get_extension(file_path)
    except FileNotFoundError:
        print(f'File not found: {file_path}')
