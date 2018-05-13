# ------------------------------------------------------------
#                            extra hv
# ------------------------------------------------------------

import re

# -------------------------- Task 100 -------------------------

print("\nTask 100:")
print("If expression matches with regex print 'Yes' or 'No' instead\n")


def regex_check(regex, text):
    """Funct. takes 2 parameters. It`s regex and some text to check it out. And output 'Yes' for full match or 'No' """
    check = re.fullmatch(regex, text)
    print('\tYES' if check else '\tNO')


Checks = ["0x012345", "0xa1b2c3", "0xdeadbeef", "0x0x0x0x", "0123abcd", "0xabcdefg"]
for sequence in Checks:
    print(sequence)
    regex_check(r"(?i)0x([A-F0-9])+\b", sequence)


# -------------------------- Task 101 -------------------------

print("\nTask 101:")
print("If expression matches with regex print 'Yes' or 'No' instead\n")
Checks = ["mfn-fulfillable-quantity", "afn-fulfillable-quantity", "afn-total-quantity",
          "afn-inbound-receiving-quantity", "per-unit-volume", "mfn-listing-list-exists", "afn-listing-exists"]
for sequence in Checks:
    print(sequence)
    regex_check(r"(mfn-|afn-)(\w+-?(?!exists))*", sequence)


# -------------------------- Task 102 -------------------------

print("\nTask 102")


def file_names_to_hyperlinks_transformer(file_list):
    """Uses 2 regexes: first - to parse filename, another - to construct html code on its basis"""
    for documents in file_list:
        print(re.sub(r"(\w+)\.(\w+)$", r'<A HREF="\1.\2" >\1</A>', documents))


file_names = ["SomeDocument1.docx", "SomeDocument2.docx", "SomeDocN.docx"]
print("File names: ", file_names)
print("Hyperlinks: ")
file_names_to_hyperlinks_transformer(file_names)
