'''
https://docs.python.org/3/tutorial/datastructures.html
List methods
'''

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

index = fruits.index('apple')
print(index)

count = fruits.count('apple')
print(count)

index2 = fruits.index('apple', 2)
print(index2)

# fruits.sort()
print(fruits)

print(fruits.pop())
