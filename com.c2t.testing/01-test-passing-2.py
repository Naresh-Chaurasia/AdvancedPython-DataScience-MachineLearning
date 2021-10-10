import unittest

from name_function import get_formatted_name_first_last

class MyTestClass(unittest.TestCase):

    def setUp(self):
        print('connect to db...')

    def test_fname_lname1(self):
        fname_lname = get_formatted_name_first_last('naresh', 'chaurasia')
        #print(fname_lname)
        self.assertEqual(fname_lname,'Naresh Chaurasia1')

    def test_fname_lname2(self):
        fname_lname = get_formatted_name_first_last('naresh', 'chaurasia')
        # print(fname_lname)
        self.assertEqual(fname_lname, 'Naresh Chaurasia')



unittest.main()
