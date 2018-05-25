# ------------------------ Task 26 -------------------------
from random import randint


def calc_frequency(lst):
    """
    :param lst: takes given list from numbers in slice [-1, 1]
    :return: integer item most in the list, but if some of them met equally - return None
    """
    zero = lst.count(0)
    one = lst.count(1)
    minus_one = lst.count(-1)
    if zero == minus_one != 0:
        return None
    if one == minus_one != 0:
        return None
    if zero == one != 0:
        return None
    if zero > one and zero > minus_one:
        return 0
    if one > zero and one > minus_one:
        return 1
    if minus_one > zero and minus_one > one:
        return -1


rand_numbers = []
while len(rand_numbers) < 11:
    rand_numbers.append(randint(-1, 1))
print(calc_frequency(rand_numbers))
