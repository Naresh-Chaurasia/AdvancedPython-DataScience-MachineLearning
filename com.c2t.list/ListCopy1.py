import copy

'''
https://docs.python.org/3/tutorial/datastructures.html
Accessing list element using index
'''

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits_copy = copy.copy(fruits)

fruits_copy[5]= 100

print('fruits=',fruits)
print('fruits_copy=',fruits_copy)