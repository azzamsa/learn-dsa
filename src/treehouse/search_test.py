from treehouse.search import linear_search, binary_search

# `range()` is exclusive!
numbers1 = list(range(1, 11))
numbers2 = list(range(1, 11))
numbers3 = list(range(1, 11))
numbers4 = list(range(1, 101))


def test_linear_search():
    assert linear_search(numbers1, 11) is None
    assert linear_search(numbers2, 3) == 2
    assert linear_search(numbers3, 6) == 5
    assert linear_search(numbers4, 50) == 49


def test_binary_search():
    assert binary_search(numbers1, 11) is None
    assert binary_search(numbers2, 3) == 2
    assert binary_search(numbers3, 6) == 5
    assert binary_search(numbers4, 50) == 49
