# ------------------------ Task 22 -------------------------

from random import randint

guessed_number = randint(1, 10)
print("Let`s try guess a number from 1 to 10\nEnter your number below: ")
user_number = 0

while user_number != guessed_number:
    try:
        user_number = int(input())
        if user_number not in range(1, 10 + 1):
            print("You are allowed enter number from 1 to 10, plz, write another number below:")
        elif user_number > guessed_number:
            print("No, actual number lower, write new number below: ")
        elif user_number < guessed_number:
            print("No, actual number higher, write new number below: ")
        elif user_number == guessed_number:
            print("Exactly! You guessed! From first attempt! ;)")
    except ValueError:
        print("You can write only 'int' numbers, plz, write number below:")
