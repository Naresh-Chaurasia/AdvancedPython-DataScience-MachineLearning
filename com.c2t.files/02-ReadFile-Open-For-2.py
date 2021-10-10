with open('pi_digits.txt') as f2:
    for f in f2:
        print(f)

print('----------------------')

with open('pi_digits.txt') as f3:
    for f in f3:
        print(f.rstrip())