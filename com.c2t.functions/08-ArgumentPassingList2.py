def modifyList(list1):
    print('Add2 in function = ',hex(id(list1)))
    list1.pop()


print('--------------Same Address---------------------')
l = [10,20,30]
print('Add1=',hex(id(l)))
print('l=',l)
modifyList(l)
print('Add3=',hex(id(l)))
print('l=',l)

print('---------------Different Address--------------------')
l2 = [100,200,300]
print('Add1=',hex(id(l2)))
print('l2=',l2)
modifyList(l2[:])
print('Add3=',hex(id(l2)))
print('l2=',l2)



