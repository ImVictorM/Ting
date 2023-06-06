import sys
import pathlib


def file_extension_is_valid(file):
    suffix = pathlib.Path(file).suffix
    available_extensions = {".txt"}

    if suffix not in available_extensions:
        return False

    return True


def txt_importer(path_file: str):
    if not file_extension_is_valid(path_file):
        return sys.stderr.write("Formato inválido")

    try:
        with open(path_file) as file:
            lines = [line.strip() for line in file.readlines()]
            return lines
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
