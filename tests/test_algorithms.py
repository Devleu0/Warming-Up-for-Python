import random

from counting_sort import counting_sort
from dijkstra import INF, dijkstra
from quick_sort import quick_select, quick_sort, quick_sort_inplace

CASES = [[], [1], [8, 5, 4, 7, 2], [3, 3, 1, 2, 3], list(range(10, 0, -1))]


def test_quick_sort_variants():
    for case in CASES:
        assert quick_sort(case) == sorted(case)
        assert quick_sort_inplace(list(case)) == sorted(case)


def test_quick_sort_random():
    data = [random.randint(0, 50) for _ in range(200)]
    assert quick_sort(data) == sorted(data)
    assert quick_sort_inplace(list(data)) == sorted(data)


def test_quick_select():
    data = [5, 3, 2, 4, 1, 3]
    for k in range(1, len(data) + 1):
        assert quick_select(data, k) == sorted(data)[k - 1]


def test_counting_sort():
    for case in CASES:
        assert counting_sort(case) == sorted(case)


def test_dijkstra():
    graph = [[] for _ in range(6)]
    for a, b, c in [(5, 1, 1), (1, 2, 2), (1, 3, 3), (2, 3, 4), (2, 4, 5), (3, 4, 6)]:
        graph[a].append((b, c))
    assert dijkstra(graph, 1)[1:] == [0, 2, 3, 7, INF]
