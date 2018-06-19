# ------------------------ Task 27 -------------------------

import random


def permute(text):
    """
    Permute text with given algorithm:
    For each word in the text:
        1. Fix the first and last characters of the word.
        2. Words with three or less letters ignored
        3. From the remaining we take the first three symbols, arbitrarily mixed.
        4. The resulting triplet is fixed, i.e. it will no longer participate in further mixing.
        5. Repeat step 2 until the uncommitted characters end.
    :param text: takes given text
    :return: Str. Permuted text
    """
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
                    to_shuffle = []
                    permuted_letters = ""
                    for letter in word[1:-1]:
                        to_shuffle.append(letter)
                        if len(to_shuffle) == 3:
                            random.shuffle(to_shuffle)
                            permuted_letters += "".join(to_shuffle)
                            to_shuffle = []
                    random.shuffle(to_shuffle)
                    permuted_letters += "".join(to_shuffle)
                    word = word[0] + permuted_letters + word[-1]
                permuted_txt += word
            word = ""
            permuted_txt += char
    return permuted_txt


txt = "Напишите функцию, которая преобразует переданный ей текст способом, похожим на описанный выше. " \
      "В качестве алгоритма перемешивания букв в слове используйте следующий:"

print(permute(txt))
