# ------------------------ Task 29 -------------------------

from random import choice
import string


def generate_password(quantity_off_passwords):
    """
    Generates passwords where at least one upper letter, one lower letter and one digit
    :param quantity_off_passwords: Quantity you wont to generate
    :return: Set. Containing randomly generated passwords
    """
    passwords_set = set({})
    symbols = string.ascii_letters + string.digits + "_"
    while len(passwords_set) < quantity_off_passwords:
        random_password = ""
        for i in range(8):
            random_password += choice(symbols)
        is_correct = all(any(1 for c in random_password if c in pattern)
                         for pattern in [string.digits, string.ascii_lowercase, string.ascii_uppercase])
        if is_correct:
            passwords_set.add(random_password)

    return passwords_set


print(generate_password(5))
