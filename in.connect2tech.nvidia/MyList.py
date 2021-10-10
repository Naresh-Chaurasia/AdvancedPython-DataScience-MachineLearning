'''
fruits = ['orange', 'apple', 'pear', 'banana']
fruits.append('This is Good')
'''

'''
print('----------')
print(fruits)
print('----------')

if 'pear' in fruits:
    print('WOW')
else:
    print('NOT WOW')

for val in fruits:
    print(val)

for i in range(7):
    print(i)
'''


'''
fruits = ['orange', 'apple', 'pear', 'banana']
copyOfFruits = fruits[:]

print('id(fruits)=',id(fruits))
print('id(copyOfFruits)=',id(copyOfFruits))

copyOfFruit2 = fruits.copy()
print('id(copyOfFruit2)=',id(copyOfFruit2))

copyOfFruit3 = list(fruits)
print('id(copyOfFruit3)=',id(copyOfFruit3))
'''

'''
# Shallow Copy
fruits = [['orange', 'apple'], ['pear', 'banana']]
copyOfFruits = fruits[:]

print('id(fruits)=',id(fruits))
print('id(copyOfFruits)=',id(copyOfFruits))

print('fruits=',fruits)
print('copyOfFruits=',copyOfFruits)

fruits[0].append('mango')

print('--------------------')
print('fruits=',fruits)
print('copyOfFruits=',copyOfFruits)
'''

'''
# Deleting

fruits = ['orange', 'apple', 'pear', 'banana']

print('--------------------')
print(id(fruits))

del fruits[0]

print(id(fruits))

'''

'''
# Sorting

fruits = ['orange', 'apple', 'pear', 'banana']
print('--------------------')
print(fruits)
fruits.sort(key=len)
print(fruits)
'''

print('--------------------')
myList = 'I really like this style of creating list'.split()
print(myList)

# Comprehension
print('--------------------')
l = [len(word) for word in myList]
print(l)
print(type(l))
