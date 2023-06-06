from ting_file_management.priority_queue import PriorityQueue
import pytest

normal_priority = {
    "nome_do_arquivo": "arquivo_1",
    "qtd_linhas": 10,
    "linhas_do_arquivo": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
}

normal_priority_2 = {
    "nome_do_arquivo": "arquivo_2",
    "qtd_linhas": 6,
    "linhas_do_arquivo": ["1", "2", "3", "4", "5", "6"],
}

high_priority = {
    "nome_do_arquivo": "arquivo_3",
    "qtd_linhas": 3,
    "linhas_do_arquivo": ["1", "2", "3"],
}


def test_basic_priority_queueing():
    # test if search with only normal priorities
    pq = PriorityQueue()
    pq.enqueue(normal_priority)
    pq.enqueue(normal_priority_2)

    assert len(pq) == 2
    assert pq.search(0) == normal_priority
    assert pq.search(1) == normal_priority_2

    # test if files with less than 5 lines is inserted with priority
    pq = PriorityQueue()
    pq.enqueue(normal_priority)
    pq.enqueue(high_priority)

    assert pq.search(0) == high_priority
    assert pq.search(1) == normal_priority

    # test if a file with priority is removed before
    pq = PriorityQueue()
    pq.enqueue(normal_priority)
    pq.enqueue(high_priority)

    assert pq.dequeue() == high_priority
    assert pq.dequeue() == normal_priority
    assert len(pq) == 0

    # test if searching for an invalid or negative index raises an error
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.search(1)

    with pytest.raises(IndexError):
        pq.search(-1)
