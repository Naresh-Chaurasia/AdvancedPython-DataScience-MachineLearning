
# Create a list by accepting input from user.
cats = []

while True:
    print('Enter the name of cat, press Enter to stop!!!')
    cat = input()

    if(cat == ''):
        break

    cats = cats + [cat]

print('for loop using in ===================>')
for c in cats:
    print(c)

print('for loop using range ===================>')
for x in range(len(cats)):
    print(cats[x])

