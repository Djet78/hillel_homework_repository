# ------------------------ Task 107 -------------------------


def bin_search(lst, element):
    """
    Search for an element in sorted(ascending) list using 'binary search' algorithm
    :param lst: takes given list
    :param element: elem to search
    :return: int. Index of element if found, -1 if don't
    """
    start = 0
    end = len(lst) - 1
    while start <= end:
        middle = int((start + end) / 2)
        if lst[middle] == element:
            return middle
        elif lst[middle] > element:
            end = middle - 1
        elif lst[middle] < element:
            start = middle + 1
    return - 1


lst = [2, 5, 7, 9, 11, 17, 33, 42, 51, 52, 76, 222]


assert 0 == bin_search(lst, 2)
assert 11 == bin_search(lst, 222)
assert 5 == bin_search(lst, 17)
assert -1 == bin_search(lst, 77)

print(bin_search(lst, 7))
