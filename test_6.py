# ----------------------- task 6 ------------------------


def is_string_isogram(text):
    """
    Checks is given word an isogram
    :param text: takes given string
    :return: boolean value
    """
    text = text.replace(" ", "")
    text = text.lower()
    for i, elem in enumerate(text):
        repetitions = text.count(elem, i, len(text))
        if repetitions > 1:
            return False
    return True


def is_list_isogram(lst):
    """
    Checks are all words in given list an isogram
    :param lst: takes given string
    :return: boolean value
    """
    for elem in lst:
        elem = elem.replace(" ", "")
        elem = elem.lower()
        for i, char in enumerate(elem):
            repetitions = elem.count(char, i, len(elem))
            if repetitions > 1:
                return False
    return True


isogram_word = 'Питон'
not_isogram_word = "Disappear"
isogram_list = ['Питон', "able", "gift", "fish"]
not_isogram_list = ['Питон', "able to", "gift", "fish", "КНигА без названия"]


print("Is '" + isogram_word + "' an isogram?\n", is_string_isogram(isogram_word))
print("Is '" + not_isogram_word + "' an isogram?\n", is_string_isogram(not_isogram_word))


print("Is all elements in", isogram_list, "an isogram?\n", is_list_isogram(isogram_list))
print("Is all elements in", not_isogram_list, "an isogram?\n", is_list_isogram(not_isogram_list))
