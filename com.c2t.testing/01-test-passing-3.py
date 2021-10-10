import unittest

from name_function import get_formatted_name_first_last

class MyTestClass(unittest.TestCase):

    def setUp(self):
        print('connect to db...')
        self.connection = 'connect to db...'

    def test_fname_lname1(self):
        print('test_fname_lname1')

    def test_fname_lname2(self):
        print('test_fname_lname2')

unittest.main()