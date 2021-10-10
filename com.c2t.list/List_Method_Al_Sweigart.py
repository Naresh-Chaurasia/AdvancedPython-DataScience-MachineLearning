

list = ['a','b','c','a']
print("list.index('a') = ",list.index('a'))
#print("list.index('x') = ",list.index('x'))

list.append('x')
print("Value of list after appending 'x' = ",list)

list.insert(1,'y')
print("Value of list inserting 'y' = ",list)

animals = ['cat','dog','tiger']
print('Original animals list ===================> ',animals)

animals.remove('cat')
print("Animals list after animals.remove('cat') ===================> ",animals)
del animals[0]
print("Animals list after del animals[0] ===================> ",animals)

animals_list = ['Zebra','cat','dog','tiger']
print('unsorted animals_list ===================>',animals_list)

animals_list.sort()
print('sorted animals_list.sort() ===================>',animals_list)

animals_list.sort(reverse=True)
print('sorted animals_list.sort(reverse=True) ===================>',animals_list)

animals_list.sort(key=str.lower)
print('sorted animals_list.sort(key=str.lower) ===================>',animals_list)

#string_number = ['cat','dog','tiger',10]
#print(string_number.sort())

