import re

phoneString = 'my phone number is 901-154-7709 and another number is 982-394-7709'
reObj1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print('type(reObj1)=',type(reObj1))

findAll = reObj1.findall(phoneString)
print('type(findAll)=',type(findAll))
print('findAll=',findAll)

searchResult = reObj1.search(phoneString)