# ----------------------- task 10 ------------------------

from random import randint


def pretty_print(txt):
    for elem in txt:
        print(elem)


def saddle_point_finder(matrix):
    """
    Find all saddle points in given matrix
    :param matrix: takes given list of lists, that should contain only numbers
    :return: list of list with coordinates of saddle points, or empty list if no saddle points in given matrix
    """
    coordinates = []
    column_values = []
    for index, row in enumerate(matrix):
        lowest_point = min(row)
        i = row.index(lowest_point)
        for index2, elem in enumerate(row):
            if elem == lowest_point:
                for _ in matrix:
                    column_values = [column[i] for column in matrix]
                if elem == max(column_values):
                    coordinates.append([index, index2])
    return coordinates


custom_matrix = [[1, 3, 1, 1],
                 [2, 4, 3, 2],
                 [2, 4, 3, 2],
                 [2, 5, 7, 2]]

random_3x3_matrix = [[randint(-10, 10) for _ in range(3)] for _ in range(3)]
random_6x5_matrix = [[randint(-10, 10) for _ in range(6)] for _ in range(5)]

print("\nCustom matrix")
pretty_print(custom_matrix)
print("\n", saddle_point_finder(custom_matrix))

print("\n------------\n")

print("Random 3x3 matrix")
pretty_print(random_3x3_matrix)
print(saddle_point_finder(random_3x3_matrix))

print("\n------------\n")

print("Random 6x5 matrix")
pretty_print(random_6x5_matrix)
print("\n", saddle_point_finder(random_6x5_matrix))
