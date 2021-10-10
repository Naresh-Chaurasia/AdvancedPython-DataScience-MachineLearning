import re

# compile() creates regular expression character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.
#p = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
p = re.compile(r'\d{3}-\d\d\d-\d\d\d\d')

print(p.findall("my phone number is 90-1154-7709 and another number is 982-394-7709"))