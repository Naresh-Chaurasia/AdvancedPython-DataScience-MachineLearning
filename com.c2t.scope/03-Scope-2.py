def f1():

    global b

    b = 200
    b = b + 100
    print('Inside f() b= : ', b)


b = 20
f1()
print('b=',b)