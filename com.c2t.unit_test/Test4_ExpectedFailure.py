import unittest

class TestStringMethods(unittest.TestCase):

    @unittest.expectedFailure
    def test_upper(self):
        print('test_upper')
        self.assertEqual(1, 0, "broken")

    def test_isupper(self):
        print('test_isupper')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()