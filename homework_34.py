# ------------------------ Task 33 -------------------------
from random import randint


class Gorilla:

    stomach_fullness = 0

    def __init__(self, stomach_volume):
        self.stomach_volume = stomach_volume

    def eat(self, human_volume):
        if self.stomach_fullness >= self.stomach_volume * 0.9:
            print("I am full")
        elif (self.stomach_fullness + human_volume) <= self.stomach_volume:
            self.stomach_fullness += human_volume
        else:
            print("I can't eat it, it's too much for me, give me another one")


def generate_human():
    """
    :return: int. Human volume
    """
    return randint(1, 42)


abe = Gorilla(100)

abe.eat(generate_human())
abe.eat(generate_human())
abe.eat(generate_human())
abe.eat(generate_human())
abe.eat(generate_human())
