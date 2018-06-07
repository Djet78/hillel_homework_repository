# ----------------------- task 8 ------------------------


def max_min_value_replacer(lst):
    """
    Uses min and max values and their indexes to replace them between each other
    :param lst: takes given list
    :return: return given list
    """
    max_value_index = lst.index(max(lst))
    min_value_index = lst.index(min(lst))
    max_value = max(lst)
    min_value = min(lst)
    lst[max_value_index] = min_value
    lst[min_value_index] = max_value
    return lst


lst = [15, 2, 33, 12312, 3, 1, 11, 33, 49]
print(lst)
print(max_min_value_replacer(lst))

print("-------------------------------------")

lst2 = [_ for _ in range(1, 10 + 1)]
print(lst2)
print(max_min_value_replacer(lst2))
