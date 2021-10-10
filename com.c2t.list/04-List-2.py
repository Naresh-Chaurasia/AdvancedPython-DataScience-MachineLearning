'''
https://docs.python.org/3/tutorial/datastructures.html

Changing Values in a List with Indexes
List Concatenation and List Replication
Removing Values from Lists with del Statements

'''

fruits = ['orange', 'apple', 'pear', 'banana']
print(fruits)
print('id(fruits)1=',id(fruits))

fruits[0]= 'modified orange'

print(fruits)
print('id(fruits)2=',id(fruits))
