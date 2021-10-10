import re

phoneString = 'my phone number is 901-154-7709 and another number is 982-394-7709'
reObj1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
searchResult = reObj1.search(phoneString)
print('searchResult=',searchResult)
gp = searchResult.group()
print('gp=',gp)