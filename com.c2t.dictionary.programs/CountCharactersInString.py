import pprint

var = 'I am going to count characters in this string'
dict = {}

for char in var:
    print(char)
    dict.setdefault(char, 0)
    dict[char] = dict[char] + 1

print(dict)
pprint.pprint(dict)