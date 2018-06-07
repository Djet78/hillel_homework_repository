# ----------------------- task 9 ------------------------

from random import randint


def normalizer(lst):
    """
    normalizes one-dimensional list to [-1;1] interval
    :param lst: Takes given list
    :return: Return modified list
    """
    ration_value = max(lst, key=abs)
    for i, elem in enumerate(lst):
        lst[i] = round(elem / ration_value, 2)
    return lst


lst = [i * randint(- 2, 2) for i in range(10, 20 + 1)]
print(lst)
print(normalizer(lst))
