# ---------------------- homework_21 ------------------------


from random import randint


def get_max_digit1(number):
    """
    With using strings
    :param number: any integer number
    :return: Int. biggest digit from given number
    """
    return max(str(number), key=int)


def get_max_digit2(number):
    """
    Without using strings
    :param number: any integer number
    :return: Int. biggest digit from given number
    """
    biggest_digit = number % 10
    number = number // 10
    while number != 0:
        curr_digit = number % 10
        biggest_digit = max(biggest_digit, curr_digit)
        number = number // 10
    return biggest_digit


rand_number = randint(1e11, 1e12-1)
print(get_max_digit1(rand_number))
print(get_max_digit2(rand_number))
