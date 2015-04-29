__author__ = 'alexander'
import re
import csv
from collections import defaultdict

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
        for variable in dict_with_variable[variables]:
            if variable - last_variable > interval:
                resulting_list.append(variable)
            last_variable = variable
        dict_with_variable[variables] = resulting_list
    return dict_with_variable

def make_output_file(dict_with_variables):
    print(dict_with_variables)
    value_dict = {
        'MO': '14',
        'CR': '13'
    }
    for prefix in dict_with_variables:
        for posts in dict_with_variables[prefix]:
            print('{}    {}'.format(value_dict[prefix], posts), end='|')


def main():
    vars = remove_chars_from_string(open_csv_file('test.csv'))
    make_output_file(find_intervals_in_variables(vars))

if __name__ == '__main__':
    main()
