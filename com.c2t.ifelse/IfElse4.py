age = 20

bool1 = True
bool2 = False

condition = age >= 18
print('condition=',condition)

condition2 = age > 21
print('condition2=',condition2)

if condition:
    print('you can vote')
elif condition2:
    print('You can driver..')
else:
    print('none of criteria met...')