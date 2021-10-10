# importing "copy" for copy operations
import copy

# initializing list 1
li1 = [1, 2, 4]
li2 = copy.copy(li1)

print('li1=',id(li1))
print('li2=',id(li2))

li1[0] = 10

print('li1=',id(li1))
print('li2=',id(li2))

print('li1=',(li1))
print('li2=',(li2))