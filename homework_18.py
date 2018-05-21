# ---------------------- homework_17 ------------------------


def sum_symbol_codes(first, last):
    """
    :return: Int. Total sum of symbols unicodes
    """
    total_sum = 0
    for unicode in range(ord(first), ord(last)+1):
        total_sum += unicode
    return total_sum


print(sum_symbol_codes("x", "x"))
