import unittest


#class TestAPI(testing.TestCase):

class TestAPI(unittest.TestCase):

 def test_first(self):
    self.assertTrue(1 == 1)

 def test_second(self):
    self.assertFalse(1 == 2)

if __name__ == '__main__':
    unittest.main()
