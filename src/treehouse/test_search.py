from treehouse.search import linear_search, binary_search

numbers = [0, 5, 7, 10, 15]


def test_linear_search():
    assert linear_search(numbers, 0) == 0
    assert linear_search(numbers, 15) == 4
    assert linear_search(numbers, 5) == 1
    assert linear_search(numbers, 6) is None


def test_binary_search():
    assert binary_search(numbers, 0) == 0
    assert binary_search(numbers, 15) == 4
    assert binary_search(numbers, 5) == 1
    assert binary_search(numbers, 6) is None
