"""Search a target from the input using linear search algorithm"""


def linear_search(input_, target):
    """Search a target from the input using linear search algorithm"""
    for index in range(len(input_)):
        if input_[index] == target:
            return index
    return None
