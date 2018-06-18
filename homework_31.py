# ------------------------ Task 31 -------------------------

import pickle


running = True

#------------------------------------------------------------------------------
phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number": "+380501234567", "comment": "None"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number": "+380507654321", "comment": "None"},
             ]


#------------------------------------------------------------------------------
def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Phone:   %20s |" % entry["phone_number"])
    print ("| Comment:   %18s |" % entry["comment"])
    print ()


#------------------------------------------------------------------------------
def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name    = input("    Enter name: ")
    age     = int(input("    Enter age: "))
    phone_number   = input("    Enter phone num.: ")
    comment     = input("    Enter comment")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    entry["comment"] = comment
    phone_book.append(entry)


#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)


#------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input("    Enter age: "))
    found = False
    for idx,  entry in enumerate(phone_book):
        if entry["age"] == age:
            print_entry(idx, entry)
            found = True
    if not found:
        printError("Not found!!")

#------------------------------------------------------------------------------
def delete_entry_name_phonebook():
    name = str(input("    Enter name: "))
    found = False
    for idx, entry in enumerate(phone_book):
        if entry["name"] == name:
            phone_book.remove(phone_book[idx])
            print("    %s was deleted." % name)
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))


#------------------------------------------------------------------------------
def print_phonebook_by_age():
    print()
    print()
    print("#########  Phone book  ##########")
    print()

    number = 1
    for entry in sorted(phone_book, key=lambda x: x["age"]):
        print_entry(number, entry)
        number += 1

#------------------------------------------------------------------------------
def increase_age():
    increase = int(input("    Enter age amount to increase: "))
    for i in phone_book:
        i["age"] += increase
    print("    Age increased.")

#------------------------------------------------------------------------------
def avr_age_of_all_persons():
    total_age = 0
    for i in phone_book:
        total_age += i["age"]
    print("| Average age: %4.f |" % (total_age / len(phone_book)))

#------------------------------------------------------------------------------
def change_number():
    try:
        idx = int(input("    Enter id of person: "))
        if phone_book[idx] in phone_book:
            number = str(input("    Enter new number: "))
            phone_book[idx]["phone_number"] = number
            print("    Number changed.")
    except Exception:
        printError("Not found!!")

#------------------------------------------------------------------------------
def add_change_comment():
    try:
        idx = int(input("    Enter id of person: "))
        if phone_book[idx] in phone_book:
            comment = str(input("    Enter your comment: "))
            phone_book[idx]["comment"] = comment
            print("    Comment changed.")
    except Exception:
        printError("Not found!!")

#------------------------------------------------------------------------------
def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


#------------------------------------------------------------------------------
def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


#------------------------------------------------------------------------------
def exit():
      global running
      running = False


#------------------------------------------------------------------------------
def print_prompt():
      print()
      print()
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1 - Print phonebook entries")
      print("     2 - Print phonebook entries (by age)")
      print("     3 - Add new entry")
      print("     4 - Find entry by name")
      print("     5 - Find entry by age")
      print("     6 - Delete entry by name")
      print("     7 - The number of entries in the phonebook")
      print("     8 - Avr. age of all persons")
      print("     9 - Increase age by num. of years")
      print("     10 - change number")
      print("     11 - add / change comment")
      print("-----------------------------")
      print("     s - Save to file")
      print("     l - Load from file")
      print("     0 - Exit")
      print()


#------------------------------------------------------------------------------
def main():

    while running:
        try:

            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '6':  delete_entry_name_phonebook,
                  '7':  count_all_entries_in_phonebook,
                  '8':  avr_age_of_all_persons,
                  '9':  increase_age,
                  '10': change_number,
                  '11': add_change_comment,

                  '0':  exit,
                  's':  save_to_file,
                  'l':  load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
