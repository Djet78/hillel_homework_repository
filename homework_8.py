# ---------------------- homework_8 ------------------------

import re


def name_swap(name):
    """Swap name and surname, in list"""
    for swap in name:
        print(re.sub(r"^(\w+)\s*(\w+)$", r"\2 \1", swap))


name_list = ["Mark Zuckerberg", "Dima Molot", "Hans Zimmer"]
name_swap(name_list)
