# ------------------------ Task 26 -------------------------

from random import randint


def calc_frequency(lst):
    """
    :param lst: takes given list from numbers in slice [-1, 1]
    :return: integer item most in the list, but if some of them met equally - return None
    """
    if lst.count(1 or -1) == lst.count(0) or lst.count(1) == lst.count(-1):
        return None
    elif lst.count(1) > lst.count(-1) and lst.count(1) > lst.count(0):
        return 1
    elif lst.count(-1) > lst.count(1) and lst.count(-1) > lst.count(0):
        return -1
    elif lst.count(0) > lst.count(1) and lst.count(0) > lst.count(-1):
        return 0


rand_numbers = []
while len(rand_numbers) < 11:
    rand_numbers.append(randint(-1, 1))

print(calc_frequency(rand_numbers))
