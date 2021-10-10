myList = [10, 20, 30, 40, 50]

sum = 0

for i in myList:
    print("value of i =", i)
    sum = sum + i
    if sum > 50:
        break

print("sum=", sum)