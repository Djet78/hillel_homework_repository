# ------------------------ Task 29 -------------------------

from random import randint


def generate_password(quantity_off_passwords):
    """
    Generates passwords where at least one upper letter, one lower letter and one digit
    :param quantity_off_passwords: Quantity you wont to generate
    :return: Set. Containing randomly generated passwords
    """
    passwords_set = set({})
    lst = [chr(i) for i in range(ord("A"), ord("Z") + 1)] + [chr(i) for i in range(ord("a"), ord("z") + 1)]
    lst += [str(i) for i in range(0, 10)] + ["_"]
    while len(passwords_set) < quantity_off_passwords:
        random_password = ""
        for i in range(8):
            random_password += lst[randint(0, len(lst) - 1)]
        if random_password.islower():
            continue
        elif random_password.isupper():
            continue
        elif random_password.isnumeric():
            continue
        else:
            any_num = []
            for i in random_password:
                if i.isnumeric():
                    any_num.append(i)
            if len(any_num) == 0:
                continue
            else:
                passwords_set.add(random_password)
    return passwords_set


print(generate_password(5))
