'''
Created on 20-Apr-2018

@author: naresh
'''
import File1

print('help(my_module)=',help(File1))

attrs_functions = dir(File1)
print('dir(my_module)=', attrs_functions)

for val in attrs_functions:
    print('val=',val)
    

