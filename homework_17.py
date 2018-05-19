# ---------------------- homework_17 ------------------------
import math


def solve_quadratic_equation(a, b, c):
    """
    Func. solves quadratic equation
    :param a: takes number that don`t equal to 0
    :param b: takes number
    :param c: takes number
    :return: 2 values: either 2 roots, 1 root and None or 2 Nones
    """
    if a != 0:
        d = b**2 - 4*a*c
        # d = discriminant
        if d > 0:
            first_root = (-b + math.sqrt(d)) / (2 * a)
            second_root = (-b - math.sqrt(d)) / (2 * a)
            return first_root, second_root
        elif d == 0:
            root = -(b / (2 * a))
            return root, None
        elif d < 0:
            return None, None
    else:
        print("Variable 'a' can`t be equal 0")


print(solve_quadratic_equation(4, 7, 2))
