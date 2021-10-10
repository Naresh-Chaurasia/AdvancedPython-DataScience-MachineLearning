def add(a, b):
   """This program adds two
   numbers and return the result"""
   print('module')
   result = a + b
   return result


def add2(a, b):
   """This program adds two
   numbers and return the result"""

   result = a + b
   return result

print('Testing code using debugging in pycharm..')

import pdb
pdb.set_trace()

add(10,20)
add2(20,40)
