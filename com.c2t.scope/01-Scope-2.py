def function1():
    a = 10
    print('a=',a)
    print('1/a_global=',a_global)

def function2():
    b = 20
    print('b=',b)
    #print('a=', a)
    print('2/a_global=', a_global)

a_global = 100

function1()
function2()