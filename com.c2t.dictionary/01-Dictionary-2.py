dictionary1 = {'key1':'val1','key2':'val2'}

dictionary2 = {'key1':'val1','key2':'val2',10:'ten','list1':[10,20]}

dictionary3 = {'key1':'val1','key2':'val2',10:'ten','dict1':dictionary2}

print(dictionary3['dict1'])
