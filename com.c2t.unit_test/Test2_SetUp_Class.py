import unittest

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('cls=',cls)

    def setUp(self):
        print('This is setUp')

    def test_upper(self):
        print('test_upper')
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print('test_isupper')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def tearDown(self):
        print('This is tearDown')

if __name__ == '__main__':
    unittest.main()