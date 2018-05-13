# ---------------------- homework_10 ------------------------


def name_and_age_output(information):
    """
    Func. takes format string: 'Name Surname*YYYY-MM-DD*YYYY-MM-DD'. Split them and removes '-' and '*'
    Count years of living and print it with name and surname
    """
    try:
        information = information.split("*")
        information[1] = information[1].split("-")
        information[2] = information[2].split("-")
        print(information[0] + ",", str(int(information[2][0]) - int(information[1][0])) + "'")
    except (AttributeError, IndexError):
        print("\n\tERROR:\n\tType of variable given to func. was wrong, it`s should be format string: "
              "'Name Surname*YYYY-MM-DD*YYYY-MM-DD'.\n\tWhere first 'YYYY-MM-DD' - date of birth and "
              "second - date of death")


name_and_age_output('Leo Tolstoy*1828-08-28*1910-11-20')
name_and_age_output('Marcus Aurelius*121-04-26*180-03-17')
