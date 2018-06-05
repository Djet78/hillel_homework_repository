# ----------------------- task 5 ------------------------


def nearest_to_ten(first_num, second_num):
    """
    :param first_num:
    :param second_num:
    :return: nearest number to ten
    """
    first_distance = abs(first_num - 10)
    second_distance = abs(second_num - 10)
    if first_distance > second_distance:
        return second_num
    else:
        return first_num


print(nearest_to_ten(-10.1, -9.8))
print(nearest_to_ten(10.1, 9.8))
