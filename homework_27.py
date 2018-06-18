# ------------------------ Task 27 -------------------------

import random


def permute(text):
    letters = [chr(i) for i in range(ord("а"), ord("я") + 1)]
    word = ""
    permuted_txt = ""
    for char in txt:
        if char.lower() in letters:
            word += char
        else:
            if len(word) < 4:
                permuted_txt += word
            else:
                if len(word) == 4:
                    word = word[0] + word[2] + word[1] + word[3]
                else:
                    first_letter = word[0]
                    last_letter = word[-1]
                    word = list(word[1:-1])
                    random.shuffle(word)
                    word = first_letter + "".join(word) + last_letter
                permuted_txt += word
            word = ""
            permuted_txt += char
    return permuted_txt


txt = "Напишите функцию, которая преобразует переданный ей текст способом, похожим на описанный выше. " \
      "В качестве алгоритма перемешивания букв в слове используйте следующий:"

print(permute(txt))
