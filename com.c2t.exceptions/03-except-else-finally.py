a = 10
b = 20
var = 0


try:
    var = b/a
except ZeroDivisionError as e:
    print('Exception Block!!!')
    print(e)
    print(type(e))
else:
    print('Else Block!!!')
finally:
    print('I am finally block...')

print(var)
