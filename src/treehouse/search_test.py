from treehouse.search import linear_search


def test_linear_search():
    # `range()` is exclusive!
    numbers = list(range(1, 11))
    assert linear_search(numbers, 11) is None

    numbers = list(range(1, 11))
    assert linear_search(numbers, 3) == 2

    numbers = list(range(1, 11))
    assert linear_search(numbers, 6) == 5

    numbers = list(range(1, 101))
    assert linear_search(numbers, 50) == 49
