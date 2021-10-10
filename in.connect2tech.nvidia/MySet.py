'''
set1 = {10,20}
print(type(set1))

e = set([10,20])
print(e)
'''

mySet = set("this is fun way to create a list".split())
print(mySet)

setComprehension = {len(values) for values in mySet}
print(type(setComprehension))
print(setComprehension)