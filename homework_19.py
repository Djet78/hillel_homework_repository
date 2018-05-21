# ---------------------- homework_19 ------------------------

from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound):
    """
    Count difference between max and min integer, in randomly created integer list  with a given amount of numbers
    :param num_limit: takes quantity of created numbers
    :param lower_bound: to method 'randint', says from where to start in numerical range
    :param upper_bound: to method 'randint', says where to stop in numerical range
    :return: Int. Difference of max and min number in list
    """
    number_list = []
    for i in range(num_limit):
        number_list.append(randint(lower_bound, upper_bound))
    max_min_diff = max(number_list) - min(number_list)
    return max_min_diff
