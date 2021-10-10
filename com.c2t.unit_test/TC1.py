import unittest

class TestStringMethods1(unittest.TestCase):

    def test_upper1(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper1(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()