# ------------------------ Task 25 -------------------------

from random import randint

# def shuffle_list(list_to_shuffle):
#     """
#     Shuffles all data in given list between each other with creating new list
#     :param list_to_shuffle: takes given list
#     :return: None
#     """
#     shuffled_list = []
#     for i in list_to_shuffle:
#         shuffled_list.insert(randint(1, 100), i)
#     print(shuffled_list)
#
#
# def shuffle_list2(list_to_shuffle):
#     """
#     Shuffles all data in given list between each other w/o creating new list
#     :param list_to_shuffle: takes given list
#     :return: None
#     """
#     for _ in list_to_shuffle:
#         list_to_shuffle.insert(randint(1, 20), list_to_shuffle.pop())
#     print(list_to_shuffle)


def shuffle_list3(list_to_shuffle):
    """
    Shuffles all data in given list between each other w/o creating new list
    :param list_to_shuffle: takes given list
    :return: None
    """
    for _ in list_to_shuffle:
        list_to_shuffle.append(list_to_shuffle.pop(randint(1, 10)))
    print(list_to_shuffle)


lst = list(range(1, 100)[::2])
shuffle_list3(lst)
