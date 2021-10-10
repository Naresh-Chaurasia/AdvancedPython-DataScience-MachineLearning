def defaultValues(val=10):
    print('val=',val)

#Pass by reference
def displayList(list1):
    list1.append(30)
    print ('list1=',list1)
    print ('id(list1)=',id(list1))

'''
list2 = [10,20]
displayList(list2)
print ('list2=',list2)
print ('id(list2)=',id(list2))
'''

defaultValues();
defaultValues(100);