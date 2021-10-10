def modifyList(list1):
    print('list1=',list1)
    list1.pop()
    print('list1=', list1)
    print('address of list1=',hex(id(list1)))
    print('address of list1=', id(list1))
    print('address of list1=', type(id(list1)))
    print('address of list1=', type(hex(id(list1))))

'''
l = [10,20,30,40,50]
print('address of l=',hex(id(l)))
print('value of l before function call..',l)
modifyList(l)
print('value of l after function call..',l)
'''


l = [10,20,30,40,50]
print('address of l=',hex(id(l)))
print('value of l before function call..',l)
modifyList(l[:])
print('value of l after function call..',l)


