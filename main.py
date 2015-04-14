__author__ = 'alexander'
import re
import csv

def open_csv_file(filename):
    with open

def remove_chars_from_string(string_list):
    resultin_list = [int(re.sub('[a-z]', '', ints.lower())) for ints in string_list]
    return resultin_list

def find_intervals_in_variables(variables):
    variables.sort()
    interval = 32
    last_variable = 0
    resulting_list = [variables[0]]
    for variable in variables:
        if variable - last_variable > interval:
            resulting_list.append(variable)
    return resulting_list


