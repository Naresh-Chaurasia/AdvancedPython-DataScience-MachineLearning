import unittest

from TC1 import TestStringMethods1
from TC2 import TestStringMethods2

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods2)

smoke = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smoke)