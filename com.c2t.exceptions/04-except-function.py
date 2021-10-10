def division(val):
    try:
        x = 10/val
    except ZeroDivisionError:
        print("Error occurred...")
    else:
        print('x in function=',x)

    print('x in function2=', x)


#print('x =',x)
division(10)