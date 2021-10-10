'''
https://docs.python.org/3/tutorial/datastructures.html

Changing Values in a List with Indexes
List Concatenation and List Replication
Removing Values from Lists with del Statements

'''

fruits = ['orange', 'apple', 'pear', 'banana',10,20,30,40,50,60]
furnitures = ['table','chair']

print('fruits=',fruits)
fruits[1] = 'modified value'

print('fruits=',fruits)

print('fruits[-2]=',fruits[-2])
fruits[-2] = 'second last value modified'
print('fruits=',fruits)
