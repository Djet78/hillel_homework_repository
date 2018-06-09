# ----------------------- task 11 ------------------------

from random import randint


def pretty_print(txt):
    for elem in txt:
        print(elem)


def even_odd_column_sort(matrix):
    """
    In given matrix sort even columns in ascending order, and odd ones in descending order
    :param matrix: takes given list of lists, that should contain only numbers
    :return: modified matrix
    """
    column_num = 0
    for i, row in enumerate(matrix):
        container = []
        try:
            for i2 in range(len(matrix)):
                container.append(matrix[i2][i])
            column_num += 1
            if column_num % 2 == 0:
                container.sort()
            else:
                container.sort(reverse=True)
            for i2 in range(len(matrix)):
                matrix[i2][i] = container[i2]
        except IndexError:
            return matrix
    return matrix


custom_list = [[1, 1, 1, 1],
               [2, 2, 2, 2],
               [3, 3, 3, 3],
               [4, 4, 4, 4],
               [5, 5, 5, 5],
               [6, 6, 6, 6]]
print("Custom list")
pretty_print(custom_list)
print("-------------------------------------")
pretty_print(even_odd_column_sort(custom_list))

print("-------------------------------------")

random_list = [[randint(1, 20) for _ in range(5)] for _ in range(5)]
print("Random list")
pretty_print(random_list)
print("-------------------------------------")
pretty_print(even_odd_column_sort(random_list))
