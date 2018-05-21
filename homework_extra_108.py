# ------------------------ Task 108 -------------------------


def remove_duplicate(lst):
    """
    removes all duplicate values with original order reserved
    :param lst: takes given list
    :return: list without duplications
    """
    removed_dupl = []
    for i in lst:
        if i not in removed_dupl:
            removed_dupl.append(i)
    return removed_dupl


list_with_duplications = [100, 33, 33, 17, 29, 4, 4, 75, 4, 33, 17, 100]
print(remove_duplicate(list_with_duplications))
