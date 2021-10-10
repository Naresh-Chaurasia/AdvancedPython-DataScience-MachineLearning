'''
Created on 26-Apr-2018

@author: naresh
'''

import unittest

class LetsAssert(unittest.TestCase):
    val = ''
    self1 = ''
    self2 = ''
    def test_assert1(self):
        __class__.self1 = self
        print('type(self)=',type(self))
        self.val = 'value1'
        self.assertEqual(self.val.upper(), 'VALUE1', 'The values are equal')

    def test_assert2(self):
        __class__.self2 = self
        self.assertEqual(__class__.self1,__class__.self2) 
        
        
if __name__ == '__main__':
    unittest.main()