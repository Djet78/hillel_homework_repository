# ------------------------ Task 34 -------------------------
from random import randint


class Gorilla:

    def __init__(self, stomach_volume):
        self.stomach_volume = stomach_volume
        self.stomach_fullness = 0
        self.EATING_LIMIT = 0.9

    def eat(self, human_volume):
        if self.stomach_fullness >= self.stomach_volume * self.EATING_LIMIT:
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
