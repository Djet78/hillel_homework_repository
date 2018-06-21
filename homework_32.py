# ------------------------ Task 32 -------------------------
import string
# import operator


def count_words(file_path_text, file_path_stop_words, top_n):
    """
    Counts words in given text file, exception 'stop' words from given file

    :param top_n: Determines quantity of returning words in list
    :return: List of tuples
    """
    letters = list(string.ascii_letters)

    stop_words = open(file_path_stop_words)
    lst_stop_words = stop_words.read().split('\n')
    stop_words.close()

    text = open(file_path_text)
    words_dict = {}
    word = ""
    for char in text.read().lower():
        if char in letters:
            word += char
        else:
            if word not in lst_stop_words:
                words_dict[word] = words_dict.get(word, 0) + 1
            word = ""
    text.close()

    # sorted_lst_words = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)
    sorted_lst_words = sorted(words_dict, key=words_dict.get, reverse=True)
    top_n_lst = []
    for i in range(top_n):
        top_n_lst.append(sorted_lst_words[i])
    return top_n_lst


print(count_words(r'1984_part_1.txt', r'stop_words.txt', 5))
