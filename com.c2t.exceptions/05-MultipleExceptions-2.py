arr = [10,20]
divisor = 0

try:
    var = 10/divisor
    print(arr[5])

except ZeroDivisionError as e:
    print('Exception has been handled2...',e)
    print('type(e) = ',type(e))
except Exception as ee:
    print('Exception has been handled1...', ee)
    print('type(ee) = ', type(ee))
except IndexError as i:
    print('Exception has been handled3...', i)
    print('type(i) = ', type(i))
except IndexError as ii:
    print('Exception has been handled4...', ii)
    print('type(ii) = ', type(ii))



