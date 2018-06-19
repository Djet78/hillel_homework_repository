# ------------------------ Task 32 -------------------------
import string
import operator


def count_words(file_path_text, file_path_stop_words, top_n):
    """
    Counts words in given text file, exception 'stop' words from given file

    :param top_n: Determines quantity of returning words in list
    :return: List of tuples
    """
    letters = [_ for _ in string.ascii_letters]

    stop_words = open(file_path_stop_words)
    stop_word = ""
    lst_stop_words = []
    for char in stop_words.read():
        if char in letters:
            stop_word += char
        else:
            lst_stop_words.append(stop_word)
            stop_word = ""
    stop_words.close()

    text = open(file_path_text)
    lst_words = {}
    word = ""
    for char in text.read().lower():
        if char in letters:
            word += char
        else:
            if word not in lst_stop_words:
                if word not in lst_words:
                    lst_words[word] = 1
                else:
                    lst_words[word] += 1
            word = ""
    text.close()

    sorted_lst_words = sorted(lst_words.items(), key=operator.itemgetter(1), reverse=True)
    top_n_lst = []
    for i in range(top_n + 1):
        top_n_lst.append(sorted_lst_words[i])
    return top_n_lst


print(count_words(r'1984_part_1.txt', r'stop_words.txt', 5))
