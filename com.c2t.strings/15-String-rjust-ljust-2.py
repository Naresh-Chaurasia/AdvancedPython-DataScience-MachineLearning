str = 'Python Scripting'

print('len(str)     =    ',len(str))

r_just = str.rjust(20)
print(r_just)
r_just2 = str.rjust(20,'*')
print(r_just2)

l_just = str.ljust(20)
print(l_just)
l_just2 = str.ljust(20,'*')
print(l_just2)

c_str = str.center(20)
print(c_str)
c_str2 = str.center(20,'*')
print(c_str2)
