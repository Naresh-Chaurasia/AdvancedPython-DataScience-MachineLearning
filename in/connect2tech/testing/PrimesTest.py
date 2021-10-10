'''
Created on 17-Apr-2018

@author: naresh
'''
import unittest
import foo.Primes

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(foo.Primes.is_prime(5))

if __name__ == '__main__':
    unittest.main()

