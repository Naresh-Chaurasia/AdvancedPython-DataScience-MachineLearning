fruits = ['oorange', 'orange', 'pear', 'banana', ]


print(fruits)

#fruits.append('water melon')
#print(fruits)

#fruits.insert(1,'water melon')
#print(fruits)

fruits.sort(reverse=True)
print(fruits)

fruits.sort(key=str.lower)

print('fruits=',fruits)