# ------------------------ Task 25 -------------------------


from random import randint


def shuffle_list(list_to_shuffle):
    """
    Shuffles all data in given list between each other
    :param list_to_shuffle: takes given list
    :return: None
    """
    shuffled_list = []
    for i in list_to_shuffle:
        shuffled_list.insert(randint(1, 100), i)
    print(shuffled_list)


lst = range(1, 100)[::2]
shuffle_list(lst)
