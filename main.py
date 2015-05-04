__author__ = 'alexander'
import re
import csv
from collections import defaultdict, namedtuple

adress_register = namedtuple('adress_register', ['UV_adress', 'length'])

def open_csv_file(filename):
    with open(filename) as csvfile:
        variable_reader = csv.reader(csvfile)
        resulting_list = [variable[1] for variable in variable_reader]
        return resulting_list

def remove_chars_from_string(string_list):
    '''
    Filter out data
    '''
    resultin_dict = defaultdict(list)
    for variables in string_list:
        split_string = re.findall(r'([A-Z]*)([\d]*)', variables)
        resultin_dict[split_string[0][0]].append(int(split_string[0][1]))
    resultin_dict = dict(resultin_dict)
    return resultin_dict

def find_intervals_in_variables(dict_with_variable):
    '''
    Make a variable list
    '''
    for variables in dict_with_variable:
        dict_with_variable[variables].sort()
        interval = 32
        last_variable = -32
        resulting_list = []
        length = 0
        for variable in dict_with_variable[variables]:
            if variable - last_variable > interval:
                resulting_list.append(adress_register(variable, make_div_by_sixteen(length)))
                length = 0
            last_variable = variable
            length += 1
        dict_with_variable[variables] = resulting_list
    return dict_with_variable

def make_output_file(dict_with_variables):
    value_dict = {
        'MO': '7',
        'CR': '3'
    }
    for prefix in dict_with_variables:
        for posts in dict_with_variables[prefix]:
            print('{:<5}{:<9}{:<4}'.format(value_dict[prefix], posts, posts), end='|')

def make_div_by_sixteen(an_int):
    temp_int = 0
    while an_int > temp_int:
        temp_int += 16
    return temp_int

def main():
    vars = remove_chars_from_string(open_csv_file('test.csv'))
    make_output_file(find_intervals_in_variables(vars))

if __name__ == '__main__':
    main()
