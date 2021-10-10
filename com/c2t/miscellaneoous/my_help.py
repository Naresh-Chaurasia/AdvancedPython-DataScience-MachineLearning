'''
Created on 20-Apr-2018

@author: naresh
'''
from com.c2t.miscellaneoous import my_module

print('help(my_module)=',help(my_module))

attrs_functions = dir(my_module)
print('dir(my_module)=', attrs_functions)

for val in attrs_functions:
    print('val=',val)
    

