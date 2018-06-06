# ------------------------ Task 25 -------------------------

from random import randint


not_even_list = [i for i in range(1, 100, 2)]
print(not_even_list)
not_even_list.sort(key=lambda elem: elem + randint(1, 100))
print(not_even_list)
