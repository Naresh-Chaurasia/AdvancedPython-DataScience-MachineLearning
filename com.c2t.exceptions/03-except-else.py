try:
    var = 10/0
except ZeroDivisionError as e:
    print(e)
    print(type(e))
else:
    print('I am in else block...')
finally:
    print('i am in finally')

print(var)
