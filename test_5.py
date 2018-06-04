# ----------------------- task 5 ------------------------


def nearest_to_ten(first_num, second_num):
    """
    :param first_num:
    :param second_num:
    :return: nearest number to ten
    """
    if first_num < 10:
        if first_num <= 0:
            first_distance = abs(first_num) + 10
        else:
            first_distance = 10 - first_num
    else:
        first_distance = first_num - 10
    if second_num < 10:
        if second_num <= 0:
            second_distance = abs(second_num) + 10
        else:
            second_distance = 10 - second_num
    else:
        second_distance = second_num - 10
    if first_distance > second_distance:
        return second_num
    else:
        return first_num


print(nearest_to_ten(-10.1, -9.8))
print(nearest_to_ten(10.1, 9.8))
