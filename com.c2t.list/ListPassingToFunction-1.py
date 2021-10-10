def f1(l):
    print('add1=',id(l))
    l.pop()


l1 = [10,20]
print('add2=',id(l1))
print(l1)
f1(l1)
print(l1)