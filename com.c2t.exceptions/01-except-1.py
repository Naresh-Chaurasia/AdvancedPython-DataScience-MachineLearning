a = 0
b = 20
var = 0

'''
try:
    var = b/a
except:
    print('Exception has been handled...')
else:
    print('No error')

print('value of var = ',var)

'''

#------------------------------------------------------------

var = 0

try:
    var = 10/10
except ZeroDivisionError as e:
    print('Exception has occured')
    print(e)
    print(type(e))
else:
    print('var in else= ', var)

print('var = ',var)
