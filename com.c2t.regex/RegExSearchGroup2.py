import re

phoneString = 'my phone number is 901-154-7709 and another number is 982-394-7709'
reObj1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print('type(reObj1)=',type(reObj1))

searchResult = reObj1.search(phoneString)
print('searchResult=',searchResult)
print('searchResult.group()=',searchResult.group())
print('searchResult.group(0)=',searchResult.group(0))
print('searchResult.group(1)=',searchResult.group(1))
print('searchResult.group(2)=',searchResult.group(2))
v1,v2 = searchResult.groups()
print('searchResult.groups()=',searchResult.groups())
print('v1=',v1)
print('v2=',v2)