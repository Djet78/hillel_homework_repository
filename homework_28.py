# ------------------------ Task 28 -------------------------

import string


def shift_str(str_to_encode, shift):
    """
    Change chars in given string on chars from encryption table with given shift

    :return: Str. Encoded string
    """
    encryption_table = string.ascii_lowercase + string.digits
    encoded_string = ""
    for i, char in enumerate(str_to_encode.lower()):
        if char in encryption_table:
            idx = encryption_table.index(char)
            new_idx = (idx + shift) % len(encryption_table)
            encoded_string += encryption_table[new_idx]
    return encoded_string


def encode(string):
    """
    Encodes given string
    :return: func which return encoded string
    """
    return shift_str(string, 5)


def decode(string):
    """
    Decodes given string
    :return: func which return decoded string
    """
    return shift_str(string, -5)


print(encode("duff"))

print(decode("izkk"))
