dict = {'name':'c2t','age':10, 5:100}

keys = dict.keys()
values = dict.values()
items = dict.items()

print('keys=',keys)
print('type(keys)=',type(keys))
print('values=',values)
print('type(values)=',type(values))
print('items=',items)
print('type(items)=',type(items))

print('list(keys)=',list(keys))

for key in dict.keys():
    print('key=',key)

for k,v in dict.items():
    print('k=',k,'v=',v)
	
for vv in dict.items():
    print(vv)