# ---------------------- homework_20 ------------------------


from random import randint


def diff_even_odd(num_limit, lower_bound, upper_bound):
    number_list = []
    total_even = 0
    total_odd = 0
    for i in range(num_limit):
        number_list.append(randint(lower_bound, upper_bound))
    for num in number_list:
        if num % 2 == 0:
            total_even += num
        else:
            total_odd += num
    return total_even - total_odd


print(diff_even_odd(10, 1, 1000))
