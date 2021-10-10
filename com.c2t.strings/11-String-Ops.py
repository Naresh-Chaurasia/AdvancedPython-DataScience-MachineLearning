print('welcome to python')

#Concatenation of Two or More Strings

str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)

# Writing two string literals together also concatenates them like + operator.
print('Writing two string literals together also concatenates them like + operator. = ','hello''world')

# Iterating Through String

count = 0
for val in 'Python Training':
    print('char at ',count, ' is ', val)
    count+=1