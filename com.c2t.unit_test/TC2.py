import unittest

class TestStringMethods2(unittest.TestCase):

    def test_upper2(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper2(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()