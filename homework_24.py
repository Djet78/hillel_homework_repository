# ------------------------ Task 24 -------------------------


def group_by_surname(list_of_enrollees):
    """
    Split given list by ' ' and create lists in list. Then, in 'for' cycle, take every first letter of surname, and by
    that letter insert student in appropriate list
    :param list_of_enrollees: takes given list format == ['Name1 Surname1', 'Name2 Surname2', 'Name3 Surname3', ...]
    :return: quantity of enrollees of each group
    """
    group_a_i = []
    group_j_p = []
    group_q_t = []
    group_u_z = []
    list_of_enrollees = [i.split(" ") for i in list_of_enrollees]
    for i in list_of_enrollees:
        if ord(i[1][0]) in range(ord("A"), ord("I") + 1):
            group_a_i.append(i)
        elif ord(i[1][0]) in range(ord("J"), ord("P") + 1):
            group_j_p.append(i)
        elif ord(i[1][0]) in range(ord("Q"), ord("T") + 1):
            group_q_t.append(i)
        elif ord(i[1][0]) in range(ord("U"), ord("Z") + 1):
            group_u_z.append(i)
    return len(group_a_i), len(group_j_p), len(group_q_t), len(group_u_z)


enrollees = ["Will Smith", "Lui Anderson", "Luke Skywalker", "Darth Weider", "R2 D2", "Fifty Cent", "Johny Cage",
             "Maksim Kozlov", "Dmitryi Lokot`", "Davey Jones", "Jack Sparrow(Captain)", "Darth Mol", "Max Fry"]

print(group_by_surname(enrollees))
