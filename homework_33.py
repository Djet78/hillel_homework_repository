# ------------------------ Task 33 -------------------------

import csv


def titanic_survivors_analyzer(file_obj):
    """
    Counts percentage of survival of 'Titanic' passengers

    Counts for each group of people depending on sex and class
    Read a CSV file using csv.DictReader
    :param file_obj: takes given file to read
    """
    reader = csv.DictReader(file_obj)
    survived = dict()
    passengers_total = dict()
    for line in reader:
        pattern = line["Sex"] + "_" + line["Pclass"] + "_class"
        if line["Pclass"] == "3":
            if line["Sex"] == "male":
                passengers_total[pattern] = passengers_total.get(pattern, 0) + 1
                if line["Survived"] == "1":
                    survived[pattern] = survived.get(pattern, 0) + 1
            else:
                passengers_total[pattern] = passengers_total.get(pattern, 0) + 1
                if line["Survived"] == "1":
                    survived[pattern] = survived.get(pattern, 0) + 1
        elif line["Pclass"] == "2":
            if line["Sex"] == "male":
                passengers_total[pattern] = passengers_total.get(pattern, 0) + 1
                if line["Survived"] == "1":
                    survived[pattern] = survived.get(pattern, 0) + 1
            else:
                passengers_total[pattern] = passengers_total.get(pattern, 0) + 1
                if line["Survived"] == "1":
                    survived[pattern] = survived.get(pattern, 0) + 1
        elif line["Pclass"] == "1":
            if line["Sex"] == "male":
                passengers_total[pattern] = passengers_total.get(pattern, 0) + 1
                if line["Survived"] == "1":
                    survived[pattern] = survived.get(pattern, 0) + 1
            else:
                passengers_total[pattern] = passengers_total.get(pattern, 0) + 1
                if line["Survived"] == "1":
                    survived[pattern] = survived.get(pattern, 0) + 1

    all_women_percent = ((survived['female_1_class'] + survived['female_2_class'] + survived['female_3_class']) * 100)\
                        / (passengers_total['female_1_class'] + passengers_total['female_2_class'] +
                           passengers_total['female_3_class'])

    all_men_percent = ((survived['male_1_class'] + survived['male_2_class'] + survived['male_3_class']) * 100)\
                        / (passengers_total['male_1_class'] + passengers_total['male_2_class'] +
                           passengers_total['male_3_class'])

    men_1st_class_percent = (survived['male_1_class'] * 100) / passengers_total['male_1_class']
    men_2nd_class_percent = (survived['male_2_class'] * 100) / passengers_total['male_2_class']
    men_3rd_class_percent = (survived['male_3_class'] * 100) / passengers_total['male_3_class']
    women_1st_class_percent = (survived['female_1_class'] * 100) / passengers_total['female_1_class']
    women_2nd_class_percent = (survived['female_2_class'] * 100) / passengers_total['female_2_class']
    women_3rd_class_percent = (survived['female_3_class'] * 100) / passengers_total['female_3_class']

    print("Percentage of Survival for men: ", round(all_men_percent, 2))
    print("Percentage of Survival for women: ", round(all_women_percent, 2))
    print("Percentage of Survival for men form 1st class: ", round(men_1st_class_percent, 2))
    print("Percentage of Survival for men form 2nd class: ", round(men_2nd_class_percent, 2))
    print("Percentage of Survival for men form 3rd class: ", round(men_3rd_class_percent, 2))
    print("Percentage of Survival for women form 1st class: ", round(women_1st_class_percent, 2))
    print("Percentage of Survival for women form 2nd class: ", round(women_2nd_class_percent, 2))
    print("Percentage of Survival for women form 3rd class: ", round(women_3rd_class_percent, 2))


if __name__ == "__main__":
    with open("titanic.csv") as f_obj:
        titanic_survivors_analyzer(f_obj)
