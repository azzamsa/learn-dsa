"""Search a target from the input using linear search algorithm"""


def linear_search(numbers, target):
    """Search a target from the input using linear search algorithm"""
    # for index in range(len(input_)):
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return None
