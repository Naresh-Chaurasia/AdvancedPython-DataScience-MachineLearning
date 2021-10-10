import copy

'''
https://docs.python.org/3/tutorial/datastructures.html
Accessing list element using index
'''

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana',[1,2,3]]

fruits_copy = copy.deepcopy(fruits)

fruits_copy[7][0] = 100

print(fruits)
print(fruits_copy)