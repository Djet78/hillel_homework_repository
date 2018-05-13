# ---------------------- homework_7 ------------------------

import re


def date_format_converter(convertions):
    """Convert from list`s with American date format to European """
    for date in convertions:
        print(re.sub(r"^'?(\d?\d)\.(\d?\d)\.(\d{4})'?$", r"'\2.\1.\3'", date))


dates_list = ["04.2.2007", "'3.8.2014", "'5.07.2016'", "11.07.1853"]
date_format_converter(dates_list)
