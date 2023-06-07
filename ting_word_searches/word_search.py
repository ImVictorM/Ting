from ting_file_management.queue import Queue


def create_file_report(file, word, include_content):
    file_report = {
        "ocorrencias": [],
        "palavra": word,
        "arquivo": file["nome_do_arquivo"],
    }

    for index, line in enumerate(file["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            occurrence = (
                {"linha": index + 1, "conteudo": line}
                if include_content
                else {"linha": index + 1}
            )
            file_report["ocorrencias"].append(occurrence)

    return file_report if file_report["ocorrencias"] else None


def exists_word(word: str, instance: Queue, *, include_content=False):
    complete_report = []

    for file in instance.queue:
        file_report = create_file_report(file, word, include_content)

        if file_report:
            complete_report.append(file_report)

    return complete_report


def search_by_word(word, instance):
    return exists_word(word, instance, include_content=True)
