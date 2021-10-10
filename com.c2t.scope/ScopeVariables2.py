def f1():
    global var1
    var1 = 10
    print('var1=',var1)
    print('var3=', var3)

def f2():
    var2 = 10
    print('var2=',var2)
    #print('var1=', var1)
    print('var3=', var3)

var3 = 100
var1 = 200

f1()
#f2()

#print('var3=', var3)
#print('var1=', var1)
#print('var2=', var2)
