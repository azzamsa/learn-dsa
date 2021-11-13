from treehouse.search import linear_search


def test_linear_search():
    input_ = list(range(10))
    assert linear_search(input_, 11) is None

    input_ = list(range(10))
    assert linear_search(input_, 3) == 3

    input_ = list(range(10))
    assert linear_search(input_, 5) == 5

    input_ = list(range(100))
    assert linear_search(input_, 50) == 50
