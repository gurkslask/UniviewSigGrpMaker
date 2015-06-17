
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
    max_time_interval = 5
    time_interval = 0
    value_dict = {
        'MO': ['7', '2'],
        'CR': ['3', '1']
    }
    result_list = []
    for prefix in dict_with_variables:
        for posts in dict_with_variables[prefix]:
            result_string = '{prefix:<5}{adress:<9}{length:<4}{type:<5}{adress:<9}{type:<5}{adress:<9}{max_interval:<9}{interval:<9}{max_interval:<9}{interval:<9}1'.format(prefix=value_dict[prefix][0], adress=posts.UV_adress, length=posts.length, type=value_dict[prefix][1], interval=time_interval, max_interval=max_time_interval)
            result_list.append(result_string)
            if time_interval == max_time_interval:
                time_interval = 0
            time_interval += 1
        time_interval = 0
    print('|\n'.join(result_list))
    return '|'.join(result_list)


def make_div_by_sixteen(an_int):
    temp_int = 0
    while an_int > temp_int:
        temp_int += 16
    return max(temp_int, 16)


def main():
    vars = remove_chars_from_string(open_csv_file('/home/alex/Documents/defreg.csv'))
    with open('test.txt', 'w') as f:
        f.write(make_output_file(find_intervals_in_variables(vars)))

if __name__ == '__main__':
    main()
