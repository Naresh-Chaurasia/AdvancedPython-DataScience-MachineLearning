try:

    a = [10, 20, 30]
    print(a[5])

    with open('pi_digits1.txt') as f:
        lines = f.read()
        print(lines)

except (FileNotFoundError,IndexError) as e:
    print(e)
    print(type(e))