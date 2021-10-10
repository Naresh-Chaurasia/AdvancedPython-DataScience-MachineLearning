dictionary1 = {'key1':'val1','key2':'val2'}

dictionary2 = {'key1':'val1','key2':'val2',10:'ten','list1':[10,20]}

dictionary3 = {'key1':'val1','key2':'val2',10:'ten','dict1':dictionary2}

print('dictionary1=',dictionary1)
print('dictionary1[key1]=',dictionary1['key1'])
#print('dictionary1[key5]=',dictionary1['key5'])
print('type(dictionary1)=',type(dictionary1))

print('dictionary2[10]=',dictionary2[10])
print('dictionary2[list1]=',dictionary2['list1'])
print('dictionary3[dict1]=',dictionary3['dict1'])
print(dictionary3)
