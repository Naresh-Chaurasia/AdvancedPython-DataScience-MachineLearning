import re

str = 'Ishan and Naresh are friends'
reObj1 = re.compile(r'Ishan|Naresh')
print('type(reObj1)=',type(reObj1))

searchResult = reObj1.search(str)
print('searchResult=',searchResult)
print('searchResult.group()=',searchResult.group())
print('searchResult.group(0)=',searchResult.group(0))
