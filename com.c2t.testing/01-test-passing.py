import unittest
from name_function import get_formatted_name_first_last, get_formatted_name_first_middle_last

class NamedTestCase(unittest.TestCase):

    def test_firstName(self):
        expected = 'Naresh Chaurasia'
        actual = get_formatted_name_first_last('naresh','chaurasia')
        self.assertEqual(actual,expected,'The excected and actual values do not match...')


unittest.main()

