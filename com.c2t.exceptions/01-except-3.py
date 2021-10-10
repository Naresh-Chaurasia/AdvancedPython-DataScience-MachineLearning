#var = 0

arr = [10,20]
divisor = 0

try:
    var = 10/divisor

    print(arr[5])


except ZeroDivisionError as e:
    print('Exception has been handled...',e)
    print('type(e) = ',type(e))
except Exception as e2:
    print('Exception has been handled...',e2)
    print('type(e) = ',type(e2))

