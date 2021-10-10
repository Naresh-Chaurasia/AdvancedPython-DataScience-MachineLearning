# Output: range(0, 10)
print('range(10)=',range(10))


for i in range(10):
	if i == 5:
		continue;
	else:
		print('i=', i)

print('-----------------------------------')

for j in range(10):
	if j == 5:
		break;
	else:
		print('j=', j)

