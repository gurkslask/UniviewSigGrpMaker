__author__ = 'alexander'

from main import find_intervals_in_variables,\
    remove_chars_from_string
import unittest

class test_find_intevals(unittest.TestCase):
    def setUp(self):
        self.test_list = [
            1, 2, 3, 4, 64, 128
        ]
    def test_variables_1(self):
        self.assertListEqual(find_intervals_in_variables(self.test_list), [1, 64, 128])

class test_remove_function(unittest.TestCase):
    def setUp(self):
        self.test_str_1 = [
            'CR12', 'CR13', 'MO449', 'LEET1337'
        ]
        self.test_result_1 = [
            12, 13, 449, 1337
        ]
    def test_func_1(self):
        self.assertListEqual(remove_chars_from_string(self.test_str_1), self.test_result_1)

if __name__ == '__main__':
    unittest.main()
