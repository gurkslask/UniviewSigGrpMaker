__author__ = 'alexander'
import re
import csv
from collections import defaultdict

def open_csv_file(filename):
    with open(filename) as csvfile:
        variable_reader = csv.reader(csvfile)
        resulting_list = [variable[1] for variable in variable_reader]
        '''for row in variable_reader:
            print(row[1])
        '''
        print(resulting_list)
        return resulting_list

def remove_chars_from_string(string_list):
    resultin_dict = defaultdict(list)
    for variables in string_list:
        split_string = re.findall(r'([A-Z]*)([\d]*)', variables)
        resultin_dict[split_string[0][0]].append(int(split_string[0][1]))
    resultin_dict = dict(resultin_dict)
    print(resultin_dict)
    return resultin_dict

def find_intervals_in_variables(variables):
    variables.sort()
    interval = 32
    last_variable = 0
    resulting_list = []
    for variable in variables:
        if variable - last_variable > interval:
            resulting_list.append(variable)
    return resulting_list

def main():
    vars = remove_chars_from_string(open_csv_file('test.csv'))
    for i in vars:
        print(find_intervals_in_variables(vars[i]))

if __name__ == '__main__':
    main()
