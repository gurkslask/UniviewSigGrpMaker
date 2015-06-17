
import re
import csv
from collections import defaultdict, namedtuple

__author__ = 'alexander'

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
        last_variable = dict_with_variable[variables][0]
        first_number = dict_with_variable[variables][0]
        resulting_list = []
        length = 1
        for variable in dict_with_variable[variables]:
            if variable - last_variable > interval:
                print(variables, first_number, last_variable - first_number)
                # If interval is big enough, add it to the list
                resulting_list.append(adress_register(
                    first_number,
                    make_div_by_sixteen(last_variable - first_number)
                    ))
                first_number = variable
                length = 0
            last_variable = variable
            length += 1
        # Add the trailing last numbers too
        resulting_list.append(adress_register(
            first_number,
            make_div_by_sixteen(last_variable - first_number)
            ))
        dict_with_variable[variables] = resulting_list
    return dict_with_variable


def make_output_file(dict_with_variables):
    value_dict = {
        'MO': '7',
        'CR': '3'
    }
    for prefix in dict_with_variables:
        for posts in dict_with_variables[prefix]:
            print('{:<5}{adress:<9}{length:<4}'.format(value_dict[prefix], adress=posts.UV_adress, length=posts.length), end='|')

def make_div_by_sixteen(an_int):
    temp_int = 0
    while an_int > temp_int:
        temp_int += 16
    return max(temp_int, 16)

def main():
    vars = remove_chars_from_string(open_csv_file('test.csv'))
    make_output_file(find_intervals_in_variables(vars))

if __name__ == '__main__':
    main()
