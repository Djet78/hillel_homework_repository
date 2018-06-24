def is_valid_credit_card(credit_card):
    """
    Given a value determine whether or not it is valid per the Luhn formula.

    The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, such as
    credit card numbers.

    The task is to check if a given string is valid.
    Strings of length 1 or less are not valid. Spaces are allowed in the input, but they should be stripped before
    checking. All other non-digit characters are disallowed.

    Example 1: valid credit card number

        4539 1488 0343 6467

        Step 1
        The first step of the Luhn algorithm is to double every second digit, starting from the right. We will be
        doubling
        4_3_ 1_8_ 0_4_ 6_6_

        Step 2
        If doubling the number results in a number greater than 9 then subtract 9 from the product.
        The results of our doubling:
        8569 2478 0383 3437

        Step 3
        Then sum all of the digits:
        8+5+6+9+2+4+7+8+0+3+8+3+3+4+3+7 = 80

        Step 4
        If the sum is evenly divisible by 10, then the number is valid. This number is valid!

    Example 2: invalid credit card number

        8273 1232 7352 0569

        Step 1, 2
        Double the second digits, starting from the right
        7253 2262 5312 0539

        Step 3
        Sum the digits
        7+2+5+3+2+2+6+2+5+3+1+2+0+5+3+9 = 57

        Step 4
        57 is not evenly divisible by 10, so this number is not valid.

    :param credit_card: credit card to check (string)
    :return: True if valid, False otherwise
    """

    # _-_-_-_-_-_-_ Step 1, 2 _-_-_-_-_-_-_

    credit_card = "".join(credit_card.split())
    modified_card = ""
    for idx, num in enumerate(credit_card):
        if (idx % 2) == 0:
            num = int(num) * 2
            if num > 9:
                num -= 9
                modified_card += str(num)
            else:
                modified_card += str(num)
        else:
            modified_card += num

    # _-_-_-_-_-_-_ Step 3 _-_-_-_-_-_-_

    added_digits = 0
    for num in modified_card:
        added_digits += int(num)

    # _-_-_-_-_-_-_ Step 4 _-_-_-_-_-_-_

    if (added_digits % 10) == 0:
        return True
    else:
        return False


print(is_valid_credit_card("4539 1488 0343 6467"))
print(is_valid_credit_card("8273 1232 7352 0569"))
