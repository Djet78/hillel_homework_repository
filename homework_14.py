# ---------------------- homework_14 ------------------------


def is_even(number):
        number = number % 2
        if number == 0:
            return True
        else:
            return False


print("Input a number to check it even or not: ")
try:
    input_number = int(input())
    print(is_even(input_number))
except ValueError:
    print("You are allowed to enter only integers")
