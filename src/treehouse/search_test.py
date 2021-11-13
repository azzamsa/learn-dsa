from treehouse.search import linear_search


def test_linear_search():
    input_ = list(range(100))
    assert linear_search(input_, 5) == 5

    input_ = list(range(100))
    assert linear_search(input_, 50) == 50

    input_ = list(range(100))
    assert linear_search(input_, 3) == 3
