from typing import Optional


def linear_search(numbers: list[int], target: int) -> Optional[int]:
    """Search a target from the input using linear search algorithm

    :param numbers: a collection with comparable items (not required to be sorted)
    :param target: item value to search
    :return: index of found item or None if item is not found
    """
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return None


def binary_search(numbers: list[int], target: int) -> Optional[int]:
    """Search a target from the input using binary search algorithm

    :param numbers: a collection with comparable items (must be sorted)
    :param target: item value to search
    :return: index of found item or None if item is not found
    """
    first_index = 0
    last_index = len(numbers) - 1

    while first_index <= last_index:
        mid_index = (last_index + first_index) // 2

        # best case
        item = numbers[mid_index]
        if item == target:
            return mid_index

        if item < target:
            # discard all numbers BEFORE mid_index
            first_index = mid_index + 1
        else:
            # discard all numbers AFTER mid_index
            last_index = mid_index - 1

    return None
