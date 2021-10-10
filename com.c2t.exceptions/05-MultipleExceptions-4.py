arr = [10,20]
divisor = 10

try:
    var = 10/divisor
    print(arr[5])
except (Exception, ZeroDivisionError, IndexError) as e:
    print('Exception has been handled...',e)
    print('type(e) = ',type(e))
