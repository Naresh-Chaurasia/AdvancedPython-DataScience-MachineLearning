'''
Created on 20-Apr-2018

@author: naresh
'''
import File1

print('help(my_module)=',help(File1))

print('-------------------------------------------')

attrs_functions = dir(File1)
print('dir(my_module)=', attrs_functions)

for attr in attrs_functions:
    print('attr=',attr)

print('--------------------------------------------')

print(__name__)
print(__package__)
print(__file__)


