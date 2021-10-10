my_tuple = (4, 2, 3, [9, 5])
my_tuple[3][0] = 90
print('Modified tuple = ',my_tuple)

print()
print('----------------Tuple concatenation---------------------')

# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)
