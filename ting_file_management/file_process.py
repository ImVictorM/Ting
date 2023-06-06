from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def queue_already_has_file(path_file, queue):
    for file in queue:
        if file["nome_do_arquivo"] == path_file:
            return True
    return False


def process(path_file: str, instance: Queue):
    if not queue_already_has_file(path_file, instance.queue):
        lines = txt_importer(path_file)
        file_info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }

        instance.enqueue(file_info)
        return sys.stdout.write(str(file_info))


def remove(instance: Queue):
    if not len(instance):
        return sys.stdout.write("Não há elementos\n")

    removed = instance.dequeue()["nome_do_arquivo"]

    print(f"Arquivo {removed} removido com sucesso", file=sys.stdout)


def file_metadata(instance: Queue, position):
    try:
        file = instance.search(position)
        return sys.stdout.write(str(file))
    except IndexError:
        return sys.stderr.write("Posição inválida")
