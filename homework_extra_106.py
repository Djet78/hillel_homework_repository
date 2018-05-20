# ------------------------ Task 106 -------------------------
import re


def extract_company_name(email):
    lst_extracted_name = re.findall(r"^.+@(\w+)\.com$", email)
    extracted_name = lst_extracted_name[0]
    return extracted_name


print(extract_company_name("sergey@google.com"))
