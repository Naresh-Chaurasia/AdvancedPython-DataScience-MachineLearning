# Automate boring stuff - Al Sweigart

# Creating list

list1 = [1, 2, 3]
print('list1 = ',list1)

list2 = ['cat', 'bat', 'rat', 'elephant']
print('list2 = ',list2)

list3 = ['hello', 3.1415, True, None, 42]
print('list3 = ',list3)

# Python will give you an IndexError error message if you use an index that exceeds the number of values in your list value.
# print(list3[10])
print('list3[-1] = ', list3[-1])
# print('list3[-6] = ', list3[-6])

# Indexes can be only integer values, not floats. The following example will cause a TypeError error:
# print(list3[1.5])

#Lists can also contain other list values. The values in these lists of lists can be accessed using multiple indexes
print('--------------------------------------------------------')
spam1 = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print('spam1 = ', spam1)
print('spam1[0] = ',spam1[0])
print('spam1[1] = ', spam1[1])
print('spam1[0][1] = ', spam1[0][1])

#Negative Indexes
print("spam1[-1] = ", spam1[-1])

#Slicing
spam2 = ['cat', 'bat', 'rat', 'elephant']
print('spam2[0:4] = ',spam2[0:4])
print('spam2[0:5] = ',spam2[0:5])
print('spam2[0:50] = ',spam2[0:50])
print('spam2[0:-1] = ',spam2[0:-1])
print('spam2[0:-2] = ',spam2[0:-2])
print('spam2[0:-3] = ',spam2[0:-3])
print('spam2[0:-4] = ',spam2[0:-4])

print('spam2[:2] = ',spam2[:2])
print('spam2[:-1] = ',spam2[:-1])
print('spam2[1:] = ',spam2[1:])
print('spam2[:20] = ',spam2[:20])
print('spam2[20:20] = ',spam2[20:20])
print('spam2[:] = ',spam2[:])

# List length
print('len(spam2) = ',len(spam2))

# Changing Values in a List with Indexes
spam3 = ['cat', 'bat', 'rat', 'elephant']
print('original spam3 = ', spam3)
spam3[2] = 'rat modified'
print('modified spam3 = ', spam3)

# List Concatenation and List Replication
print('Adding [1, 2, 3] + [\'A\', \'B\', \'C\']  = ' , [1, 2, 3] + ['A', 'B', 'C'])
print('Replicating [1, 2, 3] * 3 ===================> ' , [1, 2, 3] * 3)

#Removing Values from Lists with del Statements
del_from_list = ['cat', 'bat', 'rat', 'elephant']
print('del_from_list before delete ===================>',del_from_list)
print('deleting ', del_from_list[2], ' from ',del_from_list)
del(del_from_list[2])
print('del_from_list after delete ===================>',del_from_list)