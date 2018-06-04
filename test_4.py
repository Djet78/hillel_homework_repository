# ----------------------- task 4 ------------------------
# First variant


def not_even_digits_multiply_1():
    """
    Multiply all not even digits in number
    :return: Int. multiplied value
    """
    try:
        num = input("Enter your number, and program multiply all not even digits in it: ")
        total = 1
        for digit in num:
                if not int(digit) % 2 == 0:
                    total *= int(digit)
        return total
    except Exception as ex:
        print("Error!! You have entered non digit symbol: ", ex)


print(not_even_digits_multiply_1())
# Second variant


def not_even_digits_multiply_2():
    """
    Multiply all not even digits in number
    :return: Int. multiplied value
    """
    try:
        num = int(input("Enter your number, and program multiply all not even digits in it: "))
        total = 1
        lst_of_digits = []
        while num != 0:
            lst_of_digits.append(num % 10)
            num = num // 10
        for digit in lst_of_digits:
            if not digit % 2 == 0:
                total *= digit
        return total
    except Exception as ex:
        print("Error!! You have entered non digit symbol: ", ex)


print(not_even_digits_multiply_2())
