# ---------------------- homework_12 ------------------------


def sum_of_digits(number):
    """
    Using string
    """
    added_digits = 0
    try:
        if len(number) == 3:
            added_digits = int(number[0]) + int(number[1]) + int(number[2])
        else:
            print("Only three-digit number accepted")
    except ValueError:
        print("Only three-digit number accepted")
    return added_digits


def sum_of_digits_2(number2):
    """
    Without using string
    """
    total = 0
    try:
        if len(number2) == 3:
            first_digit = int(number2) // 100
            second_digit = (int(number2) // 10) % 10
            third_digit = int(number2) % 10
            total = first_digit + second_digit + third_digit
        else:
            print("Only three-digit number accepted")
    except ValueError:
        print("Only one, two or three-digit number accepted")
    return total


print("Input three-digit number and you add them between each-other.\nEnter your first number below:")
user_number = input()
print("Enter your second number below:")
user_number2 = input()
print("First number =", sum_of_digits(user_number))
print("Second number =", sum_of_digits_2(user_number2))
