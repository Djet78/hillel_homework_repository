# ----------------------- task 7 ------------------------


def fibonacci_calculator(n):
    """
    Calculates fibonacci sum of given quantity of counts. Calculates and in the negative side
    :param n: quantity of steps
    :return: Int. fibonacci total number
    """
    try:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == -1:
            return -1
        elif abs(n) > 1:
            total_num = 0
            back_num1 = 1
            back_num2 = 0
            for num in range(1, abs(n)):
                total_num = back_num1 + back_num2
                back_num2 = back_num1
                back_num1 = total_num
            if n < -1:
                return -total_num
            else:
                return total_num
    except Exception as ex:
        print("Error occurred!!!", ex)


print(fibonacci_calculator(10))
print(fibonacci_calculator(-10))
