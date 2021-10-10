str1 = 'my name is {} and my number is {}'
name='NC'
num = 100

print(str1.format(name,num))

str2 = 'my name is {n} and my number is {nu} and old number is {nu}'
name='NC'
num = 100

print(str2.format(n=name, nu=num))