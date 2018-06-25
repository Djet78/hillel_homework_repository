# ------------------------ Task 33 -------------------------

import csv


def distribution_of_survivals(file_obj, field_name):
    """
    Counts percentage of survival of 'Titanic' passengers

    Counts for each group of people depending on sex and class
    Read a CSV file using csv.DictReader
    :param file_obj: takes given file to read
    :param field_name: takes column name from CSV
    """
    reader = csv.DictReader(file_obj)
    survived = dict()
    passengers_total = dict()
    for line in reader:
        pattern = line[field_name]
        passengers_total[pattern] = passengers_total.get(pattern, 0) + 1
        if line["Survived"] == "1":
            survived[pattern] = survived.get(pattern, 0) + 1
    for value in sorted(passengers_total.items()):
        percentage_of_survival = round((survived[value[0]] * 100) / passengers_total[value[0]], 2)
        print("{}: {} percent has survived".format(value[0], percentage_of_survival))


if __name__ == "__main__":
    with open("titanic.csv") as f_obj:
        distribution_of_survivals(f_obj, "Pclass")
