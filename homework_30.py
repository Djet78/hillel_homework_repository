# ------------------------ Task 30 -------------------------


def gen_primes(n):
    """
    Generate primes in given range 'n'
    :param n: define range
    :return: list. All prime numbers on given range 'n'
    """
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


print(gen_primes(150))
