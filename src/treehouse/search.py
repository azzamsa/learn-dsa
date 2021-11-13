def linear_search(numbers, target):
    """Search a target from the input using linear search algorithm"""
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return None


def binary_search(numbers, target):
    """Search a target from the input using binary search algorithm"""
    first_index = 0
    last_index = len(numbers) - 1

    while first_index <= last_index:
        mid_index = (last_index + first_index) // 2

        # best case
        if numbers[mid_index] == target:
            return mid_index

        if numbers[mid_index] < target:
            # discard all numbers BEFORE mid_index
            first_index = mid_index + 1
        else:
            # discard all numbers AFTER mid_index
            last_index = mid_index - 1

    return None
