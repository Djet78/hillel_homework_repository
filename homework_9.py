# ---------------------- homework_9 ------------------------


def snake_style_converter(phrase):
    """
    Func. takes given string, removes all '_' between words and saves in 'phrase'.
    First 'for' cycle takes words from  'phrase', makes first letters capitals and saves in 'phrase_cap'.
    Second 'for' cycle takes words from  'phrase_cap' and adds up them in 'camel_case'
    At last displays 'camel_case' phrase on the screen
    """
    try:
        phrase = phrase.split("_")
        phrase_cap = []
        camel_case = ""
        for sequence in phrase:
            word_cap = sequence.capitalize()
            phrase_cap.append(word_cap)
        for sequence in phrase_cap:
            camel_case += sequence
        print(camel_case)
    except AttributeError:
        print("\n\tERROR:\n\tType of variable given to func. was wrong, it`s should be string")


print("\nSnake style string: 'employee_first_name_and_second_name'\nTransforms into a Camel case string:")
snake_style_converter("employee_first_name_and_second_name")
